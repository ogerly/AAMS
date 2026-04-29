#!/usr/bin/env python3
"""
AAMS Doctor — Validiert Tool-Integrität im Repository.

Usage (from repo root):
    python WORKING/TOOLS/validate_tools.py
    python WORKING/TOOLS/validate_tools.py --fix       (zeigt auch Vorschläge)
    python WORKING/TOOLS/validate_tools.py --json       (maschinenlesbare Ausgabe)

Checks:
  D1  Alle Python-Tools in WORKING/TOOLS/ — keine im Root
  D2  Kein Tool verwendet fragile Offset-Relative Paths (parent.parent, parent.parent.parent)
  D3  WORKING/ Struktur ist konsistent mit .agent.json
  D4  Verwaiste Ordner im Root (außer src/, public/, dist/, .git/, docs/)

AAMS/1.0 — Tool-Integritäts-Check gegen Issue #47 (Tool Decay).
"""

import sys
import json
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
WORKING = REPO_ROOT / "WORKING"
AGENT_JSON = REPO_ROOT / ".agent.json"

ALLOWED_ROOT_DIRS = {"src", "public", "dist", ".git", "docs", "reference", "templates", "registry", "prompts", "outreach", ".github", "node_modules", ".venv"}

# ── Result Container ──────────────────────────────────────────────────────────

class DoctorResult:
    def __init__(self, check_id: str, severity: str, message: str, file: str = "", suggestion: str = ""):
        self.check_id = check_id
        self.severity = severity  # ERROR, WARN, INFO
        self.message = message
        self.file = file
        self.suggestion = suggestion

    def __str__(self):
        icon = {"ERROR": "🔴", "WARN": "⚠️", "INFO": "ℹ️"}.get(self.severity, "?")
        loc = f" [{self.file}]" if self.file else ""
        return f"  {icon} {self.check_id}: {self.message}{loc}"

    def to_dict(self):
        return {
            "check": self.check_id,
            "severity": self.severity,
            "message": self.message,
            "file": self.file,
            "suggestion": self.suggestion,
        }


results: list[DoctorResult] = []


def add(check_id, severity, message, file="", suggestion=""):
    results.append(DoctorResult(check_id, severity, message, file, suggestion))


# ── D1: Tools außerhalb von WORKING/TOOLS/ ───────────────────────────────────

def check_d1():
    """Finde Python-Tools die nicht in WORKING/TOOLS/ liegen."""
    for item in REPO_ROOT.iterdir():
        if item.is_file() and item.suffix == ".py" and item.name != "validate_tools.py":
            add("D1", "ERROR", f"Python-Tool außerhalb von WORKING/TOOLS/: {item.name}", item.name,
                f"Nach WORKING/TOOLS/{item.name} verschieben")


# ── D2: Fragile Offset-Relative Paths ─────────────────────────────────────────

def check_d2():
    """Finde Tools mit fragilen Offset-Paths."""
    tools_dir = WORKING / "TOOLS"
    if not tools_dir.exists():
        add("D2", "WARN", "WORKING/TOOLS/ existiert nicht")
        return

    offset_pattern = re.compile(r"\.parent(\.parent)+")

    for py_file in (tools_dir).glob("*.py"):
        text = py_file.read_text(encoding="utf-8")
        matches = offset_pattern.findall(text)
        if matches:
            # Zähle wie tief der Offset geht
            depth = len(matches[0].split(".parent")) - 1
            if depth >= 2:  # .parent.parent oder tiefer
                add("D2", "WARN",
                    f"Fragiler Offset-Path ({depth}x .parent) in {py_file.name}",
                    py_file.name,
                    f"Dynamische Root-Erkennung verwenden: git rev-parse --show-toplevel oder package.json Suche")


# ── D3: WORKING/ Struktur vs .agent.json ─────────────────────────────────────

def check_d3():
    """Prüfe ob WORKING/ Struktur mit .agent.json übereinstimmt."""
    if not AGENT_JSON.exists():
        add("D3", "WARN", ".agent.json nicht gefunden")
        return

    import json as json_mod
    try:
        with open(AGENT_JSON, "r", encoding="utf-8") as f:
            config = json_mod.load(f)
    except (json_mod.JSONDecodeError, IOError):
        add("D3", "WARN", ".agent.json kann nicht gelesen werden")
        return

    structure = config.get("workspace", {}).get("structure", {})
    for folder_name, folder_path in structure.items():
        if folder_name.startswith("_"):
            continue  # Skip metadata fields like _doc
        full_path = REPO_ROOT / folder_path.lstrip("./")
        if not full_path.exists():
            add("D3", "WARN", f"Vorgesehener Ordner existiert nicht: {folder_path}",
                folder_path,
                f"Ordner anlegen: mkdir -p {folder_path}")


# ── D4: Verwaiste Ordner im Root ─────────────────────────────────────────────
def check_d4():
    """Finde Ordner im Root die weder Produktion noch AAMS zugeordnet sind."""
    for item in REPO_ROOT.iterdir():
        if item.is_dir() and item.name not in ALLOWED_ROOT_DIRS and not item.name.startswith("."):
            # Prüfe ob es ein AAMS-Ordner ist
            if item.name in {"WORKING", "WORKSPACE", "docs", "reference", "templates", "registry", "prompts", "outreach"}:
                continue
            add("D4", "WARN", f"Verdächtiger Root-Ordner: {item.name}", item.name,
                "Prüfen ob dieser Ordner in WORKING/ gehören würde")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    show_fix = "--fix" in sys.argv
    as_json = "--json" in sys.argv

    print("=" * 60)
    print("  AAMS Doctor — Tool Integrity Check")
    print("=" * 60)
    print()

    checks = [
        ("D1 — Tools in WORKING/TOOLS/", check_d1),
        ("D2 — Fragile Offset-Paths", check_d2),
        ("D3 — WORKING/ Struktur vs .agent.json", check_d3),
        ("D4 — Verwaiste Root-Ordner", check_d4),
    ]

    for label, fn in checks:
        print(f"▸ {label}")
        before = len(results)
        fn()
        after = len(results)
        if after == before:
            print("  ✅ Keine Findings")
        print()

    # ── Summary ──────────────────────────────────────────────────────────────
    errors = sum(1 for r in results if r.severity == "ERROR")
    warns = sum(1 for r in results if r.severity == "WARN")
    infos = sum(1 for r in results if r.severity == "INFO")

    print("=" * 60)
    print(f"  Summary: {errors} ERROR  {warns} WARN  {infos} INFO")
    print("=" * 60)

    if show_fix:
        suggestions = [r for r in results if r.suggestion]
        if suggestions:
            print("\n  Vorschläge (--fix):")
            for r in suggestions:
                print(f"    → {r.check_id} [{r.file}]: {r.suggestion}")

    if as_json:
        print("\n" + json.dumps([r.to_dict() for r in results], indent=2, ensure_ascii=False))

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
