/**
 * Pushti Study Hub - Precision Study Tools Engine
 * Version: 3.0.0 (Clean Top-Bar Fullscreen + Substantive Text-to-Speech)
 * Compliant with SOP v3.5 & Urban Hath Fero Standards.
 * Features:
 *   1. Fullscreen & Landscape Lock integrated cleanly onto the Top Bar (near Time Table / Mid-Term).
 *   2. Natural "Read Out Loud" (TTS) Indian voice engine attached ONLY to substantive text blocks (>= 140 chars).
 *   3. Zero bottom dock clutter (no bottom floating bar).
 *   4. Zero dependencies, pure vanilla JS, 100% offline & local file:// compatible.
 */

(function () {
    'use strict';

    if (window.__pushtiStudyToolsLoaded) return;
    window.__pushtiStudyToolsLoaded = true;

    // --- State Variables ---
    var isSpeaking = false;
    var currentActiveEl = null;
    var currentBtn = null;
    var availableVoices = [];
    var selectedVoice = null;
    var isHindiPage = document.documentElement.lang === 'hi' || 
                      window.location.pathname.indexOf('/hindi/') !== -1 ||
                      document.title.indexOf('Hindi') !== -1 ||
                      document.title.indexOf('हिन्दी') !== -1;

    // --- 1. CSS Ingestion ---
    function injectStyles() {
        if (document.getElementById('pushti-study-tools-styles')) return;
        var style = document.createElement('style');
        style.id = 'pushti-study-tools-styles';
        style.textContent = [
            '/* Top Bar Fullscreen Button */',
            '.pushti-topbar-fs-btn {',
            '    display: inline-flex;',
            '    align-items: center;',
            '    gap: 7px;',
            '    padding: 6px 14px;',
            '    border-radius: 9999px;',
            '    background: rgba(99, 102, 241, 0.12);',
            '    border: 1px solid rgba(99, 102, 241, 0.35);',
            '    color: #a5b4fc;',
            '    font-family: inherit;',
            '    font-size: 0.82rem;',
            '    font-weight: 600;',
            '    cursor: pointer;',
            '    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);',
            '    outline: none;',
            '    text-decoration: none;',
            '    user-select: none;',
            '    -webkit-tap-highlight-color: transparent;',
            '}',
            '[data-theme="light"] .pushti-topbar-fs-btn {',
            '    background: rgba(99, 102, 241, 0.08);',
            '    border-color: rgba(99, 102, 241, 0.3);',
            '    color: #4f46e5;',
            '}',
            '.pushti-topbar-fs-btn:hover {',
            '    background: #6366f1;',
            '    color: #ffffff !important;',
            '    border-color: #6366f1;',
            '    transform: translateY(-1px);',
            '    box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35);',
            '}',
            '.pushti-topbar-fs-btn:active { transform: translateY(0) scale(0.96); }',
            '.pushti-topbar-fs-btn i { font-size: 0.85rem; }',
            '',
            '/* Substantive Text Speaker Button */',
            '.pushti-tts-speaker-btn {',
            '    display: inline-flex;',
            '    align-items: center;',
            '    justify-content: center;',
            '    width: 28px;',
            '    height: 28px;',
            '    border-radius: 50%;',
            '    border: 1px solid rgba(139, 92, 246, 0.3);',
            '    background: rgba(139, 92, 246, 0.1);',
            '    color: #c4b5fd;',
            '    cursor: pointer;',
            '    transition: all 0.2s ease;',
            '    vertical-align: middle;',
            '    margin-left: 8px;',
            '    flex-shrink: 0;',
            '    outline: none;',
            '}',
            '[data-theme="light"] .pushti-tts-speaker-btn {',
            '    background: rgba(99, 102, 241, 0.08);',
            '    border-color: rgba(99, 102, 241, 0.25);',
            '    color: #6366f1;',
            '}',
            '.pushti-tts-speaker-btn:hover {',
            '    background: #6366f1;',
            '    color: #ffffff !important;',
            '    border-color: #6366f1;',
            '    transform: scale(1.1);',
            '    box-shadow: 0 2px 10px rgba(99, 102, 241, 0.4);',
            '}',
            '.pushti-tts-speaker-btn.speaking {',
            '    background: #10b981 !important;',
            '    color: #ffffff !important;',
            '    border-color: #10b981 !important;',
            '    animation: pushtiSpeakerPulse 1.4s infinite;',
            '}',
            '@keyframes pushtiSpeakerPulse {',
            '    0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.6); }',
            '    70% { box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }',
            '    100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }',
            '}',
            '.pushti-tts-reading-target {',
            '    outline: 2px solid rgba(139, 92, 246, 0.7) !important;',
            '    outline-offset: 3px;',
            '    border-radius: 8px;',
            '    transition: outline 0.2s ease;',
            '}',
            '',
            '/* Universal Tablet & Landscape/Portrait Dock Rail Guardrails */',
            '@media (min-width: 640px) and (max-width: 1099px) {',
            '    .sidebar-dock, .sidebar {',
            '        width: 62px !important;',
            '        position: fixed !important;',
            '        left: 0 !important;',
            '        top: 54px !important;',
            '        bottom: 0 !important;',
            '        z-index: 900 !important;',
            '    }',
            '    .sidebar-dock.pinned, .sidebar.pinned { width: 62px !important; }',
            '    .sidebar-dock .tab-label-group, .sidebar .tab-label-group { display: none !important; }',
            '    .sidebar-dock .sidebar-footer, .sidebar .sidebar-footer, .sidebar .pin-btn { display: none !important; }',
            '    .main-app-content, .main-content {',
            '        margin-left: 62px !important;',
            '        width: calc(100% - 62px) !important;',
            '        max-width: min(1600px, calc(100vw - 62px)) !important;',
            '        box-sizing: border-box !important;',
            '        padding-left: 1.5rem !important;',
            '        padding-right: 1.5rem !important;',
            '    }',
            '}',
            '',
            '@media (min-width: 1100px) {',
            '    .sidebar-dock, .sidebar {',
            '        width: 62px;',
            '        position: fixed;',
            '        left: 0;',
            '        top: 54px;',
            '        bottom: 0;',
            '        z-index: 900;',
            '    }',
            '    .main-app-content, .main-content {',
            '        margin-left: 62px !important;',
            '        width: calc(100% - 62px) !important;',
            '        max-width: min(1600px, calc(100vw - 62px)) !important;',
            '        box-sizing: border-box !important;',
            '        padding-left: 2rem !important;',
            '        padding-right: 2rem !important;',
            '        transition: margin-left 0.3s cubic-bezier(0.4, 0, 0.2, 1), width 0.3s cubic-bezier(0.4, 0, 0.2, 1);',
            '    }',
            '    .sidebar-dock.pinned, .sidebar.pinned { width: 280px !important; }',
            '    .sidebar-dock.pinned ~ .main-app-content, .sidebar.pinned ~ .main-content {',
            '        margin-left: 280px !important;',
            '        width: calc(100% - 280px) !important;',
            '        max-width: min(1600px, calc(100vw - 280px)) !important;',
            '    }',
            '    .sidebar-dock:hover .tab-label-group, .sidebar-dock.pinned .tab-label-group,',
            '    .sidebar:hover .tab-label-group, .sidebar.pinned .tab-label-group {',
            '        display: flex !important;',
            '        width: auto !important;',
            '        min-width: 140px !important;',
            '        max-width: 200px !important;',
            '        margin-left: 12px !important;',
            '        opacity: 1 !important;',
            '        pointer-events: auto !important;',
            '    }',
            '}',
            '',
            '@media (max-width: 639px) {',
            '    .flex.flex-1.relative, .app-layout { flex-direction: column !important; }',
            '    .sidebar-dock, .sidebar {',
            '        position: sticky !important;',
            '        top: 54px !important;',
            '        left: 0 !important;',
            '        right: 0 !important;',
            '        width: 100% !important;',
            '        height: 48px !important;',
            '        max-height: 48px !important;',
            '        min-height: 48px !important;',
            '        flex-direction: row !important;',
            '        border-right: none !important;',
            '        border-bottom: 1px solid rgba(51, 65, 85, 0.7) !important;',
            '        padding: 4px 6px !important;',
            '        overflow-x: auto !important;',
            '        overflow-y: hidden !important;',
            '        -webkit-overflow-scrolling: touch !important;',
            '        z-index: 850 !important;',
            '    }',
            '    .sidebar-dock > div:first-child, .sidebar .sidebar-tabs {',
            '        display: flex !important;',
            '        flex-direction: row !important;',
            '        flex-wrap: nowrap !important;',
            '        gap: 6px !important;',
            '        width: 100% !important;',
            '        padding: 0 !important;',
            '        overflow-x: auto !important;',
            '        overflow-y: hidden !important;',
            '    }',
            '    .sidebar-dock .nav-tab-btn, .sidebar .tab-btn {',
            '        width: auto !important;',
            '        height: 40px !important;',
            '        padding: 4px 10px !important;',
            '        flex-shrink: 0 !important;',
            '    }',
            '    .sidebar-dock .tab-label-group, .sidebar .tab-label-group { display: none !important; }',
            '    .sidebar-dock .sidebar-footer, .sidebar .sidebar-footer, .sidebar .pin-btn { display: none !important; }',
            '    .main-app-content, .main-content {',
            '        margin-left: 0 !important;',
            '        width: 100% !important;',
            '        max-width: 100% !important;',
            '        padding: 14px !important;',
            '    }',
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

    // --- 4. TTS Execution ---
    function stopSpeaking() {
        if (window.PushtiOnlineTTS) {
            window.PushtiOnlineTTS.stop();
        }
        if ('speechSynthesis' in window && window.speechSynthesis.speaking) {
            window.speechSynthesis.cancel();
        }
        isSpeaking = false;
        if (currentBtn) {
            currentBtn.classList.remove('speaking');
            currentBtn.innerHTML = '<i class="fas fa-volume-high"></i>';
            currentBtn = null;
        }
        if (currentActiveEl) {
            currentActiveEl.classList.remove('pushti-tts-reading-target');
            currentActiveEl = null;
        }
    }

    function speakTargetText(rawText, containerEl, btnEl) {
        // If clicking on already speaking button, toggle stop
        if (isSpeaking && currentBtn === btnEl) {
            stopSpeaking();
            return;
        }

        stopSpeaking();

        var text = sanitizeTextForSpeech(rawText);
        if (!text) return;

        currentActiveEl = containerEl;
        currentBtn = btnEl;

        // Use Online Cloud Audio TTS if available
        if (window.PushtiOnlineTTS) {
            isSpeaking = true;
            window.PushtiOnlineTTS.speak(text, {
                lang: isHindiPage ? 'hi' : 'en',
                btn: btnEl,
                targetEl: containerEl,
                onComplete: function () {
                    stopSpeaking();
                }
            });
            return;
        }

        // Fallback to Web Speech API
        if (!('speechSynthesis' in window)) {
            alert('Speech Synthesis is not supported in this browser.');
            return;
        }

        if (currentActiveEl) currentActiveEl.classList.add('pushti-tts-reading-target');
        if (currentBtn) {
            currentBtn.classList.add('speaking');
            currentBtn.innerHTML = '<i class="fas fa-stop"></i>';
        }

        var utter = new SpeechSynthesisUtterance(text);
        if (selectedVoice) utter.voice = selectedVoice;
        utter.rate = 1.0;
        utter.pitch = 1.0;

        utter.onstart = function () {
            isSpeaking = true;
        };

        utter.onend = function () {
            stopSpeaking();
        };

        utter.onerror = function () {
            stopSpeaking();
        };

        window.speechSynthesis.speak(utter);
    }

    // --- 5. Fullscreen & Landscape Lock ---
    function toggleFullscreenLandscape() {
        var doc = window.document;
        var docEl = doc.documentElement;

        var isFs = doc.fullscreenElement || doc.mozFullScreenElement || doc.webkitFullscreenElement || doc.msFullscreenElement;

        if (!isFs) {
            var requestFs = docEl.requestFullscreen || docEl.mozRequestFullScreen || docEl.webkitRequestFullScreen || docEl.msRequestFullscreen;
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
            var cancelFs = doc.exitFullscreen || doc.mozCancelFullScreen || doc.webkitExitFullscreen || doc.msExitFullscreen;
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
        var btn = document.getElementById('pushti-topbar-fs-btn');
        if (btn) {
            if (isFs) {
                btn.innerHTML = '<i class="fas fa-compress"></i> <span>Exit Fullscreen</span>';
                btn.setAttribute('title', 'Exit Fullscreen Mode');
            } else {
                btn.innerHTML = '<i class="fas fa-expand"></i> <span>Fullscreen</span>';
                btn.setAttribute('title', 'Enter Fullscreen & Landscape Mode');
            }
        }
    }

    // --- 6. Top Bar Fullscreen Button Injection ---
    function injectTopBarFullscreenButton() {
        if (document.getElementById('pushti-topbar-fs-btn')) return;

        // Try to anchor right next to Time Table, Mid-Term, Theme Toggle, or Header Nav
        var anchor = document.querySelector('.header-nav a[href*="timetable"], .site-header a[href*="timetable"], a[href*="timetable"], a[href*="midterm"], .header-nav .theme-toggle, .site-header .theme-toggle, .theme-toggle, .user-profile-wrapper');

        var fsBtn = document.createElement('button');
        fsBtn.type = 'button';
        fsBtn.id = 'pushti-topbar-fs-btn';
        fsBtn.className = 'pushti-topbar-fs-btn';
        fsBtn.title = 'Enter Fullscreen & Landscape Mode (Tablet/Laptop)';
        fsBtn.innerHTML = '<i class="fas fa-expand"></i> <span>Fullscreen</span>';
        fsBtn.addEventListener('click', toggleFullscreenLandscape);

        if (anchor && anchor.parentNode) {
            anchor.parentNode.insertBefore(fsBtn, anchor);
        } else {
            var targetContainer = document.querySelector('.header-nav, .nav-actions, .header-actions, .header-right, .top-nav, .site-header, header');
            if (targetContainer) {
                targetContainer.appendChild(fsBtn);
            }
        }

        document.addEventListener('fullscreenchange', updateFullscreenUI);
        document.addEventListener('webkitfullscreenchange', updateFullscreenUI);
        document.addEventListener('mozfullscreenchange', updateFullscreenUI);
        document.addEventListener('MSFullscreenChange', updateFullscreenUI);
    }

    // --- 7. Substantive Text Speaker Injection (Only text >= 140 chars) ---
    function attachSpeakerButtons() {
        var MIN_TEXT_LENGTH = 140;

        var candidates = document.querySelectorAll(
            'main p, .tab-content p, article p, section p, ' +
            '.concept-card, .rule-box, .formula-card, .formula-box, .key-point, ' +
            '.note-card, .theory-card, .illustration-card, .summary-box, .concept-block, ' +
            '.subtopic-pane > p, .unit-card'
        );

        candidates.forEach(function (el) {
            // Ignore headers, footers, navigation, modals, search dropdowns, quizzes, flashcards
            if (el.closest('header, nav, aside, footer, #globalSearchDropdown, .modal, .quiz-box, .flashcard')) return;
            if (el.querySelector('.pushti-tts-speaker-btn') || el.classList.contains('pushti-tts-processed')) return;
            
            // DEDUPLICATION: check if the parent container already has an explicit TTS button or speak trigger
            var parentCard = el.closest('.group, .p-4, .p-5, .p-6, .rounded-xl, .rounded-2xl, .card, article, section, div[class*="border"]');
            if (parentCard) {
                var existingBtn = parentCard.querySelector('button[onclick*="speak"], button[onclick*="tts"], button[class*="speak"], [class*="fa-volume"], [class*="fa-headphones"]');
                if (existingBtn && !existingBtn.classList.contains('pushti-tts-speaker-btn')) {
                    el.classList.add('pushti-tts-processed');
                    return;
                }
            }

            var rawText = (el.innerText || el.textContent || '').trim();
            if (rawText.length < MIN_TEXT_LENGTH) return;

            el.classList.add('pushti-tts-processed');

            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'pushti-tts-speaker-btn';
            btn.innerHTML = '<i class="fas fa-volume-high"></i>';
            btn.setAttribute('title', 'Listen to this section');

            btn.addEventListener('click', function (e) {
                e.stopPropagation();
                speakTargetText(rawText, el, btn);
            });

            var headerEl = el.querySelector('h2, h3, h4, h5, strong, .concept-title, .rule-title');
            if (headerEl) {
                headerEl.appendChild(btn);
            } else {
                el.appendChild(btn);
            }
        });

        // Cleanup sweep: remove any accidentally injected buttons inside containers that already possess an explicit speaker button
        var allInjected = document.querySelectorAll('.pushti-tts-speaker-btn');
        allInjected.forEach(function (btn) {
            var parent = btn.closest('.group, .p-4, .p-5, .p-6, .rounded-xl, .card, article, section, div[class*="border"]');
            if (parent) {
                var manualBtns = parent.querySelectorAll('button[onclick*="speak"], button[onclick*="tts"]');
                if (manualBtns.length > 0) {
                    btn.remove();
                }
            }
        });
    }

    // --- 8. Tablet & Mobile Responsive Guardrails ---
    function enforceTabletDockContainment() {
        if (window.innerWidth < 1100) {
            var docks = document.querySelectorAll('.sidebar-dock, .sidebar');
            docks.forEach(function(d) {
                d.classList.remove('pinned');
            });
        }
    }

    // --- 9. Initialization ---
    function init() {
        injectStyles();
        initVoices();
        injectTopBarFullscreenButton();
        attachSpeakerButtons();
        enforceTabletDockContainment();

        window.addEventListener('resize', enforceTabletDockContainment);
        window.addEventListener('orientationchange', function() {
            setTimeout(enforceTabletDockContainment, 100);
        });

        // Safety retry for delayed DOM rendering
        setTimeout(function() {
            injectTopBarFullscreenButton();
            attachSpeakerButtons();
            enforceTabletDockContainment();
        }, 150);

        // Refresh buttons when tabs or modules change dynamically
        document.addEventListener('click', function (e) {
            if (e.target && e.target.closest('.tab-btn, .nav-tab, .nav-item, .subtopic-pill, .branch-nav-btn')) {
                setTimeout(attachSpeakerButtons, 300);
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
