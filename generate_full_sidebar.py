<!DOCTYPE html>
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

            <div class="subject-group" onclick="toggleGroup(this)">
                <div class="subject-title">💻 ICT</div>
                <ul class="nav-links">

                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Ch-1</span>
                            <span class="chap-title">Number System</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Ch-2</span>
                            <span class="chap-title">Advanced Features of Excel</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Ch-3</span>
                            <span class="chap-title">Artificial Intelligence</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Ch-4</span>
                            <span class="chap-title">Working with HTML Tags and CSS</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Ch-5</span>
                            <span class="chap-title">Lists and Images in HTML</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                </ul>
            </div>

            <div class="subject-group" onclick="toggleGroup(this)">
                <div class="subject-title">🔢 Maths</div>
                <ul class="nav-links">

                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">-</span>
                            <span class="chap-title">Large Numbers Around Us</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">-</span>
                            <span class="chap-title">Arithmetic Expressions</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">-</span>
                            <span class="chap-title">A Peek Beyond the Point</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">-</span>
                            <span class="chap-title">Expressions using Letter-Numbers</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">-</span>
                            <span class="chap-title">Parallel and Intersecting Lines</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">-</span>
                            <span class="chap-title">Number Play</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">-</span>
                            <span class="chap-title">A Tale of Three Intersecting Lines</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">-</span>
                            <span class="chap-title">Working with Fractions</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                </ul>
            </div>

            <div class="subject-group" onclick="toggleGroup(this)">
                <div class="subject-title">🔬 Science</div>
                <ul class="nav-links">

                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Bio Ch.2</span>
                            <span class="chap-title">Adolescence</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Bio Ch.3</span>
                            <span class="chap-title">Life processes in Animals</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Chem Ch.1</span>
                            <span class="chap-title">Acids, Bases and neutral</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Chem Ch.2</span>
                            <span class="chap-title">The world of metals and non-metals</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Phy Ch.1</span>
                            <span class="chap-title">Electricity</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Phy Ch.2</span>
                            <span class="chap-title">Heat transfer</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Phy Ch.3</span>
                            <span class="chap-title">Measurement of time and motion</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                </ul>
            </div>

            <div class="subject-group" onclick="toggleGroup(this)">
                <div class="subject-title">🌍 Social Science</div>
                <ul class="nav-links">

                    <li class="nav-item">
                        <button class="nav-btn" onclick="loadChapter(event, 'gemini-code-1786806264249.html', 'Social Science', 'Interior of the Earth', this)">
                            <span class="chap-num">Ch 1</span>
                            <span class="chap-title">Interior of the Earth</span>
                            <span class="status-dot dot-ready"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn" onclick="loadChapter(event, 'gemini-code-1786807311533 (1).html', 'Social Science', 'Our Changing Earth', this)">
                            <span class="chap-num">Ch 2</span>
                            <span class="chap-title">Our Changing Earth</span>
                            <span class="status-dot dot-ready"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn" onclick="loadChapter(event, 'gemini-code-1786868059204.html', 'Social Science', 'The first Indian Empires', this)">
                            <span class="chap-num">Ch 6</span>
                            <span class="chap-title">The first Indian Empires</span>
                            <span class="status-dot dot-ready"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn" onclick="loadChapter(event, 'gemini-code-1786869713516.html', 'Social Science', 'India in the Iron Age', this)">
                            <span class="chap-num">Ch 7</span>
                            <span class="chap-title">India in the Iron Age</span>
                            <span class="status-dot dot-ready"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn" onclick="loadChapter(event, 'gemini-code-1786554270939.html', 'Social Science', 'India from the 4th -7th Century CE', this)">
                            <span class="chap-num">Ch 8</span>
                            <span class="chap-title">India from the 4th -7th Century CE</span>
                            <span class="status-dot dot-ready"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn" onclick="loadChapter(event, 'gemini-code-1786870843828.html', 'Social Science', 'Understanding Gender', this)">
                            <span class="chap-num">Ch 13</span>
                            <span class="chap-title">Understanding Gender</span>
                            <span class="status-dot dot-ready"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn" onclick="loadChapter(event, 'gemini-code-1786873269831.html', 'Social Science', 'How does Democracy Work', this)">
                            <span class="chap-num">Ch 14</span>
                            <span class="chap-title">How does Democracy Work</span>
                            <span class="status-dot dot-ready"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn" onclick="loadChapter(event, 'gemini-code-1786875375575.html', 'Social Science', 'Market around us', this)">
                            <span class="chap-num">Ch 17</span>
                            <span class="chap-title">Market around us</span>
                            <span class="status-dot dot-ready"></span>
                        </button>
                    </li>
                </ul>
            </div>

            <div class="subject-group" onclick="toggleGroup(this)">
                <div class="subject-title">📝 English</div>
                <ul class="nav-links">

                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Lit U1</span>
                            <span class="chap-title">Where Learning Begins (Ch 1,2,3)</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Lit U2</span>
                            <span class="chap-title">Wanderlust (Ch 1,2,3)</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Lit U3</span>
                            <span class="chap-title">Real-Life Heroes (Ch 1,2,3)</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Writing</span>
                            <span class="chap-title">Story, Summary, Paragraph, Letter</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Reading</span>
                            <span class="chap-title">Unseen Passages</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Grammar</span>
                            <span class="chap-title">L-1 to 10 & 17</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Vocab</span>
                            <span class="chap-title">Homonyms, suffixes, phrases</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                </ul>
            </div>

            <div class="subject-group" onclick="toggleGroup(this)">
                <div class="subject-title">🗣️ Hindi</div>
                <ul class="nav-links">

                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Lit</span>
                            <span class="chap-title">Poem 1, 3, 8 | Chapter 2, 4, 5, 6, 7</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Grammar</span>
                            <span class="chap-title">Chapter 1, 2, 3, 4, 6, 7, 22 | Extra</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Writing</span>
                            <span class="chap-title">Letter, Anucheed, Chitra Varnan...</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Reading</span>
                            <span class="chap-title">Unseen Comprehension</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                </ul>
            </div>

            <div class="subject-group" onclick="toggleGroup(this)">
                <div class="subject-title">🕉️ Sanskrit</div>
                <ul class="nav-links">

                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Ch 1</span>
                            <span class="chap-title">वन्देभारतम्</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Ch 2</span>
                            <span class="chap-title">नित्यं पिबामः सुभाषितरसम्</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Ch 3</span>
                            <span class="chap-title">मित्राय नम:</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Ch 4</span>
                            <span class="chap-title">न लभ्यते चेत् अम्लं द्राक्षाफलम्</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Ch 5</span>
                            <span class="chap-title">सेवा हि परमो धर्म:</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Ch 6</span>
                            <span class="chap-title">क्रीडाम: वयं श्लोकनाटकशालम्</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Vyakaran</span>
                            <span class="chap-title">वर्णमाला, शब्दरूपाणि...</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-btn pending" onclick="showPending(event)">
                            <span class="chap-num">Rachna</span>
                            <span class="chap-title">पत्रलेखनम्, चित्रवर्णनम्...</span>
                            <span class="status-dot dot-pending"></span>
                        </button>
                    </li>
                </ul>
            </div>

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
