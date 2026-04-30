# 2026-04-30-ARCH-VERSION-version-update

## session_goal

Whitepapers aktualisieren + Version v2.2.0 + CHANGELOG.md finalize.

## repository_inventory

| Datei/Pfad | Status |
|---|---|
| WH-001 | stale references (WP-001..WP-004, old naming) |
| WH-008 | stale data (Whitepapers 6, LTM 130) |
| Diary | old naming format |
| `.agent.json` | `_version_date: 2026-04-29` |
| CHANGELOG.md | Unreleased section empty |
| Version | v2.1.0 → needs v2.2.0 |

## key_findings

### Whitepaper-Stale-Referenzen

**WH-001:**
- Line 117: `WP-005-ARCH-naming-schema.md` → `WH-005-ARCH-naming-schema.md`
- Line 116: `2026-04-09-ARCH-RFL-reflection-protocol-step.md` → `WP-2026-04-09-ARCH-RFL-reflection-protocol-step.md`
- Lines 231-233: WP-002..WP-004 → WH-002..WH-004
- Line 249: Whitepapers 4 → 8

**WH-008:**
- Line 71: Whitepapers 6 → 8
- Line 70: LTM 130 → 136
- Line 83: Naming Schema alt

### Diary-Format

**Alt:** `YYYY-MM-DD | WP: {workpaper} | WH: {whitepaper} | {other files}`

**Neu:** `YYYY-MM-DD | WP: WP-{DATE}-{TOPIC}-{SUBTOPIC}-{description} | WH: WH-{NNN}-{TOPIC}-{description} | {other files}`

### Version

**Aktuell:** v2.1.0

**Neu:** v2.2.0 — `.agent.json` changed (workpapers_observe, naming schema, workpaper lifecycle)

## decisions

1. **[DEC-1]** WH-001 stale references fixen
2. **[DEC-2]** WH-008 stale data fixen
3. **[DEC-3]** Diary format update
4. **[DEC-4]** `.agent.json` `_version_date` update
5. **[DEC-5]** CHANGELOG.md v2.2.0 section
6. **[DEC-6]** Git-Tag v2.2.0

### DEC-1 bis DEC-6 — [PROMOTE→WP-xxx]

Version update — architekturell relevant.

## open_questions

1. CHANGELOG.md v2.2.0 Release-Notes?
2. GitHub Release v2.2.0?

## file_protocol

| Aktion | Datei | Zeit |
|---|---|---|
| UPDATE | WH-001-aams-overview.md | 2026-04-30 |
| UPDATE | WH-008-health-score-10.md | 2026-04-30 |
| UPDATE | WORKING/DIARY/2026-04.md | 2026-04-30 |
| UPDATE | `.agent.json` | 2026-04-30 |
| UPDATE | CHANGELOG.md | 2026-04-30 |
| UPDATE | INDEX.md | 2026-04-30 |
| UPDATE | READ-AGENT.md | 2026-04-30 |
| UPDATE | README.md | 2026-04-30 |
| UPDATE | README.en.md | 2026-04-30 |
| UPDATE | README.zh.md | 2026-04-30 |
| CREATE | Git-Tag v2.2.0 | 2026-04-30 |
| CLOSE | → closed/ | 2026-04-30 |

## next_steps

1. WH-001 stale references fixen
2. WH-008 stale data fixen
3. Diary format update
4. `.agent.json` update
5. CHANGELOG.md v2.2.0 section
6. INDEX.md update
7. READ-AGENT.md update
8. READMEs update
9. LTM ingest
10. Close workpaper
