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

## 4. High-Fidelity Online Cloud Audio Read-Aloud (TTS) Standard

### 4.1 Architecture & Primary Engine (`js/online_tts.js`)
- **Engine**: Pure online cloud audio streaming via Google Cloud Translate Audio API (`https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl={lang}&q={text}`).
- **Strict Prohibition**: Do **NOT** rely on the browser's built-in `window.speechSynthesis` for long text, chapter lessons, or Hindi reading. System SpeechSynthesis stutters, stalls after 15 seconds, and drops sentences due to missing OS voice packages.

### 4.2 Referrer Policy & Local Proxy Protocol
1. **Auto `no-referrer` Injection**: [js/online_tts.js](file:///d:/Users/expor/Downloads/Codes/js/online_tts.js) automatically injects `<meta name="referrer" content="no-referrer">` into `<head>` to prevent Google 404 blocking when hosted on public web servers (e.g. GitHub Pages).
2. **Local Audio Proxy**: When running locally (`localhost` / `127.0.0.1`), audio requests route through the high-speed `/api/tts?tl={lang}&q={text}` endpoint in `https_server.py`, ensuring zero CORS, zero latency, and instant playback.

### 4.3 Intelligent Sentence Chunking & Gapless Pre-Buffering
- **Chunk Threshold**: Texts are divided into natural sentence boundaries (`।`, `.`, `?`, `!`, `,`, `\n`) under 150 characters.
- **Lookahead Preload**: While chunk $i$ is actively playing, chunk $i+1$ is pre-buffered in an HTML5 `<audio>` element with `preload="auto"` so transitions between sentences have **zero delay**.

### 4.4 Selective Speaker Placement Rule
- **Substantive Content Only**: Speaker buttons must be attached **ONLY to substantive explanation paragraphs and concept cards ($\ge 140$ characters)**.
- **Prohibition**: Never spam speaker icons next to single words, labels, table headers, breadcrumbs, badges, or short metadata.
- **Hindi Chapter Specifics**:
  - Individual verse sections: `<button onclick="speakHindiText('', this)">`
  - Vocabulary tables: `<button onclick="speakHindiWord('शब्द', 'अर्थ', this)">`
  - Full chapter recitation: `<button onclick="speakFullLesson(this)">`
- **UI Feedback**: While playing, buttons transform into an animated pulsing stop button:
  `<i class="fas fa-stop text-rose-400 animate-pulse"></i> रोकें`
  Clicking again immediately halts audio playback and resets the button.

---

## 5. Local Server & Environment Automation Standard

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

## 6. Verification Checklist Gate

Every newly created or audited chapter must pass:
- [ ] **CP-GUI-14 (Top-Bar Fullscreen Placement)**: Fullscreen & Landscape button is mounted on the top header; no bottom dock clutter.
- [ ] **CP-GUI-15 (Dock Rail 0.15s Hover & Tab Sequence)**: Sidebar expands in 0.15s; Tab 11 Google Hub sits directly below Tab 10; zero empty vertical void above hero cards.
- [ ] **CP-TTS-1 (Online Cloud Audio Streaming)**: Uses `PushtiOnlineTTS`; chunks sentences cleanly; preloads gaplessly; bypasses OS voice limitations.
- [ ] **CP-TTS-2 (Substantive Placement Gate)**: Speaker buttons exist only on content blocks $\ge 140$ characters (or specific poem/vocab study cards); UI pulses stop button while playing.
- [ ] **CP-THEME-1 (Dual-Theme Token Parity)**: Flawless readability in both Dark (`data-theme="dark"`) and Light (`data-theme="light"`) modes with persistent storage.
