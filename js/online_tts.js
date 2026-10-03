/**
 * Pushti Study Hub - Online Cloud Audio TTS Engine
 * Version: 2.0.0 (High-Fidelity Dual-Route Audio Streamer)
 *
 * Solves:
 *   1. System SpeechSynthesis timeout/stutter/stalls on Windows/Chromium.
 *   2. Google Translate TTS Referrer 404 blocking via automatic no-referrer injection
 *      and dedicated local `/api/tts` proxy.
 *   3. Self-healing DOM text extraction (supports inline buttons even if sibling selectors were broken).
 *   4. Zero-delay lookahead prebuffering for gapless playback of long lessons.
 */

(function (window) {
    'use strict';

    // Auto-inject <meta name="referrer" content="no-referrer"> to allow audio streaming
    if (!document.querySelector('meta[name="referrer"]')) {
        try {
            var meta = document.createElement('meta');
            meta.name = 'referrer';
            meta.content = 'no-referrer';
            document.head.appendChild(meta);
        } catch (e) {}
    }

    var currentAudio = null;
    var preloadedAudio = null;
    var audioQueue = [];
    var currentQueueIndex = 0;
    var isPlaying = false;
    var activeBtn = null;
    var originalBtnContent = '';
    var activeTargetEl = null;
    var playSessionId = 0;

    // Detect if host has local /api/tts proxy endpoint
    var isLocalHost = (window.location.hostname === 'localhost' || 
                       window.location.hostname === '127.0.0.1' || 
                       window.location.protocol === 'file:');

    function isDevanagari(text) {
        return /[\u0900-\u097F]/.test(text);
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
        maxChars = maxChars || 150;
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

    function getAudioUrl(textChunk, lang) {
        var encText = encodeURIComponent(textChunk);
        var encLang = encodeURIComponent(lang);
        if (isLocalHost && window.location.protocol.indexOf('http') === 0) {
            // Local high-speed proxy
            return '/api/tts?tl=' + encLang + '&q=' + encText;
        }
        // Direct Google Cloud Audio endpoint (with no-referrer meta)
        return 'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=' + encLang + '&q=' + encText;
    }

    function stop() {
        playSessionId++;
        isPlaying = false;

        if (currentAudio) {
            try {
                currentAudio.pause();
                currentAudio.src = '';
            } catch (e) {}
            currentAudio = null;
        }

        if (preloadedAudio) {
            try {
                preloadedAudio.pause();
                preloadedAudio.src = '';
            } catch (e) {}
            preloadedAudio = null;
        }

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

        if ('speechSynthesis' in window && window.speechSynthesis.speaking) {
            window.speechSynthesis.cancel();
        }
    }

    function preloadNext(index, lang, sessionId) {
        if (index >= audioQueue.length) {
            preloadedAudio = null;
            return;
        }
        var nextChunk = audioQueue[index];
        var url = getAudioUrl(nextChunk, lang);
        preloadedAudio = new Audio();
        preloadedAudio.referrerPolicy = 'no-referrer';
        preloadedAudio.preload = 'auto';
        preloadedAudio.src = url;
    }

    function playQueue(lang, sessionId, onComplete) {
        if (sessionId !== playSessionId || !isPlaying) return;

        if (currentQueueIndex >= audioQueue.length) {
            stop();
            if (typeof onComplete === 'function') onComplete();
            return;
        }

        var chunk = audioQueue[currentQueueIndex];
        var audioObj = preloadedAudio;
        preloadedAudio = null;

        if (!audioObj) {
            var url = getAudioUrl(chunk, lang);
            audioObj = new Audio();
            audioObj.referrerPolicy = 'no-referrer';
            audioObj.src = url;
        }

        currentAudio = audioObj;

        // Lookahead buffer
        preloadNext(currentQueueIndex + 1, lang, sessionId);

        audioObj.onended = function () {
            if (sessionId !== playSessionId) return;
            currentQueueIndex++;
            playQueue(lang, sessionId, onComplete);
        };

        audioObj.onerror = function () {
            if (sessionId !== playSessionId) return;
            console.warn('[PushtiOnlineTTS] Audio stream error on chunk:', chunk);
            // Fallback attempt to SpeechSynthesis
            fallbackSpeechSynthesis(chunk, lang, function () {
                currentQueueIndex++;
                playQueue(lang, sessionId, onComplete);
            });
        };

        var playPromise = audioObj.play();
        if (playPromise !== undefined) {
            playPromise.catch(function (err) {
                if (sessionId !== playSessionId) return;
                console.warn('[PushtiOnlineTTS] Play error:', err);
                fallbackSpeechSynthesis(chunk, lang, function () {
                    currentQueueIndex++;
                    playQueue(lang, sessionId, onComplete);
                });
            });
        }
    }

    function fallbackSpeechSynthesis(text, lang, onEnd) {
        if (!('speechSynthesis' in window)) {
            if (onEnd) onEnd();
            return;
        }
        var utter = new SpeechSynthesisUtterance(text);
        utter.lang = (lang === 'hi') ? 'hi-IN' : 'en-IN';
        utter.onend = function () {
            if (onEnd) onEnd();
        };
        utter.onerror = function () {
            if (onEnd) onEnd();
        };
        window.speechSynthesis.speak(utter);
    }

    function speak(text, options) {
        options = options || {};

        var btn = options.btn;
        // Auto-detect button from event if not provided
        if (!btn && window.event && window.event.target) {
            try {
                btn = window.event.target.closest('button');
            } catch (e) {}
        }

        if (isPlaying && btn && btn === activeBtn) {
            stop();
            return;
        }

        stop();

        var clean = sanitizeText(text);
        if (!clean) return;

        var lang = options.lang;
        if (!lang) {
            lang = isDevanagari(clean) ? 'hi' : 'en';
        }

        var chunks = chunkText(clean, 150);
        if (!chunks.length) return;

        audioQueue = chunks;
        currentQueueIndex = 0;
        isPlaying = true;
        var mySessionId = ++playSessionId;

        if (btn) {
            activeBtn = btn;
            originalBtnContent = activeBtn.innerHTML;
            activeBtn.setAttribute('data-speaking', 'true');
            activeBtn.classList.add('speaking');

            if (lang === 'hi') {
                activeBtn.innerHTML = '<i class="fas fa-stop text-rose-400 animate-pulse"></i> रोकें';
            } else {
                activeBtn.innerHTML = '<i class="fas fa-stop"></i>';
            }
        }

        if (options.targetEl) {
            activeTargetEl = options.targetEl;
            activeTargetEl.classList.add('pushti-tts-reading-target');
        }

        playQueue(lang, mySessionId, options.onComplete);
    }

    // Expose API
    window.PushtiOnlineTTS = {
        speak: speak,
        stop: stop,
        isSpeaking: function () {
            return isPlaying;
        },
        chunkText: chunkText,
        sanitizeText: sanitizeText
    };

    // --- SELF-HEALING HINDI WRAPPERS ---
    window.speakHindiText = function (targetOrText, btn) {
        var text = '';
        var targetEl = null;

        // Try extracting text from string or DOM element
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

        // Self-heal: extract from parent card if text was missing/empty
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
            window.PushtiOnlineTTS.speak(text, { lang: 'hi', btn: activeTargetBtn, targetEl: targetEl });
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
        window.PushtiOnlineTTS.speak(text, { lang: 'hi', btn: activeTargetBtn });
    };

    window.speakFullLesson = function (btn) {
        var activeTargetBtn = btn;
        if (!activeTargetBtn && window.event && window.event.target) {
            try {
                activeTargetBtn = window.event.target.closest('button');
            } catch (e) {}
        }
        var targetContainer = document.getElementById('tabText') || document.querySelector('.lesson-content-body');
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
        window.PushtiOnlineTTS.speak(text, { lang: 'hi', btn: activeTargetBtn, targetEl: targetContainer });
    };

})(window);
