# 2026-04-30-ARCH-WPSTRUCT-workpaper-observe-folder

## session_goal

Workpaper-Lifecycle erweitern um einen dritten Zustand: `observe/` neben `closed/`. Bisherige Struktur hat nur zwei Zustände (active → closed), was在实践中 nicht alle Fälle abdeckt. Workpapers die beobachtet/beaufsichtigt werden müssen aber nicht sofort abgearbeitet werden können, haben keinen Platz.

## repository_inventory

| Datei/Pfad | Status |
|---|---|
| `WORKING/WORKPAPER/` | 6 aktive Workpapers |
| `WORKING/WORKPAPER/closed/` | ~50 geschlossene Workpapers |
| `WORKING/WORKPAPER/observe/` | **NEU** — erstellt 2026-04-30 |
| `.agent.json` | AAMS/2.0 — workspace structure needs update |
| `READ-AGENT.md` | Documentation model needs update |
| `WORKING/WHITEPAPER/INDEX.md` | Needs WP-005 entry |

## key_findings

### Problem

Aktive Workpapers in `WORKING/WORKPAPER/` sammeln sich an wenn sie nicht sofort abgeschlossen werden können. Die Direktive sagt Workpapers sollen geschlossen werden, aber现实中 gibt es Fälle wo:

1. Workpaper braucht externe Input (z.B. Issue #43 RFC offen, Issue #48 Decision-Leck offen)
2. Workpaper ist pausiert weil auf etwas gewartet wird
3. Workpaper ist komplex und braucht mehrere Sessions

Diese Workpapers liegen in `WORKING/WORKPAPER/` und verunreinigen den aktiven Flow. Der aktive Ordner sollte nur Workpapers enthalten die gerade abgearbeitet werden.

### Lösung

Drei Zustände für Workpapers:

| Zustand | Ordner | Bedeutung |
|---|---|---|
| **active** | `WORKING/WORKPAPER/` | Wird gerade abgearbeitet. Kann auch mehrere parallel sein. |
| **observe** | `WORKING/WORKPAPER/observe/` | Muss beobachtet/beaufsichtigt werden. Wartet auf externe Input. Braucht mehr Zeit. |
| **closed** | `WORKING/WORKPAPER/closed/` | Abgeschlossen. Archiviert. |

### Kriterien für observe

Ein Workpaper geht nach `observe/` wenn:

- Es ist nicht abgeschlossen
- Es wartet auf externe Input/Entscheidungen
- Es ist pausiert aber relevant (nicht vergessen)
- Es braucht mehr Sessions als ursprünglich geplant

Ein Workpaper geht nach `closed/` wenn:

- Es ist abgeschlossen
- Alle Decisions sind promoted oder verworfen
- File Protocol ist vollständig
- Ingest in Memory ist erfolgt

### Naming Convention für obsolete Workpapers

Keine neue Naming Convention. Das bestehende Schema `{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md` gilt weiter. Der Ordner `obsolete/` signalisiert den Zustand, nicht der Filename.

### Migration bestehender Workpapers

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

## decisions

1. **[DEC-1]** `WORKING/WORKPAPER/observe/` wird als dritter Lifecycle-State hinzugefügt.
2. **[DEC-2]** Active Workpapers werden nur verschoben wenn sie pausiert/waiting sind. Nicht abgearbeitete aber aktive Workpapers bleiben in `WORKING/WORKPAPER/`.
3. **[DEC-3]** Die `.agent.json` workspace structure wird um `workpapers_obsolete` erweitert.
4. **[DEC-4]** `READ-AGENT.md` Documentation Model wird um den dritten State erweitert.
5. **[DEC-5]** wp-005 whitepaper erstellt für diese Architektur-Entscheidung.

### DEC-5 — [PROMOTE→WP-005]

Diese Entscheidung ist architekturell relevant und muss in einem Whitepaper leben. WP-005 wird created mit diesem Content.

## open_questions

1. Gibt es bestehende Workpapers die nach `obsolete/` gehören? (zu prüfen)
2. Soll es einen Mechanismus geben der obsolete Workpapers automatisch erkennt? (z.B. wiki_lint.py Check)
3. Wie lange bleibt ein Workpaper in `obsolete/` bevor es nach `closed/` oder gelöscht wird?

## file_protocol

| Aktion | Datei | Zeit |
|---|---|---|
| CREATE | `WORKING/WORKPAPER/observe/` | 2026-04-30 |
| CREATE | `2026-04-30-ARCH-WPSTRUCT-workpaper-obsolete-folder.md` | 2026-04-30 |
| CREATE | `WP-005-workpaper-lifecycle-states.md` | 2026-04-30 |

## next_steps

1. WP-005 whitepaper erstellen und architekturentscheidung formalisieren
2. `.agent.json` workspace structure update
3. `READ-AGENT.md` documentation model update
4. Prüfen welche aktiven Workpapers nach `observe/` gehören
5. Optional: wiki_lint.py um observe-check erweitern
6. Diary entry erstellen
7. Ingest into memory
8. Workpaper schließen
