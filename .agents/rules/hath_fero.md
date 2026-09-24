---
name: HathFero
description: The Urban Planning & Structural Uniformity Protocol for Pushti Study Hub. Mandates that when 'Hath Fero' is invoked with a scope, the AI performs a comprehensive audit and standardization across chapters in a subject province, ensuring identical tab indices, deterministic sub-street navigation, distinct chapter color theming, and standardized 'Pending Content' sentinels so missing content is never silently dropped or hallucinated.
---

# HATH FERO (હાથ ફેરો) — URBAN PLANNING & STRUCTURAL UNIFORMITY PROTOCOL

When the user invokes the words **"Hath Fero"** (with or without specifying a scope), this rule is triggered immediately.

---

## 1. Core Meaning & Origin
> *"Hath Fero (હાથ ફેરો / હાથ ફેરવવો) means: go and look around with an expert magnifying glass; inspect every minute detail; harmonize, upgrade, and makeover according to the master architecture; and leave an expert signature of excellence."*

In Pushti Study Hub, **Hath Fero** specifically enforces **Spatial and Structural Uniformity** across every learning module.

---

## 2. The Urban Planning Metaphor (Province, City, Street, Sub-street)

To make navigation instinctive so that *"even a doozy kid knows the exact physical coordinates of every piece of learning material"*:

| Urban Planning Metaphor | Study Hub Equivalent | Rule of Uniformity |
| :--- | :--- | :--- |
| **Province** | **Subject** (Maths, Science, English, Hindi, SST, Sanskrit, ICT) | Defines the Master Architectural Blueprint for all its cities. |
| **City / Town** | **Chapter** (e.g. Ch 1, Ch 2, Ch 3...) | Structurally identical city plan. Only the **Color Palette (Accent Theme)** and the **Content** change. |
| **Main Avenues / Roads** | **Primary Navigation Tabs** (Vertical Sidebar or Sticky Horizontal Tabs) | **STRICTLY IDENTICAL INDICES (1 to N)** across every chapter in that subject. |
| **Sub-streets & Blocks** | **Submodules / Sub-pills** within a tab (e.g. Drills: MCQ, FIB, T/F, Match) | **STRICTLY IDENTICAL SUB-PILL SEQUENCE (1 to M)** across every chapter in that subject. |

---

## 3. Province Blueprints (Mandatory Street Plans)

### 3.1 Science Province Blueprint (Sticky Horizontal 5-Tab Architecture)
Every Science chapter (`chapters/science/science_*.html`) MUST have these exact 5 tabs in this exact sequence:
- **Tab 1 (`tab-notes` / `tab-theory`)**: **Core Theory & Illustrated Concepts** (Visual diagrams, laws, definitions).
- **Tab 2 (`tab-solved` / `tab-textbook`)**: **Textbook Q&A & Model Explanations** (NCERT / Main coursebook exercises).
- **Tab 3 (`tab-practice`)**: **Interactive Objective Drills** containing the 4 sub-streets in fixed order:
  - Sub-street 3.1: **MCQs**
  - Sub-street 3.2: **Fill in the Blanks (FIB)**
  - Sub-street 3.3: **True / False (T/F)**
  - Sub-street 3.4: **Match the Following / One-Word**
- **Tab 4 (`tab-traps` / `tab-hots`)**: **Exam Traps, Traps Analysis & Olympiad HOTS**.
- **Tab 5 (`tab-summary` / `tab-mindmap`)**: **Mind Map, Concept Tree & Flashcard Revision**.

---

### 3.2 Mathematics Province Blueprint (Vertical Sticky Sidebar Architecture)
Every Mathematics chapter (`chapters/maths/maths_*.html`) MUST maintain these exact tabs in sequence:
- **Tab 1 (`tab-concepts`)**: **Concepts & Core Definitions** (Number theory, theorems, rules).
- **Tab 2 (`tab-solved`)**: **Solved Examples & Step-by-Step Models** (Dual-method solvers, step breakdown).
- **Tab 3 (`tab-exercises`)**: **Coursebook & Reference Exercises** (All textbook problems 100% keyed).
- **Tab 4 (`tab-practice`)**: **Practice & Objective Drills** in fixed sub-pill order:
  - Sub-street 4.1: **Mental Math & Rapid Drills**
  - Sub-street 4.2: **OMR / Objective MCQs**
  - Sub-street 4.3: **Assertion & Reasoning / Traps**
- **Tab 5 (`tab-simulators` / `tab-lab`)**: **Interactive Laboratory & Simulators** (Dynamic HTML5/Canvas/DOM interactive tools or School Test Paper).
- **Tab 6 (`tab-mindmap`)**: **Summary, Mind Map & Formula Reference**.

---

### 3.3 English & Hindi Literature Province Blueprint
Every Literature chapter (`chapters/english/lit_*.html`, `chapters/hindi/hindi_*.html`) MUST maintain:
- **Tab 1 (`tab-prose` / `tab-poem` / `tab-text`)**: **Complete Original Text with Stanza/Paragraph Line-by-Line Paraphrase & Hindi/English Meaning**.
- **Tab 2 (`tab-vocab` / `tab-shabdarth`)**: **Glossary, Word Meanings & Antonyms/Synonyms**.
- **Tab 3 (`tab-qa`)**: **Textbook Q&A** (Extract Based / RTC, Short Answer, Long Answer, Character Sketches).
- **Tab 4 (`tab-practice`)**: **Objective Drills** in fixed sub-pill order:
  - Sub-street 4.1: **MCQs**
  - Sub-street 4.2: **Fill in the Blanks (FIB)**
  - Sub-street 4.3: **True / False (T/F)**
- **Tab 5 (`tab-grammar`)**: **Integrated Chapter Grammar & Creative Writing Drills**.
- **Tab 6 (`tab-mindmap`)**: **Mind Map, Theme Analysis & Author Profile**.

---

## 4. The Zero-Hallucination & "Pending Content" Sentinel

### Absolute Structural Invariance
Under NO circumstance may an AI assistant drop a tab, hide a sub-street, or shift tab numbering just because content for that specific section is not yet available in the knowledge base or notes!

### The Sentinel Standard
If a section or sub-street is currently missing content, render the **Standardized Pending Sentinel**:

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

**Benefits**:
1. **Zero Muscle-Memory Drift**: Tab 3 is ALWAYS Tab 3. Tab 4.2 is ALWAYS Fill in the Blanks.
2. **Instant Visual Auditing**: Parents and admins immediately spot what is missing with zero guesswork.
3. **Zero AI Hallucination**: AI assistants do not invent phantom questions or misplace components.

---

## 5. Chapter Color Theming Standard

While the **structure (streets)** remains strictly identical:
- Each chapter MUST have its own **unique primary accent color** defined via CSS custom properties on `:root` or the chapter wrapper:
  - Chapter 1: Indigo / Violet (`#6366F1`)
  - Chapter 2: Emerald Green (`#10B981`)
  - Chapter 3: Amber / Gold (`#F59E0B`)
  - Chapter 4: Sky Blue (`#0EA5E9`)
  - Chapter 5: Rose / Crimson (`#F43F5E`)
  - Chapter 6: Purple (`#8B5CF6`)
  - Chapter 7: Cyan / Teal (`#06B6D4`)
  - Chapter 8: Orange (`#F97316`)
- Tab button active states, badge highlights, and question counters automatically adopt this chapter accent color while keeping the exact same physical coordinates.

---

## 6. Hath Fero Execution Checklist

When the user says **"Hath Fero [scope]"**, execute the following 7-step pass:
1. **Identify the Province**: Determine the subject and its mandatory blueprint.
2. **Inspect Main Avenues**: Verify all N tabs exist in exact sequence with correct IDs and titles.
3. **Inspect Sub-Streets**: Verify all M submodules/pills exist in exact order inside Drills and Exercises.
4. **Plant Sentinels**: If any street is empty, insert the Standard Pending Sentinel. Never silently delete or compress tabs.
5. **Verify Color Isolation**: Ensure the chapter uses its distinct color theme consistently without breaking dark/light mode standards.
6. **Check Relative Paths & Anonymization**: Verify `../../index.html`, zero publisher names (use `Main`, `Ref 1`, etc.), and zero school names.
7. **Sign Off**: State the audit results clearly and leave the Hath Fero verification stamp.
