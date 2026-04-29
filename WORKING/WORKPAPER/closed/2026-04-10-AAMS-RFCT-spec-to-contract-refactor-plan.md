# Workpaper: Refactoring Plan — Spec → Contract
# AAMS: Vollständige Umbenennung aller "Specification"-Referenzen

**Datum:** 2026-04-10  
**Autor:** @ogerly / DEVmatrose  
**Typ:** Refactoring Plan / Change Inventory  
**Priorität:** Hoch — Breaking Change, koordinierter Rollout nötig  
**Abhängigkeit:** `2026-04-10-AAMS-STRAT-reorientation-spec-vs-contract.md` (Entscheidung: Option B angenommen)

---

## Session Goal

Vollständiges Inventar aller Dateien und Stellen die von der Umbenennung  
**"Specification" → "Agent-Contract"** / **`_spec` → `_contract`** betroffen sind.  
Jeden Change exakt beschreiben. Reihenfolge und Abhängigkeiten festlegen.  
Entscheidungen die noch offen sind markieren — nicht im Refactor vorwegnehmen.

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-10-AAMS-RFCT-spec-to-contract-refactor-plan.md` | ✅ |

---

## ⚠ KRITISCHE INVARIANTEN — dürfen durch den Refactor NICHT gebrochen werden

Diese Punkte sind nicht verhandelbar. Jede Refactor-Entscheidung muss gegen sie geprüft werden.

### INV-1: Die curl-Invariante — ein Befehl, ein File, läuft überall

```bash
curl -sO https://raw.githubusercontent.com/DEVmatrose/AAMS/main/.agent.json
```

**Das muss nach AAMS/2.0 genauso funktionieren wie nach AAMS/1.0.**

AAMS hat genau einen Grund warum Adoption reibungslos funktioniert:

> "The cost of adopting AAMS is one `curl` command. Zero dependencies. No install. No framework. No lock-in."

Dieses Versprechen darf durch den Refactor **nicht gebrochen** werden — weder technisch noch konzeptuell. `.agent.json` bleibt das einzige notwendige Artefakt. Ein Agent der es liest muss das System vollständig aufbauen können — ohne zusätzliche Schritte, ohne Voraussetzungen im Zielrepo.

**Konsequenzen für den Refactor:**
- `.agent.json` bleibt der einzige Bootstrap-Einstieg — keine Aufsplittung in mehrere Pflichtdateien
- Wenn `_spec` als deprecated markiert wird und `_contract` eingeführt wird: `.agent.json` muss **alleine** für sich lesbar sein — kein separates Schema-File nötig
- Die WORKSPACE-Discovery-Logik muss **in `.agent.json` eingebettet** sein, nicht in einer externen Datei
- Backward compat: ein Agent mit `.agent.json` v1 muss weiterhin funktionieren (kein hard-break)

### INV-2: WORKING → WORKSPACE-Migration bricht bestehende Repos

Viele Repos nutzen AAMS bereits mit `./WORKING/` als Root. Sie haben:
- Bestehende Workpapers in `WORKING/WORKPAPER/`
- LTM-Daten in `WORKING/MEMORY/`
- Eigene Whitepapers in `WORKING/WHITEPAPER/`

Der Wechsel zu `WORKSPACE/WORKING/` als bevorzugtem Default darf **keine automatische Migration** erzwingen. Die neue Bootstrap-Logik (aus dem WORKSPACE-Field-Report) muss:
1. `./WORKING/` erkennen und als legacy-konform akzeptieren
2. Keinen Datenverlust riskieren
3. Nur auf explizite Entscheidung des Users migrieren

**Bestehende externe Links** (GitHub Issues, Docs, Blog-Posts) die auf Ordnernamen verweisen bleiben valide — WORKING existiert weiterhin, nur als empfohlene Substruktur in WORKSPACE/.

### INV-3: Externe Repos die AAMS heute nutzen dürfen nicht brechen

Bekannte Deployments:
- MantisClaw — `WORKSPACE/WORKING/` (bereits konform mit neuem Standard)
- Mantis-OS — `WORKSPACE/WORKING/` (bereits konform)
- MantisNostr — `./WORKING/` (legacy, funktioniert weiterhin)
- Mantis-Family — `./WORKING/` (legacy, funktioniert weiterhin)

**Kein breaking change ohne Opt-in.** AAMS/2.0 ist backward-kompatibel bei der Ordnerstruktur. Nur `_spec` → `_contract` im JSON ist ein soft-breaking-change (mit Deprecation-Period).

### INV-4: Agent-Einstieg bleibt `AGENTS.md` + `.agent.json`

Die Kombination die AAMS von CLAUDE.md überlegen macht ist:
```
AGENTS.md (thin, tool-agnostic)
  └── .agent.json (maschinenlesbar, ausführbar)
      └── READ-AGENT.md (lebendiger Kontext)
```

Dieses drei-Ebenen-Einstiegsmodell bleibt erhalten. Keine vierte Pflichtdatei einführen.

---

## 1. Vorab-Entscheidungen (MÜSSEN vor dem Refactor getroffen werden)

Diese Fragen blocken spezifische Änderungen. Hier dokumentieren bevor angefangen wird.

### E-1: Akronym — bleibt AAMS oder nicht?
**Optionen:**
- A) AAMS = Eigenname (kein Akronym mehr) — Außendarstellung: "AAMS" ohne Auflösung
- B) AAMS = "Autonomous Agent Manifest System" — "Spec" → "System"
- C) AAMS = "Autonomous Agent Manifest Standard" — "Spec" → "Standard"

**Empfehlung:** Option A (Eigenname) — einfachster Schnitt, kein grammatikalischer Zwang.  
**Status:** ⬜ Entscheidung ausstehend

### E-2: `_spec` Schlüssel in `.agent.json` — rename oder dual?
**Optionen:**
- A) Hard rename: `"_spec"` → `"_contract"` (Breaking Change für alle Integrations die per JSON-Key lesen)
- B) Dual: `"_contract": "AAMS/2.0"` bleibt, `"_spec": "AAMS-MINI/1.0"` als deprecated field mit `_spec_deprecated: true`
- C) Dual mit Kommentar: `"_spec"` bleibt als primary, Value ändert sich auf `"AAMS/2.0-contract"`

**Empfehlung:** Option B — Breaking Change ist real, Deprecation-Feld signalisiert Migration ohne harten Bruch.  
**Status:** ⬜ Entscheidung ausstehend

### E-3: `reference/SPEC.md` — umbenennen oder alias?
**Optionen:**
- A) Umbenennen: `SPEC.md` → `CONTRACT.md` (alle Links breaken)
- B) Umbenennen + Redirect: `SPEC.md` bleibt als Stub mit Redirect-Hinweis auf `CONTRACT.md`
- C) Datei bleibt `SPEC.md`, nur Inhalt ändert sich (kein Dateinamen-Change)

**Empfehlung:** Option A für neuen Klarheitswert, Option C für minimalen Merge-Konflikt-Aufwand.  
**Status:** ⬜ Entscheidung ausstehend — betrifft viele externe Links (GitHub, README)

### E-4: Repository-Name auf GitHub
Der Repo-Name ist aktuell "AAMS" mit Description "Autonomous Agent Manifest Specification".  
Description kann ohne Breaking Change geändert werden. Repo-Name-Änderung bricht alle Clones.  
**Empfehlung:** Description ändern, Repo-Name unverändert lassen.  
**Status:** ⬜ Entscheidung ausstehend

### E-5: Version — AAMS/2.0 oder AAMS/1.4?
Die Entscheidung Spec → Contract ist konzeptuell ein Major Breaking Change.  
`AAMS/2.0` kommuniziert das klar. `AAMS/1.4` würde es verschleiern.  
**Empfehlung:** AAMS/2.0  
**Status:** ⬜ Entscheidung ausstehend

---

## 2. Vollständiges Change-Inventar

### Legende

| Symbol | Bedeutung |
|--------|-----------|
| 🔴 | Kern-Change — muss geändert werden, Breaking-relevant |
| 🟡 | Wichtig — sollte geändert werden, aber nicht Breaking |
| 🟢 | Nice-to-have — konsistent, aber nicht kritisch |
| ⬜ | Status: offen |
| ✅ | Status: erledigt |
| 🚧 | Status: in Arbeit |

---

### 2.1 `.agent.json` 🔴

**Datei:** `d:\Entwicklung\Projekte\Autonomous Agent Manifest Specification\.agent.json`

| # | Zeile | Aktuell | Änderung | Abhängigkeit |
|---|-------|---------|----------|--------------|
| 1 | 2 | `"_spec": "AAMS-MINI/1.0"` | → `"_contract": "AAMS/2.0"` + deprecation field | E-2 |
| 2 | 3 | `"_doc": "Minimal Agent Bootstrap Contract..."` | Text anpassen: "Agent-Contract" statt implizit Spec | E-1 |
| 3 | 97 | `"agent_contract": {` | Bleibt — bereits korrekt benannt | — |
| 4 | 98 | `"_doc": "Behavioral contract..."` | Kann bleiben oder gestärkt werden | 🟢 |

**Change 1 konkret:**
```json
// Aktuell:
"_spec": "AAMS-MINI/1.0",

// Neu (Option B — dual):
"_contract": "AAMS/2.0",
"_spec": "AAMS-MINI/1.0",
"_spec_note": "DEPRECATED — use _contract. _spec retained for backward compatibility with AAMS/1.x tooling.",
```

**Status:** ⬜ — blockiert durch E-2, E-5

---

### 2.2 `README.md` 🔴

**Datei:** `d:\Entwicklung\Projekte\Autonomous Agent Manifest Specification\README.md`

| # | Zeile | Aktuell | Änderung |
|---|-------|---------|----------|
| 1 | 3 | `"This is both a specification and a live example..."` | `"...a contract-based standard and a live example..."` |
| 2 | 20 | `> **AAMS — Autonomous Agent Manifest Specification**` | Tagline überarbeiten (E-1 entscheidet Auflösung) |
| 3 | 87 | `"That's exactly what AAMS is — the Autonomous Agent Manifest Specification."` | Kernsatz überarbeiten |
| 4 | 212 | `"reference/SPEC.md ... The normative specification."` | Link + Beschreibung anpassen (E-3) |
| 5 | 298 | `"execute the contract"` | Bereits "contract" — konsistent halten |
| 6 | 344 | `## Technical Specification` | `## Technical Reference` oder `## Contract Reference` |
| 7 | 348 | `reference/SPEC.md — Full technical reference` | E-3 abhängig |

**Umfang: ca. 7 Einzelstellen, ein Kernsatz der das Selbstverständnis prägt.**  
**Status:** ⬜ — blockiert durch E-1, E-3

---

### 2.3 `AGENTS.md` 🔴

**Datei:** `d:\Entwicklung\Projekte\Autonomous Agent Manifest Specification\AGENTS.md`

| # | Zeile | Aktuell | Änderung |
|---|-------|---------|----------|
| 1 | 5 | `This repository uses **AAMS — Autonomous Agent Manifest Specification**.` | `This repository uses **AAMS — an agent-contract standard for autonomous work.**` |
| 2 | 51 | `## Full specification` | `## Full Reference` oder `## Contract & Reference` |
| 3 | 53 | `reference/SPEC.md — technical reference` | E-3 abhängig |

**Status:** ⬜ — blockiert durch E-1, E-3

---

### 2.4 `READ-AGENT.md` 🔴

**Datei:** `d:\Entwicklung\Projekte\Autonomous Agent Manifest Specification\READ-AGENT.md`

| # | Zeile | Aktuell | Änderung |
|---|-------|---------|----------|
| 1 | 20 | `**Autonomous Agent Manifest Specification (AAMS)**` | Tagline (E-1) |
| 2 | 95 | `\| SPEC \| Specification work \|` | `\| SPEC \| Specification/Contract work \|` oder neues Tag `CTRT` — Vorsicht: bestehende Workpapers nutzen SPEC-Tag |
| 3 | 240 | `reference/SPEC.md — Full specification (English)` | E-3 abhängig |
| 4 | 241 | `reference/SPEC-DE.md — Full specification (German)` | E-3 abhängig |
| 5 | 248 | `Spec version: **AAMS/1.3**` | `Contract version: **AAMS/2.0**` |

**⚠ Sonderfall Zeile 95:** Das `SPEC`-Topic-Tag in der Workpaper-Namenskonvention ist in vielen bestehenden Workpapers bereits verwendet. Umbenennung bricht Rückwärts-Suche (RFL-Pattern-Matching). **Empfehlung: SPEC-Tag bleibt erhalten**, nur die Beschreibung ändert sich von "Specification work" zu "Specification/Contract work".  
**Status:** ⬜ — blockiert durch E-1, E-3, E-5

---

### 2.5 `.github/copilot-instructions.md` 🟡

**Datei:** `d:\Entwicklung\Projekte\Autonomous Agent Manifest Specification\.github\copilot-instructions.md`

| # | Zeile | Aktuell | Änderung |
|---|-------|---------|----------|
| 1 | 3 | `This repository uses AAMS — Autonomous Agent Manifest Specification.` | Tagline (E-1) |

**Status:** ⬜ — blockiert durch E-1

---

### 2.6 `reference/AGENT.json` 🟡

**Datei:** `d:\Entwicklung\Projekte\Autonomous Agent Manifest Specification\reference\AGENT.json`

| # | Zeile | Aktuell | Änderung |
|---|-------|---------|----------|
| 1 | 2 | `"_spec": "AAMS/1.0"` | → dual `_contract` + deprecated `_spec` (E-2) |
| 2 | 3 | `"_doc": "Autonomous Agent Manifest Specification..."` | Tagline (E-1) |
| 3 | 399 | `"spec_version": "1.0"` | `"contract_version": "2.0"` oder dual field |
| 4 | 400 | `"spec_url": "..."` | bleibt (URL ändert sich nicht) |

**Status:** ⬜ — blockiert durch E-1, E-2, E-5

---

### 2.7 `reference/AGENT_SCHEMA.json` 🟡

**Datei:** `d:\Entwicklung\Projekte\Autonomous Agent Manifest Specification\reference\AGENT_SCHEMA.json`

| # | Zeile | Aktuell | Änderung |
|---|-------|---------|----------|
| 1 | 4 | `"title": "AAMS — Autonomous Agent Manifest Specification"` | Tagline (E-1) |
| 2 | 8 | `"required": ["_spec", ...]` | `_spec` bleibt required für v1.x compat ODER `_contract` wird required — E-2 |
| 3 | 12 | `"_spec": {...}` | field-Definition anpassen |
| 4 | 261 | `"spec_version": {...}` | dual field oder rename |
| 5 | 262 | `"spec_url": {...}` | bleibt |
| 6 | 280 | `"...intentional deviations from the AAMS spec."` | Text anpassen |
| 7 | 285 | `"spec_path": "The path...as defined in the AAMS standard."` | Text anpassen |

**⚠ Achtung:** Schema-Änderungen brechen JSON-Schema-Validierung aller conforming Repos. `_spec` aus `required` zu entfernen ist ein Breaking Change für alle Deployments.  
**Status:** ⬜ — blockiert durch E-2

---

### 2.8 `reference/SPEC.md` 🔴

**Datei:** `d:\Entwicklung\Projekte\Autonomous Agent Manifest Specification\reference\SPEC.md`

| # | Zeile | Aktuell | Änderung |
|---|-------|---------|----------|
| 1 | 1 | `# AAMS — Autonomous Agent Manifest Specification` | Titel (E-1) |
| 2 | 21 | `"AAMS is the answer: A standardized, versionable, validatable manifest..."` | Kernsatz überarbeiten |
| 3 | 39 | `every AGENT.json carries _spec: AAMS/1.0` | Update auf `_contract: AAMS/2.0` + Deprecation-Note |
| 4 | 44 | `AAMS defines where memory lives, when...` | Bleibt inhaltlich korrekt |
| 5 | 46 | `any conforming LTM backend...` | Bleibt inhaltlich korrekt |
| — | gesamt | Dateiname `SPEC.md` | E-3: evtl. → `CONTRACT.md` |

**Umfang: Große Datei (1070+ Zeilen). Volltext-Review erforderlich für alle Stellen wo "specification" als Selbstbeschreibung auftaucht.**  
**Empfehlung: Erst E-3 entscheiden, dann SPEC.md in einem separaten Arbeitspaket angehen.**  
**Status:** ⬜ — blockiert durch E-1, E-3

---

### 2.9 `reference/SPEC-DE.md` 🟡

Analog zu SPEC.md — deutsche Version.  
**Status:** ⬜ — nach SPEC.md-Refactor

---

### 2.10 `reference/registry/capabilities.md` 🟢

| # | Zeile | Aktuell | Änderung |
|---|-------|---------|----------|
| 1 | 5 | `Part of: AAMS — Autonomous Agent Manifest Specification` | Tagline (E-1) |

**Status:** ⬜

---

### 2.11 `WORKING/WHITEPAPER/WP-001-aams-overview.md` 🔴

| # | Zeile | Aktuell | Änderung |
|---|-------|---------|----------|
| 1 | 14 | `"...ist ein offener Standard — keine Software, keine Runtime, kein Framework."` | Erweitern: "...ein Verhaltensvertrag, kein reines Datenformat." |
| 2 | 61-62 | `Bootstrap-Contract. Enthält: workspace.structure, agent_contract...` | Bereits korrekt — konsistent mit Umbenennung |

**Umfang: WP-001 ist das primäre Conceptual-Dokument. Es muss die Neupositionierung "Vertrag statt Spec" als Leitgedanken übernehmen.**  
**Status:** ⬜

---

### 2.12 Weitere Workpapers (nicht zu ändern)

Die folgenden Workpapers in `WORKING/WORKPAPER/` und `WORKING/WORKPAPER/closed/` verwenden "Specification" als historische Beschreibung. Diese werden **nicht** geändert — sie sind historische Dokumente. Nur aktive und zukünftige Workpapers nutzen die neue Terminologie.

Betroffen (zur Dokumentation, kein Action Required):
- `2026-03-28-video-marketing-kochbuch.md` — Marketing-Texte mit "Autonomous Agent Manifest Specification"
- `2026-03-27-versioning-system.md` — "AAMS-MINI/1.0 (Spec-Version)"
- `2026-04-10-AAMS-WORKSPACE-field-report-workspace-container.md` — "AAMS-Spec" als Beschreibung

---

### 2.13 `WORKING/DIARY/2026-04.md` 🟢

Diary-Einträge sind historisch — nicht ändern. Neue Einträge nutzen neue Terminologie.

---

## 3. Abhängigkeitsgraph

```
E-1 (Akronym-Entscheidung)
  └── README.md Zeile 20, 87
  └── AGENTS.md Zeile 5
  └── READ-AGENT.md Zeile 20
  └── .github/copilot-instructions.md
  └── reference/AGENT.json _doc
  └── reference/SPEC.md Titel
  └── reference/AGENT_SCHEMA.json title
  └── reference/registry/capabilities.md

E-2 (_spec/_contract Entscheidung)
  └── .agent.json Kern-Change
  └── reference/AGENT.json _spec field
  └── reference/AGENT_SCHEMA.json required[] + field definitions

E-3 (SPEC.md Dateiname)
  └── reference/SPEC.md (rename?)
  └── README.md Zeile 212, 348
  └── AGENTS.md Zeile 53
  └── READ-AGENT.md Zeile 240, 241

E-4 (GitHub Repo Description)
  └── GitHub Web UI — kein Datei-Change

E-5 (Versionsnummer AAMS/2.0)
  └── .agent.json _contract value
  └── READ-AGENT.md Zeile 248
  └── reference/AGENT.json spec_version
```

**Alle Entscheidungen E-1 bis E-5 müssen vor dem ersten File-Change getroffen sein.**  
**Entscheidungen sind nicht voneinander abhängig — parallel entscheidbar.**

---

## 4. Rollout-Strategie

### Phase 0 — Entscheidungen (vor allem anderen)
- [ ] E-1 durch E-5 entscheiden (in diesem Workpaper dokumentieren)
- [ ] GitHub Issue erstellen: "AAMS/2.0 — Spec → Contract reorientation"

### Phase 1 — Kern-Artefakte (Breaking Changes)
Reihenfolge matters — `.agent.json` first, da alle anderen Dateien darauf verweisen:

1. `.agent.json` — `_contract` field + deprecation `_spec`
2. `reference/AGENT_SCHEMA.json` — Schema Update
3. `reference/AGENT.json` — Full reference file

### Phase 2 — Einstiegspunkte (Agent-facing)
Alle Dateien die ein Agent als erstes liest:

4. `AGENTS.md`
5. `READ-AGENT.md`
6. `.github/copilot-instructions.md`

### Phase 3 — Dokumentation (Human-facing)
7. `README.md`
8. `reference/SPEC.md` (+ eventuell → `CONTRACT.md`, E-3)
9. `reference/SPEC-DE.md`

### Phase 4 — Stable Architecture Docs
10. `WORKING/WHITEPAPER/WP-001-aams-overview.md`
11. `reference/registry/capabilities.md`

### Phase 5 — Kommunikation & Migration-Guide
12. `MIGRATION.md` schreiben — was ändert sich, was nicht, wie migrieren bestehende Repos
13. GitHub Release Notes: explizit "backward-compatible — existing `./WORKING/` repos continue to work"
14. `reference/prompts/bootstrap.md` aktualisieren — curl-Befehl bleibt identisch, Erklärung um Deprecation ergänzen

### Phase 6 — Release
15. `READ-AGENT.md` Contract version → `AAMS/2.0`
16. `.env` / `CHANGELOG` aktualisieren
17. Git tag: `v2.0.0`

---

## 5. Risiken

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| Externe Links auf SPEC.md brechen | Hoch | Mittel | SPEC.md als Stub erhalten (E-3 Option B) |
| Agent-Tools die `_spec` key parsen → brechen | Mittel | Hoch | Dual-field in Phase 1 (E-2 Option B) |
| Inkonsistenz durch partiellen Rollout | Hoch | Mittel | Phase-Disziplin, kein cherry-pick |
| SPEC-Topic-Tag in alten Workpapers → RFL fail | Niedrig | Niedrig | Tag bleibt erhalten (nicht umbenennen) |
| WP-001 Whitepaper kontradiert neue Positionierung | Mittel | Hoch | Phase 4 vor Release |
| curl-Befehl ändert sich → Adoptionsbarriere steigt | Niedrig | **Kritisch** | INV-1: `.agent.json` bleibt der einzige Bootstrap-Einstieg |
| Bestehende `./WORKING/`-Repos brechen durch WORKSPACE-Default | Hoch | Hoch | INV-2: Legacy-Discovery — `./WORKING/` wird weiterhin erkannt |
| User erwartet Migration-Aufwand → kein Upgrade | Mittel | Mittel | `MIGRATION.md` + "zero forced migration"-Kommunikation |

---

## 6. Scope-Abgrenzung (nicht Teil dieses Refactors)

Die folgenden Änderungen sind strategisch verwandt aber **nicht** Teil des Spec→Contract Refactors. Sie gehören in separate Workpapers:

- WORKSPACE-Discovery-Logik (Field Report: `2026-04-10-AAMS-WORKSPACE-...md`)
- Inhaltliche Neustrukturierung von SPEC.md / CONTRACT.md
- LTM-System-Updates
- Neue Bootstrap-Logik

---

## Key Findings

- **23+ Stellen** in 11 Dateien sind betroffen — das ist ein koordinierter Multi-File-Refactor, kein Quick-Fix
- **5 Vorab-Entscheidungen** (E-1 bis E-5) müssen getroffen werden bevor der erste File-Change stattfindet
- **SPEC-Topic-Tag** in Workpaper-Naming NICHT umbenennen — würde RFL-Pattern-Matching für alle historischen Workpapers brechen
- **JSON Schema** ist das riskanteste Artefakt — `_spec` aus `required[]` zu entfernen bricht alle conforming Deployments
- **Datei `SPEC.md`** ist entscheidend für externe Verlinkung — Rename braucht Redirect-Strategie

---

## Next Steps

- [ ] E-1 bis E-5 hier dokumentieren (User-Entscheidung)
- [ ] GitHub Issue anlegen: "AAMS/2.0 — Strategic Reorientation: Spec → Agent-Contract"
- [ ] Phase 1 Änderungen umsetzen sobald Entscheidungen stehen
- [ ] WP-001 separates Workpaper für Whitepaper-Update
- [ ] Workpaper schließen → MEMORY ingesten

---

*Workpaper erstellt: 2026-04-10 — vollständiges Change-Inventar für koordinierten Refactor*
