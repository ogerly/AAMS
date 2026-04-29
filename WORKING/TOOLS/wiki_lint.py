#!/usr/bin/env python3
"""
AAMS Wiki-Lint — Health-Check für Whitepapers, Workpapers und Cross-Referenzen.
Usage (from repo root):
    python WORKING/TOOLS/wiki_lint.py
    python WORKING/TOOLS/wiki_lint.py --fix       (zeigt auch Vorschläge)
    python WORKING/TOOLS/wiki_lint.py --json       (maschinenlesbare Ausgabe)

Checks:
  L1  Whitepaper-Index vs. tatsächliche Dateien (verwaist / fehlend)
  L2  Stale Whitepapers (letztes Update > 30 Tage)
  L3  Offene Workpapers ohne TOPIC-Tag im Dateinamen
  L4  Decision-Promotion: offene Workpapers mit Decisions die nicht in Whitepapers stehen
  L4b Orphaned Decisions: E-X Pattern in Workpapers die nicht in Whitepapers gepromoted
  L5  Cross-Referenzen: Whitepapers die kein anderes WP referenzieren
  L6  LTM-Index: letzte Eintrags-Nummer vs. erwartete Konsistenz
  L7  Pending-Decision-Marker in Whitepapers (⚠️ Pending)

AAMS/1.0 — Inspiriert von Karpathy LLM-Wiki Lint-Konzept.
~3k Tokens pro Durchlauf bei aktuellem Scale.
"""

import sys
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
WORKING = REPO_ROOT / "WORKING"
WP_DIR = WORKING / "WHITEPAPER"
WORKPAPER_DIR = WORKING / "WORKPAPER"
WORKPAPER_CLOSED = WORKPAPER_DIR / "closed"
MEMORY_DIR = WORKING / "MEMORY"
INDEX_FILE = WP_DIR / "INDEX.md"
LTM_FILE = MEMORY_DIR / "ltm-index.md"

STALE_DAYS = 30

# ── Result Container ──────────────────────────────────────────────────────────

class LintResult:
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


results: list[LintResult] = []


def add(check_id, severity, message, file="", suggestion=""):
    results.append(LintResult(check_id, severity, message, file, suggestion))


# ── L1: Whitepaper-Index vs. Dateien ─────────────────────────────────────────

def check_l1():
    if not INDEX_FILE.exists():
        add("L1", "ERROR", "INDEX.md fehlt", str(INDEX_FILE))
        return

    index_text = INDEX_FILE.read_text(encoding="utf-8")
    # Extrahiere referenzierte .md-Dateien aus Markdown-Links
    referenced = set(re.findall(r"\./([A-Za-z0-9_-]+\.md)", index_text))

    actual_wps = {f.name for f in WP_DIR.glob("WP-*.md")}

    orphaned = actual_wps - referenced
    missing = referenced - actual_wps

    for f in sorted(orphaned):
        add("L1", "WARN", f"Whitepaper existiert aber fehlt in INDEX.md", f,
            f"Eintrag in INDEX.md ergänzen für {f}")

    for f in sorted(missing):
        add("L1", "ERROR", f"INDEX.md referenziert nicht-existierende Datei", f,
            f"Eintrag entfernen oder Datei erstellen: {f}")

    if not orphaned and not missing:
        add("L1", "INFO", f"INDEX.md konsistent ({len(actual_wps)} Whitepapers)")


# ── L2: Stale Whitepapers ───────────────────────────────────────────────────

def check_l2():
    today = datetime.now()
    for wp in sorted(WP_DIR.glob("WP-*.md")):
        text = wp.read_text(encoding="utf-8")
        # Suche nach "Letztes Update: YYYY-MM-DD" oder "Stand" Datum
        dates = re.findall(r"(\d{4}-\d{2}-\d{2})", text[:500])
        if not dates:
            add("L2", "WARN", "Kein Datum im Header gefunden", wp.name)
            continue

        # Nehme das späteste Datum im Header-Bereich
        latest = max(dates)
        try:
            last_update = datetime.strptime(latest, "%Y-%m-%d")
            age = (today - last_update).days
            if age > STALE_DAYS:
                add("L2", "WARN", f"Letztes Update vor {age} Tagen ({latest})", wp.name,
                    f"Prüfen ob {wp.name} noch aktuell ist")
        except ValueError:
            pass


# ── L3: Workpaper Naming-Schema ─────────────────────────────────────────────

def check_l3():
    # Pattern: YYYY-MM-DD-TOPIC-... oder YYYY-MM-DD-TOPIC-SUBTOPIC-...
    naming_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}-[A-Z]{3,4}-")

    open_wps = [f for f in WORKPAPER_DIR.glob("*.md") if f.is_file()]
    for wp in sorted(open_wps):
        if not naming_pattern.match(wp.stem):
            add("L3", "WARN", f"Kein TOPIC-Tag im Dateinamen", wp.name,
                "Umbenennen nach Schema: {DATE}-{TOPIC}-{SUBTOPIC}-{description}.md")


# ── L4: Decision-Promotion Check ────────────────────────────────────────────

def check_l4():
    """Prüft offene Workpapers auf Decisions die nicht in Whitepapers reflektiert sind."""
    # Lade alle Whitepaper-Texte für Stichwort-Suche
    wp_texts = {}
    for wp in WP_DIR.glob("WP-*.md"):
        wp_texts[wp.name] = wp.read_text(encoding="utf-8").lower()

    open_wps = [f for f in WORKPAPER_DIR.glob("*.md") if f.is_file()]
    for workpaper in sorted(open_wps):
        text = workpaper.read_text(encoding="utf-8")

        # Finde Decision-Abschnitt
        decision_match = re.search(r"## Decisions?\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
        if not decision_match:
            continue

        decisions_text = decision_match.group(1)
        # Suche nach expliziten PROMOTE-Tags
        promotes = re.findall(r"\[PROMOTE→(WP-\d+)\]", decisions_text)
        for target in promotes:
            target_file = f"{target}-" # prefix
            found = any(target_file.lower() in name.lower() for name in wp_texts)
            if not found:
                add("L4", "ERROR", f"PROMOTE→{target} verweist auf nicht-existierendes Whitepaper",
                    workpaper.name)

        # Zähle Decisions (Zeilen mit D1, D2, etc. oder **Dx:**)
        decision_lines = re.findall(r"\*\*D\d+[:\.]?\*\*", decisions_text)
        if len(decision_lines) >= 2:
            # Prüfe ob irgendein Schlüsselwort aus den Decisions in Whitepapers auftaucht
            has_promote_tag = bool(promotes)
            if not has_promote_tag:
                add("L4", "WARN",
                    f"{len(decision_lines)} Decisions ohne [PROMOTE→WP-xxx] Tag",
                    workpaper.name,
                    "Architektur-relevante Decisions mit [PROMOTE→WP-xxx] taggen")


# ── L4b: Orphaned Decisions ─────────────────────────────────────────────────

def check_l4b():
    """Finde offene Decisions in Workpapers die nicht in Whitepapers gepromoted wurden.
    
    Sucht nach Patterns wie 'E-1', 'E-2', 'Decision 1', 'D1', 'D.1' etc. in Workpapers
    und prüft ob sie in einem Whitepaper gelöst/erwähnt sind.
    """
    # Lade alle Whitepaper-Texte für Stichwort-Suche
    wp_texts = {}
    for wp in WP_DIR.glob("WP-*.md"):
        wp_texts[wp.name] = wp.read_text(encoding="utf-8")

    # Lade INDEX.md für Pending-Marker
    index_text = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""

    open_wps = [f for f in WORKPAPER_DIR.glob("*.md") if f.is_file()]
    for workpaper in sorted(open_wps):
        text = workpaper.read_text(encoding="utf-8")

        # Pattern 1: E-X (wie in RFCT Workpaper: E-1, E-2, ...)
        e_matches = re.findall(r"\bE-(\d+)\b", text)
        # Pattern 2: Decision X (wie in STRAT Workpaper)
        d_matches = re.findall(r"\bDecision\s+(\d+)\b", text)
        # Pattern 3: D1, D2, etc.
        d_short = re.findall(r"\bD\.?(\d+)\b", text)

        # Alle gefundenen Decision-IDs sammeln
        all_decisions = set()
        for m in e_matches:
            all_decisions.add(f"E-{m}")
        for m in d_matches:
            all_decisions.add(f"Decision-{m}")
        for m in d_short:
            all_decisions.add(f"D-{m}")

        if not all_decisions:
            continue

        # Für jede Decision prüfen ob sie in einem Whitepaper erwähnt
        for decision in all_decisions:
            # Prüfe ob in INDEX.md oder WP-Texten eine Lösung steht
            found_in_wps = False
            for wp_name, wp_text in wp_texts.items():
                if decision.lower() in wp_text.lower():
                    found_in_wps = True
                    break

            # Prüfe ob in INDEX.md der Pending-Marker aufgelöst wurde
            if not found_in_wps:
                # Prüfe ob INDEX.md einen gelösten Status hat
                if "✅" in index_text and decision.lower().replace("-", "") in index_text.lower().replace(" ", ""):
                    found_in_wps = True

            if not found_in_wps:
                add("L4b", "WARN",
                    f"Orphaned Decision {decision} in {workpaper.name} — nicht in Whitepaper gepromoted",
                    workpaper.name,
                    f"Decision {decision} in INDEX.md oder betroffenem Whitepaper auflösen")


# ── L5: Cross-Referenzen ────────────────────────────────────────────────────

def check_l5():
    wps = list(WP_DIR.glob("WP-*.md"))
    wp_names = {wp.stem for wp in wps}

    for wp in sorted(wps):
        text = wp.read_text(encoding="utf-8")
        # Suche nach Referenzen auf andere WP-xxx
        refs = set(re.findall(r"WP-\d+", text))
        own_id = re.match(r"(WP-\d+)", wp.stem)
        if own_id:
            refs.discard(own_id.group(1))

        if not refs:
            add("L5", "WARN", f"Keine Cross-Referenzen zu anderen Whitepapers", wp.name,
                "Mindestens einen Verweis auf verwandte WPs ergänzen")


# ── L6: LTM-Index Konsistenz ────────────────────────────────────────────────

def check_l6():
    if not LTM_FILE.exists():
        add("L6", "ERROR", "ltm-index.md fehlt", str(LTM_FILE))
        return

    text = LTM_FILE.read_text(encoding="utf-8")
    # Finde alle Eintrags-Nummern (| NNN | ...)
    entries = re.findall(r"\|\s*(\d{3})\s*\|", text)
    if not entries:
        add("L6", "WARN", "Keine nummerierten Einträge im LTM-Index gefunden")
        return

    numbers = sorted(int(e) for e in entries)
    expected = list(range(numbers[0], numbers[-1] + 1))
    gaps = set(expected) - set(numbers)

    if gaps:
        add("L6", "WARN", f"Lücken in LTM-Nummerierung: {sorted(gaps)}")
    else:
        add("L6", "INFO", f"LTM-Index konsistent ({numbers[0]}-{numbers[-1]}, {len(numbers)} Einträge)")


# ── L7: Pending-Decision-Marker ─────────────────────────────────────────────

def check_l7():
    for wp in sorted(WP_DIR.glob("WP-*.md")):
        text = wp.read_text(encoding="utf-8")
        pendings = re.findall(r"⚠️?\s*Pending[- ]Decision", text, re.IGNORECASE)
        pendings += re.findall(r"Pending Decision \(E-\d+", text)
        if pendings:
            add("L7", "WARN", f"{len(pendings)} Pending-Decision-Marker gefunden", wp.name,
                "Entscheidungen E-1..E-5 treffen und Marker auflösen")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    show_fix = "--fix" in sys.argv
    as_json = "--json" in sys.argv

    print("=" * 60)
    print("  AAMS Wiki-Lint — Health Check")
    print("=" * 60)
    print()

    checks = [
        ("L1 — Whitepaper-Index vs. Dateien", check_l1),
        ("L2 — Stale Whitepapers", check_l2),
        ("L3 — Workpaper Naming-Schema", check_l3),
        ("L4 — Decision-Promotion", check_l4),
        ("L4b — Orphaned Decisions", check_l4b),
        ("L5 — Cross-Referenzen", check_l5),
        ("L6 — LTM-Index Konsistenz", check_l6),
        ("L7 — Pending-Decision-Marker", check_l7),
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

    # Exit code: 1 wenn Errors, 0 sonst
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
