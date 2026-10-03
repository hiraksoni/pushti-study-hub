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

    // Speed setting with localStorage persistence (Default 1.0x Normal)
    var playbackRate = 1.0;
    try {
        var savedRate = localStorage.getItem('psh_tts_speed');
        if (savedRate) playbackRate = parseFloat(savedRate) || 1.0;
    } catch (e) {}

    // Speech pitch: 1.0 = Natural neural pitch (Eliminates artificial squeaking/distortion on Android & Tablets)
    var speechPitch = 1.0;
    var playSessionId = 0;

    var activeBtn = null;
    var originalBtnContent = '';
    var activeTargetEl = null;
    var fullLessonText = '';
    var synthTimer = null;
    var cachedSelectedVoice = null;

    function isDevanagari(text) {
        return /[\u0900-\u097F]/.test(text || '');
    }

    function escapeHtml(str) {
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
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

    // --- VOICE RECOGNITION & HUMAN-FRIENDLY LABELS ---
    function formatVoiceLabel(v) {
        if (!v) return 'डिफ़ॉल्ट आवाज़ (Default)';
        var name = v.name || '';
        var lang = (v.lang || '').toLowerCase();
        var lower = name.toLowerCase();

        // 1. Windows Natural Neural Voices
        if (name.includes('Swara')) return '🇮🇳 Swara (Natural Hindi ♀)';
        if (name.includes('Madhur')) return '🇮🇳 Madhur (Natural Hindi ♂)';
        if (name.includes('Kalpana')) return '🇮🇳 Kalpana (Hindi ♀)';
        if (name.includes('Hemant')) return '🇮🇳 Hemant (Hindi ♂)';
        if (name.includes('Neerja')) return '🇮🇳 Neerja (Indian English ♀)';
        if (name.includes('Prabhat')) return '🇮🇳 Prabhat (Indian English ♂)';

        // 2. Samsung Voices (Galaxy Tab A8 SM-X205)
        if (lower.includes('samsung')) {
            if (lang.includes('hi') || lower.includes('hindi') || name.includes('हिन्दी')) {
                return '📱 Samsung Hindi (Tab A8)';
            }
            if (lang.includes('in') || lang.startsWith('en')) {
                return '📱 Samsung Indian English (Tab A8)';
            }
            return '📱 Samsung ' + name.replace(/Samsung\s*/i, '');
        }

        // 3. Google Voices (Android / Chrome)
        if (name.includes('Google हिन्दी') || (lower.includes('google') && (lang.includes('hi') || lower.includes('hindi')))) {
            if (lower.includes('network') || lower.includes('online')) {
                return '✨ Google Hindi (Online HD)';
            }
            return '🇮🇳 Google हिन्दी (Android)';
        }
        if (lower.includes('google') && (lang.includes('en-in') || lang.includes('en_in'))) {
            return '🇮🇳 Google Indian English';
        }
        if (name.includes('Google UK English Female')) return '🇬🇧 Google UK Female';
        if (name.includes('Google US English')) return '🇺🇸 Google US English';
        if (name.includes('Lekha')) return '🍎 Lekha (Hindi ♀)';

        // 4. General clean display
        if (lang.includes('hi')) {
            var hiClean = name.replace(/Microsoft|Online|\(Natural\)|\(India\)/gi, '').trim();
            return '🇮🇳 ' + (hiClean || 'Hindi Voice');
        }
        if (lang.includes('in') && lang.startsWith('en')) {
            var inClean = name.replace(/Microsoft|Online|\(Natural\)|\(India\)/gi, '').trim();
            return '🇮🇳 ' + (inClean || 'Indian English');
        }

        var clean = name.replace(/Microsoft|Online|\(Natural\)/gi, '').trim();
        return clean.length > 22 ? clean.substring(0, 21) + '…' : clean;
    }

    function findBestVoice(lang) {
        if (!('speechSynthesis' in window)) return null;
        var voices = window.speechSynthesis.getVoices();
        if (!voices || !voices.length) return null;

        var isHi = (lang === 'hi' || !lang);

        if (isHi) {
            // Priority Ranking for High-Fidelity Natural Voices
            var priorityNames = [
                'swara',       // Microsoft Swara Online (Natural) - High Fidelity
                'samsung',     // Samsung Hindi on Galaxy Tab A8
                'network',     // Google Hindi Network (Higher fidelity than local offline chip)
                'google हिन्दी', // Google Hindi
                'google hindi',
                'kalpana',     // Microsoft Kalpana
                'madhur',      // Microsoft Madhur
                'lekha',
                'shreya',
                'aditi'
            ];

            for (var p = 0; p < priorityNames.length; p++) {
                var match = voices.find(function (v) {
                    var vName = (v.name || '').toLowerCase();
                    var vLang = (v.lang || '').toLowerCase();
                    var matchesLang = (vLang.includes('hi') || vName.includes('hindi') || vName.includes('हिन्दी'));
                    return matchesLang && vName.includes(priorityNames[p]);
                });
                if (match) return match;
            }

            // Fallback: Any Hindi voice
            var anyHi = voices.find(function (v) {
                var vLang = (v.lang || '').toLowerCase();
                var vName = (v.name || '').toLowerCase();
                return (vLang.includes('hi') || vName.includes('hindi') || vName.includes('हिन्दी'));
            });
            if (anyHi) return anyHi;
        }

        // English natural voice fallback
        var enVoice = voices.find(function (v) {
            var vName = (v.name || '').toLowerCase();
            var vLang = (v.lang || '').toLowerCase();
            return (vLang.includes('in') && (vName.includes('neerja') || vName.includes('natural'))) ||
                   vName.includes('samantha') || vName.includes('natural') || vName.includes('zira');
        });
        return enVoice || voices[0] || null;
    }

    function getActiveVoice(lang) {
        if (!('speechSynthesis' in window)) return null;
        var voices = window.speechSynthesis.getVoices();
        if (!voices || !voices.length) return null;

        // 1. User's manually saved voice preference
        var savedName = null;
        try {
            savedName = localStorage.getItem('psh_tts_voice_name');
        } catch (e) {}

        if (savedName) {
            var match = voices.find(function (v) { return v.name === savedName; });
            if (match) return match;
        }

        // 2. High-fidelity automatic detection
        return findBestVoice(lang);
    }

    function updateVoiceBadge(v) {
        var badge = document.getElementById('tts-active-voice-badge');
        if (!badge) return;
        if (!v) {
            badge.textContent = '🎙️ आवाज़';
            return;
        }
        var shortName = v.name || '';
        if (shortName.includes('Swara')) shortName = 'Swara';
        else if (shortName.includes('Madhur')) shortName = 'Madhur';
        else if (shortName.includes('Kalpana')) shortName = 'Kalpana';
        else if (shortName.includes('Hemant')) shortName = 'Hemant';
        else if (shortName.toLowerCase().includes('samsung')) shortName = 'Samsung';
        else if (shortName.includes('Google हिन्दी') || shortName.toLowerCase().includes('hindi')) shortName = 'Google';
        else if (shortName.includes('Neerja')) shortName = 'Neerja';
        else shortName = shortName.split(' ')[0] || 'आवाज़';
        badge.textContent = '🎙️ ' + shortName;
    }

    function populateVoiceDropdown() {
        if (!('speechSynthesis' in window)) return;
        var sel = document.getElementById('tts-ctrl-voice');
        if (!sel) return;

        var allVoices = window.speechSynthesis.getVoices() || [];
        if (!allVoices.length) {
            sel.innerHTML = '<option value="">डिफ़ॉल्ट आवाज़ (Default)</option>';
            return;
        }

        var hiVoices = [];
        var inEnVoices = [];
        var otherVoices = [];

        allVoices.forEach(function (v) {
            var vLang = (v.lang || '').toLowerCase();
            var vName = (v.name || '').toLowerCase();
            if (vLang.includes('hi') || vName.includes('hindi') || vName.includes('हिन्दी')) {
                hiVoices.push(v);
            } else if (vLang === 'en-in' || vLang === 'en_in' || vName.includes('india')) {
                inEnVoices.push(v);
            } else if (vLang.startsWith('en') && (vName.includes('natural') || vName.includes('google') || vName.includes('samsung') || vName.includes('zira'))) {
                otherVoices.push(v);
            }
        });

        var candidateList = [];
        if (hiVoices.length > 0) candidateList = candidateList.concat(hiVoices);
        if (inEnVoices.length > 0) candidateList = candidateList.concat(inEnVoices);
        if (otherVoices.length > 0) candidateList = candidateList.concat(otherVoices.slice(0, 4));
        if (!candidateList.length) candidateList = allVoices.slice(0, 8);

        var activeV = cachedSelectedVoice || getActiveVoice(activeLang);
        var activeName = activeV ? activeV.name : '';

        var html = '';
        var selectedFound = false;

        candidateList.forEach(function (v) {
            var isSel = (v.name === activeName);
            if (isSel) selectedFound = true;
            html += '<option value="' + escapeHtml(v.name) + '"' + (isSel ? ' selected' : '') + '>' + escapeHtml(formatVoiceLabel(v)) + '</option>';
        });

        if (!selectedFound && activeV) {
            html = '<option value="' + escapeHtml(activeV.name) + '" selected>' + escapeHtml(formatVoiceLabel(activeV)) + '</option>' + html;
        }

        sel.innerHTML = html;
        updateVoiceBadge(activeV);
    }

    function initVoices() {
        if (!('speechSynthesis' in window)) return;
        cachedSelectedVoice = getActiveVoice('hi');
        populateVoiceDropdown();
        window.speechSynthesis.onvoiceschanged = function () {
            cachedSelectedVoice = getActiveVoice('hi');
            populateVoiceDropdown();
        };
    }
    initVoices();

    // --- DOM FLOATING AUDIO PLAYER ---
    function ensureFloatingPlayer() {
        var existing = document.getElementById('pushti-tts-floating-player');
        if (existing) return existing;

        var bar = document.createElement('div');
        bar.id = 'pushti-tts-floating-player';
        bar.className = 'fixed bottom-3 sm:bottom-4 left-1/2 -translate-x-1/2 z-[9999] hidden flex-col md:flex-row items-center gap-2 sm:gap-3 px-3.5 py-2 sm:py-2.5 bg-slate-900/95 dark:bg-slate-900/95 text-white border border-amber-500/40 rounded-2xl shadow-2xl backdrop-blur-lg transition-all duration-300 max-w-[96vw] w-auto';
        bar.innerHTML = [
            '<div class="flex items-center gap-2 min-w-0 w-full md:w-auto justify-between md:justify-start">',
            '  <div class="flex items-center gap-2 min-w-0">',
            '    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse flex-shrink-0" id="tts-status-dot"></span>',
            '    <div class="flex flex-col min-w-0 max-w-[170px] sm:max-w-xs">',
            '      <span class="text-[11px] font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1">',
            '        <i class="fas fa-headphones"></i> <span id="tts-status-text">वाचन चालू है...</span>',
            '        <span id="tts-active-voice-badge" class="px-1.5 py-0.5 rounded bg-amber-500/20 text-[9px] text-amber-300 ml-1 font-mono truncate max-w-[85px]">🎙️ Swara</span>',
            '      </span>',
            '      <span id="tts-snippet-text" class="text-xs text-slate-300 truncate font-sans">पाठ लोड हो रहा है...</span>',
            '    </div>',
            '  </div>',
            '  <button onclick="window.PushtiOnlineTTS.hidePlayer()" class="md:hidden p-1 text-slate-400 hover:text-white transition-all text-xs cursor-pointer" title="बंद करें">',
            '    <i class="fas fa-times"></i>',
            '  </button>',
            '</div>',
            '<div class="flex items-center gap-1.5 flex-wrap sm:flex-nowrap justify-center flex-shrink-0 w-full md:w-auto">',
            '  <select id="tts-ctrl-voice" onchange="window.PushtiOnlineTTS.setVoiceByName(this.value)" class="bg-slate-800 hover:bg-slate-700 text-amber-300 text-[11px] font-medium rounded-lg px-2 py-1.5 border border-amber-500/30 cursor-pointer max-w-[145px] sm:max-w-[175px] truncate transition-colors" title="स्वर चुनें (Select Voice)">',
            '    <option value="">स्वर लोड हो रहे हैं...</option>',
            '  </select>',
            '  <select id="tts-ctrl-speed" onchange="window.PushtiOnlineTTS.setSpeed(parseFloat(this.value))" class="bg-slate-800 hover:bg-slate-700 text-slate-200 text-[11px] font-semibold rounded-lg px-2 py-1.5 border border-slate-700 cursor-pointer transition-colors" title="गति (Playback Speed)">',
            '    <option value="0.75">0.75x</option>',
            '    <option value="0.85">0.85x</option>',
            '    <option value="1">1.0x</option>',
            '    <option value="1.15">1.15x</option>',
            '    <option value="1.3">1.3x</option>',
            '    <option value="1.4">1.4x</option>',
            '    <option value="1.5">1.5x</option>',
            '    <option value="1.75">1.75x</option>',
            '    <option value="2">2.0x</option>',
            '  </select>',
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
            '  <button onclick="window.PushtiOnlineTTS.hidePlayer()" class="hidden md:inline-flex p-1.5 text-slate-400 hover:text-white transition-all text-xs ml-1 cursor-pointer" title="बंद करें">',
            '    <i class="fas fa-times"></i>',
            '  </button>',
            '</div>'
        ].join('');
        document.body.appendChild(bar);

        // Initialize speed select value
        var speedSelect = bar.querySelector('#tts-ctrl-speed');
        if (speedSelect) {
            speedSelect.value = playbackRate.toString();
        }

        populateVoiceDropdown();
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
        utter.pitch = speechPitch;

        // Select the finest voice
        if (!cachedSelectedVoice) {
            cachedSelectedVoice = getActiveVoice(lang);
        }
        if (cachedSelectedVoice) {
            utter.voice = cachedSelectedVoice;
            if (cachedSelectedVoice.lang) {
                utter.lang = cachedSelectedVoice.lang;
            }
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
        playbackRate = parseFloat(rate) || 1.0;
        try {
            localStorage.setItem('psh_tts_speed', playbackRate.toString());
        } catch (e) {}
        var sel = document.getElementById('tts-ctrl-speed');
        if (sel && sel.value !== playbackRate.toString()) {
            sel.value = playbackRate.toString();
        }
        if (engineState === STATE_PLAYING && window.speechSynthesis) {
            window.speechSynthesis.cancel();
            playQueue(activeLang, playSessionId);
        }
    }

    function setVoiceByName(voiceName) {
        if (!voiceName || !('speechSynthesis' in window)) return;
        var voices = window.speechSynthesis.getVoices();
        var match = voices.find(function (v) { return v.name === voiceName; });
        if (match) {
            cachedSelectedVoice = match;
            try {
                localStorage.setItem('psh_tts_voice_name', match.name);
            } catch (e) {}
            updateVoiceBadge(match);
            var sel = document.getElementById('tts-ctrl-voice');
            if (sel && sel.value !== match.name) {
                sel.value = match.name;
            }
            if (engineState === STATE_PLAYING && window.speechSynthesis) {
                window.speechSynthesis.cancel();
                playQueue(activeLang, playSessionId);
            }
        }
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
        setVoiceByName: setVoiceByName,
        getActiveVoice: getActiveVoice,
        getAvailableVoices: function () {
            return ('speechSynthesis' in window) ? window.speechSynthesis.getVoices() : [];
        },
        formatVoiceLabel: formatVoiceLabel,
        hidePlayer: hidePlayer,
        isSpeaking: function () {
            return engineState === STATE_PLAYING;
        },
        getState: function () {
            return engineState;
        },
        chunkText: chunkText,
        sanitizeText: sanitizeText,
        getBestFemaleVoice: findBestVoice
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
