# WP — MemPalace Analyse: Relevanz für AAMS

| Feld    | Wert                                                          |
|---------|---------------------------------------------------------------|
| Datum   | 2026-04-15                                                    |
| Status  | IN ARBEIT                                                     |
| Autor   | Agent (Copilot / Claude Sonnet 4.6)                           |
| Scope   | Technische Analyse, Abgrenzung, mögliche Synergien mit AAMS   |
| Bezug   | [2026-04-15-social-outreach.md](./2026-04-15-social-outreach.md) — Kontakt Igor Lins e Silva |

---

## 1. Ausgangsfrage

MemPalace hat inhaltliche Überschneidungen mit AAMS.  
Dieses Workpaper klärt:

1. Was macht MemPalace konkret?
2. Was überschneidet sich mit AAMS — was nicht?
3. Was ist aus AAMS-Sicht relevanter Lernstoff?
4. Was ist für AAMS nicht relevant und warum?
5. Was sind konkrete nächste Handlungsoptionen?

---

## 2. Was ist MemPalace? (Kurzfassung)

**Kategorie:** Local-first, Open-Source AI-Memory-System (Python, MIT)  
**Kern-Idee:** Gesprächshistorien werden *verbatim* (ohne LLM-Zusammenfassung) gespeichert und über semantische Suche abrufbar gemacht.

**Architektur-Metapher:** Memory Palace (Methode der Loci)
- **Wings** = Personen oder Projekte
- **Rooms** = Themen
- **Drawers** = originale Text-Chunks

**Technisch:**
- Storage-Backend: ChromaDB (pluggable, 7-Methoden-ABC)
- Retrieval: Sentence-Transformers lokal (~300 MB), kein API-Key nötig
- Knowledge Graph: SQLite, temporal mit Validity-Windows
- MCP-Server: 29 Tools (Reads, Writes, KG-Operationen, Agent-Diaries)
- Auto-Save-Hooks für Claude Code (periodic + vor Context Compression)
- Benchmarks: 96,6 % Recall@5 auf LongMemEval *ohne LLM*

**Zahlen (Stand 2026-04-15):** 46.300 Stars, 6k Forks, 47 Contributors, aktiv

---

## 3. Vergleich: MemPalace ↔ AAMS

### Gemeinsamkeiten (oberflächlich)

| Dimension              | MemPalace                              | AAMS                                        |
|------------------------|----------------------------------------|---------------------------------------------|
| Ziel                   | Agent-Persistenz über Sessions         | Agent-Persistenz über Sessions              |
| Agent-Struktur         | Wings + Diaries pro Agent              | WORKING/DIARY/ + MEMORY/ pro Projekt        |
| Multi-Tool-Kompatibilität | MCP, Claude Code, Codex, Gemini    | `.agent.json` läuft mit jedem Agent         |
| Strukturiertes Wissen  | Wings/Rooms/Drawers                    | WHITEPAPER/WORKPAPER/MEMORY/                |
| AGENTS.md              | Vorhanden (Symlink → CLAUDE.md)        | Zentrales Steuerungselement                 |

### Wesentliche Unterschiede — das ist entscheidend

| Dimension              | MemPalace                                          | AAMS                                                   |
|------------------------|----------------------------------------------------|--------------------------------------------------------|
| **Was es ist**         | Runtime-Tool (Python-Library, installieren + betreiben) | Strukturspezifikation (kein Code, kein Betrieb)    |
| **Was gespeichert wird** | Verbatim-Text aus Gesprächen (episodisch)        | Entscheidungen, Architektur, Planungskontext (strategisch) |
| **Retrieval**          | Semantische Suche (Vektoren + Metadaten-Filter)    | Kein Retrieval — strukturiertes Lesen durch Agent      |
| **Abhängigkeiten**     | Python, ChromaDB, Sentence-Transformers            | Kein Code, kein Setup — nur Dateien                    |
| **Wer es nutzt**       | Entwickler die Agents mit Gedächtnis ausstatten   | Jeder der ein Repo mit einem Agent betreibt            |
| **Komplexitätsstufe**  | Installation, Konfiguration, Benchmarking          | Ein JSON + Markdown                                    |
| **Was es löst**        | *Was hat der Agent früher gehört/gesehen?*         | *Was soll der Agent jetzt tun und wie?*                |

> **Kernformel:**
> ```
> MemPalace  →  episodisches Gedächtnis  (Was wurde gesagt/erlebt?)
> AAMS       →  strukturelles Briefing   (Was soll getan werden, wie, warum?)
> ```

Sie sind **nicht konkurrierende Ansätze** — sie lösen verschiedene Schichten desselben Problems.

---

## 4. Was ist aus AAMS-Sicht relevant — was nicht?

### Relevant ✅

| Punkt | Warum relevant für AAMS |
|-------|--------------------------|
| **Agent-Diaries-Konzept** | MemPalace gibt jedem Agent einen eigenen Wing + Diary. AAMS hat `WORKING/DIARY/`. Die Strukturähnlichkeit zeigt, dass wir auf dem richtigen Weg sind. |
| **Pluggable Backend** | MemPalace's 7-Methoden-ABC ist ein gutes Beispiel für wie ein AAMS-MEMORY/-Backend spezifiziert werden könnte (zukünftige AAMS-Erweiterung). |
| **MCP als Brücke** | MemPalace's 29 MCP-Tools zeigen, wie AAMS-Inhalte maschinell zugänglich gemacht werden könnten — AAMS hat noch kein MCP-Profil. |
| **`AGENTS.md` als Standard** | Igor hat `AGENTS.md` im Repo — ein unabhängiger Beleg dafür, dass AAMS's Ansatz (eine Datei als Einstiegspunkt) bereits in erfolgreichen Projekten auftaucht. |
| **Verbatim-Prinzip** | AAMS's Workpapers/Whitepapers archivieren auch *alles* — kein Destillat, keine Zusammenfassung als Ersatz für Original. Bestätigt unsere Philosophie. |

### Nicht relevant / nicht übernehmen ❌

| Punkt | Warum für AAMS nicht relevant |
|-------|-------------------------------|
| **ChromaDB / Embeddings** | AAMS ist absichtlich technologiefrei. Kein Retrieval-System, kein Installationsaufwand. Das ist Stärke, nicht Schwäche. |
| **Benchmark-Kultur** | AAMS ist kein Retrieval-System — Recall%-Metriken sind die falsche Erfolgsmetrik. Unsere Metrik: "Hat der Agent das Richtige getan?" |
| **Python-Library-Ansatz** | AAMS funktioniert mit jedem Setup, weil es nur Dateien sind. Eine Python-Abhängigkeit würde den Kern-USP zerstören. |
| **AAAK-Kompression** | Lossy-Kompression ist das Gegenteil von AAMS-Philosophie. Verbatim = gut; aber AAMS komprimiert anders (strukturiert statt lossy). |

---

## 5. Mögliche Synergien — was könnte Sinn machen?

### Kurzfristig (jetzt sinnvoll)

- [ ] **AAMS als Context-Provider für MemPalace dokumentieren:**  
  `.agent.json` + `READ-AGENT.md` könnten als "pre-mining" Struktur in MemPalace empfohlen werden. Vor dem Gespräch gibt AAMS Kontext — MemPalace speichert danach was passiert ist.

- [ ] **MemPalace im AAMS SHOWCASE.md erwähnen:**  
  Nicht als AAMS-Nutzer, sondern als komplementäres Tool. Ehrliche Einordnung: "Wenn du episodisches Gedächtnis brauchst, schau hier."

### Mittelfristig (nach erstem Austausch mit Igor)

- [ ] **AAMS-Workpaper als MemPalace-Wing experimentell indexieren:**  
  Test: Wie gut retrievet MemPalace AAMS-Workpapers? Zeigt ob die Tools wirklich komplementär sind.

- [ ] **Cross-Link in beiden READMEs:**  
  AAMS → "Für episodisches Gedächtnis: MemPalace". MemPalace → "Für Workspace-Governance: AAMS". Mutual benefit.

### Langfristig (nur wenn Projekt wächst)

- [ ] **AAMS MEMORY/-Erweiterung:**  
  Formale Spezifikation eines MEMORY/-Backends in `.agent.json`. MemPalace wäre eine Referenzimplementierung.

### Folgeprojekt: AAMS-Plugin für MemPalace (abhängig von Kontakt)

> **Voraussetzung:** Erfolgreicher Austausch mit Igor — erst dann PR einreichen.  
> Einen PR ohne persönlichen Kontakt bei einem 46k-Star-Projekt einzureichen wäre kontraproduktiv.

**Idee:** Mining-Plugin das die AAMS-Workspace-Struktur versteht und automatisch in den Palace indexiert.

```
mempalace mine ./WORKING --mode aams
```

**Mapping AAMS → MemPalace:**

| AAMS Ordner              | MemPalace Wing    | MemPalace Room       |
|--------------------------|-------------------|----------------------|
| `WORKING/WHITEPAPER/`    | Architecture      | je Whitepaper        |
| `WORKING/WORKPAPER/`     | Sessions          | je Workpaper-Datei   |
| `WORKING/MEMORY/`        | Memory            | je Memory-Eintrag    |
| `WORKING/DIARY/`         | Diary             | je Monatsdatei       |

**PR-Wert für beide Seiten:**
- MemPalace: strukturiertes Ingest-Format für Governance/Planungsdaten
- AAMS: native Retrieval-Unterstützung, Sichtbarkeit in 46k-Star-Ökosystem

**Status:** Konzept — wartet auf Kontaktbestätigung (→ [Social Outreach WP](./2026-04-15-social-outreach.md))

---

## 6. Was MemPalace über AAMS lehrt

> **Beobachtung:** MemPalace hat in kurzer Zeit massive Adoption erreicht — mit einem Ansatz der bewusst einfach, transparent und lokal ist.

Das bestätigt für AAMS:
1. **Einfachheit gewinnt** — MemPalace macht keine Magie, nur saubere Architektur. AAMS macht das gleiche auf Governance-Ebene.
2. **Lokale Kontrolle ist ein Wert** — kein Cloud-Zwang, keine Vendor-Lock-in. AAMS: nur Git.
3. **Verbatim > Destillat** — alles behalten, strukturiert findbar machen. AAMS archiviert alle Workpapers, nichts wird weggeworfen.
4. **AGENTS.md als Standard setzt sich durch** — wir sehen es in MemPalace, MantisClaw und anderen. AAMS ist mit dieser Idee nicht allein.

---

## 7. Offene Fragen

- Wie ist Igor in das Projekt eingestiegen? Er ist CTO bei EOS Rio (Blockchain/EOS) — MemPalace ist ein Pivot oder Nebenprojekt?
- Wer ist `milla-jovovich` / `bensig` — die ursprünglichen Autoren? Igor wurde erst später Top-Contributor?
- Hat MemPalace eine Roadmap für Governance/Context-Spezifikation jenseits von CLAUDE.md?
- Gibt es Discord/Discussions wo AAMS erwähnt werden könnte?

---

## 8. Entscheidungen dieses Workpapers

| # | Entscheidung | Begründung |
|---|-------------|------------|
| E1 | AAMS bleibt technologiefrei (kein Retrieval-System) | MemPalace zeigt: Retrieval ist ein eigener Layer. AAMS ist der Governance-Layer davor. |
| E2 | Keine Feature-Erweiterung in Richtung Vector-DB | Würde AAMS-Kern-USP zerstören. Komplementarität > Integration. |
| E3 | MemPalace nach Kontaktbestätigung als Showcase-Link erwägen | Ehrliche Einordnung als komplementäres Tool bringt mehr als Schweigen. |

---

## 9. Nächste Schritte

- [ ] Auf LinkedIn-Bestätigung von Igor warten (→ [Social Outreach WP](./2026-04-15-social-outreach.md))
- [ ] Nach Bestätigung: Nachricht senden, Komplementarität kommunizieren
- [ ] Entscheiden: MemPalace in SHOWCASE.md oder separater "Tools"-Sektion erwähnen?
- [ ] Intern: AAMS MEMORY/-Konzept schärfen (was ist Memory in AAMS, was ist es nicht?)
