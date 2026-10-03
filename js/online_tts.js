/**
 * Pushti Study Hub - Online Cloud Audio TTS Engine
 * High-fidelity, zero-delay online text-to-speech for Hindi and English.
 * Solves browser SpeechSynthesis stutter, timeout, and dropped-audio bugs by streaming
 * natural native pronunciation via Google Cloud Translate Audio API.
 *
 * Features:
 *   - Auto language detection (Hindi 'hi' for Devanagari, English 'en' for Latin).
 *   - Intelligent sentence boundary chunking (। , . ? ! \n).
 *   - Lookahead audio pre-buffering for gapless, smooth playback across long lessons.
 *   - UI button state synchronization & reading element spotlight.
 *   - Graceful fallback if offline.
 */

(function (window) {
    'use strict';

    if (window.PushtiOnlineTTS) return;

    var currentAudio = null;
    var preloadedAudio = null;
    var audioQueue = [];
    var currentQueueIndex = 0;
    var isPlaying = false;
    var activeBtn = null;
    var originalBtnContent = '';
    var activeTargetEl = null;
    var playSessionId = 0;

    // Detect if text contains Devanagari (Hindi / Sanskrit)
    function isDevanagari(text) {
        return /[\u0900-\u097F]/.test(text);
    }

    // Clean text for speech
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

    // Split text into natural sentence chunks under maxChars (Google API accepts ~180-200 chars)
    function chunkText(text, maxChars) {
        maxChars = maxChars || 160;
        var clean = sanitizeText(text);
        if (!clean) return [];

        // Split on Hindi purna viram (।), periods (.), exclamation (!), question marks (?), newlines
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
                // Split long sentence on commas, semicolons, or spaces
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
        var encoded = encodeURIComponent(textChunk);
        return 'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=' + encodeURIComponent(lang) + '&q=' + encoded;
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
        preloadedAudio = new Audio(url);
        preloadedAudio.preload = 'auto';
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
            audioObj = new Audio(url);
        }

        currentAudio = audioObj;

        // Preload next chunk ahead of time for gapless streaming
        preloadNext(currentQueueIndex + 1, lang, sessionId);

        audioObj.onended = function () {
            if (sessionId !== playSessionId) return;
            currentQueueIndex++;
            playQueue(lang, sessionId, onComplete);
        };

        audioObj.onerror = function () {
            if (sessionId !== playSessionId) return;
            console.warn('[PushtiOnlineTTS] Audio chunk error, advancing to next chunk:', chunk);
            currentQueueIndex++;
            playQueue(lang, sessionId, onComplete);
        };

        var playPromise = audioObj.play();
        if (playPromise !== undefined) {
            playPromise.catch(function (err) {
                if (sessionId !== playSessionId) return;
                console.warn('[PushtiOnlineTTS] Autoplay prevented or network error:', err);
                // Fallback attempt with SpeechSynthesis if audio fetch fails
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

        // If clicking on the same button currently speaking, toggle stop
        if (isPlaying && options.btn && options.btn === activeBtn) {
            stop();
            return;
        }

        stop();

        var clean = sanitizeText(text);
        if (!clean) return;

        // Determine language
        var lang = options.lang;
        if (!lang) {
            lang = isDevanagari(clean) ? 'hi' : 'en';
        }

        var chunks = chunkText(clean, 160);
        if (!chunks.length) return;

        audioQueue = chunks;
        currentQueueIndex = 0;
        isPlaying = true;
        var mySessionId = ++playSessionId;

        // Update UI Button
        if (options.btn) {
            activeBtn = options.btn;
            originalBtnContent = activeBtn.innerHTML;
            activeBtn.setAttribute('data-speaking', 'true');
            activeBtn.classList.add('speaking');

            if (lang === 'hi') {
                activeBtn.innerHTML = '<i class="fas fa-stop text-rose-400 animate-pulse"></i> रोकें';
            } else {
                activeBtn.innerHTML = '<i class="fas fa-stop"></i>';
            }
        }

        // Target highlight
        if (options.targetEl) {
            activeTargetEl = options.targetEl;
            activeTargetEl.classList.add('pushti-tts-reading-target');
        }

        playQueue(lang, mySessionId, options.onComplete);
    }

    // Expose Public API
    window.PushtiOnlineTTS = {
        speak: speak,
        stop: stop,
        isSpeaking: function () {
            return isPlaying;
        },
        chunkText: chunkText,
        sanitizeText: sanitizeText
    };

    // Override global helper functions so existing onclick handlers automatically use Online TTS
    window.speakHindiText = function (text, btn) {
        window.PushtiOnlineTTS.speak(text, { lang: 'hi', btn: btn });
    };

    window.speakHindiWord = function (word, meaning, btn) {
        var text = word + '... अर्थात्... ' + meaning;
        window.PushtiOnlineTTS.speak(text, { lang: 'hi', btn: btn });
    };

    window.speakFullLesson = function (btn) {
        // Collect all readable text in #tabText
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
        window.PushtiOnlineTTS.speak(text, { lang: 'hi', btn: btn, targetEl: targetContainer });
    };

})(window);
