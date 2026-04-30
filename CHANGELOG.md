# Changelog

Alle wesentlichen Änderungen an AAMS werden hier dokumentiert.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

---

## [Unreleased]

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
