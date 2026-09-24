# PUSHTI STUDY HUB — MINUTES OF MEETING (MOM)
**Standardized Knowledge Base (KB) Architecture & Automated Question Paper Generation Engine**

* **Date & Timestamp**: 24 September 2026, 03:45 PM IST
* **Participants**: Hirak Soni (Father & Project Architect), Antigravity AI (Pair Programming Assistant)
* **Status**: Codified & Active Standard
* **Version**: 2.5 (English Grammar Batch 5 Active: G4, G5, G6 Case, Adjectives, Determiners)

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
│   │   ├── ch_g1_sandhi_avyaya/                  (44 Items)
│   │   ├── ch_g2_upapada_vibhakti/               (35 Items)
│   │   └── ch_w1_rachanatmak_karyani/            (16 Tasks)
│   ├── mathematics/
│   │   ├── main_source_mtg/
│   │   │   ├── ch1_large_numbers/                (12 Items • MATH_MTG_CH01)
│   │   │   ├── ch2_arithmetic_expressions/        (70 Items • MATH_MTG_CH02)
│   │   │   ├── ch3_decimals/                      (31 Items • MATH_MTG_CH03)
│   │   │   ├── ch4_expressions_letter_numbers/    (18 Items • MATH_MTG_CH04)
│   │   │   ├── ch5_parallel_intersecting_lines/   (8 Items • MATH_MTG_CH05)
│   │   │   ├── ch6_number_play/                   (25 Items • MATH_MTG_CH06)
│   │   │   ├── ch7_tale_of_three_lines_triangles/ (13 Items • MATH_MTG_CH07)
│   │   │   └── ch8_working_with_fractions/        (12 Items • MATH_MTG_CH08)
│   │   └── reference_source_cordova/
│   │       ├── ch1_integers/                      (24 Items • MATH_CORDOVA_CH01)
│   │       ├── ch2_fractions/                     (10 Items • MATH_CORDOVA_CH02)
│   │       ├── ch3_decimals/                      (47 Items • MATH_CORDOVA_CH03)
│   │       ├── ch7_algebraic_expressions/         (10 Items • MATH_CORDOVA_CH07)
│   │       ├── ch11_lines_and_angles/             (33 Items • MATH_CORDOVA_CH11)
│   │       └── ch12_triangles_and_properties/     (36 Items • MATH_CORDOVA_CH12)
│   ├── biology/
│   │   ├── ch2_adolescence/
│   │   │   ├── bio_ch2_adolescence.md
│   │   │   └── bio_ch2_adolescence.json          (109 Items)
│   │   └── ch3_life_processes/
│   │       ├── bio_ch3_life_processes.md
│   │       └── bio_ch3_life_processes.json        (214 Items)
│   ├── chemistry/
│   │   ├── ch1_acids_bases_salts/
│   │   │   ├── chem_ch1_acids_bases_salts.md
│   │   │   └── chem_ch1_acids_bases_salts.json   (188 Items)
│   │   └── ch2_metals_and_non_metals/
│   │       ├── chem_ch2_metals_and_non_metals.md
│   │       └── chem_ch2_metals_and_non_metals.json (196 Items)
│   ├── physics/
│   │   ├── ch1_electricity/
│   │   │   ├── phy_ch1_electricity.md
│   │   │   └── phy_ch1_electricity.json          (120 Items)
│   │   ├── ch2_heat/
│   │   │   ├── phy_ch2_heat.md
│   │   │   └── phy_ch2_heat.json                 (117 Items)
│   │   └── ch3_motion_time/
│   │       ├── phy_ch3_motion_time.md
│   │       └── phy_ch3_motion_time.json          (110 Items)
│   ├── social_science/
│   │   ├── geography/
│   │   │   ├── ch1_interior_earth/               (45 Items)
│   │   │   └── ch2_changing_earth/               (36 Items)
│   │   ├── history/
│   │   │   ├── ch6_first_empires/                (42 Items)
│   │   │   ├── ch7_iron_age/                     (20 Items)
│   │   │   └── ch8_guptas_harsha/                (37 Items)
│   │   └── civics/
│   │       ├── ch13_gender/                      (40 Items)
│   │       ├── ch14_democracy/                   (15 Items)
│   │       └── ch17_markets/                     (56 Items)
│   └── ict/
│       ├── ch1_number_system/                    (108 Items)
│       │   ├── ict_ch1_number_system.md / .json
│       ├── ch2_excel_advanced/                   (74 Items)
│       ├── ch3_artificial_intelligence/          (54 Items)
│       ├── ch4_html_css/                         (82 Items)
│       └── ch5_lists_images/                     (72 Items)
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
│           └── g6_determiners/                   (79 Items • eng_gram_g6_determiners)
├── knowledge_base/                               (Mirrored System Store)
│   ├── sanskrit/
│   ├── mathematics/
│   ├── biology/
│   ├── chemistry/
│   ├── physics/
│   ├── social_science/
│   ├── ict/
│   └── english/
├── admin_worksheet_generator.html
├── scripts/
│   ├── build_chapter_from_kb.py                  (Zero-Token Production HTML Compiler)
│   ├── generate_sanskrit_kbs.py                  (Sanskrit KB Builder)
│   ├── generate_mathematics_kbs.py               (Mathematics KB Builder)
│   ├── generate_physics_kbs.py                   (Physics KB Builder)
│   └── generate_social_science_kbs.py            (Social Science KB Builder)
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

---

## 7. Active Knowledge Base Inventory (Total: 2,944 Standardized Items across 58 Dossiers)

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
| **Sanskrit** | `ch_g1_sandhi_avyaya` | G1: अनुप्रयुक्त-व्याकरणम् (स्वरसन्धिः एवं अव्ययानि) | 44 | `KB Files/sanskrit/ch_g1_sandhi_avyaya/` | ✅ Complete |
| **Sanskrit** | `ch_g2_upapada_vibhakti` | G2: उपपद-विभक्तयः (Upapada Vibhakti & Case Rules) | 35 | `KB Files/sanskrit/ch_g2_upapada_vibhakti/` | ✅ Complete |
| **Sanskrit** | `ch_w1_rachanatmak_karyani` | W1: रचनात्मककार्याणि (पत्रलेखनम्, चित्रवर्णनम्, संवादलेखनम्) | 16 | `KB Files/sanskrit/ch_w1_rachanatmak_karyani/` | ✅ Complete |
| **Mathematics (MTG)** | `ch1_large_numbers` | Large Numbers Around Us (`MATH_MTG_CH01`) | 12 | `KB Files/mathematics/main_source_mtg/ch1_large_numbers/` | ✅ Complete |
| **Mathematics (MTG)** | `ch2_arithmetic_expressions` | Arithmetic Expressions (`MATH_MTG_CH02`) | 70 | `KB Files/mathematics/main_source_mtg/ch2_arithmetic_expressions/` | ✅ Complete |
| **Mathematics (MTG)** | `ch3_decimals` | A Peek Beyond the Point (Decimals) (`MATH_MTG_CH03`) | 31 | `KB Files/mathematics/main_source_mtg/ch3_decimals/` | ✅ Complete |
| **Mathematics (MTG)** | `ch4_expressions_letter_numbers` | Expressions using Letter-Numbers (`MATH_MTG_CH04`) | 18 | `KB Files/mathematics/main_source_mtg/ch4_expressions_letter_numbers/` | ✅ Complete |
| **Mathematics (MTG)** | `ch5_parallel_intersecting_lines` | Parallel and Intersecting Lines (`MATH_MTG_CH05`) | 8 | `KB Files/mathematics/main_source_mtg/ch5_parallel_intersecting_lines/` | ✅ Complete |
| **Mathematics (MTG)** | `ch6_number_play` | Number Play (`MATH_MTG_CH06`) | 25 | `KB Files/mathematics/main_source_mtg/ch6_number_play/` | ✅ Complete |
| **Mathematics (MTG)** | `ch7_tale_of_three_lines_triangles` | A Tale of Three Intersecting Lines (`MATH_MTG_CH07`) | 13 | `KB Files/mathematics/main_source_mtg/ch7_tale_of_three_lines_triangles/` | ✅ Complete |
| **Mathematics (MTG)** | `ch8_working_with_fractions` | Working with Fractions (`MATH_MTG_CH08`) | 12 | `KB Files/mathematics/main_source_mtg/ch8_working_with_fractions/` | ✅ Complete |
| **Mathematics (Cordova)** | `ch1_integers` | Integers (`MATH_CORDOVA_CH01`) | 24 | `KB Files/mathematics/reference_source_cordova/ch1_integers/` | ✅ Complete |
| **Mathematics (Cordova)** | `ch2_fractions` | Fractions (`MATH_CORDOVA_CH02`) | 10 | `KB Files/mathematics/reference_source_cordova/ch2_fractions/` | ✅ Complete |
| **Mathematics (Cordova)** | `ch3_decimals` | Decimals (`MATH_CORDOVA_CH03`) | 47 | `KB Files/mathematics/reference_source_cordova/ch3_decimals/` | ✅ Complete |
| **Mathematics (Cordova)** | `ch7_algebraic_expressions` | Algebraic Expressions (`MATH_CORDOVA_CH07`) | 10 | `KB Files/mathematics/reference_source_cordova/ch7_algebraic_expressions/` | ✅ Complete |
| **Mathematics (Cordova)** | `ch11_lines_and_angles` | Lines and Angles (`MATH_CORDOVA_CH11`) | 33 | `KB Files/mathematics/reference_source_cordova/ch11_lines_and_angles/` | ✅ Complete |
| **Mathematics (Cordova)** | `ch12_triangles_and_properties` | The Triangle and Its Properties (`MATH_CORDOVA_CH12`) | 36 | `KB Files/mathematics/reference_source_cordova/ch12_triangles_and_properties/` | ✅ Complete |
| **Biology** | `ch2_adolescence` | Reaching the Age of Adolescence | 109 | `KB Files/biology/ch2_adolescence/` | ✅ Complete |
| **Biology** | `ch3_life_processes` | Life Processes (Control & Coordination) | 214 | `KB Files/biology/ch3_life_processes/` | ✅ Complete |
| **Chemistry** | `ch1_acids_bases_salts` | Acids, Bases and Salts | 188 | `KB Files/chemistry/ch1_acids_bases_salts/` | ✅ Complete |
| **Chemistry** | `ch2_metals_and_non_metals` | Metals and Non-Metals | 196 | `KB Files/chemistry/ch2_metals_and_non_metals/` | ✅ Complete |
| **Physics** | `ch1_electricity` | Electricity: Circuits & Components | 120 | `KB Files/physics/ch1_electricity/` | ✅ Complete |
| **Physics** | `ch2_heat` | Heat Transfer & Temperature | 117 | `KB Files/physics/ch2_heat/` | ✅ Complete |
| **Physics** | `ch3_motion_time` | Measurement of Time and Motion | 110 | `KB Files/physics/ch3_motion_time/` | ✅ Complete |
| **Social Science (Geo)** | `ch1_interior_earth` | Interior of the Earth | 45 | `KB Files/social_science/geography/ch1_interior_earth/` | ✅ Complete |
| **Social Science (Geo)** | `ch2_changing_earth` | Our Changing Earth | 36 | `KB Files/social_science/geography/ch2_changing_earth/` | ✅ Complete |
| **Social Science (Hist)** | `ch6_first_empires` | The First Indian Empires (The Mauryas) | 42 | `KB Files/social_science/history/ch6_first_empires/` | ✅ Complete |
| **Social Science (Hist)** | `ch7_iron_age` | India in the Iron Age | 20 | `KB Files/social_science/history/ch7_iron_age/` | ✅ Complete |
| **Social Science (Hist)** | `ch8_guptas_harsha` | India from 4th to 7th Century CE (Guptas & Harsha) | 37 | `KB Files/social_science/history/ch8_guptas_harsha/` | ✅ Complete |
| **Social Science (Civ)** | `ch13_gender` | Understanding Gender | 40 | `KB Files/social_science/civics/ch13_gender/` | ✅ Complete |
| **Social Science (Civ)** | `ch14_democracy` | How Does Democracy Work? (State Government) | 15 | `KB Files/social_science/civics/ch14_democracy/` | ✅ Complete |
| **Social Science (Civ)** | `ch17_markets` | Markets Around Us | 56 | `KB Files/social_science/civics/ch17_markets/` | ✅ Complete |
| **ICT** | `ch1_number_system` | Number System & Binary Arithmetic | 108 | `KB Files/ict/ch1_number_system/` | ✅ Complete |
| **ICT** | `ch2_excel_advanced` | Advanced Features of Excel | 74 | `KB Files/ict/ch2_excel_advanced/` | ✅ Complete |
| **ICT** | `ch3_artificial_intelligence`| Artificial Intelligence | 54 | `KB Files/ict/ch3_artificial_intelligence/` | ✅ Complete |
| **ICT** | `ch4_html_css` | More on CSS & HTML | 82 | `KB Files/ict/ch4_html_css/` | ✅ Complete |
| **ICT** | `ch5_lists_images` | Lists and Tables in HTML5 | 72 | `KB Files/ict/ch5_lists_images/` | ✅ Complete |
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

---
*Authored & Verified: 24 September 2026 | Pushti Study Hub Core Engineering*

