---
name: opencode-agent
description: Skill für die Arbeit mit OpenCode als Coding-Agent-Tool — opencode.json-Konfiguration, Provider/Modell-Routing (z.B. MANTIS-Proxy), Permission-System, Plugin-Hooks (tool.execute.before/after), Skill-Discovery und das AAMS-Guard-Enforcement-Pattern. Trigger bei: "opencode.json", "OpenCode Plugin", "tool.execute.before", "AAMS-Guard", "Agent Permissions", "MANTIS Modellrouting", "OpenCode Skill erstellen", "OpenCode Subagent", ".opencode/plugin", ".opencode/skills".
---

# OpenCode Agent Skill

## Kontext

OpenCode ist das primäre Coding-Agent-Tool von ffff (VS Code), kombiniert mit AAMS
als Struktur-Layer. Lokales Standardmodell: `qwen/qwen3.6-35b-a3b` über den
MANTIS-LLM-Proxy (`http://192.168.0.70:9876/v1`). Jedes Repo hat im Root sowohl
einen `WORKING`-Ordner (AAMS) als auch eine `opencode.json`.

## Config-Hierarchie (Precedence, niedrig → hoch)

1. Remote-Org-Defaults (`.well-known/opencode`)
2. Global: `~/.config/opencode/opencode.json`
3. Projekt: `opencode.json` im Repo-Root
4. `OPENCODE_CONFIG_DIR` (falls gesetzt)
5. Managed Settings (nur mit Admin-Rechten, überschreibt alles)

Regeln (AGENTS.md/CLAUDE.md) folgen eigener Precedence: lokal (hochwandernd bis
zum Git-Root) > global `~/.config/opencode/AGENTS.md` > `~/.claude/CLAUDE.md`.
**Wichtig für AAMS:** `READ-AGENT.md` und `.agent.json` sind kein natives
OpenCode-Konzept — sie müssen entweder in `AGENTS.md` referenziert werden
(`@READ-AGENT.md`, wird bei Bedarf nachgeladen) oder über das Guard-Plugin
erzwungen werden (siehe unten).

## provider/model-Block (MANTIS-Routing)

```json
"provider": {
  "mantis": {
    "npm": "@ai-sdk/openai-compatible",
    "options": { "baseURL": "http://192.168.0.70:9876/v1", "apiKey": "mantis-local-proxy" },
    "models": { "qwen/qwen3.6-35b-a3b": { "name": "..." } }
  }
}
```

Modellwechsel zwischen lokal (LM Studio, garantiert) und Cloud-Fallback
(Ollama Cloud `:cloud`-Suffix, OpenRouter `:free`-Suffix) laufen alle über
denselben Proxy-Port `9876` — kein Config-Wechsel im Projekt nötig, nur
`"model"`-Feld ändern.

## Permission-System

Statisch, pro Session gleich. Reihenfolge: **letzte passende Regel gewinnt**.

```json
"permission": {
  "edit": { ".env": "ask", ".env.*": "ask", "*": "allow" },
  "bash": { "git push*": "ask", "rm -rf*": "deny", "*": "allow" }
}
```

Werte: `allow` (sofort), `ask` (Bestätigung), `deny` (hart blockiert — Modell
bekommt Fehlermeldung, kein Reminder). Per-Agent-Override möglich (`agent.build.permission`).
Für AAMS-Zwecke reicht das **nicht**, weil es keinen dynamischen Zustand kennt
("erst erlauben, nachdem X gelesen wurde"). Dafür braucht es ein Plugin.

## Plugin-Hooks (das eigentliche Enforcement-Werkzeug)

Datei: `.opencode/plugin/<name>.ts`. Wichtigste Hooks:
- `tool.execute.before(input, output)` — vor Tool-Ausführung, kann per `throw`
  blockieren
- `tool.execute.after(input, output)` — nach Ausführung, zum Mitschreiben von
  Zustand (z.B. "wurde `.agent.json` gelesen?")

### AAMS-Guard-Pattern

Gate: `write`/`edit`/`apply_patch`/`bash` erst erlauben, wenn in der Session
`.agent.json` + `READ-AGENT.md` gelesen wurden (Session-Set, per `sessionID`
getrackt). Vollständiges Muster inkl. Workpaper-Check: siehe
`references/aams-guard-plugin.md` in diesem Skill-Ordner.

### Bekannte Bugs (Stand: aktuelle OpenCode-Version, unbedingt prüfen ob noch offen)

- **Subagent-Bypass** (`tool.execute.before` greift nicht bei Subagent-Calls
  über den Task-Tool) — Guard ist umgehbar, sobald Subagents/Delegation im
  Spiel sind. Betrifft ffffs Setup aktuell nicht (kein Multi-Agent-Delegation).
- **SDK-Deny-Bug**: `deny`-Permissions in Custom-Agents werden ignoriert, wenn
  der Agent über das SDK (nicht TUI/CLI) gestartet wird. Relevant nur, falls
  je programmatisch via `@opencode-ai/sdk` gestartet wird statt über VS Code.

## Skill-Discovery (für spätere eigene Skills)

Reihenfolge beim Laden, letzter gewinnt bei Namenskonflikt:
1. `~/.config/opencode/skills/<name>/SKILL.md` (global)
2. `.opencode/skills/<name>/SKILL.md` (Projekt, höchste Priorität)
3. Kompatibel: `.claude/skills/`, `.agents/skills/` werden ebenfalls gescannt

Frontmatter-Pflichtfelder: `name` (lowercase, Bindestriche), `description`
(min. 20 Zeichen, entscheidet über Auto-Trigger — Trigger-Begriffe explizit
reinschreiben, wie in diesem Skill). Skills laden erst bei Session-Start neu
— nach Änderung OpenCode neu starten.

## Checkliste bei neuen AAMS-Projekten mit OpenCode

1. `opencode.json` aus Template kopieren (MANTIS-Provider-Block)
2. `.opencode/plugin/aams-guard.ts` einfügen
3. `AGENTS.md` mit `@READ-AGENT.md`-Referenz anlegen (oder auf Guard verlassen)
4. Kurztest: erste Aktion im neuen Chat sollte automatisch `.agent.json` lesen,
   bevor irgendein Edit versucht wird — sonst Guard-Fehlermeldung prüfen