# WP-004 — Long-Horizon-Reasoning für reale Codebases

**WHITEPAPER — AAMS / Agent Manifest**  
**Status:** Active  
**Version:** 1.0  
**Created:** 2026-03-27  
**Updated:** 2026-04-29 — AAMS/2.0 Manifest-Prinzip  
**Source:** Workpaper `2026-03-27-long-horizon-reasoning-analyse.md` (Issue [#27](https://github.com/DEVmatrose/AAMS/issues/27))  
**Cross-Model-Validierung:** Kimi, ChatGPT, Grok, Claude (März 2026)

---

## Purpose

Dieses Whitepaper analysiert Long-Horizon-Reasoning (LHR) für reale Codebases und positioniert AAMS als die unterste lösbare Schicht im LHR-Stack. Es dokumentiert die konvergente Diagnose von vier unabhängigen KI-Modellen, die wirtschaftliche Bewertung und die identifizierten Gaps für die AAMS-Weiterentwicklung.

---

## 1. Was ist Long-Horizon-Reasoning?

**Long-Horizon-Reasoning (LHR)** bezeichnet die Fähigkeit eines KI-Agenten, über viele Schritte hinweg kohärent zu planen, zu handeln und Entscheidungen zu treffen — ohne den roten Faden zu verlieren.

> Ein Agent, der nicht nur die nächste Zeile Code schreibt, sondern versteht warum er sie schreibt, was vor 30 Schritten entschieden wurde, und welche Konsequenzen seine aktuelle Handlung 50 Schritte später hat.

### Abgrenzung

| Konzept | Fokus | Zeitrahmen | LHR-Relevanz |
|---------|-------|------------|--------------|
| **Chain-of-Thought (CoT)** | Schritt-für-Schritt-Ableitung innerhalb eines Prompts | Sekunden | Grundlage, nicht ausreichend |
| **ReAct / Tool-Use** | Reasoning + Acting in Schleifen | Minuten | Skaliert nicht über Sessions |
| **Tree-of-Thought (ToT)** | Parallele Ableitungspfade | Minuten | Verbessert Tiefe, nicht Langfristigkeit |
| **LHR** | Kohärente Planung über viele Schritte, Sessions, Entscheidungsketten | Stunden bis Tage | Das eigentliche Problem |
| **Agentic Planning** | Dekomposition + Ausführung komplexer Tasks | Minuten bis Stunden | Teilmenge — plant, aber vergisst |

---

## 2. Chronologie

| Jahr | Entwicklung | LHR-Bedeutung |
|------|-------------|---------------|
| 2022 | Chain-of-Thought (Wei et al.) | Schritt-für-Schritt verbessert Reasoning. Kein Langfrist-Aspekt. |
| 2023 | MemGPT (Packer et al.) | Erster ernster Ansatz, das Kontextfenster zu überwinden. |
| 2023 | Voyager (Wang et al.) | LLM-Agent in Minecraft, Hunderte Schritte. Erster LHR-Proof-of-Concept. |
| 2024 | SWE-bench (Jimenez et al.) | Reale SW-Tasks. Agents lösen ~30-40% isolierte Bugs. |
| 2024 | Devin (Cognition Labs) | Marketing übertrifft Realität. LHR-Defizite bei komplexen Tasks. |
| 2025 | o1/o3, Claude Extended Thinking | Natives Reasoning-Budget. Verbessert Single-Turn, nicht Cross-Session. |
| 2025 | Aider, Claude Code, Copilot Agents | Multi-Step-fähig. Kontextverlust bleibt Hauptproblem. |
| 2026 | Gas Town (Yegge) | 10-30+ parallele Agenten. Löst Parallelität, empfiehlt Rule-Dateien. |
| 2026 | AAMS v1.0.0 | Erster offener Standard für sessionsübergreifendes Scaffolding. |

---

## 3. Die Kern-Diagnose: Warum LHR heute scheitert

Vier unabhängige KI-Modelle (Kimi, ChatGPT, Grok, Claude) bestätigen dieselbe Diagnose:

> **LHR ist kein Problem der Modell-Intelligenz, sondern ein Infrastruktur-Problem des Zustands-Managements.**

### Failure Modes

| Failure Mode | Beschreibung | Bestätigt durch |
|---|---|---|
| **Session-Amnesie** | Jede neue Session ist ein Kaltstart. Agent muss mühsam rekonstruieren, *warum* in Schritt 12 eine Entscheidung getroffen wurde. | Alle 4 Modelle |
| **Kontext-Dilution** | 200k+ Token-Kontextfenster führen zum "Lost-in-the-Middle"-Phänomen. Mehr Kontext ≠ besseres Verständnis. | ChatGPT, Grok |
| **Plan-Drift** | Ohne explizite Ground Truth neigen Agenten nach 20-30 Schritten zu inkonsistenten Architekturentscheidungen. | Claude, Kimi |

### Aktueller Stand (März 2026)

**Funktioniert:**
- Single-Task-Reasoning innerhalb eines Kontextfensters (bis 200k Tokens)
- Kurzfristiges Tool-Use (Dateien lesen, Befehle ausführen, Tests laufen lassen)
- Parallele Agenten-Orchestrierung (Gas Town, OpenHands)

**Funktioniert nicht:**
- Kontextverlust über Sessions — jede neue Chat-Session startet bei null
- Kumulativer Planungsdrift — nach 50+ Schritten driftet das Ziel
- Entscheidungsrekonstruktion — "Warum haben wir in Schritt 12 das gemacht?" → Agent weiß es nicht
- Architekturverständnis über Zeit — Agent versteht Code im Moment, nicht die Entwicklungsgeschichte

---

## 4. Die unbequeme Wahrheit

| Aussage | Wahrheitsgehalt |
|---------|----------------|
| "LLMs können über lange Zeiträume kohärent planen" | **Falsch.** Ohne externes Scaffolding verliert jedes Modell den Faden nach ~20-30 Schritten. |
| "Extended Context Windows lösen das Problem" | **Teilweise.** 200k Tokens helfen innerhalb einer Session — aber Sessions enden. |
| "Autonome Agenten können Features von Anfang bis Ende bauen" | **Stark übertrieben.** Isolierte Tasks ja, zusammenhängende Architekturarbeit nein. |
| "LTM löst das Problem" | **Notwendig, aber nicht hinreichend.** LTM ohne Struktur ist ein Heuhaufen. |
| "AAMS löst LHR" | **Nein — aber es schafft die Voraussetzung.** |

---

## 5. AAMS als LHR-Enabler

### Architektonische Position

```
Reasoning           → Das Modell (o1, Claude, GPT, etc.)
Orchestrierung      → Das Framework (Gas Town, LangChain, etc.)
Gedächtnis-Backend  → Der Store (ChromaDB, Pinecone, etc.)
Scaffolding         → Der Repo-Contract (AAMS)         ◄── HIER
Codebase            → Das Repository
```

AAMS löst Long-Horizon-Reasoning nicht — es schafft die Voraussetzung. Das ist eine bewusste Designentscheidung.

### Was AAMS für LHR tut

| AAMS-Komponente | LHR-Funktion |
|-----------------|--------------|
| **Workpaper-Protokoll** | Operativer Checkpoint — was wurde in dieser Session entschieden? |
| **Whitepaper** | Architekturgedächtnis — stabile Systemwahrheit. Verhindert Architektur-Drift. |
| **Diary** | Entscheidungsrekonstruktion — WARUM wurde etwas entschieden? Das fehlende Zwischenstück. |
| **LTM (Dual-Track)** | Querybare Langzeiterinnerung — semantische Suche statt blindem Scan. |
| **Session-Start-Contract** | Automatischer Kontextaufbau — jede Session beginnt mit LTM-Abfrage, nicht bei null. |
| **Permissions** | Guardrails — verhindert destruktive Pfade in langen Reasoning-Ketten. |
| **File Protocol** | Auditierbarkeit — jede Dateiänderung dokumentiert. Multi-Step-Debugging möglich. |

### Was AAMS bewusst NICHT tut

- Reasoning selbst durchführen → das Modell
- Token-Management → MemGPT/Letta
- Agent-Orchestrierung → Gas Town
- Embedding/Retrieval → ChromaDB/Pinecone

### Analogie

> AAMS verhält sich zu LHR wie ein Dateisystem zu einer Datenbank. Das Dateisystem speichert und organisiert — die Abfrage-Intelligenz kommt von der Software darüber.

---

## 6. Cross-Model-Validierung

Vier unabhängige Modelle ordnen AAMS konsistent als unterste stabilisierende Schicht ein:

| Schicht | Komponente | Aufgabe |
|---|---|---|
| **Reasoning** | o1 / Claude / GPT | Logische Ableitung & Code-Generierung |
| **Orchestrierung** | Gas Town / OpenHands | Steuerung paralleler Agenten-Ströme |
| **Gedächtnis (LTM)** | ChromaDB / MemGPT | Technischer Abruf von Wissens-Schnipseln |
| **Scaffolding (AAMS)** | .agent.json / WORKPAPER | **Strukturierung des Wissens & Session-Kontrakt** |

### Konvergente Fakten

1. **Zustand > Intuition.** LHR erfordert, dass Goals, Constraints und Decisions als **First-Class Object** im Repository liegen — nicht im flüchtigen Chat-Verlauf.
2. **Wirtschaftlichkeit bestätigt.** 90% Token-Ersparnis für Kontext-Wiederaufbau gegen fast null Implementierungskosten.
3. **Open-Source-Zwang bestätigt.** Ein Standard für Repo-Interaktionen muss herstellerneutral sein.

### Meta-Erkenntnis

> **Wenn die Agenten selbst sagen, dass ihnen Scaffolding fehlt, ist das keine Marketing-Behauptung — es ist eine konvergente Selbstdiagnose der betroffenen Systeme.**

---

## 7. Wirtschaftliche Bewertung

### Kosten ohne Scaffolding

| Problem | Impact |
|---------|--------|
| Agent startet jede Session bei null | Token-Verbrauch x2-5 für Wiederholung |
| Architektur-Drift durch Kontextverlust | Refactoring-Kosten, technische Schulden |
| Doppelarbeit bei Multi-Agent-Teams | Agent B implementiert was Agent A verworfen hat |
| Fehlende Entscheidungsdokumentation | Debugging-Kosten multiplizieren sich |
| Kein Permission-Modell | Destruktive Änderungen ohne Guardrails |

### Kosten von AAMS

| Aufwand | Wert |
|---------|------|
| Initiales Setup | Eine Datei + curl. ~2 Minuten. |
| Laufender Overhead | ~0. Agent erstellt Workpapers automatisch. |
| Dependencies | Zero. JSON + Markdown. Optional: ChromaDB. |
| Vendor Lock-in | Keiner. |

### ROI (konservativ, mittleres Projekt, 2 Agenten, 10 Sessions/Woche)

| Metrik | Ohne AAMS | Mit AAMS | Delta |
|--------|-----------|----------|-------|
| Token-Verbrauch/Session (Kontextaufbau) | ~50k Tokens | ~5k Tokens (LTM-Query) | **-90%** |
| Architektur-Drift (Korrekturen/Monat) | 3-5 Eingriffe | 0-1 Eingriffe | **-80%** |
| Onboarding neuer Session | 10-15 Min. | 30 Sek. | **-96%** |
| Destruktive Änderungen/Monat | 1-2 | ~0 | **-95%** |

---

## 8. Open Source & Effizienz

### Warum LHR-Scaffolding Open Source sein MUSS

1. **Vendor-Neutralität ist Voraussetzung.** `.agent.json` wird von Copilot, Cursor, Claude Code, Codex, Windsurf, Aider, Continue.dev und CodeRabbit gelesen.
2. **Netzwerkeffekte.** Jedes Repo mit `.agent.json` ist sofort für jeden Agenten verständlich. Der `.editorconfig`-Effekt.
3. **Reproduzierbarkeit.** JSON + Markdown in Git = auditierbar, versionierbar, menschen- und maschinenlesbar.
4. **Kein Rent-Seeking.** Keine Lizenzgebühren, keine API-Keys, keine Cloud-Abhängigkeit. Das Dateisystem IST die Runtime.

### Effizienz

| Dimension | Assessment |
|-----------|-----------|
| **Onboarding** | Agent startet mit Kontext. Spart ~90% Aufbau. |
| **Token** | LTM-Query statt Full-Repo-Scan. -80-90% Wiederholung. |
| **Entscheidung** | Diary + Whitepaper = keine Neu-Ableitung. |
| **Audit** | File Protocol → jede Änderung nachvollziehbar. |
| **Multi-Agent** | Gemeinsamer Kontext-Layer → kein Wissensverfall. |

### Was Open Source nicht automatisch löst

- **Adoption braucht Zeit.** `.editorconfig` brauchte Jahre.
- **LTM-Qualität.** Ein leerer Index ist nutzlos. Der Agent muss diszipliniert ingestieren.
- **Governance.** Single maintainer, Issues + PRs offen.
- **Enforcement.** Empfehlung, nicht Zwang. Wie `.editorconfig`.

---

## 9. Einsatzfähigkeit (Stand März 2026)

| Fähigkeit | Status | Evidenz |
|-----------|--------|---------|
| `.agent.json` als Bootstrap-Contract | ✅ Produktionsreif | Feldberichte #17, #20 |
| `AGENTS.md` als Cross-Tool-Bridge | ✅ Produktionsreif | Nativ gelesen von 7+ Tools |
| Workpaper-Protokoll | ✅ Produktionsreif | 20+ geschlossene Workpapers |
| Whitepaper-Architekturschicht | ✅ Produktionsreif | 4 aktive Whitepapers |
| Diary (Temporal Context Layer) | ✅ Produktionsreif | 2 Monats-Dateien aktiv |
| LTM Dual-Track (Markdown + ChromaDB) | ✅ Funktional | 77+ Einträge, semantisch querybar |
| Permission-Layer | ⚠️ Deklarativ | Kein automatisches Enforcement |
| Multi-Agent-Koordination | ⚠️ Theoretisch | Kein Feldtest mit >2 Agenten |

---

## 10. Identifizierte Gaps → v1.1-Roadmap

| # | Gap | Beschreibung | Quelle | Priorität |
|---|---|---|---|---|
| G1 | **Standardisiertes LTM-Query-Protokoll** | Einheitlicher Tool-Call (`query_ltm`) für strukturierte Repo-Gedächtnis-Suche | Grok, ChatGPT | Hoch |
| G2 | **Automatische Kompression** | Session-Ende: Workpapers → prägnante LTM-Einträge. Rausch-Minimierung. | ChatGPT | Mittel |
| G3 | **Enforcement via CI** | Automatisierte Checks: "Kein Commit ohne Workpaper-Update" | Grok | Mittel |
| G4 | **Intent-Awareness** | Diary indiziert *Intent* (Absicht), nicht nur *was*. Für Refactoring-Motivation. | Claude, Kimi | Mittel |
| G5 | **Cross-Repo-Kontext** | AAMS ist repo-scoped. Agent über 3 Repos = 3 getrennte LTMs. | Analyse | Niedrig |

---

## 11. Kernthese

> **Long-Horizon-Reasoning für reale Codebases ist heute nicht gelöst — aber die Voraussetzung dafür ist lösbar. AAMS ist diese Voraussetzung.**

Ohne Scaffolding hat das Gedächtnis keine Struktur.  
Ohne Struktur hat die Orchestrierung keinen Kontext.  
Ohne Kontext dreht das Reasoning im Kreis.

**AAMS ist die unterste lösbare Schicht im LHR-Stack.**

Vier unabhängige KI-Modelle bestätigen: LHR ist ein Infrastruktur-Problem des Zustands-Managements, kein Problem der Modell-Intelligenz. Wenn die betroffenen Systeme selbst sagen, dass ihnen Scaffolding fehlt, ist das Evidenz.

---

## Referenzen

- Wei, J. et al. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.* NeurIPS 2022.
- Yao, S. et al. (2023). *Tree of Thoughts: Deliberate Problem Solving with Large Language Models.* NeurIPS 2023.
- Packer, C. et al. (2023). *MemGPT: Towards LLMs as Operating Systems.* arXiv:2310.08560.
- Wang, G. et al. (2023). *Voyager: An Open-Ended Embodied Agent with Large Language Models.* arXiv:2305.16291.
- Jimenez, C. E. et al. (2024). *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* ICLR 2024.
- Yegge, S. (2026). *Gas Town.* GitHub: https://github.com/steveyegge/gastown.
- AAMS Contract v2.0.0: https://github.com/DEVmatrose/AAMS

---

*Whitepaper maintained by project maintainer. Update on new LHR-relevant research, benchmarks, or field evidence.*
