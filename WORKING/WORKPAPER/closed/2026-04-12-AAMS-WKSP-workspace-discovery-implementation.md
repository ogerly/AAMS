# Workpaper — WORKSPACE Discovery Pattern Implementation

- **Datum:** 2026-04-12
- **Typ:** Implementation
- **Ziel:** Optional WORKSPACE container layer als Discovery-Pattern einführen (Weg A)

---

## Session-Ziel

Implementierung des WORKSPACE-Feldbericht-Ergebnisses als **optionales Discovery-Pattern** (Weg A), nicht als neuen Default (Weg B). Begründung: 110+ hardcodierte `WORKING/`-Pfade in 10+ Dateien machen einen Default-Wechsel zu destruktiv. Die curl-Invariante und Backward-Compatibility bleiben erhalten.

## Entscheidung

**Weg A gewählt:** WORKSPACE als optionales Discovery-Pattern.

- Wenn `./WORKSPACE/WORKING/` existiert → Agent nutzt das als effective root
- Wenn nicht → `./WORKING/` direkt (Status quo)
- entry_point bleibt immer im Repo-Root
- Kein bestehender Deploy bricht

## Änderungen

### `.agent.json`
- Neuer `workspace.discovery` Block mit `container_dir`, `detection`, `fallback`, `affects`
- Neuer Step `1a. DISCOVERY` in `on_first_entry`

### `READ-AGENT.md`
- Neuer Abschnitt "Discovery Rule" vor der Workspace-Structure-Tabelle

### `reference/SPEC.md`
- Neuer Abschnitt "#### Discovery (optional)" nach Base Fields

### `reference/SPEC-DE.md`
- Gleicher Abschnitt auf Deutsch

## Was NICHT geändert wurde (bewusst)

- Keine bestehenden `WORKING/`-Pfade umgeschrieben
- Kein `WORKSPACE/` in `.gitignore`, `README.md`, `AGENTS.md`, oder `reference/AGENT_SCHEMA.json`
- Kein Breaking Change an `_spec` oder Versionsnummer

## File Protocol

| Aktion | Datei |
|--------|-------|
| MODIFIED | `.agent.json` |
| MODIFIED | `READ-AGENT.md` |
| MODIFIED | `reference/SPEC.md` |
| MODIFIED | `reference/SPEC-DE.md` |
| CREATED | `WORKING/WORKPAPER/2026-04-12-AAMS-WKSP-workspace-discovery-implementation.md` |

## Next Steps

- [ ] AGENT_SCHEMA.json: `discovery`-Objekt ins JSON Schema aufnehmen (optional, kann eigene Session sein)
- [ ] reference/AGENT.json: Discovery-Block als Referenzbeispiel hinzufügen
- [ ] Mantis-Repos testen: WORKSPACE/-Verzeichnis anlegen und prüfen ob Agenten die Discovery-Logik verstehen
- [ ] Issue triage workpaper committen (noch offen von letzter Session)
