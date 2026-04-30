# 2026-04-30-ARCH-NAMING-naming-convention-update

## session_goal

Namenskonvention ändern:
- Whitepapers → `WH-{NNN}-{TOPIC}-{description}.md`
- Workpapers → `WP-{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md`

## repository_inventory

| Datei/Pfad | Status |
|---|---|
| `.agent.json` | naming schema needs update |
| `READ-AGENT.md` | naming schema needs update |
| `naming-schema.md` | guideline needs update |
| `INDEX.md` | whitepaper names need update |
| `WP-{NNN}-*.md` | 8 files need rename |
| `{DATE}-{TOPIC}-*.md` | 5 active workpapers need rename |

## key_findings

### Aktuelle Konvention

| Typ | Format | Beispiel |
|---|---|---|
| Whitepapers | `WP-{NNN}-{TOPIC}-{description}.md` | `WP-001-aams-overview.md` |
| Workpapers | `{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md` | `2026-04-30-ARCH-WPSTRUCT-workpaper-observe-folder.md` |

### Neue Konvention

| Typ | Format | Beispiel |
|---|---|---|
| Whitepapers | `WH-{NNN}-{TOPIC}-{description}.md` | `WH-001-aams-overview.md` |
| Workpapers | `WP-{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md` | `WP-2026-04-30-ARCH-WPSTRUCT-workpaper-observe-folder.md` |

### rationale

**WH für Whitepapers:**
- "Whitepaper" → "WH"
- Shorter, more intuitive
- "WP" für Workpapers (aktuell) → "WH" für Whitepapers (neu)

**WP für Workpapers:**
- "Workpaper" → "WP"
- "WP" ist intuitiver für "Workpaper"
- "WH" ist intuitiver für "Whitepaper"

### Migration

| Whitepaper | Alt | Neu |
|---|---|---|
| WP-001 | `WP-001-aams-overview.md` | `WH-001-aams-overview.md` |
| WP-002 | `WP-002-related-work.md` | `WH-002-related-work.md` |
| WP-003 | `WP-003-field-discourse.md` | `WH-003-field-discourse.md` |
| WP-004 | `WP-004-long-horizon-reasoning.md` | `WH-004-long-horizon-reasoning.md` |
| WP-005 | `WP-005-workpaper-lifecycle-states.md` | `WH-005-workpaper-lifecycle-states.md` |
| WP-006 | `WP-006-readme-consistency.md` | `WH-006-readme-consistency.md` |
| WP-007 | `WP-007-spec-contract-stub.md` | `WH-007-spec-contract-stub.md` |
| WP-008 | `WP-008-health-score-10.md` | `WH-008-health-score-10.md` |

| Workpaper | Alt | Neu |
|---|---|---|
| 2026-04-17-RES-WIKI | `2026-04-17-RES-WIKI-karpathy-llm-wiki-vergleich.md` | `WP-2026-04-17-RES-WIKI-karpathy-llm-wiki-vergleich.md` |
| 2026-04-29-projekt-analyse | `2026-04-29-projekt-analyse.md` | `WP-2026-04-29-projekt-analyse.md` |
| 2026-04-30-ARCH-WPSTRUCT | `2026-04-30-ARCH-WPSTRUCT-workpaper-observe-folder.md` | `WP-2026-04-30-ARCH-WPSTRUCT-workpaper-observe-folder.md` |
| 2026-04-30-ARCH-README | `2026-04-30-ARCH-README-consistency-check.md` | `WP-2026-04-30-ARCH-README-consistency-check.md` |
| 2026-04-30-ARCH-HEALTH | `2026-04-30-ARCH-HEALTH-10-finalize.md` | `WP-2026-04-30-ARCH-HEALTH-10-finalize.md` |

## decisions

1. **[DEC-1]** Whitepapers → `WH-{NNN}-{TOPIC}-{description}.md`
2. **[DEC-2]** Workpapers → `WP-{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md`
3. **[DEC-3]** Alle Whitepapers umbenennen
4. **[DEC-4]** Alle Workpapers umbenennen
5. **[DEC-5]** `.agent.json` + `READ-AGENT.md` + `INDEX.md` + `naming-schema.md` update

### DEC-1 bis DEC-5 — [PROMOTE→WP-xxx]

Namenskonvention — architekturell relevant.

## open_questions

1. Existing links in READMEs, INDEX.md, etc. need update
2. Git history — rename files (git mv) to preserve history

## file_protocol

| Aktion | Datei | Zeit |
|---|---|---|
| UPDATE | `.agent.json` | 2026-04-30 |
| UPDATE | `READ-AGENT.md` | 2026-04-30 |
| UPDATE | `naming-schema.md` | 2026-04-30 |
| UPDATE | `INDEX.md` | 2026-04-30 |
| RENAME | `WP-{NNN}-*.md` → `WH-{NNN}-*.md` | 2026-04-30 |
| RENAME | `{DATE}-{TOPIC}-*.md` → `WP-{DATE}-{TOPIC}-*.md` | 2026-04-30 |
| UPDATE | README.md | 2026-04-30 |
| UPDATE | README.en.md | 2026-04-30 |
| UPDATE | README.zh.md | 2026-04-30 |
| UPDATE | CHANGELOG.md | 2026-04-30 |
| CLOSE | → closed/ | 2026-04-30 |

## next_steps

1. Whitepapers umbenennen (git mv)
2. Workpapers umbenennen (git mv)
3. INDEX.md update
4. `.agent.json` + `READ-AGENT.md` update
5. Guidelines update
6. READMEs update
7. CHANGELOG.md update
8. LTM ingest
9. Close workpaper
