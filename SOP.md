# Standard Operating Procedure (SOP) / GITA

This document outlines the standard formatting and coding practices for the Pushti Study Hub project.

## 1. Standard Header Format

All generated HTML pages (including Claude Notes and Gemini Practice modules) **MUST** use the following standardized sticky header format instead of breadcrumbs. This ensures a unified UI across the entire platform.

### CSS (Standard Header)
```css
/* Standard Header */
.standard-header {
    display: flex;
    align-items: center;
    padding: 15px 40px;
    background: rgba(30, 41, 59, 0.95);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
    margin: -2rem -2rem 2rem -2rem; /* Adjust according to body padding */
}
body {
    padding-top: 0; /* Reset top padding since header handles it */
}
.standard-back-btn {
    color: #f8fafc;
    text-decoration: none;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    transition: background 0.2s;
    border: 1px solid rgba(255, 255, 255, 0.1);
}
.standard-back-btn:hover {
    background: rgba(255, 255, 255, 0.1);
}
.standard-subject-title {
    color: #f8fafc;
    font-size: 1.25rem;
    font-weight: 600;
    margin-left: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}
```

### HTML (Standard Header)
```html
<header class="standard-header">
    <a href="../../../{link_to_subject_index}.html" class="standard-back-btn">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        Back to Hub
    </a>
    <div class="standard-subject-title">
        {Subject Name} <span style="color:#64748b;">|</span> {Current Page Name}
    </div>
</header>
```

*Rule created: 2026-09-02*

## 2. Checkpoint SOP (Verification Before Completion)

Before confirming to the user that any task (like building a chapter, notes, practice module, or generating content) is complete, the agent MUST perform the following mandatory verification steps:

1. **Data Accuracy Check**: Ensure that the content (e.g., chapter names, video titles, thumbnails, interactive questions) matches the specific subject/chapter being worked on, and is not a leftover artifact from a copied template.
2. **Visual & UI Verification**: Verify that the Standard Header is present, the Firebase Timer is properly injected, and no placeholder content remains visible in the production file.
3. **Local Testing**: Check for any obvious syntax errors (e.g., missing closing tags or broken URLs) in the generated HTML.
4. **Commit & Push**: Ensure all verified files are added, committed, and pushed to the remote repository so the user can see them live.

## 3. Exam Pattern & Assessment Blueprint Standards (The Pop-Up Architecture)

When integrating examination blueprints, mark distributions, or question-type patterns into `midterm.html` (or any assessment schedule), follow the **Science Exam Pattern model**:

### 3.1 Main Assessment Table Rules
1. **Dedicated Column**: Maintain the dedicated `Exam Pattern` column as the 5th column in `midterm.html` (`width="180"` to `width="200"`).
2. **Pending Subjects**: Subjects without finalized blueprints must display a clean, muted placeholder: `<td class="center-col" style="color:var(--text-muted); vertical-align:middle; font-size:1.1rem;">—</td>`.
3. **Clickable Subject Badges**:
   * For composite subjects (e.g., Science: Physics, Chemistry, Biology) or single subjects (Maths, ICT, English), render clean, clickable badge buttons (`.pattern-badge`).
   * Each badge displays the subject icon (⚡, 🧪, 🧬, 📐), name, and total weightage (`25M`, `30M`, `80M`).
   * An additional "All Sections / Summary" badge opens the master comparison matrix.

### 3.2 Modal Pop-Up & Zero-Scrollbar Mandate
Do **NOT** cram lengthy question distributions or tables directly into the table cells. Always display them in an accessible, interactive pop-up modal (`.exam-modal-overlay` + `.exam-modal-card`):
1. **Direct Section Linking**: Clicking any badge opens the modal directly with that subject's tab active.
2. **Top Navigation Tabs**:
   * Include clean tab buttons (`.modal-tab-btn`) for quick switching across branches and the master summary.
   * Mandate `overflow: visible; flex-wrap: wrap; justify-content: center;` to strictly eliminate horizontal scrollbars on the tab bar.
3. **The 3 × 2 Balanced Grid Layout (Zero-Scrollbar Architecture)**:
   * Vertical 1-column card stacks are **forbidden** inside modals because they cause tall vertical scrollbars on standard laptop screens.
   * Organize question breakdowns into a **2-column compact grid** (`.pattern-grid-2col`), yielding a balanced **3-row × 2-column** layout:
     * **Row 1**: `MCQ & Assertion-Reason` (Left) | `Very Short Answer (VSA)` (Right)
     * **Row 2**: `Short Answer (SA)` (Left) | `Case Study` (Right)
     * **Row 3**: `Long Answer (LA)` (Left) | `💡 Revision Priority / Study Tip` (Right)
   * This limits total question breakdown height to **~140px**, allowing the entire modal (header + tabs + hero banner + 3×2 grid) to fit comfortably within the viewport without triggering scrollbars.
4. **Master Summary Tab**:
   * Highlight the master scoring formula (e.g., `20 × 1M + 6 × 2M + 7 × 3M + 3 × 4M + 3 × 5M = 80 Marks`).
   * Include a side-by-side comparison table comparing Question Type, Marks/Q, section distributions, total questions, and total marks.
   * Provide a collapsible toggle button to view the original official school blueprint infographic (`source_materials/{subject}/...`).
5. **Asset Storage & Persistence**:
   * Always save and commit uploaded blueprint images/infographics to `source_materials/{subject}/` and `artifacts/`. Never leave them only in temporary upload directories.
6. **Universal Modal Controls**:
   * Dismiss smoothly on clicking `✕`, clicking the backdrop overlay, or pressing `Escape`.
   * Lock background page scroll while the modal is active (`document.body.style.overflow = 'hidden'`).
   * Respect dark & light mode dynamically using CSS variables (`var(--surface)`, `var(--text-main)`, `var(--border)`, etc.).

---

## 4. Timetable, Assessment Schedules & Syllabus Maintenance SOP

To ensure the study hub remains reliable, accurate, and up-to-date for years to come across academic sessions:

### 4.1 Master Files & Routing
* **`midterm.html`**: Master assessment timetable, live countdown timer, and exam pattern blueprint.
* **`timetable.html`**: Weekly class timetable (SBPS Class 7 Alpha) and daily schedule.
* **Navigation Links**: Accessible from the global header (`📅 Time Table` & `🎯 Mid-Term Syllabus`) across all hub pages (`index.html`, `dashboard.html`, and subject index pages).

### 4.2 Updating Exam Dates & Live Countdown
1. **Target Date in Countdown Function**:
   * In `midterm.html`, update the target timestamp in `updateMainCountdown()`:
     ```javascript
     const targetDate = new Date('YYYY-MM-DDT00:00:00').getTime();
     ```
   * The countdown automatically renders `-[X] Days` before exams, changes to a green pulsing `"Ongoing!"` badge during the exam period, and hides/labels `"Completed"` when concluded.
2. **Synchronized Dates**:
   * When assessment dates change, update the `Date` column in `midterm.html` (`DD/MM/YYYY`) and the corresponding exam date cards/table in `timetable.html`.

### 4.3 Updating Syllabus Content & Chapter Badges
1. **Accordion Hierarchy**:
   * Group subjects into clean, collapsible accordions using `.s-category` (e.g., *Geography (2)*, *History (3)*, *अध्यायाः (Chapters 1–6)*).
   * All accordion lists use `.syllabus-list` (collapsed by default, expandable on click).
2. **Standardized AI Version Pills**:
   * When linking learning modules, use the designated pill classes:
     * `.pill-gemini`: Gemini extraction module (`<i class="fas fa-sparkles"></i> Gemini`)
     * `.pill-claude`: Claude conceptual notes (`<i class="fas fa-brain"></i> Claude`)
     * `.pill-gemini-n`: Unified notes module (`<i class="fas fa-book-open"></i> Gemini-N`)
3. **Relative URL Integrity**:
   * Relative paths from `midterm.html` (at repository root) must link to `chapters/{subject}/{file}.html` or `source_materials/chapters/{subject}/{file}.html`.

### 4.4 Mandatory File Editing & Sync Protocol
1. **UTF-8 Python Mandate**:
   * Never use Windows PowerShell redirectors (`>`, `Set-Content`) to edit `midterm.html`, `timetable.html`, or SOPs, as PowerShell defaults to Windows-1252 encoding and permanently corrupts emojis (`🎯`, `📅`, `⚡`, `🧪`, `🧬`) into `??`.
   * Always read, modify, and write files using Python with `encoding='utf-8'`.
2. **Table Structure Verification**:
   * After any change to `midterm.html`, verify that all 7 subject rows have exactly 5 columns matching `<thead>`.
3. **Git Commit & Push**:
   * Immediately stage, commit with a descriptive message, and push to `origin/master` so GitHub Pages deploys live without delay.
