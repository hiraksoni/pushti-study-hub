# Standard Operating Procedure (SOP): Web Content Verification

**Purpose:** This SOP must be executed automatically at the end of creating any chapter, page, or artifact, or whenever the user requests a "verification" of the work.

## 1. DOM Duplication & Bloat Check
- **Rule:** No content element (NCERT item, practice question, simulator, figure) may exist more than once in the HTML DOM.
- **Action:** 
  - Search the code for duplicate container patterns (e.g., `<div id="xxx-all">` containing copies of individual sections).
  - Ensure "View All" functionality is implemented via JavaScript toggling multiple existing panes (e.g., `pane.classList.add('active')`), rather than rendering a separate monolithic container.

## 2. Scrollbar Elimination & Smart Tabbing (Tier-2 Nav)
- **Rule:** Long vertical scrollbars are prohibited.
- **Action:**
  - Verify that any tab containing multiple distinct sections (like multiple exercises, theory parts, or simulators) uses a horizontal Submodule Nav pill bar.
  - Verify that the `switchSubTab(subId, btn)` JavaScript function correctly hides inactive panes and shows the target pane using `display: none` and `display: block`.

## 3. HTML Tag Balance & Scope Integrity
- **Rule:** No unclosed `<div>` tags that cause content to leak across tabs.
- **Action:** 
  - Never use naive string slicing (`text.split('</div>')`) for extraction. Always use a depth-tracking DOM stack algorithm (counting `+1` for `<div`, `-1` for `</div`).
  - Run a Div-Balance audit script to verify that every `<div class="tab-panel">` is perfectly closed before the next one begins.

## 4. Content Completeness Audit
- **Rule:** Zero data loss during transformations or rebuilds.
- **Action:**
  - Write a short Python verification script tailored to the chapter to count specific markers (e.g., `Item 2.1` to `Item 2.14`, Practice Questions `1` to `80`).
  - Assert that the final output file contains the exact same number of items, questions, and interactive simulators as the baseline requirements.

## 5. Pure Vanilla JS & Strict Encoding
- **Rule:** No frameworks, no encoding corruption.
- **Action:**
  - Confirm the absence of React, Vue, or Angular dependencies. KaTeX and FontAwesome are permitted.
  - Ensure the file is written strictly in **UTF-8** encoding. 
  - *Warning:* Never use PowerShell `>` or `>>` operators to pipe HTML output, as Windows defaults to UTF-16, which corrupts the rendering. Always use Python's `open(file, 'w', encoding='utf-8')`.

## 6. Layout & Z-Index Offset Verification
- **Rule:** Sticky headers and navigation bars must not overlap or hide content.
- **Action:**
  - Verify CSS `z-index` layering (e.g., `.controls-toolbar`).
  - Verify that URL Hash jumps (e.g., `#tab-practice`) handle scrolling correctly without permanently permanently pushing navigation out of the viewport.

## 7. Automated Headless Visual Check
- **Rule:** If major structural changes are made, they must be visually confirmed.
- **Action:**
  - Execute a Python `subprocess` using headless Chrome to take screenshots of the modified tabs.
  - Verify visually (or logically via DOM tree depth) that sub-elements are rendering correctly and KaTeX is evaluating.
