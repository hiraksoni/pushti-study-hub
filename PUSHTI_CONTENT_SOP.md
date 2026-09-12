# PUSHTI STUDY HUB — CONTENT STRATEGY SOP v1.0
*Companion to PUSHTI_DESIGN_SOP.md — covers WHAT goes into a chapter artifact, sourcing, and AI role division.*

---

## 0. PHILOSOPHY

> "Get knowledge from Claude, get Gemini to do the legwork."
> — Hirak Soni (father & project lead)

**The Goal:** A child (Pushti) must NEVER need to open the textbook.
Everything in the textbook + context + extras must exist in one well-organized page per chapter.
Think: **home-schooling-grade completeness**, not just study notes.

---

## 1. THE TWO-AI WORKFLOW

| Role | AI | Responsibility |
|------|-----|----------------|
| **Concept Master** | Claude | Conceptual explanations, analogies, real-life links, extras, videos, common mistakes |
| **Legwork Engine** | Gemini | Textbook content extraction: solved examples, exercise solutions, organization |
| **Merge Owner** | Claude | Final merge, quality check, single artifact |

### How to Use This Workflow

1. **Gemini first:** Feed Gemini the NCERT PDF/textbook images. Ask it to:
   - Extract ALL solved examples verbatim
   - Solve ALL "Figure It Out" exercises with steps
   - Make MCQs, fill-in-blanks, match-the-following from the chapter
   - Tabulate all properties/formulas
   
2. **Claude next:** Claude provides:
   - Better conceptual explanations than the textbook
   - Mental math tricks and shortcuts
   - Real-life Indian context examples
   - "Beyond NCERT" — what comes next in higher classes
   - Common mistakes children make + corrections
   - Verified video links (YouTube search cards)
   - Puzzles, challenges, brain teasers related to the topic

3. **Claude merges:** Take both outputs, merge into ONE file following PUSHTI_DESIGN_SOP.md.
   - Never duplicate content
   - Claude's concept explanation REPLACES textbook's if it's clearer
   - Gemini's extracted textbook exercises are the GOLD SOURCE for exercise content
   - Flag anything Gemini got wrong (solution errors) and correct them

---

## 2. MANDATORY CONTENT CHECKLIST FOR EVERY CHAPTER

Every chapter artifact MUST contain ALL of these sections:

### §A: CHAPTER NOTES (Concept Section)
- [ ] Chapter overview (2-3 sentences, what the chapter is about)
- [ ] Every concept/subtopic in the chapter — each as its own card
- [ ] For each concept: definition + explanation + worked example + real-life usage
- [ ] All formulas/rules in KaTeX display blocks
- [ ] All properties (with names: commutative, associative, distributive, etc.) with proofs/examples
- [ ] Memory tricks or mnemonics where applicable

### §B: SOLVED EXAMPLES (From Textbook)
- [ ] Every single solved example from the NCERT/Ganita Prakash textbook — verbatim problem, step-by-step solution
- [ ] Each example: collapsible (click to expand), default CLOSED
- [ ] Source label: "From Textbook" badge
- [ ] KaTeX for all math
- [ ] Difficulty badge: Easy / Medium / Hard

### §C: FIGURE IT OUT (Exercises)
- [ ] Every exercise question from every "Figure It Out" section in the chapter
- [ ] Answers hidden by default (reveal on click)
- [ ] Self-assessment buttons after reveal: Got It / Partial / Missed
- [ ] Full step-by-step solution for each (not just final answer)
- [ ] For multi-part questions: show all parts

### §D: EXTRA PRACTICE (Claude / Gemini Generated)
- [ ] At least 5 additional practice problems Claude generates
- [ ] MCQ section: at least 5 questions in 2x2 grid format
- [ ] Fill-in-the-blank: at least 3 questions
- [ ] Match-the-following: at least 1 table
- [ ] Challenge problem (harder than NCERT level)
- [ ] All tagged with [Extra] badge

### §E: CLAUDE EXTRAS (Insight & Enrichment)
- [ ] Mental math tricks and shortcuts for the chapter topic
- [ ] "Why does this rule exist?" explanation (intuition behind rules)
- [ ] Comparison to how other countries/systems teach it (optional but great)
- [ ] Fun puzzle or brain teaser related to the concept
- [ ] Historical fact (who invented this concept?)

### §F: VIDEOS
- [ ] Minimum 4 video cards
- [ ] Cards link to YouTube search URLs (format: `https://www.youtube.com/results?search_query=...`)
- [ ] For confirmed videos: direct YouTube link
- [ ] Each card shows: title, channel (if known), topic tags
- [ ] NEVER embed iframes — linked cards only

### §G: BEYOND TEXTBOOK
- [ ] What comes after this topic in higher classes? (Class 8, 9 preview)
- [ ] Real-world job/career connection ("Where is this math used?")
- [ ] Advanced concept teaser (inverse operations, expression trees, algebra preview, etc.)
- [ ] All tagged [Extra] badge

### §H: COMMON MISTAKES
- [ ] Minimum 5 common errors children make on this topic
- [ ] Each mistake: Wrong approach shown, then Correct approach shown
- [ ] Red/green color coding for wrong/right

---

## 3. CONTENT SOURCING RULES

### 3.1 NCERT / Ganita Prakash Textbook Content
- **Primary source for:** All solved examples, all exercise questions
- **How to get:** Feed textbook PDF pages to Gemini, extract verbatim
- **Class 7 Maths textbook is:** Ganita Prakash (2024 edition) — NOT the old "Mathematics" textbook
- **Exercises are called:** "Figure It Out" — never "Exercise 2.1/2.2"
- **After extraction:** Claude reviews and corrects any errors in Gemini's solutions

### 3.2 Claude-Generated Content
- **Use for:** Concept explanations, analogies, extras, common mistakes, puzzles
- **Do NOT use Claude for:** Claiming to replicate textbook examples (Claude may hallucinate specific numbers — always cross-check with Gemini's textbook extraction)
- **Claude's concept quality > Gemini's concept quality** — always prefer Claude explanations

### 3.3 Video Sourcing
- For confirmed videos: use direct YouTube video ID
- For unconfirmed: use YouTube search URL: `https://www.youtube.com/results?search_query=ganita+prakash+class+7+chapter+2+arithmetic+expressions`
- Preferred channels (in order): Vedantu, Khan Academy India, NCERT Official, MathonGo, Byju's
- NEVER fabricate video links

### 3.4 What NOT to Include
- ❌ Old NCERT textbook content (pre-2024) if newer Ganita Prakash version exists
- ❌ Content from other classes (class 6 or class 8 content mixed in)
- ❌ Solutions from Tiwari Academy / Vedantu if they reference old textbook exercises
- ❌ Unverified "facts" — mark uncertain content as [Needs Verification]

---

## 4. CONTENT QUALITY RULES

### 4.1 Accuracy First
- Every solution must be CORRECT — verify numerically
- Every formula must be expressed in KaTeX (no plain-text math)
- Every property name must be spelled correctly (Commutative, Associative, Distributive, Identity)

### 4.2 Age-Appropriate Language
- Target reader: 12-year-old (Class 7)
- Explanations: simple, not dumbed-down
- Analogies: real-life Indian context (cricket, markets, cooking, money, GST, Diwali, festivals)
- Never use jargon without first explaining it

### 4.3 Self-Sufficiency Test
**Before declaring a chapter page complete, ask:**
> "Can Pushti study this entire chapter for exams WITHOUT opening the textbook?"

If the answer is NO for any reason — find the gap and fill it.

### 4.4 Step Count Rule
- Every solved example: minimum 3 clearly numbered steps
- Every exercise solution: minimum 2 steps (never just "answer = X")
- Multi-step solutions: each step labelled (Step 1, Step 2...)

---

## 5. MERGE PROTOCOL (When Combining Gemini + Claude Output)

When merging Gemini's textbook extraction with Claude's content:

### Step 1: Inventory
- List all sections Gemini has
- List all sections Claude has
- Identify: (a) unique to Gemini, (b) unique to Claude, (c) overlap

### Step 2: Keep Rules
| Content Type | Winner |
|-------------|--------|
| Textbook solved examples | Gemini (verbatim) |
| Textbook exercise solutions | Gemini (verbatim), Claude corrects errors |
| Concept explanations | Claude (clearer language) |
| Real-life examples | Both — use the best, no duplicates |
| Extras/Beyond NCERT | Claude only |
| Common mistakes | Claude only |
| Videos | Claude only (verified) |
| MCQ / practice problems | Gemini base + Claude additions |
| Tables of properties | Gemini structure + Claude language |

### Step 3: Build Order
Always build in this section order (matching SOP §7.2):
1. Notes (concepts)
2. Solved Examples (textbook)
3. Figure It Out (exercises)
4. Extra Practice
5. Claude Extras
6. Videos
7. Beyond Textbook
8. Common Mistakes

### Step 4: Quality Gate
Run ALL 10 CP checks from PUSHTI_DESIGN_SOP.md Section 10 before finalizing.

---

## 6. CHAPTER COLOR MAP

Keep this updated as chapters are built:

| Subject | Chapter | Title (Ganita Prakash) | Color | Status |
|---------|---------|------------------------|-------|--------|
| Maths | Ch 1 | Large Numbers Around Us | `#0284c7` sky | Claude Notes exists |
| Maths | Ch 2 | Arithmetic Expressions | `#10b981` emerald | **Claude Notes + Gemini merge PENDING** |
| Maths | Ch 6 | Number Play (HCF/LCM) | `#f43f5e` rose | Claude Notes exists (HCF file) |
| Maths | Ch 3 | A Peek Beyond the Point | `#8b5cf6` violet | Complete (`maths_ch3_notes.html`) |
| Maths | Ch 4 | TBD | `#f59e0b` amber | Not started |
| Maths | Ch 5 | TBD | `#06b6d4` cyan | Not started |
| English | Ch 1 | The Taste of Watermelon | `#ec4899` pink | Not started |
| English | Ch 2 | TBD | `#f97316` orange | Not started |

---

## 7. FILE NAMING & LINKING

### Final Merged File Per Chapter
One comprehensive file per chapter:
```
source_materials/chapters/maths/maths_ch2_notes.html    ← THE artifact
source_materials/chapters/maths/maths_ch1_notes.html
source_materials/chapters/english/english_ch1_notes.html
```

### Index Linking Rule
- Chapter title in `maths_index.html` is the PRIMARY link → points to `_notes.html`
- Secondary buttons (Gemini, Log) kept as small sober pills
- Once a merged comprehensive file exists, OLD Gemini file becomes secondary

### Archiving Old Files
- Keep old Gemini files at `chapters/maths/maths_ch2.html` (don't delete)
- Keep old Claude files at `source_materials/chapters/maths/claude_maths_ch2.html`
- They serve as reference / fallback
- Do not link them prominently from the index

---

## 8. PUSHTI PROFILE (Always Keep in Mind)

| Field | Detail |
|-------|--------|
| Name | Pushti Soni |
| Class | 7, CBSE |
| Age | ~12 years |
| Father | Hirak Soni |
| Study style | Home-schooled level of depth |
| Learning goal | Complete self-study from the artifact — no textbook needed |
| Preferred depth | Goes beyond NCERT — needs "why" not just "what" |
| Extra motivation | Fun puzzles, real-life context, visual clarity |

---

## 9. AI PROMPT TEMPLATES

### 9.1 Prompting Gemini for Textbook Extraction

```
I'm sharing pages from Ganita Prakash Class 7 Maths Chapter [N] "[Title]".
Please:
1. List every SOLVED EXAMPLE verbatim with full step-by-step solution
2. List every "Figure It Out" question with full step-by-step solution
3. Create a table of all PROPERTIES mentioned (name, rule, example)
4. Create 5 MCQs based on this chapter
5. Create 5 fill-in-the-blank questions
6. Create a match-the-following table

Format each solved example as:
Example [N]: [Problem statement]
Solution:
Step 1: ...
Step 2: ...
Answer: [Final answer]
```

### 9.2 Prompting Claude for Concept Content

```
I'm building a comprehensive study page for Pushti (Class 7, CBSE) for Chapter [N]: [Title]
from Ganita Prakash. Treat this as home-schooling level — she must never need to open the textbook.

Please provide:
1. Clear concept explanations for each subtopic (simpler than textbook, but deeper)
2. Real-life Indian context examples for each rule
3. Mental math tricks and shortcuts
4. "Why does this rule work?" intuition behind each property
5. 3 fun puzzles or challenges
6. 5 common mistakes children make + corrections
7. What comes next in Class 8/9 (Beyond NCERT preview)
8. Historical context (who and when discovered this)
```

### 9.3 Prompting Claude for Final Merge

```
I have Gemini's textbook extraction and my own Claude content for [Chapter].
Rules for the merge:
- Use Gemini's textbook examples verbatim (they're from the actual textbook)
- Use Claude's concept explanations (clearer than textbook)
- Gemini's exercise solutions: include all, correct any errors you spot
- Claude extras section: keep all
- Follow PUSHTI_DESIGN_SOP.md for HTML/CSS/JS
- Single scroll page, 8 sections, KaTeX math, dark-default theme
- Chapter color: [color hex]
```

---

## 10. SELF-CHECK BEFORE FINISHING A CHAPTER PAGE

- [ ] **SC-1 (Completeness):** All 8 sections present (Notes, Examples, Exercises, Extra Practice, Extras, Videos, Beyond, Mistakes)?
- [ ] **SC-2 (Exercises):** Every single "Figure It Out" question is included with full solution?
- [ ] **SC-3 (Textbook examples):** Every NCERT solved example included?
- [ ] **SC-4 (Math rendering):** All math in KaTeX, none in plain text?
- [ ] **SC-5 (Age check):** Can a 12-year-old understand every explanation without external help?
- [ ] **SC-6 (No textbook needed):** If Pushti reads only this page, can she answer ALL textbook questions?
- [ ] **SC-7 (Design SOP):** Run all 10 CP checks from PUSHTI_DESIGN_SOP.md?
- [ ] **SC-8 (Links):** Are all video/resource links valid (or clearly marked as search links)?
- [ ] **SC-9 (Mistakes section):** At least 5 common errors shown?
- [ ] **SC-10 (Beyond NCERT):** Is there something that excites curiosity beyond the syllabus?

---

## 11. CHANGELOG

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-09-09 | Initial content strategy SOP — created by Antigravity (Claude) based on Hirak's vision |
