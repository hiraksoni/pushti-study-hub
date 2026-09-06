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
        },

        'eng_lit_ch5': {
            id: 'eng_lit_ch5',
            title: 'Chapter 2: The Diary of a Space Traveller',
            subject: 'English Literature',
            unit: 'Unit 2: Wanderlust',
            author: 'Satyajit Ray',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 12:20 AM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#38BDF8',
            aiProvider: 'Google DeepMind',
            taskType: 'Curriculum Digitization & Multi-Tab Interactive Module',
            summary: 'Complete multi-tab study suite for Unit 2 Chapter 2: The Diary of a Space Traveller by Satyajit Ray, featuring Professor Shonku, Prahlad, robot Bidhushekhar, cat Newton, Martian monsters, planet Tafa, travel itinerary writing, and ISRO achievements.',
            changesList: [
                'Full unabridged text digitized covering prologue, January 2-28 diary entries, Martian landing, one-eyed monster pursuit, celestial bursting spheres, planet Tafa sanctuary, and hungry black ants epilogue.',
                'Cropped and integrated 4 authentic textbook illustrations (rocket blastoff, Bidhushekhar saying Goh! Goh!, Shonku on Martian yellow mound with cat Newton, and Shonku & Bidhushekhar at porthole window).',
                'Interactive vocabulary hover tooltips for 12 key terms (ebbing, venture, luminous, ambrosia, fatigue, eerie, glistening, primitive, etc.).',
                'Comprehension suite: Virgin Galactic VSS Unity reading passage + 5 interactive self-scoring MCQs with Web Audio feedback.',
                'Section B: 6 textbook short Q&As with "Reveal Answer" buttons + comprehensive Mars vs Tafa comparative matrix.',
                'Tab 3: Travel vocabulary cloze passage with interactive validation, score calculation, and advanced glossary.',
                'Tab 4: 2-day Delhi & Agra cultural heritage itinerary model, itinerary writing checklist, and airport lounge dialogue roleplay.',
                'Tab 5: Literary analysis of Foreshadowing, 11 real-world independent travel safety protocols, and Incredible India spotlight on ISRO (Mangalyaan, Chandrayaan-3, PSLV-C37).'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Initial production release with all 5 interactive tabs, audio cues, image gallery, and glassmorphic UI.'
        },

        'eng_lit_ch6': {
            id: 'eng_lit_ch6',
            title: 'Chapter 3: The Lake Isle of Innisfree',
            subject: 'English Literature',
            unit: 'Unit 2: Wanderlust',
            author: 'William Butler Yeats',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 12:25 AM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#10B981',
            aiProvider: 'Google DeepMind',
            taskType: 'Poetry Appreciation & Literary Analysis Interactive Module',
            summary: 'Complete interactive study suite for W.B. Yeats\'s lyrical masterpiece The Lake Isle of Innisfree, covering stanza-by-stanza annotations, visual and auditory sensory imagery, the "I will arise and go now" refrain, travel postcard art, and nature ecotherapy.',
            changesList: [
                'Full 3-stanza lyrical poem digitized with line-by-line paraphrase, audio rhythm guide, and ABAB CDCD EFEF rhyme scheme breakdown.',
                'Cropped and integrated 2 authentic illustrations: the tranquil clay-and-wattles cabin on Lough Gill and Paris/London typography travel postcards.',
                'Interactive vocabulary hover tooltips for 10 key poetic words (Innisfree, wattles, bean-rows, glade, veils of the morning, glimmer, purple glow, linnet, lapping, deep heart\'s core).',
                'Poem Appreciation MCQs (3 textbook questions on city escape, tranquility, and holistic nature routines).',
                'Section 2: 5 textbook short Q&As with "Reveal Answer" buttons on London vs Innisfree contrast, cabin architecture, country nostalgia, and the literary function of the Refrain.',
                'Tab 3: Complete Visual vs Auditory Imagery comparative matrix from textbook page 60 + detailed exploration of alliteration, metaphor, and onomatopoeia.',
                'Tab 4: Art Corner on travel postcards as cultural souvenirs + Bhavnagar landmark design challenge.',
                'Tab 5: Experiential Learning connecting Lough Gill in County Sligo with modern neuroscience of Shinrin-yoku (forest bathing) and mental peace.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Initial production release with 5 interactive tabs, audio cues, image integration, and glassmorphic UI.'
                }
            ]
        },

        'eng_lit_ch7': {
            id: 'eng_lit_ch7',
            title: 'Chapter 1: The One Who Survived: Ada Blackjack',
            subject: 'English Literature',
            unit: 'Unit 3: Real-Life Heroes',
            author: 'Biographical Narrative / Iñupiat History',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 12:35 AM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#0D9488',
            aiProvider: 'Google DeepMind',
            taskType: 'Graphic Novel & Narrative Digitization',
            summary: 'Complete multi-tab study suite for Unit 3 Chapter 1: The One Who Survived: Ada Blackjack, chronicling her two-year heroic solitary survival on Arctic Wrangel Island to cure her son Bennett, Shackleton synonyms, transitive verbs grammar, and Indian women pioneers.',
            changesList: [
                'Full 5-scene graphic narrative digitized covering Alaska origins, Bennett\'s illness, voyage on the Silverwave, scurvy epidemic, Lorne Knight\'s nursing, solitary survival, and rescue by the Donaldson.',
                'Cropped and integrated 4 authentic illustrations (Silverwave ship, Arctic campfire in snowhouse, Donaldson rescue, and international press headlines).',
                'Interactive vocabulary hover tooltips for 12 key terms (scurvy, colonize, dwindling, umiak, expedition, seamstress, Chukchi Sea, etc.).',
                'Three Stages of Ada\'s Life comparative matrix + 5 detailed textbook short Q&As with "Reveal Answer" buttons.',
                'Tab 3: Synonyms cloze passage on Sir Ernest Shackleton\'s Trial by Ice with interactive validation and scoring.',
                'Tab 4: Complete grammar suite on Transitive vs Intransitive verbs, direct vs indirect objects, and syllabic consonants (/l/, /n/, /m/).',
                'Tab 5: 3 real-world survival stories, 8-item wilderness kit builder, and Incredible India spotlight on women trailblazers (Bachendri Pal, Arunima Sinha, Capt. Shiva Chouhan, Bhawana Kanth).'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Initial production release with all 5 interactive tabs, audio cues, image integration, and glassmorphic UI.'
                }
            ]
        },

        'eng_lit_ch8': {
            id: 'eng_lit_ch8',
            title: 'Chapter 2: The Narayanpur Incident',
            subject: 'English Literature',
            unit: 'Unit 3: Real-Life Heroes',
            author: 'Shashi Deshpande',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 01:20 AM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#F59E0B',
            aiProvider: 'Google DeepMind',
            taskType: 'Historical Fiction & Freedom Movement Digitization',
            summary: 'Complete multi-tab study suite for Unit 3 Chapter 2: The Narayanpur Incident by Shashi Deshpande, depicting the 1942 Quit India Movement youth resistance, underground cyclostyling operation, collocations, words expressing moods, and inspirational speech writing.',
            changesList: [
                'Full 4-scene dramatic narrative digitized covering the background of 1942 Quit India, the silent procession with Gandhiji\'s portrait, smuggling the cyclostyling machine into the puja room, and Sub-Inspector Patil\'s midnight warning and raid.',
                'Cropped and integrated 4 authentic textbook illustrations (Silent Procession with Gandhiji, Smuggling the Cyclostyle Parcel, Patil at the doorway, and British Police raid with lanterns).',
                'Interactive vocabulary hover tooltips for key terms (Quit India, flurry, downpour, aloft, cyclostyling machine, reverie, brisk, bewilderment, lugged).',
                'Comprehension suite with 3 self-scoring MCQs, 5-step narrative Graphic Organizer Flowchart, and 5 detailed textual Q&As with "Reveal Answer" buttons.',
                'Tab 3: Collocations matcher (great joy, big mistake, heavy rain, deep thought, large population, strong wind) and 8-item Words That Express Moods matching & sentence quiz.',
                'Tab 4: Attributes of a Real-Life Hero interactive mind map, model student speech template ("The Power in Silent Courage"), and tri-lingual National War Memorial tribute (English, Hindi, Sanskrit).',
                'Tab 5: Deep historical inquiry into the 1942 Quit India Movement, underground Congress Radio by Usha Mehta, teenage martyrs (Kanaklata Barua, Shirish Kumar, Matangini Hazra), and modern youth civic action.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Initial production release with all 5 interactive tabs, audio feedback, authentic illustrations, and glassmorphic UI.'
                }
            ]
        },

        'eng_lit_ch9': {
            id: 'eng_lit_ch9',
            title: 'Chapter 3: Florence Nightingale',
            subject: 'English Literature',
            unit: 'Unit 3: Real-Life Heroes',
            author: 'Emma Lazarus',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 01:45 AM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#FBBF24',
            aiProvider: 'Google DeepMind',
            taskType: 'Lyrical Poem Digitization & Healthcare Heroism Suite',
            summary: 'Complete multi-tab study suite for Unit 3 Chapter 3: Florence Nightingale by Emma Lazarus, exploring the Crimean War setting at Scutari, Contrasting Imagery (light vs dark), rhyming scheme (AABCCB), everyday heroes recognition, and interactive gold medal crafting.',
            changesList: [
                'Full 6-stanza lyrical poem digitized with line-by-line paraphrase, audio rhythm guide, and AABCCB rhyme scheme breakdown.',
                'Cropped and integrated 3 authentic illustrations (Florence tending soldier with lamp, bedside care, and gold medal with red ribbon photograph).',
                'Interactive vocabulary hover tooltips for 20 archaic and poetic terms (whitewashed, walketh, darksome, lighteth, dismal, plaintive, tenderness, fretful, coarse, profane, standeth, hushed, couch, stoop, content, graven, quivering lids, sainted brow, flits for aye, storied page).',
                'Poem appreciation suite with 3 self-scoring MCQs and 6 detailed textbook short Q&As with "Reveal Answer" buttons.',
                'Tab 3: Contrasting Imagery analysis matrix comparing positive suggestions (angelic smile, whitewashed walls) vs negative suggestions (dismal corridors, darksome floors) + poetic devices (Archaism, Metaphor, Synecdoche, Alliteration).',
                'Tab 4: Experiential Learning on unsung everyday heroes (sanitation workers, nurses, bus drivers, teachers) + Interactive Virtual Medal Studio to customize and award medals.',
                'Tab 5: Florence Nightingale’s revolution of modern healthcare, data science (Nightingale rose diagram), 95% mortality reduction at Scutari, and National Florence Nightingale Awards in India.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Initial production release with all 5 interactive tabs, audio feedback, authentic illustrations, and glassmorphic UI. Completes 100% of Class 7 English Literature curriculum!'
                }
            ]
        },

        // ==========================================
        // ENGLISH GRAMMAR & COMPOSITION
        // ==========================================
        'eng_grammar_vocab': {
            id: 'eng_grammar_vocab',
            title: 'Chapter 26: Vocabulary & Language Mechanics',
            subject: 'English Grammar',
            unit: 'Spotlight English Grammar 7',
            author: 'Spotlight Grammar / CBSE Curriculum',
            version: 'v2.0.0',
            lastModified: 'September 6, 2026, 01:15 AM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#818CF8',
            aiProvider: 'Google DeepMind',
            taskType: 'Grammar Overhaul & Multi-Tab Pedagogical Module',
            summary: 'Comprehensive overhaul of Chapter 26 (Vocabulary) following the full 5-tab SOP: Homophones, Homonyms, 5 Suffix Rules, Incorrect Phrases, Redundancies, audio feedback, and interactive self-scoring mastery quiz.',
            changesList: [
                'Upgraded to modern 5-tab glassmorphic SOP layout with responsive dual-theme support (dark/light) and sticky navigation.',
                'Tab 1: Complete Homophones Lab covering 14 textbook pairs (pgs 149-150) + 5 high-yield curriculum enrichment pairs, deer/dear visual comparison, and interactive Exercise A with Web Audio feedback.',
                'Tab 2: Homonyms & Dual Meanings Lab with 10 textbook anchor words + complete dictionary definitions and dual contextual sentences for Exercise B (bark, pound, drop, die, right, point, current, tire).',
                'Tab 3: Suffixes & 5 Golden Spelling Rules complete with master directory (50+ words), Rule 1 to 5 visual breakdown with "Stay Ahead" exceptions, and Exercise C root word transformation solutions.',
                'Tab 4: Language Polish suite with 10 Common Incorrect Phrases, 6 Indian English expressions to avoid, full 22-term Redundancy Buster, and Exercise E model sentences.',
                'Tab 5: 15-question interactive Vocabulary Mastery Lab with instant grading, Web Audio chime synthesis, and high-resolution textbook scans lightbox (Pages 149-158).',
                'Integrated Revision Log modal and provenance tracking under Gemini 2.5 Pro (via Antigravity).'
            ],
            history: [
                {
                    version: 'v2.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Major curriculum overhaul bringing Chapter 26 to full parity with the 5-tab Literature SOP, with audio chimes, dual-theme support, and full textbook exercise solutions.'
                },
                {
                    version: 'v1.0.0',
                    date: 'August 2026',
                    model: 'Legacy System',
                    notes: 'Initial text-based notes compilation.'
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
        // ==========================================
        // HINDI LITERATURE (वसन्त / हिन्दी साहित्य)
        // ==========================================
        'hin_lit_ch1': {
            id: 'hin_lit_ch1',
            title: 'अध्याय १: हम पंछी उन्मुक्त गगन के',
            subject: 'Hindi Literature',
            unit: 'Unit 1: प्रकृति एवं जीवन मूल्य',
            author: 'शिवमंगल सिंह \'सुमन\'',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 02:40 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#8B5CF6',
            aiProvider: 'Google DeepMind',
            taskType: 'Curriculum Modernization & 5-Core-Tab Architecture',
            summary: 'Complete conversion to modern 5-core-tab interactive suite matching English Lit standards. Includes full unabridged 6 stanzas, parallel English translations, hover vocabulary tooltips, interactive MCQs, question bank, vocabulary vault, grammar rules, and concept mind map.',
            changesList: [
                'Full 6 stanzas digitized with parallel English translations and hover Devanagari tooltips.',
                'Interactive MCQs with instant visual feedback and score calculation.',
                'Question bank with interactive "उत्तर देखें" toggle for active recall.',
                'Vocabulary Vault: Grammar types, Hindi meanings, English translations, and example sentences.',
                'Grammar Tab: विलोम शब्द, विशेषण के भेद, and practical exercises.',
                'Critical Thinking Tab: Freedom philosophy analysis, Mind Map flowchart, and bird conservation connect.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Initial production build with 5 core tabs, universal silence (0 audio), and zero Gujarati.'
                }
            ]
        },

        'hin_lit_ch2': {
            id: 'hin_lit_ch2',
            title: 'अध्याय २: बूढ़ी काकी',
            subject: 'Hindi Literature',
            unit: 'Unit 1: प्रकृति एवं जीवन मूल्य',
            author: 'मुंशी प्रेमचंद',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 02:45 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#10B981',
            aiProvider: 'Google DeepMind',
            taskType: 'Curriculum Modernization & 5-Core-Tab Architecture',
            summary: 'Classic Premchand short story on elderly neglect, sensitivity, and moral awakening, structured into 5 core tabs with 100% text preservation.',
            changesList: [
                'Digitized all 6 scenes of Premchand\'s narrative with parallel English translations.',
                'Interactive comprehension MCQs and question bank with toggle answers.',
                'Vocabulary Vault with detailed parts of speech and examples.',
                'Grammar Tab: मुहावरे एवं लोकोक्तियाँ (कलेजा ठंडा होना, पेट में चूहे कूदना आदि) with sentence construction.',
                'Critical Tab: Elder care empathy, ASCII Mind Map, and interdisciplinary Social Studies connect.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Converted to modern 5-tab architecture with zero content loss.'
                }
            ]
        },

        'hin_lit_ch3': {
            id: 'hin_lit_ch3',
            title: 'अध्याय ३: असफलता से सीख',
            subject: 'Hindi Literature',
            unit: 'Unit 1: प्रकृति एवं जीवन मूल्य',
            author: 'प्रेरणादायी काव्य',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 02:50 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#EC4899',
            aiProvider: 'Google DeepMind',
            taskType: 'Curriculum Modernization & 5-Core-Tab Architecture',
            summary: 'Inspirational poetry module on resilience, learning from failures, and continuous action.',
            changesList: [
                'Complete inspirational poem with parallel English translations and hover vocabulary tooltips.',
                'MCQs and short/long answer questions with reveal answers.',
                'Vocabulary Vault: कठिन शब्दों के अर्थ, व्याकरण प्रकार व प्रयोग।',
                'Grammar: विलोम शब्द, तुकांत शब्द (rhyming words) व वाक्य-रचना।',
                'Critical Tab: Growth Mindset psychology, Concept Mind Map, and Thomas Edison historical connect.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Converted to modern 5-tab architecture.'
                }
            ]
        },

        'hin_lit_ch4': {
            id: 'hin_lit_ch4',
            title: 'अध्याय ४: यह भी एक परीक्षा',
            subject: 'Hindi Literature',
            unit: 'Unit 2: समाज, कर्तव्य एवं राष्ट्रीय गौरव',
            author: 'सुरेन्द्र अंचल',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 02:55 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#3B82F6',
            aiProvider: 'Google DeepMind',
            taskType: 'Curriculum Modernization & 5-Core-Tab Architecture',
            summary: 'Dramatic play in 2 scenes contrasting academic examination with moral empathy and humanity.',
            changesList: [
                'Full 2-scene dramatic play with character dialogues and stage directions in parallel Hindi/English.',
                'Comprehension MCQs and dialogue-based "किसने किससे कहा" with toggle reveal answers.',
                'Vocabulary Vault with dramatic terms and usage examples.',
                'Grammar: विशेषण और उसके चार मुख्य भेद (गुणवाचक, संख्यावाचक, परिमाणवाचक, सार्वनामिक)।',
                'Critical Tab: Moral dilemma analysis, ASCII Flowchart, and First Aid safety guidelines.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Converted to modern 5-tab architecture.'
                }
            ]
        },

        'hin_lit_ch5': {
            id: 'hin_lit_ch5',
            title: 'अध्याय ५: स्नेह भरी पाती',
            subject: 'Hindi Literature',
            unit: 'Unit 2: समाज, कर्तव्य एवं राष्ट्रीय गौरव',
            author: 'उषा वधवा',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 03:00 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#F59E0B',
            aiProvider: 'Google DeepMind',
            taskType: 'Curriculum Modernization & 5-Core-Tab Architecture',
            summary: 'Epistolary literature module (letter from Nani to grandson) on cultural heritage, green environment, and loving familial bonds.',
            changesList: [
                'Complete epistolary prose with parallel English translations and hover vocabulary tooltips.',
                'Comprehensive Q&A bank with toggle answer reveals.',
                'Vocabulary Vault: Traditional idioms, cultural terms, and usage examples.',
                'Grammar: उपसर्ग एवं प्रत्यय (मूल शब्द, नए शब्द) rules and exercises.',
                'Critical Tab: Letter writing art, environmental conservation, and concept Mind Map.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Converted to modern 5-tab architecture.'
                }
            ]
        },

        'hin_lit_ch6': {
            id: 'hin_lit_ch6',
            title: 'अध्याय ६: मिसाइल के जनक',
            subject: 'Hindi Literature',
            unit: 'Unit 2: समाज, कर्तव्य एवं राष्ट्रीय गौरव',
            author: 'डॉ. ए. पी. जे. अब्दुल कलाम',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 03:05 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#EF4444',
            aiProvider: 'Google DeepMind',
            taskType: 'Curriculum Modernization & 5-Core-Tab Architecture',
            summary: 'Inspiring autobiographical excerpts of Dr. APJ Abdul Kalam from Rameshwaram childhood to SLV-3 and Agni missile success.',
            changesList: [
                'Full autobiographical text digitized with parallel English translations and vocabulary hover tooltips.',
                'Interactive MCQs and comprehensive question bank with toggle answers.',
                'Vocabulary Vault: Scientific and biographical Hindi vocabulary.',
                'Grammar: सामासिक पद (Compound words), विलोम शब्द, and applied grammar.',
                'Critical Tab: ISRO/DRDO space connect, Kalaripayattu martial arts, and ASCII Mind Map.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Converted to modern 5-tab architecture.'
                }
            ]
        },

        'hin_lit_ch7': {
            id: 'hin_lit_ch7',
            title: 'अध्याय ७: माँ का उपहार',
            subject: 'Hindi Literature',
            unit: 'Unit 3: राष्ट्रभक्ति, बंधुत्व एवं व्यापक मूल्यांकन',
            author: 'साहसिक ऐतिहासिक कहानी',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 03:10 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#8B5CF6',
            aiProvider: 'Google DeepMind',
            taskType: 'Curriculum Modernization & 5-Core-Tab Architecture',
            summary: 'Riveting historical story intertwining the 1942 Quit India movement, Sharda Devi\'s sacrifice, and Arun saving Commissioner Jackson\'s son Dick.',
            changesList: [
                'Full narrative with parallel English translations and vocabulary hover tooltips.',
                'Comprehension MCQs, "किसने किससे कहा", short and long questions with toggle answers.',
                'Vocabulary Vault: Historical and emotional vocabulary cards with examples.',
                'Grammar: विलोम शब्द, पर्यायवाची शब्द, विशेषण के चार भेद identification.',
                'Critical Tab: Beyond revenge philosophy, Teesta river geography, and concept flowchart.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Converted to modern 5-tab architecture.'
                }
            ]
        },

        'hin_lit_ch8': {
            id: 'hin_lit_ch8',
            title: 'अध्याय ८: विश्वराज्य (\'वसुधैव कुटुंबकम\')',
            subject: 'Hindi Literature',
            unit: 'Unit 3: राष्ट्रभक्ति, बंधुत्व एवं व्यापक मूल्यांकन',
            author: 'राष्ट्रकवि मैथिलीशरण गुप्त',
            version: 'v1.0.0',
            lastModified: 'September 6, 2026, 03:15 PM IST',
            modelUsed: 'Gemini 2.5 Pro (via Antigravity)',
            modelBadgeColor: '#10B981',
            aiProvider: 'Google DeepMind',
            taskType: 'Curriculum Modernization & 5-Core-Tab Architecture',
            summary: 'Maithili Sharan Gupt\'s vision of universal brotherhood (Vasudhaiva Kutumbakam) and democracy, plus complete First Term Model Test Paper 1 (Chapters 1 to 8).',
            changesList: [
                'All 7 stanzas of Vishwarajya with parallel English translations and hover vocabulary tooltips.',
                'MCQs, stanza completion, and भाव स्पष्टीकरण with reveal answers.',
                'Vocabulary Vault: Classical Hindi and philosophical vocabulary cards.',
                'Grammar: सर्वनाम के छह भेद (पुरुष, निश्चय, अनिश्चय, संबंध, प्रश्न, निज) and identification.',
                'Critical Tab: Sardar Vallabhbhai Patel integration, ASCII Mind Map, AND Full Model Test Paper 1 (50 marks comprehensive exam) with interactive answers.'
            ],
            history: [
                {
                    version: 'v1.0.0',
                    date: 'September 6, 2026',
                    model: 'Gemini 2.5 Pro (via Antigravity)',
                    notes: 'Converted to modern 5-tab architecture with complete Model Test Paper 1 preserved.'
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
