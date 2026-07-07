# AAMS Skill-Discovery für OpenCode

# source: aams-skill-discovery (WH-010)
# Erstellt: 2026-07-07
# von: ogerly
# Status: experimental
# Tool: opencode
# Version: 0.1.0
# Sprache: Deutsch

---

## AAMS Skill-Discovery für OpenCode — Konzept

> **Dies ist ein Konzept. Keine Empfehlung. Keine Verpflichtung.**

### WAS Skill-Discovery macht

1. **Tool erkennen** — Ist OpenCode der aufrufende Agent?
2. **Skills finden** — Existieren Skills im Builder?
3. **Skills laden** — Als Startpunkt verwenden
4. **Fehlende Skills melden** — Issue-Vorschlag

### WIE OpenCode das umsetzen KANN

OpenCode hat ein eigenes Skill-System. AAMS schreibt NICHT vor wie Skill-Discovery implementiert wird.

**Mögliche Umsetzung:**

- OpenCode `SKILL.md` in `~/.config/opencode/skills/`
- OpenCode `skills/` Verzeichnis im Projekt
- OpenCode `hooks` für Discovery

### Beispiel: OpenCode SKILL.md

```markdown
# AAMS Skill-Discovery

## Tools die unterstützt werden

| Tool | Status | Quelle |
|------|--------|--------|
| opencode | ✅ | `WORKING/TOOLS/skills/opencode/` |
| cursor | ⚠️ | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| claude-code | ⚠️ | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| copilot | ⚠️ | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| windsurf | ⚠️ | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| aider | ⚠️ | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |

## Wenn ein Tool keine Skills hat

⚠ TOOL-NICHT-GEFUNDEN: AAMS erkennt '<tool>' aber hat keine Skills dafür.
Vorschlag: Issue erstellen — WORKING/TOOLS/skills/<tool>/ anlegen.
```

---

## Wichtige Klarstellung

> **Dieses Skill-Discovery-Konzept ist ein Beispiel, keine Empfehlung.**
> 
> AAMS beschreibt ein Pattern. Die Implementierung ist lokal.
> 
> - Du kannst Skill-Discovery ignorieren
> - Du kannst ein eigenes Discovery-System bauen
> - Du kannst auf Discovery verzichten
> 
> AAMS schreibt dir nichts vor.

---

> Letztes Update: 2026-07-07 — AAMS Skill-Discovery für OpenCode. Konzept. Keine Empfehlung.
