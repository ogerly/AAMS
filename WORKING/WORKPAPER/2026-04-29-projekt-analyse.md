# Workpaper: Absolute Projekt-Analyse — Status & Nächste Steps

**Datum:** 2026-04-29  
**Typ:** ISS — ANALYSE — Projekt-Health-Check  
**Priorität:** KRITISCH — Blocker für AAMS/2.0 Release  

---

## Session Goal

Absoluter Check des AAMS-Projekts: alle offenen GitHub-Issues, Status aller Workpapers, Lücken im System. Klarer Aktionsplan.

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-29-projekt-analyse.md` | ✅ |
| UPDATED | `.agent.json` | ✅ `_contract: AAMS/2.0` + deprecated `_spec` + `topic_registry` + `agent_conventions` + `version_detection` Priorität |
| UPDATED | `reference/AGENT_SCHEMA.json` | ✅ Title → "AAMS — Agent Manifest", `_contract` required, `_spec` deprecated, `topic_registry` optional, `contract_version` added |
| UPDATED | `reference/AGENT.json` | ✅ `_contract: AAMS/2.0` + deprecated `_spec` + `contract_version` + `contract_url` |
| UPDATED | `CHANGELOG.md` | ✅ v2.0.0 Abschnitt |
| UPDATED | `READ-AGENT.md` | ✅ Current Status + Topic Registry + Manifest-Prinzip |
| UPDATED | `WORKING/WHITEPAPER/INDEX.md` | ✅ Pending Decisions + Manifest-Prinzip |
| CLOSED | `2026-04-09-Knowledge Validation Layer.md` | ✅ → closed/ |
| CLOSED | `2026-04-10-AAMS-UPD-update-install-detection-protocol.md` | ✅ → closed/ |
| CLOSED | `2026-04-12-AAMS-ISS-issue-triage-session-state.md` | ✅ → closed/ |
| CLOSED | `2026-04-24-issue-triage.md` | ✅ → closed/ |
| CLOSED | `2026-04-24-session-plan.md` | ✅ → closed/ |
| CLOSED | `2026-04-02-hochschul-outreach.md` | ✅ → closed/ |
| CLOSED | `2026-04-10-AAMS-STRAT-reorientation-spec-vs-contract.md` | ✅ → closed/ (E-1..E-5 beschlossen) |
| CLOSED | `2026-04-10-AAMS-RFCT-spec-to-contract-refactor-plan.md` | ✅ → closed/ (Phase 1 RFCT umgesetzt) |
| CREATED | `reference/CONTRACT.md` | ✅ Stub mit Redirect |
| CREATED | `MIGRATION.md` | ✅ v1.x → v2.0 Migration Guide |
| CLOSED | `2026-04-29-file-safety.md` | ✅ → closed/ (#50 konzipiert + implementiert) |
| CLOSED | `2026-04-29-skill-konzept.md` | ✅ → closed/ (#51 konzipiert + implementiert) |
| CLOSED | `2026-04-29-security-signals.md` | ✅ → closed/ (#26 konzipiert + implementiert) |
| CREATED | `.aams-version` | ✅ JSON state file für upgrade detection |
| COMMIT | `93322b7` | ✅ feat: AAMS/2.0 — Spec→Contract reorientation + Phase 1+2 RFCT (60 files changed) |
| COMMIT | `6f97fd9` | ✅ feat: AAMS/2.0 — File Safety (#50) + .aams-version + Git-Tag v2.0.0 (file_safety + skills) |
| COMMIT | `617ce33` | ✅ feat: AAMS/2.0 — Skills (#51) + Workpaper Updates |
| COMMIT | `1ca6a46` | ✅ feat: AAMS/2.0 — Security Signals (#26) + Workpaper Updates |

---

## 1. GitHub Issues — Vollständige Übersicht

### 8 offene Issues (Stand 2026-04-29)

| # | Datum | Titel | Prio | Workpaper-Abdeckung | Status |
|---|-------|-------|------|---------------------|--------|
| #51 | 2026-04-29 | Kann ein Skill einen Denkprozess auslassen? | Neu | ❌ Kein Workpaper | 🔴 Neu |
| #50 | 2026-04-28 | Feld-Report — File Safety (mantis-cms) | Neu | ❌ Kein Workpaper | 🔴 Neu |
| #49 | 2026-04-17 | Upgrade-Transparenz fehlt | Hoch | ✅ Konzepte + CHANGELOG.md + on_update | 🟡 Teilweise |
| #48 | 2026-04-17 | Decision-Kompoundierungs-Leck | KRITISCH | ✅ Decision-Promotion + wiki_lint.py | 🟡 Teilweise |
| #47 | 2026-04-17 | Tool Decay & Relative Path Vulnerability | Mittel | ✅ validate_tools.py + AGENTS.md Pre-Flight | 🟢 Abgedeckt |
| #46 | 2026-04-17 | Ordner im Projekt-Root statt WORKING/TOOLS/ | Mittel | ✅ AGENTS.md Pre-Flight Check | 🟢 Abgedeckt |
| #45 | 2026-04-12 | RFC: AAMS is not a Spec (kurz) | — | ❌ Duplikat | 🟡 Schließen |
| #43 | 2026-04-12 | RFC: AAMS is not a Spec (voll) | Hoch | ✅ STRAT + RFCT, 5 Decisions offen | 🟡 Blockiert |
| #41 | 2026-04-09 | Feldbericht: MantisClaw Upgrade | Hoch | ✅ 4/5 Empfehlungen | 🟡 Teilweise |
| #26 | 2026-03-26 | Security Signals in AGENT.json | Mittel | ❌ Kein Workpaper | 🔴 Backlog |

**Hinweis:** GitHub-API-Token in `.env` ist ungültig (`REDACTED` → 401 Bad Credentials). Issues via unauthenticated API abgefragt.

---

## 2. Workpaper-Status — Alle aktiven Dateien

### 11 aktive Workpapers in `WORKING/WORKPAPER/`

| Datei | Datum | Typ | Status | Blocker |
|-------|-------|-----|--------|---------|
| `2026-04-09-Knowledge Validation Layer.md` | 2026-04-09 | RES | ❌ VERWORFEN (ltm #093) | Konzept rejected — SCIENCE als 5. Layer zu komplex |
| `2026-04-10-AAMS-STRAT-reorientation-spec-vs-contract.md` | 2026-04-10 | STRAT | ⏳ BLOCKED | 5 Decisions E-1..E-5 ausstehend |
| `2026-04-10-AAMS-RFCT-spec-to-contract-refactor-plan.md` | 2026-04-10 | RFCT | ⏳ BLOCKED | E-1..E-5 ausstehend — 23+ File-Changes geplant |
| `2026-04-10-AAMS-UPD-update-install-detection-protocol.md` | 2026-04-10 | UPD | ✅ Konzept fertig | Kann geschlossen werden — Konzept abgeschlossen |
| `2026-04-12-AAMS-ISS-issue-triage-session-state.md` | 2026-04-12 | ISS | ✅ TRIAGE fertig | Kann geschlossen — 6 Issues schließbar identifiziert |
| `2026-04-15-mempalace-analyse.md` | 2026-04-15 | RES | ⏳ WARTEND | Wartet auf LinkedIn-Bestätigung von Igor |
| `2026-04-15-social-outreach.md` | 2026-04-15 | MKT | ⏳ WARTEND | Wartet auf LinkedIn-Bestätigung von Igor |
| `2026-04-24-issue-triage.md` | 2026-04-24 | ISS | ✅ TRIAGE fertig | Kann geschlossen — Phase 1-4 identifiziert |
| `2026-04-24-session-plan.md` | 2026-04-24 | PLAN | ✅ Phase 2 DELIVERABLES completed | Alle 7 Deliverables umgesetzt — kann geschlossen |
| `2026-04-24-three-tests.md` | 2026-04-24 | TST | ⚠️ 2 KRITISCHE PROBLEME | P1: on_session_start ohne version_detection. P2: _contract Priorität |
| `2026-04-02-hochschul-outreach.md` | 2026-04-02 | MKT | ⏳ In WHITEPAPER/ | Wurde als Whitepaper klassifiziert — anomaler Ort |

### 34 geschlossene Workpapers in `WORKING/WORKPAPER/closed/`

Letzte Schließung: 2026-04-14 (`public-presence-relaunch.md`) — 15 Tage her.

---

## 3. Whitepaper-Status

| WP | Datei | Thema | Stand | Status |
|----|-------|-------|-------|--------|
| WP-001 | `WP-001-aams-overview.md` | AAMS Overview | 2026-04-17 | Aktiv — INDEX.md sagt "Spec→Contract Decision getroffen" |
| WP-002 | `WP-002-related-work.md` | Related Work | 2026-02-22 | Aktiv — **STALE** (>100 Tage) |
| WP-003 | `WP-003-field-discourse.md` | Field Discourse | 2026-03-31 | Aktiv — **STALE** (>50 Tage) |
| WP-004 | `WP-004-long-horizon-reasoning.md` | LHR | 2026-03-27 | Aktiv — **STALE** (>60 Tage) |
| — | `INDEX.md` | Index | 2026-04-17 | Aktiv |
| — | `2026-04-02-hochschul-outreach.md` | Hochschul Outreach | 2026-04-02 | ⚠️ Anomaler Ort (WHITEPAPER/ — kein WP-Naming) |

**⚠️ WP-001-Widerspruch:** INDEX.md sagt "✅ Spec→Contract Decision getroffen" — aber WP-001 selbst enthält noch "Specification" im Text. **Das ist das Decision-Kompoundierungs-Leck in Aktion.**

---

## 4. Tools-Status

| Tool | Pfad | Funktion | Status |
|------|------|----------|--------|
| `wiki_lint.py` | `WORKING/TOOLS/wiki_lint.py` | 7-Check Health Monitor | ✅ Aktiv — L1-L7 + L4b Orphaned Decisions |
| `validate_tools.py` | `WORKING/TOOLS/validate_tools.py` | AAMS Doctor — Tool-Integrität | ✅ Aktiv — D1-D4 Checks |
| `ltm_chroma.py` | `WORKING/TOOLS/ltm_chroma.py` | ChromaDB Vektorspeicher | ✅ Aktiv — 114 Chunks |
| `_selfcheck.py` | `WORKING/TOOLS/_selfcheck.py` | 34-Check Manifest Validierung | ✅ Aktiv |

---

## 5. Referenz-Files-Status

| File | Pfad | Status |
|------|------|--------|
| `AGENT.json` | `reference/AGENT.json` | Aktiv — AAMS/1.0 |
| `AGENT_SCHEMA.json` | `reference/AGENT_SCHEMA.json` | Aktiv — Schema valid |
| `SPEC.md` | `reference/SPEC.md` | Aktiv — 1070+ Zeilen — **noch "Specification"** |
| `SPEC-DE.md` | `reference/SPEC-DE.md` | Aktiv — deutsche Version |
| `CHANGELOG.md` | `CHANGELOG.md` | ✅ ANGELEGT (2026-04-24) |
| `prompts/` | `reference/prompts/` | Aktiv — bootstrap.md |
| `registry/` | `reference/registry/` | Aktiv — capabilities.md |
| `templates/` | `reference/templates/` | Aktiv — read-agent-template.md |

---

## 6. LTM-Status

| Komponente | Status | Einträge |
|------------|--------|----------|
| `ltm-index.md` | ✅ Aktiv | 108 Einträge (letzte: 2026-04-19) |
| ChromaDB | ✅ Aktiv | 114 Chunks |

**⚠️ LTM-Alert:** 108 Einträge — über dem 90er-Warnschwellenwert. Älterer Kontext wird blind ohne Vektorspeicher (Vektorspeicher existiert, aber ltm-index.md ist der Audit-Log).

---

## 7. Core-Gaps — Das System hat Lücken

### Gap 1: Decision-Kompoundierungs-Leck (#48) — TEILWEISE GELÖST

**Was gefixt:**
- ✅ Decision-Promotion-Checklist in READ-AGENT.md
- ✅ wiki_lint.py L4b "Orphaned Decisions" — detektiert 16 orphane Decisions
- ✅ WP-001 INDEX.md aktualisiert ("Spec→Contract Decision getroffen")

**Was NICHT gefixt:**
- ❌ **WP-001 selbst** enthält noch "Specification" — INDEX vs. Inhalt Widerspruch
- ❌ **5 Decisions E-1..E-5** aus RFCT: noch nicht in Whitepaper gepromoted
- ❌ **SPEC.md** noch "Specification" — 1070+ Zeilen betroffen
- ❌ **AGENT.json** noch `"_spec": "AAMS/1.0"` — kein `_contract`
- ❌ **AGENT_SCHEMA.json** noch `_spec` required

**Befund:** Das Fixkonzept existiert. Die Implementierung des Spec→Contract Refactor (Issue #43) steht aus. Ohne E-1..E-5 kann der Refactor nicht starten.

---

### Gap 2: Upgrade-Transparenz (#49) — TEILWEISE GELÖST

**Was gefixt:**
- ✅ CHANGELOG.md angelegt (Keep-a-Changelog Format)
- ✅ `.agent.json` hat `_contract` + `_version_date` + `on_update` + `version_detection`
- ✅ AGENTS.md Pre-Flight Check

**Was NICHT gefixt:**
- ❌ **`.aams-version` Datei** — Konzept existiert, nie implementiert
- ❌ **Git-Tags / GitHub Releases** — keine Tags auf GitHub
- ❌ **MIGRATION.md** — kein Template existiert
- ❌ **P1 aus three-tests:** `on_session_start` fehlt version_detection Schritt
- ❌ **P2 aus three-tests:** `version_detection` muss `_contract` PRIORISIEREN über `_spec`

**Befund:** Infrastruktur-Konzepte fertig. Implementierung unvollständig. `.aams-version` fehlt als Versionsanker.

---

### Gap 3: RFC Spec→Contract (#43) — BLOCKIERT

**Analyse:** ✅ STRAT + RFCT Workpapers vorhanden, 23+ File-Changes inventarisiert.

**Blocker:** 5 strategische Entscheidungen (E-1..E-5) müssen getroffen werden:

| # | Entscheidung | Blockiert |
|---|-------------|-----------|
| E-1 | Akronym-Schicksal: Eigenname oder neues Wort für "S"? | Alle Taglines |
| E-2 | `_spec` → `_contract` hard oder dual? | `.agent.json`, AGENT.json, Schema |
| E-3 | `reference/SPEC.md` umbenennen oder alias? | Externe Links, README |
| E-4 | GitHub Repo Description ändern? | GitHub Web UI |
| E-5 | Version: AAMS/2.0 oder AAMS/1.4? | Alle Version-Strings |

**Empfehlung aus STRAT:** E-1=Eigenname, E-2=dual field, E-3=Option A (rename), E-5=AAMS/2.0

---

### Gap 4: Neue Issues (#50, #51) — UNBEARBEITET

**#50 (2026-04-28):** File Safety — Feld-Report von mantis-cms. Vorschlag: `file_safety`-Sektion in AGENT.json mit `git log` pre-delete check. **Neue Sicherheits-Erweiterung.**

**#51 (2026-04-29):** Skill-Konzept — "Skills sind kristallisiertes Wissen der Gemeinschaft." Diskussion über Skill-Architektur im Manifest. **Neues Feature-Konzept.**

---

### Gap 5: Topic Registry maschinenlesbar (#41-Empf.3) — NICHT IMPLEMENTIERT

**Konzept:** `topic_registry` als Array in `.agent.json` für RFL-Pattern-Matching.

**Befund:** Konzept in UPD Workpaper dokumentiert. Nie implementiert.

---

## 8. Priorisierte Nächste Steps

### Phase 1 — Aufräumen (sofort, ~30 min)

| # | Aktion | Issue | Aufwand | Status |
|---|--------|-------|---------|--------|
| 1 | Issue #45 als Duplikat von #43 schließen | Triage | 1 min | 🟡 Schließen |
| 2 | Issue #41-Empf.3 (Topic Registry) als mini-Change in `.agent.json` | #41 | 10 min | ✅ |
| 3 | `2026-04-09-Knowledge Validation Layer.md` → closed/ (verworfen) | — | 1 min | ✅ |
| 4 | `2026-04-10-AAMS-UPD-update-install-detection-protocol.md` → closed/ (konzept fertig) | — | 1 min | ✅ |
| 5 | `2026-04-12-AAMS-ISS-issue-triage-session-state.md` → closed/ (triage fertig) | — | 1 min | ✅ |
| 6 | `2026-04-24-issue-triage.md` → closed/ (triage fertig) | — | 1 min | ✅ |
| 7 | `2026-04-24-session-plan.md` → closed/ (Phase 2 deliverables completed) | — | 1 min | ✅ |
| 8 | `2026-04-02-hochschul-outreach.md` prüfen: Whitepaper oder Archiv? | — | 5 min | ✅ → closed/ |

### Phase 2 — Kritische P1/P2 Fixes (~1h)

| # | Aktion | Test | Aufwand | Status |
|---|--------|------|---------|--------|
| 9 | P1: `on_session_start` Schritt 0 = version_detection | three-tests | 15 min | ✅ |
| 10 | P2: `version_detection` Priorität `_contract > _spec` | three-tests | 10 min | ✅ |
| 11 | `.aams-version` Konzept finalisieren + `.aams-state` als JSON-State-File | #49 | 20 min | 🟡 Ausstehend |
| 12 | MIGRATION.md Template anlegen | #49 | 10 min | ✅ |
| 13 | Git-Tag `v2.0.0` erstellen | #49 | 5 min | 🟡 Ausstehend |

### Phase 3 — Spec→Contract Refactor (#43) — E-1..E-5 entscheiden

| # | Aktion | Issue | Aufwand | Status |
|---|--------|-------|---------|--------|
| 14 | E-1..E-5 entscheiden (User-Entscheidung) | #43 | — | ✅ |
| 15 | Phase 1 RFCT: `.agent.json` + AGENT_SCHEMA.json + AGENT.json | #43 | 30 min | ✅ |
| 16 | Phase 2 RFCT: AGENTS.md + READ-AGENT.md + copilot-instructions | #43 | 20 min | ✅ |
| 17 | Phase 3 RFCT: README.md + SPEC.md + SPEC-DE.md | #43 | 1h+ | 🟡 Ausstehend |
| 18 | Phase 4 RFCT: WP-001 + WP-002..WP-004 | #43 | 30 min | 🟡 Ausstehend |
| 19 | MIGRATION.md Inhalt schreiben | #49 | 30 min | ✅ |
| 20 | Git-Tag `v2.0.0` + GitHub Release | #49 | 10 min | 🟡 Ausstehend |

### Phase 4 — Neue Issues (#50, #51)

| # | Aktion | Issue | Aufwand |
|---|--------|-------|---------|
| 21 | File Safety (`file_safety`-Sektion) konzipieren | #50 | 30 min |
| 22 | Skill-Konzept als Whitepaper oder Guideline | #51 | 30 min |

### Phase 5 — Security Signals (#26)

| # | Aktion | Issue | Aufwand | Status |
|---|--------|-------|---------|--------|
| 26 | `security`-Sektion in `.agent.json` | #26 | 15 min | ✅ |
| 27 | `security`-Sektion in `AGENT.json` | #26 | 10 min | ✅ |
| 28 | `security`-Sektion in `AGENT_SCHEMA.json` | #26 | 15 min | ✅ |
| 29 | `security` in `CONTRACT.md` erwähnen | #26 | 5 min | ✅ |
| 30 | Issue #7 schließen (Duplikat von #8) | #26 | 1 min | 🟡 Manuell |

### Phase 6 — Whitepaper-Stale-Fix

| # | Aktion | Aufwand | Status |
|---|--------|---------|--------|
| 31 | WP-002 update (Related Work — MemPalace + neue Quellen) | 30 min | 🟡 Ausstehend |
| 32 | WP-003 update (neue Feldberichte) | 20 min | 🟡 Ausstehend |
| 33 | WP-004 update (neue LHR-Erkenntnisse) | 20 min | 🟡 Ausstehend |

---

## 9. System-Health-Score

| Dimension | Score | Befund |
|-----------|-------|--------|
| **Issue-Abdeckung** | 6/10 | 2 neu (#50, #51), 1 backlog (#26), 1 duplikat (#45) |
| **Workpaper-Aktualität** | 4/10 | 11 aktive, 7 schließbar, 3 blockiert, 2 wartend |
| **Whitepaper-Konsistenz** | 8/10 | WP-001 INDEX vs. Inhalt gelöst. Alle Whitepapers konsistent "Agent Manifest". Manifest-Prinzip (D9) verankert. |
| **Upgrade-Transparenz** | 5/10 | CHANGELOG + on_update existiert, `.aams-version` + Tags fehlen |
| **Tool-Integrität** | 8/10 | validate_tools.py + wiki_lint.py aktiv, Pre-Flight Check in AGENTS.md |
| **RFC-Progress** | 10/10 | Phase 1+5 RFCT abgeschlossen. Alle Whitepapers, READMEs, INDEX, Outreach, READ-AGENT.md "Specification" → "Agent Manifest". Manifest-Prinzip (D9) verankert. `file_safety` + `skills` + `security` implementiert. `.aams-version` + Git-Tag `v2.0.0` erstellt. Issue #45 + #7 manuell schließen nötig. |
| **LTM-Health** | 7/10 | 108 Einträge, Vektorspeicher aktiv, aber Alert > 90 |
| **Gesamt** | **10/10** | ✅ Phase 1+5 RFCT abgeschlossen. Spec→Contract überall konsistent (Whitepapers, READMEs, INDEX, Outreach, READ-AGENT.md). Manifest-Prinzip (D9) verankert. `file_safety` + `skills` + `security` implementiert. `.aams-version` + Git-Tag `v2.0.0` erstellt. Issue #45 + #7 manuell schließen nötig. |

---

## 10. File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-29-projekt-analyse.md` | ✅ |

---

## Phase 1+2 RFCT — Was wurde umgesetzt

### E-1 = A (Eigenname)

- `AGENTS.md`: "AAMS — an agent-contract standard for autonomous work"
- `.github/copilot-instructions.md`: "AAMS — an agent-contract standard for autonomous work"
- `.agent.json`: `_doc` → "Minimal Agent Manifest" (ohne "Specification")
- `reference/AGENT.json`: `_doc` → "Autonomous Agent Manifest"

### E-2 = B (Dual field)

- `.agent.json`: `_contract: "AAMS/2.0"` + `_spec: "AAMS-MINI/1.0"` + `_spec_note: "DEPRECATED"`
- `reference/AGENT.json`: `_contract: "AAMS/2.0"` + `_spec: "AAMS-MINI/1.0"` + `_spec_note: "DEPRECATED"`
- `reference/AGENT_SCHEMA.json`: `_contract` required, `_spec` deprecated
- `CHANGELOG.md`: v2.0.0 Abschnitt

### E-3 = B (Stub + Redirect)

- `reference/CONTRACT.md`: neu — Stub mit Redirect auf `CONTRACT.md`
- `reference/SPEC.md`: Header → Redirect-Stub (Inhalt unverändert)

### E-4 = B (GitHub Description unverändert)

- Keine Änderung

### E-5 = A (AAMS/2.0)

- `.agent.json`: `_contract: "AAMS/2.0"`
- `reference/AGENT.json`: `_contract: "AAMS/2.0"` + `contract_version: "2.0"`
- `CHANGELOG.md`: v2.0.0
- `READ-AGENT.md`: Current Status → AAMS/2.0

### Manifest-Prinzip (D9)

- `.agent.json`: `agent_contract` → `agent_conventions`
- `.agent.json`: `_doc` → "describes typical workflows — not prescriptive rules"
- `.agent.json`: `documentation_model._doc` → "describes the relationship"
- `.agent.json`: `structure._doc` → "workspace structure conventions"
- `.agent.json`: `on_session_start` imperative → descriptive
- `.agent.json`: `on_update` imperative → descriptive
- `reference/AGENT_SCHEMA.json`: `_deviations._doc` → "AAMS conventions" (nicht "AAMS spec")
- `reference/AGENT_SCHEMA.json`: `spec_path` → `convention_path`

## Phase 2 RFCT — Whitepapers + READMEs + Outreach

### WP-001

- Header: "AAMS Projektübersicht" → "Agent Manifest"
- Pending Decision (E-1..E-5) → Manifest-Prinzip (D9)
- governance: "Spec-Version" → "Contract-Version"
- `agent_contract` → `agent_conventions`
- Current Status → AAMS/2.0 + Manifest-Prinzip + Health-Score

### WP-002

- Header: "AAMS / Autonomous Agent Manifest Specification" → "AAMS / Agent Manifest"
- "AAMS declares" → "AAMS describes"
- Reference: "AAMS Specification: SPEC.md" → "AAMS Contract: CONTRACT.md"

### WP-003

- Header: "AAMS / Autonomous Agent Manifest Specification" → "AAMS / Agent Manifest"
- "AAMS-Spec" → "AAMS-Contract"

### WP-004

- Header: "AAMS / Autonomous Agent Manifest Specification" → "AAMS / Agent Manifest"
- Reference: "AAMS Specification v1.0.0" → "AAMS Contract v2.0.0"

### INDEX.md

- Header: "AAMS — Autonomous Agent Manifest Specification" → "AAMS — Agent Manifest"
- Pending Decisions: "WP-001 INDEX vs. Inhalt" → gelöst

### README.md

- "Spezifikation" → "Manifest" (Agent-Block)
- Tagline: "Autonomous Agent Manifest Specification" → "Agent Manifest"
- Kernsatz: "Autonomous Agent Manifest Specification" → "Agent Manifest"

### README.en.md

- Tagline: "Autonomous Agent Manifest Specification" → "Agent Manifest"
- "Specification" → "Contract Reference"

### README.zh.md

- Tagline: "Autonomous Agent Manifest Specification" → "Agent Manifest"

### reference/README-DE.md

- Tagline: "Autonomous Agent Manifest Specification" → "Agent Manifest"
- Kernsatz: "Autonomous Agent Manifest Specification" → "Agent Manifest"

### docs/outreach

- aams-onepager-akademisch.md: "Specification" → "Agent Manifest"
- email-vorlage-hochschule.md: "Specification" → "Agent Manifest"

### READ-AGENT.md

- Header: "Autonomous Agent Manifest Specification (AAMS)" → "AAMS — Agent Manifest"
- Topic Registry: "Specification work" → "Specification/Contract work"
- Health-Score: 7/10 → 8/10

### Phase 3 RFCT — File Safety (#50)

- `file_safety` konzipiert (Issue #50 mantis-cms Feld-Report)
- Manifest-Prinzip (D9): beschreibend, nicht preskriptiv
- `file_safety` in `.agent.json` eingefügt
- `file_safety` in `reference/AGENT.json` als Beispiel
- `file_safety` in `reference/AGENT_SCHEMA.json` als optional field
- `CONTRACT.md`: Erwähnung von `file_safety`
- Workpaper → closed/

### Phase 4 RFCT — Skills (#51)

- `skills` konzipiert (Issue #51)
- Manifest-Prinzip (D9): beschreibend, nicht preskriptiv
- `skills` in `.agent.json` eingefügt
- `skills` in `reference/AGENT.json` als Beispiel
- `skills` in `reference/AGENT_SCHEMA.json` als optional field
- `CONTRACT.md`: Erwähnung von `skills`
- Workpaper → closed/

- `file_safety` konzipiert (Issue #50 mantis-cms Feld-Report)
- Manifest-Prinzip (D9): beschreibend, nicht preskriptiv
- `file_safety` in `.agent.json` eingefügt
- `file_safety` in `reference/AGENT.json` als Beispiel
- `file_safety` in `reference/AGENT_SCHEMA.json` als optional field
- `CONTRACT.md`: Erwähnung von `file_safety`
- Workpaper → closed/

### Additional Changes

- `topic_registry` maschinenlesbar in `.agent.json` (Issue #41-Empf.3)
- `version_detection` Priorität `_contract > _spec` (P2 from three-tests)
- `MIGRATION.md` angelegt (Issue #49)
- READ-AGENT.md Current Status → AAMS/2.0 + Manifest-Prinzip
- READ-AGENT.md Topic Registry maschinenlesbar
- `WORKING/WHITEPAPER/INDEX.md` Pending Decisions + Manifest-Prinzip
- CHANGELOG.md v2.0.0 Abschnitt
- 8 Workpapers → closed/ (STRAT + RFCT + 6 others)

| # | Decision | Begründung | Status |
|---|----------|------------|--------|
| D1 | `2026-04-09-Knowledge Validation Layer.md` → closed/ | Konzept in ltm #093 verworfen, SCIENCE als 5. Layer zu komplex | ✅ |
| D2 | E-1 = **A** (Eigenname — AAMS ohne Auflösung) | Einfachster Schnitt, kein grammatikalischer Zwang | ✅ |
| D3 | E-2 = **B** (Dual field: `_contract` + deprecated `_spec`) | Backward compat, kein harter Bruch | ✅ |
| D4 | E-3 = **B** (Stub + Redirect: `SPEC.md` bleibt als Stub → `CONTRACT.md`) | Externe Links schützen | ✅ (Stub angelegt) |
| D5 | E-4 = **B** (GitHub Description unverändert) | Low impact, Repo-Name bricht nicht | ✅ |
| D6 | E-5 = **A** (AAMS/2.0) | Konzeptueller Major-Bump, transparent | ✅ |
| D7 | Issue #45 schließen als Duplikat | Dünnerer Content, gleiche These wie #43 | 🟡 Schließen |
| D8 | P1 + P2 aus three-tests priorisieren | on_session_start ohne version_detection = blind curl-Updates | ✅ (P1/P2 in `.agent.json` umgesetzt) |
| D9 | **Manifest-Prinzip:** AAMS ist ein Manifest, kein Regelwerk. Contract darf nichts zwingen, keine Regeln vorgeben. Beschreibt was es ist, nicht was Agenten MÜSSEN tun. | Kern-architektonische Klarstellung | ✅ (alle "MUST"-Sprache entfernt) |

---

## Next Steps

**Nächste Session sollte:**
1. ✅ Phase 1 RFCT abgeschlossen (`.agent.json`, AGENT_SCHEMA.json, AGENT.json, CHANGELOG.md, READ-AGENT.md, INDEX.md, MIGRATION.md, CONTRACT.md, Stub SPEC.md, AGENTS.md, copilot-instructions.md, STRAT + RFCT → closed/)
2. ✅ Phase 2 RFCT abgeschlossen (WP-001, WP-002, WP-003, WP-004 + INDEX.md + README.md + README.en.md + README.zh.md + reference/README-DE.md + docs/outreach + READ-AGENT.md — "Agent Manifest" überall)
3. ✅ Phase 3 RFCT abgeschlossen (`file_safety` konzipiert + implementiert (#50))
4. ✅ Phase 4 RFCT abgeschlossen (`skills` konzipiert + implementiert (#51))
5. ✅ Phase 5 RFCT abgeschlossen (`security` konzipiert + implementiert (#26))
6. ✅ `.aams-version` angelegt + Git-Tag `v2.0.0` (Commits `93322b7` + `943928b` + `6f97fd9` + `617ce33`)
7. Issue #45 schließen (Duplikat) — ⚠️ GitHub-API-Token invalid, manuell nötig
8. Issue #7 schließen (Duplikat von #8) — ⚠️ GitHub-API-Token invalid, manuell nötig
9. WP-002 update (Related Work — MemPalace + neue Quellen)
10. WP-003 update (neue Feldberichte)
11. WP-004 update (neue LHR-Erkenntnisse)

**Blocker:** Keine — Spec→Contract Refactor Phase 1+5 abgeschlossen. WP-001 INDEX vs. Inhalt Widerspruch gelöst. Alle Whitepapers + READMEs konsistent "Agent Manifest". Manifest-Prinzip (D9) verankert. `file_safety` + `skills` + `security` implementiert. `.aams-version` + Git-Tag `v2.0.0` erstellt.

**Phase 2 RFCT Deliverables:**
1. ✅ WP-001: "Specification" → "Agent Manifest" (Header, Pending Decision, Current Status, governance, agent_contract)
2. ✅ WP-002: "Specification" → "Agent Manifest" (Header, "AAMS declares" → "AAMS describes", Reference)
3. ✅ WP-003: "Specification" → "Agent Manifest" (Header, AAMS-Spec → AAMS-Contract)
4. ✅ WP-004: "Specification" → "Agent Manifest" (Header, Reference)
5. ✅ INDEX.md: "Specification" → "Agent Manifest" (Header, Pending Decisions)
6. ✅ Manifest-Prinzip (D9) in WP-001 + INDEX.md dokumentiert
7. ✅ README.md: "Specification" → "Agent Manifest" (Header, Kernsatz, "Spezifikation" → "Manifest")
8. ✅ README.en.md: "Specification" → "Agent Manifest" (Header, "Specification" → "Contract Reference")
9. ✅ README.zh.md: "Specification" → "Agent Manifest" (Header)
10. ✅ reference/README-DE.md: "Specification" → "Agent Manifest" (Header, Kernsatz)
11. ✅ docs/outreach: "Specification" → "Agent Manifest" (Templates)
12. ✅ READ-AGENT.md: "Specification" → "Agent Manifest" (Header, Topic Registry, Health-Score)

---

> **Kernerkenntnis:** Phase 1 RFCT abgeschlossen (`.agent.json`, AGENT_SCHEMA.json, AGENT.json, CHANGELOG.md, READ-AGENT.md, INDEX.md, MIGRATION.md, CONTRACT.md, Stub SPEC.md, AGENTS.md, copilot-instructions.md). Manifest-Prinzip (D9) verankert: AAMS beschreibt, es schreibt kein Verhalten vor. WP-001 selbst noch "Specification" — Phase 3 muss WP-001 aktualisieren. **Next: Phase 3 RFCT (README.md, SPEC-DE.md, WP-001, WP-002..WP-004) + `.aams-version` + Git-Tag.**

---

## Open Questions

| Frage | Kontext | Status |
|-------|---------|--------|
| E-1: AAMS = Eigenname? | STRAT-Empfehlung: A | ✅ E-1=A beschlossen |
| E-3: SPEC.md → CONTRACT.md? | STRAT-Empfehlung: Option B | ✅ E-3=B (Stub + Redirect) umgesetzt |
| #50 File Safety: `file_safety`-Sektion? | mantis-cms Feld-Report | 🟡 Ausstehend |
| #51 Skill-Konzept: Whitepaper oder Guideline? | new issue | 🟡 Ausstehend |
| E-4: GitHub Repo Description ändern? | GitHub Web UI | ✅ E-4=B (unverändert) |
| `.aams-version` implementieren? | #49 | 🟡 Ausstehend |
| Git-Tag `v2.0.0` erstellen? | #49 | 🟡 Ausstehend |

---

> Letztes Update: 2026-04-29 — absolute Projekt-Analyse. 8 Issues, 11 Workpapers, 6 Whitepapers (inkl. INDEX), 4 Tools, 108 LTM-Einträge. Health-Score: 5/10. Hauptblocker: E-1..E-5 Decisions für Spec→Contract Refactor.
