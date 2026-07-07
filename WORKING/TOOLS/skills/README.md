# AAMS Skill Builder

> **Skills sind kristallisiertes Wissen. Jeder Agent braucht eigene Skills. Kein "one-size-fits-all".**

---

## Warum separat?

Ein Skill für OpenCode ist für Claude Code wertlos. Ein Skill für Cursor ist für Copilot wertlos.
Ein Skill für LM Studio ist für Ollama wertlos. Ein Skill für llama.cpp ist für jedes andere Local-LLM-Tool wertlos.

Jedes Coding-Tool hat eigene:

- **Konfigurationsformate** (`.opencode/`, `.cursor/rules/`, `CLAUDE.md`, `.windsurfrules`, etc.)
- **Plugin-Systeme** (Hooks, Extension API, Skill-Discovery)
- **Permission-Modelle** (statisch, dynamisch, session-basiert)
- **Agent-Erkennung** (environment variables, config inference, user hint)

Jedes Local-LLM-Tool hat eigene:

- **Modell-Formate** (GGUF, ONNX, Safetensors, etc.)
- **Inference-Engines** (llama.cpp, Transformers, MLX, etc.)
- **Parameter-Konfigurationen** (temperature, top_p, context_window, etc.)
- **Proxy-Konfigurationen** (OpenAI-compatibel, custom endpoints, etc.)

Ein universal Skill würde alle diese Unterschiede ignorieren — und damit für KEIN Tool funktionieren.

**Skills sind lokal. Immer.**

---

## Der AAMS Skill Standard

> **Dies ist der einzige Standard den AAMS definiert — und er ist unabhängig von AAMS.**

Ein Skill MUSS diese Struktur und Metadaten haben. Das ist der einzige Standard den wir setzen. Alles andere ist optional und tool-spezifisch.

### Datei-Struktur

```
<tool-name>/
├── README.md              # Warum dieser Skill existiert, wie man mitmacht
├── SKILL-STANDARD.md      # Der AAMS Skill Standard (diese Datei)
├── aams-guard.md          # Guard-Pattern für dieses Tool
├── bootstrap.md           # Bootstrap-Prompt für dieses Tool
├── skill-discovery.md     # Skill-Discovery für dieses Tool
└── <optional-file>        # Tool-spezifische Erweiterungen
```

### Metadaten (Pflicht in jedem Skill)

Jeder Skill MUSS diese Header haben:

```markdown
# source: aams-guard-pattern (WH-010)
# Erstellt: YYYY-MM-DD
# von: <author>
# Status: experimental | stable | deprecated
# Tool: <tool-name>
# Version: <semver>
# Sprache: <language>
```

| Feld | Beschreibung |
|------|-------------|
| `source` | Ursprung des Skills (welches Whitepaper) |
| `Erstellt` | Erstellungsdatum |
| `von` | Autor |
| `Status` | experimental / stable / deprecated |
| `Tool` | Target-Tool (opencode, cursor, claude-code, etc.) |
| `Version` | Semver oder Datum |
| `Sprache` | Sprache der Dokumentation (Deutsch, Englisch, etc.) |

### Der Standard ist unabhängig von AAMS

> **AAMS darf nicht davon abhängig sein.**

Der Skill Standard ist ein eigenständiges Konzept. Er funktioniert auch ohne AAMS. AAMS ist ein "nice have" — es hilft zu verstehen wie Skills in einem Manifest-Kontext funktionieren, aber die Skills selbst sind universell einsetzbar.

---

## Skills als "Nice Have"

> **Skills haben eine garantierte Auswirkung. Sie bedürfen aber eigener Pflege und Beobachtung. Dafür übernehmen wir keine Garantie.**

Skills sind:

- **Empfohlen** — nicht verpflichtend
- **Lokal gepflegt** — jeder Adapter muss gewartet werden
- **Ohne Garantie** — wir übernehmen keine Garantie für die Funktion
- **Ohne Magie** — der Rest ist Disziplin

**Ziel:** Ein stabiles AAMS Tool zu bieten. Der Rest ist keine Magie — das ist reine Disziplin.

---

## Mitmachen

> **Wir fordern alle auf, mitzumachen. Skills zu verbessern und einzureichen.**

### Wie man mitmacht

1. **Skill für ein Tool erstellen** — nach dem Standard oben
2. **In `WORKING/TOOLS/skills/<tool>/` ablegen**
3. **Pull Request öffnen** — wir prüfen und mergen

### Wer kann mitmachen?

- Jeder der mit AAMS arbeitet
- Jeder der ein Tool nutzt das noch keine Skills hat
- Jeder der einen bestehenden Skill verbessern kann

### Was wird gesucht?

- Skills für neue Tools (die noch nicht im Builder sind)
- Verbesserungen bestehender Skills
- Lokale Anpassungen für spezifische Projekte
- Dokumentation und Beispiele

---

## Skill Builder

### Coding-Agents

| Tool | Status | Quelle |
|------|--------|--------|
| opencode | ✅ experimental | `WORKING/TOOLS/skills/opencode/` |
| cursor | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| claude-code | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| copilot | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| windsurf | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| aider | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |

### Lokale LLMs

| Tool | Status | Quelle |
|------|--------|--------|
| lm-studio | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| ollama | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| llama.cpp | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| openai-proxy | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |

### Unser Setup (AAMS in der Praxis)

> **AAMS wird bevorzugt mit LM Studio + qwen/qwen3.6-35b-a3b eingesetzt.**
> 
> LM Studio als lokaler Inference-Server. Qwen 3.6 35B als Modell. Manchmal Ollama, manchmal llama.cpp direkt.
> 
> Das ist was AAMS voll unterstützt: **Du entscheidest welches Tool und welches Modell. AAMS ist neutral.**

### Local LLMs / Proxy

| Tool | Status | Quelle |
|------|--------|--------|
| lm-studio | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| ollama | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| llama.cpp | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |
| openai-proxy | ⚠️ nicht vorhanden | [Mitmachen](https://github.com/ogerly/AAMS/issues/new) |

### Unser Setup (AAMS in der Praxis)

> **AAMS wird bevorzugt mit LM Studio + qwen/qwen3.6-35b-a3b eingesetzt.**
> 
> LM Studio als lokaler Inference-Server. Qwen 3.6 35B als Modell. Manchmal Ollama, manchmal llama.cpp direkt.
> 
> Das ist was AAMS voll unterstützt: **Du entscheidest welches Tool und welches Modell. AAMS ist neutral.**

---

## Philosophie

> **AAMS ist neutral. AAMS ist standardlos.**

Der einzige Standard den wir setzen:

1. **Skills haben Metadaten** (source, erstellt, von, status, tool, version, sprache)
2. **Skills sind lokal** — nie universal
3. **Skills sind optional** — nie verpflichtend

Alles andere ist jedem überlassen.

---

> Letztes Update: 2026-07-07 — AAMS Skill Builder. Skills sind lokal, optional, mit Metadaten. Der einzige Standard: Metadaten + lokale Struktur. Mitmachen erwünscht. Keine Garantie. Kein Magie — Disziplin.
