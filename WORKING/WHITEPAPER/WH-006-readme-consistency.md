# WP-006 — README Consistency

## AAMS — Agent Manifest

> Stabile Architektur-Entscheidung. Nicht für tägliche Arbeit.

---

### Stand

2026-04-30

### Status

Aktiv

---

## Problem

README.md, README.en.md, README.zh.md veraltete Informationen. Reality Check zeigte 9+ divergenzen zwischen READMEs und tatsächlichen Zustand. Externe Konsistenz ist kritisch für Wahrnehmung des Projekts.

## Entscheidung

Alle READMEs, READ-AGENT.md, INDEX.md, CHANGELOG.md aktualisieren.

## Kriterien für README-Aktualisierung

Jede README muss aktualisieren wenn:

- Manifest version changed
- Whitepaper count changed
- Workspace structure changed
- Health-Score changed
- LTM entries threshold changed
- New features added (observe/, topic_registry, etc.)
- Manifest-Prinzip (D9) changed
- Contract Reference changed

## Impact

### README Fixes

| README | Fixes |
|---|---|
| README.md | AAMS/2.0 + Manifest-Prinzip + observe/ + topic_registry + Current Status + CONTRACT.md reference |
| README.en.md | same fixes |
| README.zh.md | "规范" → Manifest + same fixes |

### READ-AGENT.md Fixes

| Field | Before | After |
|---|---|---|
| Whitepapers | 4 | 6 |
| Closed workpapers | ~40 | 47 |
| LTM | 116+ | 127 |
| Health-Score | 8/10 | 7/10 |
| Lifecycle | active → observe → closed | active → observe → closed |
| `.agent.json` | no `workpapers_observe` | `workpapers_observe` added |

### INDEX.md Fixes

- WP-005 entry: "obsolete" → "observe"
- WP-006 entry added
- Footer updated

### CHANGELOG.md Fixes

- [Unreleased] section: Added + Changed entries

### SPEC.md / CONTRACT.md

- README now references `CONTRACT.md` as "technical reference"
- Both remain stubs with circular redirect — **pending resolution**

### Workspace Structure

```
WORKING/
├── WORKPAPER/
│   ├── (active)
│   ├── observe/
│   └── closed/ (47)
├── WHITEPAPER/ (5 + INDEX.md)
├── DIARY/
├── MEMORY/ (127 entries)
├── LOGS/
├── GUIDELINES/
└── TOOLS/
```

### Manifest Version

AAMS/2.0 — "Agent Manifest" (nicht "Specification")

### Manifest-Prinzip (D9)

AAMS describes, es schreibt kein Verhalten vor.

### Contract Reference

- `reference/CONTRACT.md` — Hauptdoc (Agent Manifest)
- `reference/SPEC.md` — Stub (redirect auf CONTRACT.md)

### Whitepapers

| # | Datei | Thema |
|---|---|---|
| WP-001 | WP-001-aams-overview.md | AAMS Overview |
| WP-002 | WP-002-related-work.md | Related Work |
| WP-003 | WP-003-field-discourse.md | Field Discourse |
| WP-004 | WP-004-long-horizon-reasoning.md | Long-Horizon Reasoning |
| WP-005 | WP-005-workpaper-lifecycle-states.md | Workpaper Lifecycle |

### Workpaper Lifecycle

active → observe → closed (drei Zustände)

### LTM

127 entries — dual-layer (audit-log + ChromaDB)

### topic_registry

maschinenlesbar in `.agent.json`

### .aams-version

exists — state file für upgrade detection

---

> Letztes Update: 2026-04-30 — Initial creation. Decision aus `2026-04-30-ARCH-README-consistency-check.md` promoted.
