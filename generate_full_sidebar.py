import os
import glob
import re

files = glob.glob('d:/Users/expor/Downloads/Codes/gemini-code-*.html')
existing_files = {}

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
        
        if chapter != -1:
            if chapter not in existing_files or ts > existing_files[chapter]['ts']:
                existing_files[chapter] = {
                    'file': os.path.basename(f),
                    'ts': ts
                }

SYLLABUS = [
    {
        'subject': 'ICT',
        'emoji': '💻',
        'chapters': [
            {'num': 'Ch-1', 'title': 'Number System'},
            {'num': 'Ch-2', 'title': 'Advanced Features of Excel'},
            {'num': 'Ch-3', 'title': 'Artificial Intelligence'},
            {'num': 'Ch-4', 'title': 'Working with HTML Tags and CSS'},
            {'num': 'Ch-5', 'title': 'Lists and Images in HTML'}
        ]
    },
    {
        'subject': 'Maths',
        'emoji': '🔢',
        'chapters': [
            {'num': '-', 'title': 'Large Numbers Around Us'},
            {'num': '-', 'title': 'Arithmetic Expressions'},
            {'num': '-', 'title': 'A Peek Beyond the Point'},
            {'num': '-', 'title': 'Expressions using Letter-Numbers'},
            {'num': '-', 'title': 'Parallel and Intersecting Lines'},
            {'num': '-', 'title': 'Number Play'},
            {'num': '-', 'title': 'A Tale of Three Intersecting Lines'},
            {'num': '-', 'title': 'Working with Fractions'}
        ]
    },
    {
        'subject': 'Science',
        'emoji': '🔬',
        'chapters': [
            {'num': 'Bio Ch.2', 'title': 'Adolescence'},
            {'num': 'Bio Ch.3', 'title': 'Life processes in Animals'},
            {'num': 'Chem Ch.1', 'title': 'Acids, Bases and neutral'},
            {'num': 'Chem Ch.2', 'title': 'The world of metals and non-metals'},
            {'num': 'Phy Ch.1', 'title': 'Electricity'},
            {'num': 'Phy Ch.2', 'title': 'Heat transfer'},
            {'num': 'Phy Ch.3', 'title': 'Measurement of time and motion'}
        ]
    },
    {
        'subject': 'Social Science',
        'emoji': '🌍',
        'chapters': [
            {'num': 'Ch 1', 'title': 'Interior of the Earth', 'ss_id': 1},
            {'num': 'Ch 2', 'title': 'Our Changing Earth', 'ss_id': 2},
            {'num': 'Ch 6', 'title': 'The first Indian Empires', 'ss_id': 6},
            {'num': 'Ch 7', 'title': 'India in the Iron Age', 'ss_id': 7},
            {'num': 'Ch 8', 'title': 'India from the 4th -7th Century CE', 'ss_id': 8},
            {'num': 'Ch 13', 'title': 'Understanding Gender', 'ss_id': 13},
            {'num': 'Ch 14', 'title': 'How does Democracy Work', 'ss_id': 14},
            {'num': 'Ch 17', 'title': 'Market around us', 'ss_id': 17}
        ]
    },
    {
        'subject': 'English',
        'emoji': '📝',
        'chapters': [
            {'num': 'Lit U1', 'title': 'Where Learning Begins (Ch 1,2,3)'},
            {'num': 'Lit U2', 'title': 'Wanderlust (Ch 1,2,3)'},
            {'num': 'Lit U3', 'title': 'Real-Life Heroes (Ch 1,2,3)'},
            {'num': 'Writing', 'title': 'Story, Summary, Paragraph, Letter'},
            {'num': 'Reading', 'title': 'Unseen Passages'},
            {'num': 'Grammar', 'title': 'L-1 to 10 & 17'},
            {'num': 'Vocab', 'title': 'Homonyms, suffixes, phrases'}
        ]
    },
    {
        'subject': 'Hindi',
        'emoji': '🗣️',
        'chapters': [
            {'num': 'Lit', 'title': 'Poem 1, 3, 8 | Chapter 2, 4, 5, 6, 7'},
            {'num': 'Grammar', 'title': 'Chapter 1, 2, 3, 4, 6, 7, 22 | Extra'},
            {'num': 'Writing', 'title': 'Letter, Anucheed, Chitra Varnan...'},
            {'num': 'Reading', 'title': 'Unseen Comprehension'}
        ]
    },
    {
        'subject': 'Sanskrit',
        'emoji': '🕉️',
        'chapters': [
            {'num': 'Ch 1', 'title': 'वन्देभारतम्'},
            {'num': 'Ch 2', 'title': 'नित्यं पिबामः सुभाषितरसम्'},
            {'num': 'Ch 3', 'title': 'मित्राय नम:'},
            {'num': 'Ch 4', 'title': 'न लभ्यते चेत् अम्लं द्राक्षाफलम्'},
            {'num': 'Ch 5', 'title': 'सेवा हि परमो धर्म:'},
            {'num': 'Ch 6', 'title': 'क्रीडाम: वयं श्लोकनाटकशालम्'},
            {'num': 'Vyakaran', 'title': 'वर्णमाला, शब्दरूपाणि...'},
            {'num': 'Rachna', 'title': 'पत्रलेखनम्, चित्रवर्णनम्...'}
        ]
    }
]

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
    
    /* Login Overlay Styles */
    #auth-overlay {
        position: fixed; top: 0; left: 0; right: 0; bottom: 0;
        background: url('https://www.transparenttextures.com/patterns/cream-paper.png'), #F9F5EC;
        z-index: 1000;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
    }
    .auth-box {
        background: #fff; padding: 40px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        width: 100%; max-width: 350px; text-align: center;
        border-top: 5px solid var(--gold);
    }
    .auth-box h2 { font-family: 'Cinzel', serif; color: #7A2A2E; margin-top: 0; }
    .auth-input {
        width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd;
        border-radius: 6px; font-family: 'Nunito', sans-serif; box-sizing: border-box;
    }
    .auth-btn {
        width: 100%; padding: 12px; background: #7A2A2E; color: white; border: none;
        border-radius: 6px; font-family: 'Nunito', sans-serif; font-weight: bold; cursor: pointer;
        margin-top: 10px; transition: background 0.2s;
    }
    .auth-btn:hover { background: #4A1A1D; }
    .error-msg { color: #d9534f; font-size: 0.85rem; margin-top: 10px; display: none; }

    #app-container {
        display: none; /* hidden until logged in */
        width: 100%; height: 100%;
        display: flex;
    }

    #sidebar {
        width: 330px;
        background-color: var(--sidebar-bg);
        color: var(--sidebar-text);
        display: flex;
        flex-direction: column;
        box-shadow: 4px 0 15px rgba(0,0,0,0.1);
        z-index: 10;
    }
    .sidebar-header {
        padding: 24px 20px 15px 20px;
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
    .sidebar-header p { margin: 8px 0 0 0; font-size: 0.9rem; opacity: 0.8; }
    
    .user-info {
        margin-top: 15px; font-size: 0.8rem; color: #aaa;
        display: flex; justify-content: space-between; align-items: center;
    }
    .logout-btn {
        background: none; border: 1px solid #aaa; color: #aaa; padding: 3px 8px;
        border-radius: 4px; cursor: pointer; font-size: 0.75rem;
    }
    .logout-btn:hover { background: #aaa; color: #000; }

    .nav-container {
        flex-grow: 1;
        overflow-y: auto;
        padding-bottom: 40px;
    }
    .nav-container::-webkit-scrollbar { width: 6px; }
    .nav-container::-webkit-scrollbar-track { background: var(--sidebar-bg); }
    .nav-container::-webkit-scrollbar-thumb { background: #4A1A1D; border-radius: 4px; }
    
    .subject-group { border-bottom: 1px solid rgba(255,255,255,0.05); }
    .subject-title {
        background: var(--subject-bg); color: var(--gold); padding: 14px 20px;
        font-family: 'Cinzel', serif; font-size: 1.1rem; font-weight: 700;
        cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;
    }
    .subject-title:hover { background: #110e0c; }
    .subject-title::after { content: '▼'; font-size: 0.8rem; transition: transform 0.2s; }
    .subject-group.collapsed .subject-title::after { transform: rotate(-90deg); }
    .nav-links { list-style: none; padding: 0; margin: 0; overflow: hidden; }
    .subject-group.collapsed .nav-links { display: none; }
    .nav-item { border-bottom: 1px solid rgba(255,255,255,0.02); }
    .nav-btn {
        width: 100%; text-align: left; background: none; border: none; color: var(--sidebar-text);
        padding: 14px 20px 14px 25px; font-size: 0.95rem; font-family: 'Nunito', sans-serif; font-weight: 600;
        cursor: pointer; transition: all 0.2s ease; display: flex; align-items: center;
    }
    .nav-btn:hover { background-color: var(--sidebar-hover); padding-left: 30px; }
    .nav-btn.active { background-color: var(--sidebar-active); border-left: 4px solid var(--gold); padding-left: 21px; }
    .nav-btn.pending { opacity: 0.5; }
    .nav-btn.pending:hover { opacity: 0.8; }
    .chap-num { font-weight: 800; color: var(--gold); margin-right: 12px; font-size: 0.95rem; min-width: 60px; }
    .chap-title { line-height: 1.3; }
    .status-dot { width: 8px; height: 8px; border-radius: 50%; margin-left: auto; flex-shrink: 0; }
    .dot-ready { background-color: #28a745; box-shadow: 0 0 5px #28a745; }
    .dot-pending { background-color: #6c757d; }

    #content-area { flex-grow: 1; background-color: #fff; position: relative; }
    iframe { width: 100%; height: 100%; border: none; display: block; }
    .welcome-screen {
        position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        text-align: center; background: #F9F5EC; z-index: 5; padding: 40px;
    }
    .welcome-screen h2 { font-family: 'Cinzel', serif; color: #7A2A2E; font-size: 2.5rem; margin-bottom: 10px; }
    .welcome-screen p { font-size: 1.2rem; color: #2B2620; max-width: 600px; margin-bottom: 20px; }
</style>
</head>
<body>

<!-- Login Overlay -->
<div id="auth-overlay">
    <div class="auth-box">
        <h2>Study Hub Login</h2>
        <input type="email" id="email" class="auth-input" placeholder="Email" />
        <input type="password" id="password" class="auth-input" placeholder="Password" />
        <button id="login-btn" class="auth-btn">Sign In</button>
        <div id="auth-error" class="error-msg">Invalid email or password.</div>
    </div>
</div>

<!-- Main App -->
<div id="app-container" style="display:none;">
    <div id="sidebar">
        <div class="sidebar-header">
            <h1>Pushti's Hub</h1>
            <p>Exam Preparation Dashboard</p>
            <div class="user-info">
                <span id="user-display">Student Mode</span>
                <button class="logout-btn" id="logout-btn">Log Out</button>
            </div>
        </div>
        <div class="nav-container" id="nav-container">
'''

for subj in SYLLABUS:
    html_content += f'''
            <div class="subject-group" onclick="toggleGroup(this)">
                <div class="subject-title">{subj['emoji']} {subj['subject']}</div>
                <ul class="nav-links">
'''
    for ch in subj['chapters']:
        file_path = ''
        is_ready = False
        
        if 'ss_id' in ch and ch['ss_id'] in existing_files:
            file_path = existing_files[ch['ss_id']]['file']
            is_ready = True
            
        btn_class = 'nav-btn' + ('' if is_ready else ' pending')
        dot_class = 'dot-ready' if is_ready else 'dot-pending'
        onclick = f"loadChapter(event, '{file_path}', '{subj['subject']}', '{ch['title']}', this)" if is_ready else "showPending(event)"
        
        html_content += f'''
                    <li class="nav-item">
                        <button class="{btn_class}" onclick="{onclick}">
                            <span class="chap-num">{ch['num']}</span>
                            <span class="chap-title">{ch['title']}</span>
                            <span class="status-dot {dot_class}"></span>
                        </button>
                    </li>'''
                
    html_content += '''
                </ul>
            </div>
'''

html_content += '''
        </div>
    </div>

    <div id="content-area">
        <div class="welcome-screen" id="welcome">
            <h2>Welcome! 🌟</h2>
            <p>Your full syllabus has been loaded! Chapters with a <span style="color:#28a745; font-weight:bold;">green dot</span> are ready for you to study.</p>
        </div>
        <div class="welcome-screen" id="pending-screen" style="display: none; background: #FFF8E7;">
            <h2>Coming Soon 🚧</h2>
            <p>This chapter is currently being prepared. Check back later!</p>
            <button onclick="document.getElementById('pending-screen').style.display='none'; document.getElementById('welcome').style.display='flex';" 
                    style="padding: 10px 20px; font-family: 'Cinzel', serif; background: #C59B27; border: none; color: white; border-radius: 5px; cursor: pointer; font-size: 1.1rem; margin-top: 20px;">
                Go Back
            </button>
        </div>
        <iframe id="chapter-frame" src="about:blank" title="Chapter Content"></iframe>
    </div>
</div>

<script type="module">
    import { auth, db, signInWithEmailAndPassword, signOut, onAuthStateChanged, collection, addDoc, serverTimestamp, doc, getDoc } from './firebase-config.js';

    let currentUser = null;

    document.getElementById('login-btn').addEventListener('click', async () => {
        const e = document.getElementById('email').value;
        const p = document.getElementById('password').value;
        const err = document.getElementById('auth-error');
        err.style.display = 'none';
        
        try {
            await signInWithEmailAndPassword(auth, e, p);
        } catch (error) {
            err.textContent = "Error: " + error.message;
            err.style.display = 'block';
        }
    });

    document.getElementById('logout-btn').addEventListener('click', () => {
        signOut(auth);
    });

    onAuthStateChanged(auth, async (user) => {
        if (user) {
            currentUser = user;
            document.getElementById('auth-overlay').style.display = 'none';
            document.getElementById('app-container').style.display = 'flex';
            
            const userDoc = await getDoc(doc(db, 'users', user.uid));
            let role = 'student';
            if (userDoc.exists()) {
                role = userDoc.data().role || 'student';
            }
            
            document.getElementById('user-display').textContent = (role === 'admin') ? 'Parent Mode' : 'Student Mode';

            if (role === 'admin') {
                document.getElementById('welcome').style.display = 'none';
                document.getElementById('chapter-frame').style.display = 'block';
                document.getElementById('chapter-frame').src = 'parent_dashboard.html';
                
                document.getElementById('nav-container').style.opacity = '0.5';
                document.getElementById('nav-container').style.pointerEvents = 'none';
            } else {
                addDoc(collection(db, 'activity'), {
                    userId: user.uid,
                    email: user.email,
                    action: 'Logged in',
                    timestamp: serverTimestamp()
                });
            }

        } else {
            currentUser = null;
            document.getElementById('auth-overlay').style.display = 'flex';
            document.getElementById('app-container').style.display = 'none';
        }
    });

    window.toggleGroup = function(element) {
        if (event.target.closest('.nav-btn')) return;
        element.classList.toggle('collapsed');
    };

    window.loadChapter = function(e, file, subject, title, btnElement) {
        e.stopPropagation();
        
        document.getElementById('welcome').style.display = 'none';
        document.getElementById('pending-screen').style.display = 'none';
        document.getElementById('chapter-frame').style.display = 'block';
        
        document.getElementById('chapter-frame').src = file + (currentUser ? "#" + currentUser.uid : "");
        
        const buttons = document.querySelectorAll('.nav-btn');
        buttons.forEach(btn => btn.classList.remove('active'));
        btnElement.classList.add('active');
        
        if (currentUser && document.getElementById('user-display').textContent === 'Student Mode') {
            addDoc(collection(db, 'activity'), {
                userId: currentUser.uid,
                email: currentUser.email,
                action: 'Opened Chapter',
                subject: subject,
                chapter: title,
                timestamp: serverTimestamp()
            });
        }
    };
    
    window.showPending = function(e) {
        e.stopPropagation();
        document.getElementById('welcome').style.display = 'none';
        document.getElementById('chapter-frame').style.display = 'none';
        document.getElementById('pending-screen').style.display = 'flex';
        
        const buttons = document.querySelectorAll('.nav-btn');
        buttons.forEach(btn => btn.classList.remove('active'));
    };
</script>
</body>
</html>
'''

with open('d:/Users/expor/Downloads/Codes/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("index.html updated successfully.")
