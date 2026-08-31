# GITA Framework Requirements & Standards

This document outlines the finalized requirements for the GITA (Generate, Integrate, Test, and Align) architecture used across all chapter files in Pushti's Study Hub. It incorporates all lessons learned from the "Great Cleanup" of August 2026. Any AI agent or developer modifying chapter content MUST adhere to these rules.

## 1. Architectural Layout (The 5-Tab Blue Framework)
The experimental "Brutalist / Road to 20/20" architecture (hardcoded HTML questions, custom text notes, heavy CSS) is **officially rejected**. 
Every single chapter (Science, Social Science, Maths, ICT) must follow the unified **5-Tab JavaScript Framework**:
*   **Tab 1: Videos & Map:** No heavy textbook notes! This tab strictly contains unique, chapter-specific YouTube links and a concept map.
*   **Tab 2: OMR (1 Mark):** Contains the auto-grading arrays: mcqBook, illBook, 	fBook.
*   **Tab 3: 2/3 Marks:** Contains subjective Q&A populated by the shortBook JS array.
*   **Tab 4: 4+ Marks:** Contains detailed subjective Q&A populated by the longBook JS array.
*   **Tab 5: Extra Knowledge:** Contains trivia populated by the extraBook JS array.

## 2. Content Generation Rules
*   **Video Duplication:** Never hardcode generic video IDs (e.g., repeating Chapter 1 videos in Chapter 6). Videos must be uniquely scraped from YouTube for the specific chapter topic.
*   **Subjective Sorting:** When extracting "Textbook Solutions", they must be intelligently split:
    *   Answers > 40 words OR questions starting with "Explain", "Describe", or "Differentiate" go to the **4+ Marks** (longBook) section.
    *   All other questions go to the **2/3 Marks** (shortBook) section.
*   **Extra Knowledge Format:** Trivia in the extraBook array must *always* prefix the question with "Did you know? " (e.g., "Did you know? The Lion Capital").

## 3. Strict Encoding Rules (Preventing ?? Corruption)
*   **NEVER** use PowerShell echo, Set-Content, or standard output redirection (>) to modify HTML or Python files in this repository. Windows PowerShell defaults to Windows-1252 encoding, which will permanently corrupt emojis (🚀, ✨) into ?? or dY"s.
*   **ALWAYS** use a Python script with open(filepath, 'w', encoding='utf-8') to read, modify, and write files.

## 4. Dark Mode Compliance
*   Never use hardcoded hex colors (#FFFFFF, #FAFAFA) for backgrounds or text in UI components (like the Sidebar or Dashboard). 
*   Always use the designated CSS variables (ar(--bg-color), ar(--surface), ar(--text-main)) so that the Dark Mode toggle works seamlessly across the entire iframe and sidebar.

## 5. Sidebar Routing State
*   The Subject cards in index.html must write to localStorage.setItem('open-subject', '[Subject Name]').
*   The dashboard.html sidebar automatically reads this key to expand the correct accordion menu upon loading. Maintain this exact routing logic when adding new subjects.

## Data Extraction Fidelity
**CRITICAL REQUIREMENT FOR ALL SUBJECTS:** When extracting questions from source materials (PDFs, images), you MUST maintain an exact 1:1 tally. 
- **DO NOT SKIP ANY QUESTIONS.** 
- If a chapter has 90 MCQs, you must extract all 90.
- Wherever questions contain descriptions, diagrams, or additional context, include them IN FULL ALWAYS.
- Do not summarize or truncate questions to save tokens. If necessary, batch process the extraction to ensure 100% fidelity.
