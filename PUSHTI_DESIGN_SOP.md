# PUSHTI STUDY HUB — DESIGN SOP v1.0
*Standard Operating Procedure for AI-Assisted Page Generation*

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
| Maths Ch 3 | TBD | `#8b5cf6` violet | `#3b0764` |
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

## 14. CHANGELOG

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-09-08 | Initial SOP created by Antigravity (Claude) |
