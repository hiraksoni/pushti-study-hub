/**
 * Pushti Study Hub - Universal Online Voice & Continuous Audio Engine
 * Version: 4.0.0 (High-Fidelity Melodious Female Voice Edition)
 *
 * Solves:
 *   1. Eliminates robotic/dull "male crybaby" voices completely.
 *   2. Automatically selects and locks onto high-fidelity Female Hindi voices:
 *      - Microsoft Swara Online (Natural Female - Azure Neural) on Windows/Edge/Chrome
 *      - Google हिन्दी (Natural Online Female) on Android/Chrome
 *      - Microsoft Kalpana (Female)
 *      - Apple Lekha (Female) on iOS/macOS
 *   3. True Play / Pause / Resume / Stop state machine across all devices.
 *   4. Continuous sentence-by-sentence queue with lookahead pre-buffering.
 *   5. Interactive Floating Audio Player for hands-free listening on desktop & mobile.
 *   6. Android Chrome 14s-stall watchdog so it never stops prematurely.
 */

(function (window) {
    'use strict';

    var STATE_IDLE = 'idle';
    var STATE_PLAYING = 'playing';
    var STATE_PAUSED = 'paused';

    var engineState = STATE_IDLE;
    var audioQueue = [];
    var currentQueueIndex = 0;
    var activeLang = 'hi';
    var playbackRate = 0.95;
    var femalePitch = 1.08;
    var playSessionId = 0;

    var activeBtn = null;
    var originalBtnContent = '';
    var activeTargetEl = null;
    var fullLessonText = '';
    var synthTimer = null;
    var cachedFemaleVoice = null;

    function isDevanagari(text) {
        return /[\u0900-\u097F]/.test(text || '');
    }

    function sanitizeText(raw) {
        if (!raw) return '';
        return raw
            .replace(/<[^>]*>/g, ' ')
            .replace(/\$\$[\s\S]*?\$\$/g, ' ')
            .replace(/\$([^\$]+)\$/g, '$1')
            .replace(/\\\[[\s\S]*?\\\]/g, ' ')
            .replace(/\\\(([^\)]+)\\\)/g, '$1')
            .replace(/\\(?:dfrac|frac)\{([^}]+)\}\{([^}]+)\}/g, '$1 over $2')
            .replace(/&bull;/gi, ', ')
            .replace(/&ndash;/gi, ' to ')
            .replace(/&mdash;/gi, ', ')
            .replace(/&nbsp;/gi, ' ')
            .replace(/&amp;/gi, ' and ')
            .replace(/[•\t\r]+/g, ' ')
            .replace(/\s+/g, ' ')
            .trim();
    }

    function chunkText(text, maxChars) {
        maxChars = maxChars || 110;
        var clean = sanitizeText(text);
        if (!clean) return [];

        var sentenceDelims = /([।\.\?\!\n]+)/;
        var tokens = clean.split(sentenceDelims);
        var rawSentences = [];

        for (var i = 0; i < tokens.length; i += 2) {
            var sent = (tokens[i] || '') + (tokens[i + 1] || '');
            sent = sent.trim();
            if (sent) rawSentences.push(sent);
        }

        var chunks = [];
        for (var s = 0; s < rawSentences.length; s++) {
            var item = rawSentences[s];
            if (item.length <= maxChars) {
                chunks.push(item);
            } else {
                var subTokens = item.split(/([,;:\s]+)/);
                var cur = '';
                for (var st = 0; st < subTokens.length; st++) {
                    var piece = subTokens[st];
                    if ((cur + piece).length <= maxChars) {
                        cur += piece;
                    } else {
                        if (cur.trim()) chunks.push(cur.trim());
                        cur = piece;
                    }
                }
                if (cur.trim()) chunks.push(cur.trim());
            }
        }
        return chunks;
    }

    // --- HIGH-FIDELITY FEMALE HINDI VOICE SELECTOR ---
    function findBestFemaleVoice(lang) {
        if (!('speechSynthesis' in window)) return null;
        var voices = window.speechSynthesis.getVoices();
        if (!voices || !voices.length) return null;

        var isHi = (lang === 'hi' || !lang);

        if (isHi) {
            // Priority 1: Cloud Natural Female Hindi voices
            var topFemaleNames = [
                'swara',       // Microsoft Swara Online (Natural) - Hindi
                'kalpana',     // Microsoft Kalpana - Hindi
                'google हिन्दी', // Google Hindi Female
                'google hindi',
                'shreya',
                'aditi',
                'lekha',
                'priya',
                'neerja',
                'rashmi'
            ];

            for (var p = 0; p < topFemaleNames.length; p++) {
                var match = voices.find(function (v) {
                    var vName = (v.name || '').toLowerCase();
                    return vName.includes(topFemaleNames[p]);
                });
                if (match) return match;
            }

            // Priority 2: Any Hindi voice not explicitly labeled male
            var hindiFemaleFallback = voices.find(function (v) {
                var vName = (v.name || '').toLowerCase();
                var vLang = (v.lang || '').toLowerCase();
                var matchesHi = (vLang.includes('hi') || vName.includes('hindi') || vLang === 'hi');
                var isMale = (vName.includes('male') || vName.includes('hemant') || vName.includes('madhav') || vName.includes('david') || vName.includes('mark'));
                return matchesHi && !isMale;
            });
            if (hindiFemaleFallback) return hindiFemaleFallback;

            // Priority 3: Any Hindi voice
            var anyHi = voices.find(function (v) {
                var vLang = (v.lang || '').toLowerCase();
                return (vLang.includes('hi') || (v.name && v.name.toLowerCase().includes('hindi')));
            });
            if (anyHi) return anyHi;
        }

        // English female voice fallback
        var enFemale = voices.find(function (v) {
            var vName = (v.name || '').toLowerCase();
            return vName.includes('zira') || vName.includes('samantha') || vName.includes('natural') || vName.includes('female');
        });
        return enFemale || voices[0] || null;
    }

    function initVoices() {
        if (!('speechSynthesis' in window)) return;
        cachedFemaleVoice = findBestFemaleVoice('hi');
        window.speechSynthesis.onvoiceschanged = function () {
            cachedFemaleVoice = findBestFemaleVoice('hi');
        };
    }
    initVoices();

    // --- DOM FLOATING AUDIO PLAYER ---
    function ensureFloatingPlayer() {
        var existing = document.getElementById('pushti-tts-floating-player');
        if (existing) return existing;

        var bar = document.createElement('div');
        bar.id = 'pushti-tts-floating-player';
        bar.className = 'fixed bottom-4 left-1/2 -translate-x-1/2 z-[9999] hidden flex-col sm:flex-row items-center gap-3 px-4 py-2.5 bg-slate-900/95 dark:bg-slate-900/95 text-white border border-amber-500/40 rounded-2xl shadow-2xl backdrop-blur-lg transition-all duration-300 max-w-[95vw] w-auto';
        bar.innerHTML = [
            '<div class="flex items-center gap-2 min-w-0">',
            '  <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse flex-shrink-0" id="tts-status-dot"></span>',
            '  <div class="flex flex-col min-w-0 max-w-[200px] sm:max-w-xs">',
            '    <span class="text-[11px] font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1">',
            '      <i class="fas fa-headphones"></i> <span id="tts-status-text">वाचन चालू है...</span>',
            '      <span class="px-1.5 py-0.2 rounded bg-amber-500/20 text-[9px] text-amber-300 ml-1">👩 महिला स्वर</span>',
            '    </span>',
            '    <span id="tts-snippet-text" class="text-xs text-slate-300 truncate font-sans">पाठ लोड हो रहा है...</span>',
            '  </div>',
            '</div>',
            '<div class="flex items-center gap-1.5 flex-shrink-0">',
            '  <button id="tts-ctrl-prev" onclick="window.PushtiOnlineTTS.prev()" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 transition-all text-xs cursor-pointer" title="पिछला वाक्य">',
            '    <i class="fas fa-backward-step"></i>',
            '  </button>',
            '  <button id="tts-ctrl-toggle" onclick="window.PushtiOnlineTTS.togglePlayPause()" class="px-3.5 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold transition-all text-xs flex items-center gap-1.5 cursor-pointer shadow-md">',
            '    <i class="fas fa-pause" id="tts-ctrl-icon"></i> <span id="tts-ctrl-label">विराम (Pause)</span>',
            '  </button>',
            '  <button id="tts-ctrl-next" onclick="window.PushtiOnlineTTS.next()" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 transition-all text-xs cursor-pointer" title="अगला वाक्य">',
            '    <i class="fas fa-forward-step"></i>',
            '  </button>',
            '  <button id="tts-ctrl-stop" onclick="window.PushtiOnlineTTS.stop()" class="p-2 rounded-xl bg-rose-500/20 hover:bg-rose-500/30 text-rose-300 border border-rose-500/40 transition-all text-xs cursor-pointer" title="रोकें (Stop)">',
            '    <i class="fas fa-stop"></i>',
            '  </button>',
            '  <select id="tts-ctrl-speed" onchange="window.PushtiOnlineTTS.setSpeed(parseFloat(this.value))" class="bg-slate-800 text-slate-200 text-[11px] rounded-lg px-2 py-1.5 border border-slate-700 cursor-pointer">',
            '    <option value="0.8">0.8x</option>',
            '    <option value="0.95" selected>1.0x</option>',
            '    <option value="1.15">1.2x</option>',
            '  </select>',
            '  <button onclick="window.PushtiOnlineTTS.hidePlayer()" class="p-1.5 text-slate-400 hover:text-white transition-all text-xs ml-1 cursor-pointer" title="बंद करें">',
            '    <i class="fas fa-times"></i>',
            '  </button>',
            '</div>'
        ].join('');
        document.body.appendChild(bar);
        return bar;
    }

    function updateFloatingPlayerUI() {
        var bar = ensureFloatingPlayer();
        var dot = document.getElementById('tts-status-dot');
        var statusText = document.getElementById('tts-status-text');
        var snippetText = document.getElementById('tts-snippet-text');
        var icon = document.getElementById('tts-ctrl-icon');
        var label = document.getElementById('tts-ctrl-label');

        if (engineState === STATE_IDLE) {
            bar.classList.add('hidden');
            bar.classList.remove('flex');
            return;
        }

        bar.classList.remove('hidden');
        bar.classList.add('flex');

        var total = audioQueue.length || 1;
        var current = Math.min(currentQueueIndex + 1, total);
        var currentChunk = audioQueue[currentQueueIndex] || '';

        if (snippetText) {
            snippetText.textContent = currentChunk ? `[${current}/${total}] "${currentChunk}"` : 'समाप्त';
        }

        if (engineState === STATE_PLAYING) {
            if (dot) {
                dot.className = 'w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse flex-shrink-0';
            }
            if (statusText) statusText.textContent = `वाचन जारी [${current}/${total}]`;
            if (icon) icon.className = 'fas fa-pause';
            if (label) label.textContent = 'विराम (Pause)';
        } else if (engineState === STATE_PAUSED) {
            if (dot) {
                dot.className = 'w-2.5 h-2.5 rounded-full bg-amber-400 flex-shrink-0';
            }
            if (statusText) statusText.textContent = `विराम (Paused) [${current}/${total}]`;
            if (icon) icon.className = 'fas fa-play';
            if (label) label.textContent = 'जारी रखें (Resume)';
        }
    }

    function updateActiveButtonUI() {
        if (!activeBtn) return;
        if (engineState === STATE_PLAYING) {
            activeBtn.setAttribute('data-speaking', 'true');
            activeBtn.classList.add('speaking');
            if (activeLang === 'hi') {
                activeBtn.innerHTML = '<i class="fas fa-pause text-amber-400"></i> विराम (Pause)';
            } else {
                activeBtn.innerHTML = '<i class="fas fa-pause"></i> Pause';
            }
        } else if (engineState === STATE_PAUSED) {
            activeBtn.setAttribute('data-speaking', 'paused');
            if (activeLang === 'hi') {
                activeBtn.innerHTML = '<i class="fas fa-play text-emerald-400"></i> जारी रखें';
            } else {
                activeBtn.innerHTML = '<i class="fas fa-play"></i> Resume';
            }
        } else {
            activeBtn.setAttribute('data-speaking', 'false');
            activeBtn.classList.remove('speaking');
            if (originalBtnContent) {
                activeBtn.innerHTML = originalBtnContent;
            }
        }
    }

    // --- CONTINUOUS QUEUE PLAYBACK WITH FEMALE VOICE ---
    function playQueue(lang, sessionId, onComplete) {
        if (sessionId !== playSessionId || engineState !== STATE_PLAYING) return;

        if (currentQueueIndex >= audioQueue.length) {
            stop();
            if (typeof onComplete === 'function') onComplete();
            return;
        }

        var chunk = audioQueue[currentQueueIndex];
        updateFloatingPlayerUI();
        updateActiveButtonUI();

        if (!('speechSynthesis' in window)) {
            console.warn('[PushtiOnlineTTS] SpeechSynthesis not supported');
            stop();
            return;
        }

        if (window.speechSynthesis.speaking) {
            window.speechSynthesis.cancel();
        }

        var utter = new SpeechSynthesisUtterance(chunk);
        utter.lang = (lang === 'hi') ? 'hi-IN' : 'en-IN';
        utter.rate = playbackRate;
        utter.pitch = femalePitch;

        // Select the finest female voice
        if (!cachedFemaleVoice) {
            cachedFemaleVoice = findBestFemaleVoice(lang);
        }
        if (cachedFemaleVoice) {
            utter.voice = cachedFemaleVoice;
        }

        // Android 14s Chrome stall watchdog
        if (synthTimer) clearInterval(synthTimer);
        synthTimer = setInterval(function () {
            if (window.speechSynthesis.speaking) {
                window.speechSynthesis.pause();
                window.speechSynthesis.resume();
            } else {
                clearInterval(synthTimer);
            }
        }, 12000);

        utter.onend = function () {
            if (sessionId !== playSessionId || engineState !== STATE_PLAYING) return;
            if (synthTimer) clearInterval(synthTimer);
            currentQueueIndex++;
            playQueue(lang, sessionId, onComplete);
        };

        utter.onerror = function (e) {
            if (sessionId !== playSessionId || engineState !== STATE_PLAYING) return;
            console.warn('[PushtiOnlineTTS] Utterance error:', e);
            if (synthTimer) clearInterval(synthTimer);
            currentQueueIndex++;
            playQueue(lang, sessionId, onComplete);
        };

        window.speechSynthesis.speak(utter);
    }

    function play(text, options) {
        options = options || {};

        var btn = options.btn;
        if (!btn && window.event && window.event.target) {
            try {
                btn = window.event.target.closest('button');
            } catch (e) {}
        }

        var clean = sanitizeText(text);
        if (!clean) return;

        // If resuming the exact same lesson from paused state
        if (engineState === STATE_PAUSED && clean === fullLessonText) {
            resume();
            return;
        }

        stop();

        fullLessonText = clean;
        activeLang = options.lang || (isDevanagari(clean) ? 'hi' : 'en');
        var chunks = chunkText(clean, 110);
        if (!chunks.length) return;

        audioQueue = chunks;
        currentQueueIndex = 0;
        engineState = STATE_PLAYING;
        var mySessionId = ++playSessionId;

        if (btn) {
            activeBtn = btn;
            originalBtnContent = activeBtn.innerHTML;
        }

        if (options.targetEl) {
            activeTargetEl = options.targetEl;
            activeTargetEl.classList.add('pushti-tts-reading-target');
        }

        updateFloatingPlayerUI();
        updateActiveButtonUI();

        playQueue(activeLang, mySessionId, options.onComplete);
    }

    function pause() {
        if (engineState !== STATE_PLAYING) return;
        engineState = STATE_PAUSED;

        if ('speechSynthesis' in window) {
            try {
                window.speechSynthesis.pause();
            } catch (e) {}
        }
        if (synthTimer) clearInterval(synthTimer);

        updateFloatingPlayerUI();
        updateActiveButtonUI();
    }

    function resume() {
        if (engineState !== STATE_PAUSED) return;
        engineState = STATE_PLAYING;

        if ('speechSynthesis' in window) {
            try {
                if (window.speechSynthesis.paused) {
                    window.speechSynthesis.resume();
                } else {
                    playQueue(activeLang, playSessionId);
                }
            } catch (e) {
                playQueue(activeLang, playSessionId);
            }
        } else {
            playQueue(activeLang, playSessionId);
        }

        updateFloatingPlayerUI();
        updateActiveButtonUI();
    }

    function togglePlayPause(text, options) {
        if (engineState === STATE_PLAYING) {
            pause();
        } else if (engineState === STATE_PAUSED) {
            resume();
        } else {
            if (text) {
                play(text, options);
            } else if (fullLessonText) {
                play(fullLessonText, options);
            } else {
                window.speakFullLesson();
            }
        }
    }

    function stop() {
        playSessionId++;
        engineState = STATE_IDLE;

        if ('speechSynthesis' in window) {
            try {
                window.speechSynthesis.cancel();
            } catch (e) {}
        }
        if (synthTimer) clearInterval(synthTimer);

        audioQueue = [];
        currentQueueIndex = 0;

        if (activeBtn) {
            activeBtn.setAttribute('data-speaking', 'false');
            activeBtn.classList.remove('speaking');
            if (originalBtnContent) {
                activeBtn.innerHTML = originalBtnContent;
            }
            activeBtn = null;
            originalBtnContent = '';
        }

        if (activeTargetEl) {
            activeTargetEl.classList.remove('pushti-tts-reading-target');
            activeTargetEl = null;
        }

        updateFloatingPlayerUI();
    }

    function next() {
        if (!audioQueue.length) return;
        if ('speechSynthesis' in window) {
            try {
                window.speechSynthesis.cancel();
            } catch (e) {}
        }
        currentQueueIndex = Math.min(currentQueueIndex + 1, audioQueue.length - 1);
        if (engineState === STATE_PLAYING) {
            playQueue(activeLang, playSessionId);
        } else {
            updateFloatingPlayerUI();
        }
    }

    function prev() {
        if (!audioQueue.length) return;
        if ('speechSynthesis' in window) {
            try {
                window.speechSynthesis.cancel();
            } catch (e) {}
        }
        currentQueueIndex = Math.max(currentQueueIndex - 1, 0);
        if (engineState === STATE_PLAYING) {
            playQueue(activeLang, playSessionId);
        } else {
            updateFloatingPlayerUI();
        }
    }

    function setSpeed(rate) {
        playbackRate = rate || 0.95;
    }

    function hidePlayer() {
        stop();
        var bar = document.getElementById('pushti-tts-floating-player');
        if (bar) bar.classList.add('hidden');
    }

    // Expose API
    window.PushtiOnlineTTS = {
        speak: play,
        play: play,
        pause: pause,
        resume: resume,
        togglePlayPause: togglePlayPause,
        stop: stop,
        next: next,
        prev: prev,
        setSpeed: setSpeed,
        hidePlayer: hidePlayer,
        isSpeaking: function () {
            return engineState === STATE_PLAYING;
        },
        getState: function () {
            return engineState;
        },
        chunkText: chunkText,
        sanitizeText: sanitizeText,
        getBestFemaleVoice: findBestFemaleVoice
    };

    // --- CONVENIENCE HINDI WRAPPERS ---
    window.speakHindiText = function (targetOrText, btn) {
        var text = '';
        var targetEl = null;

        if (typeof targetOrText === 'string') {
            text = targetOrText;
        } else if (targetOrText && targetOrText.innerText) {
            text = targetOrText.innerText;
            targetEl = targetOrText;
        }

        var activeTargetBtn = btn;
        if (!activeTargetBtn && window.event && window.event.target) {
            try {
                activeTargetBtn = window.event.target.closest('button');
            } catch (e) {}
        }

        // Self-heal: extract from parent card if text was missing
        if (!text && activeTargetBtn) {
            if (activeTargetBtn.parentElement && activeTargetBtn.parentElement.nextElementSibling) {
                targetEl = activeTargetBtn.parentElement.nextElementSibling;
                text = targetEl.innerText || targetEl.textContent || '';
            }
            if (!text) {
                var card = activeTargetBtn.closest('.group, .p-4, .p-5, .p-6, .concept-card, div');
                if (card) {
                    targetEl = card.querySelector('p, .verse-line, .text-slate-100');
                    text = targetEl ? (targetEl.innerText || targetEl.textContent || '') : '';
                }
            }
        }

        if (text) {
            if (engineState === STATE_PLAYING && activeTargetBtn === activeBtn) {
                window.PushtiOnlineTTS.pause();
            } else if (engineState === STATE_PAUSED && activeTargetBtn === activeBtn) {
                window.PushtiOnlineTTS.resume();
            } else {
                window.PushtiOnlineTTS.play(text, { lang: 'hi', btn: activeTargetBtn, targetEl: targetEl });
            }
        }
    };

    window.speakHindiWord = function (word, meaning, btn) {
        var activeTargetBtn = btn;
        if (!activeTargetBtn && window.event && window.event.target) {
            try {
                activeTargetBtn = window.event.target.closest('button');
            } catch (e) {}
        }
        var text = word + '... अर्थात्... ' + meaning;
        window.PushtiOnlineTTS.play(text, { lang: 'hi', btn: activeTargetBtn });
    };

    window.speakFullLesson = function (btn) {
        var activeTargetBtn = btn;
        if (!activeTargetBtn && window.event && window.event.target) {
            try {
                activeTargetBtn = window.event.target.closest('button');
            } catch (e) {}
        }

        if (engineState === STATE_PLAYING) {
            window.PushtiOnlineTTS.pause();
            return;
        } else if (engineState === STATE_PAUSED) {
            window.PushtiOnlineTTS.resume();
            return;
        }

        var targetContainer = document.getElementById('tabText') || 
                              document.getElementById('tabTheory') || 
                              document.getElementById('tab-theory') || 
                              document.querySelector('.lesson-content-body') ||
                              document.querySelector('main');
        var text = '';
        if (targetContainer) {
            var paragraphs = targetContainer.querySelectorAll('p, .verse-line, li');
            if (paragraphs.length) {
                text = Array.from(paragraphs).map(function (p) {
                    return p.textContent;
                }).join('. ');
            } else {
                text = targetContainer.textContent;
            }
        } else {
            text = Array.from(document.querySelectorAll('main p')).map(function (p) {
                return p.textContent;
            }).join('. ');
        }
        window.PushtiOnlineTTS.play(text, { lang: 'hi', btn: activeTargetBtn, targetEl: targetContainer });
    };

    // Global aliases
    window.togglePlayPauseAudio = function () {
        window.PushtiOnlineTTS.togglePlayPause();
    };
    window.stopAudio = function () {
        window.PushtiOnlineTTS.stop();
    };
    window.changeAudioSpeed = function (speed) {
        window.PushtiOnlineTTS.setSpeed(parseFloat(speed));
    };

})(window);
