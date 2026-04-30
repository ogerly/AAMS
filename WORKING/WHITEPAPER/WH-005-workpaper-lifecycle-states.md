# WP-005 — Workpaper Lifecycle States

## AAMS — Agent Manifest

> Stabile Architektur-Entscheidung. Nicht für tägliche Arbeit.

---

### Stand

2026-04-30

### Status

Aktiv

---

## Problem

Die Workpaper-Lifecycle hatte zwei Zustände: `active` → `closed`. In der Praxis gibt es Workpapers die nicht sofort abgeschlossen werden können — sie warten auf externe Input, sind pausiert, oder brauchen mehr Sessions. Diese lagen in `WORKING/WORKPAPER/` und verunreinigten den aktiven Flow.

## Entscheidung

Workpaper-Lifecycle erweitert um drei Zustände:

| Zustand | Ordner | Bedeutung |
|---|---|---|
| **active** | `WORKING/WORKPAPER/` | Wird gerade abgearbeitet. Mehrere parallel erlaubt. |
| **observe** | `WORKING/WORKPAPER/observe/` | Muss beobachtet/beaufsichtigt werden. Wartet auf externe Input. Braucht mehr Zeit. |
| **closed** | `WORKING/WORKPAPER/closed/` | Abgeschlossen. Archiviert. |

## Kriterien

### → observe

Ein Workpaper wird nach `WORKING/WORKPAPER/observe/` verschoben wenn:

- Nicht abgeschlossen
- Wartet auf externe Input/Entscheidungen
- Muss auf dem Schirm bleiben (beobachtet werden)
- Benötigt mehr Sessions als geplant
- Aktive Abarbeitung momentan nicht möglich aber relevant

### → closed

Ein Workpaper wird nach `WORKING/WORKPAPER/closed/` verschoben wenn:

- Abgeschlossen
- Alle Decisions promoted oder verworfen
- File Protocol vollständig
- Ingest in Memory erfolgt

## Rationale

### Warum nicht einfach in active liegen lassen?

Der aktive Ordner signalisiert "was wird gerade gemacht". Workpapers die nur beobachtet werden müssen aber nicht aktiv abgearbeitet werden können, verunreinigen dieses Signal. Ein Agent der `WORKING/WORKPAPER/` scannt sieht nur aktive Arbeit.

### Warum observe statt closed?

Workpapers in `observe/` sind nicht finished — sie warten. Sie müssen beobachtet werden, nicht archiviert. `closed/` ist für finished workpapers. `observe/` ist für workpapers die auf dem Schirm bleiben müssen.

### Warum keine neue Naming Convention?

Der Ordner `observe/` signalisiert den Zustand. Der Filename bleibt `{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md`. Keine zusätzliche Komplexität nötig.

## Impact

### Workspace Structure

```
WORKING/
├── WORKPAPER/
│   ├── (active workpapers)
│   ├── observe/
│   └── closed/
├── WHITEPAPER/
├── DIARY/
├── MEMORY/
├── LOGS/
├── GUIDELINES/
└── TOOLS/
```

### Affected Files

- `.agent.json` — `workspace.structure.workpapers_observe` hinzufügen
- `READ-AGENT.md` — Documentation Model Table erweitern
- `WORKING/WHITEPAPER/INDEX.md` — WP-005 entry hinzufügen
- `wiki_lint.py` — Optional: observe-check hinzufügen

## Migration

| Workpaper | Datum | Grund |
|---|---|---|
| `2026-04-15-social-outreach.md` | 2026-04-15 | Pausiert — waiting |
| `2026-04-15-mempalace-analyse.md` | 2026-04-15 | Pausiert — waiting |
| `2026-04-02-wording-faktencheck.md` | 2026-04-02 | Pausiert — waiting |

| Workpaper | Datum | Grund | Status |
|---|---|---|---|
| `2026-03-27-versioning-system.md` | 2026-03-27 | Abgeschlossen | → closed/ |
| `2026-03-31-field-report-analyse.md` | 2026-03-31 | Abgeschlossen | → closed/ |
| `2026-04-24-three-tests.md` | 2026-04-24 | Abgeschlossen | → closed/ |

## Cross-References

- WP-001: Vier-Schichten-Modell (Workpaper als Layer 1)
- Issue #43: RFC — candidate für observe
- Issue #48: Decision-Leck — candidate für observe

---

> Letztes Update: 2026-04-30 — Initial creation. Decision aus `2026-04-30-ARCH-WPSTRUCT-workpaper-observe-folder.md` promoted.
