---
name: TopicSearchQueries
description: Mandatory rule prohibiting hardcoded video URLs (e.g. YouTube iframes/links) and specific channel branding across all Pushti Study Hub chapters. Mandates the generation of topic-wise dynamic search strings for Google Video and Google Web Knowledge queries, preserving token budget and preventing bit-rot.
---

# Topic Search Queries & Anti-Rot Video Protocol

This rule governs how external video explanations, multimedia demonstrations, and extended study references are provided across all chapters and subjects in Pushti Study Hub.

---

## 1. Core Mandate: Zero Hardcoded Video URLs & Channel Branding

### Strict Prohibitions:
1. **No Direct Video Links**: Never embed or link to specific third-party video URLs (e.g., `youtube.com/watch?v=...`, `youtu.be/...`, Vimeo, or third-party MP4s).
2. **No Video Iframes**: Never use `<iframe>` video players or embedded video widgets in any chapter module.
3. **Zero Channel / Creator Branding**: Never mention specific YouTube channels, coaching institutes, or online tutors (e.g. Vedantu, PhysicsWallah, Khan Academy, LearnFatafat, Magnet Brains) on student-facing UI.

### Why This Rule Exists:
* **Anti-Rot (Zero Broken Links)**: Direct video links break, get taken down, set to private, or region-restricted over time.
* **Token Conservation**: Eliminates wasting AI tokens fetching, inspecting, and verifying video links or video transcript contents.
* **Search Engine Delegation**: Google's search algorithms are vastly superior at dynamically indexing and ranking the freshest, highest-rated, and most age-appropriate educational videos.
* **Pure Academic Focus**: Protects the student from commercial platform distractions, promotional intros, and third-party advertising endorsements.

---

## 2. Mandatory Replacement: Dynamic Search Strings & Action Links

For every key topic, conceptual unit, or practical exercise requiring visual or extended reference, chapters must provide **Topic Search & Knowledge Exploration Cards**:

Each card must contain:
1. **Curated Topic Header & Description**: Clean summary of the concept to explore.
2. **Transparent Query String**: The exact recommended search query displayed visibly in a styled `<code>` block with 1-click copy capability so the student learns effective query construction.
3. **Google Video Search Action Button**: Direct link targeting Google Video Search:
   ```text
   https://www.google.com/search?tbm=vid&q=[URL_ENCODED_QUERY]
   ```
4. **Google Web Knowledge Action Button**: Direct link targeting Google Web Search for articles, simulations, and notes:
   ```text
   https://www.google.com/search?q=[URL_ENCODED_QUERY]
   ```

---

## 3. Query Engineering Formulas

To maximize search relevance and guarantee high-yield academic results, all queries must follow these standardized prompt formulas:

### A. Video Search Formula:
```text
Class 7 [Subject] "[Exact Topic/Law/Organ/Reaction]" animated explanation visual experiment
```
*Examples:*
* `Class 7 Science "Neutralisation reaction in everyday life" animated explanation experiment`
* `Class 7 Science "Human heart double circulation" 3D animated working explanation`
* `Class 7 ICT "Excel create charts column bar line" step by step tutorial`

### B. Knowledge & Practice Formula:
```text
Class 7 [Subject] "[Exact Topic/Law/Organ/Reaction]" notes summary practice questions
```
*Examples:*
* `Class 7 Science "Indicators litmus turmeric china rose" color changes table notes`
* `Class 7 Mathematics "Angle sum property of triangle" solved proof examples`
* `Class 7 ICT "Excel sort filter multiple criteria" notes examples`

---

## 4. Standardized HTML Component (`.topic-search-card`)

```html
<div class="topic-search-card">
  <div class="topic-search-header">
    <span class="topic-badge"><i class="fas fa-search"></i> Topic 1</span>
    <h4 class="topic-title">Neutralisation in Everyday Life (Soil, Ant Stings & Indigestion)</h4>
  </div>
  <p class="topic-desc">Explore animated chemical reactions, visual laboratory demonstrations, and everyday real-world applications.</p>
  
  <div class="topic-query-box">
    <span class="query-label"><i class="fas fa-terminal"></i> Recommended Search:</span>
    <code class="query-code">Class 7 Science "Neutralisation reaction in everyday life" animated explanation experiment</code>
  </div>

  <div class="topic-search-actions">
    <a href="https://www.google.com/search?tbm=vid&q=Class+7+Science+%22Neutralisation+reaction+in+everyday+life%22+animated+explanation+experiment" 
       target="_blank" rel="noopener noreferrer" class="btn-search-action btn-video-search">
      <i class="fas fa-play-circle"></i> Search Videos on Google
    </a>
    <a href="https://www.google.com/search?q=Class+7+Science+%22Neutralisation+reaction+in+everyday+life%22+notes+examples" 
       target="_blank" rel="noopener noreferrer" class="btn-search-action btn-web-search">
      <i class="fas fa-book-open"></i> Deep-Dive Articles & Notes
    </a>
  </div>
</div>
```
