# PUSHTI STUDY HUB — MASTER UNIFIED SOP (v3.5)
*The Definitive Architectural, Design, Pedagogical & Verification Standard for AI-Assisted Generation*

---

## PART 1: PHILOSOPHY & WORKFLOW FOUNDATIONS

### 1.1 Mission & Student Profile
* **Project Name**: Pushti Study Hub
* **Lead & Vision**: Hirak Soni (Father & Project Lead)
* **Student**: Pushti Soni, Class 7, CBSE Board (~12 years old)
* **Goal**: Provide a fun, aesthetically inspiring, rigorous, and self-sufficient learning environment.
* **Core Principle**: *"A child must NEVER need to open the textbook."* Every concept, solved example, exercise, diagram, formula, and enrichment context must exist in one cohesive, beautifully organized digital module.
* **Implicit Grade Standard (Zero "Class 7" Redundancy)**:
  Pushti Study Hub is built exclusively for Pushti Soni in Class 7 CBSE. Consequently, the entire portal's curriculum, difficulty level, and subject content are **implicitly and exclusively Class 7 CBSE**. AI models, developers, and documentation must **NEVER repeat or prepend "Class 7"** before chapter names, tab headers, document titles, or progress summaries unless explicitly contrasting two distinct academic standards (e.g. Class 6 prerequisite vs. Class 7 curriculum, or Class 7 vs. Class 8 Olympiad preview). In all other contexts, omitting "Class 7" is mandatory.

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

### 1.6 Publication Anonymization & Code-Name Standard
* **STRICT WEBSITE RULE**: Commercial publication, publisher, and private vendor names (e.g., **MTG**, **Cordova**, **Ratna Sagar**, **Goyal Brothers**, **Pearson**, **Selina**, **NCERT**, etc.) must **NEVER be displayed directly on the student-facing website UI** (badges, tags, headers, chapter titles, card descriptions, syllabus tables, or modal views).
* **Internal Documentation vs. Public UI Mapping**:
  | Internal Source / Documentation | Standard Website Display Label | Description / Role |
  | :--- | :--- | :--- |
  | **Primary / Prescribed Textbook** (e.g. MTG Foundation in Maths, prescribed reader) | **`Main`** / **`Main Course`** | Primary core curriculum foundation track |
  | **Secondary Textbook 1** (e.g. Cordova in Maths / Science) | **`Ref 1`** | Primary parallel reference track (exercises, drills, HOTS) |
  | **Secondary Textbook 2** (e.g. Ratna Sagar / Goyal) | **`Ref 2`** | Secondary parallel reference track |
  | **Secondary Textbook 3** | **`Ref 3`** | Tertiary reference track |
  | **Olympiad / Competitive Workbooks** | **`Advanced Track`** / **`Olympiad Prep`** | Advanced conceptual drills & high-order thinking problems |
* **Example Replacements**:
  - ❌ `"Dual Track: NCERT + Cordova Ch 1"` &rarr; ✅ `"Dual Track: Main + Ref 1 Ch 1"`
  - ❌ `"📙 Dual: MTG + Cordova Ch 11"` &rarr; ✅ `"📙 Dual: Main + Ref 1 Ch 11"`
  - ❌ `"Cordova Exercises 1.1–1.4"` &rarr; ✅ `"Ref 1 Exercises 1.1–1.4"`
  - ❌ `"MTG Aligned"` &rarr; ✅ `"Main Aligned"`
* Exact publication names may be recorded in developer notes, internal metadata, and SOP documentation, but the public UI must exclusively use the standardized code-names.

### 1.7 School Anonymization Standard (Zero Direct School Mentions & Admin-Only Profile Storage)
* **PRIVACY & SECURITY MANDATE**: The student's specific school name (e.g., **Silver Bells Public School**, or any specific private institution name) must **NEVER appear directly anywhere on the website UI**, page titles, banners, or syllabus tables.
* **Approved Generic Terminology**:
  - ❌ `"Silver Bells Public School Mid-Term Worksheet"` &rarr; ✅ `"School Curriculum Mid-Term Assessment Worksheet"`
  - ❌ `"Silver Bells Exam Pattern"` &rarr; ✅ `"Internal School Exam Pattern"`
  - ❌ `"Silver Bells Timetable"` &rarr; ✅ `"School Term Schedule & Timetable"`
* **Admin-Only Confidential Storage**:
  - In student profiles (`profile.html` and registration modals), **only the Student's Name and Parent's Name are visible** to regular viewers.
  - The **School Name is strictly confidential and reserved for the Admin only**. It is masked by default (`•••••••••••••••• [Admin Only]`) and guarded by Admin PIN verification.

### 1.8 Localhost Direct Navigation Protocol
* **MANDATORY HTTPS / LOCALHOST LINK**: At the conclusion of every chapter module (in the footer metadata / quick jump bar) and in all AI generation summaries, **always provide the direct local development link using HTTPS**:
  ```text
  https://localhost:8443/chapters/[subject]/[chapter_filename].html
  ```
  *(or the active local development port, e.g., `https://localhost:8443/...` or `https://127.0.0.1:8443/...`)*
* This ensures that during development, review, and verification, the user can instantly click to inspect the live running chapter module without searching the directory tree.

### 1.9 Student Authentication & Detailed Profile Architecture
* **Profile Data Schema & Visibility Hierarchy**:
  - **Visible Student Identity (Student & Parent View)**:
    - **Student's Full Name** (e.g., `Pushti Soni`)
    - **Father's / Guardian's Full Name** (e.g., `Hirak Soni`)
    - **Standard / Grade & Board** (e.g., `Class 7 CBSE`)
    - **Contact Credentials** (Student/Parent Phone & Email)
    - **Student Roll No. / ID**
  - **Confidential Identity (Admin Only)**:
    - **School's Name**: Restricted strictly to the **Admin only**. Never displayed publicly; masked in UI as `🔒 Admin Protected` with PIN verification required for inspection or editing.
* **Dedicated Profile Portal (`profile.html`)**:
  - Accessible via the user avatar across all site headers.
  - Features glassmorphism card layout with personal academic details, contact credentials, real-time study stats, and editable profile modal.
  - Integrated Admin School Name unlock mechanism (guarded by Admin security passkey).
  - Future-proof placeholder for enhanced password security, session timeout, and multi-factor authorization.

### 1.10 Standardized Knowledge Base Architecture (KB Files) & Zero-Waste Protocol
* **MANDATORY AUTHORITATIVE STORAGE**: All chapter knowledge bases are permanently structured under:
  ```text
  d:\Users\expor\Downloads\Codes\KB Files\<subject>\<chapter_folder>\
  ```
  *(and mirrored in `knowledge_base/<subject>/` for automated test generator engines)*.
* **THE FOUR TENETS OF KB GOVERNANCE**:
  1. **Refer SOP Before Starting**: Before processing any chapter request, the AI model (Gemini, Claude, Antigravity) must review `SOP.md` for anonymization, styling, UTF-8 safety, and formatting standards.
  2. **KB-First Retrieval Principle**: For any chapter task (answering student queries, explaining concepts, creating revision drills, or generating worksheets), the AI model MUST search and reference the chapter's KB file (`<chapter>.md` and `<chapter>.json`) first. Never ingest massive production HTML files (300KB+) or perform broad web searches.
  3. **Build Before Proceeding**: If a requested chapter does not yet possess a KB file in `KB Files/`, the AI model MUST compile the chapter's dual-file KB pair first, and only then proceed with the task.
  4. **Living Knowledge Base**: Any newly acquired knowledge, teacher notes, periodic drills, school exam problems, or corrections for that chapter must be immediately appended and synchronized back into that chapter's KB file.
  5. **Smart Token Conservation**: AI assistants must proactively provide smart recommendations to minimize token usage, such as querying structured KB files, using precise line slicing, and directing users to client-side test generation tools.

### 1.11 The "Hath Fero" Urban Planning & Deterministic Blueprint Protocol
* **Core Philosophy (The Urban Planning Metaphor)**:
  - **Subject = Province**: Sets the immutable grid system and street names for all its cities.
  - **Chapter = City**: Structurally identical footprint. Only the **Color Palette (Accent Theme)** and the **Curriculum Content** differ.
  - **Primary Navigation Tabs = Main Roads / Avenues**: Must have **strictly deterministic indices (1 to N)**. For any chapter in that province, Tab 1 is always the same type of content, Tab 2 is always the same, Tab 3 is always the same.
  - **Submodule Pills = Sub-streets & Blocks**: Inside any tab, sub-pills (e.g. Drills: MCQs, Fill in the Blanks, True/False) follow an **invariant 1 to M sequence**.
  - **The "Doozy Kid" Standard**: Even a tired or distracted 12-year-old child must know by instant muscle memory exactly which tab and sub-pill contains notes, exercises, or interactive practice without searching or guessing.
* **The Zero-Hallucination & "Pending Content" Sentinel**:
  - Under no circumstances may an AI assistant omit, drop, or renumber a mandatory street/tab simply because content for that section is not yet ready or in the knowledge base.
  - If content is missing, the AI MUST render the standardized **Pending Content Sentinel**:
    ```html
    <div class="pending-content-card">
      <div class="pending-icon"><i class="fas fa-hammer"></i></div>
      <div class="pending-body">
        <h4 class="pending-title">[Pending Content: Section Name]</h4>
        <p class="pending-desc">This curriculum street is structured in the master blueprint but pending authoring/addition. No content currently keyed.</p>
        <div class="pending-badge"><i class="fas fa-exclamation-circle"></i> PENDING_ADDITION &bull; Content Needed Here</div>
      </div>
    </div>
    ```
  - This prevents layout shifts, prevents AI hallucination, and gives the parent/admin immediate visual clarity on pending items.
* **Invocation Protocol**: When the user invokes `"Hath Fero [scope]"`, the AI model automatically runs a comprehensive audit across all chapters of that province, verifies street indices, sub-streets, color theme isolation, checks relative path depths, and leaves the Hath Fero verification stamp.


---

## PART 2: UNIVERSAL UI/UX & DESIGN SYSTEM (ALL PAGES)

### 2.1 Standard Frontend Stacks & CDN Architecture
Pushti Study Hub authorizes two complementary frontend stacks tailored to subject pedagogical requirements:

#### Stack A: Pure Custom Properties + KaTeX Engine (High-Density Mathematical Modules)
*Used for Mathematics (Ganita Prakash), Algebra, Geometry, and heavy formula-driven modules.*
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
    onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\[',right:'\\]',display:true},{left:'$',right:'$',display:false},{left:'\\(',right:'\\)',display:false}],throwOnError:false});"></script>
</head>
```

#### Stack B: Modern Tailwind Utility + Lucide Vector Engine (Interactive Simulations & Visual Hubs)
*Authorized and recommended for Social Science (Geography, History, Civics), Science (Physics, Chemistry, Biology), and rich visual media hubs requiring responsive card grids, live search engines, dynamic simulators, and fluid dark/light transitions.*
```html
<!DOCTYPE html>
<html lang="en" class="dark" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Chapter Title] — [Subject] | Pushti Study Hub</title>
  
  <!-- Inter & Outfit Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
            heading: ['Outfit', 'sans-serif'],
            mono: ['Space Mono', 'monospace'],
          }
        }
      }
    }
  </script>

  <!-- Lucide Icons (SVG-native, razor sharp, zero font flicker) -->
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
```
* **Strict Rule on Heavy JS Frameworks**: Heavy single-page-app runtimes (React, Vue, Angular) and legacy libraries (jQuery) remain strictly prohibited across both stacks. All dynamic features (simulators, quiz engines, search filters, flipcards) must be authored in fast, zero-dependency vanilla JavaScript.

### 2.2 Dynamic Theming & Dual Token Parity
All pages must support flawless Dark and Light mode switching with state persistence in `localStorage.getItem('pushti-theme')`:

* **Stack A (Pure CSS Custom Properties)**:
  Uses `:root` for Dark mode defaults and `[data-theme="light"]` for Light mode overrides:
  ```css
  :root {
    --primary: #6366f1;
    --primary-glow: #818cf8;
    --bg-main: #0a0e1a;
    --bg-card: rgba(15, 23, 42, 0.85);
    --surface: #131d31;
    --text-main: #e2e8f0;
    --text-muted: #94a3b8;
    --text-title: #ffffff;
    --border: rgba(255, 255, 255, 0.08);
  }
  [data-theme="light"] {
    --bg-main: #f8fafc;
    --bg-card: #ffffff;
    --surface: #f1f5f9;
    --text-main: #1e293b;
    --text-muted: #64748b;
    --text-title: #0f172a;
    --border: rgba(0, 0, 0, 0.08);
  }
  ```

* **Stack B (Tailwind Dual Class & Attribute Synchronization)**:
  To ensure 100% interoperability with iframe wrappers and parent dashboard listeners, Tailwind toggle handlers must update **both** the HTML class and the `data-theme` attribute:
  ```javascript
  function toggleTheme() {
    const html = document.documentElement;
    const isDark = html.classList.contains('dark');
    const newTheme = isDark ? 'light' : 'dark';
    
    if (isDark) {
      html.classList.remove('dark');
      html.setAttribute('data-theme', 'light');
    } else {
      html.classList.add('dark');
      html.setAttribute('data-theme', 'dark');
    }
    localStorage.setItem('pushti-theme', newTheme);
    updateThemeIcon(newTheme);
    
    if (window.parent && window.parent !== window) {
      window.parent.postMessage({ theme: newTheme }, '*');
    }
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

### 2.4.1 Maximum Horizontal Real-Estate Utilization Standard (Wide Desktop & Laptop Viewports)
* **The Problem (Wasted Horizontal Space)**:
  Restricting main content containers to narrow arbitrary widths (e.g. `max-width: 1000px` or `1200px`) on modern 1366px, 1440px, and 1920px widescreen displays wastes significant horizontal real estate, leaving empty voids on the right and forcing unnecessarily long vertical page scrolling. Stacking MCQ options, True/False items, or question cards in single vertical columns further inflates page height.
* **Mandatory Horizontal Utilization Rules**:
  1. **Generous Main Content Max-Width**: Main content wrappers (`.main-content`) must set `max-width: 1600px;` (or `width: calc(100% - var(--sidebar-width)); max-width: 1650px; box-sizing: border-box;`) so that content utilizes the available desktop and laptop monitor width effectively.
  2. **Responsive Multi-Column Question Grids**:
     In exercise modules, exam papers, and worksheet sections, questions (MCQs, FIBs, True/False, Short Q&A) must utilize responsive 2-column grids on desktop/laptop viewports (`@media (min-width: 1024px) { grid-template-columns: repeat(2, 1fr); gap: 18px; }`), cutting vertical scroll depth by nearly 50%.
  3. **2x2 MCQ Option Layout**:
     Inside MCQ cards, the four options (a, b, c, d) must be arranged in a responsive 2-column grid (`grid-template-columns: repeat(2, 1fr); gap: 10px;` falling back to `1fr` on mobile screens `< 640px`), eliminating tall single-column stacks.
  4. **Multi-Column Concept & Enrichment Grids**:
     Formula cards, flashcards, subtraction drills, and trivia cards must use auto-fit grids (`grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));` or `repeat(2, 1fr)`), actively populating screen width with rich learning components.
  5. **Defensive Containment (`min-width: 0 !important;`)**:
     To avoid horizontal overflow or card collisions, all grid items and question cards must declare `min-width: 0 !important; box-sizing: border-box !important;`.

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

### 2.5.2 Mathematical Typography & Fraction Legibility Standard
* **The Class 7 Ergonomics Principle**: Mathematical expressions and fractions must be instantly readable without eye strain. In standard KaTeX, inline $\frac{a}{b}$ defaults to \textstyle, which automatically compresses numerators and denominators into script size (\scriptstyle ~10px on standard displays). This makes fractions appear as tiny, illegible specks—especially inside spacious cards.
* **Mandatory KaTeX Fraction Standards**:
  1. **Display Fractions (\dfrac) for Subparts & Prompts**:
     - Whenever a standalone fraction, conversion prompt, or subpart item is presented (e.g. (i) 5/100, (ii) 16/1000), always write \dfrac (e.g., $\dfrac{5}{100}$, $\dfrac{16}{1000}$, $\dfrac{254}{1000}$) instead of \frac.
     - \dfrac forces full display-style typography, ensuring numerator and denominator numbers are rendered at full regular text height (16px–18px+).
  2. **KaTeX Font Size Amplification**:
     - Every mathematical stylesheet must include base font magnification for math elements:
       `css
       .katex {
         font-size: 1.12em; /* Elevates base KaTeX math readability */
       }
       .subpart-item .katex, .subpart-chip .katex, .fraction-box .katex {
         font-size: 1.25em; /* Guarantees standalone fractions and subparts are bold and legible */
       }
       `

### 2.5.3 Adaptive Subpart Layouts (Atomic Chips vs. Verbose Grids)
* **The Screen Real-Estate Reality**:
  - The previous rule specifying minmax(280px, 1fr) was designed specifically for **verbose descriptive subparts** (multi-sentence word problems or worked derivations).
  - When applied indiscriminately to **atomic mathematical subparts** (<=25 characters, e.g. (i) 5/100, (a) 0.34, (i) 49 paise), minmax(280px, 1fr) creates bloated 280px-wide boxes that wrap into 3 + 1 on laptops, leaving the 4th item awkwardly stranded on the second line with 66% empty void.
* **Adaptive Subpart Classification Standard**:
  1. **Atomic Mathematical Subparts** (Single fractions, decimals, simple equations, terms <=25 characters):
     - **MUST USE** .subparts-chips (flex-wrap) or .subparts-grid.compact (grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); or 
epeat(4, 1fr) on laptop/desktop viewports).
     - Standard styling:
       `css
       .subparts-grid.compact {
         display: grid;
         grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
         gap: 10px;
         margin: 10px 0;
         width: 100%;
       }
       .subparts-chips {
         display: flex;
         flex-wrap: wrap;
         gap: 10px;
         margin: 10px 0;
       }
       .subpart-chip {
         display: inline-flex;
         align-items: center;
         justify-content: center;
         gap: 8px;
         padding: 8px 14px;
         background: var(--surface);
         border: 1px solid var(--border);
         border-radius: 8px;
         font-size: 1.05rem;
         font-weight: 600;
         transition: all 0.2s ease;
         min-width: 0;
         box-sizing: border-box;
       }
       .subpart-chip:hover {
         border-color: var(--primary);
         background: var(--primary-deep);
       }
       .subpart-chip .subpart-num {
         color: var(--primary-glow);
         font-family: var(--font-mono);
         font-weight: 700;
         font-size: 0.92rem;
       }
       `
     - **Result**: All 4 subparts (i), (ii), (iii), (iv) sit side-by-side in **one single, compact row** on laptop and desktop displays. Zero stranded boxes, and question card vertical height is reduced by over 50%!
  2. **Verbose Descriptive Subparts** (Full-sentence word problems, multi-line questions):
     - Continue to use .subparts-grid (minmax(280px, 1fr)) with flex-labeled rows (.subpart-label + .subpart-text).

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
1. **Floating Jump-to-Top Button (`#scrollTopBtn` or `scroll_to_top.js`)**:
   - Circular 44px button fixed at `bottom: 24px; right: 24px; z-index: 999;`.
   - Reveals smoothly with `opacity: 1; pointer-events: auto;` when page scrolls beyond 300px (or 80px in `scroll_to_top.js`).
   - Smoothly scrolls to the top on click (`window.scrollTo({ top: 0, behavior: 'smooth' })`).
2. **Firebase Study Telemetry**:
   - Background heartbeat logging active study seconds every 60 seconds into Firestore `user_stats` for Pushti and Hirak (`import { db, doc, getDoc, setDoc } from "../../firebase-config.js"`).
3. **Custom Luminous Scrollbars**:
   - Discrete 6px scrollbars (`::-webkit-scrollbar { width: 6px; height: 6px; }`) matching theme tokens (`var(--surface)` track, `var(--border)` thumb, `var(--primary)` hover).

### 2.8 Usability, UX & Modern Reactive Component Standards
Every interactive chapter must adhere to modern web usability best practices:

1. **Debounced Live Search (`debounce(fn, 180)`)**:
   - Real-time search inputs (such as question banks, vocabulary directories, or theorem indexes) must be debounced by 150ms–250ms to prevent browser frame drops and layout jitter while typing.
   - Search should match across question statements, sub-parts, options, and model answer text.

2. **Mandatory Empty State Component (The Zero "Dead Screen" Rule)**:
   - When a student applies a filter or types a search query that yields zero results, the page must **NEVER** present a blank, broken-looking screen.
   - An explicit Empty State card must dynamically render with:
     - A contextual vector icon (e.g. Lucide `search-x` or `filter-x`).
     - A clear, friendly explanation (e.g. *"No matching textbook questions found"*).
     - A prominent 1-click action button (e.g. `<button onclick="clearSearchFilter()">Clear Search / Reset</button>`) that instantly clears the input and restores full content visibility.

3. **GPU-Accelerated 3D Transforms for Mental Flashcards**:
   - Mental recall flashcards must utilize hardware-accelerated 3D flip mechanics:
     ```css
     .perspective-1000 { perspective: 1000px; }
     .transform-style-preserve-3d { transform-style: preserve-3d; }
     .backface-hidden { backface-visibility: hidden; -webkit-backface-visibility: hidden; }
     .rotate-y-180 { transform: rotateY(180deg); }
     ```
   - Clicking or keyboard-triggering flips the card between Front (Question / Concept Name) and Back (Textbook Definition + "Why It Matters / Common Exam Trap").

4. **Micro-Interactions & State Transition Feedback**:
   - Hover elevations: Clickable action pills and cards should lift smoothly on hover (`transform: translateY(-2px);` with `transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);`).
   - Active click feedback: Instant visual scale reduction (`transform: scale(0.98);`) upon active mouse down.
   - Dynamic badges: Active filter pills must display live counter badges (e.g. `Sections [All 28]`, `MCQs [4]`) reflecting matching item counts.

### 2.9 Universal Data & Table Alignment Standard (Left for Text, Right for Numbers)
* **The Core Typographical & Cognitive Mandate**:
  Proper alignment in tabular data and listings drastically lowers cognitive overhead, enabling Pushti to scan, compare, and comprehend data effortlessly:
  1. **Left Alignment for Text (`text-align: left;`)**:
     - All textual data—including subject titles, question statements, concept definitions, MCQ option text, explanations, descriptions, and statuses—**MUST be left-aligned**.
     - Left-aligned text creates a uniform, predictable reading edge on the left margin, preventing ragged starting points and optimizing eye travel speed.
     - Table column headers for textual columns (`<th>`) must also be left-aligned to visually anchor the column text.
  2. **Right Alignment for Numbers (`text-align: right;`)**:
     - All numeric values—including question numbers (`Q#`, `#`, `Sr. No.`), scores, marks, counts, percentages, dimensions, times/durations, page numbers, and statistical metrics—**MUST be right-aligned**.
     - Right-alignment guarantees that units, tens, hundreds, and decimal points align vertically, providing instant visual cues regarding magnitude and scale.
     - Table column headers for numeric columns (`<th>`) must likewise be right-aligned directly above the figures.
     - **Tabular Numerals**: Numeric cells and columns should declare `font-variant-numeric: tabular-nums;` or utilize monospace fonts (`'Space Mono'`, `'JetBrains Mono'`) so all digits occupy identical horizontal widths.
  3. **Table CSS Implementation Standard (Universal Specification)**:
     ```css
     /* Default table styles: text-align: left for all text cells & headers */
     .key-table, .data-table {
       width: 100%;
       border-collapse: collapse;
       font-size: 0.82rem;
     }
     .key-table th, .key-table td,
     .data-table th, .data-table td {
       padding: 8px 12px;
       border: 1px solid var(--border);
       text-align: left; /* Mandatory: Left alignment for text */
     }
     
     /* Explicit numeric columns: text-align: right with tabular numerals */
     .key-table th.col-num, .key-table td.col-num,
     .data-table th.col-num, .data-table td.col-num,
     .num-cell, .col-marks, .col-score, .col-count {
       text-align: right !important; /* Mandatory: Right alignment for numbers */
       font-variant-numeric: tabular-nums;
       padding-right: 14px;
       font-family: 'Space Mono', 'JetBrains Mono', monospace;
     }
     ```

### 2.10 Clean Titling, Breadcrumb & Card Nomenclature (Elimination of Redundant Grade Prefixes)
* **The Single-Audience Standard**:
  Because Pushti Study Hub is built exclusively for Pushti in Class 7 CBSE, all grade-level context is implicit. Explicit grade tags add visual clutter without providing value.
* **Mandatory Titling & Header Guidelines**:
  1. **Page `<title>` & Site Header**:
     - Format `<title>` tags cleanly: `[Chapter Title] | [Subject] | Pushti Study Hub` (e.g. `Arithmetic Expressions | Mathematics | Pushti Study Hub`).
     - Breadcrumbs in `.site-header` follow: `Home > [Subject] > [Chapter Name]` (e.g. `Home > Mathematics > Chapter 2: Arithmetic Expressions`).
     - **Never inject "Class 7"** into the title tag, breadcrumb trail, or chapter banner.
  2. **Chapter Cards & Navigation Tabs**:
     - Card headers on subject hubs (`maths_index.html`, etc.) must display the clean chapter title and number (e.g. `02. Arithmetic Expressions`).
     - Dock rail tabs must use clean titles: `Tab 10: Practice Test Paper`, `Tab 9: Practice Test Paper (Cordova Ch 11 • 28 Qs)`.
     - Test paper labels, modal titles, and action pills must remain clean without prefixing `"Class 7"`.
* **The Sole Exception (Multi-Standard Comparison)**:
  - Mentioning a class or grade standard is **strictly prohibited UNLESS** explicitly contrasting two different academic standards (e.g., comparing *"Class 6 Prerequisite: Fractions"* vs *"Class 7: Rational Numbers"*, or referencing a *"Class 8 Advanced Olympiad Preview"*). If no second standard is being compared, omission of `"Class 7"` is mandatory.

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
*Exemplified in Chapter 5 (Parallel and Intersecting Lines) and mandatory across all present and future Geometry modules.*

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

3. **Required Submodule Stylesheet Architecture (Zero-Horizontal-Scroll & Sticky Docking Mandate)**:
   - **Sticky Top-Docking Rule**: To maintain navigation context and prevent students from losing their place during deep problem sets or multi-section exercises, Tier 2 navigation pills (`.submodule-nav`), exam control bars (`.exam-control-bar`), and interactive filter bars (`.sticky-search-bar`) must stick to the top of the viewport when scrolling, anchored precisely beneath the sticky `.site-header` (`top: var(--header-height); z-index: 900; background: var(--bg-sticky); backdrop-filter: blur(12px);`).
   ```css
   .submodule-nav {
     position: sticky;
     top: var(--header-height);
     z-index: 900;
     background: var(--bg-sticky);
     backdrop-filter: blur(12px);
     -webkit-backdrop-filter: blur(12px);
     display: flex;
     flex-wrap: wrap;
     gap: 8px;
     padding: 10px 0;
     margin-bottom: 20px;
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

### 3.1.3 Strict Textbook Visual & Notation Fidelity Mandate (Zero Creative Alteration Rule)
*Mandated by Lead Hirak Soni (13 Sep 2026) following rigorous Geometry Chapter 5 textbook audits.*

1. **The Principle of Absolute Textbook Alignment**:
   - In all geometry and mathematics chapters, **never invent, rotate, rename, or approximate** geometric elements from the textbook.
   - When converting textbook figures to native SVGs, the diagram must match the official textbook PDF **100% in topology, orientation, and labeling**.
   - Under no circumstances should an AI model invent arbitrary letter names ($A, B, C, D, O$) when the textbook presents unlabelled rays, nor should it substitute horizontal lines when the textbook depicts vertical or slanted lines.

2. **Core Invariants for Geometric Reproduction**:
   - **Line & Vertex Naming**: Use the EXACT vertex letters given in the textbook ($A, B, C, D, \dots$ or $l, m, t$).
     - If the textbook labels a figure with rays meeting at a common vertex without letters ($45^\circ, 45^\circ, x, 200^\circ$), do NOT invent arbitrary letter names like $A, B, C, D, O$.
     - If the textbook uses $IKBA \parallel GED$, keep precisely $IKBA \parallel GED$. Never simplify or re-letter.
   - **Orientation & Slopes**: Never arbitrarily rotate vertical lines into horizontal lines or vice versa:
     - If the textbook shows three **vertical** parallel lines ($AB \parallel CD \parallel EF$ with horizontal perpendicular $EA \perp AB$ as in p. 125 Q5), they **must** be rendered as vertical lines.
     - If the textbook shows slanted parallel lines ($\nearrow l \parallel m$), render them slanted $\nearrow$, not horizontal.
     - If the textbook shows a vertical zig-zag between lines $LM \parallel PQ$, render the vertical zig-zag exactly as printed.
     - If the textbook presents an hourglass configuration ($AB$ and $CD$ vertical segments crossed by diagonals $AD$ and $BC$), never draw them horizontally.
   - **Ray & Arrow Directions**: Arrowheads and ray vectors must point in the exact directions specified in the textbook. Single arrows ($\rightarrow$) and double arrows ($\twoheadrightarrow$) indicating parallel pairs must be faithfully preserved.
   - **Question Alignment**: Every question and worked solution must correspond directly to the diagram as drawn. A student looking at the textbook and looking at the screen must see an identical geometric configuration.
   - **Dual-Verification Step**: Every geometry SVG must be visually cross-referenced against high-resolution crops of the official textbook PDF before deployment.

### 3.1.4 Universal Mathematics Solution Visibility Standard (All Solutions Hidden by Default)
* **The Active Practice Pedagogical Principle**:
  - In Mathematics, passive reading of solutions inhibits deep cognitive retention. Pushti must encounter the problem statement first, challenge herself to solve it mentally or in her notebook, and only reveal worked steps when needed to check answers or overcome obstacles.
* **Non-Negotiable Rules**:
  1. **100% of Solutions Closed on Page Load**:
     - Every single solution drawer, worked derivation, exercise answer, and explanation container in all Mathematics modules MUST be **hidden (collapsed) by default**.
     - The `open` attribute on `<details class="solution-drawer">`, `<details class="solution-details">`, or any answer accordion is **strictly prohibited on initial load**.
     - Only the prompt, question number, subpart chips/cards, and `<summary><i class="fas fa-chevron-down"></i> Step-by-Step Mathematical Working</summary>` (or equivalent button) should be visible initially.
  2. **Zero Auto-Reveal on Tab Transitions**:
     - Navigating between tabs, sub-tabs, or drills must NEVER programmatically expand solution drawers. All drawers must remain closed until the student explicitly clicks `<summary>` to reveal.
  3. **Self-Assessment & Reveal Consistency**:
     - When revealed, the solution accordion displays complete step-by-step working, common pitfall warnings, and self-assessment buttons (`Got It`, `Needs Review`), keeping the student in full control of her learning pace.


### 3.2 Science & Social Science Architecture (The Modern Interactive Simulation & Searchable Solutions Hub Standard - v3.0)
*Exemplified in Geography Chapter 1 (Interior of the Earth) and Science modules.*

#### 3.2.1 Evolution Beyond Legacy GITA Mark-Split Tabs
The legacy GITA format split textbook exercises artificially by mark count (Tab 3: 2/3 Marks vs. Tab 4: 4+ Marks). Student usability testing revealed that this fragmented textbook exercises and forced students to bounce between tabs just to check homework solutions.

Under **v3.0**, all Science and Social Science modules adopt the **5-Module Interactive Simulation & Searchable Solutions Architecture**:

1. **Module 1: Interactive Phenomenon / Structural Explorer**:
   - Native vector SVG cutaway or apparatus inspector (e.g. Earth's Interior, Plant/Animal Cell Anatomy, Electric Circuit, Eye Model).
   - Interactive element selection: Clicking any sub-component (e.g. Continental Crust, Oceanic Crust, Mantle, Outer Core, Inner Core) dynamically updates a synchronized **Telemetry & Composition Inspector Card** in real time.
   - Comparative metric tables (e.g. SIAL vs. SIMA, thickness, temperature, mineral composition, physical state).

2. **Module 2: Dynamic Process & Cycle Simulator**:
   - Interactive multi-stage stepping animation (e.g. The 5-Stage Rock Cycle: Magma $\rightarrow$ Igneous $\rightarrow$ Sediments $\rightarrow$ Sedimentary $\rightarrow$ Metamorphic $\rightarrow$ Magma; Water Cycle; Photosynthesis; Nitrogen Cycle).
   - Student can step sequentially through stages or click directly to inspect stage physics, transformations, and chemical conditions.
   - **Real-Life Indian Anchors**: Every scientific process must connect directly to tangible Indian geological or environmental examples (e.g., Deccan Traps basalt in Maharashtra/Gujarat, Red Fort red sandstone in Delhi, Taj Mahal Makrana marble in Rajasthan, granite grinding stones in Indian kitchens).

3. **Module 3: Universal Textbook Solutions Hub (Searchable & Categorized)**:
   - **100% Textbook Coverage**: Unites ALL textbook exercise sections (Sections A through H: Multiple Choice, Fill in the Blanks, Match the Columns, Very Short Answer, Short Answer, Long Answer, Give Reasons, Fun Activities & Puzzles) in **ONE unified, cohesive directory**.
   - **Live Debounced Keyword Search**: Students can search for any word, mineral, concept, or question number with instant 60fps filtering.
   - **Quick-Category Pill Filters**: Category tabs (*All, MCQs, Blanks, Match, Short, Long, Give Reasons, Fun Drills*) with dynamic question count badges.
   - **Self-Assessment Question Cards**: Numbered question badges, clean question statements, model step-by-step answers, and highlighted exam tips.
   - **Mandatory Empty State**: Displays an illustrated empty state card with a 1-click `"Clear Filter"` button whenever a search returns 0 matches.

4. **Module 4: Interactive Auto-Grading Quiz Engine**:
   - 10–15 objective questions with instant visual feedback (emerald outline for correct, rose outline for incorrect).
   - **Educational Explanation Keys (`exp`)**: Every question must display an explanation detailing *why* the answer is correct and warning against common student traps.
   - Real-time progress bar, questions-answered counter, and a final score evaluation card with personalized revision guidance.

5. **Module 5: 3D Revision Flashcards & Conceptual Traps**:
   - 10+ hardware-accelerated 3D flipcards (Front: Concept Name / Question; Back: Verbatim Textbook Definition + "Why It Matters / Common Exam Misconception").
   - Covers high-school curiosity previews (e.g. Kola Superdeep Borehole, South African gold mines, why the inner core remains solid despite $5000^\circ\text{C}$ temperatures).

#### 3.2.2 Subject-Wise Navigation Layout Standard: Top Sticky Bar vs. Left Dock Rail
To prevent visual crowding and optimize screen geometry:
* **Mathematics & Heavy Algebra Modules**:
  - Use the **62px Collapsible Left Dock Rail** (expanding to 280px on 0.72s hover or pin). Mathematics derivations are vertically deep and horizontally compact, making left docks ideal to reclaim horizontal margin.
* **Science, Social Science & Visual Simulation Modules**:
  - Use the **Top Sticky Glassmorphic Navigation Bar** with horizontal wrapping pill tabs (`flex-wrap: wrap; gap: 8px;`).
  - **Reason**: Science and Geography require wide landscape canvas space for side-by-side SVG inspectors (450px cutaway + 400px telemetry card) and 4-column comparative matrices. A permanent left rail constricts these diagrams on 1366px laptop screens. The top sticky bar provides 100% viewport width while keeping navigation pinned and accessible at all times.

### 3.3 Vocational & Non-Exam Architecture (The Kaushal Bodh / KB Model)
* Designed for vocational, craft, and co-curricular subjects (e.g. Kaushal Bodh).
* **Two-Tier Navigation**:
  - Tier 1: Left category sidebar organizing units into thematic branches (*Life Forms*, *Machines & Tools*, *Materials & Arts*).
  - Tier 2: Project cards with inline activity subtabs switching between compact activity panes.
* Clear non-exam badges (`Non-Exam Vocational Subject`) to remove test anxiety while emphasizing hands-on mastery.

### 3.4 Languages Architecture (Sanskrit & English)
* **Bilingual Vocabulary Cards**: Word-by-word Sanskrit-to-Hindi/English and English vocabulary cards.
* **Grammar & Sentence Construction Tabs**: Interactive verb conjugation grids (धातुरूपाणि), noun declensions (शब्दरूपाणि), and sentence formation drills.
* **Translation Walkthroughs**: Shlokas and prose broken into individual padachheda with anvaya and poetic meaning.

### 3.5 ICT (Information & Communications Technology) Architecture & The 3-Tier Pedagogical Standard
* **Universal 7-Tab Dock Rail Architecture**:
  Every ICT chapter (`chapters/ict/ict_*.html`) MUST strictly implement the 7-Tab glassmorphic collapsible sidebar dock rail:
  1. `tab-theory`: **Comprehensive Concept Mastery** with sticky submodule filter bar.
  2. `tab-exercises`: **Textbook Solved Exercises ("Let's Exercise")** (100% closed drawers).
  3. `tab-worksheet`: **School Assessment Worksheet** (Instant interactive validation).
  4. `tab-exam`: **Terminal School Exam Paper** (Strict 40-Mark Blueprint: Q1 10 MCQs × 1M, Q2 5 FIBs × 1M, Q3 5 TF × 1M, Q4 6 Short × 2M, Q5 2 Long × 4M).
  5. `tab-drills` / `tab-simulators`: **Interactive Laboratories & Simulators** (Vanilla JS, zero external dependencies).
  6. `tab-enrichment`: **Enrichment & Olympiad Question Bank** (Live debounced search & counter).
  7. `tab-flashcards`: **Interactive 3D Flip Flashcards & Rapid Recall** (16+ cards with 3D flip transform).

* **The Mandatory 3-Tier Pedagogical Model (In Tab 1 Theory)**:
  To eliminate abstract cognitive friction and ensure joyful self-study for Pushti:
  1. **Tier 1 (Hook & Hardware Warm-Up)**:
     - Pre-lesson motivation hook: Connect the chapter topic to physical computer hardware or human real-world activity (e.g. transistors as light switches in Number Systems; bookkeeping vs automated formulas in Excel; sensors and cognition in AI).
     - Intuitive non-technical analogies before introducing formal mathematical or syntax definitions.
  2. **Tier 2 (Visual Framework & Progressive Worked Examples)**:
     - **Visual Concept Framework**: Conversion ladders with bottom-to-top arrows, positional expansion grids, cell-referencing drag tables, chart component diagrams, and logic flowcharts.
     - **3-Tier Progressive Worked Drills**: Level 1 (Beginner) &rarr; Level 2 (Standard Exam) &rarr; Level 3 (Tricky/Edge-Case) with step-by-step reasoning.
     - **Common Student Traps ("Watch Out")**: Alert callout boxes highlighting common exam blunders.
  3. **Tier 3 (Chapter Wrap-Up & Master Revision Cheat-Sheet)**:
     - **"In a Nutshell"**: 5-bullet executive takeaway summary.
     - **Master Quick-Reference Lookup Matrix / Formula Sheet**: Side-by-side comparative table of all key values, formulas, or syntax rules.
     - **Top 5 Exam Traps & Common Student Mistakes**: Highlight the 5 most frequent mistakes students make on school exams with corrections.

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

### 4.4 Subject Hub Centralized Test & Exam Prep Architecture (`#tab-tests` & `#sec-tests`)
* **The Centralization & Decoupling Mandate**:
  All school test papers, terminal examination blueprints, revision worksheets, practice test modules, and diagnostic drills must be collected and presented in a dedicated **"Tests & Exam Prep"** tab (`#tab-tests` -> `#sec-tests`) on each subject hub (`maths_index.html`, `hindi_index.html`, `science_index.html`, `sanskrit_index.html`, `english_index.html`, `social_science_index.html`, `ict_index.html`).
* **Zero Scattering Rule**:
  Tests, worksheets, and exam prep modules must **NEVER be buried or scattered inside individual chapter modules**. They are preserved in this dedicated subject tab to provide a single, organized assessment portal for rapid exam preparation.
* **Mandatory Administration & Exam Context Metadata**:
  Every test paper card in `#sec-tests` must explicitly record:
  1. **Administration Timing & Date**: Exactly when the test was administered (e.g. `Given: Sep 2026`).
  2. **Target Examination Role**: The specific exam it prepares the student for (e.g. `🎯 Mid-Term (80M)`, `🎯 Half-Yearly Exam Blueprint`).
  3. **Curricular & Section Scope**: Clear breakdown of sections, chapters, or questions covered (e.g. `खण्ड 'क' अपठित बोध (14M)`, `खण्ड 'ख' व्याकरण (16M)`, `Ch 1–8 Literature (30M)`, `रचनात्मक लेखन (20M)`).
  4. **Multi-Source Action Triggers**: Direct launch links to interactive practice modules (`.btn-gemini`, `.btn-claude`) and high-resolution PDF scans of the original school test papers whenever available.
* **Deep-Link Protocol & Hash State Switcher**:
  Every subject hub must support direct deep-linking via URL hash:
  ```javascript
  document.addEventListener('DOMContentLoaded', () => {
      if (window.location.hash === '#tests') {
          showCategory('tests');
      }
  });
  ```
  This allows portals (`index.html`, `midterm.html`, `timetable.html`) to link straight into the subject's test bank (e.g. `hindi_index.html#tests`).
* **Standalone Practice Test Layout Standards**:
  When authoring or updating standalone test modules (e.g. `practice_hindi_midterm_worksheet.html`):
  1. **Strict Left Dock Rail**: Use the standard SOP collapsible sidebar rail (`.sidebar` 64px collapsed, 280px pinned with `#pin-btn`, zero text peeking). Top horizontal tabs are strictly forbidden.
  2. **High-Density 4-Column Single-Line MCQ Layout**: Use `.mcq-grid` with `grid-template-columns: repeat(4, 1fr)` (switching to 2 columns on tablet, 1 column on mobile) so that short, concise options sit cleanly on a single row without bulky 2-row wrapping.
  3. **Subject-Appropriate Typography**: Enhance visual appeal and focus with rich typography (e.g. `Rozha One`, `Yatra One`, `Poppins`, `Outfit`, `Space Mono`).
  4. **Hidden Solutions**: 100% of solutions collapsed by default (`open details = 0`).

### 4.5 Verified Badges, Notification Dots & Syllabus Batteries
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

### 4.6 Syllabus Topic Tag Mapping & Completeness Calculation Standard (The Topic-to-Battery Rule)
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
- [ ] **CP-MATH-3 (Zero Default-Open Solutions Gate)**: In all Mathematics chapters, verify that 100% of solution drawers, worked step accordions, and exercise answers are collapsed by default. The `open` attribute on `<details>` is strictly forbidden on initial load (open count == 0 across all solution drawers).
- [ ] **CP-MATH-2 (Fraction Readability & Subpart Compactness Gate)**: Are all standalone fractions formatted with \dfrac or font-amplified KaTeX (>=1.15em)? Do atomic mathematical subparts (<=25 chars) use compact chips/grids (minmax(140px, 1fr) or flex chips) fitting 4 subparts in a single row on laptop viewports without stranding an orphaned box on a second row?
- [ ] **CP-GUI-11 (Empty State & Search UX Gate)**: Does every search-enabled or filtered directory implement a dedicated empty state container with an illustrative vector icon, friendly message, and an actionable 1-click "Clear Filters" button when 0 results match?
- [ ] **CP-GUI-12 (Dual-Theme Token Parity Gate)**: In Tailwind CSS modules, are both `class="dark"` and `data-theme="dark"` / `data-theme="light"` attributes synchronized on `<html>` to guarantee flawless parent dashboard and iframe interoperability?

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
- [ ] **CP-GEO-5 (Strict Visual & Notation Fidelity with Textbook PDF)**: In all geometry chapters, have all figures been cross-verified against high-resolution crops of the official textbook PDF? Are all line names, vertex letters, ray directions, orientations (vertical vs. horizontal vs. slanted), and question alignments 100% faithful with zero invented letters, zero arbitrary rotations, and zero altered notations?


### Checkpoint Suite 3: Intent & Student Experience
- [ ] **CP-INT-1 (Self-Sufficiency)**: Can Pushti study this page and achieve 100% without opening the textbook or searching online?
- [ ] **CP-INT-2 (No Cluttered Anchor Jumps)**: Are dense sections partitioned into clean sub-panes rather than chaotic in-page jump links?
- [ ] **CP-INT-3 (Mental Flashcards for Subjective)**: Are subjective questions formatted as revealable flashcards without requiring tedious typing?
- [ ] **CP-INT-4 (Active Simulation & Exploratory Learning Gate)**: In Science and Social Science modules, do core physical, earth, or living systems feature interactive visual exploration (dynamic SVG cutaway/cycle inspector) rather than static textual paragraphs alone?
- [ ] **CP-TITLE-1 (Implicit Grade Scope Gate — Zero "Class 7" Clutter)**:
  Verify that chapter titles, tab labels, breadcrumbs, card headings, and test paper names do NOT redundantly prepend `"Class 7"`. The Class 7 CBSE standard is implicit across Pushti Study Hub; grade numbers may only be stated when explicitly contrasting two different academic standards (e.g. Class 6 prerequisite vs. Class 7 curriculum, or Class 7 vs. Class 8 Olympiad preview).
- [ ] **CP-TEST-1 (Centralized Test & Exam Prep Hub & Standalone Test Architecture Gate)**:
  - Verify that every subject hub (`*_index.html`) features a functional `#tab-tests` on the branch sidebar and a rich `#sec-tests` section with deep-link hash listener (`#tests`).
  - Verify that tests and practice papers are decoupled from chapter interiors and centralized in the subject hub with complete administration metadata (administration date, target exam role, section marks distribution, and original scan links).
  - In standalone test modules (e.g. `practice_hindi_midterm_worksheet.html`):
    - **Tab Location**: Strict SOP Left Dock Rail (`.sidebar` 64px collapsed, 280px pinned with `#pin-btn`, zero peeking) replacing top horizontal tabs.
    - **MCQ Option Compactness**: High-density 4-column responsive grid (`grid-template-columns: repeat(4, 1fr)`) preventing bulky 2-row multi-line wrapping on desktop viewports.
    - **Typography**: Enhanced subject-appropriate fonts (e.g., `Rozha One`, `Yatra One`, `Poppins`, `Outfit`, `Space Mono`).
    - **Initial State**: 100% of solutions hidden by default (`open details = 0`).
    - **Omission of Redundant Grade Prefixes**: Zero `"Class 7"` prefixes across titles, tabs, breadcrumbs, and question cards.

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
| **v3.5** | 2026-09-24 | **The "Hath Fero" Urban Planning & Deterministic Blueprint Protocol (Section 1.11, `.agents/rules/hath_fero.md`, `scripts/maintenance/hath_fero_audit.py`)**: Codified the province-city-street-substreet spatial invariance standard. Mandates strictly identical tab indices across all chapters within a subject province, invariant sub-street sequences (e.g. MCQs, FIB, T/F), isolated chapter color theming, and standardized 'Pending Content' Sentinels (`.pending-content-card`) so missing material is never silently omitted or hallucinated. |
| **v3.4** | 2026-09-20 | **Maximum Horizontal Real-Estate Utilization & Sticky Tier-2 Submodule Nav Standard (Section 2.4.1 & 3.1.2)**: Mandated generous 1600px+ content max-width, responsive multi-column question grids (2-column on desktop/laptop), 2x2 MCQ option layout, and multi-column concept/enrichment grids, eliminating wasteful whitespace voids and reducing vertical page scrolling by ~50% on wide desktop and laptop viewports. Standardized sticky top-docking (`top: var(--header-height); z-index: 900; background: var(--bg-sticky); backdrop-filter: blur(12px)`) for submodule navigation pills (`.submodule-nav`), exam control bars (`.exam-control-bar`), and search bars (`.sticky-search-bar`). |
| **v3.3** | 2026-09-19 | **Centralized Test & Exam Prep Hub Architecture & High-Density Test Standards (Section 4.4, CP-TEST-1)**: Standardized dedicated "#tab-tests" / "#sec-tests" across all 7 subject hubs with deep-link hash listener, decoupling tests from chapter interiors and aggregating them in a centralized subject test bank with complete administration metadata (date given, target 80M exam, syllabus scope, interactive links, original scans); codified strict Left Dock Rail and high-density 4-column single-line MCQ layout for standalone test papers. |
| **v3.2** | 2026-09-18 | **Implicit Grade Scope & Zero "Class 7" Redundancy Standard (Section 1.1, Section 2.10, CP-TITLE-1)**: Codified that because Pushti Study Hub is built exclusively for Pushti in Class 7 CBSE, all grade context is implicit. Prepending or repeating "Class 7" before chapter names, tab headers, breadcrumbs, card headings, and test papers is strictly prohibited unless explicitly contrasting across two different academic standards (e.g. Class 6 prerequisite vs. Class 7 curriculum, or Class 7 vs. Class 8 Olympiad preview). |
| **v3.1** | 2026-09-17 | **Master SOP Unification & Mathematical Typography Standard**: Archived and redirected legacy secondary SOP files (PUSHTI_CONTENT_SOP, PUSHTI_DESIGN_SOP) to ensure zero contradictions; established Section 2.5.2 (Fraction Legibility Mandate with \dfrac and .katex font amplification) and Section 2.5.3 (Adaptive Subparts: Atomic Chips minmax(140px, 1fr) vs. Verbose Grids minmax(280px, 1fr) eliminating orphaned 4th boxes on laptop viewports); added CP-MATH-2. |
| **v3.0** | 2026-09-14 | **Modern Interactive Simulation, Tailwind/Lucide UI & Unified Searchable Solutions Hub Standard**: Authorized Stack B (Tailwind CSS + Lucide Icons) for Science and Social Science; superseded mark-based question splitting with the 5-Module Interactive Simulation & Searchable Solutions Hub Standard (Tab 1 SVG Cutaway Inspector, Tab 2 Cycle Simulator, Tab 3 Searchable NCERT Hub with live debounced search and empty states, Tab 4 Auto-Grading Quiz, Tab 5 3D Flipcards); codified Top Sticky Nav for visual landscape subjects vs. Left Dock Rail for dense math; added CP-GUI-11, CP-GUI-12, and CP-INT-4. |
| **v2.6** | 2026-09-13 | **Strict Textbook Visual & Notation Fidelity Mandate (Section 3.1.3 & CP-GEO-5)**: Mandated absolute fidelity of all geometry figures against official textbook PDFs. Prohibits creative modification of line names, inventing unlabelled vertices, rotating line orientations (vertical vs. horizontal), reversing ray arrows, or altering textbook problem alignments across all geometry modules. |
| **v2.5** | 2026-09-13 | **Two-Tier Navigation Architecture, Dock Rail Zero-Peeking Containment & Complete KaTeX Delimiter Suite**: Codified Section 3.1.2, CP-GUI-9, CP-GUI-10, and CP-TECH-7 establishing the Two-Tier Navigation standard (`.submodule-nav` pills breaking dense sections into short, screen-sized views to eliminate long vertical scrolling), strict collapsed dock rail text isolation (`.tab-label-group` width: 0 / opacity: 0 preventing letter peeking at 62px), and universal KaTeX auto-rendering for all 4 standard delimiters (`$`, `\(`, `$$`, `\[`) with dynamic re-rendering on tab and sub-tab transitions. |
| **v2.4** | 2026-09-13 | **Geometry Chapters Visual Standard (The Native Vector SVG Mandate)**: Codified Section 3.1.1 and Checkpoints CP-GEO-1 to CP-GEO-4 establishing the mandatory standard for all geometry chapters: complete replacement of scanned/pencil-scribbled textbook images with pristine native SVG vector graphics; 100% figure coverage across all illustrations, solved examples, drills, and practice questions; theme-adaptive color tokens; standard geometric symbols (parallel arrows, perpendicular squares, auxiliary dashed constructions); and strict laptop viewport containment. |
| **v2.3** | 2026-09-13 | **Laptop Viewport Compatibility & Solved Examples Derivation Gate**: Established Section 2.5.1 and CP-GUI-8 ensuring full 1280px–1366px laptop compatibility with sidebar pinned/active: mandatory stacked `\begin{aligned}` formatting for all multi-step math in Solved Examples, `minmax(240px, 1fr)` responsive fallbacks, KaTeX display auto-scroll, and zero box overflow on Pushti's laptop screen. |
| **v2.2** | 2026-09-13 | **Zero-Collision & Text Overwrite Prevention Standard (Universal Math & Layout Containment)**: Added Section 2.5, CP-GUI-7, and CP-TECH-6 establishing mandatory rules to prevent matter from crossing over and overwriting cards: atomic KaTeX math lists, `\begin{aligned}` multi-step math, universal `min-width: 0` / `overflow: hidden` card containment, and `minmax(280px, 1fr)` grid track minimums. |
| **v2.1** | 2026-09-13 | **Syllabus Topic Tag Mapping & Completeness Standard (Topic-to-Battery Rule)**: Standardized that chapter card tags/tabs must directly reflect syllabus-prescribed topics, highlighted tags signify covered topics, dim tags indicate pending syllabus items, and the ratio directly determines the completeness percentage. |
| **v2.0** | 2026-09-13 | **Master Unified SOP Consolidation**: Consolidated all separate design, operational, content, and GITA guidelines into a single authoritative master reference with subject-wise architectures and 4 comprehensive QA checkpoint suites. |
| **v1.4** | 2026-09-13 | Mathematics Theme & GUI unification (Zero White Patches universal button reset, desktop margin push, floating jump-to-top). |
| **v1.3** | 2026-09-13 | Collapsible vertical dock rail (1.2s delay), submodule partitioning, subparts grid, and syllabus batteries. |
| **v1.2** | 2026-09-12 | Exam Pattern Pop-up Modal, 3×2 balanced grid, and timetable synchronization. |
| **v1.1** | 2026-09-08 | Design SOP creation with KaTeX and CSS custom properties for notes pages. |
| **v1.0** | 2026-09-02 | Initial operational checklist and early GITA 5-Tab rules. |
