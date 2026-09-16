# PUSHTI STUDY HUB — DESIGN SOP (Consolidated into SOP.md v3.0)
> **NOTE**: All guidelines from this document have been consolidated, enhanced, and standardized into the master authoritative standard:
> 👉 **[SOP.md](file:///d:/Users/expor/Downloads/Codes/SOP.md)** (Master Unified SOP v3.0)
> Please refer directly to [SOP.md](file:///d:/Users/expor/Downloads/Codes/SOP.md) for the active rules, subject-wise architectures, and QA verification gates.

---
## 0. WHO THIS IS FOR

This SOP is given to any AI model (Claude, Gemini, GPT, etc.) to build pages for the **Pushti Study Hub** — a Class 7 CBSE study website built by Hirak Soni for his daughter Pushti.

**When in doubt: follow the rules here EXACTLY. Do not improvise.**

---

## 1. IDENTITY & PURPOSE

| Field | Value |
|-------|-------|
| Project | Pushti Study Hub |
| Student | Pushti Soni, Class 7, CBSE board |
| Textbook (Maths) | Ganita Prakash (new NCERT 2024-25 edition) |
| Textbook (English) | Honeycomb |
| Goal | Make studying fun, accurate, and self-sufficient |
| Repo root | `d:\Users\expor\Downloads\Codes\` |
| GitHub | `https://github.com/hiraksoni/pushti-study-hub` |
| Preferred AI style | Claude-style |

---

## 2. FILE & PATH RULES

### 2.1 File Naming Convention

```
[subject]_[chapter|topic]_notes.html       <- primary notes pages
[subject]_[chapter|topic]_practice.html    <- practice-only pages
[subject]_[chapter|topic].html             <- full interactive chapter
```

### 2.2 File Locations

```
repo_root/
  index.html                               <- home
  maths_index.html                         <- maths chapter index
  source_materials/
    chapters/
      maths/
        maths_ch1_notes.html               <- DEPTH 3 from root
        maths_ch2_notes.html
      english/
        english_ch1_notes.html
  chapters/
    maths/
      maths_ch2.html                       <- DEPTH 2 from root
  js/
    scroll_to_top.js
  firebase-config.js
```

### 2.3 CRITICAL: Relative Paths by Depth

| File location | To root | Firebase | Scroll script | Home |
|---------------|---------|----------|---------------|------|
| repo root | `./` | `firebase-config.js` | `js/scroll_to_top.js` | `index.html` |
| `chapters/maths/` | `../../` | `../../firebase-config.js` | `../../js/scroll_to_top.js` | `../../index.html` |
| `source_materials/chapters/maths/` | `../../../` | `../../../firebase-config.js` | `../../../js/scroll_to_top.js` | `../../../index.html` |

**CHECKLIST before finalizing any file:**
- [ ] Home link has correct depth?
- [ ] Maths index link has correct depth?
- [ ] Firebase script has correct depth?
- [ ] Scroll script has correct depth?

---

## 3. HTML HEAD REQUIREMENTS (ALL PAGES)

```html
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[Page Title] | Pushti Study Hub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false});"></script>
```

**FORBIDDEN:**
- NO Bootstrap, Tailwind, Material UI, any CSS framework
- NO jQuery, React, Vue, Angular, any JS framework

---

## 4. CSS ARCHITECTURE — NON-NEGOTIABLE

### 4.1 Mandatory Variable Block

```css
:root {
  --bg-base:        #060d16;
  --surface:        #0a1726;
  --surface-glass:  rgba(10,23,38,0.95);
  --bg-card:        rgba(13,29,48,0.80);
  --bg-card-hover:  rgba(16,36,60,0.95);
  --border:         rgba([R],[G],[B],0.18);
  --border-hover:   rgba([R],[G],[B],0.45);
  --primary:        [chapter hex];
  --primary-glow:   [lighter shade];
  --primary-subtle: rgba([R],[G],[B],0.12);
  --primary-deep:   rgba([R],[G],[B],0.06);
  --accent-purple:        #a855f7;
  --accent-purple-subtle: rgba(168,85,247,0.12);
  --accent-amber:         #f59e0b;
  --accent-amber-subtle:  rgba(245,158,11,0.12);
  --accent-cyan:          #06b6d4;
  --accent-cyan-subtle:   rgba(6,182,212,0.12);
  --accent-rose:          #f43f5e;
  --accent-rose-subtle:   rgba(244,63,94,0.12);
  --text-title:  #f0fdf4;
  --text-main:   #cbd5e1;
  --text-muted:  #94a3b8;
  --text-dim:    #64748b;
  --shadow-sm: 0 2px 8px rgba(0,0,0,0.30);
  --shadow-md: 0 4px 20px rgba(0,0,0,0.45);
  --shadow-lg: 0 8px 36px rgba(0,0,0,0.60);
  --font-head: 'Outfit', sans-serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --header-h: 60px;
  --jump-h:   46px;
}

[data-theme="light"] {
  --bg-base:       #f0fdf8;
  --surface:       #ffffff;
  --surface-glass: rgba(255,255,255,0.97);
  --bg-card:       rgba(255,255,255,0.95);
  --bg-card-hover: rgba(240,253,248,1);
  --primary:       [slightly darker shade];
  --text-title:    #064e3b;
  --text-main:     #1e293b;
  --text-muted:    #475569;
  --text-dim:      #94a3b8;
  --shadow-sm:     0 2px 8px rgba(0,0,0,0.08);
  --shadow-md:     0 4px 20px rgba(0,0,0,0.12);
  --shadow-lg:     0 8px 36px rgba(0,0,0,0.15);
}
```

### 4.2 Forbidden CSS Patterns

| DO NOT | DO INSTEAD |
|--------|------------|
| `color: #10b981` | `color: var(--primary)` |
| `background: #060d16` | `background: var(--bg-base)` |
| `font-family: 'Fredoka One'` | `font-family: var(--font-head)` |
| `element.style.display = 'block'` | `element.classList.add('open')` |
| `!important` anywhere | Fix specificity properly |

---

## 5. COLOR PALETTE — PER CHAPTER

| Chapter | Title | Primary | Light title text |
|---------|-------|---------|------------------|
| Maths Ch 1 | Large Numbers | `#0284c7` sky blue | `#0c4a6e` |
| Maths Ch 2 | Arithmetic Expressions | `#10b981` emerald | `#064e3b` |
| Maths Ch 3 | A Peek Beyond the Point | `#8b5cf6` violet | `#3b0764` |
| Maths Ch 4 | TBD | `#f59e0b` amber | `#78350f` |
| Maths Ch 5 | TBD | `#06b6d4` cyan | `#164e63` |
| English Ch 1 | The Honeycomb | `#ec4899` pink | `#831843` |
| English Ch 2 | TBD | `#f97316` orange | `#7c2d12` |

---

## 6. TYPOGRAPHY RULES

| Element | Font | Weight | Size |
|---------|------|--------|------|
| h1, h2 headings | Outfit | 700-900 | 1.3-2rem |
| Card headings | Outfit | 700 | 0.9-1rem |
| Body text | Inter | 400 | 0.88-0.95rem |
| Labels, badges | Outfit | 600-700 | 0.68-0.75rem |
| Code, filenames | JetBrains Mono | 400-500 | 0.85rem |

Line height: always 1.65-1.75 for body text.

---

## 7. LAYOUT RULES

### 7.1 Max Width
`max-width: 960px; margin: 0 auto;` on all content wrappers.

### 7.2 Sticky System (Notes Pages)
```
Tier 1: .site-header  — sticky, top: 0,    z-index: 100, height: 60px
Tier 2: .jump-bar     — sticky, top: 60px, z-index: 90,  height: 46px
```
For full interactive pages with tabs, add:
```
Tier 3: .subnav       — sticky, top: 106px, z-index: 80, height: 46px
```

### 7.3 Header Contents
- LEFT: breadcrumb nav (Home / Subject / Chapter name)
- RIGHT: chapter badge + theme toggle button

### 7.4 NO Hero Banners
- FORBIDDEN: full-width colorful hero sections
- REQUIRED: compact `.chapter-intro` block only

### 7.5 Notes Pages = Single Scroll
- NO internal tabs hiding content
- YES: sticky jump bar with anchor pills to sections

### 7.6 Zero Horizontal Scroll Mandate on Tab & Pill Bars
- FORBIDDEN: `overflow-x: auto` with `white-space: nowrap` on tab bars or subtab containers. It creates unsightly horizontal scrollbars across desktop screens.
- REQUIRED: Always use `flex-wrap: wrap; gap: 8px 6px;` on all tab bars (`.activity-tab-bar`, `.modal-tabs`, `.subnav-pills`) with `overflow-x: hidden`. Pills must wrap cleanly onto 1–2 rows so all options remain immediately visible without horizontal scrolling.

### 7.7 Universal Data & Table Alignment Standard (Left for Text, Right for Numbers)
- **Left Alignment for Text (`text-align: left;`)**: All text columns (questions, topics, options, explanations, descriptions) and their corresponding headers must be left-aligned.
- **Right Alignment for Numbers (`text-align: right;`)**: All numeric data (`Q#`, counts, scores, marks, percentages, quantities) and their corresponding headers must be right-aligned with `font-variant-numeric: tabular-nums;` so digits align vertically for easy scanning.

---

## 8. CONTENT RULES

### 8.1 Math
- ALL math in KaTeX: `$inline$` or `$$display$$`
- NEVER plain text math (no `3 x 4` — use `$3 \times 4$`)

### 8.2 Examples
- Numbered steps with circle badge
- Final answer in `.formula-box`
- Collapsible — default CLOSED

### 8.3 Exercises
- Answers hidden by default
- `.reveal-btn` reveals `.answer-panel`
- Show 3 self-assessment buttons: Got It / Partial / Missed

### 8.4 MCQ Options
- 2x2 grid layout (NOT vertical list)
- Min-height 44px per option

### 8.5 Extra Content (Beyond NCERT)
- Tag with `[Extra]` badge
- Place in `id="missing"` or `id="extras"` section

### 8.6 Videos
- Linked cards ONLY — never `<iframe>` embeds
- Opens YouTube in new tab

### 8.7 Real-Life Applications
- Minimum 2 per chapter using `.callout-real`
- Indian context: cricket, markets, GST, school

---

## 9. JAVASCRIPT RULES

### 9.1 Forbidden
- jQuery, React, Vue, Angular
- `element.style.display = 'block'` for show/hide
- Anonymous inline onclick handlers

### 9.2 Required Patterns

Theme toggle (MUST be on every page):
```javascript
function toggleTheme() {
  const html = document.documentElement;
  const isDark = html.getAttribute('data-theme') === 'dark';
  html.setAttribute('data-theme', isDark ? 'light' : 'dark');
  document.getElementById('themeIcon').className = isDark ? 'fas fa-sun' : 'fas fa-moon';
  localStorage.setItem('pushti-theme', isDark ? 'light' : 'dark');
}
(function() {
  const saved = localStorage.getItem('pushti-theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
})();
```

Show/hide (use class toggling, not style.display):
```javascript
function revealAnswer(id) {
  document.getElementById(id + '-ans').classList.toggle('open');
}
// CSS: .answer-panel { display: none; }
// CSS: .answer-panel.open { display: block; }
```

### 9.3 External Scripts (end of body)
```html
<script src="../../../firebase-config.js"></script>
<script src="../../../js/scroll_to_top.js"></script>
```

---

## 10. QUALITY CHECKPOINTS (Run Before Done)

- [ ] CP-1: No hardcoded colors — all `var(--...)` 
- [ ] CP-2: File paths correct — count depth, verify prefix
- [ ] CP-3: All math uses KaTeX `$...$` syntax
- [ ] CP-4: Dark + light theme blocks both complete; theme toggle present
- [ ] CP-5: No hero banner — compact `.chapter-intro` only
- [ ] CP-6: Single scroll (notes pages) — no internal tabs
- [ ] CP-7: Answers hidden by default — `.answer-panel { display: none }`
- [ ] CP-8: Firebase + scroll script with correct paths at end of body
- [ ] CP-9: Mobile responsive — has `@media (max-width: 640px)` rules
- [ ] CP-10: Correct chapter color from Section 5

---

## 11. ANTI-PATTERN LIST

| Anti-Pattern | Why Wrong |
|-------------|-----------|
| Full-width hero banner | Wastes space, flashy |
| Hardcoded hex color | Breaks dark/light theme |
| `font-family: 'Fredoka One'` | Wrong font for this project |
| `style.display = 'block'` in JS | Use class toggle instead |
| `<iframe>` for YouTube | Heavy, layout problems |
| Tabs on notes pages | Hides content, bad UX |
| Answers visible by default | Removes recall benefit |
| No KaTeX — plain text math | Ugly, error-prone |
| Missing `[data-theme="light"]` | Light mode broken |
| Numbered exercises "2.1, 2.2" for Ganita Prakash | WRONG textbook style — use "Figure It Out" |

---

## 12. GANITA PRAKASH (NCERT MATHS) SPECIFIC NOTES

- Textbook: **Ganita Prakash** (new NCERT 2024-25) — NOT old NCERT
- Exercises are called **"Figure It Out"** — NEVER "Exercise 2.1"
- Ch2 = Arithmetic Expressions (NOT Fractions & Decimals — that was old NCERT Ch2)
- Check video/resource thumbnails: confirm they say "Ganita Prakash" not old textbook

---

## 13. TEMPLATE SKELETON

Use this as starting point for every new notes page:

```html
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ch N: [Title] — Notes | Pushti Study Hub</title>
<!-- [paste full font/icon/katex links from Section 3] -->
<style>
/* [paste full CSS variable block from Section 4.1, set correct --primary] */
</style>
</head>
<body>

<header class="site-header"><!-- breadcrumb + theme toggle --></header>

<nav class="jump-bar">
  <a href="#notes"     class="jump-pill"><i class="fas fa-book-open"></i> Notes</a>
  <a href="#examples"  class="jump-pill"><i class="fas fa-lightbulb"></i> Solved Examples</a>
  <a href="#exercises" class="jump-pill"><i class="fas fa-pen-to-square"></i> Exercises</a>
  <a href="#extras"    class="jump-pill"><i class="fas fa-brain"></i> Claude Extras</a>
  <a href="#videos"    class="jump-pill"><i class="fas fa-play-circle"></i> Videos</a>
  <a href="#missing"   class="jump-pill"><i class="fas fa-star"></i> Beyond Textbook</a>
  <a href="#mistakes"  class="jump-pill"><i class="fas fa-triangle-exclamation"></i> Common Mistakes</a>
</nav>

<div class="chapter-intro">
  <div class="ch-num">0N</div>
  <div class="ch-text">
    <h1>[Chapter Title]</h1>
    <p class="subtitle">Ganita Prakash · Class 7 · Pushti Study Hub</p>
    <div class="ch-tags"><!-- topic tags --></div>
  </div>
</div>

<main class="page-content">
  <section class="section" id="notes"><!-- Notes --></section>
  <section class="section" id="examples"><!-- Solved Examples --></section>
  <section class="section" id="exercises"><!-- Figure It Out --></section>
  <section class="section" id="extras"><!-- Claude Extras --></section>
  <section class="section" id="videos"><!-- Videos --></section>
  <section class="section" id="missing"><!-- Beyond Textbook --></section>
  <section class="section" id="mistakes"><!-- Common Mistakes --></section>
</main>

<button class="back-top" id="backTop" onclick="window.scrollTo({top:0,behavior:'smooth'})">
  <i class="fas fa-arrow-up"></i>
</button>

<script src="../../../firebase-config.js"></script>
<script src="../../../js/scroll_to_top.js"></script>
<script>
/* [paste full JS from Section 9: theme toggle, revealAnswer, toggleExample] */
</script>
</body>
</html>
```

---

## 14. EXAM PATTERN & ASSESSMENT BLUEPRINT ARCHITECTURE

When integrating assessment blueprints, mark distributions, or exam patterns in `midterm.html` or assessment dashboards:

### 14.1 Main Table Standard
* **Dedicated Column**: The `Exam Pattern` column is positioned as the 5th column. Pending subjects display a muted `—`.
* **Subject Badges**: Compact buttons with subject icon, name, and total marks (e.g. `⚡ Physics [25M]`, `🧪 Chemistry [25M]`, `🧬 Biology [30M]`, `📊 Summary [80M]`).

### 14.2 Pop-up Modal Zero-Scrollbar Architecture
* **Do NOT embed tall question lists directly in table cells.** Open an interactive modal (`.exam-modal-overlay`).
* **Direct Deep-Linking**: Clicking any badge opens the modal directly to that subject's pane.
* **Tabs with Zero Horizontal Scrollbar**: `.modal-nav-tabs` must use `overflow: visible; flex-wrap: wrap; justify-content: center;` to avoid horizontal scrolling.
* **The 3 × 2 Balanced Grid Layout**:
  Arrange question types in a responsive 2-column grid (`.pattern-grid-2col`) yielding a compact 3-row × 2-column matrix:
  * Row 1: `MCQ & Assertion-Reason` (Left) | `Very Short Answer (VSA)` (Right)
  * Row 2: `Short Answer (SA)` (Left) | `Case Study` (Right)
  * Row 3: `Long Answer (LA)` (Left) | `💡 Revision Priority Tip` (Right)
  This limits vertical height to **~140px**, ensuring zero vertical scrollbars on all standard desktop and laptop screens.
* **Asset Storage**: Save official infographic images to `source_materials/{subject}/` and `artifacts/` and commit to Git.

---

## 17. COLLAPSIBLE VERTICAL DOCK RAIL ARCHITECTURE

For lengthy multi-unit chapters with 8–10+ concept units (e.g. Mathematics and Science core chapters), horizontal tab strips create unwanted wrapping or horizontal scrollbars. We adopt the **Collapsible Vertical Dock Rail**:

### 17.1 Width & Screen Space Reclamation
* **Collapsed Width**: `width: 60px–64px` default rail width. Reclaims nearly **200px of horizontal space**, allowing formulas, tables, and answer cards to stretch wider, dramatically reducing overall vertical page scroll size.
* **Expanded Width**: `width: 260px` floating frosted-glass dock (`backdrop-filter: blur(16px)`).
* **Grid Layout**: `.chapter-vertical-layout` uses `grid-template-columns: 62px minmax(0, 1fr)` by default.

### 17.2 Intentional Hover Delay (1.2s to 1.5s)
* Casual cursor pass-throughs across the screen while reading or scrolling **must never trigger drawer expansion**.
* CSS transition delay must be specified:
  ```css
  .chapter-tabs.vertical-tabs {
    transition: width 0.32s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease;
    transition-delay: 0.1s; /* rapid clean retraction on exit */
  }
  .chapter-tabs.vertical-tabs:hover {
    width: 260px !important;
    transition-delay: 1.2s !important; /* deliberate 1.2s hover threshold */
  }
  .chapter-tabs.vertical-tabs:hover .tab span {
    opacity: 1;
    transform: translateX(0);
    transition-delay: 1.25s;
  }
  ```

### 17.3 Persistent Selection Outline & Highlight
* In both collapsed (icon-only) and expanded states, the active tab must be unmistakable:
  ```css
  .chapter-tabs.vertical-tabs .tab.active {
    background: linear-gradient(135deg, rgba(var(--primary-rgb), 0.32), rgba(var(--primary-rgb), 0.12)) !important;
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 2px rgba(var(--primary-rgb), 0.65), 0 4px 16px rgba(var(--primary-rgb), 0.3) !important;
  }
  .chapter-tabs.vertical-tabs .tab.active i {
    color: #ffffff !important;
    filter: drop-shadow(0 0 8px var(--primary-glow)) !important;
    transform: scale(1.15) !important;
  }
  ```

### 17.4 Tooltip Titles & Pin Toggle
* **Instant Native Tooltips**: Every tab button MUST have a descriptive `title="..."` attribute (e.g. `title="1. Place Value & Representation"`), giving instant hints without waiting for drawer expansion.
* **Pin / Unpin Toggle**: Include `<button class="sidebar-dock-toggle" onclick="toggleSidebarPin()">` with `<i class="fas fa-thumbtack">` at the top of the dock header. Pin status is stored in `localStorage.setItem('pushti-sidebar-pinned', isPinned)`.

---

## 18. SUBMODULE TABBED PARTITIONING (AVOID ANCHOR-JUMP DUMPS)

For dense content blocks with >15–20 problems (e.g., NCERT Solved Examples [22], Figure It Out Exercises [16], Practice Banks [150+]):
* **NEVER jam all questions into one gigantic vertical scroll list.**
* **NEVER rely on floating anchor jump bars (e.g., `#q1`, `#q5`) within the same page**, which clutter the screen and disorient students.
* **Partition into Nested Submodule Vertical Tabs**:
  - Example (Solved Examples): Subtab 1 (Ex 1–5), Subtab 2 (Ex 6–10), Subtab 3 (Ex 11–16), Subtab 4 (Ex 17–22).
  - Example (Figure It Out): Subtab 1 (In-Text Activities), Subtab 2 (Exercises Part 1), Subtab 3 (Exercises Part 2).
  - Example (Practice Bank): Subtabs for MCQs L1/L2/HOTS, Match, AR, Comprehension, Subjective, Integer, Case Studies.
* **Isolation**: Submodule panes switch using `.submodule-pane.active` so only the currently studied subset is rendered.

---

## 19. SUBPARTS GRID & SOLUTION TILE ARCHITECTURE

To optimize screen space and eliminate scroll within scrollbars:
* **Multi-Part Questions**: Use `.subparts-grid`:
  ```css
  .subparts-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)) !important;
    gap: 10px 14px !important;
  }
  ```
  Distributes subparts (i), (ii), (iii) in a clean 2–4 column horizontal flow instead of a tall vertical bullet stack.
* **Answer Cards**: Multi-part solutions render inside `.solution-grid`:
  ```css
  .solution-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)) !important;
    gap: 12px !important;
  }
  ```
  Each subpart answer gets a distinct `.solution-card` tile with a dedicated sub-badge (e.g. `(i)`, `(ii)`).

---

## 20. KATEX & LATEX STRING INTEGRITY RULES

When building mathematical and scientific pages using Python compilation scripts:
* **Raw Python Strings Rule**: In Python files using raw multi-line strings `r"""..."""`, **NEVER double the backslashes** (`\\frac`, `\\text`). Python raw strings preserve single backslashes literally.
* **Double Backslash Disaster**: `\\frac` outputs literal `\\frac` to HTML. In KaTeX, `\\` evaluates to a newline, turning `\frac{1}{10}` into broken text `frac110` and `\text{cm}` into italic math `textcm`.
* **Currency Formatting**: Inside math mode `$...$`, bare Indian Rupee signs (`₹`) crash or misrender. Always use `\text{₹}` (e.g. `$\text{₹}100$`). Outside math mode, plain `₹` in HTML is fine.
* **Math Underscores**: Underscores `_` in KaTeX represent subscripts. Bare underscores (e.g. for fill-in blanks) crash KaTeX. Use `\_` or `\underline{\hspace{1.5cm}}`.

---

## 21. VERIFIED TIMESTAMPS, NOTIFICATION DOTS & SYLLABUS BATTERIES

To track syllabus readiness and keep study progress transparent:
* **Verified Date Badges**: Every tab and submodule header should indicate its last verification date:
  `<span class="verified-badge"><i class="fas fa-calendar-check"></i> Verified: 13 Sep 2026</span>`
* **Section Notification Dot**: Newly added or freshly verified sections feature an Android-style pulsing indicator dot (`.update-dot`), guiding the student immediately to updated material.
* **Topic Tag Syllabus Mapping & Highlighting (The Topic-to-Battery Rule)**:
  - **Purpose**: The tags and pills on chapter cards (`.ch-tags .tag`, `.subtopic-pills-row .topic-pill`) are **functional syllabus audit markers**, not decorative keywords. They must list the exact topics prescribed in the syllabus for that chapter/unit.
  - **Covered Topics (`.tag-covered` / Highlighted)**: When a topic has been authored, verified, and integrated into the digital module, its tag must be visually highlighted (active theme accent color, bold text, illuminated border).
  - **Pending Topics (`.tag-pending` / Dim)**: If a topic is in the syllabus but has not yet been authored inside the module, it must remain dim / un-highlighted (muted color, dashed/standard border).
  - **Completeness Calculation**: Completeness percentage is strictly calculated from the covered-to-prescribed ratio:
    $$\text{Topic Completeness \%} = \frac{\text{Syllabus Topics Covered (Highlighted)}}{\text{Total Syllabus Topics Prescribed in Syllabus}} \times 100$$
  - A chapter card or subject may **never** be labeled `Ready` or `100%` if any prescribed syllabus topic remains pending.
* **Syllabus Progress Battery**:
  - A compact, colorful micro-battery widget showing completion vs. Mid-Term syllabus.
  - Emerald Green (`#10b981`) for 100% / Completed.
  - Cyan (`#06b6d4`) for 70%–99%.
  - Amber (`#f59e0b`) for 30%–69%.
  - Rose (`#f43f5e`) for <30% / Pending.
  - Displayed on the Home Page (`index.html`), Subject Index (`maths_index.html`), and Chapter Headers as an unobtrusive status pill (e.g. `🔋 3/8 Chapters (38%)`).

---

## 22. MATHEMATICS CHAPTER THEME & GUI UNIFICATION STANDARD (v1.4)

To guarantee an ultra-polished, distraction-free visual experience across all Mathematics chapters (demonstrated in Chapters 3 & 4), adhere to the following strict theme and interface conventions:

### 22.1 Universal Button & Input Theme Reset (Zero "White Patches" Rule)
* **The Problem**: Browsers default unstyled `<button>` and `<input>` elements to the OS `buttonface` appearance (stark `#ffffff` white or light grey background with black text). Any missing CSS rule immediately causes jarring white patches on dark themes.
* **The Universal Reset**: Every chapter stylesheet must define:
  ```css
  button {
    font-family: inherit;
    color: var(--text-main);
    background: transparent;
    border: 1px solid var(--border);
  }
  ```
* **Explicit Styling on All Interactive Elements**:
  - `.tool-btn`: Styled as dark glass pills (`var(--surface)`) with glowing indigo hover effects for accordion toggles (e.g. `Show All`, `Hide All`).
  - `.back-to-theory-btn`: Subtle badge-style buttons for cross-referencing theory sections, featuring `var(--surface)` background, border outline, and hover illumination.
  - `.mcq-opt-btn`: Distinct card-style options with `.opt-label` tags; dynamically turning emerald on correct and rose on incorrect.
  - `.overview-launch-btn`: Smooth action button with subtle elevation on hover.
  - `.conf-btn`: Confidence tracker buttons styled with `.nailed` (`#10b981`), `.review` (`#f59e0b`), and `.stuck` (`#f43f5e`).

### 22.2 Unified Header & Breadcrumb Hierarchy
* Sticky 54px top header (`.site-header`) with high z-index (1000) and glassmorphic backdrop filter.
* Standardized breadcrumb structure with FontAwesome icons:
  `Home (fa-home) / Mathematics (fa-calculator) / Chapter N: Title`.
* Right cluster includes:
  - Micro-battery syllabus pill badge: `🔋 100% Mid-Term Ready` (emerald border & fill).
  - Theme toggle button (`.theme-toggle-btn`) with synchronized `localStorage.getItem('pushti_theme')` persistence.

### 22.3 Edge-Docked Collapsible Sidebar & Desktop Margin Push
* Dock rail is pinned to `left: 0; top: 54px; bottom: 0; width: 62px;`.
* Hover expansion: Expands to 280px with a **1.2-second delay** to eliminate jitter while reading.
* Pin Lock: Clicking `#pin-btn` toggles `.pinned` state and updates `localStorage`.
* **Desktop Content Margin Push**: When pinned on desktop (`@media (min-width: 861px)`), `.main-content` smoothly shifts `margin-left: 280px;` (with `transition: margin-left 0.3s cubic-bezier(0.4, 0, 0.2, 1)`) so the dock never obscures reading text.
* Active Tab Glow: 2px glowing outline (`box-shadow: 0 0 0 2px var(--primary)`) with green pulsing `.update-dot`.

### 22.4 Interactive Floating Utilities & Telemetry
* **Floating Scroll-To-Top**: Every chapter includes `#scrollTopBtn` (44px circle, `bottom: 24px; right: 24px; z-index: 999`), revealing when scroll depth exceeds 300px.
* **Firebase Study Time Logging**: Background module logging study seconds every 60s to Firestore `user_stats` for active users (`pushti` / `hirak`).
* **Custom Luminous Scrollbars**: Discrete 6px scrollbars (`::-webkit-scrollbar`) with `var(--border)` thumb and `var(--primary)` hover state.

### 22.5 Zero Content Alteration Verification Gate
* When upgrading GUI or layout templates, **zero mathematical content, equations, solutions, or descriptions may be altered or lost**.
* Before approving any chapter file, run automated integrity checks:
  1. HTML tag balance verification: `<div>` open == close (diff: 0), `<button>` open == close (diff: 0).
  2. KaTeX delimiter parity: Even count of display math `$$` blocks.
  3. Class coverage: 100% of custom classes must map to valid CSS rules with 0 unstyled elements.

---

## 23. COMPANION SOPS

* **`SOP.md`**: Master Standard Operating Procedure & Checkpoint verification rules.
* **`PUSHTI_CONTENT_SOP.md`**: Content strategy, Two-AI workflow (Gemini legwork + Claude concept mastery), and chapter completeness rules.
* **`GITA_Requirements.md`**: 5-Tab blue framework and UTF-8 encoding safety.

All files work together as the architectural standard for Pushti's Study Hub.

---

## 24. CHANGELOG

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-09-08 | Initial SOP created by Antigravity (Claude) |
| 1.1 | 2026-09-09 | Added companion PUSHTI_CONTENT_SOP.md reference |
| 1.2 | 2026-09-12 | Added Section 14: Exam Pattern Pop-up Modal & Zero-Scrollbar Architecture; added Timetable & Assessment Maintenance standards |
| 1.3 | 2026-09-13 | Added Sections 17–21: Collapsible Vertical Dock Rail Architecture (1.2s delay), Submodule Partitioning, Subparts Grid & Answer Tiles, KaTeX Single-Backslash Rules, and Verified Timestamps / Notification Dots / Syllabus Progress Batteries |
| 1.4 | 2026-09-13 | Added Section 22: Mathematics Chapter Theme & GUI Unification Standard (Zero "White Patches" universal button reset, unified header breadcrumbs, desktop margin push, floating scroll-to-top, and 0-content-loss verification gate) |

