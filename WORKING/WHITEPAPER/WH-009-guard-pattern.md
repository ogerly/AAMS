# WH-009: Guard-Pattern — Zwei-Ebenen-Modell für Contract Enforcement

**Datum:** 2026-07-06  
**Status:** Aktiv  
**Referenz:** Issue #48 (Decision-Kompoundierungs-Leck), Issue #47 (Tool Decay)

---

## Problem

AAMS beschreibt Workspace-Struktur und Dokumentationskonventionen — aber nicht, wie Agenten diese Konventionen **durchsetzen**.

Ohne Guard-Pattern:
1. Agenten lesen `.agent.json`, ignorieren es aber bei der Ausführung
2. Keine Validierung, ob ein Workpaper offen ist
3. Keine Prüfung, ob Manifest gelesen wurde
4. Tools (write/edit/bash) werden ohne Kontext ausgeführt

---

## Ansatz: Zwei-Ebenen-Modell

AAMS beschreibt ein **Pattern**, keine Implementierung. Jedes Tool (Opencode, Cursor, Claude Code, Copilot) implementiert das Pattern auf seine eigene Weise.

```
┌─────────────────────────────────────────────────────────┐
│                    AAMS-Spec (WHAT)                     │
│  "Vor jeder write-Operation: Workpaper muss offen sein" │
├─────────────────────────────────────────────────────────┤
│              Local Adaptation (HOW)                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │ Opencode │  │  Cursor  │  │ Claude   │             │
│  │  Plugin  │  │  Rules   │  │  MCP     │             │
│  └──────────┘  └──────────┘  └──────────┘             │
└─────────────────────────────────────────────────────────┘
```

**Prinzip:** AAMS sagt **was** geprüft werden muss. Das Tool entscheidet **wie**.

---

## Check-Ebenen

### Ebene 1: manifest_read

**Was:** Vor jeder write/edit-Operation muss das Agent Manifest gelesen sein.

**AAMS-Spec:**
```json
"guard": {
  "checks": {
    "manifest_read": {
      "required_reads": [".agent.json", "READ-AGENT.md"],
      "description": "Vor jeder write-Operation: Manifest muss geladen sein."
    }
  }
}
```

**Tool-Implementierung (Beispiel Opencode):**
```typescript
// aams-guard-opencode.ts
const readState = new Set<string>();
// tool.execute.before hook:
if (tool === 'write' && !readState.has('.agent.json')) {
  // Block und lies Manifest
}
```

### Ebene 2: workpaper_open

**Was:** Vor jeder write/edit-Operation muss ein aktives Workpaper existieren.

**AAMS-Spec:**
```json
"guard": {
  "checks": {
    "workpaper_open": {
      "check": "WORKING/WORKPAPER/ enthält Datei mit status: open",
      "description": "Alle Änderungen müssen session-gebunden dokumentiert sein."
    }
  }
}
```

**Tool-Implementierung (Beispiel Cursor):**
```json
// .cursor/rules/aams-guard.mdc
// Vor jedem Edit: Prüfe WORKING/WORKPAPER/ für offene Workpapers
// Wenn keine existiert: Erstelle neue mit status: open
```

### Ebene 3: tools_gated

**Was:** write/edit/apply_patch/bash werden erst freigegeben, wenn Ebene 1 + 2 erfüllt.

**AAMS-Spec:**
```json
"guard": {
  "checks": {
    "tools_gated": {
      "gated_tools": ["write", "edit", "apply_patch", "bash"]
    }
  }
}
```

---

## Fehlerformate

AAMS empfiehlt beschreibende (nicht imperativische) Fehlermeldungen:

```json
"guard": {
  "error_format": {
    "manifest_not_read": "GUARD-VERSTOSS: Lies zuerst .agent.json und READ-AGENT.md, bevor du Änderungen vornimmst.",
    "no_workpaper": "GUARD-VERSTOSS: Kein offenes Workpaper unter WORKING/. Lege zuerst ein Workpaper an."
  }
}
```

**Warum beschreibend?** Imperative Form ("Du MUSST...") widerspricht D9 (Manifest-Prinzip). Beschreibende Form informiert über den Zustand, nicht über das Verhalten.

---

## Schema

Die guard-Sektion ist im AGENT_SCHEMA.json validierbar:

```json
{
  "$id": "https://github.com/ogerly/AAMS/schema/v1.0/guard.json",
  "properties": {
    "checks": {
      "manifest_read": { "required_reads": ["array"] },
      "workpaper_open": { "check": "string" },
      "tools_gated": { "gated_tools": ["array"] }
    },
    "error_format": { "manifest_not_read": "string" },
    "implementation": { "opencode": "path", "cursor": "path" },
    "status": { "enum": ["descriptive_only", "enforced"] }
  }
}
```

---

## Referenzimplementierungen

| Tool | Pfad | Status |
|------|------|--------|
| Opencode | `WORKING/TOOLS/aams-guard-opencode.ts` | ✅ Referenz |
| Cursor | `WORKING/TOOLS/aams-guard-cursor.md` | 📋 Planned |
| Claude Code | `WORKING/TOOLS/aams-guard-claude.md` | 📋 Planned |
| Copilot | `WORKING/TOOLS/aams-guard-copilot.md` | 📋 Planned |

---

## Design-Prinzipien

1. **Pattern, nicht Implementation** — AAMS sagt WAS, nicht WIE
2. **Optional** — guard ist kein Required-Feld in AGENT_SCHEMA.json
3. **Beschreibend, nicht imperativ** — Fehlermeldungen informieren, nicht befehlen
4. **Local Adaptation** — jedes Tool implementiert nach seiner Architektur
5. **Validierbar** — AGENT_SCHEMA.json erlaubt Tool-Validierung

---

## Status

- [x] WH-009 Whitepaper erstellt
- [x] .agent.json guard-Sektion als Beispiel
- [x] AGENT_SCHEMA.json guard-Schema
- [x] CONTRACT.md guard-Erwähnung
- [x] INDEX.md mit WH-009
- [x] READ-AGENT.md Current Status
- [ ] Referenzimplementierungen für Cursor/Claude/Copilot
- [ ] Issue #48 (Decision-Leck) teilweise gelöst durch Guard

---

> Letztes Update: 2026-07-06 — WH-009 Guard-Pattern: Zwei-Ebenen-Modell (AAMS beschreibt Pattern, Implementierung = local_adaptation). Manifest-Prinzip (D9) gewahrt: beschreibend, nicht imperativ.
