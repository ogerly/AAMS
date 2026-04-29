# Workpaper: Session-Plan — Decision-Promotion + Upgrade-Transparenz

**Datum:** 2026-04-24  
**Autor:** @DEVmatrose  
**Typ:** Session-Plan / Implementierungs-Auftrag  
**Priorität:** KRITISCH — Phase 2 der Issue-Triage  
**Referenz:** `2026-04-24-issue-triage.md` (Triage vom heute)

---

## Session Goal

**Heute:** Decision-Kompoundierungs-Leck (#48) schließen — WP-001 updaten + Decision-Promotion-Checklist aufnehmen + wiki_lint.py prüfen.

**Demnächst:** Upgrade-Transparenz (#49) implementieren — CHANGELOG.md + `.aams-version` + `on_update` Handler.

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-24-session-plan.md` | ✅ |

---

## 1. Kontext: Was haben wir auf dem Schirm?

### Analytisch abgeschlossen (kein weiterer Aufwand nötig)

| Issue | Workpaper | Stand |
|-------|-----------|-------|
| #43 — RFC: AAMS is not a Spec | STRAT + RFCT | ✅ Analyse fertig, Option B (Spec → Contract) angenommen. Refactor-Plan mit 5 offenen Decisions. **Implementierung steht an, aber nach Phase 2.** |

### Teilweise abgedeckt

| Issue | Workpaper | Lücke |
|-------|-----------|-------|
| #41 (MantisClaw) | UPD | Empfehlung 3 (Topic Registry maschinenlesbar) — kein Workpaper. Kann warten. |

### Implementierungs-reif (Phase 2 — HEUTE)

| Issue | Titel | Konzept | Implementierung |
|-------|-------|---------|----------------|
| **#48** | Decision-Kompoundierungs-Leck | Diagnose in RES-WIKI Workpaper ✅, Fix konzipiert ✅ | ❌ **NICHT umgesetzt** |
| **#49** | Upgrade-Transparenz | UPD + versioning-system ✅, CHANGELOG-Konzept ✅ | ❌ **NICHT umgesetzt** |

### Neu / Unbearbeitet (Phase 3)

| Issue | Titel | Status |
|-------|-------|--------|
| #47 | Tool Decay & Relative Path Vulnerability | Kein Workpaper |
| #46 | Ordner im Projekt-Root statt WORKING/TOOLS/ | Kein Workpaper |
| #26 | Security Signals in AGENT.json | Kein Workpaper |

### Zu schließen

| Issue | Grund |
|-------|-------|
| #45 | Duplikat von #43 |
| #42 | Duplikat von #41 (aus vorheriger Triage) |

---

## 2. Phase 2 — Heute: Decision-Kompoundierung (#48)

### 2.1 Das Problem (aus #48)

**Kritische Architekturschwärze:** Entscheidungen die in Workpapers getroffen werden versickern. Neue Agents operieren auf veralteter Wahrheit.

**Konkreter Befund:**
- `2026-04-10-AAMS-STRAT` hat **Option B angenommen** (Spec → Contract Umbenennung)
- `2026-04-10-AAMS-RFCT` hat **Refactoring-Plan mit 5 offenen Decisions (E-1 bis E-5)** erstellt
- **WP-001 weiß davon nichts.** WP-001 INDEX.md steht noch auf "⚠️ Pending"
- Ein neuer Agent der WP-001 liest → weiß nicht dass AAMS kein Spec mehr sein soll

### 2.2 Deliverable 1: WP-001 INDEX.md aktualisieren

**Was zu tun ist:**

```
Die "Offene Widersprüche / Pending Decisions"-Tabelle in WP-001 INDEX.md aktualisieren:

| Bereich | Aktueller Stand | Neuer Stand | Tracking |
|---|---|---|---|
| "Spezifikation" → "Contract" Rename | ⚠️ Pending — E-1..E-5 Decisions offen | ✅ Entscheidung getroffen: Option B. E-1..E-5 warten auf Implementierung. | STRAT + RFCT Workpaper, Issue #43 |
```

**Konkrete Änderungen an `WORKING/WHITEPAPER/INDEX.md`:**
- Zeile "Pending Decisions" Tabelle: "Pending" → "Decision getroffen" für Spec→Contract
- Cross-Referenz hinzufügen: `WP-001 ←→ RFCT Workpaper: Spec→Contract Decision + Refactor-Inventar`
- Datum auf 2026-04-24 aktualisieren

### 2.3 Deliverable 2: Decision-Promotion-Checklist in READ-AGENT.md

**Was zu tun ist:**

READ-AGENT.md um einen Abschnitt ergänzen:

```markdown
## Decision-Promotion — Session-End Checklist

Bevor du diese Session schließt, prüfe:

- [ ] Wurde eine Architektur-Entscheidung getroffen?
  - [ ] Ist sie in `WORKING/WHITEPAPER/INDEX.md` eingetragen?
  - [ ] Wurde das betroffene Whitepaper aktualisiert?
- [ ] Existieren offene Decisions in diesem Workpaper?
  - [ ] Sind alle offenen Decisions in einem Whitepaper gepromoted?
  - [ ] Falls nein: Workpaper schließen und erst nach Decision-Promotion wieder öffnen.

**Regel:** Keine offenen Decisions in Workpapers nach Session-Ende.
Die Decision muss in einem Whitepaper leben, nicht im Workpaper.
```

**Wo einfügen:** Nach dem "What this project is" Abschnitt in READ-AGENT.md, vor dem Discovery-System.

### 2.4 Deliverable 3: wiki_lint.py — Cross-Ref-Integrität prüfen

**Aktueller Stand:** `wiki_lint.py` existiert in `WORKING/TOOLS/`. Prüft L1-L7:

| Check | Was er macht | Relevant für #48? |
|-------|-------------|-------------------|
| L1 | Whitepaper-Index vs. Dateien | ✅ — zeigt fehlende WP-Einträge |
| L2 | Stale Whitepapers (>30 Tage) | ✅ — zeigt veraltete WPs |
| L3 | Offene Workpapers ohne TOPIC-Tag | ❌ |
| L4 | **Decision-Promotion** | ✅ **Genau das was wir brauchen** |
| L5 | Cross-Referenzen zwischen WPs | ✅ |
| L6 | LTM-Index Konsistenz | ❌ |
| L7 | Pending-Decision-Marker | ✅ |

**Was zu prüfen ist:**
1. `wiki_lint.py --fix` ausführen — Gibt es bereits L4-L7 Warnungen?
2. Falls L4 existiert: Funktioniert er korrekt gegen unsere aktuelle Struktur?
3. Falls L4 nicht existiert oder fehlerhaft: L4 implementieren — "orphaned decisions" detektieren (Open Decisions in Workpapers die nicht in einem Whitepaper gepromoted wurden)

**Erwartetes Ergebnis:** wiki_lint.py sollte warnen wenn:
- Ein Workpaper "offene Decisions" enthält die nicht in WP-001 INDEX.md stehen
- Ein Whitepaper "Pending" Markierungen hat die älter als 7 Tage sind

### 2.5 Deliverable 4: wiki_lint.py — "Orphaned Decisions" Check

**Neuer Check L4b: Orphaned Decisions**

```python
def check_l4b():
    """Finden offene Decisions in Workpapers die nicht in Whitepapers gepromoted wurden."""
    # 1. Alle Workpapers durchsuchen nach "E-X", "Decision", "offen", "Pending"
    # 2. Alle Whitepapers durchsuchen nach gleichen Keywords
    # 3. Match: Decision in Workpaper aber nicht in Whitepaper → WARN
```

Dieser Check adressiert direkt das Kernproblem von #48.

---

## 3. Phase 2b: Upgrade-Transparenz (#49)

### 3.1 Was bereits konzipiert ist

| Konzept | Workpaper | Stand |
|---------|-----------|-------|
| Versioning-System (semver + CHANGELOG) | `2026-03-27-versioning-system.md` | Konzipiert, nicht umgesetzt |
| Update-Detection-Protocol | `2026-04-10-AAMS-UPD-update-install-detection-protocol.md` | Konzipiert, nicht umgesetzt |

### 3.2 Deliverable 1: CHANGELOG.md anlegen

```markdown
# Changelog

Alle wesentlichen Änderungen an AAMS werden hier dokumentiert.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

## [Unreleased]

## [1.3.0] — 2026-04-24
### Changed
- Spec → Contract Neuausrichtung (RFC #43, STRAT Workpaper)
- WORKSPACE-Discovery-Logik ergänzt (Field Report)
- Update-Detection-Protocol konzipiert (UPD Workpaper)

## [1.2.0] — 2026-04-10
### Added
- WORKSPACE-Container-Discovery
- Bootstrap-Rules for idempotent workspace creation

## [1.1.0] — 2026-03-27
### Added
- Vier-Schichten-Dokumentationsmodell
- LTM/ChromaDB-Integration

## [1.0.0] — 2026-02-18
### Added
- Initial AAMS Specification
```

### 3.3 Deliverable 2: `.aams-version` im `.agent.json`

**Was zu tun ist:** In `.agent.json` ein Feld ergänzen:

```json
"_contract": "AAMS/1.3",
"_version_date": "2026-04-24"
```

Und im UPD-Protokoll definieren: Agent vergleicht `_contract` bei jedem curl-Update mit der lokalen Version. Bei Diskrepanz → `on_update` Handler ausführen.

### 3.4 Deliverable 3: `on_update` Handler in `.agent.json`

**Was zu tun ist:** `.agent.json` um einen neuen entry-point erweitern:

```json
"agent_contract": {
    "on_first_entry": [...],
    "on_session_start": [...],
    "on_update": [
        "Vergleiche `_contract`-Version mit lokaler Version",
        "Bei Minor/Major-Bump: CHANGELOG.md Abschnitt lesen",
        "Bei Major-Bump: User warnen vor Breaking Changes",
        "Aktualisierte READ-AGENT.md schreiben"
    ]
}
```

### 3.5 Deliverable 4: Git-Tags + GitHub Releases

**Nicht im Code, aber nötig:**
- `git tag v1.3.0` für aktuellen Stand
- GitHub Release anlegen mit CHANGELOG-Inhalt
- Nächste Releases: Nur mit Tags + Releases verteilen

---

## 4. Phase 3: Tool-Integrität (#47 + #46)

### 4.1 Gebündelter Ansatz

Beide Issues betreffen denselben Kern: **Agent-Verhaltensregeln für Tool- und Ordner-Management.**

### 4.2 Deliverable 1: AGENTS.md — Pre-Flight Path Check

```markdown
### Before Creating Any Directory or File

- **NEVER** create utility/tool/script folders in the project root
- Check `WORKING/` structure first — `WORKING/TOOLS/` is the designated location
- Before executing any tool: validate its root-anchoring does not point outside WORKING/
- If a tool uses `Path(__file__).resolve().parent.parent` or similar offset paths:
  - Verify it still resolves to the correct root
  - If uncertain: ask before executing
```

### 4.3 Deliverable 2: validate_tools.py (AAMS Doctor)

```python
#!/usr/bin/env python3
"""AAMS Doctor — Validiert Tool-Integrität im Repository."""

# Checks:
# D1: Alle Python-Tools in WORKING/TOOLS/ — keine im Root
# D2: Kein Tool verwendet fragile Offset-Relative Paths
# D3: WORKING/ Struktur ist konsistent mit .agent.json
# D4: Verwaiste Ordner im Root (außer src/, public/, dist/, .git/)
```

---

## 5. Arbeitsplan — Timeline

### HEUTE (2026-04-24)

| # | Deliverable | Issue | Aufwand |
|---|-------------|-------|---------|
| 1 | WP-001 INDEX.md updaten | #48 | 15 min |
| 2 | Decision-Promotion-Checklist in READ-AGENT.md | #48 | 10 min |
| 3 | wiki_lint.py prüfen + L4b "Orphaned Decisions" | #48 | 30 min |
| **Total** | | | **~1h** |

### DEMNÄCHST (nächste Sessions)

| # | Deliverable | Issue | Aufwand |
|---|-------------|-------|---------|
| 4 | CHANGELOG.md anlegen | #49 | 15 min |
| 5 | `.aams-version` + `on_update` Konzept finalisieren | #49 | 30 min |
| 6 | Git-Tag + GitHub Release erstellen | #49 | 10 min |
| 7 | AGENTS.md um Pre-Flight Check ergänzen | #47 + #46 | 15 min |
| 8 | validate_tools.py konzipieren | #47 | 30 min |
| 9 | Issue #45 + #42 schließen | Triage | 2 min |
| **Total** | | | **~2h** |

---

## 6. Offene Fragen vor Implementierung

| Frage | Kontext | Entscheidung nötig? |
|-------|---------|---------------------|
| Soll `_spec` als deprecated Feld in `.agent.json` erhalten bleiben? | RFCT Workpaper E-3 | Ja — backward compat |
| Soll der Spec→Contract Refactor vor #49 kommen? | RFCT sagt: vor Major-Bump | Ja — sonst CHANGELOG erwähnt falsche Begriffe |
| Topic Registry maschinenlesbar (#41-Empf.3) — implementieren oder verschieben? | Niedrige Prio | Verschieben auf Phase 4 |
| Security Signals (#26) — wann implementieren? | Kann warten | Nach Phase 2 |

---

## 7. Priorisierte Reihenfolge der Implementation

```
1. WP-001 INDEX.md updaten          → #48 (5 min)
2. Decision-Promotion in READ-AGENT  → #48 (10 min)
3. wiki_lint.py L4b implementieren   → #48 (30 min)
4. CHANGELOG.md anlegen              → #49 (15 min)
5. Spec→Contract Refactor            → #43 (groß)
6. CHANGELOG nach Refactor updaten   → #49 (15 min)
7. `.aams-version` + `on_update`     → #49 (30 min)
8. Git-Tag + Release                 → #49 (10 min)
9. AGENTS.md Pre-Flight Check        → #47+#46 (15 min)
10. validate_tools.py konzipieren    → #47 (30 min)
11. Issues #45+#42 schließen         → Triage (2 min)
```

---

## 8. Session-Zustand

```
HEUTE erledigt (2026-04-24):
✅ WP-001 INDEX.md aktualisieren — Spec→Contract Decision von "Pending" auf "Decision getroffen"
✅ Decision-Promotion-Checklist in READ-AGENT.md aufgenommen
✅ wiki_lint.py L4b "Orphaned Decisions" implementiert — 16 orphane Decisions in 7 Workpapers gefunden
✅ CHANGELOG.md angelegt (Keep-a-Changelog Format)
✅ .agent.json: _contract + _version_date + on_update + version_detection ergänzt
✅ AGENTS.md: Pre-Flight Path Check ergänzt (Issues #47+#46)
✅ validate_tools.py (AAMS Doctor) erstellt und getestet — D1-D4 Checks, keine Findings

Noch offen (nächste Sessions):
☐ Spec→Contract Refactor starten (RFCT als Blaupause) → Issue #43
☐ Issues #45+#42 schließen → Triage
☐ Topic Registry maschinenlesbar (#41-Empf.3) → Phase 4
☐ Security Signals in AGENT.json (#26) → Phase 4
```

---

> **Session-Ergebnis:** Alle Phase-2-Deliverables abgeschlossen (#48 + #49 Infrastruktur). Wiki-Lint L4b detektiert orphane Decisions in Echtzeit. validate_tools.py (AAMS Doctor) schützt vor Tool Decay. .agent.json kennt jetzt Version und Update-Handler.

---

> **Wichtigste Erkenntnis:** Das Decision-Kompoundierungs-Leck (#48) ist kein Feature-Problem — es ist ein **Prozess-Problem**. Unser System produziert Wissen, aber das Wissen versickert weil es nicht promoted wird. Die Lösung ist keine neue Technologie, sondern eine neue **Disziplin**: Jede Session-Ende → jede Decision muss in einem Whitepaper leben.
