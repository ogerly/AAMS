# WP-2026-07-07: Skills, Guard & Agent-Erkennung

**Datum:** 2026-07-07  
**Typ:** WP — Whitepaper-Planung  
**Priorität:** HOCH

---

## Session Goal

Skills/Konzept finalisieren mit absoluter Neutralität. AAMS muss zuerst das aufrufende Agent/Coding-Tool erkennen. Guard und Plugin nur als Vorschlag.

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/WP-2026-07-07-skills-guard-agent-erkennung.md` | ✅ |
| CREATED | `WORKING/WHITEPAPER/WH-010-skills.md` | ✅ |
| CREATED | `WORKING/TOOLS/skills/README.md` | ✅ |
| CREATED | `WORKING/TOOLS/skills/opencode/README.md` | ✅ |
| CREATED | `WORKING/TOOLS/skills/opencode/aams-guard.md` | ✅ |
| CREATED | `WORKING/TOOLS/skills/opencode/bootstrap.md` | ✅ |
| CREATED | `WORKING/TOOLS/skills/opencode/skill-discovery.md` | ✅ |
| CREATED | `WORKING/TOOLS/skills/cursor/README.md` | ✅ |
| CREATED | `WORKING/TOOLS/skills/claude-code/README.md` | ✅ |
| CREATED | `WORKING/TOOLS/skills/copilot/README.md` | ✅ |
| CREATED | `WORKING/TOOLS/skills/windsurf/README.md` | ✅ |
| CREATED | `WORKING/TOOLS/skills/aider/README.md` | ✅ |
| CREATED | `WORKING/TOOLS/skills/lm-studio/` | ✅ Verzeichnis angelegt |
| CREATED | `WORKING/TOOLS/skills/ollama/` | ✅ Verzeichnis angelegt |
| CREATED | `WORKING/TOOLS/skills/llama.cpp/` | ✅ Verzeichnis angelegt |
| CREATED | `WORKING/TOOLS/skills/openai-proxy/` | ✅ Verzeichnis angelegt |
| MODIFIED | `.agent.json` | ✅ tool_detection + skills aktualisiert |
| MODIFIED | `reference/AGENT.json` | ✅ skills + tool_detection + URLs |
| MODIFIED | `reference/AGENT_SCHEMA.json` | ✅ skills schema + URL |
| MODIFIED | `INDEX.md` | ✅ WH-010 eingetragen |
| MODIFIED | `README.md` | ✅ Sprachpolitik + Upgrade-Satz |

---

## 1. GitHub Releases — Warum wir welche brauchen

### Deine richtige Einsicht

> "Wir brauchen wahrscheinlich nur ein neues GitHub Release, wenn wir damit hier durch sind. Dann gibt es für die anderen was zum Upgraden."

**Korrektur:** Wir brauchen KEINE GitHub Releases für v2.0.0 / v2.1.0 / v2.2.0. Die Git-Tags genügen. Ein GitHub Release ist nur sinnvoll wenn wir ein "fertiges" AAMS haben das andere upgraden können.

### Was passiert mit den alten Tags?

| Tag | Status | Aktion |
|-----|--------|--------|
| v2.0.0 | Git-Tag nur | Behalten, kein GitHub Release |
| v2.1.0 | Git-Tag nur | Behalten, kein GitHub Release |
| v2.2.0 | Git-Tag nur | Behalten, kein GitHub Release |
| **nächster** | **GitHub Release** | Erst wenn Skills/Guard fertig |

**Begründung:** GitHub Releases sind für "verteilte Versionen". Wenn AAMS noch im Fluss ist, sind Releases irreführend. Die Git-Tags sind die Quelle der Wahrheit.

---

## 2. Skills — Absolute Neutralität

### Kernprinzip

> **AAMS ist neutral. AAMS ist standardlos.**  
> AAMS sagt NICHT welches Tool du verwenden sollst. AAMS sagt NICHT wie du Skills implementieren sollst.  
> AAMS beschreibt WAS ein Skill sein KANN. Jedes Tool entscheidet WIE.

### Manifest-Prinzip (D9)

- **Beschreibend, nicht preskriptiv** — "Ein Skill KANN ..." statt "Ein Skill MUSS ..."
- **Optional** — Keine Pflicht, Skills zu haben
- **Tool-agnostic** — Kein Tool wird bevorzugt
- **Local Adaptation** — Jeder Agent passt Skills an seine Umgebung an

---

## 3. Agent-Erkennung — Das entscheidende Problem

### Aktueller Stand

AAMS (.agent.json) ist statisch. Es weiss nicht welches Tool es aufruft.

**Problem:** Ein Skill für OpenCode ist für Claude Code wertlos. Ein Skill für Cursor ist für Copilot wertlos.

### Lösung: Tool-Erkennung im Manifest

```json
{
  "tool_detection": {
    "_doc": "AAMS detects the calling agent/tool at runtime. This enables tool-specific skill recommendations.",
    "mechanism": "environment_variable or config_file_inference",
    "priority": "mandatory_if_present"
  }
}
```

**Wie es funktioniert:**
1. `.agent.json` wird geladen
2. AAMS erkennt welches Tool den Aufruf macht (via Environment-Variable, config inference, oder user_hint)
3. Basierend auf der Erkennung werden tool-spezifische Skills vorgeschlagen
4. Wenn kein Skill existiert → AAMS schlägt ein Issue vor

### Tool-Erkennung — Beispiele

| Tool | Erkennungsmuster |
|------|------------------|
| OpenCode | `process.env.OPCODE_SESSION_ID` oder `.opencode/` vorhanden |
| Cursor | `.cursor/rules/` vorhanden + `CLAUDE.md` |
| Claude Code | `CLAUDE.md` im Root |
| GitHub Copilot | `.github/copilot-instructions.md` vorhanden |
| Windsurf | `.windsurfrules` vorhanden |
| Aider | `.aider.conf.yaml` vorhanden |

**Aber:** AAMS schreibt NICHT vor wie die Erkennung passiert. Es sagt nur: "Wenn du erkennen KANNST, dann nutze es."

---

## 4. Skill-Baukasten — Struktur

### Kernidee

Skills sind für JEDEN Agent SEPARAT und SAUBER. Kein gemischter Müll.

```
WORKING/TOOLS/skills/
├── opencode/
│   ├── aams-guard.ts          # Guard-Pattern für OpenCode
│   ├── bootstrap.md           # Bootstrap-Prompt für OpenCode
│   └── skill-discovery.md     # Skill-Discovery für OpenCode
├── cursor/
│   ├── aams-guard.mdc         # Guard-Pattern für Cursor
│   ├── bootstrap.md           # Bootstrap-Prompt für Cursor
│   └── skill-discovery.md     # Skill-Discovery für Cursor
├── claude-code/
│   ├── aams-guard.md          # Guard-Pattern für Claude Code
│   └── bootstrap.md           # Bootstrap-Prompt für Claude Code
├── copilot/
│   ├── aams-guard.md          # Guard-Pattern für Copilot
│   └── bootstrap.md           # Bootstrap-Prompt für Copilot
└── windsurf/
    ├── aams-guard.md          # Guard-Pattern für Windsurf
    └── bootstrap.md           # Bootstrap-Prompt für Windsurf
```

### Jeder Skill hat:

- **Datum** des Erstellungs-/Letztes-Update
- **Version** (semver oder Datum)
- **Quelle** (wer hat ihn erstellt)
- **Status** (experimental / stable / deprecated)
- **Tool-Spezifische Implementierung** (nicht generisch)

---

## 5. Issue-Vorschlag — Wenn Tool nicht im Skill-Baukasten

### AAMS schlägt ein Issue vor wenn:

1. Tool-Erkennung erfolgreich
2. Kein Skill im Baukasten für dieses Tool gefunden
3. AAMS kennt das Tool nicht (noch nicht dokumentiert)

**Output:**
```
⚠ TOOL-NICHT-GEFUNDEN: AAMS erkennt 'unknown-tool' aber hat keine Skills dafür.
Vorschlag: Issue erstellen — `WORKING/TOOLS/skills/<tool>/` anlegen.
```

### Issue-Template für neue Tools

```markdown
# Tool-Support: <tool-name>

## Status
- **Erstellt:** YYYY-MM-DD
- **von:** <author>
- **Status:** experimental | stable | deprecated

## Tool-Erkennung
- <erkennungsmuster>

## Skills
- [ ] aams-guard
- [ ] bootstrap
- [ ] skill-discovery
- [ ] ...

## Notes
- <tool-spezifische Hinweise>
```

---

## 6. Guard — Nur als Vorschlag

### WH-009 Guard-Pattern — Korrektur

Aktueller Stand: Guard ist als "descriptive_only" markiert. Das ist korrekt.

**Aber:** Wir müssen klarer machen:

> **Guard ist ein Beispiel, keine Empfehlung.**  
> AAMS beschreibt ein Pattern. Die Implementierung ist lokal.  
> Du kannst Guard ignorieren. Du kannst Guard anpassen. Du kannst Guard ersetzen.  
> AAMS schreibt dir nichts vor.

### aams-guard-opencode.ts — Status

- Referenzimplementierung für OpenCode
- NICHT verpflichtend
- NICHT empfohlen (nur als Beispiel)
- **Vorschlag** wie ein Guard aussehen KANN

---

## 7. Decisions

| # | Decision | Begründung |
|---|----------|------------|
| D1 | Keine GitHub Releases für v2.0.0-v2.2.0 | Git-Tags genügen. Releases erst bei "fertiger" Version |
| D2 | Absolute Neutralität bei Skills | AAMS ist standardlos. Kein Tool wird bevorzugt |
| D3 | Tool-Erkennung vor Skill-Empfehlung | Ein Skill für OpenCode ist für Claude Code wertlos |
| D4 | Issue-Vorschlag wenn Tool fehlt | Automatisches Feedback für den Skill-Baukasten |
| D5 | Guard nur als Vorschlag | Manifest-Prinzip (D9): beschreibend, nicht preskriptiv |

---

## 8. Skill-Baukasten — Ausgeführt (diese Session)

### Was erstellt wurde

| # | Aktion | Status |
|---|--------|--------|
| 1 | `WORKING/TOOLS/skills/README.md` — Hauptdatei mit Erklärung, Standard, Aufruf zum Mitmachen | ✅ |
| 2 | `WORKING/TOOLS/skills/opencode/` — 4 Dateien (README, aams-guard, bootstrap, skill-discovery) | ✅ |
| 3 | `WORKING/TOOLS/skills/cursor/` — README (nicht vorhanden) | ✅ |
| 4 | `WORKING/TOOLS/skills/claude-code/` — README (nicht vorhanden) | ✅ |
| 5 | `WORKING/TOOLS/skills/copilot/` — README (nicht vorhanden) | ✅ |
| 6 | `WORKING/TOOLS/skills/windsurf/` — README (nicht vorhanden) | ✅ |
| 7 | `WORKING/TOOLS/skills/aider/` — README (nicht vorhanden) | ✅ |
| 8 | `.agent.json` aktualisiert (tool_detection, skills) | ✅ |
| 9 | `reference/AGENT.json` aktualisiert (skills, tool_detection, URLs) | ✅ |
| 10 | `reference/AGENT_SCHEMA.json` aktualisiert (skills schema) | ✅ |
| 11 | `INDEX.md` aktualisiert (WH-010) | ✅ |
| 12 | `README.md` aktualisiert (Sprachpolitik, Upgrade-Satz) | ✅ |
| 13 | `WORKING/TOOLS/skills/lm-studio/` — Platzhalter | ✅ |
| 14 | `WORKING/TOOLS/skills/ollama/` — Platzhalter | ✅ |
| 15 | `WORKING/TOOLS/skills/llama.cpp/` — Platzhalter | ✅ |
| 16 | `WORKING/TOOLS/skills/openai-proxy/` — Platzhalter | ✅ |

### Der Skill-Standard

> **Dies ist der einzige Standard den AAMS definiert — und er ist unabhängig von AAMS.**

Ein Skill MUSS:

1. **Metadaten haben** — source, erstellt, von, status, tool, version, sprache
2. **Lokal sein** — nie universal
3. **Optional sein** — nie verpflichtend

Alles andere ist tool-spezifisch und jedem überlassen.

### Philosophie

> **AAMS darf nicht davon abhängig sein.**
> 
> Skills sind ein "nice have" — sie helfen zu verstehen wie Skills in einem Manifest-Kontext funktionieren, aber die Skills selbst sind universell einsetzbar.
> 
> Skills haben eine garantierte Auswirkung. Sie bedürfen aber eigener Pflege und Beobachtung. Dafür übernehmen wir keine Garantie.
> 
> **Ziel:** Ein stabiles AAMS Tool zu bieten. Der Rest ist keine Magie — das ist reine Disziplin.

### Aufruf zum Mitmachen

> **Wir fordern alle auf, mitzumachen. Skills zu verbessern und einzureichen.**
> 
> - **Skills für neue Tools erstellen** (die noch nicht im Builder sind)
> - **Bestehende Skills verbessern**
> - **Lokale Anpassungen für spezifische Projekte beisteuern**
> - **Dokumentation und Beispiele schreiben**

---

## 10. Lokale LLMs — Voll unterstützt

### Unser Setup (AAMS in der Praxis)

> **AAMS wird bevorzugt mit LM Studio + qwen/qwen3.6-35b-a3b eingesetzt.**
> 
> LM Studio als lokaler Inference-Server. Qwen 3.6 35B als Modell. Manchmal Ollama, manchmal llama.cpp direkt.

Das ist was AAMS voll unterstützt: **Du entscheidest welches Tool und welches Modell. AAMS ist neutral.**

### Lokale LLMs als "Tools"

Lokale LLMs sind keine "ausgenommen" — sie sind Tools wie jedes andere. Sie brauchen eigene Skills:

- **LM Studio** — OpenAI-compatible endpoint auf localhost
- **Ollama** — llama.cpp-basiert, eigene API
- **llama.cpp** — Direct binary, GGUF models
- **OpenAI-Proxy** — Jeder Provider mit OpenAI-compatible API

Jedes Local-LLM-Tool hat eigene:

- **Modell-Formate** (GGUF, ONNX, Safetensors, etc.)
- **Inference-Engines** (llama.cpp, Transformers, MLX, etc.)
- **Parameter-Konfigurationen** (temperature, top_p, context_window, etc.)
- **Proxy-Konfigurationen** (OpenAI-compatibel, custom endpoints, etc.)

### Verzeichnisse angelegt

| Tool | Verzeichnis | Status |
|------|-------------|--------|
| lm-studio | `WORKING/TOOLS/skills/lm-studio/` | ✅ Platzhalter |
| ollama | `WORKING/TOOLS/skills/ollama/` | ✅ Platzhalter |
| llama.cpp | `WORKING/TOOLS/skills/llama.cpp/` | ✅ Platzhalter |
| openai-proxy | `WORKING/TOOLS/skills/openai-proxy/` | ✅ Platzhalter |

---

## 11. Nächste Steps

### P0 — Nächste Session

| # | Aktion |
|---|--------|
| 1 | WH-010-Skills erstellen basierend auf diesen Entscheidungen |
| 2 | `.agent.json` tool_detection-Sektion ergänzen |
| 3 | AGENT_SCHEMA.json tool_detection-Schema ergänzen |
| 4 | INDEX.md mit WH-010 |
| 5 | READ-AGENT.md Current Status updaten |

### P1 — Nächste Sessions

| # | Aktion |
|---|--------|
| 6 | Skill-Baukasten-Struktur in `WORKING/TOOLS/skills/` anlegen |
| 7 | Guard-Pattern als Beispiel nur (nicht empfohlen) |
| 8 | Issue-Vorschlag-Logik in `.agent.json` dokumentieren |
| 9 | Skills für alle bekannten Tools separat erstellen |

---

## Session Closing Checklist

- [x] File protocol complete (created/modified)
- [x] No temporary test files in repo
- [x] No secrets/passwords/tokens in plain text
- [x] Whitepapers checked for currency (WH-010 created)
- [x] Architecture decisions noted (Skills, Guard, Agent-Erkennung)
- [x] Next steps concretely formulated
- [x] Cleanup tasks named
- [x] LTM re-ingest performed

---

> Letztes Update: 2026-07-07 — WP-2026-07-07 Session 3: Lokale LLMs (LM Studio, Ollama, llama.cpp, OpenAI-Proxy) hinzugefügt. AAMS unterstützt und setzt lokale LLMs voll ein. Unser Setup: LM Studio + qwen/qwen3.6-35b-a3b. Mitmachen für alle Tools erwünscht. Keine Garantie. Kein Magie — Disziplin.
