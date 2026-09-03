# Hindi Chapter Processing Instructions

You are tasked with converting images of a Hindi textbook chapter into an interactive HTML module.

## Layout & Design
1. The HTML must use the standard modern dark-mode glassmorphism UI.
2. The page MUST have a `<title>` tag with the Chapter Name.
3. The page MUST include the standard sticky header. Use the exact code below for the header:
```html
<header class="site-header" style="display:flex; justify-content:space-between; align-items:center; padding: 10px 20px; border-bottom: 1px solid rgba(255,255,255,0.1); background: var(--bg-main); position: sticky; top: 0; z-index: 1000;">
    <div class="header-left" style="display:flex; align-items:center; gap: 8px; font-size: 1.1rem; font-weight: 500; color: var(--text-main);">
        <a href="../../index.html" style="text-decoration:none; color:inherit; display:flex; align-items:center; gap:6px;">
            <i class="fas fa-home"></i> Home
        </a>
        <span style="margin: 0 8px; color: var(--text-muted);">&gt;</span> <a href="../../hindi_index.html" style="text-decoration:none; color:inherit;">Hindi</a><span style="margin: 0 8px; color: var(--text-muted);">&gt;</span> <span style="color:var(--accent); font-weight:600;">Chapter [X]</span>
    </div>
    
    <div class="header-right" style="display:flex; align-items:center; gap: 20px;">
        <div class="search-container" style="display:flex; align-items:center;">
            <button id="global-search-btn" aria-label="Search" style="background:transparent; border:none; color:var(--text-muted); cursor:pointer; padding:5px; display:flex; align-items:center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></button>
            <input id="global-search-input" type="text" placeholder="Search..." style="display:none; margin-left:10px; padding: 6px 15px; border-radius:20px; border:1px solid var(--border); background:rgba(0,0,0,0.2); color:white; width: 180px;">
        </div>
        
        <nav class="header-nav" style="display:flex; align-items:center; gap: 15px;">
            <button class="icon-btn theme-toggle" aria-label="Toggle dark mode" style="background:transparent; border:none; color:white; cursor:pointer; font-size:1.2rem;">
                <i class="fas fa-moon"></i>
            </button>
            
            <a href="../../timetable.html" style="text-decoration:none; color:var(--text-main); font-weight:600; font-size:14px; padding: 6px 12px; background:var(--surface); border:1px solid var(--border); border-radius:20px;">📅 Time Table</a>
            <a href="../../midterm.html" style="text-decoration:none; color:var(--text-main); font-weight:600; font-size:14px; padding: 6px 12px; background:var(--surface); border:1px solid var(--border); border-radius:20px;">🎯 Mid-Term Syllabus</a>

            <div class="user-profile-wrapper" style="position:relative;">
                <div id="global-user-avatar" style="cursor:pointer; border-radius:50%; overflow:hidden; width:40px; height:40px; border:2px solid var(--accent);" onclick="const d = document.getElementById('global-dropdown'); d.style.display = d.style.display === 'none' ? 'flex' : 'none';">
                    <img src="https://ui-avatars.com/api/?name=Pushti&background=8B5CF6&color=ffffff&rounded=true&bold=true" alt="User" style="width:100%; height:100%; object-fit:cover;">
                </div>
                <div id="global-dropdown" style="display:none; position:absolute; right:0; top:50px; background:var(--surface); border:1px solid var(--border); border-radius:12px; padding:15px; width:220px; box-shadow: 0 8px 24px rgba(0,0,0,0.3); flex-direction:column; gap:12px; z-index:1001;">
                    <div style="text-align:center; padding-bottom:10px; border-bottom:1px solid rgba(255,255,255,0.1);">
                        <div style="font-weight:700; font-size:1.1rem; color:var(--text-primary);">Pushti</div>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-size:0.9rem; font-weight:500;">Student</span>
                        <label class="switch" style="position:relative; display:inline-block; width:34px; height:20px;">
                            <input type="checkbox" id="global-role-checkbox" style="opacity:0; width:0; height:0;">
                            <span class="slider" style="position:absolute; cursor:pointer; top:0; left:0; right:0; bottom:0; background-color:var(--border); transition:.4s; border-radius:34px;"></span>
                        </label>
                        <span style="font-size:0.9rem; font-weight:500;">Parent</span>
                    </div>
                </div>
            </div>
        </nav>
    </div>
</header>
```

4. The page MUST have tabs for navigating the content. Use the EXACT following CSS for the `.tabs-wrapper`:
```css
.tabs-wrapper { position: sticky !important; top: 61px !important; z-index: 990 !important; background: var(--bg-main) !important; border-bottom: 1px solid var(--border); padding-top: 10px; padding-bottom: 10px; margin-top: 0 !important; }
```
5. Inside `.tabs-wrapper`, create buttons like `Chapter Text`, `Q&A`, `Grammar`. DO NOT prepend numbers (like "1. ", "2. "). Just use the words!

## Content Extraction
1. **Poems & Stories:** You must transcribe the Hindi text perfectly. Do NOT skip any lines. 
2. **Translation:** For every Hindi stanza/paragraph, provide a direct English translation. Use a `.translation-grid` layout (Left column: Hindi text, Right column: English Translation).
3. **Exercises/Q&A:** If the images contain exercises, multiple-choice questions, or Q&A at the end of the chapter, include them in an 'Exercises' or 'Q&A' tab. For every answer, provide a "Reveal Answer" button that shows the correct answer when clicked. (e.g. `<button class="reveal-btn" onclick="this.nextElementSibling.style.display='block'; this.style.display='none'">Reveal Answer</button><div class="answer" style="display:none;">Correct Answer</div>`)

## Target File
Save the HTML file in: `d:\Users\expor\Downloads\Codes\chapters\hindi\hindi_ch[X].html` (where X is the chapter number).
Do NOT place it in the `source_materials` folder. Place it in `chapters\hindi\`.

If you are unsure of how to style things, read `d:\Users\expor\Downloads\Codes\chapters\sanskrit\sanskrit_ch3.html` as a template for translation grids and exercises, but MAKE SURE you use the `site-header` and `tabs-wrapper` specifications provided above.

