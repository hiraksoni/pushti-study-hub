---
name: GUIThemeTTSStandards
description: Mandatory standards for UI layout, Dual-Theme styling, Top-Bar tooling, Collapsible Dock Rail geometry, and High-Fidelity Online Cloud Audio Read-Aloud (TTS) capability across all HTML artifacts and chapters in Pushti Study Hub.
---

# PUSHTI STUDY HUB — GUI, THEME & ONLINE TTS MASTER STANDARD

This rulebook defines the authoritative visual, structural, and audio synthesis standards across all learning modules, chapter artifacts, and subject portals in Pushti Study Hub. Every newly created or refactored page must strictly adhere to these specifications.

---

## 1. GUI & Header Top-Bar Architecture

### 1.1 Sticky Header Geometry (54px Fixed Height)
Every chapter module must feature a clean, sticky top header (`h-[54px]` / `height: 54px; sticky top: 0; z-index: 1000;`) housing standard navigation controls:
```html
<header class="h-[54px] sticky top-0 z-50 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 flex items-center justify-between px-4 sm:px-6">
  <!-- Left: Subject & Chapter Breadcrumb (Zero 'Class 7' redundancy) -->
  <div class="flex items-center gap-2">
    <a href="../../index.html" class="flex items-center gap-2 text-slate-300 hover:text-white font-semibold text-sm">
      <i class="fas fa-home text-amber-400"></i>
      <span>Pushti Study Hub</span>
    </a>
    <span class="text-slate-600">/</span>
    <span class="text-xs font-medium text-amber-400 font-mono">Chapter Title</span>
  </div>

  <!-- Right: Tooling Suite -->
  <div class="flex items-center gap-2 sm:gap-3">
    <!-- 1. Search Button / Modal Trigger -->
    <button id="globalSearchBtn" onclick="toggleGlobalSearch()" class="p-2 rounded-lg bg-slate-800/80 hover:bg-slate-700 border border-slate-700 text-slate-300 hover:text-white">...</button>
    <!-- 2. Dual-Theme Toggle -->
    <button onclick="toggleTheme()" class="p-2 rounded-lg bg-slate-800/80 hover:bg-slate-700 border border-slate-700 text-slate-300 hover:text-white">...</button>
    <!-- 3. Top-Bar Fullscreen & Landscape Button -->
    <button id="pushti-topbar-fs-btn" onclick="toggleFullscreenLandscape()" class="pushti-topbar-fs-btn">
      <i class="fas fa-expand"></i> <span>Fullscreen</span>
    </button>
    <!-- 4. Schedule & Readiness Pills -->
    <a href="../../timetable.html" class="hidden sm:inline-flex ...">📅 Time Table</a>
    <a href="../../midterm.html" class="hidden md:inline-flex ...">🎯 Mid-Term Syllabus</a>
  </div>
</header>
```

### 1.2 Fullscreen & Landscape Engine Placement
- **Location**: Top header bar, adjacent to the Theme Toggle and Time Table pill.
- **Strict Prohibition**: Never place the fullscreen button at the bottom of the viewport or inside floating bottom docks.
- **Tablet / Laptop Auto-Lock**: On devices supporting the Screen Orientation API, invoking Fullscreen attempts `screen.orientation.lock('landscape')` to ensure wide math/science readability.
- **Quick Recap Button Status**: Simple / placeholder "quick recap" buttons are **strictly halted** until a comprehensive, pedagogical micro-recap engine is engineered.

---

## 2. Collapsible Vertical Dock Rail Standard

### 2.1 Spatial Dimensions & Hover Dynamics
- **Width**: `62px` collapsed (showing clean icon column), expanding to `280px` on hover or when pinned.
- **Universal Snappy Hover Delay**: The hover expansion transition must be set to snappy **`0.15s`** (`transition: width 0.15s cubic-bezier(0.16, 1, 0.3, 1)`). Sluggish delays (e.g. 1.0s or 1.2s) are strictly prohibited across all subject hubs.
- **Pinned State**: When pinned (`sidebar.pinned`), it persists in `localStorage` and applies a margin push (`.sidebar.pinned ~ .main-app-content { margin-left: 280px; }`) ensuring zero sidebar overlap over reading material.

### 2.2 Strict Tab Button Nesting & Google Hub Sequence
- All navigation tab buttons (Tabs 1 to 10 + Tab 11 Google Hub) must be nested **inside** the top button container:
  `<div class="flex flex-col gap-1.5 p-2">`
- **Tab 11 (Google Knowledge & Video Hub)** must sit **contiguously immediately beneath Tab 10**, NOT isolated or pushed to the bottom of the screen.
- **Dock Footer**: Only the Pin Toggle button (`#pinToggleBtn`) resides inside the bottom `.sidebar-footer`.
- **Zero Top-Void / Div Balance Rule**: Div open and close tags inside `<aside>` must balance with 100% precision (35 open / 35 close). Leaking elements or premature closing tags that push `<main>` downward causing large blank black spaces are strictly prohibited.

---

## 3. Dual-Theme Standard (Dark / Light Parity)

- **Default Theme**: Dark Mode (`<html lang="en" class="dark" data-theme="dark">`).
- **Overrides**: `[data-theme="light"]` defines high-contrast light mode styling.
- **State Persistence**: Persisted in `localStorage.getItem('pushti-theme')` or `'psh_theme'`.
- **Cross-Window Sync**: Emits `window.parent.postMessage({ theme: newTheme }, '*')` so iframes and dashboards synchronize seamlessly.
- **Zero Unstyled Elements**: All buttons, cards, and inputs must use theme tokens:
  - Dark surfaces: `bg-slate-900`, `bg-slate-950`, border `border-slate-800`.
  - Light surfaces: `bg-white`, `bg-slate-50`, border `border-slate-200`.

---

## 4. High-Fidelity Natural Female Audio Read-Aloud (TTS) Standard (v4.0)

### 4.1 Architecture & Voice Priority Hierarchy (`js/online_tts.js`)
- **Melodious Female Voice Priority**: To ensure pleasant, natural, and engaging listening for Pushti without robotic fatigue (avoiding harsh or robotic male voices), the audio engine dynamically discovers, prioritizes, and locks onto high-fidelity **Female Hindi Voices**:
  1. `Microsoft Swara Online (Natural) - Hindi (India)` (Edge / Windows 11)
  2. `Microsoft Kalpana - Hindi (India)`
  3. `Google हिन्दी` (Android / Chrome Natural Female)
  4. `Lekha` (macOS / iOS)
- **State Machine with Real Play / Pause / Resume**:
  - Full playback controls: 1-click **Play**, **Pause**, **Resume**, and **Stop**.
  - Persistent Floating Player Widget: Stays pinned at bottom-right during active reading, showing real-time sentence progress (`वाक्य ३ / १८`) and `👩 महिला स्वर` active badge.
- **Continuous Multi-Sentence Queue & 14s Android Watchdog**:
  - Long prose and poems are tokenized into natural sentence boundaries (`।`, `.`, `?`, `!`, `,`, `\n`).
  - Includes a proactive **14-second watchdog timer** that refreshes speech synthesis utterances to prevent the notorious Chromium/Android freeze bug on long passages.
- **Graceful Cloud Fallback**: If a client device lacks high-quality neural female voices, the engine automatically falls back to online cloud streaming via the local proxy `/api/tts?tl=hi&q=...` or Google TTS (`https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=hi&q=...`).

### 4.2 Selective Speaker Placement Rule
- **Substantive Content Only**: Speaker buttons must be attached **ONLY to substantive explanation paragraphs, poems, and concept cards ($\ge 140$ characters)**.
- **Prohibition**: Never spam speaker icons next to single words, labels, table headers, breadcrumbs, badges, or short metadata.
- **Hindi Chapter Specifics**:
  - Individual verse/paragraph sections: `<button onclick="speakHindiText('', this)">`
  - Vocabulary tables: `<button onclick="speakHindiWord('शब्द', 'अर्थ', this)">`
  - Full chapter continuous recitation: `<button onclick="speakFullLesson(this)">`
- **UI Feedback**: While playing, buttons transform into an animated pulsing stop button:
  `<i class="fas fa-stop text-rose-400 animate-pulse"></i> रोकें`
  Clicking again immediately halts audio playback and resets the button.

---

## 5. Bilingual Language Learning & English Equivalent Naming Standard

Because Pushti studies in an **English-medium CBSE curriculum**, language subjects (Hindi & Sanskrit) must provide clear bilingual scaffolding to ensure 100% comprehension:

### 5.1 English Equivalent Chapter Naming
- In all chapter `<title>`, main hero `<h1>`, breadcrumbs, sidebar dock tooltips, and subject portal cards (`hindi_index.html`), every Hindi chapter title must include its clear English translation / transliterated equivalent in parentheses:
  - Example: `Chapter 1: हमको मन की शक्ति देना (Humko Man Ki Shakti Dena — Prayer for Mental Strength)`
  - Example: `Chapter 1: भाषा, लिपि और व्याकरण (Language, Script & Grammar)`
  - Example: `Chapter 6: समास (Compound Words — Samas)`

### 5.2 Dynamic Bilingual Scaffolding (`js/bilingual_helper.js`)
- **Header Toggle Button**: Every language module must include a prominent `#btn-en-toggle` button in the top bar:
  `<button id="btn-en-toggle" onclick="toggleEnglishHints()" ...>🔤 EN Hints / अर्थ</button>`
- **Inline English Hints (`.en-hint`)**: Subtle contextual translations embedded alongside difficult literary Hindi terms, hidden by default and smoothly toggled via CSS `.show-en-hints .en-hint { display: inline-block !important; }`.
- **Dotted Term Glosses (`.term-gloss`)**: Key literary, grammatical, and cultural terms feature a subtle dotted cyan underline with instant hover tooltip definition (`title="..."`).

---

## 6. Local Server & Environment Automation Standard

- **Dual-Protocol Server (`https_server.py`)**:
  - Simultaneously serves HTTPS on port `8443` (`https://localhost:8443/`) and zero-warning HTTP on port `8000` (`http://localhost:8000/`) using multi-threaded `ThreadingHTTPServer`.
  - Built-in `/api/tts` proxy for instant audio streaming.
  - Automatic SSL dev certificate generation via `werkzeug`.
- **Windows UTF-8 Encoding**: `https_server.py` reconfigures `sys.stdout` and `sys.stderr` to `UTF-8` on launch to prevent Windows `cp1252` encoding crashes on Hindi Devanagari text.
- **Requirements Automation**: All Python dependencies are codified in [requirements.txt](file:///d:/Users/expor/Downloads/Codes/requirements.txt) (`werkzeug`, `cryptography`, `beautifulsoup4`, `websocket-client`).
- **One-Click Launchers**:
  - [launch_hindi_chapters.bat](file:///d:/Users/expor/Downloads/Codes/launch_hindi_chapters.bat) (Auto-starts server & opens browser)
  - [start_servers.bat](file:///d:/Users/expor/Downloads/Codes/start_servers.bat) (Auto-checks pip dependencies & launches server)
  - [start_background_server.vbs](file:///d:/Users/expor/Downloads/Codes/start_background_server.vbs) (Runs server silently in background)
  - [stop_server.bat](file:///d:/Users/expor/Downloads/Codes/stop_server.bat) (Stops background server)

---

## 7. Target Hardware Specification: Samsung Galaxy Tab A8 (SM-X205) & 15.6" Laptop Protocol

Pushti's primary study devices consist of two distinct environments that must be rigorously verified during all QA runs:

### 7.1 Samsung Galaxy Tab A8 (Model SM-X205 — LTE/Wi-Fi)
- **Physical Specifications**: 10.5-inch TFT LCD, $1920 \times 1200$ physical resolution (16:10 aspect ratio, ~216 ppi), running Android One UI with Google Chrome for Android and Samsung Internet.
- **Display Viewport Dynamics (Default DPR ~1.875)**:
  - **Landscape Mode ($1024 \times 640$ CSS Viewport)**:
    - 62px collapsed vertical dock rail fixed on the left edge.
    - The main content area (`.main-app-content` / `.main-content`) **MUST enforce**:
      ```css
      @media (min-width: 640px) and (max-width: 1099px) {
        .main-app-content, .main-content {
          margin-left: 62px !important;
          width: calc(100% - 62px) !important;
          max-width: min(1600px, calc(100vw - 62px)) !important;
          padding-left: 1.5rem !important;
          padding-right: 1.5rem !important;
        }
      }
      ```
    - Strictly prevents the fixed sidebar from overlapping, touching, or obscuring chapter titles, paragraphs, or equations.
  - **Portrait Mode ($640 \times 1024$ / $800 \times 1280$ CSS Viewport)**:
    - 62px dock rail in compact icon-only mode (`.tab-label-group { display: none !important; }`).
    - Content takes remaining width: `width: calc(100% - 62px) !important; margin-left: 62px !important;`.
    - **Disallowance of 280px Pinned Dock on Tablets**: On screen widths $< 1100px$, sidebar pinning to 280px is strictly forbidden (`width: 62px !important;`). The pin toggle button (`.sidebar-footer`, `.pin-btn`) is hidden via `@media (max-width: 1099px)` to prevent accidental viewport crushing.
    - Hero banner flex layouts use `lg:flex-row` (staying `flex-col` below 1024px) so headings (`h1`) span 100% of the available width without squashing into narrow 4-line columns, with action badges and continuous audio play buttons wrapping gracefully beneath.
- **Touch Parameters**: All tap targets (tabs, speaker buttons, flashcards, MCQ cards, option tiles) must maintain $\ge 44\text{px} \times 44\text{px}$ touch envelopes with `-webkit-tap-highlight-color: transparent;` and smooth momentum touch scrolling (`-webkit-overflow-scrolling: touch;`).

### 7.2 15.6" Windows 11 Laptop
- $1366 \times 768$ (Native Laptop) or $1920 \times 1080$ (Full HD at 125% scaling = $1536 \times 864$).
- Supports snappy 0.15s hover expansion of the 62px dock rail to 280px, and user-initiated dock pinning with automatic 280px margin push (`.sidebar-dock.pinned ~ .main-app-content { margin-left: 280px !important; }`).

---

## 8. Verification Checklist Gate

Every newly created or audited chapter must pass:
- [ ] **CP-GUI-14 (Top-Bar Fullscreen Placement)**: Fullscreen & Landscape button is mounted on the top header; no bottom dock clutter.
- [ ] **CP-GUI-15 (Dock Rail 0.15s Hover & Tab Sequence)**: Sidebar expands in 0.15s; Tab 11 Google Hub sits directly below Tab 10; zero empty vertical void above hero cards.
- [ ] **CP-GUI-16 (Samsung Galaxy Tab A8 SM-X205 Dual-Orientation Gate)**:
  - Landscape (1024×640): 62px dock rail cleared via `margin-left: 62px !important; width: calc(100% - 62px) !important;`; zero title or card overlap.
  - Portrait (640×1024 / 800×1280): 62px dock rail capped (no 280px pin); hero banner uses `lg:flex-row` so title spans 100% width; badges wrap cleanly beneath.
  - Touch targets $\ge 44\text{px} \times 44\text{px}$ with `-webkit-tap-highlight-color: transparent;`.
- [ ] **CP-TTS-1 (Natural Female Voice Priority)**: Uses `js/online_tts.js` v4.0; locks onto sweet, natural female voices (`Microsoft Swara`, `Kalpana`, `Google हिन्दी`, `Lekha`); includes 14s watchdog timer; fallbacks to cloud proxy.
- [ ] **CP-TTS-2 (Play/Pause/Resume & Floating Player)**: State machine allows 1-click play, pause, and resume; floating widget displays sentence counter (`वाक्य x / y`).
- [ ] **CP-TTS-3 (Substantive Placement Gate)**: Speaker buttons exist only on content blocks $\ge 140$ characters (or specific poem/vocab study cards); UI pulses stop button while playing.
- [ ] **CP-LANG-1 (Bilingual English Equivalents & Hints)**: Chapter titles display English equivalents in parentheses; `#btn-en-toggle` enables/disables inline `.en-hint` translations.
- [ ] **CP-THEME-1 (Dual-Theme Token Parity)**: Flawless readability in both Dark (`data-theme="dark"`) and Light (`data-theme="light"`) modes with persistent storage.

