# Workpaper — Versionierungssystem für GitHub einrichten

> Session: 2026-03-27 | Agent: Copilot (Claude Opus 4.6) | Status: OPEN

## Session Goal

Ein Versionierungssystem einrichten, das auf GitHub klar zeigt was in jeder Version neu ist. Aktuell: 46 Commits, 0 Tags, 0 Releases, kein CHANGELOG. Das Diary (Workpaper 2026-02-22-review) hatte bereits identifiziert: *"AAMS braucht ein 'What's New' / Changelog."*

---

## Ist-Zustand

| Aspekt | Status |
|---|---|
| Git Tags | ❌ Keine |
| GitHub Releases | ❌ Keine (Diary erwähnt "v1.0.0" aber kein Tag existiert) |
| CHANGELOG.md | ❌ Nicht vorhanden |
| Version in `.agent.json` | `AAMS-MINI/1.0` (Spec-Version, kein Release) |
| Version in SPEC.md | `AAMS/1.0` |
| Commits | 46 auf `main` |

---

## Konzept: Semantic Versioning + GitHub Releases + CHANGELOG

### 1. Versionierungsschema

**Semantic Versioning (SemVer)** — `MAJOR.MINOR.PATCH`

| Typ | Wann | Beispiel |
|---|---|---|
| MAJOR (1.x → 2.x) | Breaking Change in der Spec (Felder umbenannt, Pflichtfelder entfernt) | `2.0.0` |
| MINOR (1.0 → 1.1) | Neue Features, neue Felder, neue Templates | `1.1.0` |
| PATCH (1.0.0 → 1.0.1) | Bugfixes, Typos, Doku-Verbesserungen | `1.0.1` |

Für AAMS konkret:
- **v1.0.0** — Alles bis heute (Bootstrap, Spec, 4-Layer-Modell, LTM dual-track, Whitepapers WP-001 bis WP-004)
- **v1.0.1** — Issue #25 (Bootstrap-Gap), WP-003 Updates, etc.
- **v1.1.0** — Wenn G1-G4 umgesetzt werden (LTM-Query-Protokoll, Auto-Kompression, CI-Enforcement, Intent-Awareness)

### 2. CHANGELOG.md

Datei im Repo-Root. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

```markdown
# Changelog

All notable changes to AAMS are documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

## [Unreleased]

### Added
- WP-003: Kochbuch-Analogie für NonDev-Kommunikation
- Issue #25: Session-Start Prompts überarbeitet (bootstrap.md 7 Sektionen)
- README: "Chat Agent Users: Start Here" Abschnitt

## [1.0.0] — 2026-03-27

### Added
- `.agent.json` — Minimal bootstrap contract (drop into any repo)
- `AGENTS.md` — Universal bridge file for all AI tools
- `READ-AGENT.md` — Agent contract (on_first_entry, on_session_start, on_session_end)
- `reference/SPEC.md` — Full specification (English + German)
- `reference/AGENT_SCHEMA.json` — JSON Schema for validation
- Four-layer documentation model (Workpaper, Whitepaper, Diary, Memory)
- LTM dual-track: `ltm-index.md` (audit log) + ChromaDB (vector store)
- `reference/prompts/bootstrap.md` — Copy-paste prompts for chat agents
- `reference/templates/` — Workpaper, whitepaper, project analysis templates
- WP-001: AAMS Overview
- WP-002: Related Work
- WP-003: Field Discourse (Agent-A debate, CodeRabbit discovery, Projekt-O analysis)
- WP-004: Long-Horizon-Reasoning analysis with cross-model validation
- LHR positioning in SPEC.md
- `_deviations` as official schema field
- §4 Agent-Specific Workflow Integration (blueprint.md pattern)
- Tool mapping table (no CLAUDE.md/GEMINI.md needed)
- Secret exclusion policy
- 20+ closed workpapers documenting full build history
- 90 LTM entries in audit log

### Fixed
- Four-layer model consistency (diary was missing in .agent.json)
- SPEC path references
- LTM entry numbering
- Stale workpapers cleaned up
```

### 3. Git Tags + GitHub Releases

**Workflow für jedes Release:**

```bash
# 1. CHANGELOG.md aktualisieren (Unreleased → Version + Datum)
# 2. Commit
git add CHANGELOG.md
git commit -m "release: v1.0.0"

# 3. Tag setzen (annotated tag mit Release-Notes)
git tag -a v1.0.0 -m "AAMS v1.0.0 — Initial public release

Full specification, four-layer docs, dual-track LTM, 
cross-tool compatibility, 4 whitepapers, 20+ session archive."

# 4. Push
git push origin main --tags

# 5. GitHub Release erstellen (mit CHANGELOG-Ausschnitt als Body)
gh release create v1.0.0 --title "AAMS v1.0.0" --notes-file RELEASE_NOTES.md
```

**Oder einfacher via GitHub UI:**
- Repo → Releases → "Create a new release"
- Tag: `v1.0.0`, Target: `main`
- Title: `AAMS v1.0.0 — Initial public release`
- Body: Copy aus CHANGELOG.md
- ✅ "Set as the latest release"

### 4. Release-Badge im README

```markdown
[![Release](https://img.shields.io/github/v/release/DEVmatrose/AAMS)](https://github.com/DEVmatrose/AAMS/releases)
```

Zeigt die aktuelle Version direkt im README. Klick führt zu den Release Notes.

### 5. Künftiger Workflow (pro Release)

| Schritt | Was | Wer |
|---|---|---|
| 1 | Features/Fixes implementieren | Agent + User |
| 2 | CHANGELOG.md: Einträge unter `[Unreleased]` sammeln | Agent (bei jedem Commit) |
| 3 | Release entscheiden | User |
| 4 | `[Unreleased]` → `[x.y.z] — YYYY-MM-DD` | Agent |
| 5 | `git tag -a vx.y.z` + push | User/Agent |
| 6 | `gh release create` mit CHANGELOG-Ausschnitt | User/Agent |

---

## Umsetzungsplan

| # | Aktion | Aufwand |
|---|---|---|
| 1 | `CHANGELOG.md` erstellen (mit v1.0.0 + Unreleased) | 1 min |
| 2 | Release-Badge in README.md einfügen | 1 min |
| 3 | Commit: `release: add CHANGELOG.md, prepare v1.0.0` | 1 min |
| 4 | Git Tag `v1.0.0` setzen | 1 min |
| 5 | Push + GitHub Release erstellen | 2 min |

**Gesamtaufwand: ~5 Minuten.** Danach hat jede Version eine saubere Release Page auf GitHub mit "What's New".

---

## Decisions

- **SemVer** statt Datums-basiert — ist der de-facto Standard, GitHub und Tooling (Dependabot, Badge-Services) verstehen es nativ
- **Keep a Changelog Format** — etablierter Standard, strukturiert (Added/Changed/Deprecated/Removed/Fixed/Security)
- **v1.0.0 als Baseline** — alles Bisherige wird zu v1.0.0 zusammengefasst. Keine retroaktiven Tags für Zwischenstände
- **CHANGELOG.md im Root** — dort wo GitHub es erwartet und automatisch erkennt
- **Annotated Tags** (`git tag -a`) statt lightweight — enthalten Release-Message und sind signierbar

## File Protocol

| Aktion | Datei |
|---|---|
| CREATED | `WORKING/WORKPAPER/2026-03-27-versioning-system.md` |

## Next Steps

- [ ] User entscheidet: Umsetzung jetzt oder später?
- [ ] CHANGELOG.md erstellen
- [ ] README Badge einfügen
- [ ] v1.0.0 taggen + GitHub Release erstellen
- [ ] Workflow in READ-AGENT.md oder GUIDELINES dokumentieren (optional)
