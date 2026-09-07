/**
 * Pushti Study Hub - Universal Jump to Top Engine
 * Mandate: Whenever a scroll bar appears on any page, a Jump to Top button must immediately appear.
 * Version: 1.1.0 - High Performance, Zero-Freeze Engine
 */
(function () {
    'use strict';

    if (window.__pushtiScrollToTopLoaded) return;
    window.__pushtiScrollToTopLoaded = true;

    var SCROLL_THRESHOLD = 80;
    var btn = null;
    var ticking = false;

    function injectStyles() {
        if (document.getElementById('pushti-jump-to-top-styles')) return;
        var style = document.createElement('style');
        style.id = 'pushti-jump-to-top-styles';
        style.textContent = [
            '.pushti-jump-to-top {',
            '    position: fixed;',
            '    bottom: 24px;',
            '    right: 24px;',
            '    width: 46px;',
            '    height: 46px;',
            '    border-radius: 50%;',
            '    background: linear-gradient(135deg, #6366f1, #8b5cf6);',
            '    color: #ffffff;',
            '    border: none;',
            '    outline: none;',
            '    display: flex;',
            '    align-items: center;',
            '    justify-content: center;',
            '    cursor: pointer;',
            '    box-shadow: 0 4px 18px rgba(99, 102, 241, 0.45), 0 2px 6px rgba(0, 0, 0, 0.15);',
            '    opacity: 0;',
            '    visibility: hidden;',
            '    transform: translateY(16px) scale(0.9);',
            '    transition: opacity 0.28s cubic-bezier(0.16, 1, 0.3, 1),',
            '                visibility 0.28s cubic-bezier(0.16, 1, 0.3, 1),',
            '                transform 0.28s cubic-bezier(0.16, 1, 0.3, 1),',
            '                box-shadow 0.2s ease,',
            '                background 0.2s ease;',
            '    z-index: 99999;',
            '    backdrop-filter: blur(8px);',
            '    -webkit-tap-highlight-color: transparent;',
            '}',
            '.pushti-jump-to-top.visible {',
            '    opacity: 1;',
            '    visibility: visible;',
            '    transform: translateY(0) scale(1);',
            '}',
            '.pushti-jump-to-top:hover {',
            '    background: linear-gradient(135deg, #4f46e5, #7c3aed);',
            '    box-shadow: 0 6px 22px rgba(99, 102, 241, 0.6), 0 3px 8px rgba(0, 0, 0, 0.2);',
            '    transform: translateY(-3px) scale(1.06);',
            '}',
            '.pushti-jump-to-top:active {',
            '    transform: translateY(0) scale(0.95);',
            '}',
            '.pushti-jump-to-top svg {',
            '    width: 22px;',
            '    height: 22px;',
            '    fill: none;',
            '    stroke: currentColor;',
            '    stroke-width: 2.6;',
            '    stroke-linecap: round;',
            '    stroke-linejoin: round;',
            '    transition: transform 0.2s ease;',
            '}',
            '.pushti-jump-to-top:hover svg {',
            '    transform: translateY(-2px);',
            '}',
            '@media (max-width: 640px) {',
            '    .pushti-jump-to-top {',
            '        bottom: 18px;',
            '        right: 18px;',
            '        width: 42px;',
            '        height: 42px;',
            '    }',
            '    .pushti-jump-to-top svg {',
            '        width: 19px;',
            '        height: 19px;',
            '    }',
            '}'
        ].join('\n');
        document.head.appendChild(style);
    }

    function createButton() {
        if (btn && document.body.contains(btn)) return;
        btn = document.getElementById('pushti-jump-to-top');
        if (!btn) {
            btn = document.createElement('button');
            btn.id = 'pushti-jump-to-top';
            btn.className = 'pushti-jump-to-top';
            btn.setAttribute('aria-label', 'Jump to top');
            btn.setAttribute('title', 'Jump to Top');
            btn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M12 19V5M5 12l7-7 7 7"></path></svg>';

            btn.addEventListener('click', function (e) {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: 'smooth' });
                var scrollableContainers = document.querySelectorAll('.topic-content, .main-content, main, .tab-pane, .subtopic-pane');
                scrollableContainers.forEach(function (el) {
                    if (el.scrollTop > 0) {
                        el.scrollTo({ top: 0, behavior: 'smooth' });
                    }
                });
            });

            document.body.appendChild(btn);
        }
    }

    function updateVisibility() {
        if (!btn) return;
        var scrollY = window.pageYOffset || (document.documentElement ? document.documentElement.scrollTop : 0) || (document.body ? document.body.scrollTop : 0) || 0;
        
        var isScrolled = scrollY > SCROLL_THRESHOLD;
        if (!isScrolled) {
            var scrollableContainers = document.querySelectorAll('.topic-content, .main-content, main, .tab-pane.active, .subtopic-pane.active');
            for (var i = 0; i < scrollableContainers.length; i++) {
                if (scrollableContainers[i].scrollTop > SCROLL_THRESHOLD) {
                    isScrolled = true;
                    break;
                }
            }
        }

        var currentlyVisible = btn.classList.contains('visible');
        if (isScrolled && !currentlyVisible) {
            btn.classList.add('visible');
        } else if (!isScrolled && currentlyVisible) {
            btn.classList.remove('visible');
        }
        ticking = false;
    }

    function requestTick() {
        if (!ticking) {
            ticking = true;
            window.requestAnimationFrame(updateVisibility);
        }
    }

    function init() {
        injectStyles();
        createButton();
        requestTick();

        window.addEventListener('scroll', requestTick, { passive: true });
        window.addEventListener('resize', requestTick, { passive: true });
        document.addEventListener('scroll', requestTick, { passive: true });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
