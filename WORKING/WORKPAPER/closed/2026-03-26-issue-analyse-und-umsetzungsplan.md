# WORKPAPER — Issue-Analyse & Umsetzungsplan

**Session:** 2026-03-26  
**Status:** CLOSED  
**Agent:** GitHub Copilot / Claude Sonnet 4.6  
**Typ:** AAMS Self-Check · GitHub Issue Review · Umsetzungsplan

---

## Session Scope

AAMS-Selbstcheck (Kontrakt, Workspace, Git-Status), vollständiger GitHub Issue Review  
(alle offenen Issues), konsolidierte Analyse und priorisierter Umsetzungsplan für  
die nächsten Implementierungen.

---

## AAMS Self-Check

### Kontrakt-Check

| Datei | Status | Befund |
|-------|--------|--------|
| `.agent.json` | ✅ | AAMS-MINI/1.0, alle Felder korrekt, `gitignore_patterns` mit glob+negation |
| `AGENTS.md` | ✅ | Tool-Bridge, verweist auf `READ-AGENT.md` + `reference/AGENT.json` |
| `READ-AGENT.md` | ✅ | Dual-track LTM, AAMS-MINI vs full, Diary Layer, State Recovery |
| `reference/SPEC.md` | ✅ | In `reference/` nach Konsolidierung 30c3631 |
| `reference/AGENT.json` | ✅ | Verschoben in Session 2026-03-03 |
| `reference/AGENT_SCHEMA.json` | ✅ | Verschoben in Session 2026-03-03 |
| `docs/index.html` | ✅ | GitHub Pages One-Pager aktiv |
| LTM-Audit-Log | ✅ | 67 Einträge — unter Warnschwelle (90) |

### Git-Status

- **HEAD:** `30c3631` → `refactor: consolidate spec material into reference/`
- **Remote:** `origin/main` = HEAD → sauber, kein Rückstand
- **Working Tree:** clean (keine uncommitted Changes)
- **Letzter Commit-Inhalt:** reference/ Konsolidierung aus Session 2026-03-03 committed

### Workspace-Anomalien

| Problem | Befund | Aktion |
|---------|--------|--------|
| **4 offene Workpapers** | `2026-02-22-feldtest-independentes-repo.md`, `2026-02-23-fix-ltm-python-interpreter.md`, `2026-02-24-diary-layer-konzept.md`, `2026-03-03-session-check-issues-review.md` — alle nicht nach `closed/` verschoben | → Session-Close nachholen (T7) |
| **T1–T5 aus 2026-03-03** | Alle Tasks noch offen — keine weitere Implementierung seit letzter Session | → Diese Session |
| **Keine neue LTM-Ingestion** | Letzter Ingest: 2026-02-28 laut ltm-index.md | → Nach Session-Close |

---

## GitHub Issues — Vollständiger Review (Stand 2026-03-26)

### Offene Issues: 9

| # | Titel | Autor | Datum | Typ |
|---|-------|-------|-------|-----|
| #20 | AAMS Erfolgsbericht: DevMatroses Testcenter (Antigravity) | ogerly | 2026-03-21 | field-report |
| #19 | ImprintGuard Agent: Gemini — AAMS-Integration Statusbericht | ogerly | 2026-03-04 | field-report |
| #18 | Report: GEMINI.md / airules.md | ogerly | 2026-03-03 | — |
| #17 | Field Report: AAMS in a Real Production Project (Luna-1) | ogerly | 2026-03-02 | field-report |
| #16 | Report & Guideline: Gemini/Firebase Studio Workflow in AAMS | ogerly | 2026-03-02 | field-report |
| #15 | Proposal: Agent-Specific Planning Artifacts in AAMS | ogerly | 2026-03-02 | enhancement, documentation |
| #14 | CLAUDE.md in Claude-Code-Projekte — Hintergrund & Trend | ogerly | 2026-03-01 | — |
| #8 | Feature: Security Signals in AGENT.json | AgentGurke | 2026-02-27 | — |
| #7 | Feature: Security Audit Fields in AGENT.json | AgentGurke | 2026-02-27 | — |

---

### Detailanalyse

#### #20 — AAMS Erfolgsbericht: DevMatroses Testcenter (NEU)
**Status:** NEU — seit letzter Session  
**Inhalt:** Lokales, KI-gestütztes API E2E-Testtool (FastAPI + LLMs) wurde auf AAMS migriert.  
**Implementierungs-Schritte laut Report:**
1. `AGENTS.md` + `.agent.json` als Root-Bridge heruntergeladen
2. `READ-AGENT.md` mit projektspezifischen Konventionen erstellt (FastAPI, lokale Ausführung, Security-Guard)
3. `WORKING/` Struktur angelegt
4. Agenten starten via `on_session_start`, schreiben am Ende Workpaper → `ltm-index.md`

**Kern-Aussage:** AAMS verleiht einem Agenten-gestützten Tool strukturiertes Langzeitgedächtnis. Neue Mitarbeiter (menschlich oder KI) können Status sofort erfassen, ohne in Logs zu suchen.

**Bedeutung für AAMS:** 
- Zweiter Produktions-Feldtest (neben Luna-1 #17) → Muster bestätigt
- Antigravity (Gemini CLI / Firebase Studio) als Agent genutzt → bestätigt #16/#18 Relevanz
- Keine neuen Spec-Lücken — aber starkes Argument für Bootstrap-Verbesserungen (onboarding)

---

#### #19 — ImprintGuard Agent: Gemini AAMS-Integration (NEU)
**Status:** NEU — seit letzter Session  
**Inhalt:** Gemini-Agent in Firebase Studio integriert AAMS in ImprintGuard-Repo (Security Layer Architektur-Tool).

**Durchgeführte Aktionen laut Report:**
- AAMS-Struktur initialisiert (`WORKING/` + Unterordner)
- Repository gescannt, README analysiert
- Initiales Workpaper erstellt
- READ-AGENT.md angelegt
- Whitepaper für Security Layer initiiert
- Architekturentscheidungen: Unix Domain Sockets (IPC), In-Memory Nonce Store (Replay-Schutz)

**Offene Punkte im Report:**
- Liveness Detection Grenzen noch nicht final dokumentiert
- Whitepaper-Abschluss ausstehend
- LTM-Ingestion (`AGENT-MEMORY/`) steht noch aus

**Bedeutung für AAMS:**  
- Zeigt: Gemini in Firebase Studio folgt AAMS ohne Reibung, wenn Agent prompts korrekt sind
- Bestätigt die Blueprint.md 2-Phasen-Workflow-Relevanz (#15/#16)
- Zeigt: `READ-AGENT.md`-Erstellung durch Gemini funktioniert autonomous

---

#### #18 — Report: GEMINI.md / airules.md
**Inhalt:** Detaillierte Aufschlüsselung der GEMINI.md in Firebase Studio (Persona, Tech Stack, Coding Standards, Workflow-Modi). Limits: Token-Bloat bei langen Dateien, Halluzinationen bei widersprüchlichen Anweisungen.  
**Kernpunkt:** Firebase Studio priorisiert `.idx/airules.md` vor `GEMINI.md`. JIT-Kontext via Unterordner-GEMINI.md.

**Zusammenhang:** Direkt mit #14 (CLAUDE.md-Trend) und #15/#16 (Gemini-Workflow) verknüpft.  
**AAMS-Relevanz:** Jedes Ökosystem hat seine eigene Config-Datei. AAMS muss sich explizit und klar davon abgrenzen.

---

#### #17 — Field Report Luna-1 (4 Monate Produktion)
**Was funktioniert:**
- 3-Layer Model ist in der Praxis "load-bearing" (nicht theoretisch)
- Vector LTM (ChromaDB, 2120 Chunks) = höchster Wert
- Workpaper-Disziplin verhindert "Where Were We"-Syndrom
- Security Zero Policy: 0 Secret Leaks

**Friction Points:**
1. Chat Agents bootstrappen sich nicht selbst — User muss explizit prompten
2. Naming Drift: `close/` vs `closed/` — 50+ Dateien, Deviation dokumentiert
3. `ltm-index.md` Track fehlte bis zur Adoption
4. `AGENTS.md` Bridge fehlte am Anfang
5. Folder Naming vs Spec → 40+ Cross-References verhindern Umbenennung

**5 Empfehlungen (direkt umsetzbar):**
1. `ltm-index.md` als Hero Artifact — survives fresh clone, GitHub-lesbar
2. `_deviations` als offizielles Schema-Feld in `.agent.json`
3. `AGENTS.md` vor `.agent.json` im Onboarding
4. Session-Start Prompts / VS Code Snippets für Copilot Chat
5. `workpapers_closed_aliases` Feld erwägen

---

#### #16 — Blueprint.md 2-Phasen-Workflow (Gemini/Firebase Studio)
**Inhalt:** Konkreter Zwei-Phasen-Workflow für `blueprint.md`:
- Phase 1: `blueprint.md` = ephemerales Live-Planungs-Dokument (während der Task im Root)
- Phase 2: AAMS Formalisierung → Workpaper + Whitepaper erstellen → `blueprint.md` löschen

**Umzusetzende Aktion:** Neuer Abschnitt in `READ-AGENT.md` unter "4. Agent-Specific Workflows"

---

#### #15 — Proposal: Agent-Specific Planning Artifacts
**Inhalt:** Formaler Proposal (von Gemini eingereicht) für denselben Ansatz wie #16.  
**Verhältnis zu #16:** #15 = Proposal, #16 = konkretes Guideline. Nach Implementierung von #16 → #15 schließen.

---

#### #14 — CLAUDE.md Trend (März 2026)
**Trend:** Lange CLAUDE.md (>150 Zeilen) schaden der Antwortqualität → kürzen auf 20-60 Zeilen.  
**AAMS-Status:** Kein CLAUDE.md — stattdessen `AGENTS.md` + `.agent.json` + `READ-AGENT.md`.  
**Umsetzung:** Abschnitt in `README.md` oder `SPEC.md`: "Warum kein CLAUDE.md/GEMINI.md?"  

---

#### #8 + #7 — Security Signals in AGENT.json (AgentGurke)
**#8 Vorschlag** — `security`-Sektion:
```json
{
  "security": {
    "last_scan": "...",
    "scan_type": "dependency-vulnerability",
    "findings": { "critical": 0, "high": 0, "medium": 1, "low": 3 },
    "deployed_services": [...],
    "behavioral_signals": { "sessions_without_incident": 48, "trust_score": 0.97 }
  }
}
```

**#7 Vorschlag** — `security_audit`-Sektion (nahezu identisch, Basis für #8-Implementierung).  
**Entscheidung:** #8 als Basis (neueres Issue, klarere Struktur), #7 schließen nach Implementierung.

---

## Issue-Kategorisierung & Priorisierung

| # | Typ | Priorität | Aktion |
|---|-----|-----------|--------|
| #17 | Production Field Report (Luna-1) | **HIGH** | 5 Empfehlungen → Spec + Schema + README |
| #20 | Field Report (Testcenter) | **HIGH** | Bestätigung + Bootstrap-Prozess verbessern |
| #18 | Report GEMINI.md/airules.md | **HIGH** | Mit #14 → AAMS-Positionierung schärfen |
| #14 | CLAUDE.md-Trend | **HIGH** | Abschnitt README.md: "Warum kein CLAUDE.md?" |
| #16 | Blueprint.md Workflow Guideline | **MEDIUM** | → READ-AGENT.md neuer Abschnitt |
| #15 | Proposal Planning Artifacts | **MEDIUM** | Nach #16 Impl. → schließen |
| #19 | Field Report ImprintGuard | **LOW** | Bestätigung, keine Spec-Lücken |
| #8 | Security Signals (Basis) | **LOW** | → AGENT.json + AGENT_SCHEMA.json |
| #7 | Security Audit (Duplikat) | **LOW** | Nach #8 Impl. → schließen |

---

## Umsetzungsplan — Taskübersicht

### T1 — `_deviations` als offizielles Schema-Feld *(HIGH — aus #17)*
**Ziel:** Projekte die AAMS auf bestehende Strukturen aufsetzen können abweichende Pfade formal dokumentieren.

**DoD (Definition of Done):**
- [ ] `reference/AGENT_SCHEMA.json` — `_deviations` Objekt-Feld mit `properties.spec_path`, `properties.actual_path`, `properties.reason`
- [ ] `reference/AGENT.json` — Beispiel-`_deviations` aus Luna-1 ergänzen
- [ ] `reference/SPEC.md` — Unterabschnitt "Deviations" unter workspace → erklärt Konzept und zeigt Beispiel

---

### T2 — `ltm-index.md` als Hero Artifact herausstellen *(HIGH — aus #17)*
**Ziel:** Neuen AAMS-Adoptern klarstellen: `ltm-index.md` zuerst einrichten, ChromaDB ist optional.

**DoD:**
- [ ] `README.md` — Sektion "LTM: Start here" mit `ltm-index.md` als primärem Artefakt
- [ ] Setup-Reihenfolge: `ltm-index.md` → `ChromaDB` (nicht umgekehrt)
- [ ] `.agent.json` — `ltm_mode: "markdown"` als default klarer dokumentieren

---

### T3 — AAMS-Positionierung vs. CLAUDE.md / GEMINI.md / airules.md *(HIGH — #14 + #18)*
**Ziel:** Klare, knapp gehaltene Erklärung warum AAMS kein tool-spezifisches Config-File braucht/empfiehlt.

**DoD:**
- [ ] `README.md` — Neuer Abschnitt "Why no CLAUDE.md / GEMINI.md?" (max. 8 Zeilen)
- [ ] Mapping-Tabelle: `CLAUDE.md` / `GEMINI.md` / `airules.md` / `CURSOR` → werden durch `AGENTS.md` + `.agent.json` ersetzt
- [ ] Optionaler Hinweis: Falls doch tool-spezifisch → keep short, point to AGENTS.md

---

### T4 — Blueprint.md 2-Phasen-Workflow in READ-AGENT.md *(MEDIUM — #15 + #16)*
**Ziel:** Agenten die Gemini/Firebase Studio nutzen wissen explizit wie temporäre Planungsartefakte mit AAMS koexistieren.

**DoD:**
- [ ] `READ-AGENT.md` — Neuer Abschnitt "§4 Agent-Specific Workflow Integration"
- [ ] Phase 1 (Live Planning mit `blueprint.md`) dokumentiert
- [ ] Phase 2 (AAMS Formalisierung + Cleanup) dokumentiert
- [ ] Regel: `blueprint.md` ist ephemeral, wird nach Formalisierung gelöscht
- [ ] #15 auf GitHub schließen nach Impl.

---

### T5 — Session-Start Prompts verbessern *(MEDIUM — aus #17 + #20)*
**Ziel:** Chat-Agent-Bootstrap-Gap minimieren. 80% Compliance-Steigerung ohne technischen Umbau.

**DoD:**
- [ ] `reference/prompts/bootstrap.md` — Prompt-Set für Copilot Chat Session Start reviewen/verbessern
- [ ] Optionaler Schritt: VS Code Workspace Snippet für `on_session_start` Prompt dokumentieren
- [ ] `README.md` — Hinweis auf `bootstrap.md` als empfohlener Session-Start für Chat-Agenten

---

### T6 — Security Signals in AGENT.json *(LOW — #7 + #8)*
**Ziel:** Manifest wird zu Trust-Artefakt für Multi-Agent-Szenarien.

**DoD:**
- [ ] `reference/AGENT.json` — `security`-Sektion gemäß #8-Vorschlag ergänzen
- [ ] `reference/AGENT_SCHEMA.json` — Schema für `security`-Objekt mit allen Feldern
- [ ] `reference/SPEC.md` — kurze Erwähnung als optionales Feld
- [ ] #7 schließen nach Impl. (Duplikat)

---

### T7 — Offene Workpapers schließen *(SESSION-HYGIENE)*
**Ziel:** Workspace-Ordnung wiederherstellen.

**DoD:**
- [ ] `2026-02-22-feldtest-independentes-repo.md` → nach `closed/` verschieben
- [ ] `2026-02-23-fix-ltm-python-interpreter.md` → nach `closed/` verschieben
- [ ] `2026-02-24-diary-layer-konzept.md` → nach `closed/` verschieben
- [ ] `2026-03-03-session-check-issues-review.md` → nach `closed/` verschieben (nach LTM-Ingest)
- [ ] LTM-Audit-Log (`ltm-index.md`) mit neuen Einträgen befüllen

---

## Reihenfolge der Umsetzung

```
[1] T1: _deviations Schema          → reference/AGENT_SCHEMA.json + AGENT.json + SPEC.md
[2] T2: ltm-index.md als Hero        → README.md
[3] T3: AAMS vs CLAUDE.md/GEMINI.md  → README.md (gleicher Edit wie T2)
[4] T4: Blueprint.md Workflow         → READ-AGENT.md
[5] T5: Bootstrap Prompts             → reference/prompts/bootstrap.md + README.md
[6] T6: Security Signals              → AGENT.json + AGENT_SCHEMA.json + SPEC.md
[7] T7: Workpapers schließen          → Session-End
```

> **Startreihenfolge:** T1 → T2+T3 (zusammen, beide in README.md) → T4 → T5 → T6 → T7

---

## File Protocol

| Action | File | Detail |
|--------|------|--------|
| CREATED | `WORKING/WORKPAPER/2026-03-26-issue-analyse-und-umsetzungsplan.md` | Diese Session |
| EDITED | `reference/AGENT_SCHEMA.json` | T1: `_deviations` Array-Feld als offizielle Property ergänzt |
| EDITED | `reference/AGENT.json` | T1: Beispiel-`_deviations` aus Luna-1 ergänzt (2 Einträge) |
| EDITED | `reference/SPEC.md` | T1: Neuer Abschnitt `_deviations — Intentional Deviations` vor `_ Annotation Convention` |
| EDITED | `README.md` | T2: LTM Setup Order Tabelle in Four-Layer Section |
| EDITED | `README.md` | T3: No CLAUDE.md/GEMINI.md/airules.md Sektion + Mapping-Tabelle in Works With Every Agent |
| EDITED | `READ-AGENT.md` | T4: Neuer Abschnitt §4 Agent-Specific Workflow Integration (Blueprint.md 2-Phasen-Workflow) |
| MOVED | `WORKING/WORKPAPER/2026-02-22-feldtest-independentes-repo.md` → `closed/` | T7: Workpaper-Hygiene |
| MOVED | `WORKING/WORKPAPER/2026-02-23-fix-ltm-python-interpreter.md` → `closed/` | T7: Workpaper-Hygiene |
| MOVED | `WORKING/WORKPAPER/2026-02-24-diary-layer-konzept.md` → `closed/` | T7: Workpaper-Hygiene |
| MOVED | `WORKING/WORKPAPER/2026-03-03-session-check-issues-review.md` → `closed/` | T7: Workpaper-Hygiene |
| GITHUB | Issues #21–#26 | Neue Issues: T1 (_deviations), T2 (ltm hero), T3 (CLAUDE.md/GEMINI.md pos.), T4 (blueprint), T5 (bootstrap prompts), T6 (security signals) |
| GITHUB | Issue #8 closed | Superseded by #26 (Security Signals) — Tracking in #26 |
| GITHUB | Issue #14 closed | T3 implementiert (README.md CLAUDE.md/GEMINI.md Positionierung) |
| GITHUB | Issue #16 closed | T4 implementiert (§4 Blueprint.md in READ-AGENT.md) |
| GITHUB | Issue #17 closed | Alle 5 Empfehlungen umgesetzt (T1–T4 + #25 offen) |
| GITHUB | Issue #18 closed | T3 implementiert (GEMINI.md/airules.md Mapping in README.md) |
| GITHUB | Issue #19 closed | Field Report anerkannt, §4 READ-AGENT.md adressiert Use Case |
| GITHUB | Issue #20 closed | Field Report anerkannt, Bootstrap-Gap → #25 |

---

## AAMS Self-Check Ergebnis

**Gesamtstatus: ⚠️ NEEDS WORK**

| Bereich | Status | Kritikalität |
|---------|--------|-------------|
| Kontrakt-Dateien | ✅ Aktuell | — |
| Git / Remote | ✅ Sauber | — |
| LTM-Auslastung | ✅ 67 Einträge (< 90) | — |
| reference/ Struktur | ✅ Konsolidiert | — |
| Offene Workpapers | ⚠️ 4 Stück | LOW |
| Offene T1–T5 | ⚠️ Alle noch offen | MEDIUM |
| Neue Issues #19 + #20 | ⚠️ Analysiert, nicht bearbeitet | MEDIUM |
| LTM-Ingest | ⚠️ Seit 2026-02-28 kein Ingest | LOW |

---

## Next Steps

1. → **T1 starten:** `_deviations` in `reference/AGENT_SCHEMA.json`
2. → **T2 + T3:** `README.md` Update (LTM Hero + CLAUDE.md/GEMINI.md Abschnitt)
3. → **T4:** `READ-AGENT.md` Blueprint.md Workflow
4. → **T5:** `reference/prompts/bootstrap.md` Review
5. → **T6:** Security Signals (wenn Zeit)
6. → **T7:** Session-Close + LTM-Ingest
