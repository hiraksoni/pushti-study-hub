---
name: GITA
description: General Instructions & Thematic Architecture (GITA) for Pushti's Study Hub chapter generation. This rule must be followed strictly when generating all new Science, Maths, and Social Science chapters.
---

# GITA: Unified Chapter Generation Rules
These rules constitute the "Gold Standard" framework for Pushti's Study Hub. They must be adhered to without regression when creating Python generators or HTML files for new chapters (Biology, Chemistry, Physics, etc.).

## 1. Unified Tab Architecture
All chapters must use a top-sticky navigation bar with exactly 5 tabs in a single line:
- **Tab 1: Videos & Map:** Contains YouTube video links for topics (displayed as cards with thumbnails) and a pure CSS Structural Concept Map (do NOT use Mermaid.js charts).
- **Tab 2: OMR (1 Mark):** Contains objective questions (MCQs, Fill in the blanks, True/False) with a toggle switch at the top for "Practice Mode" vs "Test Mode".
- **Tab 3: 2/3 Marks:** Mental flashcard style (use `<details>` and `<summary>`, NO text inputs) for Short Answer questions.
- **Tab 4: 4+ Marks:** Mental flashcard style (NO text inputs) for Long Answer and Case-Based questions. Model answers must be highly detailed and comprehensive. Case studies must inject the full reading passage above the question.
- **Tab 5: Extra Knowledge:** Deep-dive trivia, "Did you know?" facts, and additional context to satisfy curiosity beyond the textbook.

## 2. Dashboard Integration & Theming
- Do not use hardcoded distinct colors (like Sandstone or Maroon) for the main body.
- **CSS Variables:** Use standard CSS custom properties linked to `@media (prefers-color-scheme: dark)` to support System Light/Dark mode dynamically.
- **Palette:** In Light mode, use a White (`#FFFFFF`), Indigo (`#4F46E5`), and Slate theme to blend seamlessly with the main sidebar in `index.html`. In Dark mode, invert to Deep Slate and Blue.
- **Iframe Blending:** Ensure the background `body` color in the iframe matches the container (`var(--bg-main)`) so it does not clash or create visual seams with the `index.html` wrapper.

## 3. OMR System Details
- **Toggle Modes:** Implement Practice Mode (instant visual feedback per question via `onchange` events) and Test Mode (hides questions initially, time-bound countdown timer of 1 min/question, deferred grading with a summary breakdown panel).
- **Explanations:** ALL 1-mark questions (MCQs, Fill in blanks, T/F) MUST have an `exp` (explanation) key injected into their JSON data. When graded (in Practice or Test mode), the feedback box must explain *why* the answer is correct or incorrect.
- **Collapsible Headers:** ALL major section headers (e.g. `<h2>OMR Practice (MCQs)</h2>`) MUST be interactive, collapsible accordions.
- **Dynamic Counts:** Headers must include a live count of questions in that section inside a badge (e.g. `(54)`).
- **Chevron:** The expand/collapse chevron (`svg`) must be prominent (`32x32px`, primary colored circular background, visible on hover).
- **Default State:** All OMR headers and their subsequent Content `<div>` sections MUST start with the `collapsed` CSS class by default on page load.

## 4. Subject-Specific Navigation Mapping
- When updating `generate_full_sidebar.py` (or similar index generators), Science chapters must use isolated IDs: `sci_id: 'science_bio'`, `'science_chem'`, or `'science_phy'`. 
- This prevents overwriting between Biology, Chemistry, and Physics chapters that share the same Chapter Number (e.g., Biology Chapter 2 vs Physics Chapter 2).

## 5. Subjective Formatting
- Never use `<textarea>` or typing inputs for subjective (2, 3, 4+ mark) questions. Pushti studies on a laptop where heavy typing is inconvenient. Use the "Mental Flashcard" approach where the question is presented, she thinks of the answer, and clicks a button to reveal the detailed textbook-quality explanation.
