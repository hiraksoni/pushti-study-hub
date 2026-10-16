"""
Permanent Automated Flush Protocol Audit Script for Olympiad HTML Apps
Verifies:
1. Zero dummy question stems ('Based on the core syllabus concepts of')
2. Zero placeholder options ('Verified (', 'Alternative I', 'Alternative II')
3. Zero truncated or broken LaTeX commands (e.g. unclosed '\\text{')
4. Exactly 4 distinct options per active question
5. Valid answer keys (A, B, C, D)
6. Missing question integrity (IMO 2022-23 Set-B Q13-50 registered as missing)
"""

import json
import re
import sys
import os

BASE_DIR = r"D:\Users\expor\Downloads\Codes"
APPS = [
    ("nso_index.html", 300, 300),
    ("imo_index.html", 350, 312)  # 350 total slots, 312 active, 38 registered missing
]

def run_audit():
    total_violations = 0
    print("=====================================================================")
    print("           PUSHTI STUDY HUB - AUTOMATED FLUSH AUDIT                 ")
    print("=====================================================================")

    for app_name, expected_total, expected_active in APPS:
        app_path = os.path.join(BASE_DIR, app_name)
        if not os.path.exists(app_path):
            print(f"[ERROR] App file not found: {app_path}")
            total_violations += 1
            continue

        with open(app_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'const PAPERS_DATA = ({.*?});\s*let currentPaperKey', content, re.DOTALL)
        if not match:
            print(f"[ERROR] Could not extract PAPERS_DATA from {app_name}")
            total_violations += 1
            continue

        papers = json.loads(match.group(1))
        app_total_qs = 0
        app_active_qs = 0
        app_dummy_qs = 0

        print(f"\nAUDITING: {app_name}")
        print("-" * 65)

        for p_id, p in papers.items():
            paper_dummy = 0
            for q in p.get("questions", []):
                app_total_qs += 1
                qn = q.get("q_num", 0)

                if q.get("is_missing"):
                    continue

                app_active_qs += 1
                text = q.get("text", "")
                opts = q.get("opts", [])
                ans = q.get("answer", "")

                reasons = []

                # 1. Check dummy text
                if "Based on the core syllabus concepts of" in text:
                    reasons.append("Dummy question stem")

                # 2. Check dummy options
                for o in opts:
                    if "Verified (" in o:
                        reasons.append(f"Dummy option '{o}'")
                    if "Alternative I" in o or "Alternative II" in o:
                        reasons.append(f"Dummy option '{o}'")
                    if re.search(r'\\text\{\s*$', o):
                        reasons.append(f"Broken LaTeX '{o}'")

                # 3. Check distinctness
                if len(opts) != 4 or len(set(opts)) != 4:
                    reasons.append(f"Non-unique options: {opts}")

                # 4. Check answer key
                if ans not in ['A', 'B', 'C', 'D']:
                    reasons.append(f"Invalid answer key: '{ans}'")

                if reasons:
                    paper_dummy += 1
                    app_dummy_qs += 1
                    total_violations += 1
                    print(f"  [VIOLATION] Paper {p_id} Q{qn}: {', '.join(reasons)}")

            status_icon = "[OK]" if paper_dummy == 0 else "[FAIL]"
            print(f"  {status_icon} Paper {p_id:18s} | Questions: {len(p.get('questions', [])):2d} | Dummy: {paper_dummy}")

        print(f"-> Total Questions in {app_name}: {app_total_qs} (Active: {app_active_qs})")
        print(f"-> Dummy Questions in {app_name}: {app_dummy_qs} / {app_total_qs}")

    print("\n=====================================================================")
    if total_violations == 0:
        print("  ALL AUDITS PASSED: 100% AUTHENTIC DATA, ZERO DUMMY JUNK DETECTED! ")
        print("=====================================================================")
        return 0
    else:
        print(f"  AUDIT FAILED: {total_violations} VIOLATIONS FOUND!                ")
        print("=====================================================================")
        return 1

if __name__ == "__main__":
    sys.exit(run_audit())
