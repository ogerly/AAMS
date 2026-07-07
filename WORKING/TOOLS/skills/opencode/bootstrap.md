# AAMS Bootstrap für OpenCode

# source: aams-bootstrap-pattern (WH-010)
# Erstellt: 2026-07-07
# von: ogerly
# Status: experimental
# Tool: opencode
# Version: 0.1.0
# Sprache: Deutsch

---

## AAMS Bootstrap für OpenCode — Prompt

> **Dies ist ein Beispiel. Keine Empfehlung. Keine Verpflichtung.**

### Prompt für OpenCode

```
Lies .agent.json und führe agent_contract.on_first_entry aus.
Erstelle die WORKING/ Struktur, scanne das Repo, schreibe das erste Workpaper und indiziere ins LTM.
```

### Prompt für bestehende Projekte (on_session_start)

```
Lies .agent.json und führe agent_contract.on_session_start aus.
Prüfe die Version. Query WORKING/MEMORY/ltm-index.md für Kontext.
Erstelle ein Workpaper in WORKING/WORKPAPER/ bevor du arbeitest.
```

### Was dieser Prompt macht

1. **`.agent.json` lesen** — Workspace-Vertrag
2. **`READ-AGENT.md` lesen** — Projektkontext
3. **Struktur erstellen** — falls fehlend
4. **Repo scannen** — File-Inventory
5. **Workpaper schreiben** — Session-Protokoll
6. **LTM indizieren** — Langzeitgedächtnis

---

## OpenCode-spezifische Hinweise

OpenCode kann diesen Prompt direkt im Chat verwenden.

**Für Chat-Agents (die nicht bootstrapen):**

```
Lies READ-AGENT.md und führe agent_contract.on_session_start aus.
Query WORKING/MEMORY/ltm-index.md für Kontext zu [THEMA].
Erstelle ein Workpaper in WORKING/WORKPAPER/ bevor du arbeitest.
```

---

## Wichtige Klarstellung

> **Dieser Bootstrap-Prompt ist ein Beispiel, keine Empfehlung.**
> 
> AAMS beschreibt ein Pattern. Die Implementierung ist lokal.
> 
> - Du kannst diesen Prompt ignorieren
> - Du kannst einen eigenen Prompt schreiben
> - Du kannst einen anderen Agent nutzen
> 
> AAMS schreibt dir nichts vor.

---

> Letztes Update: 2026-07-07 — AAMS Bootstrap für OpenCode. Beispiel. Keine Empfehlung.
