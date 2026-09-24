---
name: KnowledgeBase
description: Core Knowledge Base Protocol for Pushti Study Hub. Mandates that AI models (Gemini, Claude, Antigravity) ALWAYS refer to SOP first, prioritize pre-compiled Knowledge Base files (in 'KB Files/<subject>/<chapter>/' and 'knowledge_base/<subject>/') before processing heavy HTML or performing web searches, build missing KB files before proceeding, continuously update KB files with new knowledge, and proactively provide smart suggestions to minimize token usage.
---

# Knowledge Base (KB) Autonomous Protocol & Token Optimization Standard

This rule governs all interactions involving curriculum queries, explanations, revision drills, question paper drafting, and worksheet generation across all subjects (Science, ICT, Mathematics, Social Science, Hindi, English, Sanskrit).

---

## 1. SOP-First Principle (Mandatory Prerequisite)
Before processing ANY request, analyzing files, or generating content:
- **ALWAYS refer to `SOP.md`** (Master Unified SOP v3.3) for:
  - Strict publication & school anonymization (Section 1.6 & 1.7).
  - Explicit omission of "Class 7" redundancy (Section 1.1).
  - Mandatory Python UTF-8 file operations (Section 1.5).
  - 5-tab architectural compliance and self-sufficiency (Section 1.3).

---

## 2. Fixed KB Location & "KB-First" Mandatory Retrieval
The authoritative, permanent storage location for chapter knowledge bases is:
```text
d:\Users\expor\Downloads\Codes\KB Files\<subject>\<chapter_folder>\
```
*(and mirrored in `d:\Users\expor\Downloads\Codes\knowledge_base\<subject>\` for automated test generator compatibility).*

### Mandatory Operational Protocol:
1. **Search KB First**: Whenever a curriculum question is asked, a concept explanation is requested, or a worksheet/exam is to be generated:
   - **DO NOT** perform broad web searches.
   - **DO NOT** ingest 4,000–9,000 line production HTML files (e.g. `chapters/science/science_bio_ch2.html`), which waste 85–90% of tokens on CSS/JS/DOM markup.
   - **ALWAYS** inspect and load the pre-compiled `<chapter>.md` and `<chapter>.json` files from `KB Files/<subject>/<chapter_folder>/` first.
2. **Build KB First If Missing**: If a requested chapter does not yet possess a KB file in `KB Files/`:
   - **FIRST** extract, compile, and store the chapter's dual-file pair (`<chapter>.md` and `<chapter>.json`) under `KB Files/<subject>/<chapter_folder>/`.
   - **THEN** proceed to fulfill the user's specific request using the newly compiled KB.
3. **Living Knowledge Base (Continuous Update Protocol)**:
   - Any new pedagogical insight, teacher worksheet drill, school assessment problem, correction, or Olympiad trick discovered or generated regarding that chapter **MUST be immediately appended and synchronized** into both the `.md` dossier and `.json` item bank of that chapter's KB file.

---

## 3. Dual-File Structure & Tagging Taxonomy
Every chapter knowledge base must maintain a synchronized pair:
1. **Human & AI Dossier (`.md`)**:
   - Executive Summary & Curriculum Scope.
   - Core Conceptual Theory & Notes (tagged by topic).
   - Complete Tagged Question & Assessment Bank (with question prompts, options, answers, and rubrics).
2. **Machine Item Bank (`.json`)**:
   - Algorithmic structure with keys: `subject`, `chapter_num`, `chapter_title`, `summary`, `theory_summary`, and `questions`.
   - Each question object includes: `id`, `source`, `type`, `difficulty`, `marks`, `topic`, `question`, `options`, `answer`, `explanation`.

### Source Taxonomy (`source`):
- `textbook_exercise`: Direct questions from prescribed core textbooks.
- `chapter_notes`: Core theory, laws, definitions, and physiological/mathematical models.
- `school_worksheet`: Internal periodic tests, teacher worksheets, and revision papers.
- `researched_enrichment`: High-yield real-world context, history, and scientific trivia.
- `exam_trap`: Common student misconceptions, tricky distractors, and calculation pitfalls.

---

## 4. Proactive Token Optimization Standard
Every AI assistant (Gemini, Claude, Antigravity) must practice proactive token conservation:
1. **Suggest KB Referencing**: When the user requests a drill or revision sheet, suggest querying the KB JSON/MD rather than parsing full HTML templates.
2. **Use Targeted Reads**: Specify exact line slices (`StartLine`/`EndLine`) when viewing files rather than loading whole 800+ line blocks.
3. **Leverage Client-Side Generation**: Remind users that `admin_worksheet_generator.html` compiles print-ready, randomized question papers client-side with 0 API token cost.
4. **Batch Extractions**: When parsing new chapters, extract and compile structured data in Python scripts rather than dumping hundreds of raw strings into conversation context.
