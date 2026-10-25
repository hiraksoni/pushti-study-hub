# -*- coding: utf-8 -*-
"""
Verification script for Class 7 Biology Chapter 4: Life Processes in Plants KB.
Checks dual-store parity, dual-schema parity, item count, diagram slot protocol,
pure Unicode compliance, and zero publisher brand names.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

KB_DIR = "KB Files/biology/ch4_life_processes_plants"
PROD_DIR = "knowledge_base/biology/ch4_life_processes_plants"

kb_json_path = os.path.join(KB_DIR, "bio_ch4_life_processes_plants.json")
kb_md_path = os.path.join(KB_DIR, "bio_ch4_life_processes_plants.md")
prod_json_path = os.path.join(PROD_DIR, "bio_ch4_life_processes_plants.json")
prod_md_path = os.path.join(PROD_DIR, "bio_ch4_life_processes_plants.md")

passed_checks = 0
total_checks = 0

def check(condition, message):
    global passed_checks, total_checks
    total_checks += 1
    if condition:
        print(f"  [PASS] {message}")
        passed_checks += 1
    else:
        print(f"  [FAIL] {message}")

print("=== VERIFYING BIOLOGY CHAPTER 4 KNOWLEDGE BASE ===")

# 1. Existence and size
for p in [kb_json_path, kb_md_path, prod_json_path, prod_md_path]:
    exists = os.path.isfile(p)
    size = os.path.getsize(p) if exists else 0
    check(exists and size > 50000, f"File exists and size > 50KB: {p} ({size:,} bytes)")

# 2. Dual-store bitwise identity
with open(kb_json_path, "rb") as f1, open(prod_json_path, "rb") as f2:
    check(f1.read() == f2.read(), "Dual-store JSON files are bit-for-bit identical")

with open(kb_md_path, "rb") as f1, open(prod_md_path, "rb") as f2:
    check(f1.read() == f2.read(), "Dual-store Markdown files are bit-for-bit identical")

# 3. JSON schema and integrity
with open(kb_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

expected_top_keys = ["subject", "discipline", "chapter_num", "chapter_title", "learning_outcomes", "theory_summary", "questions", "assessment_items"]
check(all(k in data for k in expected_top_keys),
      f"Top-level keys conform to dual-schema specification: {list(data.keys())}")

items = data["assessment_items"]
questions = data["questions"]

check(items == questions, "Dual-schema parity: 'assessment_items' == 'questions'")
check(len(items) == 191, f"Total assessment items count is {len(items)} (191 expected)")

# 4. Diagram Slots Protocol
slots_found = 0
for it in items:
    slot = it.get("diagram_slot")
    if slot:
        slots_found += 1
        check(slot.get("status") == "pending", f"Item {it['id']} diagram slot status is 'pending'")
        check(slot.get("image_path") is None, f"Item {it['id']} diagram slot image_path is null")
        check(bool(slot.get("source_hint")) and bool(slot.get("description")), f"Item {it['id']} diagram slot has valid hint & description")

check(slots_found >= 8, f"Found active pending diagram slots: {slots_found} (>= 8 expected)")

# 5. Publisher brand name checks
forbidden_brands = ["lead school", "leadschool", "lead learning", "lead edutech", "ratna sagar", "oxford university press", "orient blackswan", "pearson"]
json_str = json.dumps(data, ensure_ascii=False).lower()
found_brands_json = [b for b in forbidden_brands if b in json_str]
check(len(found_brands_json) == 0, f"Zero publisher brand names in JSON (found: {found_brands_json})")

with open(kb_md_path, "r", encoding="utf-8") as f:
    md_str = f.read().lower()
found_brands_md = [b for b in forbidden_brands if b in md_str]
check(len(found_brands_md) == 0, f"Zero publisher brand names in Markdown (found: {found_brands_md})")

# 6. Check for pure unicode biochemical and mathematical symbols
unicode_symbols = ["co₂", "o₂", "h₂o", "c₆h₁₂o₆", "ca(oh)₂", "caco₃", "nahco₃", "koh", "→"]
for sym in unicode_symbols:
    check(sym in json_str, f"Proper Unicode chemical symbol '{sym}' present in knowledge base content")

print("=" * 50)
print(f"VERIFICATION RESULT: {passed_checks}/{total_checks} checks passed.")
if passed_checks == total_checks:
    print("ALL TESTS PASSED! Ready for production.")
else:
    print("WARNING: Some checks failed.")
    sys.exit(1)
