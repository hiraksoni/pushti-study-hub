import os
import glob
import re

files = glob.glob('d:/Users/expor/Downloads/Codes/gemini-code-*.html')
data = []

# Syllabus Mapping for auto-categorization based on chapter number or title keywords
SYLLABUS = {
    'Social Science': [1, 2, 6, 7, 8, 13, 14, 17],
    'ICT': ['number system', 'excel', 'artificial intelligence', 'html', 'css', 'lists and images'],
    'Science': ['adolescence', 'life processes', 'acids', 'bases', 'metals', 'electricity', 'heat transfer', 'measurement'],
    'Maths': ['numbers around us', 'arithmetic', 'peek beyond', 'expressions', 'parallel', 'intersecting', 'number play', 'fractions'],
    'English': ['where learning begins', 'wanderlust', 'real-life heroes', 'story writing', 'paragraph', 'unseen'],
    'Hindi': ['literature', 'grammar', 'writing', 'comprehension', 'anucheed', 'chitra varnan'],
    'Sanskrit': ['vandebharatam', 'shlok', 'mitraya namah', 'drakshaphalam']
}

for f in files:
    with open(f, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
        match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = match.group(1) if match else 'No Title'
        
        chap_match = re.search(r'Chapter\s*(\d+)', title, re.IGNORECASE)
        if not chap_match:
            chap_match = re.search(r'Chapter\s*(\d+)', content, re.IGNORECASE)
            
        chapter = int(chap_match.group(1)) if chap_match else -1
        
        ts_match = re.search(r'(\d+)', os.path.basename(f))
        ts = int(ts_match.group(1)) if ts_match else 0
        
        # Clean the title safely
        clean = title
        if '\ufffd' in clean:
            clean = clean.split('\ufffd')[0]
        elif '—' in clean:
            clean = clean.split('—')[0]
        elif '-' in clean:
            clean = clean.split('-')[0]
            
        clean = clean.replace('Chapter ' + str(chapter) + ':', '').replace('Chapter ' + str(chapter), '').strip()
        if not clean:
            clean = "Overview"
            
        # Determine Subject
        subject = "Other"
        clean_lower = clean.lower()
        title_lower = title.lower()
        
        # Rule 1: Social Science known chapters
        if chapter in [1, 2, 6, 7, 8, 13, 14, 17] and "social" not in clean_lower and "ict" not in clean_lower:
            subject = "Social Science"
            
        # Rule 2: Keyword matching
        for subj, keywords in SYLLABUS.items():
            if subject != "Other":
                break
            for kw in keywords:
                if isinstance(kw, str) and (kw in clean_lower or kw in title_lower):
                    subject = subj
                    break
        
        # Fallback for the current known files if they got missed
        if subject == "Other" and chapter != -1:
             subject = "Social Science" # Assuming all current numbered chapters are SS
        
        data.append({
            'file': os.path.basename(f), 
            'title': clean, 
            'chapter': chapter, 
            'ts': ts,
            'subject': subject
        })

# Get latest file for each (Subject, Chapter) combination
latest_files = {}
for d in data:
    if d['chapter'] != -1:
        key = f"{d['subject']}_{d['chapter']}"
        if key not in latest_files or d['ts'] > latest_files[key]['ts']:
            latest_files[key] = d

# Group by Subject
grouped = {}
for key, d in latest_files.items():
    subj = d['subject']
    if subj not in grouped:
        grouped[subj] = []
    grouped[subj].append(d)

for subj in grouped:
    grouped[subj] = sorted(grouped[subj], key=lambda x: x['chapter'])

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pushti's Master Study Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
    :root {
        --sidebar-bg: #2B2620;
        --sidebar-text: #F9F5EC;
        --sidebar-hover: #4A1A1D;
        --sidebar-active: #7A2A2E;
        --gold: #C59B27;
        --subject-bg: #1a1612;
    }
    body {
        margin: 0;
        padding: 0;
        display: flex;
        height: 100vh;
        font-family: 'Nunito', sans-serif;
        background-color: #F9F5EC;
        overflow: hidden;
    }
    #sidebar {
        width: 320px;
        background-color: var(--sidebar-bg);
        color: var(--sidebar-text);
        display: flex;
        flex-direction: column;
        box-shadow: 4px 0 15px rgba(0,0,0,0.1);
        z-index: 10;
    }
    .sidebar-header {
        padding: 24px 20px;
        text-align: center;
        background: linear-gradient(135deg, #1a1612, #2B2620);
        border-bottom: 3px solid var(--gold);
        flex-shrink: 0;
    }
    .sidebar-header h1 {
        font-family: 'Cinzel', serif;
        margin: 0;
        font-size: 1.6rem;
        color: var(--gold);
        letter-spacing: 1px;
    }
    .sidebar-header p {
        margin: 8px 0 0 0;
        font-size: 0.9rem;
        opacity: 0.8;
    }
    .nav-container {
        flex-grow: 1;
        overflow-y: auto;
        padding-bottom: 20px;
    }
    .subject-group {
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .subject-title {
        background: var(--subject-bg);
        color: var(--gold);
        padding: 14px 20px;
        font-family: 'Cinzel', serif;
        font-size: 1.1rem;
        font-weight: 700;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        user-select: none;
    }
    .subject-title:hover {
        background: #110e0c;
    }
    .subject-title::after {
        content: '▼';
        font-size: 0.8rem;
        transition: transform 0.2s;
    }
    .subject-group.collapsed .subject-title::after {
        transform: rotate(-90deg);
    }
    .nav-links {
        list-style: none;
        padding: 0;
        margin: 0;
        transition: max-height 0.3s ease-out;
        overflow: hidden;
    }
    .subject-group.collapsed .nav-links {
        display: none;
    }
    .nav-item {
        border-bottom: 1px solid rgba(255,255,255,0.02);
    }
    .nav-btn {
        width: 100%;
        text-align: left;
        background: none;
        border: none;
        color: var(--sidebar-text);
        padding: 14px 20px 14px 30px;
        font-size: 0.95rem;
        font-family: 'Nunito', sans-serif;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
        display: flex;
        align-items: center;
    }
    .nav-btn:hover {
        background-color: var(--sidebar-hover);
        padding-left: 35px;
    }
    .nav-btn.active {
        background-color: var(--sidebar-active);
        border-left: 4px solid var(--gold);
        padding-left: 26px; /* 30 - 4 */
    }
    .chap-num {
        font-weight: 800;
        color: var(--gold);
        margin-right: 12px;
        font-size: 1.05rem;
        min-width: 45px;
    }
    .chap-title {
        line-height: 1.3;
    }
    #content-area {
        flex-grow: 1;
        background-color: #fff;
        position: relative;
    }
    iframe {
        width: 100%;
        height: 100%;
        border: none;
        display: block;
    }
    .welcome-screen {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        background: #F9F5EC;
        z-index: 5;
        padding: 40px;
    }
    .welcome-screen h2 {
        font-family: 'Cinzel', serif;
        color: #7A2A2E;
        font-size: 2.5rem;
        margin-bottom: 10px;
    }
    .welcome-screen p {
        font-size: 1.2rem;
        color: #2B2620;
        max-width: 600px;
        margin-bottom: 20px;
    }
    .empty-state {
        padding: 15px 20px 15px 30px;
        font-size: 0.85rem;
        color: #888;
        font-style: italic;
    }
</style>
</head>
<body>

<div id="sidebar">
    <div class="sidebar-header">
        <h1>Pushti's Hub</h1>
        <p>Master Study Dashboard</p>
    </div>
    <div class="nav-container">
'''

# Subject emojis for UI
EMOJIS = {
    'Social Science': '🌍',
    'ICT': '💻',
    'Science': '🔬',
    'Maths': '🔢',
    'English': '📝',
    'Hindi': '🗣️',
    'Sanskrit': '🕉️',
    'Other': '📂'
}

# Display all subjects even if empty right now, to show the structure
for subj in ['ICT', 'Maths', 'Science', 'Social Science', 'English', 'Hindi', 'Sanskrit']:
    emoji = EMOJIS.get(subj, '')
    html_content += f'''
        <div class="subject-group" onclick="toggleGroup(this)">
            <div class="subject-title">{emoji} {subj}</div>
            <ul class="nav-links">
'''
    if subj in grouped and grouped[subj]:
        for ch in grouped[subj]:
            html_content += f'''
                <li class="nav-item">
                    <button class="nav-btn" onclick="loadChapter(event, '{ch['file']}', this)">
                        <span class="chap-num">Ch {ch['chapter']}</span>
                        <span class="chap-title">{ch['title']}</span>
                    </button>
                </li>'''
    else:
        html_content += f'''
                <li class="nav-item empty-state">Chapters coming soon!</li>'''
                
    html_content += '''
            </ul>
        </div>
'''

html_content += '''
    </div>
</div>

<div id="content-area">
    <div class="welcome-screen" id="welcome">
        <h2>Welcome, Pushti! 🌟</h2>
        <p>Your dashboard is now upgraded with all your subjects! Click on a subject in the sidebar to view its chapters.</p>
        <p style="font-size: 0.9rem; color: #666;">New chapters and quizzes will appear here as soon as they are uploaded.</p>
    </div>
    <iframe id="chapter-frame" src="about:blank" title="Chapter Content"></iframe>
</div>

<script>
    function toggleGroup(element) {
        // Only toggle if we clicked the title, not a button inside
        if (event.target.closest('.nav-btn')) return;
        element.classList.toggle('collapsed');
    }

    function loadChapter(e, file, btnElement) {
        e.stopPropagation(); // Prevent group toggle
        
        // Hide welcome screen
        document.getElementById('welcome').style.display = 'none';
        
        // Load iframe
        document.getElementById('chapter-frame').src = file;
        
        // Update active state
        const buttons = document.querySelectorAll('.nav-btn');
        buttons.forEach(btn => btn.classList.remove('active'));
        btnElement.classList.add('active');
    }
</script>
</body>
</html>
'''

with open('d:/Users/expor/Downloads/Codes/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully generated index.html with Subjects!")
