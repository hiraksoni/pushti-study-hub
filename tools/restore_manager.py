#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Restore Point and Failsafe Manager
----------------------------------
Instantaneous snapshot backups and Git tags before any modifications.
Allows 1-command deterministic rollbacks with complete audit trail.

Usage:
  python tools/restore_manager.py create "<Description>" [optional specific files...]
  python tools/restore_manager.py list
  python tools/restore_manager.py restore <ID_OR_TAG>
  python tools/restore_manager.py delete <ID_OR_TAG>
"""

import os
import sys
import json
import zipfile
import subprocess
from datetime import datetime

RESTORE_DIR = os.path.abspath(".restore_points")
MANIFEST_FILE = os.path.join(RESTORE_DIR, "manifest.json")

# Ignored directories for fast snapshotting
IGNORE_DIRS = {".git", "node_modules", ".restore_points", "__pycache__", "chem1_pages", "chem2_pages", "geo1_pages"}
# Ignored binary extensions for fast code snapshotting
IGNORE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".zip", ".tar", ".gz", ".pdf"}


def load_manifest():
    if not os.path.exists(RESTORE_DIR):
        os.makedirs(RESTORE_DIR, exist_ok=True)
    if os.path.exists(MANIFEST_FILE):
        try:
            with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"restore_points": []}
    return {"restore_points": []}


def save_manifest(manifest):
    os.makedirs(RESTORE_DIR, exist_ok=True)
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


def get_git_commit():
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
        return commit
    except Exception:
        return "unknown"


def create_git_tag(tag_name):
    try:
        subprocess.run(
            ["git", "tag", tag_name],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=3
        )
        return True
    except Exception:
        return False


def create_restore_point(description, specific_files=None):
    manifest = load_manifest()
    now = datetime.now()
    timestamp_str = now.strftime("%Y%m%d_%H%M%S")
    clean_desc = "".join(c if c.isalnum() else "_" for c in description[:30].strip()).strip("_")
    rp_id = f"RP_{timestamp_str}_{clean_desc}"
    git_tag = f"rp-{timestamp_str}"
    
    commit = get_git_commit()
    archive_filename = f"{rp_id}.zip"
    archive_path = os.path.join(RESTORE_DIR, archive_filename)

    files_to_backup = []
    if specific_files and len(specific_files) > 0:
        for f in specific_files:
            if os.path.exists(f):
                files_to_backup.append(f)
    else:
        for root, dirs, filenames in os.walk("."):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for fn in filenames:
                ext = os.path.splitext(fn)[1].lower()
                if ext in IGNORE_EXTS:
                    continue
                rel_path = os.path.relpath(os.path.join(root, fn), ".")
                files_to_backup.append(rel_path)

    # Fast Zip creation
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files_to_backup:
            zf.write(f, arcname=f)

    # Tag in git
    tag_created = create_git_tag(git_tag)

    entry = {
        "id": rp_id,
        "tag": git_tag if tag_created else None,
        "commit": commit,
        "timestamp": now.isoformat(),
        "display_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "description": description,
        "archive": archive_filename,
        "file_count": len(files_to_backup),
        "size_bytes": os.path.getsize(archive_path),
        "target": "selective" if specific_files else "codebase"
    }

    manifest["restore_points"].append(entry)
    save_manifest(manifest)

    print("\n" + "=" * 80)
    print(f"  [FAILSAPFE RESTORE POINT CREATED]")
    print(f"  ID          : {rp_id}")
    print(f"  Description : {description}")
    print(f"  Git Commit  : {commit} (Tag: {git_tag})")
    print(f"  Files Saved : {len(files_to_backup)} files ({entry['size_bytes'] / 1024:.1f} KB)")
    print(f"  Archive     : {archive_path}")
    print("=" * 80 + "\n")
    return rp_id


def list_restore_points():
    manifest = load_manifest()
    rps = manifest.get("restore_points", [])
    if not rps:
        print("\nNo restore points found in manifest.\n")
        return

    print("\n" + "=" * 95)
    print(f"{'ID':<35} | {'TIMESTAMP':<19} | {'FILES':<6} | {'DESCRIPTION'}")
    print("-" * 95)
    for rp in reversed(rps):
        rp_id = rp.get("id", "")
        ts = rp.get("display_time", rp.get("timestamp", ""))[:19]
        fc = str(rp.get("file_count", 0))
        desc = rp.get("description", "")
        print(f"{rp_id:<35} | {ts:<19} | {fc:<6} | {desc}")
    print("=" * 95)
    print(f"Total: {len(rps)} restore point(s) available.\n")


def restore_point(identifier):
    manifest = load_manifest()
    target_rp = None
    for rp in manifest.get("restore_points", []):
        if rp.get("id") == identifier or rp.get("tag") == identifier:
            target_rp = rp
            break

    if not target_rp:
        print(f"\n[Error] Restore point '{identifier}' not found in manifest.\n")
        return False

    archive_path = os.path.join(RESTORE_DIR, target_rp["archive"])
    if not os.path.exists(archive_path):
        print(f"\n[Error] Archive file '{archive_path}' is missing.\n")
        return False

    print(f"\n[Restoring] From: {target_rp['id']}")
    print(f"            Description: {target_rp['description']}...")
    with zipfile.ZipFile(archive_path, "r") as zf:
        zf.extractall(".")

    print(f"[Success] {target_rp['file_count']} files cleanly restored to working directory!\n")
    return True


def delete_restore_point(identifier):
    manifest = load_manifest()
    rps = manifest.get("restore_points", [])
    found = None
    for rp in rps:
        if rp.get("id") == identifier or rp.get("tag") == identifier:
            found = rp
            break

    if not found:
        print(f"\n[Error] Restore point '{identifier}' not found.\n")
        return False

    # Delete archive file
    archive_path = os.path.join(RESTORE_DIR, found.get("archive", ""))
    if os.path.exists(archive_path):
        try:
            os.remove(archive_path)
        except Exception as e:
            print(f"Warning: Could not remove archive file: {e}")

    # Delete git tag if present
    tag = found.get("tag")
    if tag:
        try:
            subprocess.call(["git", "tag", "-d", tag], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

    manifest["restore_points"] = [rp for rp in rps if rp != found]
    save_manifest(manifest)
    print(f"\n[Deleted] Restore point: {found['id']}\n")
    return True


def main():
    if len(sys.argv) < 2:
        print("\nRestore Point Manager Usage:")
        print("  python tools/restore_manager.py create \"<Description>\" [specific files...]")
        print("  python tools/restore_manager.py list")
        print("  python tools/restore_manager.py restore <ID_OR_TAG>")
        print("  python tools/restore_manager.py delete <ID_OR_TAG>\n")
        return

    cmd = sys.argv[1].lower()
    if cmd == "create":
        desc = sys.argv[2] if len(sys.argv) > 2 else "Manual checkpoint"
        files = sys.argv[3:] if len(sys.argv) > 3 else None
        create_restore_point(desc, files)
    elif cmd == "list":
        list_restore_points()
    elif cmd == "restore":
        if len(sys.argv) < 3:
            print("Please specify a restore point ID or tag.")
            return
        restore_point(sys.argv[2])
    elif cmd == "delete":
        if len(sys.argv) < 3:
            print("Please specify a restore point ID or tag to delete.")
            return
        delete_restore_point(sys.argv[2])
    else:
        print(f"Unknown command '{cmd}'")


if __name__ == "__main__":
    main()
