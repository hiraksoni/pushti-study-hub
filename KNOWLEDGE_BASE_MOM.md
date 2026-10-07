# PUSHTI STUDY HUB — MINUTES OF MEETING (MOM)
**Standardized Knowledge Base (KB) Architecture & Automated Question Paper Generation Engine**

* **Date & Timestamp**: 07 October 2026, 09:45 PM IST
* **Participants**: Hirak Soni (Father & Project Architect), Antigravity AI (Pair Programming Assistant)
* **Status**: Codified & Active Standard
* **Version**: 3.7 (Science Biology Ch2 & Ch3 TLBR Authoritative Expansion — 407 Authoritative Items | Global Total: 5,191 Items across 86 Dossiers)

---

## 1. Executive Summary & Problem Statement

### 1.1 The Challenge: Token Inefficiency & Latency
* Previously, generating revision exercises, practice test papers, or answering student questions required the AI to either:
  1. Ingest massive 4,000–9,000 line production HTML files (chapters/maths/maths_ch1.html, etc.) where over 70% of the byte weight consists of repetitive UI styling, SVG markup, animations, and DOM scripts.
  2. Perform dynamic web searches, incurring latency, token cost, and potential discrepancies with the specific school curriculum.
* **Objective**: Establish a centralized, authoritative, lightweight **Knowledge Base (KB)** repository stored locally in pure Markdown (.md) and structured JSON (.json) per chapter.

### 1.2 Core Benefits
1. **85%–90% Token Reduction**: The AI reads a 15–30 KB structured dossier instead of a 350 KB HTML file.
2. **Zero-Token Client-Side Generation**: An in-browser Admin Worksheet Generator compiles randomized, print-ready question papers locally without consuming any API tokens.
3. **100% Curriculum Determinism**: All questions, formulas, conversion steps, and solutions are pre-verified against textbook scans and school teacher worksheets. Zero hallucination risk.
4. **Source Transparency**: Every item is tagged by origin (Textbook Exercise vs. Chapter Notes vs. Researched Enrichment).

---

## 2. Directory Structure & Naming Conventions

All authoritative Knowledge Base files are permanently organized in the dedicated root directory `KB Files/` with dedicated subfolders per chapter (and mirrored in `knowledge_base/` for backwards compatibility with automated test generator engines):

```text
d:\Users\expor\Downloads\Codes\
├── KB Files/
│   ├── sanskrit/
│   │   ├── ch1_vande_bharatam/                   (39 Items)
│   │   ├── ch2_subhashitas/                      (29 Items)
│   │   ├── ch3_mitraya_namah/                    (41 Items)
│   │   ├── ch4_na_gyayate_brahmanatvam/          (43 Items)
│   │   ├── ch5_seva_hi_paramo_dharmah/           (42 Items)
│   │   ├── ch6_kreedamah_rangnatyashalam/        (46 Items)
│   │   ├── ch13_varna_matra_sankhya/             (40 Items)
│   │   ├── ch14_shabdarupani/                    (28 Items)
│   │   ├── ch15_dhaturupani/                   (30 Items)
│   │   ├── ch19_prashnirmanam/                 (60 Items)
│   │   ├── ch_g1_sandhi_avyaya/                  (44 Items)
│   │   ├── ch_g2_upapada_vibhakti/               (35 Items)
│   │   └── ch_w1_rachanatmak_karyani/            (16 Tasks)
│   ├── mathematics/
│   │   ├── main_source_mtg/
│   │   │   ├── ch1_large_numbers/                (112 Items • Expanded & Verified)
│   │   │   ├── ch2_arithmetic_expressions/        (92 Items • Expanded & Verified)
│   │   │   ├── ch3_decimals/                      (31 Items • MATH_MTG_CH03)
│   │   │   ├── ch4_expressions_letter_numbers/    (18 Items • MATH_MTG_CH04)
│   │   │   ├── ch5_parallel_intersecting_lines/   (126 Items • Expanded & Verified)
│   │   │   ├── ch6_number_play/                   (25 Items • MATH_MTG_CH06)
│   │   │   ├── ch7_tale_of_three_lines_triangles/ (13 Items • MATH_MTG_CH07)
│   │   │   └── ch8_working_with_fractions/        (12 Items • MATH_MTG_CH08)
│   │   ├── reference_source_cordova/
│   │   │   ├── ch1_integers/                      (24 Items • MATH_CORDOVA_CH01)
│   │   │   ├── ch2_fractions/                     (10 Items • MATH_CORDOVA_CH02)
│   │   │   ├── ch3_decimals/                      (47 Items • MATH_CORDOVA_CH03)
│   │   │   ├── ch7_algebraic_expressions/         (10 Items • MATH_CORDOVA_CH07)
│   │   │   ├── ch11_lines_and_angles/             (33 Items • MATH_CORDOVA_CH11)
│   │   │   └── ch12_triangles_and_properties/     (36 Items • MATH_CORDOVA_CH12)
│   │   └── school_worksheet/
│   │       └── midterm_2026_silver_bells/          (50 Items • Mid-Term 80 Marks)
│   ├── biology/
│   │   ├── ch2_adolescence/
│   │   │   ├── bio_ch2_adolescence.md
│   │   │   └── bio_ch2_adolescence.json          (157 Items • 100% TLBR Ingested)
│   │   └── ch3_life_processes/
│   │       ├── bio_ch3_life_processes.md
│   │       └── bio_ch3_life_processes.json        (250 Items • 100% TLBR Ingested • Pure Unicode Text)
│   ├── chemistry/
│   │   ├── ch1_acids_bases_salts/
│   │   │   ├── chem_ch1_acids_bases_salts.md
│   │   │   └── chem_ch1_acids_bases_salts.json   (197 Items • 100% TLBR Ingested)
│   │   └── ch2_metals_and_non_metals/
│   │       ├── chem_ch2_metals_and_non_metals.md
│   │       └── chem_ch2_metals_and_non_metals.json (208 Items • 100% TLBR Ingested)
│   ├── physics/
│   │   ├── ch1_electricity/
│   │   │   ├── phy_ch1_electricity.md
│   │   │   └── phy_ch1_electricity.json          (251 Items • 100% TLBR Ingested)
│   │   ├── ch2_heat/
│   │   │   ├── phy_ch2_heat.md
│   │   │   └── phy_ch2_heat.json                 (225 Items • 100% TLBR Ingested)
│   │   └── ch3_motion_time/
│   │       ├── phy_ch3_motion_time.md
│   │       └── phy_ch3_motion_time.json          (192 Items • 100% TLBR Ingested)
│   ├── social_science/
│   │   ├── geography/
│   │   │   ├── ch1_interior_earth/               (54 Items)
│   │   │   └── ch2_changing_earth/               (36 Items)
│   │   ├── history/
│   │   │   ├── ch6_first_empires/                (51 Items)
│   │   │   ├── ch7_iron_age/                     (20 Items)
│   │   │   └── ch8_guptas_harsha/                (37 Items)
│   │   └── civics/
│   │       ├── ch13_gender/                      (49 Items)
│   │       ├── ch14_democracy/                   (15 Items)
│   │       └── ch17_markets/                     (65 Items)
│   └── ict/
│       ├── ch1_number_system/                    (80 Items • Expanded & Verified)
│       │   ├── ict_ch1_number_system.md / .json
│       ├── ch2_excel_advanced/                   (74 Items • Expanded & Verified)
│       │   ├── ict_ch2_excel_advanced.md / .json
│       ├── ch3_artificial_intelligence/          (54 Items • Expanded & Verified)
│       │   ├── ict_ch3_artificial_intelligence.md / .json
│       ├── ch4_html_css/                         (82 Items)
│       └── ch5_lists_images/                     (74 Items • Expanded & Verified)
│           ├── ict_ch5_lists_images.md / .json
│   └── english/
│       ├── literature/
│       │   ├── ch1_a_hero/                       (23 Items • eng_lit_ch1_a_hero)
│       │   ├── ch2_taste_of_watermelon/          (23 Items • eng_lit_ch2_taste_of_watermelon)
│       │   ├── ch3_flower_school/                (18 Items • eng_lit_ch3_flower_school)
│       │   ├── ch4_atlantis/                     (27 Items • eng_lit_ch4_atlantis)
│       │   ├── ch5_space_traveller/              (24 Items • eng_lit_ch5_space_traveller)
│       │   ├── ch6_lake_isle_innisfree/          (19 Items • eng_lit_ch6_lake_isle_innisfree)
│       │   ├── ch7_ada_blackjack/                (25 Items • eng_lit_ch7_ada_blackjack)
│       │   ├── ch8_narayanpur_incident/          (25 Items • eng_lit_ch8_narayanpur_incident)
│       │   └── ch9_florence_nightingale/         (19 Items • eng_lit_ch9_florence_nightingale)
│       └── grammar/
│           ├── g1_nouns_classification/          (66 Items • eng_gram_g1_nouns_classification)
│           ├── g2_nouns_number_gender/           (79 Items • eng_gram_g2_nouns_number_gender)
│           ├── g3_pronouns/                      (79 Items • eng_gram_g3_pronouns)
│           ├── g4_case_noun_pronoun/             (79 Items • eng_gram_g4_case_noun_pronoun)
│           ├── g5_adjectives/                    (79 Items • eng_gram_g5_adjectives)
│           ├── g6_determiners/                   (79 Items • eng_gram_g6_determiners)
│           ├── g7_articles/                      (79 Items • eng_gram_g7_articles)
│           ├── g8_verbs/                         (79 Items • eng_gram_g8_verbs)
│           ├── g9_modals_auxiliaries/            (79 Items • eng_gram_g9_modals_auxiliaries)
│           ├── g10_finite_non_finite/            (79 Items • eng_gram_g10_finite_non_finite)
│           ├── g17_active_passive/               (79 Items • eng_gram_g17_active_passive)
│           └── v1_vocabulary_word_power/         (79 Items • eng_gram_v1_vocabulary_word_power)
│   └── hindi/
│       ├── literature/
│       │   ├── ch1_humko_man_ki_shakti_dena/     (19 Items • 100% Textbook & Notebook Ingested)
│       │   ├── ch2_boodhi_kaki/                  (23 Items • 100% Textbook & Notebook Ingested)
│       │   ├── ch3_asafalta_se_seekh/            (25 Items • 100% Textbook & Notebook Ingested)
│       │   ├── ch4_yeh_bhi_ek_pariksha/          (24 Items • 100% Textbook & Notebook Ingested)
│       │   ├── ch5_sneh_bhari_paati/             (19 Items • 100% Textbook & Notebook Ingested)
│       │   ├── ch6_missile_ke_janak/             (16 Items • 100% Textbook & Notebook Ingested)
│       │   ├── ch7_maa_ka_upahar/                (23 Items • 100% Textbook & Notebook Ingested)
│       │   └── ch8_vishwarajya/                  (23 Items • 100% Textbook Ingested + 50M Term-1 Exam)
│       └── grammar/
│           ├── g1_bhasha_lipi_vyakaran/          (23 Items • 100% Textbook & Notebook Ingested)
│           ├── g2_varna_vichar/                  (27 Items • 100% Textbook & Notebook Ingested)
│           ├── g3_shabda_vichar/                 (26 Items • 100% Textbook & Notebook Ingested)
│           ├── g4_upsarg_pratyay/                (19 Items • 100% Textbook & Notebook Ingested)
│           ├── g6_samas/                         (13 Items • 100% Textbook & Notebook Ingested)
│           ├── g7_sangya/                        (14 Items • 100% Textbook & Notebook Ingested)
│           ├── g20_shabdo_ka_parivar/            (12 Items • 100% Textbook Ingested)
│           ├── g22_muhavare_lokoktiyan/          (11 Items • 100% Textbook Ingested)
│           ├── g23_patra_lekhan/                 (10 Items • 100% Textbook Ingested)
│           └── g25_anuched_lekhan/               (9 Items • 100% Textbook Ingested)
├── knowledge_base/                               (Mirrored System Store)
│   ├── sanskrit/
│   ├── mathematics/
│   ├── biology/
│   ├── chemistry/
│   ├── physics/
│   ├── social_science/
│   ├── ict/
│   ├── english/
│   └── hindi/
├── admin_worksheet_generator.html
├── scripts/
│   ├── build_chapter_from_kb.py                  (Zero-Token Production HTML Compiler)
│   ├── generate_sanskrit_kbs.py                  (Sanskrit KB Builder)
│   ├── generate_mathematics_kbs.py               (Mathematics KB Builder)
│   ├── generate_physics_kbs.py                   (Physics KB Builder)
│   ├── generate_social_science_kbs.py            (Social Science KB Builder)
│   ├── generate_english_batch1_kbs.py            (English Literature KB Builder)
│   ├── generate_english_batch7_grammar_kbs.py    (English Grammar Batch 7 Builder)
│   └── generate_hindi_batch1_kbs.py              (Hindi Literature Batch 1 Builder)
└── KNOWLEDGE_BASE_MOM.md                         (This Document)
```


---

## 2.1 Autonomous AI Model Protocol (Gemini, Claude, Antigravity)

Whenever an AI model is invoked to answer curriculum questions, generate worksheets, create revision drills, or explain concepts:
1. **Always Refer SOP First**: Review `SOP.md` for mandatory publication/school anonymization, CBSE standards, and UTF-8 encoding integrity.
2. **Mandatory KB-First Retrieval**: Never read 4,000–9,000 line production HTML files or make broad web searches. Always load the pre-compiled `<chapter>.md` and `<chapter>.json` files from `KB Files/<subject>/<chapter>/` first.
3. **Build Before Proceeding**: If a requested chapter does not yet have a KB file in `KB Files/`, the AI model MUST compile the chapter's dual-file KB pair first, and only then proceed with the task.
4. **Living Document Protocol**: Any newly gathered knowledge, question items, or corrections must be immediately updated back into that chapter's KB file.
5. **Token Conservation Practice**: Proactively offer smart recommendations to minimize token usage (leveraging structured JSON/MD files, client-side generation, and targeted section reads).

### File Pair Principle
Each chapter maintains a synchronized **Dual-File Pair**:
1. **Human/AI Dossier (.md)**: Formatted for quick reading, conceptual review, and LLM context injection.
2. **Machine Item Bank (.json)**: Formatted for immediate algorithmic filtering, shuffling, and rendering by `admin_worksheet_generator.html`.

---

## 3. Metadata & Tagging Taxonomy

Every entry in the Knowledge Base is strictly annotated with standardized attributes:

### 3.1 Source Taxonomy (`source`)
| Tag Key | Display Label | Description |
| :--- | :--- | :--- |
| `textbook_exercise` | **Textbook Exercise** | Direct questions, exercises, and problem sets from the prescribed school textbook. |
| `chapter_notes` | **Chapter Notes & Theory** | Core theoretical explanations, definitions, laws, formulas, and step-by-step model examples. |
| `school_worksheet` | **School Assessment** | Questions extracted from school teacher test papers, unit assessment sheets, and periodic tests. |
| `researched_enrichment` | **Researched Enrichment** | High-yield extra context, real-world tech trivia, historical milestones, and industry applications gathered from research. |
| `exam_trap` | **Common Pitfall / Trap** | Classic examination trick questions, negative-marking traps, and frequent student mistakes. |

### 3.2 Challenge & Difficulty Levels (`difficulty`)
* **`easy` (Level 1 — Confidence Builder)**: Direct factual recall, straightforward definitions, basic binary rules, single-cell Excel formulas.
* **`medium` (Level 2 — School Standard)**: Multi-step conversions, standard application problems, sorting/filtering scenarios, standard MCQs.
* **`hard_hots` (Level 3 — Advanced HOTS / Olympiad)**: Complex binary arithmetic with multiple carries/borrows, nested formula logic, multi-domain AI synergy, boundary conditions.

### 3.3 Question Types (`type`)
* `mcq`: Multiple Choice Question with 4 distinct options and detailed distractor analysis.
* `fib`: Fill in the Blanks with exact string matching and acceptable aliases.
* `tf`: True / False assertion with logical justification.
* `conversion`: Mathematical or numeric step-by-step conversion drill.
* `short_answer`: 2 to 3 marks conceptual explanation.
* `long_answer`: 4 to 5 marks comprehensive analysis or comparative table.

### 3.4 Scientific, Chemical & Mathematical Notation Standards
To ensure zero confusion for students, AI models, and printable worksheets, scientific notations must never be stored as squashed ASCII (e.g., `H2SO4` or `cm3`):
1. **Chemical Formulas**: Subscripts must use pure Unicode characters (`₀₁₂₃₄₅₆₇₈₉`) so formulas remain legible in both plain text and rich formats. Examples:
   - Acids: `H₂SO₄`, `HNO₃`, `HCl`, `H₂CO₃`, `CH₃COOH`
   - Bases: `NaOH`, `Ca(OH)₂`, `Mg(OH)₂`, `NH₄OH`, `Al(OH)₃`
   - Salts & Oxides: `NaCl`, `CaCO₃`, `NaHCO₃`, `Na₂CO₃·10H₂O`, `CaO`, `Fe₂O₃`
   - Stoichiometric Coefficients: Maintain normal digits before elements: `2H₂ + O₂ → 2H₂O`, `2Mg + O₂ → 2MgO`
2. **Reaction Arrows & State Symbols**:
   - Arrows: Always use Unicode right arrow `→` (never ASCII `->` or `-->`). Reversible reactions use `⇌`.
   - States of matter: Clearly designate `(s)` solid, `(l)` liquid, `(g)` gas, `(aq)` aqueous solution.
   - Precipitate / Gas evolution: `↓` (precipitate), `↑` (gas released).
3. **Ions & Valencies**: Use superscripts for charges: `Na⁺`, `Ca²⁺`, `Al³⁺`, `Cl⁻`, `SO₄²⁻`, `OH⁻`, `NO₃⁻`.
4. **Mathematical Powers & Scientific Units**:
   - Area & Volume: `cm²`, `cm³`, `m²`, `m³`
   - Exponents & Variables: `x²`, `y³`, `10⁻²`
   - Temperature: `°C`, `°F`, `K`

### 3.5 Mathematics Dual-Source Architecture & Cross-Referencing Protocol
In Mathematics, curriculum content originates from two distinct, non-overlapping pedagogical sources:
1. **Main Source (MTG Coursebook)**: Prescribed primary textbook containing standard syllabus theory, CBSE exercises, and graded problems.
2. **Reference Source (Cordova / Ref 1)**: Parallel supplementary textbook providing alternate problem sets, practice test papers, HOTS challenges, and Olympiad drills.

#### Storage & Taxonomy Rules:
- **Strict Separation**: MTG files reside exclusively under `KB Files/mathematics/main_source_mtg/` and Cordova files reside exclusively under `KB Files/mathematics/reference_source_cordova/`. Contents are never blended into a single file.
- **Dedicated Chapter Codes**:
  - MTG: `MATH_MTG_CH01` through `MATH_MTG_CH08`
  - Cordova: `MATH_CORDOVA_CH01` (Integers), `MATH_CORDOVA_CH02` (Fractions), `MATH_CORDOVA_CH03` (Decimals), `MATH_CORDOVA_CH07` (Algebraic Expressions), `MATH_CORDOVA_CH11` (Lines & Angles), `MATH_CORDOVA_CH12` (Triangles)
- **Cross-Referencing Metadata**:
  - Whenever an MTG chapter maps conceptually to a Cordova chapter, its JSON metadata includes `"paired_reference_code": "MATH_CORDOVA_CHxx"` and its Markdown Section 1 includes an explicit markdown link.
  - Reciprocally, Cordova JSON files include `"paired_main_code": "MATH_MTG_CHxx"` with markdown link back to the main coursebook chapter.
- **Anonymization & Zero-Token Compliance**:
  - All student-facing text strictly adheres to SOP v3.3 (referencing "Main Source" and "Reference Source (Ref 1)").
  - KaTeX formatting (`$...$` and `$$...$$`) is preserved with zero truncation.

### 3.6 Diagram Slot & Admin Ingestion Protocol
* **Architectural Standard (07 October 2026)**:
  1. **Zero AI Token Waste on Cropping**: AI assistants must **never** perform raster image cropping, PDF clipping, or pixel guessing during Knowledge Base compilation.
  2. **Standardized `diagram_slot` Object**: When an item references a figure, circuit, or diagram, the compiler inserts a `diagram_slot` object:
     ```json
     "diagram_slot": {
       "status": "pending",
       "image_path": null,
       "source_hint": "Textbook Page 56, Solved Example 3: Mechanism of Inhalation",
       "book_page": 56,
       "description": "Mechanism of Inhalation showing ribcage and diaphragm motion"
     }
     ```
  3. **Graceful Student Experience (Pushti's View)**:
     - When `status == "pending"`, displays: `[📖 Diagram Reference: Refer to Textbook Page XX]` with an optional prompt `[Ask Papa to Upload 🔔]`.
     - When `status == "uploaded"`, the real image is seamlessly rendered with zero layout disruption.
  4. **Admin Ingestion Hub (Parent Portal)**:
     - Guarded by PIN `1985` in the Admin Dashboard.
     - Centralizes all pending diagram slots across all chapters with drag-and-drop / clipboard paste upload for the parent to add diagrams at leisure.
     - Saves the file directly to the chapter's `images/` directory and activates the slot without code duplication.

---

## 4. Admin Worksheet & Exam Generator Governance

1. **Admin Exclusivity**:
   - The Worksheet Generator is housed in [`admin_worksheet_generator.html`](file:///d:/Users/expor/Downloads/Codes/admin_worksheet_generator.html).
   - Guarded by Admin PIN verification (`1985`) and parent role session state.
2. **Parametric Generation Controls**:
   - Filter by source: choose strictly Textbook Exercises, include Chapter Notes, or inject Researched Enrichment.
   - Filter by difficulty: Easy (100% basics), Standard (70/30), or HOTS Challenge.
   - Target length: 10 Marks (Quick Recap), 20 Marks (Periodic Test), or 40 Marks (Mid-Term Blueprint).
3. **Dual-Mode Output**:
   - **Student View**: Clean, printable worksheet with name/date headers, question prompts, and response lines.
   - **Teacher / Admin View**: Displays full step-by-step answers, KaTeX conversion grids, and marking rubrics.
   - **Print Optimization**: High-contrast `@media print` layout formatting to standard A4 paper without clipped margins or background bleed.

---

## 5. Maintenance & Revision Protocol

* **Living Document**: This MOM must be updated whenever:
  1. A new subject is added to the Knowledge Base (e.g. Mathematics, Science).
  2. A new question type or taxonomy tag is introduced.
  3. School test patterns evolve.
* **Quality Gate Integration**: Merged with Master Unified SOP v3.3 Section 1.6 (Strict Anonymization) and Section 4.4 (Centralized Tests Architecture).

---

## 6. Official Examination Blueprints (Codified from Teacher / School Guidelines)

### 6.1 Computer Studies (ICT) — 40 Marks Mid-Term Pattern
* **Date of Receipt**: 23 September 2026 (Handwritten Paper Style Verification)
* **Chapters Covered**: Ch 1 (Number System), Ch 2 (Advanced Excel), Ch 3 (AI), Ch 4 (HTML & CSS), Ch 5 (Lists & Images)
* **Question-by-Question Blueprint**:
  1. **Q1] MCQs**: 10 Questions × 1 Mark = **10 Marks** (25.0%)
  2. **Q2] Fill in the blanks**: 5 Questions × 1 Mark = **5 Marks** (12.5%)
  3. **Q3] True & False**: 5 Questions × 1 Mark = **5 Marks** (12.5%)
  4. **Q4] Short Q/A**: 6 Questions × 2 Marks = **12 Marks** (30.0%)
  5. **Q5] Long Q/A**: 2 Questions × 4 Marks = **8 Marks** (20.0%)
  * **Total**: 5 Questions • **40 Marks** (100%)

### 6.2 English — 80 Marks Mid-Term Pattern
* **Section A (Reading)**: 2 Unseen Passages × 10M = **20 Marks**
* **Section B (Writing & Grammar)**: Creative Writing (15M) + Do as Directed Grammar (15M) = **30 Marks**
* **Section C (Literature)**: Extracts (8M) + Short Answers 30-40w (14M) + Long Answers 80-100w (8M) = **30 Marks**
* **Total**: 3 Sections • **80 Marks**

### 6.3 Social Science — 80 Marks Mid-Term Pattern
* **History**: 30 Marks (Case Study 4M, MCQ/FB 5M, Short Q/A 6M, Long Q/A 12M, Map Work 3M)
* **Civics**: 30 Marks (Case Study 5M, MCQ/FB 5M, Short Q/A 4M, Very Short 4M, Long Answers 12M)
* **Geography**: 20 Marks (Case Study 3M, MCQ/FB 5M, Short Q/A 4M, Label Picture 2M, Long Q/A 6M)
* **Total**: 3 Subjects • **80 Marks**

### 6.4 Mathematics — 80 Marks Mid-Term Pattern
* **Date of Receipt**: 29 September 2026 (Actual Exam Paper dated 28 September 2026)
* **Section A (25 Marks)**: Q1 MCQs 10 × 1M = 10 | Q2 Fill in the Blanks 5 × 1M = 5 | Q3 True/False 5 × 1M = 5 | Q4 Attempt 5 of 6 × 1M = 5
* **Section B (47 Marks)**: Q5 Attempt 6 of 7 × 2M = 12 | Q6 Attempt 5 of 6 × 3M = 15 | Q7 Attempt 4 of 5 × 5M = 20
* **Section C (8 Marks)**: Q8 — 2 Case Studies × 4M ((a) 1M + (b) 1M + (c) 2M, internal choice)
* **Total**: 3 Sections • **80 Marks**

---

## 7. Active Knowledge Base Inventory (Total: 4,489 Standardized Items across 84 Dossiers)

| Subject | Chapter Key | Chapter Name | Items | File Path | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sanskrit** | `ch1_vande_bharatam` | अध्यायः १: वन्दे भारतम् (वन्दे भारतमातरम्) | 39 | `KB Files/sanskrit/ch1_vande_bharatam/` | ✅ Complete |
| **Sanskrit** | `ch2_subhashitas` | अध्यायः २: नित्यं पिबामः सुभाषितरसम् | 29 | `KB Files/sanskrit/ch2_subhashitas/` | ✅ Complete |
| **Sanskrit** | `ch3_mitraya_namah` | अध्यायः ३: मित्राय नमः (सूर्यनमस्कारः) | 41 | `KB Files/sanskrit/ch3_mitraya_namah/` | ✅ Complete |
| **Sanskrit** | `ch4_na_gyayate_brahmanatvam` | अध्यायः ४: न ज्ञायते चेत् अस्मत् ब्राह्मणत्वम् (आम्लं द्राक्षाफलम्) | 43 | `KB Files/sanskrit/ch4_na_gyayate_brahmanatvam/` | ✅ Complete |
| **Sanskrit** | `ch5_seva_hi_paramo_dharmah` | अध्यायः ५: सेवा हि परमो धर्मः | 42 | `KB Files/sanskrit/ch5_seva_hi_paramo_dharmah/` | ✅ Complete |
| **Sanskrit** | `ch6_kreedamah_rangnatyashalam` | अध्यायः ६: क्रीडामः वयं रङ्गनाट्यशालाम् (श्लोकान्त्याक्षरी) | 46 | `KB Files/sanskrit/ch6_kreedamah_rangnatyashalam/` | ✅ Complete |
| **Sanskrit** | `ch13_varna_matra_sankhya` | अध्यायः १३: वर्णमात्रा-परिचयः एवं संख्याज्ञानम् | 40 | `KB Files/sanskrit/ch13_varna_matra_sankhya/` | ✅ Complete |
| **Sanskrit** | `ch14_shabdarupani` | अध्यायः १४: शब्दरूपाणि (Noun Declensions) | 28 | `KB Files/sanskrit/ch14_shabdarupani/` | ✅ Complete |
| **Sanskrit** | `ch15_dhaturupani` | अध्यायः १५: धातुरूपाणि (Verb Conjugations) | 30 | `KB Files/sanskrit/ch15_dhaturupani/` | ✅ Complete |
| **Sanskrit** | `ch19_prashnirmanam` | अध्यायः १९: प्रश्ननिर्माणम् (Question Formation) | 60 | `KB Files/sanskrit/ch19_prashnirmanam/` | ✅ Complete |
| **Sanskrit** | `ch_g1_sandhi_avyaya` | G1: अनुप्रयुक्त-व्याकरणम् (स्वरसन्धिः एवं अव्ययानि) | 44 | `KB Files/sanskrit/ch_g1_sandhi_avyaya/` | ✅ Complete |
| **Sanskrit** | `ch_g2_upapada_vibhakti` | G2: उपपद-विभक्तयः (Upapada Vibhakti & Case Rules) | 35 | `KB Files/sanskrit/ch_g2_upapada_vibhakti/` | ✅ Complete |
| **Sanskrit** | `ch_w1_rachanatmak_karyani` | W1: रचनात्मककार्याणि (पत्रलेखनम्, चित्रवर्णनम्, संवादलेखनम्) | 16 | `KB Files/sanskrit/ch_w1_rachanatmak_karyani/` | ✅ Complete |
| **Mathematics (MTG)** | `ch1_large_numbers` | Large Numbers Around Us (`MATH_MTG_CH01`) | 112 | `KB Files/mathematics/main_source_mtg/ch1_large_numbers/` | ✅ Complete (Exhaustive) |
| **Mathematics (MTG)** | `ch2_arithmetic_expressions` | Arithmetic Expressions (`MATH_MTG_CH02`) | 92 | `KB Files/mathematics/main_source_mtg/ch2_arithmetic_expressions/` | ✅ Complete (Exhaustive) |
| **Mathematics (MTG)** | `ch3_decimals` | A Peek Beyond the Point (Decimals) (`MATH_MTG_CH03`) | 31 | `KB Files/mathematics/main_source_mtg/ch3_decimals/` | ✅ Complete |
| **Mathematics (MTG)** | `ch4_expressions_letter_numbers` | Expressions using Letter-Numbers (`MATH_MTG_CH04`) | 18 | `KB Files/mathematics/main_source_mtg/ch4_expressions_letter_numbers/` | ✅ Complete |
| **Mathematics (MTG)** | `ch5_parallel_intersecting_lines` | Parallel and Intersecting Lines (`MATH_MTG_CH05`) | 126 | `KB Files/mathematics/main_source_mtg/ch5_parallel_intersecting_lines/` | ✅ Complete (Exhaustive) |
| **Mathematics (MTG)** | `ch6_number_play` | Number Play (`MATH_MTG_CH06`) | 25 | `KB Files/mathematics/main_source_mtg/ch6_number_play/` | ✅ Complete |
| **Mathematics (MTG)** | `ch7_tale_of_three_lines_triangles` | A Tale of Three Intersecting Lines (`MATH_MTG_CH07`) | 13 | `KB Files/mathematics/main_source_mtg/ch7_tale_of_three_lines_triangles/` | ✅ Complete |
| **Mathematics (MTG)** | `ch8_working_with_fractions` | Working with Fractions (`MATH_MTG_CH08`) | 12 | `KB Files/mathematics/main_source_mtg/ch8_working_with_fractions/` | ✅ Complete |
| **Mathematics (Cordova)** | `ch1_integers` | Integers (`MATH_CORDOVA_CH01`) | 24 | `KB Files/mathematics/reference_source_cordova/ch1_integers/` | ✅ Complete |
| **Mathematics (Cordova)** | `ch2_fractions` | Fractions (`MATH_CORDOVA_CH02`) | 10 | `KB Files/mathematics/reference_source_cordova/ch2_fractions/` | ✅ Complete |
| **Mathematics (Cordova)** | `ch3_decimals` | Decimals (`MATH_CORDOVA_CH03`) | 47 | `KB Files/mathematics/reference_source_cordova/ch3_decimals/` | ✅ Complete |
| **Mathematics (Cordova)** | `ch7_algebraic_expressions` | Algebraic Expressions (`MATH_CORDOVA_CH07`) | 10 | `KB Files/mathematics/reference_source_cordova/ch7_algebraic_expressions/` | ✅ Complete |
| **Mathematics (Cordova)** | `ch11_lines_and_angles` | Lines and Angles (`MATH_CORDOVA_CH11`) | 33 | `KB Files/mathematics/reference_source_cordova/ch11_lines_and_angles/` | ✅ Complete |
| **Mathematics (Cordova)** | `ch12_triangles_and_properties` | The Triangle and Its Properties (`MATH_CORDOVA_CH12`) | 36 | `KB Files/mathematics/reference_source_cordova/ch12_triangles_and_properties/` | ✅ Complete |
| **Biology** | `ch2_adolescence` | Adolescence: A Stage of Growth and Change | 157 | `KB Files/biology/ch2_adolescence/` | ✅ 100% TLBR Ingested, Pure Unicode Notation, Dual Schema & Store |
| **Biology** | `ch3_life_processes` | Life Processes in Animals | 250 | `KB Files/biology/ch3_life_processes/` | ✅ 100% TLBR Ingested, Pure Unicode Notation, Dual Schema & Store |
| **Chemistry** | `ch1_acids_bases_salts` | Exploring Substances: Acidic, Basic and Neutral | 197 | `KB Files/chemistry/ch1_acids_bases_salts/` | ✅ 100% TLBR Ingested, Pure Unicode Sub/Superscripts, Dual Schema & Store |
| **Chemistry** | `ch2_metals_and_non_metals` | The World of Metals and Non-metals | 208 | `KB Files/chemistry/ch2_metals_and_non_metals/` | ✅ 100% TLBR Ingested, Pure Unicode Sub/Superscripts, Dual Schema & Store |
| **Physics** | `ch1_electricity` | Electricity: Circuits & Components | 251 | `KB Files/physics/ch1_electricity/` | ✅ 100% TLBR Ingested, Pure Unicode Notation, Dual Schema & Store |
| **Physics** | `ch2_heat` | Heat Transfer in Nature | 225 | `KB Files/physics/ch2_heat/` | ✅ 100% TLBR Ingested, Pure Unicode Notation, Dual Schema & Store |
| **Physics** | `ch3_motion_time` | Measurement of Time and Motion | 192 | `KB Files/physics/ch3_motion_time/` | ✅ 100% TLBR Ingested, Pure Unicode Notation, Dual Schema & Store |
| **Social Science (Geo)** | `ch1_interior_earth` | Interior of the Earth | 54 | `KB Files/social_science/geography/ch1_interior_earth/` | ✅ Complete |
| **Social Science (Geo)** | `ch2_changing_earth` | Our Changing Earth | 36 | `KB Files/social_science/geography/ch2_changing_earth/` | ✅ Complete |
| **Social Science (Hist)** | `ch6_first_empires` | The First Indian Empires (The Mauryas) | 51 | `KB Files/social_science/history/ch6_first_empires/` | ✅ Complete |
| **Social Science (Hist)** | `ch7_iron_age` | India in the Iron Age | 20 | `KB Files/social_science/history/ch7_iron_age/` | ✅ Complete |
| **Social Science (Hist)** | `ch8_guptas_harsha` | India from 4th to 7th Century CE (Guptas & Harsha) | 37 | `KB Files/social_science/history/ch8_guptas_harsha/` | ✅ Complete |
| **Social Science (Civ)** | `ch13_gender` | Understanding Gender | 49 | `KB Files/social_science/civics/ch13_gender/` | ✅ Complete |
| **Social Science (Civ)** | `ch14_democracy` | How Does Democracy Work? (State Government) | 15 | `KB Files/social_science/civics/ch14_democracy/` | ✅ Complete |
| **Social Science (Civ)** | `ch17_markets` | Markets Around Us | 65 | `KB Files/social_science/civics/ch17_markets/` | ✅ Complete |
| **ICT** | `ch1_number_system` | Number System & Binary Arithmetic | 80 | `KB Files/ict/ch1_number_system/` | ✅ Complete (Exhaustive) |
| **ICT** | `ch2_excel_advanced` | Advanced Features of Excel | 74 | `KB Files/ict/ch2_excel_advanced/` | ✅ Complete (Exhaustive) |
| **ICT** | `ch3_artificial_intelligence`| Artificial Intelligence | 54 | `KB Files/ict/ch3_artificial_intelligence/` | ✅ Complete (Exhaustive) |
| **ICT** | `ch4_html_css` | More on CSS & HTML | 82 | `KB Files/ict/ch4_html_css/` | ✅ Complete |
| **ICT** | `ch5_lists_images` | Lists and Tables in HTML5 | 74 | `KB Files/ict/ch5_lists_images/` | ✅ Complete (Exhaustive) |
| **English (Literature)** | `ch1_a_hero` | Unit 1.1: A Hero (R.K. Narayan) | 23 | `KB Files/english/literature/ch1_a_hero/` | ✅ Complete |
| **English (Literature)** | `ch2_taste_of_watermelon` | Unit 1.2: The Taste of Watermelon (Borden Deal) | 23 | `KB Files/english/literature/ch2_taste_of_watermelon/` | ✅ Complete |
| **English (Literature)** | `ch3_flower_school` | Unit 1.3: The Flower-School (Rabindranath Tagore) | 18 | `KB Files/english/literature/ch3_flower_school/` | ✅ Complete |
| **English (Literature)** | `ch4_atlantis` | Unit 2.1: Atlantis (Plato) | 27 | `KB Files/english/literature/ch4_atlantis/` | ✅ Complete |
| **English (Literature)** | `ch5_space_traveller` | Unit 2.2: The Diary of a Space Traveller (Satyajit Ray) | 24 | `KB Files/english/literature/ch5_space_traveller/` | ✅ Complete |
| **English (Literature)** | `ch6_lake_isle_innisfree` | Unit 2.3: The Lake Isle of Innisfree (W.B. Yeats) | 19 | `KB Files/english/literature/ch6_lake_isle_innisfree/` | ✅ Complete |
| **English (Literature)** | `ch7_ada_blackjack` | Unit 3.1: The One Who Survived: Ada Blackjack | 25 | `KB Files/english/literature/ch7_ada_blackjack/` | ✅ Complete |
| **English (Literature)** | `ch8_narayanpur_incident` | Unit 3.2: The Narayanpur Incident (Shashi Deshpande) | 25 | `KB Files/english/literature/ch8_narayanpur_incident/` | ✅ Complete |
| **English (Literature)** | `ch9_florence_nightingale` | Unit 3.3: Florence Nightingale (Emma Lazarus) | 19 | `KB Files/english/literature/ch9_florence_nightingale/` | ✅ Complete |
| **English (Grammar)** | `g1_nouns_classification` | Lesson 1: Nouns — Formation & Classification | 66 | `KB Files/english/grammar/g1_nouns_classification/` | ✅ Complete |
| **English (Grammar)** | `g2_nouns_number_gender` | Lesson 2: Countable & Uncountable Nouns | 79 | `KB Files/english/grammar/g2_nouns_number_gender/` | ✅ Complete |
| **English (Grammar)** | `g3_pronouns` | Lesson 3: Pronouns — Types & Usage | 79 | `KB Files/english/grammar/g3_pronouns/` | ✅ Complete |
| **English (Grammar)** | `g4_case_noun_pronoun` | Lesson 4: Case — Noun and Pronoun | 79 | `KB Files/english/grammar/g4_case_noun_pronoun/` | ✅ Complete |
| **English (Grammar)** | `g5_adjectives` | Lesson 5: Adjectives — Classification & Comparison | 79 | `KB Files/english/grammar/g5_adjectives/` | ✅ Complete |
| **English (Grammar)** | `g6_determiners` | Lesson 6: Determiners — Types & Functions | 79 | `KB Files/english/grammar/g6_determiners/` | ✅ Complete |
| **English (Grammar)** | `g7_articles` | Lesson 7: Articles — Rules & Omission | 79 | `KB Files/english/grammar/g7_articles/` | ✅ Complete |
| **English (Grammar)** | `g8_verbs` | Lesson 8: Verbs — Revision & Forms | 79 | `KB Files/english/grammar/g8_verbs/` | ✅ Complete |
| **English (Grammar)** | `g9_modals_auxiliaries` | Lesson 9: Modals and Auxiliaries | 79 | `KB Files/english/grammar/g9_modals_auxiliaries/` | ✅ Complete |
| **English (Grammar)** | `g10_finite_non_finite` | Lesson 10: Finite and Non-Finite Verbs | 79 | `KB Files/english/grammar/g10_finite_non_finite/` | ✅ Complete |
| **English (Grammar)** | `g17_active_passive` | Lesson 17: Active and Passive Voice | 79 | `KB Files/english/grammar/g17_active_passive/` | ✅ Complete |
| **English (Grammar)** | `v1_vocabulary_word_power` | Lesson 26: Vocabulary & Language Usage | 79 | `KB Files/english/grammar/v1_vocabulary_word_power/` | ✅ Complete |
| **Hindi (Literature)** | `ch1_humko_man_ki_shakti_dena` | पाठ १: हमको मन की शक्ति देना (गुलज़ार) | 19 | `KB Files/hindi/literature/ch1_humko_man_ki_shakti_dena/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Literature)** | `ch2_boodhi_kaki` | पाठ २: बूढ़ी काकी (मुंशी प्रेमचंद) | 23 | `KB Files/hindi/literature/ch2_boodhi_kaki/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Literature)** | `ch3_asafalta_se_seekh` | पाठ ३: असफलता से सीख (गीता तिवारी) | 25 | `KB Files/hindi/literature/ch3_asafalta_se_seekh/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Literature)** | `ch4_yeh_bhi_ek_pariksha` | पाठ ४: यह भी एक परीक्षा (सुरेन्द्र अंचल) | 24 | `KB Files/hindi/literature/ch4_yeh_bhi_ek_pariksha/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Literature)** | `ch5_sneh_bhari_paati` | पाठ ५: स्नेह भरी पाती (उषा वधवा) | 19 | `KB Files/hindi/literature/ch5_sneh_bhari_paati/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Literature)** | `ch6_missile_ke_janak` | पाठ ६: मिसाइल के जनक (डॉ. ए. पी. जे. अब्दुल कलाम) | 16 | `KB Files/hindi/literature/ch6_missile_ke_janak/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Literature)** | `ch7_maa_ka_upahar` | पाठ ७: माँ का उपहार (ऐतिहासिक प्रेरक कथा) | 23 | `KB Files/hindi/literature/ch7_maa_ka_upahar/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Literature)** | `ch8_vishwarajya` | पाठ ८: विश्वराज्य (राष्ट्रकवि मैथिलीशरण गुप्त) | 23 | `KB Files/hindi/literature/ch8_vishwarajya/` | ✅ 100% Textbook Ingested + 50M Exam |
| **Hindi (Grammar)** | `g1_bhasha_lipi_vyakaran` | व्याकरण पाठ १: भाषा, लिपि और व्याकरण | 23 | `KB Files/hindi/grammar/g1_bhasha_lipi_vyakaran/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Grammar)** | `g2_varna_vichar` | व्याकरण पाठ २: वर्ण विचार (स्वर, व्यंजन, उच्चारण) | 27 | `KB Files/hindi/grammar/g2_varna_vichar/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Grammar)** | `g3_shabda_vichar` | व्याकरण पाठ ३: शब्द विचार (तत्सम, तद्भव, रूढ़, यौगिक) | 26 | `KB Files/hindi/grammar/g3_shabda_vichar/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Grammar)** | `g4_upsarg_pratyay` | व्याकरण पाठ ४: शब्द रचना — उपसर्ग एवं प्रत्यय | 19 | `KB Files/hindi/grammar/g4_upsarg_pratyay/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Grammar)** | `g6_samas` | व्याकरण पाठ ६: शब्द रचना — समास | 13 | `KB Files/hindi/grammar/g6_samas/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Grammar)** | `g7_sangya` | व्याकरण पाठ ७: शब्द भेद : विकारी शब्द — संज्ञा | 14 | `KB Files/hindi/grammar/g7_sangya/` | ✅ 100% Textbook & Notebook Ingested |
| **Hindi (Grammar)** | `g20_shabdo_ka_parivar` | व्याकरण पाठ २०: शब्दों का परिवार (Vocabulary) | 12 | `KB Files/hindi/grammar/g20_shabdo_ka_parivar/` | ✅ 100% Textbook Ingested |
| **Hindi (Grammar)** | `g22_muhavare_lokoktiyan` | व्याकरण पाठ २२: मुहावरे एवं लोकोक्तियाँ (Phrases & Proverbs) | 11 | `KB Files/hindi/grammar/g22_muhavare_lokoktiyan/` | ✅ 100% Textbook Ingested |
| **Hindi (Grammar)** | `g23_patra_lekhan` | व्याकरण पाठ २३: पत्र लेखन (Letter Writing) | 10 | `KB Files/hindi/grammar/g23_patra_lekhan/` | ✅ 100% Textbook Ingested |
| **Hindi (Grammar)** | `g25_anuched_lekhan` | व्याकरण पाठ २५: अनुच्छेद लेखन (Paragraph Writing) | 9 | `KB Files/hindi/grammar/g25_anuched_lekhan/` | ✅ 100% Textbook Ingested |

---

## 8. Science (Chemistry) Authoritative Audit & TLBR Rule Implementation (03 October 2026)

### 8.1 Scope & Source Verification
- **Chapter 1: Exploring Substances: Acidic, Basic and Neutral**
  - **Source Material:** `source_materials/science/Chem 1 23 Aug 2026.pdf` (17 scanned pages / book pages 3–34)
  - **Total Items Verified:** **197 items** (12 NCERT, 14 Solved Examples, 65 MCQs [Level 1, Level 2, Level 3 HOTS], 15 FIBs, 15 True/False, 5 Match, 10 Assertion & Reason, 14 Comprehension, 15 Very Short Answer, 10 Short Answer, 10 Long Answer, 5 Numerical, 7 Case Based).
  - **Sub/Superscripts Standard:** 100% pure Unicode (`H₂SO₄`, `HNO₃`, `HCl`, `Ca(OH)₂`, `Mg(OH)₂`, `OH⁻`, `H⁺`, `CuSO₄·5H₂O`, `FeSO₄·7H₂O`, `Na₂CO₃·10H₂O`, `→`).
  - **Theory Modules:** 7 comprehensive sections covering definitions, dissociation, indicators, everyday neutralisation, salts classification, pH scale, acid rain, and all 7 activity corners & illustrations.
- **Chapter 2: The World of Metals and Non-metals**
  - **Source Material:** `source_materials/science/Chem 2 23 Aug 2026 (1).pdf` (17 scanned pages / book pages 35–66)
  - **Total Items Verified:** **208 items** (12 NCERT, 15 Solved Examples, 60 MCQs [Level 1, Level 2, Level 3 HOTS], 15 FIBs, 15 True/False, 5 Match, 10 Assertion & Reason, 13 Comprehension, 15 Very Short Answer, 15 Short Answer, 5 Long Answer, 5 Numerical, 23 Case Based across Cases I to V).
  - **Sub/Superscripts Standard:** 100% pure Unicode (`Al₂O₃`, `Fe₂O₃·xH₂O`, `CuCO₃·Cu(OH)₂`, `Ag₂S`, `ZnSO₄`, `CuSO₄`, `FeSO₄`, `H₂`, `O₂`, `→`).
  - **Theory Modules:** 5 comprehensive sections covering metal/non-metal properties, reactivity series, displacement reactions, corrosion & industrial prevention (galvanizing, electroplating, alloying), commercial alloy tables (10 alloys), non-metal reactions, and comparison tables.

### 8.2 Architectural & Quality Compliance
1. **Dual Schema Enforcement:** Both `questions` and `assessment_items` arrays are populated with identical, validated, high-pedagogical content.
2. **Dual-Store Synchronization:** 100% mirrored between `KB Files/chemistry/` (hierarchical) and `knowledge_base/chemistry/` (flat root mirrors).
3. **No Commercial Publisher Names:** 0 occurrences of proprietary brand names.
4. **Automated Verification:** Verified and passed by `scripts/verify_chemistry_kbs.py` with 405 total items.

---

## 9. Science (Physics) Authoritative Audit & TLBR Rule Implementation (07 October 2026)

### 9.1 Scope & Source Verification
- **Chapter 1: Electricity: Circuits and their Components**
  - **Source Material:** `source_materials/science/phy ch1.pdf` (Pages 1–36)
  - **Total Items Verified:** **251 items** (11 NCERT Section items, 20 Solved Examples, 90 MCQs [Level 1, Level 2, Level 3 HOTS], 18 Fill in the Blanks, 15 True/False, 4 Match the Following, 8 Assertion & Reason, 7 Comprehension items across Passages I–III, 20 Very Short Answer, 15 Short Answer, 8 Long Answer, 4 Numerical problems, 32 Case-Based items across Cases I–VII).
  - **Mathematical & Scientific Formatting:** 100% pure Unicode standard notation (Powers: `²`, `⁻¹⁹`, `¹⁸`; Ohm: `Ω`; Signs: `+`, `−`, `×`; Formulas: `H = I²Rt`, `V = IR`, `I = Q/t`, `W = V·Q`, `P = VI = I²R = V²/R`). Zero raw ASCII approximations.
  - **Theory Modules:** 7 comprehensive sections covering Electric Current & Charge, Potential Difference & Cells/Batteries, Circuit Components & Symbols, Resistance & Factors, Heating Effect of Current & Joule's Law, Safety Devices (Fuses & MCBs), Magnetic Effect of Current & Electromagnets, plus Activity Corners 1–4, Illustrations 1–15, and Competition Windows.
- **Chapter 2: Heat Transfer in Nature & Temperature**
  - **Source Material:** `source_materials/science/phy ch1.pdf` (p. 37 / Book p. 39) + `source_materials/science/phy 2 30-Aug-2026.pdf` (Book pp. 40–73) + `source_materials/science/phy3.pdf` (p. 1 / Book p. 74)
  - **Total Items Verified:** **225 items** (10 NCERT Section items, 17 Solved Examples, 80 MCQs [Level 1, Level 2, Level 3 HOTS], 15 Fill in the Blanks, 14 True/False, 3 Match the Following, 10 Assertion & Reason, 7 Comprehension items across Passages I–III, 25 Very Short Answer, 15 Short Answer, 3 Long Answer, 4 Numerical problems, 24 Case-Based items across Cases I–VII).
  - **Mathematical & Scientific Formatting:** 100% pure Unicode standard notation (Units: `°C`, `°F`, `K`; Conversion formulas: `C/5 = (F − 32)/9 = (K − 273.15)/5`; Thermal conduction, convection, and radiation equations; zero raw ASCII approximations).
  - **Theory Modules:** 5 comprehensive sections covering Concept of Heat vs Temperature, Thermometric Scales & Conversions, Conduction & Thermal Conductivity, Convection & Meteorological Phenomena (Sea & Land Breezes, Monsoons), Radiation & Black Body Properties, and Thermos Flask Mechanics.
- **Chapter 3: Measurement of Time and Motion**
  - **Source Material:** `source_materials/science/phy3.pdf` (Pages 2–31 / Book pp. 75–104)
  - **Total Items Verified:** **192 items** (11 NCERT Section items, 20 Solved Examples, 70 MCQs [Level 1, Level 2, Level 3 HOTS], 10 Fill in the Blanks, 10 True/False, 2 Match the Following, 5 Assertion & Reason, 4 Comprehension items across Passages I–II, 20 Very Short Answer, 10 Short Answer, 5 Long Answer, 3 Numerical problems, 22 Case-Based items across Cases I–V).
  - **Mathematical & Scientific Formatting:** 100% pure Unicode standard notation (Units: `km/h`, `m/s`, `m s⁻¹`, `m/s²`; Powers: `²`, `³`, `⁻¹`; Formulas: `v = d/t`, `T = 2π√(l/g)`, `v_av = Total d / Total t`, `1 km/h = 5/18 m/s`; zero raw ASCII approximations).
  - **Theory Modules:** 6 comprehensive sections covering Historical Timekeeping & Natural Periodic Events (Sundial, Clepsydra, Hourglass, Quartz & NPL Atomic Clocks), Simple Pendulum & Isochronism Mechanics, Motion & Speed & Telemetry Instrumentation (Speedometer vs Odometer), Distance vs Displacement & Scalars vs Vectors, Distance-Time Graphs & Slope Analysis, Displacement-Time & Velocity-Time Graphs & Area Principles, plus Activities 1–2, Illustrations 1–10, and Competition Windows.

### 9.2 Architectural & Quality Compliance
1. **Dual Schema Enforcement:** Both `questions` and `assessment_items` arrays are populated with identical, validated, high-pedagogical content in Chapter 1, Chapter 2, and Chapter 3.
2. **Dual-Store Synchronization:** 100% bitwise parity mirrored between `KB Files/physics/` (hierarchical) and `knowledge_base/physics/` (flat root mirrors).
3. **No Commercial Publisher Names:** 0 occurrences of proprietary brand names across all files.
4. **Automated Verification:** Verified and passed 100% by `scripts/verify_physics_kbs.py` with **668 total items** (Ch1: 251, Ch2: 225, Ch3: 192).

---

## 10. Science (Biology) Authoritative Audit & TLBR Rule Implementation (07 October 2026)

### 10.1 Scope & Source Verification
- **Chapter 2: Adolescence: A Stage of Growth and Change (Reaching the Age of Adolescence)**
  - **Source Material:** `source_materials/science/Bio ch 2-3.pdf` (Pages 1–12 / Book pp. 23–34)
  - **Total Items Verified:** **157 items** (10 Solved Examples, 9 NCERT Section items, 64 MCQs [Level 1, Level 2, Level 3 HOTS], 10 Fill in the Blanks, 10 True/False, 2 Match the Following, 8 Assertion & Reason, 4 Comprehension items, 15 Very Short Answer, 10 Short Answer, 5 Long Answer, 10 Case-Based items across Cases I–II).
  - **Biological & Endocrine Formatting:** 100% pure Unicode standard notation (Hormones: Pituitary GH, TSH, ACTH, FSH, LH; Thyroid thyroxine; Adrenal adrenaline; Pancreas insulin; Testes testosterone; Ovaries estrogen & progesterone; Sex chromosomes: 44 + XY, 44 + XX, 22 + X, 22 + Y; Menstrual cycle phases; Adam's apple larynx cartilage). Zero raw ASCII approximations.
  - **Theory Modules:** 6 comprehensive sections covering Adolescence vs Puberty Milestones, Height Growth Equations & Bone Maturation, Secondary Sexual Characteristics & Adam's Apple, Endocrine Gland System & Hormonal Feedback Loops, Menstrual Cycle Phases & Sex Determination Genetics, and Adolescent Health, Nutrition & Mental Well-being, plus Activities 1–2, Illustrations 1–4, and Competition Windows 1–2.
- **Chapter 3: Life Processes in Animals**
  - **Source Material:** `source_materials/science/Bio ch 2-3.pdf` (Pages 12–34 / Book pp. 35–70)
  - **Total Items Verified:** **250 items** (24 Solved Examples, 10 NCERT Section items, 74 MCQs [Level 1, Level 2, Level 3 HOTS], 21 Fill in the Blanks, 19 True/False, 3 Match the Following, 9 Assertion & Reason, 22 Very Short Answer, 19 Short Answer, 11 Long Answer, 3 Extra Scientific Inquiries, 35 Case-Based MCQs across Cases I–VII).
  - **Biochemical & Physiological Formatting:** 100% pure Unicode standard notation (Chemical formulas: `Ca(OH)₂`, `CaCO₃`, `CO₂`, `O₂`, `H₂O`, `ATP`; Inhaled vs Exhaled gas percentages: 21% vs 16.4% `O₂`, 0.04% vs 4.4% `CO₂`; Equations: `C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + 38 ATP`, `Ca(OH)₂ + CO₂ → CaCO₃ ↓ + H₂O`; Digestive enzymes: ptyalin/amylase, pepsin, trypsin, lipase, maltase; Ruminant 4 chambers: Rumen, Reticulum, Omasum, Abomasum; Avian digestion: Crop, Proventriculus, Gizzard).
  - **Theory Modules:** 6 comprehensive sections covering 5 Stages of Holozoic Nutrition & Ingestion in Lower Taxa (Amoeba pseudopodia, Paramecium cilia, Hydra nematocysts, Starfish stomach eversion), Human Digestive System Anatomy & Enzymatic Digestion, Comparative Digestion in Ruminant Herbivores & Birds, Cellular Respiration vs Mechanical Ventilation, Human Respiratory System Anatomy & Thoracic Pressure Dynamics, and Comparative Respiration across Taxa (Earthworm cutaneous, Insect tracheal, Fish gills counter-current, Frog dual breathing), plus Activities 1–2, Illustrations 1–12, and Competition Windows 1–2.

### 10.2 Architectural & Quality Compliance
1. **Dual Schema Enforcement:** Both `questions` and `assessment_items` arrays are populated with identical, validated, high-pedagogical content in Chapter 2 (157 items) and Chapter 3 (250 items).
2. **Dual-Store Synchronization:** 100% bitwise parity mirrored between `KB Files/biology/` (hierarchical) and `knowledge_base/biology/` (flat root mirrors).
3. **No Commercial Publisher Names:** 0 occurrences of proprietary brand names across all JSON and Markdown files.
4. **Automated Verification:** Verified and passed 100% by `scripts/verify_biology_kbs.py` with **407 total items** (Ch2: 157, Ch3: 250).

---
*Authored & Verified: 07 October 2026 | Pushti Study Hub Core Engineering*



