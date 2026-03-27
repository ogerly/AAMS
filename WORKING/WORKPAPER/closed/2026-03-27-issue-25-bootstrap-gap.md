# Workpaper — Issue #25: Bootstrap-Gap schließen

> Session: 2026-03-27 | Agent: Copilot (Claude Opus 4.6) | Status: CLOSED

## Session Goal

Issue #25 umsetzen: Session-Start Prompts für Chat-Agenten verbessern. Das Bootstrap-Gap (Chat-Agents bootstrappen nicht von selbst) durch bessere, prominentere Prompts schließen.

## Definition of Done (aus Issue #25)

1. ✅ `reference/prompts/bootstrap.md` — Review + Verbesserung
2. ✅ `README.md` — Prominenter Hinweis auf `bootstrap.md`
3. ✅ Optional: VS Code Workspace Snippet dokumentiert

## Umsetzung

### 1. `reference/prompts/bootstrap.md` — komplett überarbeitet

**Vorher:** 1 Bootstrap-Prompt, 4 Tool-Varianten, 1 Session-Start-Prompt am Ende. Kein LTM-Query, kein Workpaper-Prompt, kein Session-Close.

**Nachher (7 Sektionen):**
- §Quick Reference — Copy-Paste-Tabelle mit allen 5 Situationen
- §1 First-Time Bootstrap — minimal + two-step + was der Agent danach tut
- §2 Session Start Prompt — **hervorgehoben als wichtigster Prompt**, mit Erklärung warum "before starting any work" entscheidend ist
- §3 LTM Query Prompt — für Kontext-Abfrage ohne volle Session (markdown + ChromaDB)
- §4 Workpaper Prompt — für nachträgliche Workpaper-Erstellung
- §5 Session Close Prompt — 5-Schritte-Checkliste
- §6 Tool-Specific Variants — Copilot, Claude, Cursor, Aider/Codex/Windsurf
- §7 VS Code Workspace Snippet — `aams-start` + `aams-close` code-snippets
- Bootstrap Gap Tabelle — Agent-Typ → auto-bootstrap? → was tun?
- Observed failure modes dokumentiert

### 2. `README.md` — "Chat Agent Users: Start Here"

Neuer Abschnitt direkt nach "Start in 2 Steps" mit:
- Warnung: Chat agents don't self-bootstrap
- Session-Start-Prompt zum Kopieren
- Verweis auf bootstrap.md für weitere Prompts
- Bestehender "bridge" Satz am Ende des Bootstrap-Gap-Abschnitts verbessert

### 3. VS Code Snippet

Dokumentiert in bootstrap.md §7 als `.vscode/aams.code-snippets`:
- `aams-start` — Session-Start mit Tab-Stop auf TOPIC
- `aams-close` — Session-Close Checkliste

## File Protocol

| Aktion | Datei |
|---|---|
| MODIFIED | `reference/prompts/bootstrap.md` |
| MODIFIED | `README.md` |
| CREATED | `WORKING/WORKPAPER/2026-03-27-issue-25-bootstrap-gap.md` |
| MODIFIED | `WORKING/DIARY/2026-03.md` |
| MODIFIED | `WORKING/MEMORY/ltm-index.md` |

## Decisions

- LTM-Query und Workpaper-Prompt als eigenständige Sektionen statt als Varianten des Session-Start-Prompts — damit User sie einzeln kopieren können.
- VS Code Snippet als Dokumentation in bootstrap.md statt als committete `.vscode/`-Datei — jedes Projekt hat seine eigenen .vscode-Einstellungen.
- "before starting any work" als explizite Formulierung im Session-Start-Prompt — adressiert direkt das 30%-Failure-Pattern.

## Next Steps

- Issue #25 auf GitHub schließen
- Issue #26 (Security Signals) als nächstes
