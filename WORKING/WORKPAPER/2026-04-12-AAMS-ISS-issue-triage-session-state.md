# Workpaper: Issue Triage & Session-Standermittlung
# AAMS — Alle offenen Issues geprüft, Abdeckung gegen Workpapers gemapped

**Datum:** 2026-04-12  
**Autor:** @ogerly / DEVmatrose  
**Typ:** Triage / Session-Orientierung  
**Priorität:** Mittel — kein blocking, aber Aufräumen nötig

---

## Session Goal

Alle 9 offenen GitHub-Issues prüfen:
1. Gibt es bereits ein Workpaper dazu?
2. Sind Issues doppelt?
3. Sind Issues bereits implementiert (Commit vorhanden, Issue nur offen gelassen)?
4. Was ist wirklich neu / unbearbeitet?
5. Letzten Arbeitsstand dokumentieren.

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-12-AAMS-ISS-issue-triage-session-state.md` | ✅ |

---

## 1. Issue Triage — vollständige Analyse

### #44 — [RFC] AAMS is not a Spec - it is an Agent Contract
**Geöffnet:** 2026-04-12  
**Inhalt:** Kurze Zusammenfassung — "Empirical analysis shows AAMS defines behavior, not structure."  
**Status:** 🔴 **DUPLIKAT von #43** — dünnerer Content, gleiche These  
**Workpaper-Abdeckung:** ✅ Vollständig durch `2026-04-10-AAMS-STRAT-reorientation-spec-vs-contract.md`  
**Aktion:** Issue #44 schließen als Duplikat von #43

---

### #43 — [RFC] AAMS is not a Spec — it is an Agent Contract
**Geöffnet:** 2026-04-12  
**Inhalt:** Vollständige RFC mit Analyse-Tabelle, konkreten Änderungsvorschlägen (`_spec` → `_contract`), Backward-Compat-Aussagen, WORKSPACE-Verweis  
**Status:** ✅ **NEU — aber vollständig durch Workpapers abgedeckt**  
**Workpaper-Abdeckung:**
- Analyse → `2026-04-10-AAMS-STRAT-reorientation-spec-vs-contract.md` (Abschnitt 3)
- Änderungsinventar → `2026-04-10-AAMS-RFCT-spec-to-contract-refactor-plan.md`
- Backward compat + curl-Invariante → RFCT Abschnitt INV-1/INV-2  
**Offener Punkt im Issue der noch nicht in Workpaper ist:** Keine.  
**Aktion:** Issue offen lassen als öffentlicher RFC-Tracker, mit Verweis auf interne Workpapers in Kommentar

---

### #42 — Feldbericht: AAMS Upgrade v1.0.0 → v1.3.0 (MantisClaw) 
**Geöffnet:** 2026-04-09  
**Status:** 🔴 **DUPLIKAT von #41** — identischer Inhalt, zweimal eingereicht  
**Aktion:** Issue #42 schließen als Duplikat von #41

---

### #41 — Feldbericht: AAMS Upgrade v1.0.0 → v1.3.0 (MantisClaw)
**Geöffnet:** 2026-04-09  
**Inhalt:** Vollständiger MantisClaw-Field-Report. 5 Empfehlungen:
1. `UPGRADING.md` pro Release — **Hoch**
2. `_deviations` in Spec — **Mittel**
3. Topic Registry maschinenlesbar — **Mittel**  
4. `_spec` vs `AAMS_VERSION` klären — **Niedrig**
5. Compatibility Matrix für parallele Features — **Niedrig**

**Workpaper-Abdeckung:**
- Empfehlung 1 (UPGRADING.md) → **vollständig** in `2026-04-10-AAMS-UPD-update-install-detection-protocol.md` (MIGRATION.md-Konzept)
- Empfehlung 2 (`_deviations`) → **bereits implementiert** in Commit 3cde55e (T1: `_deviations in AGENT_SCHEMA.json + AGENT.json + SPEC.md`)
- Empfehlung 3 (Topic Registry maschinenlesbar) → ❌ **NICHT in einem Workpaper** — neue Lücke
- Empfehlung 4 (`_spec` vs `AAMS_VERSION`) → **vollständig** in STRAT + RFCT Workpaper
- Empfehlung 5 (Compatibility Matrix) → ❌ **NICHT in einem Workpaper** — niedrige Prio, kann warten

**Aktion:** Issue offen lassen. Für Empfehlung 3 einen eigenen Work-Item-Eintrag anlegen (siehe Abschnitt 3).

---

### #39 — chore: v1.2.0 release — RFL + Naming Schema
**Geöffnet:** 2026-04-09  
**Inhalt:** Release-Tracking-Issue für v1.2.0 (Naming Schema + RFL)  
**Status:** 🟡 **VERALTET** — v1.2.0 wurde released, v1.3.0 ebenfalls. Issue wurde nicht geschlossen.  
**Workpaper-Abdeckung:** Closed Workpapers `2026-04-09-SPEC-VER-version-centralization.md` + `2026-04-09-rfl-reflection-protocol-step.md`  
**Aktion:** Issue #39 schließen — Release wurde abgeschlossen (Commit c0d63c6 `feat: v1.2.0`).

---

### #26 — feat: Security Signals in AGENT.json
**Geöffnet:** 2026-03-26  
**Inhalt:** Optionale `security`-Sektion in `reference/AGENT.json` und Schema. Scan-Daten, behavioral_signals, trust_score.  
**Status:** 🔵 **OFFEN — kein Workpaper, kein Commit**  
**Workpaper-Abdeckung:** ❌ Keine  
**Priorität:** Niedrig-Mittel — sinnvolles Feature, aber kein Blocker für AAMS/2.0  
**Aktion:** Eigenes Arbeitspaket — nach AAMS/2.0-Refactor angehen. Nicht in RFCT einbauen.

---

### #24 — feat: Blueprint.md 2-Phasen-Workflow in READ-AGENT.md
**Geöffnet:** 2026-03-26  
**Inhalt:** §4 Agent-Specific Workflow Integration in READ-AGENT.md dokumentieren  
**Status:** 🟢 **IMPLEMENTIERT** — Commit 3cde55e: "T4: §4 Agent-Specific Workflow Integration in READ-AGENT.md (blueprint.md 2-phase)"  
**Workpaper-Abdeckung:** Bereits umgesetzt  
**Aktion:** Issue #24 schließen — Implementierung abgeschlossen.

---

### #23 — docs: AAMS-Positionierung vs. CLAUDE.md / GEMINI.md / airules.md
**Geöffnet:** 2026-03-26  
**Inhalt:** Mapping-Tabelle in README.md — AAMS ersetzt CLAUDE.md/GEMINI.md/airules.md  
**Status:** 🟢 **IMPLEMENTIERT** — Commit 3cde55e: "T3: No CLAUDE.md/GEMINI.md/airules.md needed — mapping table in README.md"  
**Aktion:** Issue #23 schließen — Implementierung abgeschlossen.

---

### #22 — docs: ltm-index.md als primäres LTM-Hero-Artefakt
**Geöffnet:** 2026-03-26  
**Inhalt:** ltm-index.md in README als Startpunkt herausstellen, ChromaDB als optional  
**Status:** 🟢 **IMPLEMENTIERT** — Commit 3cde55e: "T2: ltm-index.md LTM setup order table in README.md (start here, not ChromaDB)"  
**Aktion:** Issue #22 schließen — Implementierung abgeschlossen.

---

## 2. Zusammenfassung Triage

| Issue | Titel (kurz) | Status | Aktion |
|-------|-------------|--------|--------|
| #44 | RFC: Spec → Contract (kurz) | Duplikat #43 | **Schließen** |
| #43 | RFC: Spec → Contract (voll) | Workpaper ✅ | Offen als RFC-Tracker |
| #42 | MantisClaw Field Report (kurz) | Duplikat #41 | **Schließen** |
| #41 | MantisClaw Field Report (voll) | Teilweise ✅ | Offen, neue Items |
| #39 | v1.2.0 release chore | Implementiert | **Schließen** |
| #26 | Security Signals AGENT.json | Kein Workpaper | Backlog — post AAMS/2.0 |
| #24 | Blueprint.md 2-Phasen-Workflow | Implementiert | **Schließen** |
| #23 | CLAUDE.md Positionierung | Implementiert | **Schließen** |
| #22 | ltm-index.md Hero | Implementiert | **Schließen** |

**Zu schließen: #44, #42, #39, #24, #23, #22** (6 Issues)  
**Offen zu lassen: #43** (RFC-Tracker), **#41** (Field Report mit offenen Items), **#26** (Security, Backlog)

---

## 3. Neue Lücken aus Issue-Analyse (noch kein Workpaper)

### Lücke A: Topic Registry maschinenlesbar (#41, Empfehlung 3)
**Problem:** Die TOPIC-Tags (ARCH, SPEC, LTM, SEC, etc.) sind nur als Prosa-Beispiele in `.agent.json` erwähnt. Für RFL-Pattern-Matching braucht ein Agent eine maschinenlesbare Liste.

**Vorgeschlagene Lösung (aus #41):**
```json
"topic_registry": {
  "tags": ["ARCH", "SPEC", "LTM", "SEC", "BOOT", "FLD", "RES", "MKT", "ISS", "GOV", "EDU"],
  "extensible": true,
  "_doc": "Official TOPIC tags for workpaper naming. Agents use these for RFL pattern-matching."
}
```

**Priorität:** Mittel — relevant für AAMS/2.0, passt gut in den RFCT-Plan (Phase 1 `.agent.json`)  
**Passt in:** RFCT-Workpaper als Change 2.1-Ergänzung (oder separater mini-change)

### Lücke B: Compatibility Matrix (#41, Empfehlung 5)
**Problem:** Wenn Frameworks (MantisClaw etc.) Features bereits unabhängig entwickelt haben, fehlt eine Übersicht "If you already have X, AAMS-Y relates as..."  
**Priorität:** Niedrig — nice-to-have, kein Blocker  
**Passt in:** Separates Whitepaper oder SPEC.md-Abschnitt, nach AAMS/2.0

---

## 4. Aktueller Arbeitsstand — AAMS gesamt

### Was wurde zuletzt getan (letzte Session 2026-04-10/11)

```
76f6b5c — Commit: workpaper: AAMS/2.0 strategic reorientation
  ├── 2026-04-10-AAMS-WORKSPACE-field-report-workspace-container.md
  │     WORKSPACE-Container-Layer-Lücke, Discovery-Logik, Konflikt-Check
  ├── 2026-04-10-AAMS-STRAT-reorientation-spec-vs-contract.md
  │     Strategische Entscheidung: AAMS = Agent-Contract, kein Spec
  ├── 2026-04-10-AAMS-RFCT-spec-to-contract-refactor-plan.md
  │     23+ Stellen, 11 Dateien, Invarianten INV-1..4, 5 Pre-Decisions
  └── 2026-04-10-AAMS-UPD-update-install-detection-protocol.md
        Install/Update Detection: 3 Szenarien, .aams-state, on_update
```

### Noch NICHT entschieden (Pre-Decisions E-1 bis E-5 aus RFCT-Workpaper)

| # | Entscheidung | Blockiert |
|---|-------------|-----------|
| E-1 | AAMS-Akronym-Schicksal: Eigenname oder neues Wort für "S"? | README, AGENTS.md, alle Taglines |
| E-2 | `_spec` → `_contract` hard oder dual? | `.agent.json`, AGENT.json, AGENT_SCHEMA.json |
| E-3 | `reference/SPEC.md` umbenennen oder behalten? | externe Links, README |
| E-4 | GitHub Repo Description ändern? | GitHub Web |
| E-5 | Version: AAMS/2.0 oder AAMS/1.4? | Alle Version-Strings |

**Kein einziger File-Change wurde für AAMS/2.0 bisher implementiert — nur Workpapers.**  
Die Arbeit ist dokumentiert, die Umsetzung steht aus.

### Nächster logischer Schritt

E-1 bis E-5 entscheiden. Dann Phase 1 des RFCT-Plans starten: `.agent.json` + AGENT_SCHEMA.json + AGENT.json.

---

## 5. Offene Issues die jetzt nicht angegangen werden

| Issue | Grund für Defer |
|-------|----------------|
| #26 Security Signals | Feature-Addition, kein Blocker für AAMS/2.0. Nach Refactor. |
| #41 (Empfehlung 5) Compat Matrix | Niedrige Prio, kein konkreter Bedarf |

---

## Key Findings

- **6 von 9 Issues sollten geschlossen werden** — 2 Duplikate, 4 bereits implementiert (Commit 3cde55e)
- **#43 + #41 bleiben offen** — als RFC-Tracker bzw. als Quelle für Backlog-Items
- **Neue Lücke identifiziert:** Topic Registry als maschinenlesbares Array fehlt in `.agent.json`  
- **Letzter Ist-Stand:** Nur Workpapers erstellt, keine einzige Datei für AAMS/2.0 noch geändert
- **Blocker:** 5 strategische Entscheidungen (E-1 bis E-5) — ohne die startet der Refactor nicht

---

## Next Steps

- [ ] Issues #44, #42, #39, #24, #23, #22 auf GitHub schließen
- [ ] E-1 bis E-5 entscheiden (User-Entscheidung)
- [ ] Topic Registry als maschinenlesbares Feld in RFCT-Inventar aufnehmen
- [ ] Nach E-1..E-5: Phase 1 RFCT starten (`.agent.json` → `_contract` field)
- [ ] Workpaper schließen → MEMORY ingesten

---

*Workpaper erstellt: 2026-04-12 — vollständige Issue-Triage, Session-Orientierung wiederhergestellt*
