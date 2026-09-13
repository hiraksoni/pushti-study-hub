# PUSHTI STUDY HUB — MASTER UNIFIED SOP (v2.5)
*The Definitive Architectural, Design, Pedagogical & Verification Standard for AI-Assisted Generation*

---

## PART 1: PHILOSOPHY & WORKFLOW FOUNDATIONS

### 1.1 Mission & Student Profile
* **Project Name**: Pushti Study Hub
* **Lead & Vision**: Hirak Soni (Father & Project Lead)
* **Student**: Pushti Soni, Class 7, CBSE Board (~12 years old)
* **Goal**: Provide a fun, aesthetically inspiring, rigorous, and self-sufficient learning environment.
* **Core Principle**: *"A child must NEVER need to open the textbook."* Every concept, solved example, exercise, diagram, formula, and enrichment context must exist in one cohesive, beautifully organized digital module.

### 1.2 The Two-AI Workflow
We leverage the unique cognitive strengths of two complementary AI systems:
| Role | Engine | Core Responsibilities |
| :--- | :--- | :--- |
| **Concept Master & Pedagogue** | **Claude** | Conceptual clarity, mental math shortcuts, real-world Indian analogies, "Beyond NCERT" previews, common student mistakes & traps, brain teasers, and final synthesis. |
| **Legwork & Extraction Engine** | **Gemini** | Verbatim extraction of textbook problems, comprehensive step-by-step solutions to all *Figure It Out* exercises, property tables, and raw problem set generation. |
| **Architect & Quality Gate** | **Claude / Antigravity** | Layout assembly, SOP compliance, zero-content-loss verification, CSS/JS polish, and responsive QA. |

### 1.3 The Self-Sufficiency & Content Integrity Test
Before declaring any chapter or educational artifact complete, verify:
> *"Can Pushti master this topic and achieve 100% on CBSE school and Olympiad exams relying SOLELY on this artifact without opening any external book or website?"*
If the answer is no, identify the missing concept, diagram, or exercise and resolve it immediately.

### 1.4 Directory Structure & Relative Path Depth Rules
Every page must use deterministic relative paths based on directory nesting depth:
```
d:\Users\expor\Downloads\Codes\
├── index.html                                  (Root Hub)
├── midterm.html, timetable.html                (Root Portals)
├── maths_index.html, science_index.html, ...   (Subject Hubs - Depth 0)
├── chapters/
│   ├── maths/maths_ch1.html, maths_ch5.html    (Primary Chapter Modules - Depth 2)
│   └── science/                                (Science Modules - Depth 2)
├── source_materials/
│   ├── chapters/archive/                       (Archived / Historical Reference Code)
│   └── raw_pages/                              (Extracted Textbook Page Screenshots)
├── js/scroll_to_top.js, chapter_logs.js        (Core UI Scripts)
├── scripts/maintenance/                        (Python Build & Maintenance Utilities)
└── firebase-config.js                          (Database & Telemetry Config)
```

**Relative Path Depth Verification Matrix:**
| File Location | Depth | Relative to Root | Firebase Script | Jump Script | Home Link |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Root (`*.html`) | `0` | `./` | `firebase-config.js` | `js/scroll_to_top.js` | `index.html` |
| `chapters/{subject}/` | `2` | `../../` | `../../firebase-config.js` | `../../js/scroll_to_top.js` | `../../index.html` |
| `source_materials/chapters/{sub}/` | `3` | `../../../` | `../../../firebase-config.js` | `../../../js/scroll_to_top.js` | `../../../index.html` |

### 1.5 System Safety & Encoding (Mandatory Python UTF-8)
* **CRITICAL ENCODING RULE**: Never use Windows PowerShell redirectors (`>`, `>>`, `Set-Content`) to edit or generate HTML, JSON, or Python files. PowerShell defaults to Windows-1252 or UTF-16, permanently corrupting emojis (`🎯`, `🔋`, `✨`, `📐`, `₹`) into broken characters (`??` or `dY"s`).
* **MANDATORY**: Always read, modify, and write files using Python with explicit `open(filepath, 'w', encoding='utf-8')`.

---

## PART 2: UNIVERSAL UI/UX & DESIGN SYSTEM (ALL PAGES)

### 2.1 Standard HTML Head & CDN Stack
Every HTML artifact must load the official font stack, FontAwesome icons, and KaTeX math renderer:
```html
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Chapter / Subject Title] | Pushti Study Hub</title>
  
  <!-- Fonts: Outfit (Display), Inter (Body), JetBrains Mono / Space Mono (Code & Numbers) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- FontAwesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <!-- KaTeX Math Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\[',right:'\]',display:true},{left:'$',right:'$',display:false},{left:'\(',right:'\)',display:false}],throwOnError:false});"></script>
</head>
```
* **Strictly Forbidden**: No external UI frameworks (Bootstrap, Tailwind, Material) or heavy JS libraries (jQuery, React, Vue). Write clean, fast, vanilla CSS and modern JavaScript.

### 2.2 Global CSS Custom Properties & Dynamic Theming
Every stylesheet must define the core color tokens supporting seamless Dark and Light mode switching:
```css
:root {
  --primary: #6366f1;
  --primary-glow: #818cf8;
  --primary-subtle: rgba(99, 102, 241, 0.12);
  --primary-deep: rgba(99, 102, 241, 0.08);
  
  /* Dark Mode Default */
  --bg-main: #0a0e1a;
  --bg-card: rgba(15, 23, 42, 0.85);
  --surface: #131d31;
  --surface-hover: #1c2a44;
  --text-main: #e2e8f0;
  --text-muted: #94a3b8;
  --text-title: #ffffff;
  --border: rgba(255, 255, 255, 0.08);
  --border-hover: rgba(99, 102, 241, 0.4);
  
  /* Status Accents */
  --success: #10b981;
  --warning: #f59e0b;
  --danger: #f43f5e;
  --cyan: #06b6d4;
  
  --font-body: 'Inter', sans-serif;
  --font-head: 'Outfit', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

[data-theme="light"] {
  --bg-main: #f8fafc;
  --bg-card: #ffffff;
  --surface: #f1f5f9;
  --surface-hover: #e2e8f0;
  --text-main: #1e293b;
  --text-muted: #64748b;
  --text-title: #0f172a;
  --border: rgba(0, 0, 0, 0.08);
  --border-hover: rgba(99, 102, 241, 0.5);
}
```

### 2.3 Universal Button & Input Reset (The Zero "White Patches" Mandate)
* **The Root Cause**: Browsers render unstyled `<button>` and `<input>` elements using the operating system's native `buttonface` (stark `#ffffff` white with black text), causing bright jarring white patches on dark themes whenever an explicit CSS rule is missing.
* **The Universal Reset (Non-Negotiable)**:
  ```css
  button, input, select, textarea {
    font-family: inherit;
    color: var(--text-main);
    background: transparent;
    border: 1px solid var(--border);
  }
  ```
* Every interactive button (`.tool-btn`, `.btn-solution-toggle`, `.mode-btn`, `.mcq-opt-btn`, `.sub-pill-btn`) must be explicitly styled with dark glass surfaces (`var(--surface)`), rounded borders (8–10px), and smooth hover states.

### 2.4 The Zero-Horizontal-Scroll Mandate
Horizontal scrollbars on desktop/laptop displays degrade readability and break responsive rhythm:
1. **Never use `overflow-x: auto` with `white-space: nowrap`** on pill bars or tab bars.
2. Always apply responsive multi-row flex wrapping:
   ```css
   .subtopic-pills-row, .modal-tabs, .activity-tab-bar {
     display: flex;
     flex-wrap: wrap;
     gap: 8px 6px;
     overflow-x: hidden;
   }
   ```
3. Sidebars on mobile breakpoints (`@media (max-width: 860px)`) must flex-wrap cleanly (`flex-direction: row; flex-wrap: wrap;`).

### 2.5 The Zero-Collision & Text Overwrite Prevention Standard (Universal Math & Layout Containment)
* **The Problem (Root Causes)**:
  1. **Indivisible KaTeX Spans (`white-space: nowrap`)**: When lists of numbers, units, or values are grouped in a single `$ ... $` block with `\quad` (e.g. `$11.01,\quad 1.011,\quad 1.101$`), KaTeX renders an indivisible math span. The browser is forbidden from wrapping lines between values, causing the formula to expand to ~350px+ and smash into or overwrite neighboring cards.
  2. **Missing Flex/Grid Child Shrink (`min-width: auto`)**: By CSS default, flex and grid items have `min-width: auto`. Wide contents prevent items from shrinking to their assigned column tracks, causing them to push outside card borders or overlap adjacent columns.
  3. **Multi-Step Formulas on Single Lines (`A = B = C = D`)**: Display equations with multiple steps placed on a single line inside cards become wider than the card width (~240px–280px), bleeding through boundaries.
* **Mandatory Coding Prevention Rules (Non-Negotiable)**:
  1. **Isolate Every List Item into Its Own Math Tag**:
     - ❌ **STRICTLY FORBIDDEN**: `$11.01,\quad 1.011,\quad 1.101,\quad 11.10,\quad 1.01$`
     - ✅ **MANDATORY**: `$11.01$, $1.011$, $1.101$, $11.10$, $1.01$`
     Standard HTML commas and spaces outside the math delimiter allow natural, responsive line wrapping across any container width.
  2. **Multi-Step Calculations Must Use `\begin{aligned}` or Explicit Line Breaks**:
     - ❌ **STRICTLY FORBIDDEN**: `$$8(100) + l(20) + 4(5) = 800 + 20l + 20 = \mathbf{\text{₹}(820 + 20l)}$$`
     - ✅ **MANDATORY**:
       ```latex
       $$\begin{aligned}
         &8(100) + l(20) + 4(5) \\
         &= 800 + 20l + 20 \\
         &= \mathbf{\text{₹}(820 + 20l)}
       \end{aligned}$$
       ```
  3. **Universal Card Box-Sizing & Min-Width Reset**:
     Every card container (`.subpart-card`, `.subpart-item`, `.solution-card`, `.sop-card`, `.mcq-card`, `.question-card`) must declare:
     ```css
     min-width: 0 !important;
     overflow: hidden !important;
     box-sizing: border-box !important;
     ```
  4. **Text & Math Body Overflow Containment**:
     Every text/math container (`.subpart-body`, `.subpart-text`, `.solution-card-body`, `.solution-content`, `.problem-statement`, `.q-statement`) must declare:
     ```css
     min-width: 0 !important;
     max-width: 100% !important;
     overflow-x: auto !important;
     overflow-y: hidden !important;
     word-break: break-word !important;
     -webkit-overflow-scrolling: touch;
     ```
  5. **Grid Track Minimum Widths**:
     `.subparts-grid` and `.solution-grid` must use `minmax(280px, 1fr)` rather than `240px` to ensure subpart cards have adequate reading width before wrapping into fewer columns.
  6. **Flex Sizing on Labeled Subparts**:
     `.subpart-item` must be `display: flex !important; align-items: flex-start !important; gap: 10px !important;` with `.subpart-label { flex-shrink: 0 !important; }` and `.subpart-text { flex: 1 1 0% !important; min-width: 0 !important; }`.

### 2.5.1 Laptop Viewport Compatibility & Solved Examples Math Formatting Standard
* **The Student Context**: Pushti actively studies and practices mathematics solutions directly on her laptop (standard 1366×768 or 1280×800 display).
* **The Laptop Display Reality**:
  - When the 280px vertical dock rail is pinned or hovering, the usable main content viewport drops to ~1000px.
  - In chapters featuring submodule sidebars (220px–260px) or multi-column subpart/solution grids, the actual width available for a solution drawer or subpart card is often only **240px to 320px**!
  - A single-line KaTeX equation containing 2+ equality steps or fractions (e.g. `$2\frac{6}{10} + 3\frac{5}{10} = (2+3) + \frac{6+5}{10} = 5 + \frac{11}{10} = \dots$`) has a native rendered width of **600px to 850px**.
  - On desktop widescreen this may fit, but on a laptop display it violently **crosses over the card borders, overlaps adjacent text, or produces disruptive horizontal scrollbars**.
* **Mandatory Laptop Prevention Standard (Zero-Overflow Gate)**:
  1. **Strict Multi-Step Decomposition (`\begin{aligned}`)**:
     - Any equation in Solved Examples or Exercise Solutions with **more than 1 equals sign (`=`)** or **length exceeding 40 characters** MUST be written as a vertically stacked `\begin{aligned}` block with line breaks at `&=`.
     - *Maximum single-line width limit*: No line within an aligned environment may exceed 30–35 characters.
  2. **Dedicated Laptop Media Query (`@media (max-width: 1366px)`)**:
     Every chapter stylesheet must enforce laptop-specific grid and padding adjustments:
     ```css
     @media (max-width: 1366px) {
       .main-content {
         padding: 20px 24px 50px 24px !important;
       }
       .submodule-layout {
         grid-template-columns: 220px 1fr !important;
         gap: 14px !important;
       }
       .subparts-grid, .solution-grid, .grid-2, .grid-3 {
         grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)) !important;
         gap: 10px !important;
       }
       .katex-display {
         font-size: 0.95em !important;
         margin: 0.5em 0 !important;
       }
     }
     @media (max-width: 1050px) {
       .submodule-layout {
         grid-template-columns: 1fr !important;
       }
       .submodule-sidebar {
         position: static !important;
         flex-direction: row !important;
         overflow-x: auto !important;
       }
     }
     ```
  3. **Defensive Solution Drawer & Step Containment**:
     All `.solution-drawer`, `.solution-details`, `.solution-content`, and `.sol-step` elements must declare:
     ```css
     min-width: 0 !important;
     max-width: 100% !important;
     overflow-x: auto !important;
     word-break: break-word !important;
     box-sizing: border-box !important;
     ```
  4. **Strict Pre-Confirmation Laptop Audit**:
     Before certifying any solved example or chapter module as complete, test and verify the layout within a 1280px–1366px viewport width with the sidebar pinned. Ensure zero text collision, zero border breach, and flawless visual elegance.

### 2.6 Unified Sticky Header (`.site-header`)
Every chapter and subject page must present the standardized 54px glassmorphic sticky top bar:
```html
<header class="site-header">
  <div class="header-left">
    <a href="../../index.html" class="nav-home"><i class="fas fa-home"></i> Home</a>
    <span class="breadcrumb-separator">/</span>
    <a href="../../maths_index.html"><i class="fas fa-calculator"></i> Mathematics</a>
    <span class="breadcrumb-separator">/</span>
    <span class="breadcrumb-current">Chapter 1: Large Numbers Around Us</span>
  </div>
  
  <div class="header-right">
    <!-- Micro-Battery Readiness Indicator -->
    <div class="battery-pill" title="Mid-Term Syllabus Coverage">
      <span class="battery-meter"><span class="battery-body"><span class="battery-fill" style="width:100%;"></span></span><span class="battery-cap"></span></span>
      <span>🔋 100% Mid-Term Ready</span>
    </div>
    
    <!-- Theme Toggle -->
    <button class="icon-btn theme-toggle-btn" onclick="toggleTheme()" aria-label="Toggle Dark/Light Mode" title="Toggle theme">
      <i class="fas fa-moon"></i>
    </button>
  </div>
</header>
```

### 2.7 Floating Interactive Utilities & Telemetry
1. **Floating Jump-to-Top Button (`#scrollTopBtn`)**:
   - Circular 44px button fixed at `bottom: 24px; right: 24px; z-index: 999;`.
   - Reveals smoothly with `opacity: 1; pointer-events: auto;` when page scrolls beyond 300px.
   - Smoothly scrolls to the top on click (`window.scrollTo({ top: 0, behavior: 'smooth' })`).
2. **Firebase Study Telemetry**:
   - Background heartbeat logging active study seconds every 60 seconds into Firestore `user_stats` for Pushti and Hirak.
3. **Custom Luminous Scrollbars**:
   - Discrete 6px scrollbars (`::-webkit-scrollbar { width: 6px; height: 6px; }`) matching theme tokens (`var(--surface)` track, `var(--border)` thumb, `var(--primary)` hover).

---

## PART 3: SUBJECT-WISE CHAPTER ARCHITECTURES

### 3.1 Mathematics Architecture (High-Density Geometry & Algebra Model)
*Exemplified in Chapters 1, 3, 4, and 5.*

1. **Collapsible Vertical Dock Rail & The Zero-Peeking Text Mandate**:
   - Default width collapsed to `62px` pinned to the left edge (`left: 0; top: 54px; bottom: 0;`).
   - Reclaims ~200px of screen real estate for wide formulas, coordinate tables, and answer cards.
   - Snappy **0.72-second hover delay** (`transition-delay: 0.72s;`, reduced to 60% of original 1.2s) providing an effortless, non-awkward expansion while still protecting against accidental cursor pass-throughs.
   - **The Zero-Peeking Text Mandate (Non-Negotiable)**:
     - In the collapsed 62px state, **zero letters, words, or label fragments may ever peek out** into the main viewport.
     - All button text labels and metadata must be enclosed within a dedicated `.tab-label-group` container:
       ```css
       .tab-btn {
         display: flex;
         align-items: center;
         width: 100%;
         height: 44px;
         padding: 0 12px;
         overflow: hidden;
       }
       .tab-icon-wrap {
         width: 38px;
         min-width: 38px;
         display: flex;
         align-items: center;
         justify-content: center;
       }
       .tab-label-group {
         display: flex;
         flex-direction: column;
         margin-left: 12px;
         width: 0;
         opacity: 0;
         overflow: hidden;
         pointer-events: none;
         white-space: nowrap;
         transition: opacity 0.2s ease, width 0.28s ease;
       }
       .sidebar:hover .tab-label-group,
       .sidebar.pinned .tab-label-group {
         width: auto;
         opacity: 1;
         pointer-events: auto;
         transition-delay: 0.12s;
       }
       ```
     - This guarantees that in collapsed mode, only perfectly centered, glowing icons with status dots appear.
   - Active tab highlighted by a glowing 2px outline (`box-shadow: 0 0 0 2px var(--primary)`), illuminated icon, and green pulsing `.update-dot`.
   - **3-Second Active Viewing Rule**: Section notification dots automatically fade out and dismiss when viewed for $\ge 3$ seconds (persisted in `localStorage`). Switching away under 3 seconds leaves the dot active.
   - Pin button (`#pin-btn`, `<i class="fas fa-thumbtack">`) locks sidebar expanded to `280px` and saves state in `localStorage`.
2. **Desktop Content Margin Push**:
   - When pinned on desktop screens (`@media (min-width: 861px)`):
     `.sidebar.pinned ~ .main-content { margin-left: 280px; }` with `transition: margin-left 0.3s cubic-bezier(0.4, 0, 0.2, 1)`.
   - Ensures zero sidebar overlap over reading material.
3. **Submodule Tabbed Partitioning**:
   - Dense sections (>15 questions, Solved Examples, Figure It Out, Practice Banks) must be partitioned into nested sub-panes rather than one continuous vertical scroll dump.
4. **Subparts Grid & Solution Tile Cards**:
   - Multi-part questions (i, ii, iii) format in responsive auto-fit grids (`.subparts-grid`, minmax 210px).
   - Solutions display in structured card tiles (`.solution-grid`, minmax 240px) with dedicated sub-badges.
5. **KaTeX Raw String Single-Backslash Rule**:
   - In Python generator scripts (`r"""..."""`), **never use double backslashes** (`\\frac`, `\\text`). Raw strings output single backslashes literally. In KaTeX, `\\` evaluates to a newline, breaking formulas.
   - Currency in math mode must always be written as `\text{₹}` (e.g. `$\text{₹}500$`).
6. **100% Textbook Extraction Fidelity**:
   - Every single NCERT Solved Example and *Figure It Out* exercise must be solved with full step-by-step mathematical reasoning. Never skip or truncate exercises.

### 3.1.1 Geometry Chapters Visual Standard (The Native Vector SVG Mandate)
*Exemplified in Class 7 Chapter 5 (Parallel and Intersecting Lines) and mandatory across all present and future Geometry modules.*

1. **Pencil Scribble & Scan Noise Elimination**:
   - **The Reality**: Uploaded textbook scans or photocopies (e.g. NCERT PDFs) frequently suffer from heavy student pencil markings, handwritten answers, teacher correction ticks, scanner skew, moiré patterns, and muddy raster compression.
   - **Strict Prohibition**: Never crop, embed, or rely on raw scanned raster images containing pencil scribbles or artifact noise. Attempting to filter scanned bitmaps results in jagged edges, artifact halos, and unreadable text that clashes jarringly against dark themes.
   - **The Native Vector Mandate**: Every geometric figure must be constructed from scratch as a **clean, mathematically exact native SVG vector graphic**.

2. **100% Geometric Figure Coverage (Zero Missing Figures Policy)**:
   - A geometry chapter can NEVER present purely textual problem statements when a diagram is conceptually needed or referenced in the textbook.
   - Every single element across the entire chapter must have its own dedicated, crystal-clear diagram:
     - All foundational concept definitions (Parallel, Perpendicular, Linear Pairs, Transversals, Alternate/Corresponding/Co-Interior Angles).
     - All worked textbook illustrations (e.g. Illustrations 1 to 5).
     - All NCERT solved examples (100% coverage, e.g. Examples 1 to 10).
     - All *Figure It Out* drills and exercises (e.g. Drills 1 to 7).
     - All practice questions, MCQs, and HOTS/Case studies that state *"In the given figure..."*.

3. **Standard Component Anatomy & CSS Classes**:
   Every geometric visual must be structured using the standardized three-tier component wrapper:
   ```html
   <div class="geo-figure-card">
     <svg class="geo-svg" viewBox="0 0 340 180" width="340" height="180" xmlns="http://www.w3.org/2000/svg">
       <defs>...</defs>
       <!-- Geometry elements (lines, arcs, markers, text) -->
     </svg>
     <div class="geo-caption"><strong>Figure X.Y:</strong> Descriptive Geometric Caption</div>
   </div>
   ```
   **Required Stylesheet Rules (Non-Negotiable)**:
   ```css
   .geo-figure-card {
     background: var(--surface) !important;
     border: 1px solid var(--border) !important;
     border-radius: 12px !important;
     padding: 16px !important;
     margin: 14px 0 !important;
     display: flex !important;
     flex-direction: column !important;
     align-items: center !important;
     justify-content: center !important;
     text-align: center !important;
     overflow: hidden !important;
     box-sizing: border-box !important;
     min-width: 0 !important;
   }
   .geo-svg {
     max-width: 100% !important;
     height: auto !important;
     display: block !important;
     margin: 0 auto !important;
     transition: transform 0.2s ease;
   }
   .geo-caption {
     font-size: 0.82rem !important;
     color: var(--text-muted) !important;
     margin-top: 10px !important;
     font-family: var(--font-mono) !important;
     font-weight: 500 !important;
   }
   ```

4. **Theme-Adaptive Geometric Color Palette & Annotation Tokens**:
   Geometric elements must use standardized, high-contrast, theme-resilient colors:
   | Element | Color Code | Role & Pedagogical Purpose |
   | :--- | :--- | :--- |
   | **Primary Lines & Rays** | `#818cf8` (Indigo) | Base geometric framework, ray lines, and main figure boundaries. |
   | **Transversals & Stepped Lines** | `#f59e0b` (Amber) | Intersecting transversal lines, given reference angles. |
   | **Auxiliary & Construction Lines** | `#10b981` (Emerald) | Dashed parallel/normal auxiliary lines through vertices (`stroke-dasharray="4,4"`). |
   | **Corresponding & Normal Elements** | `#06b6d4` (Cyan) | F-Rule corresponding angles, perpendicular normals. |
   | **Unknown Angles & Highlights** | `#ec4899` (Rose) | Target unknown variables ($x, y, z, a, b$) and callout badges. |
   | **Vertex Points & Labels** | `#6366f1` / `#94a3b8` | Solid vertex dots (`r="3.5"`) with high-contrast label typography. |
   | **Angle Sectors & Arcs** | `rgba(..., 0.15–0.20)` | Translucent arc fills bounded by 1.8px–2px stroked boundary paths. |

5. **Geometric Symbols & Notation Standard**:
   - **Arrowheads on Lines & Rays**: Defined once inside `<defs>` with `orient="auto-start-reverse"` markers (`#arr-p`, `#arr-amb`, `#arr-em`, `#arr-cyan`).
   - **Parallel Line Identifiers**: Prominent single (`>`) or double (`>>`) directional arrowheads positioned along the line segments.
   - **Perpendicular Indicators**: A crisp $90^\circ$ right-angle square symbol (`∟`) centered at intersection vertices.
   - **Auxiliary Constructions**: Always drawn with dashed strokes (`stroke-dasharray="4,4"` or `"5,4"`) and explicit vertex markers (e.g. $N'$, $O'$, $E-M-F$).

6. **Laptop Viewport & Zero-Overflow Containment (SOP v2.3 Strict Adherence)**:
   - On standard laptop screens (1280px–1366px), SVG figures inside cards, drawers, or multi-column grids must **NEVER** induce horizontal scrolling or bleed outside container boundaries.
   - SVGs must always use a proportional `viewBox` (typical dimensions: `0 0 320 160`, `0 0 340 180`, or `0 0 360 200`) and declare `max-width: 100%`.



### 3.1.2 Two-Tier Navigation Architecture (Submodule Tab Partitioning & Vertical Scroll Elimination)
*Exemplified in Chapter 6 (Number Play) and mandatory across all comprehensive modules.*

1. **The Cognitive Challenge of "Page Dumps"**:
   - Dumping 15 solved examples, 5 multi-part drills, or 20 MCQs into a single continuous vertical tab creates an overwhelming wall of text, causes disorientation, and requires excessive scrolling.
   - **The Two-Tier Mandate**: Every major subject module must use a structured **Two-Tier Navigation Architecture**:
     - **Tier 1 (Left Collapsible Dock Rail)**: Organizes the high-level curriculum into major units (e.g. *Overview*, *Ordering*, *Parity*, *Magic Squares*, *Virāhaṅka Numbers*, *Cryptarithms*, *Solved Examples*, *Figure It Out Drills*, *MCQ Bank*, *Advanced Evaluation*).
     - **Tier 2 (Horizontal Submodule Navigation `.submodule-nav`)**: Positioned at the top of each Tier 1 tab panel, presenting interactive pill buttons (`.submodule-btn`) that switch between focused, screen-sized sub-panes (`.submodule-pane`).

2. **Standard Submodule Partitioning Rules**:
   - **Solved Examples**: Never place >5 solved examples in a single view. Partition into logical batches (e.g., *Sub-tab 1: Examples 1–5*, *Sub-tab 2: Examples 6–10*, *Sub-tab 3: Examples 11–15*).
   - **Exercises / Drills ("Figure It Out")**: Partition page-wise or drill-wise (e.g., *Drill 1 (p.128)*, *Drill 2 (p.131)*, *Drills 3–4 (pp.136–137)*, *Drill 5 (pp.143–144)*).
   - **Practice Question Bank (MCQs)**: Partition by difficulty level (*Sub-tab 1: Level 1 Foundation*, *Sub-tab 2: Level 2 Application*, *Sub-tab 3: Level 3 HOTS / Exemplar*).
   - **Advanced Evaluation & Interactive Labs**: Partition by assessment type (*Sub-tab 1: Match the Columns*, *Sub-tab 2: Assertion & Reasoning*, *Sub-tab 3: Case Study Drill*, *Sub-tab 4: Flashcards & Revision*).

3. **Required Submodule Stylesheet Architecture (Zero-Horizontal-Scroll Enforced)**:
   ```css
   .submodule-nav {
     display: flex;
     flex-wrap: wrap;
     gap: 8px;
     margin-bottom: 20px;
     padding-bottom: 12px;
     border-bottom: 1px solid var(--border);
     overflow-x: hidden; /* Zero horizontal scrollbars */
   }
   .submodule-btn {
     display: inline-flex;
     align-items: center;
     gap: 8px;
     padding: 8px 16px;
     border-radius: 20px;
     font-size: 0.88rem;
     font-weight: 600;
     color: var(--text-muted);
     background: var(--surface);
     border: 1px solid var(--border);
     cursor: pointer;
     transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
   }
   .submodule-btn:hover {
     color: var(--text-title);
     border-color: var(--primary-glow);
     background: var(--surface-hover);
     transform: translateY(-1px);
   }
   .submodule-btn.active {
     color: #ffffff;
     background: var(--primary);
     border-color: var(--primary);
     box-shadow: 0 4px 12px rgba(99, 102, 241, 0.35);
   }
   .submodule-pane {
     display: none;
     animation: fadeIn 0.25s cubic-bezier(0.4, 0, 0.2, 1);
   }
   .submodule-pane.active {
     display: block;
   }
   ```

4. **Dynamic KaTeX Rendering Hook**:
   - Switching between Tier 1 tabs or Tier 2 sub-panes reveals previously hidden elements (`display: none` -> `display: block`).
   - The switching function MUST immediately re-trigger KaTeX rendering on the revealed container:
     ```javascript
     function renderMathOnElement(elem) {
       if (window.renderMathInElement) {
         renderMathInElement(elem || document.body, {
           delimiters: [
             { left: '$$', right: '$$', display: true },
             { left: '\\[', right: '\\]', display: true },
             { left: '$', right: '$', display: false },
             { left: '\\(', right: '\\)', display: false }
           ],
           throwOnError: false
         });
       }
     }
     ```

### 3.2 Science & Social Science Architecture (The 5-Tab GITA Framework)
All Science (Physics, Chemistry, Biology) and Social Science chapters follow the unified 5-Tab architecture:
1. **Tab 1: Videos & Concept Map**:
   - Chapter-specific YouTube video cards with search deep-links.
   - Pure CSS visual Concept Hierarchy Map (no Mermaid charts).
2. **Tab 2: OMR Practice (1 Mark)**:
   - Objective questions (MCQs, Fill-in-the-Blanks, True/False) with auto-grading arrays (`mcqBook`, `fillBook`, `tfBook`).
   - Toggle switch between **Practice Mode** (immediate per-question feedback) and **Timed OMR Test Mode** (countdown timer, question navigator palette, deferred grading scorecard).
   - Every question includes an explanation key (`exp`) detailing *why* the answer is correct.
3. **Tab 3: 2/3 Marks (Short Answer)**:
   - Mental Flashcard style using `<details>` and `<summary>` (no typing inputs). Student thinks through the answer, then reveals textbook-grade solution.
4. **Tab 4: 4+ Marks (Long Answer & Case Studies)**:
   - Comprehensive model answers. Case-based questions provide the complete reference passage above the question.
5. **Tab 5: Extra Knowledge & Curiosities**:
   - "Did you know?" trivia, historical discoveries, scientific breakthroughs beyond the textbook.

### 3.3 Vocational & Non-Exam Architecture (The Kaushal Bodh / KB Model)
* Designed for vocational, craft, and co-curricular subjects (e.g. Kaushal Bodh • Class 7).
* **Two-Tier Navigation**:
  - Tier 1: Left category sidebar organizing units into thematic branches (*Life Forms*, *Machines & Tools*, *Materials & Arts*).
  - Tier 2: Project cards with inline activity subtabs switching between compact activity panes.
* Clear non-exam badges (`Non-Exam Vocational Subject`) to remove test anxiety while emphasizing hands-on mastery.

### 3.4 Languages Architecture (Sanskrit & English)
* **Bilingual Vocabulary Cards**: Word-by-word Sanskrit-to-Hindi/English and English vocabulary cards.
* **Grammar & Sentence Construction Tabs**: Interactive verb conjugation grids (धातुरूपाणि), noun declensions (शब्दरूपाणि), and sentence formation drills.
* **Translation Walkthroughs**: Shlokas and prose broken into individual padachheda with anvaya and poetic meaning.

---

## PART 4: PLATFORM HUBS, TIMETABLES & EXAM PATTERNS

### 4.1 Subject Hub Standards (`*_index.html`)
* Standard header with live search, theme toggle, and time table / midterm pills.
* Chapter cards featuring chapter number, title, description, topic tags, Gemini/Notes action pills, and status badges.
* Active chapters feature green pulsing `.update-dot`, `🔋 100% Ready` badge, and `Verified: [Date]` timestamp.

### 4.2 Timetable & Midterm Maintenance (`midterm.html`, `timetable.html`)
* **Master Target Countdown**: Live countdown timer calculating days until examination. Updates automatically to `"Ongoing!"` during exam week and `"Completed"` afterward.
* **Synchronized Dates**: Updating exam dates in `midterm.html` requires updating the corresponding cards in `timetable.html`.
* **Accordion Syllabus Breakdown**: Subjects organized in collapsible accordions (`.s-category` and `.syllabus-list`).

### 4.3 Exam Pattern Pop-Up Modal Architecture (Zero-Scrollbar Mandate)
* **Dedicated Column**: Exam Pattern is column 5 in `midterm.html`.
* **Clickable Pattern Badges**: Click badge to open modal directly to that subject.
* **The 3 × 2 Balanced Grid Layout**:
  - Inside `.exam-modal-card`, question distributions are organized into a compact 2-column grid:
    - **Row 1**: `MCQ & Assertion-Reason` (Left) | `Very Short Answer (VSA)` (Right)
    - **Row 2**: `Short Answer (SA)` (Left) | `Case Study` (Right)
    - **Row 3**: `Long Answer (LA)` (Left) | `💡 Revision Priority Tip` (Right)
  - Limits question breakdown height to ~140px, ensuring zero vertical scrollbars on standard laptop displays.

### 4.4 Verified Badges, Notification Dots & Syllabus Batteries
* **Verified Badges**: `<span class="verified-badge">Verified: 13 Sep 2026</span>` on audited sections.
* **Android-Style Notification Dot (.update-dot) & The 3-Second Active Viewing Rule**:
  - Pulsing green dot guiding the student immediately to updated or unread material.
  - **Auto-Dismissal**: When a student actively views a section for 3 seconds or more, the dot smoothly scales down, fades out (`opacity: 0; transform: scale(0)`), and is recorded in `localStorage`.
  - **Accidental Switch Protection**: Switching away under 3 seconds does not dismiss the dot, ensuring genuine review.
  - Chapter cards on `maths_index.html` also clear their notification dots once all sections of a chapter are reviewed.
* **Micro-Battery Progress Indicators**:
  - Emerald Green (`#10b981`) = 100% Ready
  - Cyan (`#06b6d4`) = 60%–99% Progress
  - Amber (`#f59e0b`) = 30%–59% Progress
  - Rose (`#f43f5e`) = <30% / Pending

### 4.5 Syllabus Topic Tag Mapping & Completeness Calculation Standard (The Topic-to-Battery Rule)
* **Functional Purpose of Chapter Tags/Pills**:
  - The tags and pill tabs on subject chapter cards (`.ch-tags .tag`, `.subtopic-pills-row .topic-pill`) are **functional syllabus audit markers**, NOT decorative or arbitrary keywords.
  - Every tag must represent a specific, verifiable topic or component prescribed by the official school/CBSE syllabus (e.g. *पत्रलेखनम्*, *चित्रवर्णनम्*, *मञ्जूषा*, *संवादपूर्तिः*, *कथापूर्तिः*).
* **Visual Status Differentiation (Covered vs. Pending)**:
  - **Covered Topics (`.tag-covered` / Highlighted)**:
    When a prescribed topic has been authored, verified, and integrated into the digital module with full theory, examples, or interactive practice, its tag must be **visually highlighted** (active theme accent color, bold text, and illuminated border). This signals: *"This syllabus topic is fully covered and ready to study inside!"*
  - **Pending / Uncovered Topics (`.tag-pending` / Dim)**:
    If a topic is prescribed by the syllabus but is still pending, incomplete, or not yet built into the digital module, its tag must remain **dim and un-highlighted** (muted text, standard/dashed border, or reduced opacity). This signals: *"This topic is on the syllabus but not yet authored in this module."*
* **Mathematical Derivation of Completeness & Battery Percentage**:
  - The readiness percentage displayed on chapter status badges, subject cards, and the `midterm.html` battery meters is **strictly derived from this ratio**:
    $$\text{Topic Completeness \%} = \frac{\text{Number of Syllabus Topics Covered (Highlighted)}}{\text{Total Syllabus Topics Prescribed in Syllabus}} \times 100$$
  - **Strict Readiness Integrity**: A chapter card or subject module may **NEVER** be marked `Ready` or `🔋 100%` if any syllabus-prescribed topic tag remains pending/uncovered.
  - When partial coverage exists, the badge must explicitly display the verified fraction (e.g. `4/5 Topics Ready (80%)`).
  - This mathematically transparent mechanism powers the **Subject Readiness Battery** in `midterm.html` and the **Master Dashboard KPI Strip** in `index.html`.

---

## PART 5: QUALITY ASSURANCE & VERIFICATION GATES

Before marking any task, chapter, or feature as complete, the agent must pass the following **Master Verification Gates**:

### Checkpoint Suite 1: Theme & GUI Integrity
- [ ] **CP-GUI-1 (Zero White Patches)**: Has the universal button reset (`button { font-family: inherit; color: var(--text-main); background: transparent; border: 1px solid var(--border); }`) been applied? Verify that 0 unstyled native `buttonface` elements appear in dark mode.
- [ ] **CP-GUI-2 (Zero Horizontal Scroll)**: Do all pill rows, modal tabs, and activity headers wrap cleanly using flex-wrap with 0 horizontal scrollbars?
- [ ] **CP-GUI-3 (Dock Rail & Margin Push)**: Does the collapsible vertical dock rail operate with a 0.72s hover delay? When pinned, does `.main-content` shift right by 280px without overlapping text?
- [ ] **CP-GUI-4 (Question Palette Wrap)**: Is `.palette-grid` styled as an auto-filling grid (`repeat(auto-fill, minmax(36px, 1fr))`) so numbers wrap cleanly instead of stacking vertically?
- [ ] **CP-GUI-5 (MCQ Option Cards)**: Are MCQ options styled as structured card tiles (`.option-item` / `.options-grid`) with distinct letter badges (`A`, `B`, `C`, `D`), rather than cramped plain-text rows?
- [ ] **CP-GUI-6 (Dark/Light Contrast)**: Do all text, badges, borders, and callouts maintain strong readability in both dark and light modes?
- [ ] **CP-GUI-7 (Zero-Collision & Text Overwrite Prevention)**: Verify across all viewport sizes (1440px, 1200px, 992px, 768px, 375px) and with the sidebar pinned that NO card, subpart, or equation bleeds out of its container or overwrites neighboring text/borders.
- [ ] **CP-GUI-9 (Zero Dock Rail Text Peeking)**: In collapsed mode (62px), verify that exactly ZERO letters, words, or label fragments peek out into the main content. Only centered icons with status dots are visible.
- [ ] **CP-GUI-10 (Two-Tier Submodule Tab Partitioning & Vertical Scroll Reduction)**: Verify that dense sections (Solved Examples, Drills, MCQs) use horizontal `.submodule-nav` pills to eliminate excessive vertical scrollbar length, with zero horizontal scrollbars on desktop and laptop viewports.
- [ ] **CP-GUI-8 (Laptop Viewport Verification at 1280px–1366px with Sidebar Pinned)**:
  Simulate Pushti's laptop display (1366×768 or 1280×800) with the 280px sidebar pinned:
  - Verify that ALL Solved Examples and Illustrations fit completely within their solution drawer without crossing borders or forcing page-level horizontal scrolling.
  - Verify that all multi-step math derivations are stacked cleanly using `\begin{aligned}`.
  - Verify that `.subparts-grid` and `.solution-grid` cards wrap smoothly without squeezing math content below 240px.

### Checkpoint Suite 2: Content & Pedagogical Completeness
- [ ] **CP-CON-1 (100% Textbook Fidelity)**: Are ALL solved examples and ALL *Figure It Out* exercise problems extracted and solved with full mathematical steps?
- [ ] **CP-CON-2 (Step Count Rule)**: Does every solved example have at least 3 clearly numbered steps? Does every exercise solution have at least 2 steps?
- [ ] **CP-CON-3 (Real-Life Indian Context)**: Are rules explained using relatable analogies (cricket, market transactions, cooking, railway tracks, festivals)?
- [ ] **CP-CON-4 (Common Traps & Mistakes)**: Are at least 5 common misconceptions or traps explicitly highlighted with wrong vs. right comparisons?
- [ ] **CP-CON-5 (Beyond Textbook)**: Does the module include enrichment curiosities (historical origins, number tricks, high-school previews) to inspire wonder?
- [ ] **CP-CON-6 (Syllabus Topic Tag Audit & Battery Derivation)**: Do all chapter card tags map 1:1 to official syllabus topics? Are all covered topics clearly highlighted, with pending topics remaining dim? Does the battery / completeness percentage strictly reflect this covered-to-prescribed ratio?
- [ ] **CP-GEO-1 (100% Geometric Figure Coverage)**: In all geometry chapters, does every single concept, worked illustration, solved example, drill, and diagram-dependent question have a dedicated, mathematically accurate diagram?
- [ ] **CP-GEO-2 (Zero Pencil Scribble & Scan Noise Mandate)**: Are 100% of figures native SVG vector graphics with zero scanned raster images, zero pencil markings, and zero blur?
- [ ] **CP-GEO-3 (Theme-Adaptive Vector Contrast)**: Do all lines, angle arcs, markers, and text labels maintain crisp legibility in both Dark Mode and Light Mode?
- [ ] **CP-GEO-4 (Responsive Laptop Containment for Geometry)**: Do all SVGs scale fluidly without causing card border breaches or horizontal scrolling on a 1280px–1366px laptop viewport?


### Checkpoint Suite 3: Intent & Student Experience
- [ ] **CP-INT-1 (Self-Sufficiency)**: Can Pushti study this page and achieve 100% without opening the textbook or searching online?
- [ ] **CP-INT-2 (No Cluttered Anchor Jumps)**: Are dense sections partitioned into clean sub-panes rather than chaotic in-page jump links?
- [ ] **CP-INT-3 (Mental Flashcards for Subjective)**: Are subjective questions formatted as revealable flashcards without requiring tedious typing?

### Checkpoint Suite 4: Technical & Code Verification Gate
- [ ] **CP-TECH-1 (HTML Tag Balance)**: Run automated verification ensuring:
  - `<div>` open count == `</div>` close count (diff: 0)
  - `<button>` open count == `</button>` close count (diff: 0)
  - All semantic tags (`<header>`, `<aside>`, `<main>`, `<script>`, `<style>`, `<table>`) balanced.
- [ ] **CP-TECH-2 (KaTeX Delimiter Parity)**: Even count of display math `$$` delimiters. No unescaped double-backslashes (`\\frac`) in raw strings. All Indian currency formatted as `\text{₹}`.
- [ ] **CP-TECH-3 (Class Coverage)**: 100% of custom HTML classes in the body must map to valid CSS declarations in the `<style>` block (0 unstyled classes).
- [ ] **CP-TECH-4 (UTF-8 File Integrity)**: Files read and written using explicit UTF-8 encoding. Zero emoji corruption (`??`).
- [ ] **CP-TECH-5 (Hub & Timetable Sync)**: Subject index cards, timetable links, and `midterm.html` entries properly updated with accurate links and battery percentages.
- [ ] **CP-TECH-7 (Complete KaTeX Delimiter Suite & Dynamic Sub-Tab Re-render)**:
  - Verify that `<head>` auto-render registers the complete delimiter suite: inline `$` and `\(`, display `$$` and `\[`.
  - Verify that tab and sub-tab switching callbacks invoke `renderMathOnElement(targetPanel)` to ensure newly revealed mathematical content renders crisply without raw LaTeX markup.
- [ ] **CP-TECH-6 (KaTeX List Isolation & Multi-Step Math Alignment)**:
  - 100% of comma-separated quantity/fraction lists formatted as individual math blocks (`$x$, $y$, $z$`), NEVER a single `$ ... $` block with `\quad`.
  - All multi-step derivations with 2+ equals signs or >40 characters inside cards broken cleanly using `\begin{aligned}` or line breaks.
  - Zero mismatched KaTeX delimiters (`$...$$` or `$$...$`).

---

## PART 6: CHANGELOG & VERSION HISTORY

| Version | Date | Key Architectural Additions |
| :---: | :---: | :--- |
| **v1.0** | 2026-09-02 | Initial operational checklist and early GITA 5-Tab rules. |
| **v1.1** | 2026-09-08 | Design SOP creation with KaTeX and CSS custom properties for notes pages. |
| **v1.2** | 2026-09-12 | Exam Pattern Pop-up Modal, 3×2 balanced grid, and timetable synchronization. |
| **v1.3** | 2026-09-13 | Collapsible vertical dock rail (1.2s delay), submodule partitioning, subparts grid, and syllabus batteries. |
| **v1.4** | 2026-09-13 | Mathematics Theme & GUI unification (Zero White Patches universal button reset, desktop margin push, floating jump-to-top). |
| **v2.0** | 2026-09-13 | **Master Unified SOP Consolidation**: Consolidated all separate design, operational, content, and GITA guidelines into a single authoritative master reference with subject-wise architectures and 4 comprehensive QA checkpoint suites. |
| **v2.1** | 2026-09-13 | **Syllabus Topic Tag Mapping & Completeness Standard (Topic-to-Battery Rule)**: Standardized that chapter card tags/tabs must directly reflect syllabus-prescribed topics, highlighted tags signify covered topics, dim tags indicate pending syllabus items, and the ratio directly determines the completeness percentage. |
| **v2.2** | 2026-09-13 | **Zero-Collision & Text Overwrite Prevention Standard (Universal Math & Layout Containment)**: Added Section 2.5, CP-GUI-7, and CP-TECH-6 establishing mandatory rules to prevent matter from crossing over and overwriting cards: atomic KaTeX math lists, `\begin{aligned}` multi-step math, universal `min-width: 0` / `overflow: hidden` card containment, and `minmax(280px, 1fr)` grid track minimums. |
| **v2.3** | 2026-09-13 | **Laptop Viewport Compatibility & Solved Examples Derivation Gate**: Established Section 2.5.1 and CP-GUI-8 ensuring full 1280px–1366px laptop compatibility with sidebar pinned/active: mandatory stacked `\begin{aligned}` formatting for all multi-step math in Solved Examples, `minmax(240px, 1fr)` responsive fallbacks, KaTeX display auto-scroll, and zero box overflow on Pushti's laptop screen. |
| **v2.5** | 2026-09-13 | **Two-Tier Navigation Architecture, Dock Rail Zero-Peeking Containment & Complete KaTeX Delimiter Suite**: Codified Section 3.1.2, CP-GUI-9, CP-GUI-10, and CP-TECH-7 establishing the Two-Tier Navigation standard (`.submodule-nav` pills breaking dense sections into short, screen-sized views to eliminate long vertical scrolling), strict collapsed dock rail text isolation (`.tab-label-group` width: 0 / opacity: 0 preventing letter peeking at 62px), and universal KaTeX auto-rendering for all 4 standard delimiters (`$`, `\(`, `$$`, `\[`) with dynamic re-rendering on tab and sub-tab transitions. |
| **v2.4** | 2026-09-13 | **Geometry Chapters Visual Standard (The Native Vector SVG Mandate)**: Codified Section 3.1.1 and Checkpoints CP-GEO-1 to CP-GEO-4 establishing the mandatory standard for all geometry chapters: complete replacement of scanned/pencil-scribbled textbook images with pristine native SVG vector graphics; 100% figure coverage across all illustrations, solved examples, drills, and practice questions; theme-adaptive color tokens; standard geometric symbols (parallel arrows, perpendicular squares, auxiliary dashed constructions); and strict laptop viewport containment. |
