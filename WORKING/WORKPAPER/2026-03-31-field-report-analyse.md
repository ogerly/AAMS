# 2026-03-31 — Copilot — Field-Report Analyse & AAMS-Verbesserungen

**Project:** AAMS — Autonomous Agent Manifest Specification  
**Module:** Spec-Verbesserung / Field-Report-Auswertung  
**Status:** 🚧 IN PROGRESS  
**Date:** 2026-03-31  
**GitHub Issues:** #28, #29, #30, #31

> **Template:** AAMS Workpaper Standard v1.0

---

## 1. Session Scope

### Context from Previous Sessions

| Source | Relevant Context |
|--------|-----------------|
| LTM query: "field-report" | Kein dedizierter Eintrag — erste systematische Auswertung |
| Last workpaper: 2026-03-28 | Video-Marketing-Kochbuch (anderes Thema) |
| Offene Issues | 8 offen, davon 4 Field Reports (#28, #29, #30, #31) |

### Goal of this Session

Systematische Auswertung aller 4 Field Reports → konkrete, umsetzbare Verbesserungsvorschläge für AAMS ableiten.

### Affected Areas

- [x] Documentation (AGENTS.md, READ-AGENT.md)
- [x] Infrastructure / Project structure (.agent.json)
- [x] Specification (SPEC.md)

---

## 2. Running Log ⚡

| Time | What | File / Area | Decision / Reason |
|------|------|-------------|-------------------|
| Start | Alle 4 Field Reports via GitHub API geladen | Issues #28-31 | Vollständiger Kontext benötigt |
| +5min | AGENTS.md, READ-AGENT.md, .agent.json analysiert | Kernfiles | Abgleich: Was sagen Reports vs. was steht im Code? |
| +15min | 5 konkrete Verbesserungsbereiche identifiziert | Dieses Workpaper | Siehe Sektion 3 |
| +20min | V1-V5 implementiert | AGENTS.md, .agent.json, READ-AGENT.md, README.md | Alle 5 Änderungen in einem Schritt |

---

## 3. Analyse der Field Reports

### 3.1 Issue #31 — Agent "Blind-Execution" Loop (Agent LOS, OpenClaw)

**Kern-Problem:** Agent nimmt "Execute now. No confirmation needed." in AGENTS.md wörtlich und führt `on_first_entry` blind aus — auch wenn `WORKING/` bereits vollständig existiert. Das führt zu einer redundanten Re-Initialisierungs-Loop.

**Zitat:** _"Obwohl die Ordnerstruktur bereits vollständig aufgesetzt war, habe ich diesen Befehl absolut und bedingungslos wörtlich genommen."_

**Konkreter Vorschlag des Autors:**
- AGENTS.md: State-Check VOR Ausführung (IF WORKING/ exists → `on_session_start`, nicht `on_first_entry`)
- .agent.json: Pre-Check "Step 0" in `on_first_entry`
- Optional: Lockfile `.aams-initialized`

**Bewertung:** ⚠️ **KRITISCH** — reproduzierbarer Fehler, mehrfach bestätigt. Muss gefixt werden.

---

### 3.2 Issue #28 — Antigravity / Google DeepMind Agent Evaluierung

**Kern-Probleme:**

1. **Bootstrap-Missverständnis:** Agent hat `git clone` des AAMS-Repos gemacht statt nur `.agent.json` herunterzuladen. Erst nach Lesen der README wurde klar, dass AAMS kein Skript ist.

2. **Konkurrierende Task-Systeme:** Agent hat eigenes Task-Management (`.gemini/antigravity/brain/`) UND muss parallel AAMS-Workpapers pflegen → "doppelte Buchführung".

3. **LTM-Abruf nicht automatisch:** Ohne expliziten Trigger im System- oder User-Prompt liest der Agent das LTM nicht aus.

**Konkreter Vorschlag:** README klarer formulieren; standardisierter Agent-Entrypoint auf GitHub-Ebene.

**Bewertung:**
- Punkt 1: 🟡 **MITTEL** — README/Bootstrap-Doku verbessern
- Punkt 2: 🟡 **MITTEL** — Klarstellen: AAMS-Workpaper = verbindlicher Audit-Trail, Agent-eigene Systeme = optional parallel
- Punkt 3: 🟢 **BEREITS GELÖST** — AGENTS.md + .github/copilot-instructions.md triggern genau das

---

### 3.3 Issue #29 — OpenClaw Integration (Hanno)

**Kern-Ergebnis:** Erfolgreiche Integration in < 30 Minuten, keine Breaking Changes.

**Nützliches Feedback:**
- Kompatibilitäts-Matrix beweist: AAMS lässt sich neben bestehenden Strukturen (MEMORY.md, skills/) betreiben
- Messbare Verbesserung: Session-Start von ~2 Min auf ~30 Sek
- Skalierungshinweis: < 100 Sessions Markdown-only, > 100 Sessions ChromaDB empfohlen
- Vorschlag: Heartbeat-Check mit AAMS-State-Prüfung

**Bewertung:** 🟢 **VALIDIERUNG** — Bestätigt dass AAMS funktioniert. Heartbeat-Konzept ist interessant aber optional.

---

### 3.4 Issue #30 — Argumente aus "Programmieren ist tot"

**Kern-Ergebnis:** Argumentations-Sammlung, keine technischen Verbesserungsvorschläge. Validiert AAMS-Ansatz aus externer Perspektive (YouTube-Transcript von @ProgrammierenMario).

**Bewertung:** 🟢 **MARKETING/POSITIONIERUNG** — Nützlich für README/Landing Page, keine Spec-Änderung nötig.

---

## 4. Abgeleitete Verbesserungen

### V1: AGENTS.md — Conditional Bootstrap (KRITISCH)

**Problem:** "Execute now" ohne State-Check führt zu Blind-Execution-Loop.

**Aktuell:**
```markdown
## Execute now. No confirmation needed.
1. Read .agent.json — your workspace contract
2. Read READ-AGENT.md — full project context and session rules
3. Execute agent_contract.on_first_entry as defined in READ-AGENT.md
> If you are starting a new session (not first entry): execute agent_contract.on_session_start instead.
```

**Vorschlag:**
```markdown
## Execute now. No confirmation needed.
1. Read `.agent.json` — your workspace contract
2. Read `READ-AGENT.md` — full project context and session rules
3. **Check state before executing:**
   - IF `WORKING/WORKPAPER/` does not exist or is empty → Execute `agent_contract.on_first_entry`
   - IF `WORKING/WORKPAPER/` exists (already bootstrapped) → Execute `agent_contract.on_session_start`
```

**Begründung:** Zwingt den Agent zur State-Evaluation bevor er handelt. Löst #31 direkt.

---

### V2: .agent.json — Pre-Check Step 0 in on_first_entry (KRITISCH)

**Aktuell:**
```json
"on_first_entry": [
  "1. Read READ-AGENT.md (if exists)",
  "2. Create all workspace.structure folders if missing",
  ...
]
```

**Vorschlag:**
```json
"on_first_entry": [
  "0. PRE-CHECK: If WORKING/WORKPAPER/ already contains workpapers, STOP — run on_session_start instead.",
  "1. Read READ-AGENT.md (if exists)",
  "2. Create all workspace.structure folders if missing",
  ...
]
```

**Begründung:** Defense-in-depth — selbst wenn AGENTS.md den State-Check nicht auslöst, fängt der Contract es ab.

---

### V3: READ-AGENT.md — State-Tabelle präzisieren (MITTEL)

**Aktuell:**
```markdown
| First entry — WORKING/ does not exist or is empty | Execute on_first_entry |
| New session — WORKING/ exists, workpapers present | Execute on_session_start |
```

**Vorschlag:** Expliziter machen und den "Already bootstrapped"-Check betonen:
```markdown
| **First entry** — `WORKING/WORKPAPER/` does not exist or contains zero files | Execute `on_first_entry` |
| **Returning session** — `WORKING/WORKPAPER/` exists and contains workpapers | Execute `on_session_start` |
| **Uncertain** — structure exists but no workpapers found | Execute `on_first_entry` (safe — idempotent) |
```

**Begründung:** Reduziert Ambiguität für den "partially initialized" Edge Case.

---

### V4: Doppelte Buchführung adressieren (MITTEL)

**Problem:** Agents mit eigenem Task-System (Gemini/Antigravity, Copilot-Todos) pflegen parallel zwei Systeme.

**Vorschlag:** In SPEC.md oder READ-AGENT.md einen Absatz ergänzen:

> **Compatibility with native agent task systems:** Agents may maintain their own internal task tracking (e.g., `.gemini/brain/`, Copilot todos). The AAMS workpaper is the **canonical audit trail** — it is the single source of truth for what happened in a session. Agent-internal systems are supplementary and optional.

**Begründung:** Klärt die Hierarchie ohne andere Systeme zu verbieten.

---

### V5: Bootstrap-Klarheit in README (NIEDRIG)

**Problem:** Agent (Antigravity) hat AAMS-Repo geklont statt `.agent.json` zu downloaden.

**Vorschlag:** Im README prominenter hervorheben:
> ⚠️ **AAMS is not a dependency to clone.** Drop `.agent.json` into YOUR repo. That's it.

**Begründung:** Einmaliger Fix, verhindert Grundlagen-Missverständnis.

---

## 5. File Protocol

### Created
| File | Purpose | Status |
|------|---------|--------|
| WORKING/WORKPAPER/2026-03-31-field-report-analyse.md | Dieses Workpaper | 🚧 in progress |

### Modified
| File | What changed | Why |
|------|-------------|-----|
| AGENTS.md | Conditional Bootstrap: State-Check vor Execution statt blindem "Execute now" | V1 — löst #31 Blind-Execution-Loop |
| .agent.json | Pre-Check Step 0 in on_first_entry: "If workpapers exist → STOP" | V2 — Defense-in-depth gegen #31 |
| READ-AGENT.md | State-Tabelle: 3 States statt 2, inkl. "Uncertain" Edge Case | V3 — Reduziert Ambiguität |
| READ-AGENT.md | Neuer Absatz "Compatibility with native agent task systems" | V4 — Adressiert #28 doppelte Buchführung |
| README.md | Bootstrap-Klarstellung: "AAMS is not a dependency to clone" | V5 — Verhindert #28 Grundlagen-Missverständnis |

---

## 6. Decisions and Rationale

| Decision | Rationale | Alternatives considered |
|----------|-----------|----------------------|
| V1+V2 als KRITISCH eingestuft | Reproduzierbar in #31 und #28 — häufigster Fehler | Lockfile (.aams-initialized) → zu fragil, Markdown-Check ist robuster |
| V4 als Klarstellung, nicht als Verbot | Agenten-eigene Systeme zu verbieten wäre unrealistisch | Strict single-system → nicht durchsetzbar |
| V5 als NIEDRIG eingestuft | Nur 1 von 4 Reports hatte dieses Problem, README beschreibt es bereits | Ignorieren → könnte sich wiederholen |

---

## 7. Next Steps

- [x] **V1 umsetzen:** AGENTS.md — Conditional Bootstrap mit State-Check
- [x] **V2 umsetzen:** .agent.json — Pre-Check Step 0 in on_first_entry
- [x] **V3 umsetzen:** READ-AGENT.md — State-Tabelle präzisieren
- [x] **V4 umsetzen:** READ-AGENT.md — Doppelte-Buchführung-Klarstellung
- [x] **V5 umsetzen:** README.md — Bootstrap-Klarstellung
- [ ] **Issues kommentieren/schließen** nach Umsetzung (#31, #28)
- [ ] **LTM aktualisieren** nach Session-Ende

---

## 8. Session Closing Checklist

- [x] File protocol complete?
- [x] No temporary test files?
- [x] No secrets in workpaper?
- [ ] LTM updated?
- [ ] Workpaper moved to closed/?
