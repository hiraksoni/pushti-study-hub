# Pushti's Master Study Hub 🎓

A centralized, interactive learning dashboard for Pushti to access her study materials, interactive quizzes, and textbook solutions across multiple subjects. 

## Features
*   **Comprehensive Syllabus Sidebar**: Easy navigation mapped precisely to her curriculum across 7 subjects (ICT, Maths, Science, Social Science, English, Hindi, Sanskrit).
*   **Dynamic Interactive Content**: Each chapter contains engaging explanations, visual cues, interactive 4-option MCQs, 2-choice drills, and true/false questions.
*   **Parental Analytics & Access Control**: Secure login system using Firebase Authentication. The `parent@study.com` admin account has exclusive access to a real-time analytics dashboard tracking exactly what chapters are opened and when.
*   **Remote Answer Locking**: The Parent Dashboard features a remote kill-switch that instantly hides or reveals the answer keys and explanations across the entire platform via Firebase Firestore.

## Architecture
*   **Frontend**: Pure HTML/CSS/JavaScript with responsive, multi-line tab wrapping.
*   **Backend / DB**: Google Firebase (Authentication & Firestore).
*   **Hosting**: GitHub Pages.
