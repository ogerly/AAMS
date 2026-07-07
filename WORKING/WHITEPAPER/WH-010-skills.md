# WH-010 — Skills: Kristallisiertes Wissen im Manifest

**Datum:** 2026-07-07  
**Version:** AAMS/2.0  
**Status:** Aktiv

---

## Sinn

Skills sind kristallisiertes Wissen der Gemeinschaft. Sie ermöglichen es einem Agent, nicht bei Null zu starten, sondern auf erprobtem Wissen aufzubauen.

AAMS sagt NICHT welches Tool du verwenden sollst. AAMS sagt NICHT wie du Skills implementieren sollst.

AAMS beschreibt WAS ein Skill sein KANN. Jedes Tool entscheidet WIE.

---

## Kernprinzip: Standardlosigkeit

> AAMS ist neutral. AAMS ist standardlos.

- **Beschreibend, nicht preskriptiv** — "Ein Skill KANN ..." statt "Ein Skill MUSS ..."
- **Optional** — Keine Pflicht, Skills zu haben
- **Tool-agnostic** — Kein Tool wird bevorzugt
- **Local Adaptation** — Jeder Agent passt Skills an seine Umgebung an

Ein Skill für OpenCode ist für Claude Code wertlos. Ein Skill für Cursor ist für Copilot wertlos.
Ein Skill für LM Studio ist für Ollama wertlos. Ein Skill für llama.cpp ist für jedes andere Local-LLM-Tool wertlos.

**Auch lokale LLMs zählen als "Tools".**

Skills sind niemals universal. Sie sind immer lokal.

---

## Lokale LLMs — Voll unterstützt

> **AAMS unterstützt und setzt lokale LLMs voll ein.**

Unser Setup:

- **LM Studio** als lokaler Inference-Server (OpenAI-compatible endpoint)
- **qwen/qwen3.6-35b-a3b** als Modell
- Manchmal **Ollama**
- Manchmal **llama.cpp** direkt

Das ist was AAMS voll unterstützt: **Du entscheidest welches Tool und welches Modell. AAMS ist neutral.**

Ein Skill für LM Studio ist für Ollama wertlos. Ein Skill für Ollama ist für llama.cpp wertlos.

Jedes Local-LLM-Tool hat eigene:

- **Modell-Formate** (GGUF, ONNX, Safetensors, etc.)
- **Inference-Engines** (llama.cpp, Transformers, MLX, etc.)
- **Parameter-Konfigurationen** (temperature, top_p, context_window, etc.)
- **Proxy-Konfigurationen** (OpenAI-compatibel, custom endpoints, etc.)

**Aber:** AAMS schreibt NICHT vor wie die Erkennung passiert. Es sagt nur: "Wenn du erkennen KANNST, dann nutze es."

---

## Vorgang: Wie Skills funktionieren

### 1. Tool-Erkennung

Bevor ein Skill empfohlen wird, muss AAMS das aufrufende Tool erkennen.

```json
"tool_detection": {
  "_doc": "AAMS erkennt das aufrufende Agent/Coding-Tool. Basierend auf der Erkennung werden tool-spezifische Skills vorgeschlagen. Die Erkennungsmethode ist vom Tool abhängig.",
  "mechanism": "environment_variable or config_file_inference",
  "priority": "mandatory_if_present"
}
```

**Beispiele für Erkennungsmuster:**

| Tool | Erkennungsmuster |
|------|------------------|
| OpenCode | `OPCODE_SESSION_ID` vorhanden oder `.opencode/` Verzeichnis |
| Cursor | `.cursor/rules/` vorhanden + `CLAUDE.md` |
| Claude Code | `CLAUDE.md` im Root |
| GitHub Copilot | `.github/copilot-instructions.md` vorhanden |
| Windsurf | `.windsurfrules` vorhanden |
| Aider | `.aider.conf.yaml` vorhanden |
| **LM Studio** | LM Studio läuft auf localhost (Standard-Port 1234), OpenAI-compatible endpoint |
| **Ollama** | `ollama serve` läuft auf localhost (Standard-Port 11434) |
| **llama.cpp** | `llama-server` oder llama.cpp binary läuft, GGUF Modell geladen |
| **OpenAI-Proxy** | OpenAI-compatible API Endpoint konfiguriert (jeder Provider) |

**Aber:** AAMS schreibt NICHT vor wie die Erkennung passiert. Es sagt nur: "Wenn du erkennen KANNST, dann nutze es."

### 2. Skill-Discovery

Nach der Tool-Erkennung sucht AAMS nach Skills:

```
WORKING/TOOLS/skills/<tool-name>/
├── aams-guard.md          # Guard-Pattern für dieses Tool
├── bootstrap.md           # Bootstrap-Prompt für dieses Tool
├── skill-discovery.md     # Skill-Discovery für dieses Tool
└── ...
```

**Regeln:**

- Jeder Skill hat ein Datum (Erstellung + letztes Update)
- Jeder Skill hat eine Version (semver oder Datum)
- Jeder Skill hat eine Quelle (wer hat ihn erstellt)
- Jeder Skill hat einen Status (experimental / stable / deprecated)

### 3. Issue-Vorschlag

Wenn ein Tool erkannt wird aber kein Skill im Baukasten existiert:

```
⚠ TOOL-NICHT-GEFUNDEN: AAMS erkennt '<tool>' aber hat keine Skills dafür.
Vorschlag: Issue erstellen — `WORKING/TOOLS/skills/<tool>/` anlegen.
```

Dies ermöglicht Feedback-Loop für den Skill-Baukasten.

---

## Handhabung

### Für den Entwickler

Ein Skill ist eine lokale Anpassung. Er trägt seine Quelle als Header:

```markdown
# source: aams-guard-pattern (WH-010)
# Erstellt: 2026-07-07
# von: ogerly
# Status: experimental
# Tool: opencode
# Version: 0.1.0
```

### Für den Agent

Beim Bootstrap:

1. `.agent.json` lesen
2. Tool-Erkennung durchführen (wenn möglich)
3. Nach Skills im Baukasten suchen
4. Wenn Skills gefunden: als Startpunkt verwenden (nicht als Pflicht)
5. Wenn keine Skills gefunden: den Nutzer informieren (optional)
6. Wenn Tool nicht bekannt: Issue-Vorschlag machen (optional)

### Für die Gemeinschaft

Skills sind kristallisiertes Wissen. Wer einen Skill erstellt, teilt erprobtes Wissen.

- **Global Pool** — Quelle der Wahrheit, nicht modifizierbar, nur referenzierbar
- **Lokale Anpassung** — 100% auf den Projekt-Kontext zugeschnitten, Quelle bleibt erhalten

---

## Skill-Baukasten-Struktur

### Coding-Agents

```
WORKING/TOOLS/skills/
├── opencode/
│   ├── aams-guard.md          # Guard-Pattern für OpenCode
│   ├── bootstrap.md           # Bootstrap-Prompt für OpenCode
│   └── skill-discovery.md     # Skill-Discovery für OpenCode
├── cursor/
│   ├── aams-guard.md          # Guard-Pattern für Cursor
│   ├── bootstrap.md           # Bootstrap-Prompt für Cursor
│   └── skill-discovery.md     # Skill-Discovery für Cursor
├── claude-code/
│   ├── aams-guard.md          # Guard-Pattern für Claude Code
│   └── bootstrap.md           # Bootstrap-Prompt für Claude Code
├── copilot/
│   ├── aams-guard.md          # Guard-Pattern für Copilot
│   └── bootstrap.md           # Bootstrap-Prompt für Copilot
├── windsurf/
│   ├── aams-guard.md          # Guard-Pattern für Windsurf
│   └── bootstrap.md           # Bootstrap-Prompt für Windsurf
└── aider/
    ├── aams-guard.md          # Guard-Pattern für Aider
    └── bootstrap.md           # Bootstrap-Prompt für Aider
```

### Lokale LLMs

```
WORKING/TOOLS/skills/
├── lm-studio/
│   ├── README.md              # Warum dieser Skill existiert, wie man mitmacht
│   └── ...
├── ollama/
│   ├── README.md
│   └── ...
├── llama.cpp/
│   ├── README.md
│   └── ...
└── openai-proxy/
    ├── README.md
    └── ...
```

**Jeder Skill ist SEPARAT und SAUBER.** Kein gemischter Müll. Kein "one-size-fits-all".

---

## Manifest-Integration

### .agent.json

```json
"tool_detection": {
  "_doc": "AAMS erkennt das aufrufende Agent/Coding-Tool. Basierend auf der Erkennung werden tool-spezifische Skills vorgeschlagen.",
  "mechanism": "environment_variable or config_file_inference",
  "priority": "mandatory_if_present"
},

"skills": {
  "_doc": "Beschreibt die Beziehung zwischen globalem Skill-Pool und lokalen Anpassungen. Skills sind kristallisiertes Wissen der Gemeinschaft — Agents können sie als Startpunkt verwenden.",
  "global_pool": {
    "_doc": "Ein globaler Pool von Skills ist die Quelle der Wahrheit. Nicht modifizierbar — nur referenzierbar.",
    "reference": "https://skills.sh"
  },
  "local_adaptation": {
    "_doc": "Wenn ein Skill für ein Projekt angepasst wird, trägt er seine Quelle als Header und kann zu 100% auf den Projekt-Kontext zugeschnitten werden.",
    "storage": "WORKING/TOOLS/skills/<tool-name>/"
  },
  "issue_suggestion": {
    "_doc": "Wenn ein erkanntes Tool keine Skills im Baukasten hat, kann AAMS einen Issue-Vorschlag machen.",
    "enabled": true,
    "format": "⚠ TOOL-NICHT-GEFUNDEN: AAMS erkennt '<tool>' aber hat keine Skills dafür. Vorschlag: Issue erstellen — WORKING/TOOLS/skills/<tool>/ anlegen."
  },
  "relationship": {
    "_doc": "Global → Lokal: Quelle → Feinschliff. Exploration → direkter Griff."
  }
}
```

### AGENT.json

```json
"skills": {
  "_doc": "Optional. Skills are crystallized community knowledge. Agents may use them as starting points, not as requirements.",
  "global_pool": {
    "_doc": "A global pool of skills is the source of truth. Not to be modified — only referenced.",
    "reference": "https://skills.sh"
  },
  "local_adaptation": {
    "_doc": "When a skill is adapted for a project, it carries its origin as a header comment (# source: origin/skill-name) and may be tailored to the project context.",
    "storage": "WORKING/TOOLS/skills/<tool-name>/"
  },
  "issue_suggestion": {
    "_doc": "When a detected tool has no skills in the builder, AAMS may suggest creating a new skill entry.",
    "enabled": true
  },
  "relationship": {
    "_doc": "Global → Local: Source → Refinement. Exploration → direct reach."
  }
}
```

---

## Guard — Nur als Vorschlag

> Guard ist ein Beispiel, keine Empfehlung.

AAMS beschreibt ein Pattern. Die Implementierung ist lokal.

- Du kannst Guard ignorieren
- Du kannst Guard anpassen
- Du kannst Guard ersetzen

AAMS schreibt dir nichts vor.

---

## Decisions

| # | Decision | Begründung |
|---|----------|------------|
| D1 | Absolute Neutralität | AAMS ist standardlos. Kein Tool wird bevorzugt |
| D2 | Tool-Erkennung vor Skill-Empfehlung | Ein Skill für OpenCode ist für Claude Code wertlos |
| D3 | Skills optional | Manifest-Prinzip (D9): beschreibend, nicht preskriptiv |
| D4 | Issue-Vorschlag wenn Tool fehlt | Automatisches Feedback für den Skill-Baukasten |
| D5 | Guard nur als Vorschlag | Manifest-Prinzip (D9): beschreibend, nicht preskriptiv |
| D6 | Jeder Skill separat | Kein "one-size-fits-all". Jeder Agent braucht eigene Skills |
| D7 | Lokale LLMs voll unterstützt | LM Studio, Ollama, llama.cpp — Du entscheidest. AAMS ist neutral. |

---

## Nächste Schritte

| # | Aktion |
|---|--------|
| 1 | Skill-Baukasten-Struktur in `WORKING/TOOLS/skills/` anlegen |
| 2 | Guard-Pattern als Beispiel nur (nicht empfohlen) |
| 3 | Skills für alle bekannten Tools separat erstellen |
| 4 | Issue-Vorschlag-Logik in `.agent.json` dokumentieren |

---

> Letztes Update: 2026-07-07 — WH-010: Skills als kristallisiertes Wissen. AAMS ist neutral und standardlos. Jeder Agent braucht eigene Skills. Lokale LLMs voll unterstützt (LM Studio + qwen/qwen3.6-35b-a3b). Guard nur als Vorschlag.
