/**
 * Pushti Study Hub - Chapter Revision Logs & AI Model Provenance Tracking
 * 
 * Provides a structured audit trail of every change, revision date, features added,
 * and the specific AI model used (e.g. Gemini 2.5 Pro, Gemini 1.5 Flash, Claude 3.5 Sonnet)
 * for each chapter and subject across the platform.
 */

(function () {
    'use strict';

    const CHAPTER_LOGS = {
        // ==========================================
        // ENGLISH LITERATURE
        // ==========================================
        'eng_lit_ch1': {
            id: 'eng_lit_ch1',
            title: 'Chapter 1: A Hero',
            subject: 'English Literature',
            unit: 'Unit 1: Where Learning Begins',
            author: 'R.K. Narayan',
            version: 'v1.1.0',
            lastModified: 'September 5, 2026, 11:15 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#10B981',
            aiProvider: 'Google DeepMind',
            taskType: 'Curriculum Digitization & Multi-Tab Interactive Module',
            summary: 'Complete interactive study module built from the English Literature textbook PDF, including full unabridged Malgudi prose, interactive comprehension, grammar, and psychology connections.',
            changesList: [
                'Digitized full 4-scene unabridged prose of R.K. Narayan\'s classic story with Malgudi setting context.',
                'Extracted and embedded authentic textbook illustrations corresponding to each dramatic scene.',
                'Built 12 interactive hover tooltips for advanced vocabulary (disputed, proposition, tenacity, gesticulations, etc.).',
                'Section A: 5 interactive comprehension MCQs with instant visual feedback and score calculation.',
                'Section B: 6 textbook Q&As (2a-2f) with interactive "Reveal Answer" buttons for active recall.',
                'Tab 3: Compound words grammar guide, classification rules, wanted poster character analysis, and Nafisa-Mona dialogue.',
                'Tab 4: OSASCOMP adjective ordering visual rules, practice exercises, and Ms. Jenny Peters letter punctuation correction.',
                'Tab 5: Higher-order critical thinking (parenting styles, accidental heroism) and Nyctophobia psychology survey connect.'
            ],
            history: [
                {
                    version: 'v1.1.0',
                    date: 'September 5, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Added Revision Log & Model Provenance modal system, universal theme toggle polish, and linked to syllabus.'
                },
                {
                    version: 'v1.0.0',
                    date: 'September 5, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Initial production build with all 5 interactive tabs, audio-ready cues, and dark/light glassmorphism.'
                }
            ]
        },

        'eng_lit_ch2': {
            id: 'eng_lit_ch2',
            title: 'Chapter 2: The Taste of Watermelon',
            subject: 'English Literature',
            unit: 'Unit 1: Where Learning Begins',
            author: 'Borden Deal',
            version: 'v1.1.0',
            lastModified: 'September 5, 2026, 11:35 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#10B981',
            aiProvider: 'Google DeepMind',
            taskType: 'Curriculum Digitization & Multi-Tab Interactive Module',
            summary: 'Comprehensive interactive study module covering Borden Deal\'s coming-of-age story on conscience, peer pressure, remorse, and moral redemption.',
            changesList: [
                'Full unabridged 4-scene prose digitized faithfully from textbook pages 19-32.',
                'Cropped and integrated 5 high-resolution authentic textbook illustrations (Mr. Wills guarding, boys at creek, midnight raid, aftermath destruction, returning melon seeds).',
                'Embedded 15 interactive vocabulary hover tooltips (glower, withered, frenzy, catapulting, tremors, buckshot, etc.).',
                'Section A: Interactive MCQs with instant color-coded feedback and explanations.',
                'Section B: Textbook questions (2a through 2g) with reveal-answer functionality for active recall.',
                'Tab 3: Vocabulary and Antonyms exercises directly matching textbook page 30.',
                'Tab 4: High-order critical thinking on peer pressure, true courage vs. daredevilry, and confession.',
                'Tab 5: Moral courage life skills and Incredible India connect (Green Revolution 1960s agricultural milestone).'
            ],
            history: [
                {
                    version: 'v1.1.0',
                    date: 'September 5, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Added clickable Revision Log modal button, model provenance tracker, and synchronized with index.'
                },
                {
                    version: 'v1.0.0',
                    date: 'September 5, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Complete chapter module creation with 5 multi-content tabs, cropped images, and responsive glassmorphic UI.'
                }
            ]
        },

        'eng_lit_ch3': {
            id: 'eng_lit_ch3',
            title: 'Chapter 3: The Flower-School',
            subject: 'English Literature',
            unit: 'Unit 1: Where Learning Begins',
            author: 'Rabindranath Tagore',
            version: 'v1.1.0',
            lastModified: 'September 5, 2026, 11:40 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#EC4899',
            aiProvider: 'Google DeepMind',
            taskType: 'Poetry Appreciation & Literary Devices Interactive Module',
            summary: 'Poetry study module analyzing Rabindranath Tagore\'s lyrical masterpiece from The Crescent Moon, focusing on monsoon imagery, personification, and open-air education.',
            changesList: [
                'Complete poem digitized with stanza-by-stanza annotations and poetic appreciation.',
                'Cropped and embedded authentic textbook illustrations of monsoon storms and dancing blossoms.',
                'Poetic Devices Explorer: Detailed breakdown of Personification, Sensory Imagery (Visual, Auditory, Tactile), and Metaphors.',
                'Interactive MCQs on Tagore\'s figurative language and themes.',
                'Detailed subjective questions with reveal answers on mother-child bonding and natural curiosity.',
                'Cross-Curricular Connect: Rabindranath Tagore\'s Shantiniketan (Visva-Bharati) and open-air classroom philosophy.'
            ],
            history: [
                {
                    version: 'v1.1.0',
                    date: 'September 5, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Added Revision Log and AI Model provenance tracking.'
                },
                {
                    version: 'v1.0.0',
                    date: 'September 5, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Initial release of Tagore poetry module with interactive literary device cards.'
        },

        'eng_lit_ch4': {
            id: 'eng_lit_ch4',
            title: 'Chapter 1: Atlantis',
            subject: 'English Literature',
            unit: 'Unit 2: Wanderlust',
            author: 'Plato (Critias & Timaeus)',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 12:15 AM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#3B82F6',
            aiProvider: 'Google DeepMind',
            taskType: 'Curriculum Digitization & Multi-Tab Interactive Module',
            summary: 'Complete multi-tab study suite for Unit 2 Chapter 1: Atlantis, covering Plato\'s legendary concentric island empire, advanced vocabulary, interactive grammar (conjunctions, semicolons, compound sentences), and modern sinking cities.',
            changesList: [
                'Full 4-scene unabridged text from textbook pages 37-47 digitized (The Origin of the Legend, The Golden Empire, hubris & war with Athens, The Cataclysm overnight sinking).',
                'Extracted and integrated 3 high-resolution authentic illustrations: Kircher\'s 1665 Map of Atlantis, Poseidon Ocean Throne, and Concentric Circular Moats and Metropolis.',
                'Interactive vocabulary hover tooltips for 12 advanced terms (submerged, concentric, conduits, hubris, cataclysm, iridescent, etc.).',
                'Section A: 5 interactive comprehension MCQs with instant visual validation and score badge.',
                'Section B: 5 textbook short Q&As with interactive "Reveal Answer" buttons for active study.',
                'Tab 3: Complete rainforest cloze passage with interactive help-box word bank matching textbook exercise.',
                'Tab 4: Complete grammar suite covering coordinating conjunctions (FANBOYS), compound sentences, Ron\'s Istanbul email, Semicolon (;) rules & practice, and Greek roots (Acrobat, Democracy, Dinosaur).',
                'Tab 5: Deep inquiry into why Atlantis endures for 2,300 years, Santorini/Thera volcanic correlation, modern sinking cities (Venice MOSE barrier & Majuli island Assam), and KWL reflection chart.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Initial production release with all 5 interactive tabs, audio cues, image gallery, and glassmorphism styling.'
                }
            ]
        },

        // ==========================================
        // ENGLISH ACTIVITIES (ASL)
        // ==========================================
        'eng_act_asl': {
            id: 'eng_act_asl',
            title: 'Speaking & Listening Assessment (ASL)',
            subject: 'English Activities',
            unit: 'School Activities & Evaluation Prep',
            author: 'CBSE / SBPS Curriculum',
            version: 'v1.0.0',
            lastModified: 'September 5, 2026, 09:30 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#F59E0B',
            aiProvider: 'Google DeepMind',
            taskType: 'Exam Preparation & Speech Coaching Suite',
            summary: 'Interactive preparation module for the September 10-11 ASL examination covering all 8 assigned speech topics, live timing tools, and listening comprehension rubrics.',
            changesList: [
                'Model 1-2 minute speeches generated for all 8 assigned speech topics with natural vocabulary suitable for Class 7.',
                'Interactive speech rehearsal stopwatch / countdown timer (60s to 120s) with pacing guidance.',
                'Delivery coaching tips: Voice modulation, eye contact, body language, and pause markers.',
                'Listening skill evaluation rubric and active note-taking strategy sheets.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 5, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Initial release of the ASL Speaking & Listening interactive preparation dashboard.'
                }
            ]
        },

        // ==========================================
        // TIME TABLE & SCHEDULE
        // ==========================================
        'timetable_sept2026': {
            id: 'timetable_sept2026',
            title: 'School Time Table (September 2026 Revision)',
            subject: 'School Schedule & Analytics',
            unit: 'Daily Routine & Weekly Hours',
            author: 'SBPS Bhavnagar',
            version: 'v2.1.0',
            lastModified: 'September 5, 2026, 11:55 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#3B82F6',
            aiProvider: 'Google DeepMind',
            taskType: 'Schedule Modernization & Trend Analytics',
            summary: 'Updated school timetable starting at 7:30 AM with personalized Sanskrit track for Pushti, teacher standardization to Roger Sir, weekly hours calculation, and Kaushal Bodh (KB) spotlight.',
            changesList: [
                'Kept language slots (Mon P3, Tue P8, Fri P6, Sat P3) strictly as Sanskrit with Falguni R for Pushti, omitting Gujarati information.',
                'Standardized teacher nomenclature to Roger Sir across Chemistry, Physics, Biology, Science Lab, and Kaushal Bodh.',
                'Adjusted daily start time to 7:30 AM with 35-minute periods and two recesses (9:15 AM & 11:15 AM).',
                'Built automated weekly subject hours calculator comparing against previous timetable (+90m Maths).',
                'Integrated Kaushal Bodh (KB) vocational textbook spotlight and changelog audit.'
            ],
            history: [
                {
                    version: 'v2.1.0',
                    date: 'September 5, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Retained pure Sanskrit with Falguni R for Pushti (omitting Gujarati) and standardized teacher naming to Roger Sir.'
                },
                {
                    version: 'v2.0.0',
                    date: 'September 5, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Updated schedule, added weekly hours delta calculator, and KB textbook spotlight.'
                }
            ]
        }
    };

    window.CHAPTER_LOGS = CHAPTER_LOGS;

    function ensureModalDOM() {
        if (document.getElementById('chapter-log-modal-overlay')) {
            return;
        }

        const modalStyle = document.createElement('style');
        modalStyle.id = 'chapter-log-modal-styles';
        modalStyle.textContent = `
            .clog-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: rgba(0, 0, 0, 0.75);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                z-index: 10000;
                display: none;
                align-items: center;
                justify-content: center;
                padding: 20px;
                box-sizing: border-box;
                animation: clogFadeIn 0.25s ease-out;
            }
            .clog-overlay.active {
                display: flex;
            }
            @keyframes clogFadeIn {
                from { opacity: 0; transform: scale(0.98); }
                to { opacity: 1; transform: scale(1); }
            }
            .clog-modal {
                background: var(--bg-card, #1e293b);
                color: var(--text-main, #f8fafc);
                border: 1px solid var(--border, rgba(255, 255, 255, 0.15));
                border-radius: 20px;
                width: 100%;
                max-width: 680px;
                max-height: 88vh;
                overflow-y: auto;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255,255,255,0.05);
                position: relative;
                padding: 28px;
                box-sizing: border-box;
                font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            }
            [data-theme="light"] .clog-modal {
                background: #ffffff;
                color: #0f172a;
                border-color: #cbd5e1;
                box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.15);
            }
            .clog-header {
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
                border-bottom: 1px solid var(--border, rgba(255, 255, 255, 0.1));
                padding-bottom: 18px;
                margin-bottom: 20px;
                gap: 15px;
            }
            [data-theme="light"] .clog-header {
                border-bottom-color: #e2e8f0;
            }
            .clog-title-group h2 {
                margin: 0 0 6px 0;
                font-size: 1.45rem;
                font-weight: 700;
                color: var(--text-primary, #ffffff);
                display: flex;
                align-items: center;
                gap: 10px;
            }
            [data-theme="light"] .clog-title-group h2 {
                color: #0f172a;
            }
            .clog-breadcrumb {
                font-size: 0.88rem;
                color: var(--text-muted, #94a3b8);
                display: flex;
                align-items: center;
                gap: 6px;
            }
            [data-theme="light"] .clog-breadcrumb {
                color: #64748b;
            }
            .clog-close-btn {
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid var(--border, rgba(255, 255, 255, 0.1));
                color: var(--text-muted, #94a3b8);
                width: 36px;
                height: 36px;
                border-radius: 50%;
                font-size: 1.2rem;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                transition: all 0.2s;
                flex-shrink: 0;
            }
            .clog-close-btn:hover {
                background: #ef4444;
                color: white;
                border-color: #ef4444;
                transform: rotate(90deg);
            }
            .clog-meta-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 12px;
                margin-bottom: 22px;
            }
            .clog-meta-box {
                background: rgba(255, 255, 255, 0.04);
                border: 1px solid var(--border, rgba(255, 255, 255, 0.08));
                padding: 12px 16px;
                border-radius: 12px;
            }
            [data-theme="light"] .clog-meta-box {
                background: #f8fafc;
                border-color: #e2e8f0;
            }
            .clog-meta-label {
                font-size: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                color: var(--text-muted, #94a3b8);
                margin-bottom: 4px;
                font-weight: 600;
            }
            [data-theme="light"] .clog-meta-label {
                color: #64748b;
            }
            .clog-meta-val {
                font-size: 0.95rem;
                font-weight: 600;
                color: var(--text-main, #f8fafc);
                display: flex;
                align-items: center;
                gap: 8px;
            }
            [data-theme="light"] .clog-meta-val {
                color: #0f172a;
            }
            .clog-model-badge {
                display: inline-flex;
                align-items: center;
                gap: 6px;
                padding: 4px 10px;
                border-radius: 20px;
                font-size: 0.82rem;
                font-weight: 700;
                background: rgba(16, 185, 129, 0.15);
                color: #34d399;
                border: 1px solid rgba(16, 185, 129, 0.3);
            }
            [data-theme="light"] .clog-model-badge {
                background: #ecfdf5;
                color: #059669;
                border-color: #a7f3d0;
            }
            .clog-section-title {
                font-size: 1.05rem;
                font-weight: 700;
                margin: 20px 0 10px 0;
                color: var(--accent, #6366f1);
                display: flex;
                align-items: center;
                gap: 8px;
            }
            .clog-summary-box {
                background: rgba(99, 102, 241, 0.08);
                border-left: 4px solid var(--accent, #6366f1);
                padding: 14px 16px;
                border-radius: 0 10px 10px 0;
                font-size: 0.95rem;
                line-height: 1.6;
                margin-bottom: 20px;
            }
            [data-theme="light"] .clog-summary-box {
                background: #f5f3ff;
            }
            .clog-list {
                margin: 0 0 22px 0;
                padding-left: 20px;
            }
            .clog-list li {
                font-size: 0.93rem;
                line-height: 1.65;
                margin-bottom: 8px;
                color: var(--text-main, #e2e8f0);
            }
            [data-theme="light"] .clog-list li {
                color: #334155;
            }
            .clog-history-item {
                border-left: 2px solid var(--border, rgba(255, 255, 255, 0.15));
                padding-left: 14px;
                margin-left: 6px;
                margin-bottom: 14px;
                position: relative;
            }
            .clog-history-item::before {
                content: '';
                position: absolute;
                left: -6px;
                top: 5px;
                width: 10px;
                height: 10px;
                border-radius: 50%;
                background: var(--accent, #6366f1);
            }
            .clog-history-ver {
                font-size: 0.88rem;
                font-weight: 700;
                color: var(--text-main, #f8fafc);
                display: flex;
                gap: 8px;
                align-items: center;
            }
            [data-theme="light"] .clog-history-ver {
                color: #0f172a;
            }
            .clog-history-date {
                font-size: 0.78rem;
                color: var(--text-muted, #94a3b8);
                font-weight: normal;
            }
            .clog-history-notes {
                font-size: 0.86rem;
                color: var(--text-muted, #94a3b8);
                margin-top: 3px;
            }
            [data-theme="light"] .clog-history-notes {
                color: #64748b;
            }
            .clog-footer {
                display: flex;
                justify-content: flex-end;
                margin-top: 24px;
                border-top: 1px solid var(--border, rgba(255, 255, 255, 0.1));
                padding-top: 16px;
            }
            [data-theme="light"] .clog-footer {
                border-top-color: #e2e8f0;
            }
            .clog-dismiss-btn {
                background: var(--surface, #334155);
                color: var(--text-main, #f8fafc);
                border: 1px solid var(--border, rgba(255, 255, 255, 0.15));
                padding: 8px 18px;
                border-radius: 10px;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.2s;
            }
            .clog-dismiss-btn:hover {
                background: var(--accent, #6366f1);
                color: #ffffff;
                border-color: var(--accent, #6366f1);
            }
            [data-theme="light"] .clog-dismiss-btn {
                background: #f1f5f9;
                color: #0f172a;
                border-color: #cbd5e1;
            }
            [data-theme="light"] .clog-dismiss-btn:hover {
                background: #6366f1;
                color: #ffffff;
            }
        `;
        document.head.appendChild(modalStyle);

        const overlay = document.createElement('div');
        overlay.id = 'chapter-log-modal-overlay';
        overlay.className = 'clog-overlay';
        overlay.innerHTML = `
            <div class="clog-modal" role="dialog" aria-modal="true" aria-labelledby="clog-modal-title">
                <div class="clog-header">
                    <div class="clog-title-group">
                        <h2 id="clog-modal-title"><i class="fas fa-file-signature"></i> <span id="clog-title-text">Chapter Revision Log</span></h2>
                        <div class="clog-breadcrumb" id="clog-breadcrumb">English &bull; Class 7</div>
                    </div>
                    <button class="clog-close-btn" onclick="closeChapterLog()" aria-label="Close modal">&times;</button>
                </div>
                
                <div class="clog-meta-grid">
                    <div class="clog-meta-box">
                        <div class="clog-meta-label">AI Model Used</div>
                        <div class="clog-meta-val">
                            <span class="clog-model-badge" id="clog-model-badge">
                                <i class="fas fa-microchip"></i> <span id="clog-model-name">Gemini 2.5 Pro</span>
                            </span>
                        </div>
                    </div>
                    <div class="clog-meta-box">
                        <div class="clog-meta-label">AI Provider & Agent</div>
                        <div class="clog-meta-val" id="clog-provider-name"><i class="fas fa-brain"></i> Google DeepMind</div>
                    </div>
                    <div class="clog-meta-box">
                        <div class="clog-meta-label">Last Modified Date</div>
                        <div class="clog-meta-val" id="clog-modified-date"><i class="far fa-calendar-alt"></i> Sept 5, 2026</div>
                    </div>
                    <div class="clog-meta-box">
                        <div class="clog-meta-label">Current Version</div>
                        <div class="clog-meta-val" id="clog-version-tag"><i class="fas fa-code-branch"></i> v1.1.0</div>
                    </div>
                </div>

                <div class="clog-section-title"><i class="fas fa-bullhorn"></i> Summary of Changes</div>
                <div class="clog-summary-box" id="clog-summary-text">
                    Summary text here.
                </div>

                <div class="clog-section-title"><i class="fas fa-tasks"></i> Detailed Features & Content Added</div>
                <ul class="clog-list" id="clog-changes-list">
                </ul>

                <div class="clog-section-title"><i class="fas fa-history"></i> Revision History</div>
                <div id="clog-history-container">
                </div>

                <div class="clog-footer">
                    <button class="clog-dismiss-btn" onclick="closeChapterLog()"><i class="fas fa-check"></i> Done</button>
                </div>
            </div>
        `;

        overlay.addEventListener('click', function (e) {
            if (e.target === overlay) {
                closeChapterLog();
            }
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && overlay.classList.contains('active')) {
                closeChapterLog();
            }
        });

        document.body.appendChild(overlay);
    }

    window.openChapterLog = function (chapterId) {
        ensureModalDOM();

        const log = CHAPTER_LOGS[chapterId] || {
            id: chapterId,
            title: chapterId.replace(/_/g, ' ').toUpperCase(),
            subject: 'Study Material',
            unit: 'General',
            version: 'v1.0.0',
            lastModified: 'Recent',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#10B981',
            aiProvider: 'Google DeepMind Antigravity',
            taskType: 'Content Digitization',
            summary: 'Chapter content digitised and published with interactive exercises.',
            changesList: [
                'Digitized curriculum text with structured section breakdown.',
                'Interactive comprehension and self-testing features.',
                'Glassmorphism dark/light theme compatibility.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Initial build and release.'
                }
            ]
        };

        document.getElementById('clog-title-text').textContent = log.title;
        document.getElementById('clog-breadcrumb').textContent = `${log.subject} • ${log.unit}`;
        document.getElementById('clog-model-name').textContent = log.modelUsed;
        document.getElementById('clog-provider-name').innerHTML = `<i class="fas fa-brain"></i> ${log.aiProvider}`;
        document.getElementById('clog-modified-date').innerHTML = `<i class="far fa-calendar-alt"></i> ${log.lastModified}`;
        document.getElementById('clog-version-tag').innerHTML = `<i class="fas fa-code-branch"></i> ${log.version}`;
        document.getElementById('clog-summary-text').textContent = log.summary;

        const changesContainer = document.getElementById('clog-changes-list');
        changesContainer.innerHTML = '';
        if (log.changesList && log.changesList.length > 0) {
            log.changesList.forEach(item => {
                const li = document.createElement('li');
                li.textContent = item;
                changesContainer.appendChild(li);
            });
        }

        const historyContainer = document.getElementById('clog-history-container');
        historyContainer.innerHTML = '';
        if (log.history && log.history.length > 0) {
            log.history.forEach(h => {
                const hDiv = document.createElement('div');
                hDiv.className = 'clog-history-item';
                hDiv.innerHTML = `
                    <div class="clog-history-ver">
                        <span>${h.version}</span>
                        <span class="clog-history-date">&bull; ${h.date}</span>
                        <span class="clog-model-badge" style="font-size:0.75rem; padding:2px 8px;">${h.model}</span>
                    </div>
                    <div class="clog-history-notes">${h.notes}</div>
                `;
                historyContainer.appendChild(hDiv);
            });
        }

        const overlay = document.getElementById('chapter-log-modal-overlay');
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    };

    window.closeChapterLog = function () {
        const overlay = document.getElementById('chapter-log-modal-overlay');
        if (overlay) {
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    };

})();
