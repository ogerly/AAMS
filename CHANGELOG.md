# Changelog

Alle wesentlichen Änderungen an AAMS werden hier dokumentiert.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

---

## [Unreleased]

---

## [2.6.0] — 2026-09-23

### Added

- **Team-Authorship (optional, backward-kompatibel)** — `team`-Sektion in `.agent.json`, `reference/AGENT.json`, `AGENT_SCHEMA.json`
- **Roster** — `WORKING/TEAM.md`: dynamisch, vom Bootstrap idempotent erstellt (`create_if_missing`), ab Tag 1 — Team oder Solo, gleiche Struktur, null Unterschied
- **Authorship** — `BY: {name|—} / {tool} / {model} / {capability}` in Workpaper-Header, Diary-Format und LTM-Index
- **Passive Detection** — Tool/Modell/capability (`local`|`frontier`) werden aus dem Tech-Stack erkannt (tool_detection + Runtime-Konfiguration + Endpoint) — niemals an den Menschen gefragt, niemals Pflicht
- **Handover** — `continued_from` + `observe/`-Status (wartet auf Weiterarbeit) + Single-Writer pro Workpaper
- **Guard-Check `authorship_present`** (optional, vor Write/Edit): Reihenfolge `manifest_read → workpaper_open → authorship_present → tools_gated`
- **`bootstrap_rules.team_file`** — `./WORKING/TEAM.md` (create_if_missing)
- **`on_update`** — neuer MIGRATE-Schritt: `TEAM.md` anlegen wenn fehlend (nie überschreiben)

### Changed

- **`reference/AGENT.json`** — synchronisiert (war `AAMS/2.3.1`, jetzt `AAMS/2.6.0`), `skills`-Duplikat bereinigt (Capabilities + Skill-Pool in einer Sektion)
- **`AGENT_SCHEMA.json`** — Version `2.6.0` ($id + version), `team`-Property (alle Felder optional), `skills`-Duplikat bereinigt, `authorship_present`-Guard-Check + `no_authorship`-Error + `bootstrap_rules.team_file`
- **`_deviations`** — AGENT.json + SPEC.md auf Schema-Naming `convention_path` synchronisiert (war `spec_path`, Validierungs-Drift)
- **README.md / READ-AGENT.md / docs/index.html** — Version auf `AAMS/2.6.0` synchronisiert

### Decisions

- **Whitepaper bleiben author-frei** (Wahrheit-in-Zeit) — keine „wer/womit"-Infos
- **Struktur-Invarianz** — Team oder Solo = gleiche Struktur, null Unterschied im Schema
- **Detection statt Frage** — erkennbare Fakten (Tool, Modell, local/frontier) aus dem Tech-Stack, keine menschliche Eingabe
- **Sämtliche Team-Felder `descriptive_only`** (D9) — kein Required-Feld, bestehende Repos 1:1 gültig

### Breaking changes

Keine. Alle Team-Felder optional, keine neuen Pflicht-Pfade, nichts wird überschrieben.

---

## [2.5.0] — 2026-07-08

### Added

- **INDEX.md-Pflege** — `WORKING/WHITEPAPER/INDEX.md` + `WORKING/WORKPAPER/INDEX.md`: erstellen wenn fehlend, bestehende Papers indexieren, bei neuem Paper aktualisieren
- **Max-5-Regel** — mehr als 5 offene Workpapers → Warnung + Vorschlag zum Schließen
- **WH-011-upgrade-system.md** — Whitepaper zum Upgrade-System

### Changed

- **`on_update`** — um 4 INDEX-Schritte erweitert (Index-Check/-Erstellung/-Aktualisierung + Max-5-Prüfung)
- **`_contract`** — `AAMS/2.3.1` → `AAMS/2.4.0`
- **`.aams-version`** — `installed_version` → `AAMS/2.4.0`, `install_type` → `local_tag`

---

## [2.4.0] — 2026-07-08

### Added

- **Upgrade-Sicherheit** — `on_update`/Upgrade-Pfad überschreibt nicht mehr blind: Backup (`.agent.json.bak`) + Merge statt Überschreiben
- **Anonymisierter Upgrade-Report** — `agent_conventions.feedback`: GitHub-Issue an `ogerly/AAMS` (nur wenn GITHUB_TOKEN vorhanden; keine Repo-Namen, keine Secrets, keine Personaldaten)
- **UPGRADE.md** — Anleitung für Consumer-Repos (Automatischer Upgrade-Befehl + manuelle Schritte)

### Fixed

- **Versioning** — „niemals runter in der Version": CHANGELOG-Konsistenz + `_contract` trägt die reale Patch-Version (Basis für Update-Detection)

---

## [2.3.2] — 2026-07-08

### Fixed

- **Update-Detection kaputt** — `version_detection` verglich nur `_contract` mit `.aams-version`. Da `_contract` immer `AAMS/2.0` war, merkten Consumer-Repos keine Änderung. Jetzt: `_contract` trägt Patch-Version (`AAMS/2.3.1`), `version_detection` vergleicht zusätzlich `_version_date` mit `.aams-version.installed_date`. Bei Diskrepanz → `on_update` wird ausgeführt.
- **`_version_date` nicht in `on_update`** — Der `on_update`-Contract hat `_version_date` in `.agent.json` nicht aktualisiert. Neue Zeile hinzugefügt: "Update `_version_date` in `.agent.json` to current date (YYYY-MM-DD)".
- **Andere Consumer-Repos blind** — Ohne Patch-Version im `_contract` und ohne `_version_date`-Vergleich bleibt ein Upgrade für alle Repos unsichtbar. Fix: semver im `_contract` + `_version_date`-Vergleich in `version_detection`.

### Changed

- **`_contract`** — `AAMS/2.0` → `AAMS/2.3.1` (Patch-Version für Update-Detection)
- **`.aams-version`** — `installed_version` → `AAMS/2.3.1`, `install_type` → `upgrade`
- **`version_detection.check`** — Erweitert: vergleicht nun `_contract` UND `_version_date` mit `.aams-version`
- **`reference/AGENT_SCHEMA.json`** — `$id` und `version` auf `2.3.0` aktualisiert
- **`reference/AGENT.json`** — `_version_date: 2026-07-08` hinzugefügt
- **`on_update` erweitert** — Migriert jetzt Konventionen, nicht nur Zahlen:
  - Parse CHANGELOG "Added"/"Changed" für neue workspace.structure-Pfade
  - MIGRATE: Erstelle neue Pfade im Consumer-Repo wenn fehlend
  - MIGRATE: Wende neue Konventionen an
  - MIGRATE: Prüfe tool_detection-Beispiele auf Relevanz
  - MIGRATE: Flagge "Removed"-Dateien zur Review (kein Auto-Delete)
  - Logge Migration-Aktionen in DIARY/
  - Aktualisiert `_version_date` in `.agent.json`

---

## [2.3.0] — 2026-07-07

### Added

- **Skill-Baukasten** — `WORKING/TOOLS/skills/` mit Platzhaltern für alle bekannten Tools
- **Lokale LLMs als First-Class-Citizen** — LM Studio, Ollama, llama.cpp, OpenAI-Proxy als Skill-Kategorien
- **WH-010-skills.md** — Skills als kristallisiertes Wissen, Tool-Erkennung, Skill-Baukasten, Issue-Vorschlag, Absolute Neutralität, Lokale LLMs
- **Passive Tool-Detection** — `passive_only: true` in `.agent.json` — Agents sollen NICHT aktiv nach Tools suchen
- **Passive Detection Documentation** — Klarstellung: "if you CAN detect, use it" ≠ "search for every tool"

### Changed

- **Passive Tool Detection** — `tool_detection` in `.agent.json`, `reference/AGENT.json`, `reference/AGENT_SCHEMA.json` — Klarstellung: passive Erkennung, keine aktive Suche nach 10+ Tools
- **Skills-Erweiterung** — Lokale LLMs (LM Studio, Ollama, llama.cpp, OpenAI-Proxy) als Skill-Kategorien
- **README.md** — Current Status auf 10 Whitepapers aktualisiert
- **INDEX.md** — WH-010 Eintrag hinzugefügt

### Removed

- **`.github/copilot-instructions.md`** — Copilot-Brücke entfernt. AAMS ist standardlos: keine tool-spezifische Datei darf im Repo liegen. Bridge = `AGENTS.md` → `READ-AGENT.md` → `.agent.json`. Die Bridge-Datei war ein Relikt aus alter Copilot-Nutzung.

### Security

- **Tool Decay Prävention** — Entfernt was nicht mehr genutzt wird. AAMS ist standardlos: keine tool-spezifischen Dateien im Repo.

---

## [2.3.0] — 2026-07-07

### Added

- **Skill-Baukasten** — `WORKING/TOOLS/skills/` mit Platzhaltern für alle bekannten Tools
- **Lokale LLMs als First-Class-Citizen** — LM Studio, Ollama, llama.cpp, OpenAI-Proxy als Skill-Kategorien
- **WH-010-skills.md** — Skills als kristallisiertes Wissen, Tool-Erkennung, Skill-Baukasten, Issue-Vorschlag, Absolute Neutralität, Lokale LLMs
- **Passive Tool-Detection** — `passive_only: true` in `.agent.json` — Agents sollen NICHT aktiv nach Tools suchen
- **Passive Detection Documentation** — Klarstellung: "if you CAN detect, use it" ≠ "search for every tool"

### Changed

- **Passive Tool Detection** — `tool_detection` in `.agent.json`, `reference/AGENT.json`, `reference/AGENT_SCHEMA.json` — Klarstellung: passive Erkennung, keine aktive Suche nach 10+ Tools
- **Skills-Erweiterung** — Lokale LLMs (LM Studio, Ollama, llama.cpp, OpenAI-Proxy) als Skill-Kategorien
- **README.md** — Current Status auf 10 Whitepapers aktualisiert
- **INDEX.md** — WH-010 Eintrag hinzugefügt

### Removed

- **`.github/copilot-instructions.md`** — Copilot-Brücke entfernt. AAMS ist standardlos: keine tool-spezifische Datei darf im Repo liegen. Bridge = `AGENTS.md` → `READ-AGENT.md` → `.agent.json`. Die Bridge-Datei war ein Relikt aus alter Copilot-Nutzung.

### Security

- **Tool Decay Prävention** — Entfernt was nicht mehr genutzt wird. AAMS ist standardlos: keine tool-spezifischen Dateien im Repo.

---

## [2.2.0] — 2026-04-30

### Added
- WH-001-aams-overview.md (renamed from WP-001)
- WH-002-related-work.md (renamed from WP-002)
- WH-003-field-discourse.md (renamed from WP-003)
- WH-004-long-horizon-reasoning.md (renamed from WP-004)
- WH-007-spec-contract-stub.md
- WH-008-health-score-10.md
- `.agent.json` `_version_date` updated to 2026-04-30

### Changed
- Naming Schema: Whitepapers → WH-*, Workpapers → WP-*
- WH-001 stale references fixed
- WH-008 stale data fixed
- Diary format updated to new naming convention
- Health-Score: 10/10

### Fixed
- Issue #45 closed (Duplikat von #43)
- `.aams-version` date updated to 2026-04-30

---

## [2.1.0] — 2026-04-30

### Added
- `WORKING/WORKPAPER/observe/` — third workpaper lifecycle state (active → observe → closed)
- `workpapers_observe` in `.agent.json` workspace structure
- WH-005-workpaper-lifecycle-states.md
- WH-006-readme-consistency.md
- WH-007-spec-contract-stub.md
- WH-008-health-score-10.md
- `topic_registry` maschinenlesbar in `.agent.json`
- `.aams-version` state file (updated)
- **12 Guidelines** in `WORKING/GUIDELINES/` (Documentation Model, Naming Schema, Workpaper Lifecycle, Decision-Promotion, File Protocol, LTM Rules, Topic Registry, Wiki Lint, AAMS Doctor, Git Safety, README Consistency, Diary Format)
- `docs/presenter-image.png` — Live Demo in README.md + README.en.md

### Changed
- Workpaper Lifecycle: active → observe → closed (drei Zustände)
- README.md, README.en.md, README.zh.md — **done** (Reality Check: 9+ divergenzen fixed)
- READ-AGENT.md Current Status — Health-Score 10/10, Whitepaper count 8, LTM entries 135
- INDEX.md — WH-005 + WH-006 + WH-007 + WH-008 entry
- Git-Tag: v2.1.0
- Health-Score: 10/10
- **Naming Schema: Whitepapers → WH-*, Workpapers → WP-***

### Fixed
- Issue #45 closed (Duplikat von #43)
- `.aams-version` date updated to 2026-04-30

## [2.0.0] — 2026-04-29

### Changed
- AAMS redefined as Agent Manifest (not Specification)
- `_contract: "AAMS/2.0"` added alongside deprecated `_spec`
- `agent_contract` → `agent_conventions` (descriptive, not prescriptive)
- `SPEC.md` → `CONTRACT.md` (stub with redirect)
- GitHub Repo Description unchanged (E-4)
- All "MUST" language removed — manifest describes, does not prescribe
- `topic_registry` added as maschinenlesbare Topic-Liste (Issue #41-Empf.3)
- `version_detection` prioritizes `_contract` over `_spec` (P2 from three-tests)

### Added
- `file_safety`-Sektion konzipiert (Issue #50)
- Skill-Konzept dokumentiert (Issue #51)
- MIGRATION.md Template angelegt (Issue #49)

### Deprecated
- `_spec` field in `.agent.json` and AGENT.json (backward compat only)
- Imperative agent_contract language → descriptive agent_conventions

---

## [1.3.0] — 2026-04-24

### Changed
- Spec → Contract Neuausrichtung (RFC #43, STRAT Workpaper)
- WORKSPACE-Discovery-Logik ergänzt (Field Report)
- Update-Detection-Protocol konzipiert (UPD Workpaper)

### Added
- `_deviations` in AGENT_SCHEMA.json + AGENT.json + SPEC.md (Commit 3cde55e)
- WORKSPACE-Container-Discovery in `.agent.json`

---

## [1.2.0] — 2026-04-10

### Added
- WORKSPACE-Container-Discovery in `.agent.json`
- Bootstrap-Rules for idempotent workspace creation
- UPD Workpaper: Update-Detection-Protocol

---

## [1.1.0] — 2026-03-27

### Added
- Vier-Schichten-Dokumentationsmodell (Workpaper, Whitepaper, Diary, Memory)
- Versioning-System konzipiert (semver + CHANGELOG + GitHub Releases)
- LTM/ChromaDB-Integration konzipiert

---

## [1.0.0] — 2026-02-18

### Added
- Initial AAMS Specification
- `.agent.json` Bootstrap-Contract
- READ-AGENT.md
- Workpaper-Template
