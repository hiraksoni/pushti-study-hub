# 🏆 The Holy Grail of App Development

This document serves as the absolute source of truth for all current and future development on Pushti's Study Hub. Any AI agent or developer contributing to this project MUST adhere to these universal statements and acknowledge the historical developments.

## Universal Development Statements (The Golden Rules)

1.  **Strict File Organization**: The root directory must remain pristine. All chapter content files must be placed in their respective `chapters/[subject]/` folders (e.g., `chapters/social_science/`).
2.  **Clean Naming Conventions**: No "gemini-code" gibberish. All files must be named cleanly and descriptively representing their exact content (e.g., `social_science_ch1.html`).
3.  **Firebase Security Injection**: Every new chapter HTML file must include the standard Firebase Injection script block right before the `</body>` tag to ensure remote answer locking and activity logging always works.
4.  **No Extraneous Code Tracking**: Python generator scripts, temporary scratch files, and debug logs (e.g., `*.py`, `firebase-debug.log`) must remain in `.gitignore` and never be committed to the live repository. The repository is strictly for production hosting.
5.  **Always Maintain the Generator**: The `generate_full_sidebar.py` script is the heart of the UI. Whenever new subject structures or folders are added, this script must be updated and re-run to cleanly regenerate `index.html`. Do not manually edit the sidebar in `index.html`.

## Major Developments & Milestones Tracker

*   **Epoch 1 (The Foundation)**: Created the initial Master Dashboard with a responsive, 7-subject sidebar based on the syllabus. Uploaded directly to GitHub Pages for instant web access.
*   **Epoch 2 (The Parent Lock)**: Integrated Firebase Auth and Firestore. Created `parent_dashboard.html` allowing the parent to monitor student activity and globally lock/unlock answer reveal buttons across all chapter files. 
*   **Epoch 3 (The Great Cleanup)**: Purged all messy `gemini-code-*.html` files. Restructured the repository to use clean naming (`social_science_chX.html`) and organized them into dedicated sub-folders (`chapters/social_science/`). Implemented `.gitignore` to prevent clutter.
