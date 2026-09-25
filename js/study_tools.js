/**
 * Pushti Study Hub - Universal Study Tools & Active Recall Engine
 * Features:
 *   1. Fullscreen & Landscape Orientation Lock (Optimized for Android Tablets & Laptops)
 *   2. Natural Text-to-Speech (TTS) "Read Out Loud" Engine (en-IN / hi-IN priority)
 *   3. Intelligent Card-Level Listen Buttons & Floating Media Controller
 *   4. Clean Math & Text Sanitizer for Pronunciation
 *   5. Quick Recall Checklist & Summary Paper Generator (Active Recall Tab in Vertical Tabs)
 * Version: 2.0.0 — Pure Vanilla JS, Zero Dependencies, Zero-Freeze Engine
 */

(function () {
    'use strict';

    if (window.__pushtiStudyToolsLoaded) return;
    window.__pushtiStudyToolsLoaded = true;

    // --- State & Variables ---
    var isSpeaking = false;
    var isPaused = false;
    var currentUtterance = null;
    var currentActiveEl = null;
    var playbackSpeed = 1.0;
    var availableVoices = [];
    var selectedVoice = null;
    var isHindiPage = document.documentElement.lang === 'hi' || 
                      window.location.pathname.indexOf('/hindi/') !== -1 ||
                      document.title.indexOf('Hindi') !== -1 ||
                      document.title.indexOf('हिन्दी') !== -1;

    // Recall State
    var recallItems = [];
    var recallFilter = 'all';
    var storageKey = 'pushti_recall_' + window.location.pathname.replace(/[^a-zA-Z0-9]/g, '_');

    // --- DOM Elements ---
    var dock = null;
    var playPauseBtn = null;
    var stopBtn = null;
    var speedBtn = null;
    var fullscreenBtn = null;
    var recallDockBtn = null;
    var statusText = null;

    // --- 1. CSS Ingestion ---
    function injectStyles() {
        if (document.getElementById('pushti-study-tools-styles')) return;
        var style = document.createElement('style');
        style.id = 'pushti-study-tools-styles';
        style.textContent = [
            '/* Pushti Study Tools Floating Dock */',
            '.pushti-study-dock {',
            '    position: fixed;',
            '    bottom: 24px;',
            '    left: 24px;',
            '    z-index: 99998;',
            '    display: flex;',
            '    align-items: center;',
            '    gap: 8px;',
            '    background: rgba(26, 24, 41, 0.92);',
            '    border: 1px solid rgba(139, 92, 246, 0.35);',
            '    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.45), 0 2px 8px rgba(99, 102, 241, 0.2);',
            '    border-radius: 40px;',
            '    padding: 6px 12px;',
            '    backdrop-filter: blur(12px);',
            '    -webkit-backdrop-filter: blur(12px);',
            '    font-family: "Outfit", "Inter", system-ui, sans-serif;',
            '    color: #fffffe;',
            '    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);',
            '    user-select: none;',
            '    -webkit-tap-highlight-color: transparent;',
            '}',
            '[data-theme="light"] .pushti-study-dock {',
            '    background: rgba(255, 255, 255, 0.94);',
            '    border-color: rgba(99, 102, 241, 0.25);',
            '    box-shadow: 0 8px 30px rgba(99, 102, 241, 0.15), 0 2px 8px rgba(0, 0, 0, 0.06);',
            '    color: #1e1b4b;',
            '}',
            '.pushti-dock-btn {',
            '    background: transparent;',
            '    border: none;',
            '    outline: none;',
            '    color: inherit;',
            '    cursor: pointer;',
            '    padding: 6px 10px;',
            '    border-radius: 20px;',
            '    font-size: 0.84rem;',
            '    font-weight: 600;',
            '    display: flex;',
            '    align-items: center;',
            '    gap: 6px;',
            '    transition: background 0.18s, color 0.18s, transform 0.18s;',
            '    white-space: nowrap;',
            '}',
            '.pushti-dock-btn:hover {',
            '    background: rgba(139, 92, 246, 0.2);',
            '    color: #c4b5fd;',
            '    transform: translateY(-1px);',
            '}',
            '[data-theme="light"] .pushti-dock-btn:hover {',
            '    background: rgba(99, 102, 241, 0.12);',
            '    color: #4f46e5;',
            '}',
            '.pushti-dock-btn:active { transform: translateY(0) scale(0.96); }',
            '.pushti-dock-btn svg { width: 16px; height: 16px; fill: currentColor; }',
            '.pushti-dock-divider {',
            '    width: 1px;',
            '    height: 18px;',
            '    background: rgba(255, 255, 255, 0.15);',
            '    margin: 0 2px;',
            '}',
            '[data-theme="light"] .pushti-dock-divider { background: rgba(0, 0, 0, 0.12); }',
            '.pushti-dock-status {',
            '    font-size: 0.75rem;',
            '    color: #a78bfa;',
            '    padding: 0 6px;',
            '    font-family: "JetBrains Mono", monospace;',
            '    max-width: 120px;',
            '    white-space: nowrap;',
            '    overflow: hidden;',
            '    text-overflow: ellipsis;',
            '}',
            '[data-theme="light"] .pushti-dock-status { color: #6366f1; }',
            '/* Card Listen Button */',
            '.pushti-tts-card-btn {',
            '    display: inline-flex;',
            '    align-items: center;',
            '    gap: 5px;',
            '    padding: 3px 8px;',
            '    font-size: 0.72rem;',
            '    font-weight: 700;',
            '    border-radius: 12px;',
            '    border: 1px solid rgba(139, 92, 246, 0.35);',
            '    background: rgba(139, 92, 246, 0.12);',
            '    color: #c4b5fd;',
            '    cursor: pointer;',
            '    transition: all 0.2s ease;',
            '    vertical-align: middle;',
            '    margin-left: 8px;',
            '    text-transform: uppercase;',
            '}',
            '[data-theme="light"] .pushti-tts-card-btn {',
            '    background: rgba(99, 102, 241, 0.08);',
            '    border-color: rgba(99, 102, 241, 0.25);',
            '    color: #4f46e5;',
            '}',
            '.pushti-tts-card-btn:hover {',
            '    background: #6366f1;',
            '    color: #ffffff !important;',
            '    border-color: #6366f1;',
            '    transform: translateY(-1px);',
            '    box-shadow: 0 2px 8px rgba(99, 102, 241, 0.35);',
            '}',
            '.pushti-tts-card-btn.speaking {',
            '    background: #10b981 !important;',
            '    color: #ffffff !important;',
            '    border-color: #10b981 !important;',
            '    animation: pushtiPulse 1.4s infinite;',
            '}',
            '@keyframes pushtiPulse {',
            '    0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.5); }',
            '    70% { box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }',
            '    100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }',
            '}',
            '.pushti-tts-active-card {',
            '    outline: 2px solid #8b5cf6 !important;',
            '    outline-offset: 3px;',
            '    box-shadow: 0 0 20px rgba(139, 92, 246, 0.3) !important;',
            '    transition: outline 0.25s, box-shadow 0.25s;',
            '}',
            '/* QUICK RECALL CHECKLIST STYLES */',
            '.pushti-recall-tab-btn {',
            '    position: relative;',
            '    border-left: 3px solid #10b981 !important;',
            '}',
            '.pushti-recall-tab-btn .badge-recall {',
            '    font-size: 0.68rem;',
            '    padding: 2px 6px;',
            '    border-radius: 4px;',
            '    background: rgba(16, 185, 129, 0.2);',
            '    color: #34d399;',
            '    font-weight: 700;',
            '    margin-left: auto;',
            '}',
            '#tab-quick-recall {',
            '    display: none;',
            '    animation: fadeInRecall 0.25s ease;',
            '}',
            '#tab-quick-recall.active {',
            '    display: block !important;',
            '}',
            '@keyframes fadeInRecall {',
            '    from { opacity: 0; transform: translateY(8px); }',
            '    to { opacity: 1; transform: translateY(0); }',
            '}',
            '.recall-banner {',
            '    background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(99, 102, 241, 0.08));',
            '    border: 1px solid rgba(16, 185, 129, 0.35);',
            '    border-radius: 14px;',
            '    padding: 20px 24px;',
            '    margin-bottom: 24px;',
            '}',
            '.recall-banner-top {',
            '    display: flex;',
            '    justify-content: space-between;',
            '    align-items: center;',
            '    flex-wrap: wrap;',
            '    gap: 12px;',
            '    margin-bottom: 12px;',
            '}',
            '.recall-title {',
            '    font-family: "Outfit", sans-serif;',
            '    font-size: 1.45rem;',
            '    font-weight: 700;',
            '    margin: 0;',
            '    display: flex;',
            '    align-items: center;',
            '    gap: 10px;',
            '}',
            '.recall-actions-bar {',
            '    display: flex;',
            '    align-items: center;',
            '    gap: 8px;',
            '}',
            '.recall-btn-action {',
            '    padding: 6px 12px;',
            '    border-radius: 8px;',
            '    font-size: 0.8rem;',
            '    font-weight: 600;',
            '    border: 1px solid rgba(16, 185, 129, 0.35);',
            '    background: rgba(16, 185, 129, 0.12);',
            '    color: #34d399;',
            '    cursor: pointer;',
            '    display: inline-flex;',
            '    align-items: center;',
            '    gap: 6px;',
            '    transition: all 0.2s;',
            '}',
            '.recall-btn-action:hover {',
            '    background: #10b981;',
            '    color: #fff;',
            '}',
            '.recall-progress-wrap {',
            '    margin: 14px 0;',
            '}',
            '.recall-progress-bar-bg {',
            '    height: 8px;',
            '    background: rgba(255, 255, 255, 0.08);',
            '    border-radius: 4px;',
            '    overflow: hidden;',
            '}',
            '.recall-progress-fill {',
            '    height: 100%;',
            '    width: 0%;',
            '    background: linear-gradient(90deg, #10b981, #34d399);',
            '    transition: width 0.3s ease;',
            '}',
            '.recall-stats-pills {',
            '    display: flex;',
            '    align-items: center;',
            '    gap: 10px;',
            '    flex-wrap: wrap;',
            '    margin-top: 10px;',
            '}',
            '.recall-pill {',
            '    font-size: 0.78rem;',
            '    font-weight: 700;',
            '    padding: 4px 10px;',
            '    border-radius: 12px;',
            '    display: inline-flex;',
            '    align-items: center;',
            '    gap: 5px;',
            '}',
            '.recall-pill.pill-all { background: rgba(255,255,255,0.06); color: var(--text-main, #f1f5f9); }',
            '.recall-pill.pill-mastered { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }',
            '.recall-pill.pill-review { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }',
            '.recall-pill.pill-untested { background: rgba(148, 163, 184, 0.12); color: #94a3b8; }',
            '.recall-filter-bar {',
            '    display: flex;',
            '    gap: 8px;',
            '    margin-bottom: 20px;',
            '    flex-wrap: wrap;',
            '}',
            '.recall-filter-btn {',
            '    padding: 6px 14px;',
            '    border-radius: 20px;',
            '    border: 1px solid rgba(255, 255, 255, 0.1);',
            '    background: rgba(0, 0, 0, 0.15);',
            '    color: var(--text-muted, #94a3b8);',
            '    font-size: 0.82rem;',
            '    font-weight: 600;',
            '    cursor: pointer;',
            '    transition: all 0.2s;',
            '}',
            '.recall-filter-btn.active {',
            '    background: #10b981;',
            '    border-color: #10b981;',
            '    color: #fff;',
            '}',
            '/* Recall Items List */',
            '.recall-item-card {',
            '    background: var(--bg-card, rgba(13, 29, 48, 0.75));',
            '    border: 1px solid rgba(255, 255, 255, 0.08);',
            '    border-radius: 12px;',
            '    padding: 16px 20px;',
            '    margin-bottom: 12px;',
            '    transition: all 0.2s;',
            '}',
            '.recall-item-card.state-mastered {',
            '    border-left: 4px solid #10b981;',
            '    background: rgba(16, 185, 129, 0.06);',
            '}',
            '.recall-item-card.state-review {',
            '    border-left: 4px solid #f59e0b;',
            '    background: rgba(245, 158, 11, 0.06);',
            '}',
            '.recall-item-top {',
            '    display: flex;',
            '    justify-content: space-between;',
            '    align-items: center;',
            '    gap: 12px;',
            '}',
            '.recall-item-title {',
            '    font-family: "Outfit", sans-serif;',
            '    font-weight: 700;',
            '    font-size: 1.05rem;',
            '    color: var(--text-main, #f1f5f9);',
            '}',
            '.recall-item-badge {',
            '    font-size: 0.72rem;',
            '    padding: 2px 8px;',
            '    border-radius: 4px;',
            '    font-weight: 700;',
            '    text-transform: uppercase;',
            '}',
            '.badge-mastered { background: rgba(16,185,129,0.2); color: #34d399; }',
            '.badge-review { background: rgba(245,158,11,0.2); color: #fbbf24; }',
            '.badge-untested { background: rgba(148,163,184,0.15); color: #94a3b8; }',
            '.recall-prompt {',
            '    font-size: 0.88rem;',
            '    color: var(--text-muted, #94a3b8);',
            '    margin: 8px 0 12px 0;',
            '}',
            '.recall-actions-row {',
            '    display: flex;',
            '    align-items: center;',
            '    justify-content: space-between;',
            '    flex-wrap: wrap;',
            '    gap: 10px;',
            '}',
            '.recall-btns-group {',
            '    display: flex;',
            '    gap: 8px;',
            '}',
            '.recall-btn-state {',
            '    padding: 5px 11px;',
            '    border-radius: 6px;',
            '    font-size: 0.78rem;',
            '    font-weight: 600;',
            '    border: 1px solid rgba(255, 255, 255, 0.1);',
            '    background: rgba(0, 0, 0, 0.2);',
            '    color: var(--text-muted, #94a3b8);',
            '    cursor: pointer;',
            '    display: inline-flex;',
            '    align-items: center;',
            '    gap: 5px;',
            '    transition: all 0.18s;',
            '}',
            '.recall-btn-state:hover { background: rgba(255, 255, 255, 0.08); }',
            '.recall-btn-state.active-mastered { background: #10b981; color: #fff; border-color: #10b981; }',
            '.recall-btn-state.active-review { background: #f59e0b; color: #000; border-color: #f59e0b; font-weight: 700; }',
            '.recall-peek-btn {',
            '    padding: 5px 12px;',
            '    border-radius: 6px;',
            '    font-size: 0.78rem;',
            '    font-weight: 600;',
            '    border: 1px solid rgba(99, 102, 241, 0.3);',
            '    background: rgba(99, 102, 241, 0.1);',
            '    color: #a5b4fc;',
            '    cursor: pointer;',
            '    display: inline-flex;',
            '    align-items: center;',
            '    gap: 5px;',
            '}',
            '.recall-peek-btn:hover { background: #6366f1; color: #fff; }',
            '.recall-peek-answer {',
            '    display: none;',
            '    margin-top: 12px;',
            '    padding: 12px 16px;',
            '    border-radius: 8px;',
            '    background: rgba(0, 0, 0, 0.25);',
            '    border-left: 3px solid #6366f1;',
            '    font-size: 0.86rem;',
            '    color: var(--text-main, #f1f5f9);',
            '    line-height: 1.55;',
            '}',
            '.recall-peek-answer.visible { display: block; }',
            '/* Summary Paper Print Styles */',
            '@media print {',
            '    .pushti-study-dock, .pushti-jump-to-top, .sidebar, .sidebar-nav, .tab-bar, .top-nav,',
            '    .recall-actions-bar, .recall-filter-bar, .recall-btns-group, .recall-peek-btn {',
            '        display: none !important;',
            '    }',
            '    #tab-quick-recall { display: block !important; }',
            '    .recall-banner { border: 1px solid #ccc !important; color: #000 !important; background: #fff !important; }',
            '    .recall-item-card { background: #fff !important; border: 1px solid #ddd !important; color: #000 !important; page-break-inside: avoid; }',
            '    .recall-peek-answer { display: block !important; background: #f9f9f9 !important; color: #000 !important; border-left: 3px solid #666 !important; }',
            '}',
            '@media (max-width: 768px) {',
            '    .pushti-study-dock {',
            '        bottom: 16px;',
            '        left: 16px;',
            '        padding: 5px 8px;',
            '        gap: 4px;',
            '    }',
            '    .pushti-dock-status { display: none; }',
            '    .pushti-dock-btn { padding: 6px 8px; font-size: 0.78rem; }',
            '}'
        ].join('\n');
        document.head.appendChild(style);
    }

    // --- 2. Voice Selection (Prioritizing Indian English & Hindi) ---
    function initVoices() {
        if (!('speechSynthesis' in window)) return;
        
        function populate() {
            availableVoices = window.speechSynthesis.getVoices();
            if (!availableVoices || availableVoices.length === 0) return;

            if (isHindiPage) {
                selectedVoice = availableVoices.find(function (v) {
                    return v.lang === 'hi-IN' || v.lang.indexOf('hi') === 0;
                });
            } else {
                selectedVoice = availableVoices.find(function (v) {
                    return v.lang === 'en-IN' && (v.name.indexOf('Google') !== -1 || v.name.indexOf('Natural') !== -1);
                }) || availableVoices.find(function (v) {
                    return v.lang === 'en-IN';
                }) || availableVoices.find(function (v) {
                    return (v.lang === 'en-GB' || v.lang === 'en-US') && (v.name.indexOf('Natural') !== -1 || v.name.indexOf('Google') !== -1);
                }) || availableVoices.find(function (v) {
                    return v.lang.indexOf('en') === 0;
                }) || availableVoices[0];
            }

            if (statusText) {
                var voiceLabel = selectedVoice ? (selectedVoice.lang + ' Voice') : 'Voice Ready';
                statusText.textContent = voiceLabel;
            }
        }

        populate();
        if (window.speechSynthesis.onvoiceschanged !== undefined) {
            window.speechSynthesis.onvoiceschanged = populate;
        }
    }

    // --- 3. Speech Text Sanitizer ---
    function sanitizeTextForSpeech(text) {
        if (!text) return '';
        var clean = text
            .replace(/\$\$[\s\S]*?\$\$/g, ' mathematical equation ')
            .replace(/\$([^\$]+)\$/g, '$1')
            .replace(/\\\[[\s\S]*?\\\]/g, ' mathematical expression ')
            .replace(/\\\(([^\)]+)\\\)/g, '$1')
            .replace(/\\(?:dfrac|frac)\{([^}]+)\}\{([^}]+)\}/g, '$1 over $2')
            .replace(/\\times/g, ' multiplied by ')
            .replace(/\\div/g, ' divided by ')
            .replace(/\\pm/g, ' plus or minus ')
            .replace(/\\leq/g, ' less than or equal to ')
            .replace(/\\geq/g, ' greater than or equal to ')
            .replace(/\\neq/g, ' is not equal to ')
            .replace(/\\circ/g, ' degrees ')
            .replace(/\\text\{([^}]+)\}/g, '$1')
            .replace(/\\mathbf\{([^}]+)\}/g, '$1')
            .replace(/\b₹\s*([0-9,]+)/g, '$1 rupees')
            .replace(/°C\b/g, ' degrees Celsius')
            .replace(/&bull;/gi, ', ')
            .replace(/&ndash;/gi, ' to ')
            .replace(/&mdash;/gi, ', ')
            .replace(/&nbsp;/gi, ' ')
            .replace(/&amp;/gi, ' and ')
            .replace(/<[^>]+>/g, ' ')
            .replace(/\s+/g, ' ')
            .trim();
        return clean;
    }

    // --- 4. TTS Playback Controls ---
    function speakText(rawText, el) {
        if (!('speechSynthesis' in window)) {
            alert('Speech Synthesis is not supported in this browser.');
            return;
        }

        var text = sanitizeTextForSpeech(rawText);
        if (!text) return;

        window.speechSynthesis.cancel();

        if (currentActiveEl) {
            currentActiveEl.classList.remove('pushti-tts-active-card');
            var oldBtn = currentActiveEl.querySelector('.pushti-tts-card-btn');
            if (oldBtn) oldBtn.classList.remove('speaking');
        }

        if (el) {
            currentActiveEl = el;
            currentActiveEl.classList.add('pushti-tts-active-card');
            var cardBtn = currentActiveEl.querySelector('.pushti-tts-card-btn');
            if (cardBtn) cardBtn.classList.add('speaking');
        }

        currentUtterance = new SpeechSynthesisUtterance(text);
        if (selectedVoice) currentUtterance.voice = selectedVoice;
        currentUtterance.rate = playbackSpeed;
        currentUtterance.pitch = 1.0;

        currentUtterance.onstart = function () {
            isSpeaking = true;
            isPaused = false;
            updateDockUI();
        };

        currentUtterance.onend = function () {
            isSpeaking = false;
            isPaused = false;
            if (currentActiveEl) {
                currentActiveEl.classList.remove('pushti-tts-active-card');
                var b = currentActiveEl.querySelector('.pushti-tts-card-btn');
                if (b) b.classList.remove('speaking');
                currentActiveEl = null;
            }
            updateDockUI();
        };

        currentUtterance.onerror = function (e) {
            console.warn('SpeechSynthesis error:', e);
            isSpeaking = false;
            isPaused = false;
            if (currentActiveEl) {
                currentActiveEl.classList.remove('pushti-tts-active-card');
                var b = currentActiveEl.querySelector('.pushti-tts-card-btn');
                if (b) b.classList.remove('speaking');
                currentActiveEl = null;
            }
            updateDockUI();
        };

        window.speechSynthesis.speak(currentUtterance);
    }

    function togglePlayPause() {
        if (!('speechSynthesis' in window)) return;

        if (isSpeaking && !isPaused) {
            window.speechSynthesis.pause();
            isPaused = true;
            updateDockUI();
        } else if (isSpeaking && isPaused) {
            window.speechSynthesis.resume();
            isPaused = false;
            updateDockUI();
        } else {
            var activeTab = document.querySelector('.tab-pane.active, .tab-content.active, [data-tab-pane].active, main, body');
            if (activeTab) {
                var firstCard = activeTab.querySelector('.concept-card, .rule-box, .formula-card, .card, h2, h3');
                if (firstCard) {
                    speakText(firstCard.innerText || firstCard.textContent, firstCard);
                } else {
                    speakText(activeTab.innerText || activeTab.textContent, null);
                }
            }
        }
    }

    function stopSpeaking() {
        if (!('speechSynthesis' in window)) return;
        window.speechSynthesis.cancel();
        isSpeaking = false;
        isPaused = false;
        if (currentActiveEl) {
            currentActiveEl.classList.remove('pushti-tts-active-card');
            var b = currentActiveEl.querySelector('.pushti-tts-card-btn');
            if (b) b.classList.remove('speaking');
            currentActiveEl = null;
        }
        updateDockUI();
    }

    function cycleSpeed() {
        if (playbackSpeed === 1.0) playbackSpeed = 1.2;
        else if (playbackSpeed === 1.2) playbackSpeed = 0.85;
        else playbackSpeed = 1.0;

        if (speedBtn) speedBtn.textContent = playbackSpeed + 'x';

        if (isSpeaking && currentUtterance) {
            var el = currentActiveEl;
            var text = currentUtterance.text;
            speakText(text, el);
        }
    }

    // --- 5. Fullscreen & Landscape Lock ---
    function toggleFullscreenLandscape() {
        var doc = window.document;
        var docEl = doc.documentElement;

        var requestFs = docEl.requestFullscreen || docEl.mozRequestFullScreen || docEl.webkitRequestFullScreen || docEl.msRequestFullscreen;
        var cancelFs = doc.exitFullscreen || doc.mozCancelFullScreen || doc.webkitExitFullscreen || doc.msExitFullscreen;
        var isFs = doc.fullscreenElement || doc.mozFullScreenElement || doc.webkitFullscreenElement || doc.msFullscreenElement;

        if (!isFs) {
            if (requestFs) {
                requestFs.call(docEl).then(function () {
                    tryLockLandscape();
                }).catch(function () {
                    tryLockLandscape();
                });
            } else {
                tryLockLandscape();
            }
        } else {
            if (cancelFs) {
                cancelFs.call(doc).then(function () {
                    tryUnlockOrientation();
                }).catch(function () {
                    tryUnlockOrientation();
                });
            } else {
                tryUnlockOrientation();
            }
        }
    }

    function tryLockLandscape() {
        if (screen.orientation && screen.orientation.lock) {
            screen.orientation.lock('landscape').catch(function () {});
        } else if (screen.lockOrientation) {
            screen.lockOrientation('landscape');
        }
    }

    function tryUnlockOrientation() {
        if (screen.orientation && screen.orientation.unlock) {
            screen.orientation.unlock();
        } else if (screen.unlockOrientation) {
            screen.unlockOrientation();
        }
    }

    function updateFullscreenUI() {
        var isFs = document.fullscreenElement || document.webkitFullscreenElement;
        if (fullscreenBtn) {
            if (isFs) {
                fullscreenBtn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M5 16h3v3h2v-5H5v2zm3-8H5v2h5V5H8v3zm6 11h2v-3h3v-2h-5v5zm2-14v3h3v2h-5V5h2z"></path></svg> ⛶ Exit';
            } else {
                fullscreenBtn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"></path></svg> ⛶ Landscape';
            }
        }
    }

    // --- 6. Card Button Auto-Injection ---
    function attachCardAudioButtons() {
        var targets = document.querySelectorAll(
            '.concept-card, .rule-box, .formula-card, .formula-box, .key-point, ' +
            '.note-card, .illustration-card, .concept-pillar, .topic-card, .summary-box'
        );

        targets.forEach(function (card) {
            if (card.querySelector('.pushti-tts-card-btn')) return;

            var titleEl = card.querySelector('h2, h3, h4, h5, .concept-title, .rule-title, strong');
            if (!titleEl) return;

            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'pushti-tts-card-btn';
            btn.innerHTML = '🔊 Listen';
            btn.setAttribute('title', 'Read this concept out loud');

            btn.addEventListener('click', function (e) {
                e.stopPropagation();
                if (btn.classList.contains('speaking')) {
                    stopSpeaking();
                } else {
                    speakText(card.innerText || card.textContent, card);
                }
            });

            titleEl.appendChild(btn);
        });
    }

    // --- 7. Dock Creation & UI Updates ---
    function updateDockUI() {
        if (!playPauseBtn) return;
        if (isSpeaking && !isPaused) {
            playPauseBtn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"></path></svg> Pause';
            if (statusText) statusText.textContent = 'Speaking...';
        } else if (isSpeaking && isPaused) {
            playPauseBtn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"></path></svg> Resume';
            if (statusText) statusText.textContent = 'Paused';
        } else {
            playPauseBtn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"></path></svg> Listen';
            if (statusText) {
                statusText.textContent = selectedVoice ? (selectedVoice.lang) : 'Ready';
            }
        }
    }

    function createStudyDock() {
        if (document.getElementById('pushti-study-dock')) return;

        dock = document.createElement('div');
        dock.id = 'pushti-study-dock';
        dock.className = 'pushti-study-dock';

        // Play/Pause Button
        playPauseBtn = document.createElement('button');
        playPauseBtn.className = 'pushti-dock-btn';
        playPauseBtn.setAttribute('title', 'Read Out Loud / Pause');
        playPauseBtn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"></path></svg> Listen';
        playPauseBtn.addEventListener('click', togglePlayPause);

        // Stop Button
        stopBtn = document.createElement('button');
        stopBtn.className = 'pushti-dock-btn';
        stopBtn.setAttribute('title', 'Stop Audio');
        stopBtn.innerHTML = '<svg viewBox="0 0 24 24"><rect x="6" y="6" width="12" height="12"></rect></svg> Stop';
        stopBtn.addEventListener('click', stopSpeaking);

        // Speed Toggle Button
        speedBtn = document.createElement('button');
        speedBtn.className = 'pushti-dock-btn';
        speedBtn.textContent = '1.0x';
        speedBtn.setAttribute('title', 'Playback Speed: 1.0x');
        speedBtn.addEventListener('click', cycleSpeed);

        // Recall Shortcut Button
        recallDockBtn = document.createElement('button');
        recallDockBtn.className = 'pushti-dock-btn';
        recallDockBtn.setAttribute('title', 'Open Quick Recall Checklist');
        recallDockBtn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-9 14l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path></svg> Recall';
        recallDockBtn.addEventListener('click', openQuickRecallTab);

        // Fullscreen / Landscape Button
        fullscreenBtn = document.createElement('button');
        fullscreenBtn.className = 'pushti-dock-btn';
        fullscreenBtn.setAttribute('title', 'Toggle Fullscreen & Landscape Mode');
        fullscreenBtn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"></path></svg> ⛶ Landscape';
        fullscreenBtn.addEventListener('click', toggleFullscreenLandscape);

        // Status Label
        statusText = document.createElement('span');
        statusText.className = 'pushti-dock-status';
        statusText.textContent = 'Ready';

        // Dividers
        var d1 = document.createElement('div'); d1.className = 'pushti-dock-divider';
        var d2 = document.createElement('div'); d2.className = 'pushti-dock-divider';
        var d3 = document.createElement('div'); d3.className = 'pushti-dock-divider';

        // Append to Dock
        dock.appendChild(playPauseBtn);
        dock.appendChild(stopBtn);
        dock.appendChild(speedBtn);
        dock.appendChild(d1);
        dock.appendChild(recallDockBtn);
        dock.appendChild(d2);
        dock.appendChild(fullscreenBtn);
        dock.appendChild(d3);
        dock.appendChild(statusText);

        document.body.appendChild(dock);

        document.addEventListener('fullscreenchange', updateFullscreenUI);
        document.addEventListener('webkitfullscreenchange', updateFullscreenUI);
        document.addEventListener('mozfullscreenchange', updateFullscreenUI);
        document.addEventListener('MSFullscreenChange', updateFullscreenUI);
    }

    // --- 8. QUICK RECALL CHECKLIST ENGINE ---
    function strHash(s) {
        var h = 0;
        for (var i = 0; i < s.length; i++) {
            h = ((h << 5) - h) + s.charCodeAt(i);
            h |= 0;
        }
        return Math.abs(h);
    }

    function harvestChapterConcepts() {
        var concepts = [];
        var seen = {};

        var cardEls = document.querySelectorAll(
            '.concept-card, .rule-box, .formula-card, .formula-box, .definition-card, ' +
            '.theory-card, .important-box, .concept-block, .unit-card'
        );

        cardEls.forEach(function(el) {
            if (el.closest('#tab-quick-recall') || el.closest('#sidebar')) return;
            var tEl = el.querySelector('h2, h3, h4, h5, strong, .concept-title, .rule-title') || el;
            var title = (tEl.textContent || '').trim();
            title = title.replace(/^(Rule|Concept|Topic|Pillar|Unit|Ch|Chapter|\d+[\.\)]|\s)+/i, '').trim();
            if (!title || title.length < 3 || title.length > 90 || seen[title.toLowerCase()]) return;
            seen[title.toLowerCase()] = true;

            var clone = el.cloneNode(true);
            clone.querySelectorAll('button, .tag, .badge, .pushti-tts-card-btn').forEach(function(r) { r.remove(); });
            var text = (clone.textContent || '').trim();
            if (text.startsWith(title)) text = text.slice(title.length).trim();
            if (text.length > 320) text = text.slice(0, 320) + '...';
            if (!text) text = 'Core concept principles and key rules detailed in chapter study notes.';

            concepts.push({
                id: 'rc_' + strHash(title),
                title: title,
                summary: text
            });
        });

        // Fallback if few cards found
        if (concepts.length < 4) {
            document.querySelectorAll('main h2, main h3, .main-content h2, .main-content h3').forEach(function(h) {
                var title = (h.textContent || '').trim();
                if (!title || title.length < 4 || title.length > 80 || seen[title.toLowerCase()]) return;
                seen[title.toLowerCase()] = true;

                var nextP = h.nextElementSibling;
                while (nextP && nextP.tagName !== 'P' && nextP.tagName !== 'DIV') {
                    nextP = nextP.nextElementSibling;
                }
                var text = nextP ? (nextP.textContent || '').trim() : 'Core syllabus topic.';
                if (text.length > 320) text = text.slice(0, 320) + '...';

                concepts.push({
                    id: 'rc_' + strHash(title),
                    title: title,
                    summary: text
                });
            });
        }

        return concepts;
    }

    function loadSavedRecallState() {
        try {
            var raw = localStorage.getItem(storageKey);
            return raw ? JSON.parse(raw) : {};
        } catch(e) {
            return {};
        }
    }

    function saveRecallState(state) {
        try {
            localStorage.setItem(storageKey, JSON.stringify(state));
        } catch(e) {}
    }

    function openQuickRecallTab() {
        // Hide other tab panes
        document.querySelectorAll('.tab-pane, .tab-content, .tab-panel').forEach(function(el) {
            el.classList.remove('active');
            if (el.id !== 'tab-quick-recall') {
                el.style.display = 'none';
            }
        });
        document.querySelectorAll('.tab-btn, .nav-tab, .branch-nav-btn').forEach(function(el) {
            el.classList.remove('active');
        });

        // Show Quick Recall
        var pane = document.getElementById('tab-quick-recall');
        if (pane) {
            pane.classList.add('active');
            pane.style.display = 'block';
            pane.scrollIntoView({ behavior: 'smooth' });
        }
        var btn = document.querySelector('.pushti-recall-tab-btn');
        if (btn) btn.classList.add('active');
    }

    function initQuickRecallChecklist() {
        // Only run on chapter pages with tab bars
        var tabBar = document.querySelector('.sidebar-nav, .tab-bar, .tab-list, .nav-tabs, .branch-nav');
        if (!tabBar) return;
        if (document.getElementById('tab-quick-recall')) return;

        recallItems = harvestChapterConcepts();
        if (recallItems.length === 0) return;

        var state = loadSavedRecallState();

        // 1. Inject Tab Button
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'tab-btn pushti-recall-tab-btn';
        btn.setAttribute('data-tab', 'tab-quick-recall');
        btn.setAttribute('title', 'Quick Recall Checklist: Active Recollection Engine');
        btn.innerHTML = '<span class="tab-icon-wrap"><i class="fas fa-clipboard-check" style="color:#10b981;"></i></span>' +
                        '<div class="tab-label-group"><span class="tab-label">Quick Recall Checklist</span>' +
                        '<span class="badge-recall">Active Recall</span></div>';

        btn.addEventListener('click', function(e) {
            e.preventDefault();
            openQuickRecallTab();
        });

        tabBar.appendChild(btn);

        // When any other tab is clicked, hide Quick Recall
        document.addEventListener('click', function(e) {
            var otherBtn = e.target.closest('.tab-btn, .nav-tab, .branch-nav-btn');
            if (otherBtn && !otherBtn.classList.contains('pushti-recall-tab-btn')) {
                var pane = document.getElementById('tab-quick-recall');
                if (pane) {
                    pane.classList.remove('active');
                    pane.style.display = 'none';
                }
                btn.classList.remove('active');
            }
        });

        // 2. Inject Tab Pane Container
        var contentWrapper = document.querySelector('.main-content, .tab-content-area, .content-container, main') || document.body;
        var pane = document.createElement('div');
        pane.id = 'tab-quick-recall';
        pane.className = 'tab-pane tab-content';

        contentWrapper.appendChild(pane);

        renderRecallPane(pane);
    }

    function renderRecallPane(pane) {
        var state = loadSavedRecallState();
        var total = recallItems.length;
        var masteredCount = 0;
        var reviewCount = 0;

        recallItems.forEach(function(item) {
            var s = state[item.id];
            if (s === 'mastered') masteredCount++;
            else if (s === 'review') reviewCount++;
        });

        var pct = total > 0 ? Math.round((masteredCount / total) * 100) : 0;

        var bannerHtml = '<div class="recall-banner">' +
                         '  <div class="recall-banner-top">' +
                         '    <div>' +
                         '      <h2 class="recall-title"><i class="fas fa-brain" style="color:#10b981;"></i> Quick Recall Checklist &amp; Summary Paper</h2>' +
                         '      <p style="font-size:0.88rem; color:var(--text-muted); margin:4px 0 0 0;">Test and recollect concepts in your head before peeking at notes. Concentrate on things flagged for quick look!</p>' +
                         '    </div>' +
                         '    <div class="recall-actions-bar">' +
                         '      <button class="recall-btn-action" onclick="window.print()" title="Print or Save as 1-Page PDF Summary Paper"><i class="fas fa-print"></i> Print Summary Paper</button>' +
                         '      <button class="recall-btn-action" id="btn-reset-recall" style="border-color:rgba(255,255,255,0.2); background:rgba(0,0,0,0.2); color:var(--text-muted);"><i class="fas fa-rotate-right"></i> Reset</button>' +
                         '    </div>' +
                         '  </div>' +
                         '  <div class="recall-progress-wrap">' +
                         '    <div style="display:flex; justify-content:space-between; font-size:0.8rem; font-weight:700; margin-bottom:4px;">' +
                         '      <span>Recollection Mastery</span><span>' + pct + '% Mastered</span>' +
                         '    </div>' +
                         '    <div class="recall-progress-bar-bg"><div class="recall-progress-fill" style="width:' + pct + '%;"></div></div>' +
                         '  </div>' +
                         '  <div class="recall-stats-pills">' +
                         '    <span class="recall-pill pill-all">Total: ' + total + '</span>' +
                         '    <span class="recall-pill pill-mastered"><i class="fas fa-check-circle"></i> Mastered: ' + masteredCount + '</span>' +
                         '    <span class="recall-pill pill-review"><i class="fas fa-triangle-exclamation"></i> Need Quick Look: ' + reviewCount + '</span>' +
                         '    <span class="recall-pill pill-untested">Unchecked: ' + (total - masteredCount - reviewCount) + '</span>' +
                         '  </div>' +
                         '</div>';

        var filterHtml = '<div class="recall-filter-bar">' +
                         '  <button class="recall-filter-btn ' + (recallFilter === 'all' ? 'active' : '') + '" data-filter="all">Show All (' + total + ')</button>' +
                         '  <button class="recall-filter-btn ' + (recallFilter === 'review' ? 'active' : '') + '" data-filter="review" style="color:#fbbf24;">⚠️ Need Quick Look (' + reviewCount + ')</button>' +
                         '  <button class="recall-filter-btn ' + (recallFilter === 'mastered' ? 'active' : '') + '" data-filter="mastered" style="color:#34d399;">✅ Mastered (' + masteredCount + ')</button>' +
                         '</div>';

        var itemsHtml = '<div class="recall-items-container">';
        recallItems.forEach(function(item, idx) {
            var itemState = state[item.id] || 'untested';
            if (recallFilter !== 'all' && recallFilter !== itemState) return;

            var cardClass = 'recall-item-card';
            var badgeText = 'Unchecked';
            var badgeClass = 'badge-untested';
            if (itemState === 'mastered') {
                cardClass += ' state-mastered';
                badgeText = '✅ Mastered';
                badgeClass = 'badge-mastered';
            } else if (itemState === 'review') {
                cardClass += ' state-review';
                badgeText = '⚠️ Need Quick Look';
                badgeClass = 'badge-review';
            }

            itemsHtml += '<div class="' + cardClass + '" id="card-' + item.id + '">' +
                         '  <div class="recall-item-top">' +
                         '    <div class="recall-item-title">' + (idx + 1) + '. ' + item.title + '</div>' +
                         '    <span class="recall-item-badge ' + badgeClass + '">' + badgeText + '</span>' +
                         '  </div>' +
                         '  <div class="recall-prompt">Can you recall the core definition, key rules, and formula for this in your head?</div>' +
                         '  <div class="recall-actions-row">' +
                         '    <div class="recall-btns-group">' +
                         '      <button class="recall-btn-state ' + (itemState === 'mastered' ? 'active-mastered' : '') + '" onclick="window.__setPushtiRecall(\'' + item.id + '\', \'mastered\')"><i class="fas fa-check"></i> I Know This</button>' +
                         '      <button class="recall-btn-state ' + (itemState === 'review' ? 'active-review' : '') + '" onclick="window.__setPushtiRecall(\'' + item.id + '\', \'review\')"><i class="fas fa-eye"></i> Need Quick Look</button>' +
                         '    </div>' +
                         '    <button class="recall-peek-btn" onclick="window.__togglePushtiPeek(\'' + item.id + '\')"><i class="fas fa-unlock"></i> Peek Answer</button>' +
                         '  </div>' +
                         '  <div class="recall-peek-answer" id="peek-' + item.id + '">' +
                         '    <strong>Key Summary:</strong> ' + item.summary +
                         '  </div>' +
                         '</div>';
        });
        itemsHtml += '</div>';

        pane.innerHTML = bannerHtml + filterHtml + itemsHtml;

        // Attach Filter listeners
        pane.querySelectorAll('.recall-filter-btn').forEach(function(fBtn) {
            fBtn.addEventListener('click', function() {
                recallFilter = fBtn.getAttribute('data-filter');
                renderRecallPane(pane);
            });
        });

        // Reset progress listener
        var resetBtn = pane.querySelector('#btn-reset-recall');
        if (resetBtn) {
            resetBtn.addEventListener('click', function() {
                if (confirm('Reset recall progress for this chapter?')) {
                    localStorage.removeItem(storageKey);
                    renderRecallPane(pane);
                }
            });
        }
    }

    // Global helper callbacks
    window.__setPushtiRecall = function(itemId, newState) {
        var state = loadSavedRecallState();
        if (state[itemId] === newState) {
            delete state[itemId];
        } else {
            state[itemId] = newState;
        }
        saveRecallState(state);
        var pane = document.getElementById('tab-quick-recall');
        if (pane) renderRecallPane(pane);
    };

    window.__togglePushtiPeek = function(itemId) {
        var box = document.getElementById('peek-' + itemId);
        if (box) box.classList.toggle('visible');
    };

    // --- 9. Initialization ---
    function init() {
        injectStyles();
        createStudyDock();
        initVoices();
        attachCardAudioButtons();
        initQuickRecallChecklist();

        // Re-attach card audio buttons when tabs change dynamically
        document.addEventListener('click', function (e) {
            if (e.target && e.target.closest('.tab-btn, .nav-tab, .submodule-btn, .branch-nav-btn')) {
                setTimeout(attachCardAudioButtons, 350);
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
