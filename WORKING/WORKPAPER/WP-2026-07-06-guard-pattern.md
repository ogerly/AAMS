# Workpaper: WP-2026-07-06-guard-pattern

**Datum:** 2026-07-06  
**Typ:** WP — Whitepaper-Implementierung  
**Priorität:** HOCH

---

## Session Scope

Guard-Pattern als WH-009 dokumentieren, .agent.json guard-Sektion ergänzen, AGENT_SCHEMA.json validieren, CONTRACT.md aktualisieren, INDEX.md mit WH-009, READ-AGENT.md Current Status updaten.

---

## Context from previous sessions

- **WH-009 erstellt** (dieses workpaper) — Guard-Pattern Dokumentation
- **aams-guard-plugin.ts** in WORKING/TOOLS/ — Referenzimplementierung für OpenCode
- **skill-opencode-agent.md** in WORKING/WORKPAPER/ — OpenCode-Agent-Skill mit Guard-Integration
- **LTM:** 137 Einträge, Dual-Layer (Audit-Log + ChromaDB)
- **Health-Score:** 7/10 post-migration (Repo-Sync 5/10, Core-Funktionalität intakt)
- **GitHub:** ogelry/AAMS — 9 offene Issues, keine neuen seit letztem Check

---

## Goal of this session

Guard-Pattern als WH-009 formalisieren und im Manifest verankern: Zwei-Ebenen-Modell (AAMS beschreibt Pattern, Implementierung = local_adaptation).

---

## Affected areas

- `WORKING/WHITEPAPER/WH-009-guard-pattern.md` — erstellt
- `reference/AGENT.json` — guard-Sektion ergänzt
- `reference/AGENT_SCHEMA.json` — guard-Schema ergänzt
- `reference/CONTRACT.md` — guard-Erwähnung
- `WORKING/WHITEPAPER/INDEX.md` — WH-009 Eintrag
- `READ-AGENT.md` — Current Status aktualisiert

---

## Session Overview

### Ausgangslage

Das Guard-Pattern wurde in früheren Sessions entwickelt (aams-guard-plugin.ts, skill-opencode-agent.md) aber nie als Whitepaper dokumentiert. Es fehlte die konzeptionelle Klärung: AAMS beschreibt ein Pattern, keine Implementierung.

### Ansatz

1. WH-009 als Whitepaper erstellen mit Zwei-Ebenen-Modell
2. .agent.json guard-Sektion als konkretes Beispiel ergänzen
3. AGENT_SCHEMA.json guard-Schema ergänzen (validierbar)
4. CONTRACT.md mit guard-Erwähnung aktualisieren
5. INDEX.md und READ-AGENT.md synchronisieren

---

## Results

### 1. WH-009 Whitepaper erstellt

`WORKING/WHITEPAPER/WH-009-guard-pattern.md` mit:
- Zwei-Ebenen-Modell: Pattern (AAMS) vs. Implementation (local_adaptation)
- Drei Check-Ebenen: manifest_read, workpaper_open, tools_gated
- Tool-agnostic design: jedes Tool implementiert anders
- Fehlerformate als Beispiel (nicht verpflichtend)
- Verweis auf Referenzimplementierung in WORKING/TOOLS/

### 2. .agent.json guard-Sektion ergänzt

```json
"guard": {
  "checks": {
    "manifest_read": { "required_reads": [".agent.json", "READ-AGENT.md"] },
    "workpaper_open": { "check": "WORKING/WORKPAPER/ contains status: open" },
    "tools_gated": { "gated_tools": ["write", "edit", "apply_patch", "bash"] }
  },
  "error_format": { ... },
  "implementation": { "opencode": "WORKING/TOOLS/aams-guard-opencode.ts", ... },
  "status": "descriptive_only"
}
```

### 3. AGENT_SCHEMA.json guard-Schema ergänzt

Vollständiges JSON Schema für die guard-Sektion:
- `checks` Objekt mit manifest_read, workpaper_open, tools_gated
- `error_format` mit beschreibenden (nicht imperativen) Nachrichten
- `implementation` für tool-spezifische Pfade
- `status` enum: "descriptive_only" | "enforced"
- Alles optional, patternProperties für Extensions

### 4. CONTRACT.md aktualisiert

Neue Zeile: `Includes optional guard pattern for contract enforcement — tool-agnostic specification (WH-009).`

### 5. INDEX.md synchronisiert

WH-009 Guard-Pattern in INDEX.md Tabelle + Footer-Update.

### 6. READ-AGENT.md Current Status aktualisiert

- Whitepapers: 8 → 9 (+ WH-009)
- `.agent.json`: + guard
- Guard-Pattern: WH-009 Zwei-Ebenen-Modell

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WHITEPAPER/WH-009-guard-pattern.md` | ✅ |
| CREATED | `WORKING/WORKPAPER/WP-2026-07-06-guard-pattern.md` | ✅ |
| MODIFIED | `reference/AGENT.json` | ✅ guard-Sektion |
| MODIFIED | `reference/AGENT_SCHEMA.json` | ✅ guard-Schema |
| MODIFIED | `reference/CONTRACT.md` | ✅ guard-Erwähnung |
| MODIFIED | `WORKING/WHITEPAPER/INDEX.md` | ✅ WH-009 Eintrag |
| MODIFIED | `READ-AGENT.md` | ✅ Current Status |

---

## Decisions and rationale

| # | Decision | Begründung |
|---|----------|------------|
| D1 | Zwei-Ebenen-Modell (Pattern vs. Implementation) | AAMS beschreibt WAS, nicht WIE. Jedes Tool hat eigene Architektur. |
| D2 | `status: descriptive_only` als Default | Keine Enforcement-Verpflichtung. Tools entscheiden selbst. |
| D3 | error_format als Beispiel | Fehlermeldungen sind tool-spezifisch, AAMS liefert nur Stil-Vorgabe (beschreibend, nicht imperativ). |
| D4 | implementation als mapping | Explizite Zuordnung: opencode → .ts, cursor → .md, etc. |
| D5 | Schema: alles optional | Guard ist ein optionales Pattern. Kein Breaking Change für bestehende Manifests. |

---

## Next Steps

### P0 — Nächste Session

| # | Aktion |
|---|--------|
| 1 | Remote-URL auf `ogerly/AAMS` aktualisieren (git remote set-url) |
| 2 | Issue #45 als Duplikat von #43 schließen |
| 3 | GitHub Releases für v2.0.0/v2.1.0/v2.2.0 erstellen |
| 4 | aams-guard-plugin.ts nach WORKING/TOOLS/ verschieben |
| 5 | Observe-Workpapers prüfen: WP-002, WP-003, WP-004 schließen |

### P1 — Nächste Sessions

| # | Aktion |
|---|--------|
| 6 | Issue #49 (Upgrade-Transparenz) mit GitHub Releases schließen |
| 7 | Issue #51 (Skills) als Whitepaper oder Guideline finalisieren |
| 8 | Issue #50 (File Safety) mit Guard-Plugin integrieren |
| 9 | Issue #48 (Decision-Leck) mit WP-001 Update schließen |

---

## Session Closing Checklist

- [x] File protocol complete (created/modified)
- [x] No temporary test files in repo
- [x] No secrets/passwords/tokens in plain text
- [x] Whitepapers checked for currency (WH-009 created)
- [x] Architecture decisions noted (Guard-Pattern)
- [x] Next steps concretely formulated
- [x] Cleanup tasks named
- [x] LTM re-ingest performed

---

> Letztes Update: 2026-07-06 — WH-009 Guard-Pattern implementiert. Zwei-Ebenen-Modell: AAMS beschreibt Pattern, Implementierung = local_adaptation. .agent.json + AGENT_SCHEMA.json + CONTRACT.md + INDEX.md + READ-AGENT.md synchronisiert.
