# Standard Operating Procedure (SOP) / GITA

This document outlines the standard formatting and coding practices for the Pushti Study Hub project.

## 1. Standard Header Format

All generated HTML pages (including Claude Notes and Gemini Practice modules) **MUST** use the following standardized sticky header format instead of breadcrumbs. This ensures a unified UI across the entire platform.

### CSS (Standard Header)
```css
/* Standard Header */
.standard-header {
    display: flex;
    align-items: center;
    padding: 15px 40px;
    background: rgba(30, 41, 59, 0.95);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
    margin: -2rem -2rem 2rem -2rem; /* Adjust according to body padding */
}
body {
    padding-top: 0; /* Reset top padding since header handles it */
}
.standard-back-btn {
    color: #f8fafc;
    text-decoration: none;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    transition: background 0.2s;
    border: 1px solid rgba(255, 255, 255, 0.1);
}
.standard-back-btn:hover {
    background: rgba(255, 255, 255, 0.1);
}
.standard-subject-title {
    color: #f8fafc;
    font-size: 1.25rem;
    font-weight: 600;
    margin-left: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}
```

### HTML (Standard Header)
```html
<header class="standard-header">
    <a href="../../../{link_to_subject_index}.html" class="standard-back-btn">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        Back to Hub
    </a>
    <div class="standard-subject-title">
        {Subject Name} <span style="color:#64748b;">|</span> {Current Page Name}
    </div>
</header>
```

*Rule created: 2026-09-02*
