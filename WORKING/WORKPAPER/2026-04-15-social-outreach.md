# WP — Social Outreach & Netzwerk

| Feld    | Wert                                              |
|---------|---------------------------------------------------|
| Datum   | 2026-04-15                                        |
| Status  | AKTIV                                             |
| Autor   | Agent (Copilot / Claude Sonnet 4.6)               |
| Scope   | Kontakte, Kooperationen, Community-Aufbau         |

---

## 1. Zweck dieses Workpapers

Dokumentiert alle Personen, mit denen im Kontext von AAMS Kontakt aufgebaut wurde oder wird.
Enthält: Kontext, Projekt-Analyse, Gesprächsstatus, geplante Nachricht.

---

## 2. Kontaktliste

### Kontakt 001 — Igor Lins e Silva

| Feld              | Wert                                                        |
|-------------------|-------------------------------------------------------------|
| Name              | Igor Lins e Silva                                           |
| Pronouns          | He/Him                                                      |
| Rolle             | Chief Technology Officer @ EOS Rio                          |
| Standort          | Rio de Janeiro, Brasilien                                   |
| LinkedIn          | https://www.linkedin.com/in/igorls/                         |
| GitHub            | https://github.com/igorls                                   |
| Projekt           | https://github.com/MemPalace/mempalace                      |
| Status Kontakt    | ⏳ LinkedIn-Anfrage gestellt — warte auf Bestätigung        |
| Gesprächsstatus   | Noch kein Austausch — erst nach Bestätigung schreiben       |
| Priorität         | Hoch — inhaltlich sehr relevant (siehe Analyse unten)       |

---

## 3. Projektanalyse: MemPalace vs. AAMS

### Was ist MemPalace?

MemPalace ist ein **local-first AI-Memory-System**.  
Es speichert Gesprächshistorien als verbatim Text (keine Zusammenfassungen, keine Paraphrasen)
und ermöglicht semantische Suche über diese Inhalte.

**Architektur:**
- Strukturiertes Index-Modell: Personen/Projekte → Wings, Themen → Rooms, Inhalte → Drawers
- Pluggable Retrieval-Backend (Standard: ChromaDB)
- Temporales Knowledge Graph (Entity-Relationship + Validity-Windows, SQLite)
- 29 MCP-Tools für Palace-Reads/Writes, Knowledge-Graph, Agent-Diaries
- Jeder Agent bekommt eigenen Wing + Diary
- Auto-Save-Hooks für Claude Code (periodic + vor Context Compression)
- Python, MIT-Lizenz
- Benchmarks: 96.6% R@5 auf LongMemEval ohne LLM, 98.4% hybrid

**Zahlen (Stand: 2026-04-15):**
- 46.300 Stars
- 6.000 Forks
- 47 Contributors
- Aktiv: letzter Commit vor 1 Stunde
- igorls ist Hauptentwickler (top Contributor)

---

### Vergleich: MemPalace ↔ AAMS

#### Gemeinsamkeiten

| Dimension              | MemPalace                                    | AAMS                                             |
|------------------------|----------------------------------------------|--------------------------------------------------|
| Kernidee               | Persistenz über Sessions hinweg              | Persistenz über Sessions hinweg                   |
| Agent-Gedächtnis       | Wings + Diaries pro Agent                    | WORKING/DIARY/ + MEMORY/ pro Projekt             |
| Tool-Agnostik          | Pluggable Backend, MCP, Claude/Codex/Gemini  | Jeder Agent liest `.agent.json` + `READ-AGENT.md` |
| Lokale Ausführung      | Local-first, keine Cloud nötig               | Git-basiert, kein Cloud-Zwang                    |
| Strukturiertes Wissen  | Wings/Rooms/Drawers                          | WHITEPAPER/WORKPAPER/MEMORY/                     |
| Agent-Diaries          | `mempalace_list_agents` + diary pro Agent    | `WORKING/DIARY/` (monatlich, chronologisch)      |
| AGENTS.md vorhanden    | Ja (Symlink zu CLAUDE.md)                    | Ja (zentrales Steuerungsdokument)                |

#### Unterschiede

| Dimension              | MemPalace                                         | AAMS                                                         |
|------------------------|---------------------------------------------------|--------------------------------------------------------------|
| **Layer**              | Runtime-Tool (Python-Library, installierbar)      | Strukturspezifikation (Manifest-Standard, kein Code)         |
| **Was wird gespeichert** | Verbatim-Text von Gesprächen                   | Entscheidungen, Architektur, Planungskontext                  |
| **Retrieval**          | Semantische Suche über Vektoren (ChromaDB)        | Kein automatisches Retrieval — Agent liest manuell/strukturiert |
| **Memory-Typ**         | *Was wurde gesagt* (episodisch/faktisch)          | *Was wurde entschieden und gebaut* (strukturell/strategisch) |
| **Zielgruppe**         | Entwickler die Agents mit Gedächtnis ausstatten   | Jeden der ein Repo mit einem Agent betreibt                  |
| **Komplexität**        | Installationsaufwand, Python, ChromaDB, Benchmarks | Ein JSON + Markdown — fertig                                 |
| **Phase**              | v3.3.0 — produktionsreif, benchmarked            | Spezifikation/Standard — frühe Phase                         |
| **Fokus**              | *Finden*, was der Agent früher erfahren hat       | *Orientieren*, was der Agent jetzt tun soll                  |

---

### Komplementarität — das eigentliche Potenzial

> MemPalace und AAMS lösen **verschiedene Teile desselben Problems**.

```
AAMS:       Struktur   → Was der Agent TUN soll (Kontext, Regeln, Entscheidungen)
MemPalace:  Retrieval  → Was der Agent WISSEN soll (Gesprächshistorie, Fakten)
```

**Konkrete Synergie:**
- AAMS's `WORKING/MEMORY/` könnte von MemPalace als semantisch durchsuchbares Backend betrieben werden
- AAMS-Workpapers + Whitepapers könnten als "mining source" in MemPalace indexiert werden
- MemPalace's Agent-Diaries könnten das AAMS DIARY/ Format implementieren
- AAMS gibt die Governance-Schicht, MemPalace gibt die Retrieval-Schicht

**Formuliert für den Kontakt:**
> *"AAMS ist das Briefing des Agents — MemPalace ist sein Langzeitgedächtnis. Beides braucht man, um einen autonomen Agent wirklich persistent zu machen."*

---

### Einschätzung: Relevanz für AAMS-Ökosystem

**Sehr hoch.** Begründung:
1. Igor ist technisch tief im Thema — kein Noob-Kontakt
2. MemPalace hat bereits ein Ökosystem (Plugins, Hooks, MCP) wo AAMS als Governance-Layer integrierbar wäre
3. Das Projekt hat eine riesige Community — ein Erwähnungs-Effekt wäre wertvoll
4. Igor hat selbst `AGENTS.md` im Repo — er denkt bereits in der gleichen Sprache
5. Mögliche Kooperation: AAMS-Plugin für MemPalace / MemPalace als MEMORY/-Backend für AAMS

---

## 4. Geplante Nachrichten

### Nachricht an Igor (nach LinkedIn-Bestätigung)

**Entwurf — kurz, direkt, respektvoll:**

---

> Hi Igor,
>
> danke für die Verbindung. Ich habe MemPalace analysiert — beeindruckendes Projekt, besonders die Kombination aus verbatim storage und strukturiertem Index (Wings/Rooms). 46k Stars in kurzer Zeit sagt alles.
>
> Ich arbeite an AAMS (Autonomous Agent Manifest Specification) — einem anderen Layer des gleichen Problems: nicht Retrieval, sondern Governance. Ein standardisiertes Workspace-Manifest das jedem Agent sofort Kontext, Regeln und Session-Persistenz gibt — ohne Code, nur Markdown + JSON.
>
> Ich sehe eine echte Komplementarität: AAMS bringt dem Agent das Briefing, MemPalace bringt das Langzeitgedächtnis. Wäre neugierig auf deine Sicht.
>
> GitHub: https://github.com/DEVmatrose/AAMS
>
> Grüße aus Berlin

---

**Status:** Entwurf — noch nicht gesendet (warte auf LinkedIn-Bestätigung)

---

## 5. Nächste Schritte

- [ ] LinkedIn-Bestätigung von Igor abwarten
- [ ] Nachricht senden (Entwurf oben)
- [ ] Nach Antwort: Kontext in diesem Workpaper dokumentieren
- [ ] Prüfen: AAMS-Eintrag in MemPalace-Discussions / README-Showcase vorschlagen?
- [ ] Prüfen: MemPalace als Backend-Empfehlung für AAMS WORKING/MEMORY/ dokumentieren?

---

## 6. Weitere Kontakte (Platzhalter)

| # | Name | Plattform | Projekt/Kontext | Status |
|---|------|-----------|-----------------|--------|
| 1 | Igor Lins e Silva | LinkedIn | MemPalace — AI Memory | ⏳ Anfrage offen |
| … | — | — | — | — |
