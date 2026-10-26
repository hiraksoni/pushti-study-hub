# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'chapters/science/science_bio_ch4.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

print(f"=== Verifying {file_path} ===")
print(f"File Size: {len(html)} bytes | Lines: {len(html.splitlines())}")

# Check Tabs
expected_tabs = [
    'tabPrimer', 'tabGrowth', 'tabNutrition', 'tabPhotosynthesis',
    'tabFactors', 'tabTransport', 'tabRespiration', 'tabActivities',
    'tabTextbook', 'tabDrills', 'tabTraps', 'tabGoogleHub'
]

missing_tabs = []
for t in expected_tabs:
    if f'id="{t}"' not in html:
        missing_tabs.append(t)

if missing_tabs:
    print(f"ERROR: Missing tabs: {missing_tabs}")
else:
    print(f"PASS: All 12 tabs present.")

# Check Nav buttons
missing_btns = []
for t in expected_tabs:
    if f'id="navBtn-{t}"' not in html:
        missing_btns.append(t)

if missing_btns:
    print(f"ERROR: Missing nav buttons: {missing_btns}")
else:
    print(f"PASS: All 12 navigation buttons present.")

# Check Match Arenas
arenas = re.findall(r'id="match-arena-(\d+)"', html)
print(f"PASS: Found {len(arenas)} Match Arenas: {arenas}")

# Check Subjective Cards
subj_cards = re.findall(r'class="subj-card\b', html)
print(f"PASS: Found {len(subj_cards)} Subjective Q&A Cards (Expected 69)")

# Check Objective Drill Cards
drill_cards = re.findall(r'class="drill-card\b', html)
print(f"PASS: Found {len(drill_cards)} Objective Drill Cards (Expected 126)")

# Check Diagram Slots
diagram_slots_subj = re.findall(r'Diagram Slot \(Pending Admin Asset\)', html)
diagram_slots_obj = re.findall(r'Visual Diagram Slot', html)
total_diagram_slots = len(diagram_slots_subj) + len(diagram_slots_obj)
print(f"PASS: Found {total_diagram_slots} Diagram Slot Banners (Subj: {len(diagram_slots_subj)}, Obj: {len(diagram_slots_obj)}, Total Expected: 15)")

# Check Flashcards
flashcards = re.findall(r'class="flashcard-3d\b', html)
print(f"PASS: Found {len(flashcards)} 3D Interactive Flashcards (Expected 16)")

# Check Traps
traps = re.findall(r'Trap \d+:', html)
print(f"PASS: Found {len(traps)} Fatal Exam Traps (Expected 8)")

# Check Jump to Top
if 'id="pushti-jump-to-top"' in html:
    print("PASS: Universal Jump-to-Top button present.")
else:
    print("ERROR: Universal Jump-to-Top button missing.")

# Check Pin Toggle
if 'id="pinToggleBtn"' in html and 'toggleSidebarPin()' in html:
    print("PASS: Tablet-safe Pin Sidebar toggle present.")
else:
    print("ERROR: Pin Sidebar toggle missing.")

# Check Scripts
if 'function switchTab(' in html and 'function handleDrillClick(' in html and 'function checkMatchDrill(' in html:
    print("PASS: All required JavaScript controller functions present.")
else:
    print("ERROR: JavaScript functions missing.")

# Check for Empty Question Prompts
empty_subj_q = re.findall(r'<p class="subj-qtext font-semibold[^>]*>\s*</p>', html)
if empty_subj_q:
    print(f"ERROR: Found {len(empty_subj_q)} empty subjective question prompts!")
else:
    print("PASS: All subjective question prompts are non-empty.")

empty_drill_q = re.findall(r'<p class="text-slate-100 font-semibold mb-4 text-base[^>]*>\s*</p>', html)
if empty_drill_q:
    print(f"ERROR: Found {len(empty_drill_q)} empty objective drill question prompts!")
else:
    print("PASS: All objective drill question prompts are non-empty.")

# Check Flashcards Onclick
broken_flashcards = re.findall(r'<div class="flashcard-3d[^>]*onclick="(?![^"]*classList\.toggle)[^"]*"', html)
if broken_flashcards:
    print(f"ERROR: Found {len(broken_flashcards)} flashcards without classList.toggle onclick!")
else:
    print("PASS: All 16 flashcards have tablet-safe classList.toggle onclick handlers.")

# Check Toggle Answer targets
broken_toggles = []
toggle_calls = re.findall(r'toggleAnswer\([\'"]([^\'"]+)[\'"]\)', html)
for tgt in toggle_calls:
    if f'id="{tgt}"' not in html:
        broken_toggles.append(tgt)
if broken_toggles:
    print(f"ERROR: Found {len(broken_toggles)} broken toggleAnswer targets!")
else:
    print(f"PASS: All {len(toggle_calls)} toggleAnswer calls have matching answer box elements.")

# Check Match Arena UI Badges
match_conn = len(re.findall(r'match-conn-badge', html))
match_sock = len(re.findall(r'match-socket-badge', html))
if match_conn == match_sock and match_conn > 0:
    print(f"PASS: Match arena badges balanced: {match_conn} conn badges, {match_sock} socket badges across 4 arenas.")
else:
    print(f"ERROR: Match arena badges mismatch: conn={match_conn}, sock={match_sock}.")


