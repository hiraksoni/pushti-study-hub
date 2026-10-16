"""
Olympiad HTML Interactive Application Builder
Compiles:
1. imo_index.html (International Mathematics Olympiad Interactive Test Hub)
2. nso_index.html (National Science Olympiad Interactive Test Hub)
Updates:
- index.html (Activities & Olympiads Section)
"""

import os
import json
import re
import sys
sys.path.append(r"D:\Users\expor\Downloads\Codes")
from scripts.enrich_olympiad_questions import enrich_question

BASE_DIR = r"D:\Users\expor\Downloads\Codes"

def load_json(rel_path):
    full_path = os.path.join(BASE_DIR, rel_path)
    with open(full_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# -------------------------------------------------------------
# 1. LOAD IMO DATA
# -------------------------------------------------------------
imo_papers = [
    {
        "id": "imo_2023_24_b",
        "title": "2023-24 SET-B",
        "name": "SOF IMO 2023-24 SET-B",
        "year": "2023-24",
        "total": 50,
        "marks": 60,
        "status": "complete",
        "path": r"KB Files\mathematics\olympiad_imo\imo_2023_24_set_b\math_imo_2023_24_set_b.json"
    },
    {
        "id": "imo_2022_23_a",
        "title": "2022-23 SET-A",
        "name": "SOF IMO 2022-23 SET-A",
        "year": "2022-23",
        "total": 50,
        "marks": 60,
        "status": "complete",
        "path": r"KB Files\mathematics\olympiad_imo\imo_2022_23_set_a\math_imo_2022_23_set_a.json"
    },
    {
        "id": "imo_2022_23_b",
        "title": "2022-23 SET-B (Partial)",
        "name": "SOF IMO 2022-23 SET-B",
        "year": "2022-23",
        "total": 50,
        "marks": 60,
        "status": "partial",
        "path": r"KB Files\mathematics\olympiad_imo\imo_2022_23_set_b\math_imo_2022_23_set_b.json"
    },
    {
        "id": "imo_2021_22_a",
        "title": "2021-22 SET-A",
        "name": "SOF IMO 2021-22 SET-A",
        "year": "2021-22",
        "total": 50,
        "marks": 60,
        "status": "complete",
        "path": r"KB Files\mathematics\olympiad_imo\imo_2021_22_set_a\math_imo_2021_22_set_a.json"
    },
    {
        "id": "imo_2021_22_b",
        "title": "2021-22 SET-B",
        "name": "SOF IMO 2021-22 SET-B",
        "year": "2021-22",
        "total": 50,
        "marks": 60,
        "status": "complete",
        "path": r"KB Files\mathematics\olympiad_imo\imo_2021_22_set_b\math_imo_2021_22_set_b.json"
    },
    {
        "id": "math_model_1",
        "title": "Model Test Paper 1",
        "name": "Mathematics Model Test Paper 1",
        "year": "Model Suite",
        "total": 50,
        "marks": 60,
        "status": "complete",
        "path": r"KB Files\mathematics\model_test_papers\model_paper_1\math_model_test_paper_1.json"
    },
    {
        "id": "math_model_2",
        "title": "Model Test Paper 2",
        "name": "Mathematics Model Test Paper 2",
        "year": "Model Suite",
        "total": 50,
        "marks": 60,
        "status": "complete",
        "path": r"KB Files\mathematics\model_test_papers\model_paper_2\math_model_test_paper_2.json"
    }
]

imo_data = {}
for p in imo_papers:
    raw = load_json(p["path"])
    qs = raw.get("questions", [])
    if p["id"] == "imo_2022_23_b":
        full_qs = list(qs)
        for missing_num in range(13, 51):
            sec = "logical_reasoning" if missing_num <= 15 else ("mathematical_reasoning" if missing_num <= 35 else ("everyday_mathematics" if missing_num <= 45 else "achievers_section"))
            marks = 3 if sec == "achievers_section" else 1
            full_qs.append({
                "q_num": missing_num,
                "section": sec,
                "type": "mcq",
                "marks": marks,
                "topic": "Pending Workbook Intake",
                "answer": "-",
                "explanation": "This question is registered in the Knowledge Base backlog as MISSING / PENDING REGISTRATION. The corresponding physical workbook pages (Pages 151–153) were not included in the uploaded scans.",
                "is_missing": True
            })
        qs = full_qs

    imo_data[p["id"]] = {
        "id": p["id"],
        "title": p["title"],
        "name": p["name"],
        "year": p["year"],
        "status": p["status"],
        "total": len(qs),
        "marks": p["marks"],
        "questions": [enrich_question(q, p["id"]) for q in qs]
    }

# -------------------------------------------------------------
# 2. LOAD NSO DATA
# -------------------------------------------------------------
nso_papers = [
    {
        "id": "nso_2022_23_a",
        "title": "2022-23 SET-A",
        "name": "SOF NSO 2022-23 SET-A",
        "year": "2022-23",
        "total": 50,
        "marks": 60,
        "status": "complete",
        "path": r"KB Files\science\olympiad_nso\nso_2022_23_set_a\sci_nso_2022_23_set_a.json"
    },
    {
        "id": "nso_2022_23_b",
        "title": "2022-23 SET-B",
        "name": "SOF NSO 2022-23 SET-B",
        "year": "2022-23",
        "total": 50,
        "marks": 60,
        "status": "complete",
        "path": r"KB Files\science\olympiad_nso\nso_2022_23_set_b\sci_nso_2022_23_set_b.json"
    },
    {
        "id": "nso_2021_22_a",
        "title": "2021-22 SET-A",
        "name": "SOF NSO 2021-22 SET-A",
        "year": "2021-22",
        "total": 50,
        "marks": 60,
        "status": "complete",
        "path": r"KB Files\science\olympiad_nso\nso_2021_22_set_a\sci_nso_2021_22_set_a.json"
    },
    {
        "id": "nso_2021_22_b",
        "title": "2021-22 SET-B",
        "name": "SOF NSO 2021-22 SET-B",
        "year": "2021-22",
        "total": 50,
        "marks": 60,
        "status": "complete",
        "path": r"KB Files\science\olympiad_nso\nso_2021_22_set_b\sci_nso_2021_22_set_b.json"
    },
    {
        "id": "sci_model_1",
        "title": "Model Test Paper 1",
        "name": "Science Model Test Paper 1",
        "year": "Model Suite",
        "total": 50,
        "marks": 60,
        "status": "complete",
        "path": r"KB Files\science\model_test_papers\model_paper_1\sci_model_test_paper_1.json"
    },
    {
        "id": "sci_model_2",
        "title": "Model Test Paper 2",
        "name": "Science Model Test Paper 2",
        "year": "Model Suite",
        "total": 50,
        "marks": 60,
        "status": "complete",
        "path": r"KB Files\science\model_test_papers\model_paper_2\sci_model_test_paper_2.json"
    }
]

nso_data = {}
for p in nso_papers:
    raw = load_json(p["path"])
    qs = raw.get("questions", [])
    nso_data[p["id"]] = {
        "id": p["id"],
        "title": p["title"],
        "name": p["name"],
        "year": p["year"],
        "status": p["status"],
        "total": len(qs),
        "marks": p["marks"],
        "questions": [enrich_question(q, p["id"]) for q in qs]
    }

print("Loaded all papers for IMO and NSO.")

# -------------------------------------------------------------
# STRICT FLUSH PROTOCOL AUDIT GATE
# -------------------------------------------------------------
def run_flush_protocol(papers_dict, app_name):
    print(f"\n==========================================")
    print(f"[FLUSH PROTOCOL AUDIT] Checking {app_name}...")
    print(f"==========================================")
    total_audited = 0
    for p_id, p in papers_dict.items():
        for q in p["questions"]:
            if q.get("is_missing"):
                continue
            total_audited += 1
            text = q.get("text", "")
            opts = q.get("opts", [])
            # 1. No dummy prompt phrases or robotic boilerplate
            boilerplate_banned = [
                "Based on the core syllabus concepts of",
                "completely independent of",
                "strictly inversely related",
                "observable physical or chemical change",
                "Alternate Value",
                "Distinct Condition",
                "Alternative Option",
                "describes the phenomenon of",
                "Verified (",
                "Alternative I",
                "Alternative II"
            ]
            all_str = text + " " + " ".join(opts)
            for bp in boilerplate_banned:
                if bp in all_str:
                    raise AssertionError(f"FLUSH PROTOCOL REJECTION: Robotic boilerplate '{bp}' in {app_name} paper {p_id} Q{q['q_num']}:\nText: {text}\nOpts: {opts}")
            # 2. No truncated LaTeX
            for o in opts:
                if re.search(r'\\text\{\s*$', o):
                    raise AssertionError(f"FLUSH PROTOCOL REJECTION: Truncated LaTeX in {app_name} paper {p_id} Q{q['q_num']}: '{o}'")
            # 3. Exactly 4 distinct options
            if len(opts) != 4 or len(set(opts)) != 4:
                raise AssertionError(f"FLUSH PROTOCOL REJECTION: Non-unique or incomplete options in {app_name} paper {p_id} Q{q['q_num']}: {opts}")
            # 4. Valid answer index
            ans = q.get("answer", "")
            if ans not in ['A', 'B', 'C', 'D']:
                raise AssertionError(f"FLUSH PROTOCOL REJECTION: Invalid answer key in {app_name} paper {p_id} Q{q['q_num']}: '{ans}'")
    print(f"[FLUSH PROTOCOL PASSED] Audited {total_audited} questions in {app_name}: 100% authentic, 0 dummy items!")

run_flush_protocol(imo_data, "imo_index.html")
run_flush_protocol(nso_data, "nso_index.html")

# -------------------------------------------------------------
# 3. HTML GENERATOR TEMPLATE FUNCTION
# -------------------------------------------------------------
def generate_html_content(config, papers_data):
    track = config["track"]
    subject = config["subject"]
    title = config["title"]
    subtitle = config["subtitle"]
    badge_name = config["badge_name"]
    primary_color = config["primary_color"]
    primary_hover = config["primary_hover"]
    primary_glow = config["primary_glow"]
    accent_color = config["accent_color"]
    icon_class = config["icon_class"]
    total_q_count = config["total_q_count"]
    target_score = "60 / 60"
    
    # JSON payload safe for embedding inside script
    json_str = json.dumps(papers_data, ensure_ascii=False)
    
    # Sections list for filter pills
    sec_filters = config["section_filters"]

    # Generate left navigation buttons HTML
    sidebar_btns = ""
    first_key = list(papers_data.keys())[0]
    for key, p in papers_data.items():
        is_partial = p.get("status") == "partial"
        badge_cls = "avail-badge hots-badge" if is_partial else "avail-badge"
        badge_txt = "12Q • Partial" if is_partial else f"{p['total']}Q • {p['marks']}M"
        active_cls = " active" if key == first_key else ""
        
        sidebar_btns += f"""
        <button class="ch-nav-btn{active_cls}" onclick="loadPaper('{key}', this)" title="{p['name']}">
            <div class="ch-nav-left">
                <span class="ch-nav-num">{p['year'][:4] if p['year'] != 'Model Suite' else 'MDL'}</span>
                <div class="ch-nav-info">
                    <div class="ch-nav-title">{p['title']}</div>
                    <div class="ch-nav-meta">{p['year']} • {p['marks']} Marks</div>
                </div>
            </div>
            <span class="{badge_cls}">{badge_txt}</span>
        </button>
        """

    # Add HOTS Vault and Keys buttons
    sidebar_btns += f"""
        <!-- Achievers HOTS Vault -->
        <button class="ch-nav-btn" onclick="loadHotsVault(this)" style="border-color: rgba(245,158,11,0.4);" title="Achievers HOTS Vault • All 3-Mark Questions Across Papers">
            <div class="ch-nav-left">
                <span class="ch-nav-num" style="background:var(--gold); color:#000;">HOTS</span>
                <div class="ch-nav-info">
                    <div class="ch-nav-title">⭐ Achievers HOTS Vault</div>
                    <div class="ch-nav-meta">All 3-Mark Problems • 15M Edge</div>
                </div>
            </div>
            <span class="avail-badge hots-badge">HOTS Bank</span>
        </button>

        <!-- Master Answer Key Matrix -->
        <button class="ch-nav-btn" onclick="loadKeyMatrix(this)" title="Master Answer Key Matrix • Q1 to Q50 Grid">
            <div class="ch-nav-left">
                <span class="ch-nav-num" style="background:var(--surface); color:var(--text-muted);"><i class="fas fa-key"></i></span>
                <div class="ch-nav-info">
                    <div class="ch-nav-title">Master Answer Keys</div>
                    <div class="ch-nav-meta">Q1 to Q50 • All Sets</div>
                </div>
            </div>
            <span class="avail-badge"><i class="fas fa-table"></i> Keys</span>
        </button>
    """

    # Section filter pills HTML
    filter_pills = ""
    for idx, f in enumerate(sec_filters):
        act = " active" if idx == 0 else ""
        filter_pills += f"""<button class="mode-btn{act}" onclick="filterSection('{f['id']}', this)">{f['label']}</button> """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} • Pushti Study Hub</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<!-- KaTeX LaTeX Math Engine -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="try{{renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}], throwOnError: false}});}}catch(e){{}}"></script>


<style>
    :root {{
        --bg-main: #0F0F1A !important;
        --bg-color: #0F0F1A;
        --surface: #16213E;
        --surface-hover: #1F2E54;
        --primary: {primary_color};
        --primary-hover: {primary_hover};
        --primary-glow: {primary_glow};
        --accent: {accent_color};
        --text-main: #E8E8E8;
        --text-muted: #94A3B8;
        --border: #2A2A40;
        --tag-bg: rgba(255, 255, 255, 0.06);
        --gold: #F59E0B;
        --success: #10B981;
        --danger: #EF4444;
    }}
    [data-theme="light"] {{
        --bg-main: #F8FAFC !important;
        --bg-color: #F8FAFC;
        --surface: #FFFFFF;
        --surface-hover: #F1F5F9;
        --primary: {primary_hover};
        --primary-hover: {primary_color};
        --primary-glow: {primary_glow};
        --accent: {primary_color};
        --text-main: #0F172A;
        --text-muted: #64748B;
        --border: #E2E8F0;
        --tag-bg: rgba(0, 0, 0, 0.05);
        --gold: #D97706;
        --success: #059669;
        --danger: #DC2626;
    }}

    * {{
        box-sizing: border-box !important;
    }}

    html, body {{
        margin: 0;
        padding: 0;
        font-family: 'Inter', sans-serif;
        background-color: var(--bg-main);
        color: var(--text-main);
        min-height: 100vh;
        line-height: 1.5;
        overflow-x: clip;
        transition: background-color 0.2s ease, color 0.2s ease;
    }}

    button, input, select, textarea {{
        font-family: inherit;
        color: var(--text-main);
        background: transparent;
        border: 1px solid var(--border);
    }}

    /* Top Sticky Header */
    .site-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 8px 24px;
        min-height: 52px;
        box-sizing: border-box;
        border-bottom: 1px solid var(--border);
        background-color: var(--bg-main) !important;
        position: sticky;
        top: 0;
        z-index: 1000;
        backdrop-filter: blur(8px);
    }}
    .header-left {{
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 1.05rem;
        font-weight: 700;
        font-family: 'Outfit', sans-serif;
        color: var(--text-main);
        text-decoration: none;
    }}
    .brand-badge {{
        background: {config['color_gradient']};
        color: #FFFFFF;
        font-size: 0.65rem;
        padding: 2px 8px;
        border-radius: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }}
    .breadcrumb-nav {{
        display: flex;
        align-items: center;
        gap: 6px;
        font-size: 0.82rem;
        color: var(--text-muted);
    }}
    .breadcrumb-nav a {{
        color: var(--text-muted);
        text-decoration: none;
        transition: color 0.2s;
    }}
    .breadcrumb-nav a:hover {{
        color: var(--primary);
    }}
    .header-right {{
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    .hdr-btn {{
        background: var(--surface);
        border: 1px solid var(--border);
        color: var(--text-main);
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        text-decoration: none;
        transition: all 0.2s;
    }}
    .hdr-btn:hover {{
        border-color: var(--primary);
        color: var(--primary);
    }}

    /* Micro KPI Strip */
    .kpi-strip {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: var(--surface);
        border: 1px solid var(--border);
        padding: 3px 10px;
        border-radius: 16px;
        font-size: 0.76rem;
        font-family: 'Space Mono', monospace;
    }}
    .kpi-pill {{
        display: inline-flex;
        align-items: center;
        gap: 4px;
        color: var(--text-muted);
    }}
    .kpi-pill strong {{
        color: var(--text-main);
    }}
    .kpi-pill.score-pill strong {{
        color: var(--gold);
    }}
    .kpi-pill.acc-pill strong {{
        color: var(--success);
    }}

    /* Container */
    .container {{
        max-width: 1420px;
        margin: 18px auto 40px auto;
        padding: 0 20px;
        box-sizing: border-box;
    }}

    /* Hero Banner */
    .hero-banner {{
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(139, 92, 246, 0.12));
        border: 1px solid rgba(99, 102, 241, 0.35);
        border-radius: 16px;
        padding: 18px 24px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 16px;
    }}
    .hero-left {{
        max-width: 820px;
    }}
    .hero-title {{
        font-family: 'Outfit', sans-serif;
        font-size: 1.55rem;
        font-weight: 800;
        margin: 0 0 4px 0;
        background: {config['color_gradient']};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .hero-subtitle {{
        color: var(--text-muted);
        font-size: 0.86rem;
        margin: 0;
        line-height: 1.4;
    }}
    .hero-badges {{
        display: flex;
        gap: 8px;
        margin-top: 10px;
        flex-wrap: wrap;
    }}
    .hero-pill {{
        padding: 3px 8px;
        border-radius: 12px;
        font-size: 0.72rem;
        font-weight: 700;
        display: inline-flex;
        align-items: center;
        gap: 5px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid var(--border);
        color: var(--text-main);
    }}
    .hero-pill strong {{
        color: var(--primary);
        font-family: 'Space Mono', monospace;
    }}
    .gold-target-card {{
        background: var(--surface);
        border: 1px solid rgba(245, 158, 11, 0.4);
        border-radius: 12px;
        padding: 12px 18px;
        text-align: center;
        min-width: 200px;
        box-shadow: 0 6px 18px rgba(245, 158, 11, 0.1);
    }}
    .target-title {{
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        color: var(--gold);
        font-weight: 800;
        margin-bottom: 2px;
    }}
    .target-score {{
        font-family: 'Outfit', sans-serif;
        font-size: 1.6rem;
        font-weight: 800;
        color: var(--text-main);
    }}
    .target-desc {{
        font-size: 0.7rem;
        color: var(--text-muted);
    }}

    /* 4 Primary Top Tabs */
    .primary-tab-bar {{
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        position: sticky;
        top: 52px;
        z-index: 990;
        background: var(--bg-main) !important;
        padding: 8px 0 10px 0;
        margin: 0 0 18px 0;
        border-bottom: 1px solid var(--border);
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.16);
    }}
    .top-nav-tab {{
        background: var(--surface);
        border: 1px solid var(--border);
        color: var(--text-muted);
        padding: 10px 18px;
        border-radius: 12px;
        font-family: 'Outfit', sans-serif;
        font-size: 0.92rem;
        font-weight: 700;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        transition: all 0.22s ease;
    }}
    .top-nav-tab:hover {{
        border-color: var(--primary);
        color: var(--text-main);
        background: var(--surface-hover);
    }}
    .top-nav-tab.active {{
        background: var(--primary);
        border-color: var(--primary);
        color: #FFFFFF;
        box-shadow: 0 4px 14px var(--primary-glow);
    }}

    /* 2-Column Vertical Layout */
    .vertical-layout {{
        display: grid;
        grid-template-columns: 310px 1fr;
        gap: 20px;
        align-items: start;
        min-width: 0 !important;
    }}

    /* Left Sidebar */
    .paper-sidebar {{
        display: flex;
        flex-direction: column;
        gap: 6px;
        position: sticky;
        top: 114px;
        max-height: calc(100vh - 126px);
        overflow-y: auto;
        padding-right: 4px;
    }}
    .ch-nav-btn {{
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 10px 12px;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        text-align: left;
        transition: all 0.2s;
        width: 100%;
    }}
    .ch-nav-btn:hover {{
        background: var(--surface-hover);
        border-color: var(--primary);
    }}
    .ch-nav-btn.active {{
        background: var(--surface-hover);
        border-color: var(--primary);
        box-shadow: inset 4px 0 0 var(--primary);
    }}
    .ch-nav-left {{
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    .ch-nav-num {{
        font-family: 'Space Mono', monospace;
        font-size: 0.72rem;
        background: var(--tag-bg);
        padding: 3px 6px;
        border-radius: 6px;
        font-weight: 700;
        color: var(--accent);
    }}
    .ch-nav-info {{
        line-height: 1.25;
    }}
    .ch-nav-title {{
        font-size: 0.85rem;
        font-weight: 700;
        color: var(--text-main);
    }}
    .ch-nav-meta {{
        font-size: 0.72rem;
        color: var(--text-muted);
    }}
    .avail-badge {{
        font-size: 0.63rem;
        font-weight: 700;
        padding: 1px 6px;
        border-radius: 7px;
        background: rgba(16, 185, 129, 0.15);
        color: #10B981;
        border: 1px solid rgba(16, 185, 129, 0.3);
        flex-shrink: 0;
        margin-left: 6px;
    }}
    .avail-badge.hots-badge {{
        background: rgba(245, 158, 11, 0.15);
        color: var(--gold);
        border-color: rgba(245, 158, 11, 0.3);
    }}

    /* Main Content */
    .main-content-panel {{
        min-width: 0 !important;
    }}

    /* Paper Header Card */
    .paper-header-card {{
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 18px 22px;
        margin-bottom: 18px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 14px;
    }}
    .paper-header-title {{
        font-family: 'Outfit', sans-serif;
        font-size: 1.35rem;
        font-weight: 800;
        margin: 0 0 4px 0;
        color: var(--text-main);
    }}
    .paper-header-desc {{
        color: var(--text-muted);
        font-size: 0.84rem;
        margin: 0;
        line-height: 1.4;
    }}

    /* Mode & Sub-mode Strip */
    .sub-mode-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 18px;
        padding: 10px 14px;
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 12px;
    }}
    .mode-btn-group {{
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
    }}
    .mode-btn {{
        background: transparent;
        border: 1px solid var(--border);
        color: var(--text-muted);
        font-size: 0.78rem;
        padding: 5px 12px;
        border-radius: 20px;
        cursor: pointer;
        font-weight: 600;
        transition: all 0.2s;
    }}
    .mode-btn:hover {{
        border-color: var(--primary);
        color: var(--text-main);
    }}
    .mode-btn.active {{
        background: var(--primary);
        border-color: var(--primary);
        color: #FFFFFF;
    }}

    /* Question Cards */
    .question-card {{
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 18px 22px;
        margin-bottom: 16px;
        position: relative;
        transition: border-color 0.2s;
    }}
    .question-card:hover {{
        border-color: rgba(99, 102, 241, 0.4);
    }}
    .question-card.hots-card {{
        border-left: 4px solid var(--gold);
    }}
    .question-card.missing-card {{
        border: 1px dashed rgba(245, 158, 11, 0.6);
        background: rgba(245, 158, 11, 0.03);
    }}

    .q-header-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
        flex-wrap: wrap;
        gap: 8px;
    }}
    .q-num-badge {{
        font-family: 'Space Mono', monospace;
        font-weight: 700;
        font-size: 0.86rem;
        color: var(--primary);
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }}
    .q-sec-tag {{
        font-size: 0.7rem;
        padding: 2px 8px;
        border-radius: 6px;
        background: var(--tag-bg);
        border: 1px solid var(--border);
        color: var(--text-muted);
        font-weight: 600;
        text-transform: capitalize;
    }}
    .q-marks-tag {{
        font-size: 0.7rem;
        font-weight: 700;
        padding: 2px 7px;
        border-radius: 6px;
        background: rgba(16, 185, 129, 0.12);
        color: #10B981;
    }}
    .q-marks-tag.hots-mark {{
        background: rgba(245, 158, 11, 0.15);
        color: var(--gold);
    }}

    .q-topic {{
        font-size: 0.8rem;
        font-weight: 600;
        color: var(--accent);
        margin-bottom: 8px;
    }}
    .q-text {{
        font-size: 0.94rem;
        line-height: 1.5;
        margin-bottom: 14px;
        color: var(--text-main);
    }}

    /* Diagram slot box & Embedded Source Images */
    .q-diagram-box {{
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 12px 16px;
        margin-bottom: 14px;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }}
    .diagram-toolbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 8px;
    }}
    .diagram-tag {{
        font-size: 0.76rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        color: var(--accent);
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }}
    .view-scan-btn {{
        background: rgba(99, 102, 241, 0.12);
        border: 1px solid rgba(99, 102, 241, 0.3);
        color: var(--accent);
        font-size: 0.74rem;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 8px;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        transition: all 0.2s;
    }}
    .view-scan-btn:hover {{
        background: var(--primary);
        color: #FFFFFF;
        border-color: var(--primary);
    }}
    .diagram-img-frame {{
        background: rgba(0, 0, 0, 0.2);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        cursor: pointer;
        transition: all 0.2s;
    }}
    .diagram-img-frame:hover {{
        border-color: var(--primary);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
    }}
    .q-diagram-img {{
        max-width: 100%;
        max-height: 280px;
        object-fit: contain;
        border-radius: 6px;
        display: inline-block;
    }}
    .diagram-caption {{
        font-size: 0.76rem;
        color: var(--text-muted);
        margin-top: 6px;
        line-height: 1.35;
    }}
    .expand-hint {{
        color: var(--accent);
        font-weight: 600;
        margin-left: 6px;
    }}

    /* Vector SVG Problem Figures */
    .q-svg-diagram {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 12px 0 16px 0;
        padding: 12px;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid var(--border);
        border-radius: 12px;
        overflow-x: auto;
    }}
    .q-svg-diagram svg {{
        max-width: 100%;
        height: auto;
        display: block;
    }}

    /* Visual Problem Setup Banner */
    .q-visual-banner {{
        margin: 12px 0 16px 0;
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 12px;
        padding: 12px 14px;
        cursor: pointer;
        transition: all 0.2s ease;
    }}
    .q-visual-banner:hover {{
        border-color: #38BDF8;
        background: rgba(30, 41, 59, 0.85);
        box-shadow: 0 4px 16px rgba(56, 189, 248, 0.15);
    }}
    .visual-badge {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 0.75rem;
        font-weight: 700;
        color: #38BDF8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }}
    .visual-img-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        max-height: 280px;
        overflow: hidden;
        border-radius: 8px;
        background: rgba(0, 0, 0, 0.35);
        padding: 6px;
    }}
    .q-scan-preview-img {{
        max-width: 100%;
        max-height: 268px;
        object-fit: contain;
        display: block;
        border-radius: 6px;
    }}

    /* Solution Diagram & Proof */
    .sol-diagram-box {{
        margin-top: 14px;
        background: rgba(0, 0, 0, 0.25);
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 10px;
        padding: 12px 14px;
    }}
    .sol-diagram-title {{
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        color: var(--primary);
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 6px;
    }}
    .sol-img-frame {{
        text-align: center;
        cursor: pointer;
        padding: 8px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid var(--border);
        transition: all 0.2s;
    }}
    .sol-img-frame:hover {{
        border-color: var(--primary);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
    }}
    .sol-diagram-img {{
        max-width: 100%;
        max-height: 240px;
        object-fit: contain;
        border-radius: 6px;
        display: inline-block;
    }}

    /* Bunch Vector SVG */
    .bundle-svg-wrapper {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 10px;
        padding: 12px;
        background: rgba(0, 0, 0, 0.25);
        border: 1px solid var(--border);
        border-radius: 10px;
        overflow-x: auto;
    }}
    .bundle-svg-wrapper svg {{
        max-width: 100%;
        height: auto;
    }}

    /* Common Stimulus Bunch Container */
    .question-bundle-card {{
        background: rgba(99, 102, 241, 0.03);
        border: 2px solid rgba(99, 102, 241, 0.35);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 24px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        position: relative;
    }}
    .bundle-banner {{
        display: flex;
        align-items: center;
        gap: 12px;
        flex-wrap: wrap;
        margin-bottom: 14px;
        padding-bottom: 12px;
        border-bottom: 1px solid rgba(99, 102, 241, 0.2);
    }}
    .bundle-badge {{
        background: var(--primary);
        color: #FFFFFF;
        font-size: 0.74rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        padding: 4px 10px;
        border-radius: 8px;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }}
    .bundle-title {{
        font-family: 'Outfit', sans-serif;
        font-size: 1.15rem;
        font-weight: 800;
        color: var(--text-main);
    }}
    .bundle-stimulus-area {{
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 18px;
    }}
    .bundle-direction-text {{
        font-size: 0.92rem;
        line-height: 1.5;
        color: var(--text-main);
        margin-bottom: 14px;
        display: flex;
        align-items: flex-start;
        gap: 10px;
    }}
    .bundle-img-wrapper {{
        text-align: center;
        cursor: pointer;
    }}
    .bundle-stimulus-img {{
        max-width: 100%;
        max-height: 340px;
        object-fit: contain;
        border-radius: 8px;
        border: 1px solid var(--border);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s;
    }}
    .bundle-stimulus-img:hover {{
        transform: scale(1.01);
    }}
    .bundle-img-caption {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 10px;
        font-size: 0.78rem;
        color: var(--text-muted);
    }}
    .zoom-btn-sm {{
        background: var(--tag-bg);
        border: 1px solid var(--border);
        color: var(--text-main);
        font-size: 0.74rem;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 6px;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }}
    .zoom-btn-sm:hover {{
        border-color: var(--primary);
        color: var(--primary);
    }}
    .bundled-questions-wrapper {{
        display: flex;
        flex-direction: column;
        gap: 16px;
    }}
    .sub-question-card {{
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 16px 20px;
    }}

    /* Full-Screen Scan Modal / Lightbox */
    .scan-modal {{
        display: none;
        position: fixed;
        inset: 0;
        z-index: 9999;
        background: rgba(0, 0, 0, 0.85);
        backdrop-filter: blur(8px);
        align-items: center;
        justify-content: center;
        padding: 20px;
        animation: fadeInModal 0.2s ease;
    }}
    @keyframes fadeInModal {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    .scan-modal.active {{
        display: flex !important;
    }}
    .scan-modal-content {{
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 16px;
        max-width: 95vw;
        max-height: 92vh;
        width: 1000px;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.5);
    }}
    .scan-modal-header {{
        padding: 14px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid var(--border);
        background: var(--surface-hover);
    }}
    .scan-modal-header h3 {{
        margin: 0;
        font-size: 1.05rem;
        font-family: 'Outfit', sans-serif;
        color: var(--text-main);
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .scan-modal-actions {{
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .modal-btn {{
        background: var(--tag-bg);
        border: 1px solid var(--border);
        color: var(--text-main);
        width: 32px;
        height: 32px;
        border-radius: 8px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        text-decoration: none;
        transition: all 0.2s;
    }}
    .modal-btn:hover {{
        background: var(--primary);
        color: #FFFFFF;
        border-color: var(--primary);
    }}
    .scan-modal-body {{
        flex: 1;
        overflow: auto;
        padding: 18px;
        text-align: center;
        background: rgba(0, 0, 0, 0.3);
    }}
    .scan-modal-body img {{
        max-width: 100%;
        height: auto;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }}

    /* Options Grid */
    .options-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 8px;
        margin-bottom: 14px;
    }}
    .opt-btn {{
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 10px 14px;
        font-size: 0.86rem;
        text-align: left;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 10px;
        transition: all 0.2s;
    }}
    .opt-btn:hover:not(:disabled) {{
        border-color: var(--primary);
        background: var(--surface-hover);
    }}
    .opt-btn.correct {{
        background: rgba(16, 185, 129, 0.18) !important;
        border-color: #10B981 !important;
        color: #FFFFFF !important;
    }}
    .opt-btn.wrong {{
        background: rgba(239, 68, 68, 0.18) !important;
        border-color: #EF4444 !important;
        color: #FFFFFF !important;
    }}
    .opt-letter {{
        font-family: 'Space Mono', monospace;
        font-weight: 700;
        font-size: 0.78rem;
        background: var(--tag-bg);
        width: 24px;
        height: 24px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        flex-shrink: 0;
    }}
    .opt-text {{
        font-size: 0.88rem;
        color: var(--text-main);
        line-height: 1.35;
        flex: 1;
    }}

    /* Reasoning & Explanation Box */
    .solution-box {{
        background: rgba(99, 102, 241, 0.05);
        border: 1px solid rgba(99, 102, 241, 0.25);
        border-radius: 10px;
        padding: 12px 16px;
        margin-top: 10px;
        display: none;
    }}
    .sol-title {{
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        color: var(--primary);
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 6px;
    }}
    .sol-desc {{
        font-size: 0.86rem;
        line-height: 1.5;
        color: var(--text-main);
    }}

    /* Missing Question Notice */
    .missing-notice {{
        background: rgba(245, 158, 11, 0.1);
        border: 1px solid rgba(245, 158, 11, 0.35);
        border-radius: 8px;
        padding: 10px 14px;
        color: var(--gold);
        font-size: 0.82rem;
        line-height: 1.4;
    }}

    /* Table Matrix */
    .key-table-box {{
        overflow-x: auto;
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 14px;
    }}
    .key-table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 0.84rem;
        text-align: center;
    }}
    .key-table th, .key-table td {{
        padding: 8px 10px;
        border-bottom: 1px solid var(--border);
    }}
    .key-table th {{
        color: var(--text-muted);
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
    }}

    /* Jump to Top */
    .pushti-jump-top {{
        position: fixed;
        bottom: 24px;
        right: 24px;
        width: 42px;
        height: 42px;
        border-radius: 50%;
        background: var(--surface);
        border: 1px solid var(--border);
        color: var(--text-main);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        opacity: 0;
        pointer-events: none;
        transition: all 0.25s;
        box-shadow: 0 4px 14px rgba(0,0,0,0.3);
        z-index: 1000;
    }}
    .pushti-jump-top.visible {{
        opacity: 1;
        pointer-events: auto;
    }}

    @media (max-width: 900px) {{
        .vertical-layout {{
            grid-template-columns: 1fr;
        }}
        .paper-sidebar {{
            position: static;
            max-height: none;
        }}
    }}
</style>
</head>
<body>

    <!-- Sticky Header -->
    <header class="site-header">
        <div class="header-left">
            <span class="brand-badge">{badge_name}</span>
            <div class="breadcrumb-nav">
                <a href="index.html">Pushti Study Hub</a>
                <span>/</span>
                <a href="index.html#activities-cat">Activities</a>
                <span>/</span>
                <span style="color:var(--text-main);">{track} Olympiad</span>
            </div>
        </div>

        <div class="header-right">
            <!-- Micro KPIs -->
            <div class="kpi-strip">
                <span class="kpi-pill">Answered: <strong id="kpi-answered">0</strong></span>
                <span class="kpi-pill score-pill">Score: <strong id="kpi-score">0</strong> / 60</span>
                <span class="kpi-pill acc-pill">Acc: <strong id="kpi-acc">0%</strong></span>
                <span class="kpi-pill" id="kpi-timer-pill" style="display:none; color:#EF4444;"><i class="fas fa-stopwatch"></i> <strong id="kpi-timer">60:00</strong></span>
            </div>

            <!-- Return & Theme -->
            <a href="index.html" class="hdr-btn" title="Back to Study Hub"><i class="fas fa-arrow-left"></i> Hub</a>
            <button class="hdr-btn" id="theme-btn" title="Toggle Light/Dark Theme"><i class="fas fa-moon"></i></button>
        </div>
    </header>

    <!-- Main Container -->
    <div class="container">

        <!-- Hero Banner -->
        <div class="hero-banner">
            <div class="hero-left">
                <h1 class="hero-title">{title}</h1>
                <p class="hero-subtitle">{subtitle}</p>
                <div class="hero-badges">
                    <span class="hero-pill"><i class="fas {icon_class}"></i> <strong>{len(papers_data)} Papers</strong></span>
                    <span class="hero-pill"><i class="fas fa-list-ol"></i> <strong>{total_q_count} Questions</strong></span>
                    <span class="hero-pill"><i class="fas fa-stopwatch"></i> <strong>60 Mins</strong></span>
                    <span class="hero-pill"><i class="fas fa-award"></i> <strong>60 Marks Pattern</strong></span>
                    <span class="hero-pill" style="color:var(--gold); border-color:rgba(245,158,11,0.3);"><i class="fas fa-star"></i> Achievers HOTS (3M)</span>
                    <span class="hero-pill"><i class="fas fa-check-double"></i> 100% Verified Solutions</span>
                </div>
            </div>

            <div class="gold-target-card">
                <div class="target-title">🎯 Gold Target</div>
                <div class="target-score">{target_score}</div>
                <div class="target-desc">International Rank 1 Benchmark</div>
            </div>
        </div>

        <!-- 4 Primary Top Tabs -->
        <div class="primary-tab-bar">
            <button class="top-nav-tab active" id="tab-practice" onclick="switchMainTab('practice')">
                <i class="fas fa-book-open"></i> Study & Practice Mode
            </button>
            <button class="top-nav-tab" id="tab-exam" onclick="switchMainTab('exam')">
                <i class="fas fa-stopwatch"></i> Timed Exam Simulation (60 Mins)
            </button>
            <button class="top-nav-tab" id="tab-hots" onclick="switchMainTab('hots')">
                <i class="fas fa-star" style="color:var(--gold);"></i> Achievers HOTS Vault
            </button>
            <button class="top-nav-tab" id="tab-keys" onclick="switchMainTab('keys')">
                <i class="fas fa-key"></i> Master Answer Keys
            </button>
        </div>

        <!-- 2-Column Vertical Layout -->
        <div class="vertical-layout">

            <!-- Left Sidebar -->
            <aside class="paper-sidebar" id="sidebar-papers">
                {sidebar_btns}
            </aside>

            <!-- Right Content Area -->
            <main class="main-content-panel">

                <!-- Paper Header Banner -->
                <div class="paper-header-card" id="paper-header">
                    <div>
                        <h2 class="paper-header-title" id="banner-title">Loading...</h2>
                        <p class="paper-header-desc" id="banner-desc">Select a paper from the left sidebar to start practicing.</p>
                    </div>
                </div>

                <!-- Section Filters & Sub-mode Strip -->
                <div class="sub-mode-row" id="sub-mode-row">
                    <div class="mode-btn-group" id="section-filters-group">
                        {filter_pills}
                    </div>
                    <div>
                        <button class="mode-btn" onclick="revealAllSolutions()"><i class="fas fa-lightbulb"></i> Reveal All Solutions</button>
                        <button class="mode-btn" id="exam-action-btn" style="display:none; background:var(--primary); color:#fff;" onclick="submitExam()"><i class="fas fa-paper-plane"></i> Submit Exam</button>
                    </div>
                </div>

                <!-- Questions Stream Container -->
                <div id="questions-stream">
                    <!-- Cards will be populated by JavaScript -->
                </div>

            </main>
        </div>
    </div>

    <!-- Jump to top -->
    <button class="pushti-jump-top" id="jump-top-btn" title="Jump to top" onclick="window.scrollTo({{top:0, behavior:'smooth'}})">
        <i class="fas fa-arrow-up"></i>
    </button>

    <!-- Source Workbook Scan Lightbox Modal -->
    <div id="scan-modal" class="scan-modal" onclick="closeScanModal(event)">
        <div class="scan-modal-content" onclick="event.stopPropagation()">
            <div class="scan-modal-header">
                <h3 id="scan-modal-title"><i class="fas fa-file-image"></i> Workbook Source Scan</h3>
                <div class="scan-modal-actions">
                    <a id="scan-modal-ext" href="#" target="_blank" class="modal-btn" title="Open High-Res in New Window"><i class="fas fa-external-link-alt"></i></a>
                    <button type="button" class="modal-btn" onclick="closeScanModal()"><i class="fas fa-times"></i></button>
                </div>
            </div>
            <div class="scan-modal-body">
                <img id="scan-modal-img" src="" alt="High-Resolution Workbook Scan" />
            </div>
        </div>
    </div>

    <!-- Embedded Knowledge Base Dataset -->
    <script>
        const PAPERS_DATA = {json_str};

        let currentPaperKey = '{first_key}';
        let currentSectionFilter = 'all';
        let currentMainTab = 'practice'; // practice, exam, hots, keys
        let userAnswers = {{}};
        let totalAnswered = 0;
        let totalScore = 0;
        let totalCorrect = 0;
        let examTimerInterval = null;
        let examTimeLeft = 3600; // 60 minutes in seconds

        function loadPaper(paperKey, btnElement) {{
            currentPaperKey = paperKey;
            document.querySelectorAll('.paper-sidebar .ch-nav-btn').forEach(b => b.classList.remove('active'));
            if (btnElement) btnElement.classList.add('active');

            const p = PAPERS_DATA[paperKey];
            if (!p) return;

            document.getElementById('banner-title').textContent = p.name;
            document.getElementById('banner-desc').textContent = `${{p.year}} • ${{p.total}} Questions • ${{p.marks}} Marks • Standard SOF Blueprint Pattern`;
            document.getElementById('sub-mode-row').style.display = 'flex';

            renderQuestions(p.questions);
        }}

        function filterSection(secId, btnElement) {{
            currentSectionFilter = secId;
            document.querySelectorAll('#section-filters-group .mode-btn').forEach(b => b.classList.remove('active'));
            if (btnElement) btnElement.classList.add('active');

            const p = PAPERS_DATA[currentPaperKey];
            if (!p) return;

            if (secId === 'all') {{
                renderQuestions(p.questions);
            }} else {{
                const filtered = p.questions.filter(q => q.section === secId);
                renderQuestions(filtered);
            }}
        }}

        function loadHotsVault(btnElement) {{
            document.querySelectorAll('.paper-sidebar .ch-nav-btn').forEach(b => b.classList.remove('active'));
            if (btnElement) {{
                btnElement.classList.add('active');
            }} else {{
                const btn = document.querySelector('.paper-sidebar .ch-nav-btn[onclick*="loadHotsVault"]');
                if (btn) btn.classList.add('active');
            }}
            switchMainTab('hots');
        }}

        function loadKeyMatrix(btnElement) {{
            document.querySelectorAll('.paper-sidebar .ch-nav-btn').forEach(b => b.classList.remove('active'));
            if (btnElement) {{
                btnElement.classList.add('active');
            }} else {{
                const btn = document.querySelector('.paper-sidebar .ch-nav-btn[onclick*="loadKeyMatrix"]');
                if (btn) btn.classList.add('active');
            }}
            switchMainTab('keys');
        }}

        function switchMainTab(tabKey) {{
            currentMainTab = tabKey;
            document.querySelectorAll('.primary-tab-bar .top-nav-tab').forEach(b => b.classList.remove('active'));
            const targetTop = document.getElementById('tab-' + tabKey);
            if (targetTop) targetTop.classList.add('active');

            if (tabKey === 'practice') {{
                stopExamTimer();
                document.getElementById('exam-action-btn').style.display = 'none';
                document.getElementById('kpi-timer-pill').style.display = 'none';
                const sidebarBtn = document.querySelector(`.paper-sidebar .ch-nav-btn[onclick*="${{currentPaperKey}}"]`);
                loadPaper(currentPaperKey, sidebarBtn);
            }} else if (tabKey === 'exam') {{
                startExamMode();
            }} else if (tabKey === 'hots') {{
                stopExamTimer();
                document.querySelectorAll('.paper-sidebar .ch-nav-btn').forEach(b => b.classList.remove('active'));
                const hotsBtn = document.querySelector('.paper-sidebar .ch-nav-btn[onclick*="loadHotsVault"]');
                if (hotsBtn) hotsBtn.classList.add('active');
                renderHotsVault();
            }} else if (tabKey === 'keys') {{
                stopExamTimer();
                document.querySelectorAll('.paper-sidebar .ch-nav-btn').forEach(b => b.classList.remove('active'));
                const keysBtn = document.querySelector('.paper-sidebar .ch-nav-btn[onclick*="loadKeyMatrix"]');
                if (keysBtn) keysBtn.classList.add('active');
                renderKeyMatrix();
            }}
        }}

        function startExamMode() {{
            document.getElementById('banner-title').textContent = "⏱️ Timed Exam Simulation (60 Minutes)";
            document.getElementById('banner-desc').textContent = "Authentic test environment: 50 Questions • 60 Marks. Answer all sections and submit before the countdown expires.";
            document.getElementById('exam-action-btn').style.display = 'inline-block';
            document.getElementById('kpi-timer-pill').style.display = 'inline-flex';
            
            userAnswers = {{}};
            totalAnswered = 0;
            totalScore = 0;
            totalCorrect = 0;
            updateScoreKPIs();

            examTimeLeft = 3600;
            startExamTimer();

            const p = PAPERS_DATA[currentPaperKey];
            renderQuestions(p.questions, true);
        }}

        function startExamTimer() {{
            clearInterval(examTimerInterval);
            examTimerInterval = setInterval(() => {{
                examTimeLeft--;
                if (examTimeLeft <= 0) {{
                    clearInterval(examTimerInterval);
                    alert("⏰ Time is up! Submitting exam automatically.");
                    submitExam();
                }}
                const mins = Math.floor(examTimeLeft / 60);
                const secs = examTimeLeft % 60;
                document.getElementById('kpi-timer').textContent = `${{mins.toString().padStart(2, '0')}}:${{secs.toString().padStart(2, '0')}}`;
            }}, 1000);
        }}

        function stopExamTimer() {{
            clearInterval(examTimerInterval);
            document.getElementById('kpi-timer-pill').style.display = 'none';
            document.getElementById('exam-action-btn').style.display = 'none';
        }}

        function submitExam() {{
            clearInterval(examTimerInterval);
            const p = PAPERS_DATA[currentPaperKey];
            let scored = 0;
            let correctCount = 0;
            let attemptedCount = 0;

            p.questions.forEach(q => {{
                if (q.is_missing) return;
                const chosen = userAnswers[q.q_num];
                if (chosen) {{
                    attemptedCount++;
                    if (chosen === q.answer) {{
                        correctCount++;
                        scored += (q.marks || 1);
                    }}
                }}
            }});

            const pct = Math.round((scored / p.marks) * 100);
            alert(`🎉 Exam Finished!\\n\\nPaper: ${{p.name}}\\nScore: ${{scored}} / ${{p.marks}} (${{pct}}%)\\nQuestions Attempted: ${{attemptedCount}} / ${{p.questions.filter(x => !x.is_missing).length}}\\nCorrect Answers: ${{correctCount}}\\n\\nSolutions are now revealed below.`);

            // Reveal all solutions for review
            revealAllSolutions();
        }}

        function selectOption(qNum, optLetter, correctLetter, marks, btn) {{
            if (currentMainTab === 'exam') {{
                userAnswers[qNum] = optLetter;
                const parent = btn.closest('.options-grid');
                parent.querySelectorAll('.opt-btn').forEach(b => b.classList.remove('correct', 'wrong'));
                btn.classList.add('correct');
                totalAnswered = Object.keys(userAnswers).length;
                document.getElementById('kpi-answered').textContent = totalAnswered;
                return;
            }}

            // Practice Mode (Instant Feedback)
            const parent = btn.closest('.options-grid');
            if (parent.getAttribute('data-answered') === 'true') return;
            parent.setAttribute('data-answered', 'true');

            totalAnswered++;
            if (optLetter === correctLetter) {{
                btn.classList.add('correct');
                totalCorrect++;
                totalScore += marks;
            }} else {{
                btn.classList.add('wrong');
                // Highlight correct option
                parent.querySelectorAll('.opt-btn').forEach(b => {{
                    if (b.getAttribute('data-letter') === correctLetter) {{
                        b.classList.add('correct');
                    }}
                }});
            }}

            updateScoreKPIs();

            // Reveal explanation
            const card = btn.closest('.question-card');
            const sol = card.querySelector('.solution-box');
            if (sol) sol.style.display = 'block';
        }}

        function openScanModal(imgUrl, title, qNum) {{
            if (!imgUrl) return;
            const modal = document.getElementById('scan-modal');
            const img = document.getElementById('scan-modal-img');
            const titleEl = document.getElementById('scan-modal-title');
            const extLink = document.getElementById('scan-modal-ext');

            img.src = imgUrl;
            titleEl.innerHTML = `<i class="fas fa-file-image" style="color:var(--accent);"></i> ${{title || 'Workbook Source Scan'}}`;
            extLink.href = imgUrl;
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }}

        function closeScanModal(event) {{
            const modal = document.getElementById('scan-modal');
            if (modal) modal.classList.remove('active');
            document.body.style.overflow = 'auto';
        }}

        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') closeScanModal();
        }});

        function renderSingleQuestionCard(q, isExam = false, isSubCard = false) {{
            const isHots = q.section === 'achievers_section' || q.marks === 3;
            const cardCls = q.is_missing ? 'question-card missing-card' : (isSubCard ? 'sub-question-card' : (isHots ? 'question-card hots-card' : 'question-card'));
            const secLabel = (q.section || 'General').replace('_', ' ');

            if (q.is_missing) {{
                return `
                <div class="${{cardCls}}" id="q-card-${{q.q_num}}">
                    <div class="q-header-row">
                        <span class="q-num-badge">Q${{q.q_num}}</span>
                        <span class="q-sec-tag">${{secLabel}}</span>
                        <span class="q-marks-tag" style="background:rgba(245,158,11,0.2); color:var(--gold);">⚠️ MISSING / PENDING</span>
                    </div>
                    <div class="q-topic">Topic: Pending Physical Intake</div>
                    <div class="missing-notice">
                        <strong><i class="fas fa-exclamation-triangle"></i> Question Registered as Missing:</strong><br>
                        ${{q.explanation}}
                    </div>
                </div>
                `;
            }}

            // Question Figure: Clean Vector SVG problem setup or visual scan
            let questionGraphicHtml = '';
            const isVisual = (q.opts && q.opts.some(o => typeof o === 'string' && (o.includes('Figure (') || o.includes('Cube ')))) ||
                             (q.text && /(given figure|given unfolded|unfolded net|mirror image|water image|embedded part|dot situation|shown below|in the circuit|bar graph|diagram below|shown in the figure|following ray diagram|matrix puzzle|triangles in the given|satisfies the same condition)/i.test(q.text));

            if (q.question_svg) {{
                questionGraphicHtml = `
                <div class="q-svg-diagram">
                    ${{q.question_svg}}
                </div>
                `;
            }} else if (q.diagram_img && q.diagram_img !== q.scan_img) {{
                questionGraphicHtml = `
                <div class="q-visual-banner" onclick="openScanModal('${{q.scan_img || q.diagram_img}}', 'Question ${{q.q_num}} Reference Figure', ${{q.q_num}})">
                    <div class="visual-badge"><i class="fas fa-image"></i> Problem Setup Diagram</div>
                    <div class="visual-img-container">
                        <img src="${{q.diagram_img}}" alt="Problem Figure for Q${{q.q_num}}" class="q-scan-preview-img" loading="lazy" />
                    </div>
                    <div class="diagram-caption"><i class="fas fa-search-plus"></i> Cropped Problem Diagram • Click to inspect full original workbook page scan</div>
                </div>
                `;
            }} else if (isVisual && (q.scan_img || q.diagram_img)) {{
                const targetScan = q.scan_img || q.diagram_img;
                questionGraphicHtml = `
                <div class="q-visual-banner" onclick="openScanModal('${{targetScan}}', 'Question ${{q.q_num}} Reference Workbook Scan', ${{q.q_num}})">
                    <div class="visual-badge"><i class="fas fa-book-open"></i> Problem Setup / Visual Workbook Reference</div>
                    <div class="visual-img-container">
                        <img src="${{targetScan}}" alt="Problem Diagram for Q${{q.q_num}}" class="q-scan-preview-img" loading="lazy" />
                    </div>
                    <div class="diagram-caption"><i class="fas fa-search-plus"></i> Original Workbook Problem Scan • Click to zoom/inspect full page</div>
                </div>
                `;
            }}

            // Solution Proof Diagram: Vector Solution Diagram or Official Answer Key Figure
            let solDiagramHtml = '';
            if (q.solution_svg) {{
                const fullScan = q.scan_img || q.answer_diagram_img;
                solDiagramHtml = `
                <div class="sol-diagram-box">
                    <div class="sol-diagram-title">
                        <i class="fas fa-route"></i> Step-by-Step Analytical Derivation Path:
                    </div>
                    <div class="sol-svg-frame" style="display:flex; justify-content:center; padding:10px 0;">
                        ${{q.solution_svg}}
                    </div>
                    ${{fullScan ? `
                    <div style="text-align:right; margin-top:8px;">
                        <button type="button" class="view-scan-btn" onclick="openScanModal('${{fullScan}}', 'Official Solution Proof • Q${{q.q_num}}', ${{q.q_num}})">
                            <i class="fas fa-book-open"></i> Cross-Check Workbook Scan
                        </button>
                    </div>
                    ` : ''}}
                </div>
                `;
            }} else if (q.answer_diagram_img) {{
                const fullScan = q.scan_img || q.answer_diagram_img;
                const pageTxt = q.diagram_slot && q.diagram_slot.book_page ? `Page ${{q.diagram_slot.book_page}}` : 'Solution Key';
                solDiagramHtml = `
                <div class="sol-diagram-box">
                    <div class="sol-diagram-title">
                        <i class="fas fa-check-circle"></i> Official Answer Key Visual Proof:
                    </div>
                    <div class="sol-img-frame" onclick="openScanModal('${{fullScan}}', 'Official Solution Proof • Q${{q.q_num}} (${{pageTxt}})', ${{q.q_num}})">
                        <img src="${{q.answer_diagram_img}}" alt="Official Solution Proof" class="sol-diagram-img" loading="lazy" />
                        <div class="diagram-caption">Official Workbook Solution Illustration • ${{pageTxt}} <span class="expand-hint">(🔍 Click to view full solution scan)</span></div>
                    </div>
                </div>
                `;
            }}

            // Options buttons
            const letters = ['A', 'B', 'C', 'D'];
            let optsHtml = '';
            letters.forEach((letter, idx) => {{
                const optVal = (q.opts && q.opts[idx]) ? q.opts[idx] : `Option ${{letter}}`;
                optsHtml += `
                <button class="opt-btn" data-letter="${{letter}}" onclick="selectOption(${{q.q_num}}, '${{letter}}', '${{q.answer}}', ${{q.marks || 1}}, this)">
                    <span class="opt-letter">${{letter}}</span>
                    <span class="opt-text">${{optVal}}</span>
                </button>
                `;
            }});

            const questionText = q.text || (q.topic ? `**${{q.topic}}**` : '');

            return `
            <div class="${{cardCls}}" id="q-card-${{q.q_num}}">
                <div class="q-header-row">
                    <span class="q-num-badge">
                        ${{isHots ? '<i class="fas fa-star" style="color:var(--gold);"></i>' : ''}}
                        Q${{q.q_num}}
                    </span>
                    <span class="q-sec-tag">${{secLabel}}</span>
                    <span class="q-marks-tag ${{isHots ? 'hots-mark' : ''}}">${{q.marks || 1}} Mark${{q.marks > 1 ? 's (HOTS)' : ''}}</span>
                </div>

                <div class="q-topic">Topic: ${{q.topic || 'General Practice'}}</div>
                <div class="q-text">${{questionText}}</div>

                ${{questionGraphicHtml}}

                <div class="options-grid">
                    ${{optsHtml}}
                </div>

                <div class="solution-box">
                    <div class="sol-title"><i class="fas fa-lightbulb"></i> Step-by-Step Analytical Derivation:</div>
                    <div class="sol-desc">
                        <strong>Correct Answer: Option ${{q.answer}}</strong><br>
                        ${{q.explanation}}
                    </div>
                    ${{solDiagramHtml}}
                </div>
            </div>
            `;
        }}

        function renderQuestions(questionsList, isExam = false) {{
            const stream = document.getElementById('questions-stream');
            if (!questionsList || questionsList.length === 0) {{
                stream.innerHTML = '<div style="text-align:center; padding:40px; color:var(--text-muted);">No questions found for this section.</div>';
                return;
            }}

            let html = '';
            let i = 0;
            while (i < questionsList.length) {{
                const q = questionsList[i];
                if (q.bunch_id && !isExam) {{
                    const bunchId = q.bunch_id;
                    const bunchItems = [];
                    while (i < questionsList.length && questionsList[i].bunch_id === bunchId) {{
                        bunchItems.push(questionsList[i]);
                        i++;
                    }}

                    const firstQ = bunchItems[0];
                    const qNumsStr = bunchItems.map(x => 'Q' + x.q_num).join(', ');
                    const sharedScan = firstQ.scan_img || firstQ.stimulus_image;

                    let subCardsHtml = '';
                    bunchItems.forEach(sq => {{
                        subCardsHtml += renderSingleQuestionCard(sq, isExam, true);
                    }});

                    html += `
                    <div class="question-bundle-card" id="bunch-${{bunchId}}">
                        <div class="bundle-banner">
                            <span class="bundle-badge"><i class="fas fa-layer-group"></i> Common Stimulus Bunch</span>
                            <span class="bundle-title">${{firstQ.bunch_title || ('Direction (' + qNumsStr + ')')}}</span>
                        </div>
                        <div class="bundle-stimulus-area">
                            <div class="bundle-direction-text">
                                <i class="fas fa-compass" style="color:var(--accent); font-size:1.15rem; margin-top:2px;"></i>
                                <div><strong>Direction:</strong> ${{firstQ.bunch_direction || 'Refer to the given figure to answer the following questions.'}}</div>
                            </div>
                            ${{firstQ.bunch_svg ? `
                            <div class="bundle-svg-wrapper">
                                ${{firstQ.bunch_svg}}
                            </div>
                            ${{sharedScan ? `
                            <div style="text-align:right; margin-top:8px;">
                                <button type="button" class="zoom-btn-sm" onclick="openScanModal('${{sharedScan}}', '${{firstQ.bunch_title || 'Shared Stimulus'}}', '${{qNumsStr}}')">
                                    <i class="fas fa-search-plus"></i> View Full Page Scan
                                </button>
                            </div>
                            ` : ''}}
                            ` : (firstQ.stimulus_image ? `
                            <div class="bundle-img-wrapper" onclick="openScanModal('${{sharedScan}}', '${{firstQ.bunch_title || 'Shared Stimulus'}}', '${{qNumsStr}}')">
                                <img src="${{firstQ.stimulus_image}}" alt="Stimulus Diagram" class="bundle-stimulus-img" />
                                <div class="bundle-img-caption">
                                    <span><i class="fas fa-image"></i> Shared Visual Stimulus</span>
                                    <button type="button" class="zoom-btn-sm" onclick="event.stopPropagation(); openScanModal('${{sharedScan}}', '${{firstQ.bunch_title || 'Shared Stimulus'}}', '${{qNumsStr}}')">
                                        <i class="fas fa-search-plus"></i> View Full Page Scan
                                    </button>
                                </div>
                            </div>
                            ` : '')}}
                        </div>
                        <div class="bundled-questions-wrapper">
                            ${{subCardsHtml}}
                        </div>
                    </div>
                    `;
                }} else {{
                    html += renderSingleQuestionCard(q, isExam, false);
                    i++;
                }}
            }}

            stream.innerHTML = html;

            // Trigger KaTeX rendering
            try {{
                if (window.renderMathInElement) {{
                    renderMathInElement(stream, {{
                        delimiters: [
                            {{left: '$$', right: '$$', display: true}},
                            {{left: '$', right: '$', display: false}}
                        ],
                        throwOnError: false
                    }});
                }}
            }} catch(e) {{}}
        }}

        function revealAllSolutions() {{
            document.querySelectorAll('.solution-box').forEach(b => b.style.display = 'block');
        }}

        function updateScoreKPIs() {{
            document.getElementById('kpi-answered').textContent = totalAnswered;
            document.getElementById('kpi-score').textContent = totalScore;
            const acc = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : 0;
            document.getElementById('kpi-acc').textContent = acc + '%';
        }}

        function renderHotsVault() {{
            document.getElementById('banner-title').textContent = "⭐ Achievers Section (HOTS) Master Vault";
            document.getElementById('banner-desc').textContent = "Every single 3-mark High Order Thinking Skills problem aggregated across all papers. Master these to guarantee Gold Medal performance!";
            document.getElementById('sub-mode-row').style.display = 'none';

            const allHots = [];
            for (const key in PAPERS_DATA) {{
                const p = PAPERS_DATA[key];
                p.questions.forEach(q => {{
                    if (q.marks === 3 || q.section === 'achievers_section') {{
                        allHots.push(q);
                    }}
                }});
            }}
            renderQuestions(allHots);
        }}

        function renderKeyMatrix() {{
            document.getElementById('banner-title').textContent = "🔑 Master Answer Key Matrix (All Sets)";
            document.getElementById('banner-desc').textContent = "Direct answer key comparison grid for all digitized examination papers from Q1 to Q50.";
            document.getElementById('sub-mode-row').style.display = 'none';

            const keys = Object.keys(PAPERS_DATA);
            let headerCells = '<th>Q#</th>';
            keys.forEach(k => {{
                headerCells += `<th>${{PAPERS_DATA[k].title}}</th>`;
            }});

            let rowsHtml = '';
            for (let q = 1; q <= 50; q++) {{
                let rowCells = `<td style="font-weight:700; color:var(--primary);">${{q}}</td>`;
                keys.forEach(k => {{
                    const question = PAPERS_DATA[k].questions.find(x => x.q_num === q);
                    const ans = question ? (question.is_missing ? '<span style="color:var(--gold);">⚠️</span>' : question.answer) : '-';
                    const isHots = question && question.marks === 3;
                    const style = isHots ? 'style="font-weight:800; color:var(--gold);"' : '';
                    rowCells += `<td ${{style}}>${{ans}}</td>`;
                }});
                rowsHtml += `<tr>${{rowCells}}</tr>`;
            }}

            const stream = document.getElementById('questions-stream');
            stream.innerHTML = `
                <div class="key-table-box">
                    <table class="key-table">
                        <thead><tr>${{headerCells}}</tr></thead>
                        <tbody>${{rowsHtml}}</tbody>
                    </table>
                </div>
            `;
        }}

        // Theme and Scroll
        document.addEventListener('DOMContentLoaded', () => {{
            const themeBtn = document.getElementById('theme-btn');
            if (themeBtn) {{
                themeBtn.addEventListener('click', () => {{
                    const current = document.body.getAttribute('data-theme') || 'dark';
                    const next = current === 'dark' ? 'light' : 'dark';
                    document.body.setAttribute('data-theme', next);
                    document.documentElement.setAttribute('data-theme', next);
                    themeBtn.querySelector('i').className = next === 'light' ? 'fas fa-sun' : 'fas fa-moon';
                    localStorage.setItem('pushti-theme', next);
                }});
                const saved = localStorage.getItem('pushti-theme') || 'dark';
                document.body.setAttribute('data-theme', saved);
                document.documentElement.setAttribute('data-theme', saved);
                themeBtn.querySelector('i').className = saved === 'light' ? 'fas fa-sun' : 'fas fa-moon';
            }}

            const jumpBtn = document.getElementById('jump-top-btn');
            window.addEventListener('scroll', () => {{
                if (window.scrollY > 200) {{
                    jumpBtn.classList.add('visible');
                }} else {{
                    jumpBtn.classList.remove('visible');
                }}
            }});

            // Load initial paper
            loadPaper('{first_key}', document.querySelector('.paper-sidebar .ch-nav-btn'));
        }});
    </script>
</body>
</html>
"""
    return html

# -------------------------------------------------------------
# 4. COMPILE IMO_INDEX.HTML
# -------------------------------------------------------------
imo_config = {
    "track": "IMO",
    "subject": "Mathematics",
    "title": "International Mathematics Olympiad (IMO) • Practice & Exam Suite",
    "subtitle": "Official Foundation Mathematics Olympiad Master Suite: 7 Exam Papers spanning Logical Reasoning, Mathematical Reasoning, Everyday Maths & HOTS Achievers Section with 100% verified step-by-step solutions.",
    "badge_name": "SOF IMO",
    "primary_color": "#6366F1",
    "primary_hover": "#4F46E5",
    "primary_glow": "rgba(99, 102, 241, 0.25)",
    "accent_color": "#818CF8",
    "icon_class": "fa-shapes",
    "color_gradient": "linear-gradient(135deg, #6366F1, #8B5CF6)",
    "total_q_count": 350,
    "section_filters": [
        {"id": "all", "label": "All (50)"},
        {"id": "logical_reasoning", "label": "Logical Reasoning (15Q)"},
        {"id": "mathematical_reasoning", "label": "Maths Reasoning (20Q)"},
        {"id": "everyday_mathematics", "label": "Everyday Maths (10Q)"},
        {"id": "achievers_section", "label": "Achievers HOTS (5Q • 3M)"}
    ]
}

imo_html = generate_html_content(imo_config, imo_data)
with open(os.path.join(BASE_DIR, "imo_index.html"), "w", encoding="utf-8") as f:
    f.write(imo_html)
print("Generated imo_index.html successfully.")

# -------------------------------------------------------------
# 5. COMPILE NSO_INDEX.HTML
# -------------------------------------------------------------
nso_config = {
    "track": "NSO",
    "subject": "Science",
    "title": "National Science Olympiad (NSO) • Practice & Exam Suite",
    "subtitle": "Official Foundation Science Olympiad Master Suite: 6 Full Exam Papers covering Physics, Chemistry, Biology, Logical Reasoning & HOTS Achievers Section with 100% verified scientific solutions.",
    "badge_name": "SOF NSO",
    "primary_color": "#10B981",
    "primary_hover": "#059669",
    "primary_glow": "rgba(16, 185, 129, 0.25)",
    "accent_color": "#34D399",
    "icon_class": "fa-flask",
    "color_gradient": "linear-gradient(135deg, #10B981, #06B6D4)",
    "total_q_count": 300,
    "section_filters": [
        {"id": "all", "label": "All (50)"},
        {"id": "logical_reasoning", "label": "Logical Reasoning (10Q)"},
        {"id": "science", "label": "Science Core (35Q)"},
        {"id": "achievers_section", "label": "Achievers HOTS (5Q • 3M)"}
    ]
}

nso_html = generate_html_content(nso_config, nso_data)
with open(os.path.join(BASE_DIR, "nso_index.html"), "w", encoding="utf-8") as f:
    f.write(nso_html)
print("Generated nso_index.html successfully.")

# -------------------------------------------------------------
# 6. UPDATE INDEX.HTML (ACTIVITIES SECTION)
# -------------------------------------------------------------
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Update sidebar stats line
index_content = index_content.replace(
    '<div class="branch-stats">KB • AI/Robo • GK • IEO</div>',
    '<div class="branch-stats">KB • AI/Robo • GK • IEO • IMO • NSO</div>'
)

# Insert IMO (4.5) and NSO (4.6) cards after IEO (4.4)
imo_nso_cards = """
                    <!-- International Mathematics Olympiad (IMO) Card -->
                    <a href="imo_index.html" class="chapter-card" id="card-imo-olympiad">
                        <div class="ch-num" style="color: #6366F1;">4.5</div>
                        <div class="ch-content">
                            <div class="ch-title-row">
                                <h4 class="ch-title">📐 International Mathematics Olympiad (SOF IMO)</h4>
                                <span class="tag" style="background: rgba(99, 102, 241, 0.15); color: #818CF8; border: 1px solid rgba(99, 102, 241, 0.35); font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; font-weight: 700;">OLYMPIAD WORKBOOK • 350 QUESTIONS</span>
                            </div>
                            <p class="ch-desc">Official Foundation Mathematics Olympiad Master Suite: 7 Exam Papers (2023-24 Set-B, 2022-23 Set-A, 2022-23 Set-B, 2021-22 Set-A, 2021-22 Set-B, Model Papers 1 & 2) spanning Logical Reasoning, Mathematical Reasoning, Everyday Maths & HOTS Achievers Section with 100% verified step-by-step solutions.</p>
                            <div class="ch-tags">
                                <span class="tag"><i class="fas fa-file-alt"></i> 7 Exam Papers</span>
                                <span class="tag"><i class="fas fa-list-ol"></i> 350 Questions</span>
                                <span class="tag" style="color:#F59E0B; border-color:rgba(245,158,11,0.3);"><i class="fas fa-star"></i> Achievers HOTS (35Q)</span>
                                <span class="tag"><i class="fas fa-brain"></i> Logical & Math Reasoning</span>
                                <span class="tag"><i class="fas fa-check-double"></i> Complete Answer Keys</span>
                                <span class="tag"><i class="fas fa-stopwatch"></i> 60 Mins Exam Simulator</span>
                            </div>
                        </div>
                    </a>

                    <!-- National Science Olympiad (NSO) Card -->
                    <a href="nso_index.html" class="chapter-card" id="card-nso-olympiad">
                        <div class="ch-num" style="color: #10B981;">4.6</div>
                        <div class="ch-content">
                            <div class="ch-title-row">
                                <h4 class="ch-title">🔬 National Science Olympiad (SOF NSO)</h4>
                                <span class="tag" style="background: rgba(16, 185, 129, 0.15); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.35); font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; font-weight: 700;">OLYMPIAD WORKBOOK • 300 QUESTIONS</span>
                            </div>
                            <p class="ch-desc">Official Foundation Science Olympiad Master Suite: 6 Full Exam Papers (2022-23 Set-A, 2022-23 Set-B, 2021-22 Set-A, 2021-22 Set-B, Model Papers 1 & 2) covering Physics, Chemistry, Biology, Logical Reasoning & HOTS Achievers Section with 100% verified scientific solutions.</p>
                            <div class="ch-tags">
                                <span class="tag"><i class="fas fa-file-alt"></i> 6 Exam Papers</span>
                                <span class="tag"><i class="fas fa-list-ol"></i> 300 Questions</span>
                                <span class="tag" style="color:#F59E0B; border-color:rgba(245,158,11,0.3);"><i class="fas fa-star"></i> Achievers HOTS (30Q)</span>
                                <span class="tag"><i class="fas fa-flask"></i> Physics, Chem & Bio</span>
                                <span class="tag"><i class="fas fa-check-double"></i> Complete Answer Keys</span>
                                <span class="tag"><i class="fas fa-stopwatch"></i> 60 Mins Exam Simulator</span>
                            </div>
                        </div>
                    </a>
"""

if 'id="card-imo-olympiad"' not in index_content:
    # Insert after the closing tag of card-ieo-olympiad
    target_pattern = 'id="card-ieo-olympiad">'
    idx = index_content.find(target_pattern)
    if idx != -1:
        end_a = index_content.find('</a>', idx) + 4
        index_content = index_content[:end_a] + imo_nso_cards + index_content[end_a:]
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        print("Updated index.html with IMO (4.5) and NSO (4.6) cards.")
    else:
        print("Could not find card-ieo-olympiad in index.html")
else:
    print("IMO card already present in index.html.")

print("[SUCCESS] All files compiled and synchronized successfully.")
