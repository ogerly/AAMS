# AAMS Migration Guide — v1.x → v2.0

## Ist das ein Breaking Change?

**Nein** — AAMS/2.0 ist backward-kompatibel.

Bestehende `./WORKING/`-Repos funktionieren weiterhin. Der curl-Befehl bleibt identisch.

## Was ändert sich automatisch?

- Neue Ordner in `workspace.structure` werden angelegt (idempotent)
- `topic_registry` in `.agent.json` — maschinenlesbare Topic-Liste für RFL-Pattern-Matching
- `agent_conventions` replaces `agent_contract` — beschreibend statt preskriptiv

## Was muss der User manuell tun?

- **Nichts.** AAMS/2.0 ist additive — kein manueller Schritt nötig.
- Optional: `.aams-version` Datei im Zielrepo anlegen für Upgrade-Transparenz.

## Was ändert sich NICHT?

- Bestehende Workpapers bleiben unberührt
- Bestehende WORKING/MEMORY/ bleibt unberührt
- curl-Befehl bleibt identisch
- Ordnerstruktur bleibt identisch
- `.agent.json` bleibt der einzige Bootstrap-Einstieg

## Backward Compatibility

- Repos mit `./WORKING/` (legacy) funktionieren weiterhin
- `_spec: AAMS-MINI/1.0` wird noch erkannt (deprecated, aber funktional)
- Alte Agenten die `_contract` nicht kennen: ignorieren das Feld (patternProperties `^_` erlaubt)
- JSON Schema: `_contract` required, `_spec` deprecated — alte Deployments mit nur `_spec` brechen nicht (patternProperties `^_` erlaubt)

## Was sich konzeptionell ändert

AAMS ist jetzt ein **Agent Manifest**, keine **Specification**.

- Beschreibt Workspace- und Dokumentationskonventionen
- Schreibt Agenten kein Verhalten vor
- Keine "MUST"-Sprache — beschreibend, nicht preskriptiv

Der curl-Befehl bleibt identisch:

```bash
curl -sO https://raw.githubusercontent.com/DEVmatrose/AAMS/main/.agent.json
```

---

> **AAMS/2.0 — Agent Manifest (not Specification)**
> AAMS describes. It does not prescribe.
> [Learn more](https://github.com/DEVmatrose/AAMS)
