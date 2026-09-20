# PUSHTI STUDY HUB — MINUTES OF MEETING (MOM)
**Standardized Knowledge Base (KB) Architecture & Automated Question Paper Generation Engine**

* **Date & Timestamp**: 20 September 2026, 12:30 PM IST
* **Participants**: Hirak Soni (Father & Project Architect), Antigravity AI (Pair Programming Assistant)
* **Status**: Codified & Active Standard
* **Version**: 1.0 (Initial Foundation & ICT Pilot)

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

All Knowledge Base files reside in the dedicated root directory knowledge_base/, categorized by subject and chapter:

`
d:\Users\expor\Downloads\Codes\
├── knowledge_base/
│   ├── ict/
│   │   ├── ict_ch1_number_system.md
│   │   ├── ict_ch1_number_system.json
│   │   ├── ict_ch2_excel_advanced.md
│   │   ├── ict_ch2_excel_advanced.json
│   │   ├── ict_ch3_artificial_intelligence.md
│   │   └── ict_ch3_artificial_intelligence.json
│   ├── maths/                 (Upcoming Phase)
│   ├── science/               (Upcoming Phase)
│   └── hindi/                 (Upcoming Phase)
├── admin_worksheet_generator.html
└── KNOWLEDGE_BASE_MOM.md      (This Document)
`

### File Pair Principle
Each chapter maintains a synchronized **Dual-File Pair**:
1. **Human/AI Dossier (.md)**: Formatted for quick reading, conceptual review, and LLM context injection.
2. **Machine Item Bank (.json)**: Formatted for immediate algorithmic filtering, shuffling, and rendering by dmin_worksheet_generator.html.

---

## 3. Metadata & Tagging Taxonomy

Every entry in the Knowledge Base is strictly annotated with standardized attributes:

### 3.1 Source Taxonomy (source)
| Tag Key | Display Label | Description |
| :--- | :--- | :--- |
| 	extbook_exercise | **Textbook Exercise** | Direct questions, exercises, and problem sets from the prescribed school textbook. |
| chapter_notes | **Chapter Notes & Theory** | Core theoretical explanations, definitions, laws, formulas, and step-by-step model examples. |
| school_worksheet | **School Assessment** | Questions extracted from school teacher test papers, unit assessment sheets, and periodic tests. |
| 
esearched_enrichment | **Researched Enrichment** | High-yield extra context, real-world tech trivia, historical milestones, and industry applications gathered from research. |
| exam_trap | **Common Pitfall / Trap** | Classic examination trick questions, negative-marking traps, and frequent student mistakes. |

### 3.2 Challenge & Difficulty Levels (difficulty)
* **easy (Level 1 — Confidence Builder)**: Direct factual recall, straightforward definitions, basic binary rules, single-cell Excel formulas.
* **medium (Level 2 — School Standard)**: Multi-step conversions, standard application problems, sorting/filtering scenarios, standard MCQs.
* **hard_hots (Level 3 — Advanced HOTS / Olympiad)**: Complex binary arithmetic with multiple carries/borrows, nested formula logic, multi-domain AI synergy, boundary conditions.

### 3.3 Question Types (	ype)
* mcq: Multiple Choice Question with 4 distinct options and detailed distractor analysis.
* ib: Fill in the Blanks with exact string matching and acceptable aliases.
* 	f: True / False assertion with logical justification.
* conversion: Mathematical or numeric step-by-step conversion drill.
* short_answer: 2 to 3 marks conceptual explanation.
* long_answer: 4 to 5 marks comprehensive analysis or comparative table.

---

## 4. Admin Worksheet & Exam Generator Governance

1. **Admin Exclusivity**:
   - The Worksheet Generator is housed in [dmin_worksheet_generator.html](file:///d:/Users/expor/Downloads/Codes/admin_worksheet_generator.html).
   - Guarded by Admin PIN verification (1985) and parent role session state.
2. **Parametric Generation Controls**:
   - Filter by source: choose strictly Textbook Exercises, include Chapter Notes, or inject Researched Enrichment.
   - Filter by difficulty: Easy (100% basics), Standard (70/30), or HOTS Challenge.
   - Target length: 10 Marks (Quick Recap), 20 Marks (Periodic Test), or 40 Marks (Mid-Term Blueprint).
3. **Dual-Mode Output**:
   - **Student View**: Clean, printable worksheet with name/date headers, question prompts, and response lines.
   - **Teacher / Admin View**: Displays full step-by-step answers, KaTeX conversion grids, and marking rubrics.
   - **Print Optimization**: High-contrast @media print layout formatting to standard A4 paper without clipped margins or background bleed.

---

## 5. Maintenance & Revision Protocol

* **Living Document**: This MOM must be updated whenever:
  1. A new subject is added to the Knowledge Base (e.g. Mathematics, Science).
  2. A new question type or taxonomy tag is introduced.
  3. School test patterns evolve.
* **Quality Gate Integration**: Merged with Master Unified SOP v3.3 Section 1.6 (Strict Anonymization) and Section 4.4 (Centralized Tests Architecture).

---
*Authored & Verified: 20 September 2026 | Pushti Study Hub Core Engineering*
