# Workpaper: RFL — Reflection Protocol Step

- **Datum:** 2026-04-09
- **Agent:** GitHub Copilot (Claude Opus 4.6)
- **Status:** CLOSED — Umgesetzt in v1.2.0
- **Vorgänger:** `2026-04-09-science-knowledge-validation-layer.md` (verworfen — zu komplex für Spec)

---

## Session Goal

Einen **Reflection-Schritt (RFL)** als neuen Protokollschritt im Agent Contract (`READ-AGENT.md`) einführen. Kein neuer Layer. Kein neuer Ordner. Eine Zeile im Contract — die das häufigste Failure-Pattern agentischer Sessions löst.

---

## 1. Das Problem

> Agent entscheidet in Session 47 das Gegenteil von Session 12 — und merkt es nicht.

**Warum das passiert:**

- LTM-Query beim Session-Start holt Kontext zum *Thema* — nicht zu *vergangenen Entscheidungen*
- Diary dokumentiert *warum* entschieden wurde — aber niemand liest es systematisch
- Workpapers haben Decisions-Sektionen — aber kein Agent vergleicht sie mit dem aktuellen Vorhaben
- Ergebnis: **Schleichende Inkonsistenz** über viele Sessions

**Warum die bestehenden 4 Layer das nicht lösen:**

| Layer | Speichert | Prüft aktiv? |
|-------|----------|-------------|
| Workpaper | Aktuelle Entscheidungen | ❌ Nein |
| Whitepaper | Architekturwahrheit | ❌ Nein (wird gelesen, nicht verglichen) |
| Diary | Entscheidungsmotive | ❌ Nein (chronologisch, nicht analytisch) |
| Memory/LTM | Gelerntes | ❌ Nein (holt Kontext, prüft nicht Konsistenz) |

**Alle vier Layer sind Speicher. Keiner ist Prüfung.**

RFL schließt diese Lücke — als Protokollschritt, nicht als Layer.

---

## 2. Fundament: Strukturierte Dateinamen (Naming Schema)

RFL funktioniert besser, wenn ein Agent thematisch relevante Workpapers **finden** kann. Strukturierte Dateinamen sind der Idealfall — aber wir können nicht garantieren, dass jeder Agent sie einhält.

### 2.1 Realitätscheck

**Das Problem:** Eine Spec kann empfehlen. Nur ein Framework kann erzwingen.

| Szenario | Naming Schema eingehalten? | RFL-Qualität |
|----------|--------------------------|-------------|
| Eigenes Framework zwingt | ✅ Ja, garantiert | Perfekt — Pattern-Matching |
| Agent liest READ-AGENT.md sorgfältig | 🟡 Meistens | Gut — gelegentlich Fallback nötig |
| Agent ignoriert Schema | ❌ Nein | Nur via LTM oder chronologischem Scan |
| Bestehende Alt-Workpapers | ❌ Nein | Kein Pattern-Match möglich |

> **Müll-Ergebnisse zu produzieren macht keinen Sinn.** Jeder Mensch kann im Kopf schon selber denken ob etwas widersprüchlich ist. RFL hat nur dann Wert, wenn es **strukturierten Mehrwert** liefert — nicht wenn es ein leeres Ritual wird.

### 2.2 Lösung: Hybrides RFL (3-Stufen-Fallback)

RFL nutzt drei Strategien in absteigender Präzision:

```
RFL Strategy Cascade:
│
├─ Stufe 1: Pattern-Match auf TOPIC-Tag
│  → Scan closed/ für *-{TOPIC}-*
│  → Treffer? → Decisions lesen → FERTIG
│
├─ Stufe 2: LTM-Query-Ergebnisse aus Schritt 3
│  → LTM liefert thematisch relevante Einträge
│  → Referenzierte Workpapers → Decisions lesen → FERTIG
│
└─ Stufe 3: Letztes closed Workpaper (chronologisch)
   → Minimaler Kontext, besser als nichts
   → Nur wenn Stufe 1 + 2 leer
```

**Warum das funktioniert:**

- Stufe 1 ist der Idealfall. Wird besser über Zeit, je mehr Workpapers mit Schema existieren.
- Stufe 2 fängt Alt-Workpapers und Schema-Verletzungen auf. LTM kennt auch `2026-02-22-gas-town-research-wp002.md`.
- Stufe 3 ist der Notnagel. Ein Blick ins letzte Workpaper ist besser als keiner.

**Kein Szenario produziert Müll.** In jedem Fall liefert RFL nur Ergebnisse wenn es welche gibt — und schweigt wenn nicht.

### 2.3 Workpaper Naming Schema (empfohlen, angestrebt)

```
{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md
```

| Segment | Format | Beispiel | Funktion |
|---------|--------|---------|---------|
| `DATE` | `YYYY-MM-DD` | `2026-04-09` | Chronologische Ordnung |
| `TOPIC` | 3-4 Buchstaben, UPPERCASE | `ARCH` | Themenbereich — primärer Ordnungsschlüssel |
| `SUBTOPIC` | 3-4 Buchstaben, UPPERCASE | `RFL` | Teilthema — sekundärer Ordnungsschlüssel |
| `description` | kebab-case, lowercase | `reflection-protocol-step` | Menschenlesbare Kurzbeschreibung |

**Beispiele:**

```
2026-04-09-ARCH-RFL-reflection-protocol-step.md
2026-03-27-ARCH-LHR-long-horizon-reasoning-analyse.md
2026-03-28-MKT-VID-video-marketing-kochbuch.md
2026-02-22-LTM-CHR-chroma-implementation.md
2026-02-22-SEC-POL-secret-exclusion-policy.md
```

### 2.4 Topic Registry

| TOPIC | Bedeutung | Beispiel-Subtopics |
|-------|-----------|-------------------|
| `ARCH` | Architektur & Systemdesign | `LYR`, `RFL`, `LHR`, `DOC` |
| `SPEC` | Spezifikationsarbeit | `SCH`, `VAL`, `GAP`, `VER` |
| `LTM` | Long-Term Memory | `CHR`, `MDX`, `ING`, `SYN` |
| `SEC` | Security & Governance | `POL`, `AUD`, `PRM` |
| `BOOT` | Bootstrap & Onboarding | `CTR`, `ENT`, `IDM` |
| `FLD` | Feldtests & Reports | `RPT`, `TST`, `EXT` |
| `RES` | Research & Related Work | `GAS`, `MEM`, `PAP` |
| `MKT` | Marketing & Kommunikation | `VID`, `SOC`, `WEB` |
| `ISS` | Issue-Bearbeitung | `FIX`, `REV`, `PLN` |
| `GOV` | Governance & Process | `WFL`, `STD`, `RUL` |
| `EDU` | Education & Kurse | `KRS`, `TUT`, `MAT` |

> Erweiterbar. Maximal 4 Buchstaben, UPPERCASE, eindeutig.

### 2.5 Whitepaper Naming Schema

```
WP-{NNN}-{TOPIC}-{description}.md
```

Beispiel: `WP-001-ARCH-aams-overview.md`

### 2.6 Compliance-Stufen

| Kontext | Schema-Enforcement | RFL-Strategie |
|---------|-------------------|--------------|
| **AAMS Spec (READ-AGENT.md)** | Empfohlen, nicht erzwingbar | Hybrid (3-Stufen-Fallback) |
| **Eigenes Framework** | Erzwungen (Validation bei Dateierstellung) | Stufe 1 reicht — garantierte Qualität |
| **Fremdes Repo, frisch gebootstrapped** | Nur für neue Dateien | Stufe 2+3 für Alt-Dateien, Stufe 1 für neue |

> **Die Spec gibt das Ziel vor. Das Framework erzwingt es. Die Realität ist dazwischen.** RFL funktioniert auf jeder Stufe — nur mit unterschiedlicher Präzision.

---

## 3. Der RFL-Mechanismus

### Definition

> **RFL (Reflection)** ist eine systematische Konsistenzprüfung beim Session-Start mit 3-Stufen-Fallback: Pattern-Match auf TOPIC-Tags → LTM-Query-Ergebnisse → letztes Workpaper chronologisch.

### Einordnung

```
Session-Start:
1. READ-AGENT.md lesen                      ← existiert
2. Letztes Workpaper prüfen                 ← existiert
3. LTM query für Session-Thema              ← existiert
4. ★ RFL: Consistency Check ★               ← NEU
   Stufe 1: Pattern-Match *-{TOPIC}-*
   Stufe 2: LTM-Ergebnisse aus Schritt 3
   Stufe 3: Letztes closed Workpaper
5. Workpaper öffnen/erstellen               ← existiert
```

### Was RFL konkret tut

```
RFL-Schritt:
1. Bestimme TOPIC aus Session-Ziel
2. Stufe 1: Scan closed/ für *-{TOPIC}-* → Treffer? → Decisions lesen
3. Stufe 2: Kein Treffer? → LTM-Ergebnisse aus Schritt 3 → referenzierte Workpapers → Decisions lesen
4. Stufe 3: Immer noch nichts? → Letztes closed Workpaper → Decisions lesen
5. Vergleiche gefundene Decisions mit aktuellem Session-Ziel
6. Bei Widerspruch → Flag im neuen Workpaper:
   
   ## ⚠ RFL Consistency Flag
   - Conflict: Session {date} entschied {X}, aktuelles Ziel impliziert {Y}
   - Source: {workpaper-filename}
   - Found via: Stufe {1|2|3}
   - Resolution: [bestätigt | revidiert | bewusst geändert + Begründung]
```

### Warum Hybrid statt einer einzigen Strategie?

| Strategie | Pro | Contra |
|-----------|-----|--------|
| Nur Naming Pattern | Präzise, zero dependency | Nicht garantiert — Spec kann nicht erzwingen |
| Nur LTM | Semantisch stark | Abhängig von LTM-Qualität, funktioniert nicht in frischen Repos |
| Nur chronologisch | Einfach | Themen-fremdes Rauschen |
| **Hybrid (3-Stufen)** | **Funktioniert immer, Qualität steigt mit Compliance** | **Etwas komplexer in der Beschreibung** |

> **Die Spec gibt das Ziel vor (Naming Schema). Die Realität ist dazwischen. RFL funktioniert auf jeder Stufe** — nur mit unterschiedlicher Präzision. Kein Szenario produziert Müll.

### Was RFL NICHT tut

- ❌ Keine externe Recherche (das wäre SCIENCE → Framework-Ebene)
- ❌ Kein vollständiger Audit aller 100+ Workpapers
- ❌ Keine automatische Korrektur — nur Flagging
- ❌ Kein neuer Ordner, kein neues Schema-Ordner

---

## 4. Konkreter Patch für READ-AGENT.md

### 4.1 Naming Schema (neue Sektion)

Neue Sektion in READ-AGENT.md nach "Documentation Model":

```markdown
### Naming Schema (mandatory)

**Workpapers:**

`{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md`

- `DATE` — `YYYY-MM-DD`
- `TOPIC` — 3-4 letter tag, UPPERCASE (e.g. `ARCH`, `LTM`, `SPEC`)
- `SUBTOPIC` — 3-4 letter tag, UPPERCASE (e.g. `RFL`, `CHR`, `GAP`)
- `description` — kebab-case, lowercase

Example: `2026-04-09-ARCH-RFL-reflection-protocol-step.md`

The TOPIC tag is the primary key for cross-session consistency checks (RFL). Agents MUST use consistent TOPIC tags. See the Topic Registry in this section.

**Whitepapers:**

`WP-{NNN}-{TOPIC}-{description}.md`

Example: `WP-001-ARCH-aams-overview.md`

The TOPIC tag links whitepapers to related workpapers.
```

### 4.2 Session-Start Patch

Aktuell:

```markdown
### On every session start
1. Read this file
2. Check last workpaper in `WORKING/WORKPAPER/` — what was the last state?
3. Query `WORKING/MEMORY/` for the session topic
4. Open or create workpaper for this session
```

Neu:

```markdown
### On every session start
1. Read this file
2. Check last workpaper in `WORKING/WORKPAPER/` — what was the last state?
3. Query `WORKING/MEMORY/` for the session topic
4. **RFL — Reflection (3-stage cascade):**
   - **Stage 1:** Determine the TOPIC tag for this session. Scan `WORKING/WORKPAPER/closed/` for files matching `*-{TOPIC}-*`. If found, read their Decisions sections.
   - **Stage 2:** If no matches in Stage 1, use the LTM results from step 3 to identify prior workpapers with decisions on the current topic.
   - **Stage 3:** If still nothing, read the Decisions section of the most recent closed workpaper.
   - If any prior decision conflicts with the current session goal, flag it in the new workpaper under `## ⚠ RFL Consistency Flag` with: the conflicting decision, its source workpaper, the stage it was found in, and a resolution (confirmed | revised | intentionally changed + rationale).
   - If no conflicts found: no flag needed. Zero overhead.
5. Open or create workpaper for this session (recommended naming: `{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md`)
```

Das ist **Pattern-Matching auf Dateinamen** — kein LTM nötig, kein externes Tool, funktioniert ab Tag eins.

---

## 5. Workpaper-Erweiterung

Wenn RFL einen Widerspruch findet, erscheint im neuen Workpaper:

```markdown
## ⚠ RFL Consistency Flag

| Prior Decision | Date | Conflict | Resolution |
|---------------|------|----------|-----------|
| "LTM soll rein Markdown bleiben" | 2026-03-15 | Aktuelles Ziel: ChromaDB als Default einführen | Bewusst revidiert — Markdown bleibt Track A, ChromaDB wird Track B (dual-track) |
```

**Wenn kein Widerspruch:** Keine Sektion nötig. Kein Overhead bei konsistenten Sessions.

---

## 6. Warum das wegweisend ist

### 6.1 Kein anderer Standard hat das

- `.cursorrules` — keine Reflection
- `CLAUDE.md` — keine Reflection
- MemGPT — managed Memory, keine Konsistenzprüfung
- Gas Town — parallele Agenten, keine Cross-Session-Konsistenz
- LangChain Memory — Runtime-Buffer, kein Decision-Audit

**AAMS wäre der erste offene Standard der explizite Session-Konsistenzprüfung definiert.**

### 6.2 Es ist das Minimum das funktioniert

- Kein neuer Layer (Spec bleibt 4 Schichten)
- Kein neuer Ordner (nutzt existierende closed/ Workpapers)
- Kein neues Tool (Agent liest Markdown — kann er schon)
- Kein externer Zugang nötig (local-first bleibt intact)
- Kein Breaking Change (bestehende Agenten ignorieren den Schritt einfach)

### 6.3 Es macht Entscheidungen explizit reversibel

Ohne RFL: Agent überschreibt stillschweigend alte Entscheidungen.
Mit RFL: Agent muss begründen warum er abweicht — oder bestätigen dass er konsistent ist.

> Das ist der Unterschied zwischen *"wir haben das geändert"* und *"wir haben das bewusst geändert, weil..."*

---

## 7. Abgrenzung: SCIENCE → Framework

Die SCIENCE-Idee (Knowledge Validation Layer — externe Recherche, Quellengewichtung, Delta_3-Analyse) ist **nicht verworfen**. Sie wandert in das Agent-Loop-Framework, das AAMS als Körper nutzt.

```
AAMS (Spec)          = Körper (Struktur, Speicher, Protokoll)
Agent-Loop-Framework  = Geist (Reasoning, Recherche, Validierung)
```

SCIENCE passt in den Geist — nicht in den Körper. Die Spec definiert *wo* Dinge liegen. Das Framework definiert *was* der Agent denkt.

RFL ist die Brücke: Es ist ein **Denkschritt** der nur **bestehende Struktur** nutzt.

---

## 8. Decisions

| # | Entscheidung | Begründung |
|---|-------------|-----------|
| D1 | **Naming Schema ist empfohlen** — `{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md` für Workpapers, `WP-{NNN}-{TOPIC}-{description}.md` für Whitepapers | Ziel für Compliance, aber Spec kann nicht erzwingen. Framework kann. |
| D2 | **Topic Registry** — vordefinierte TOPIC-Tags (ARCH, SPEC, LTM, SEC, etc.) | Einheitliche Tags ermöglichen Pattern-Matching. Erweiterbar bei Bedarf. |
| D3 | RFL wird als Schritt 4 im `on_session_start` Contract eingefügt | Natürliche Position: nach Kontext-Aufbau, vor Workpaper-Erstellung |
| D4 | **RFL nutzt 3-Stufen-Fallback** (Pattern → LTM → chronologisch) | Kein Szenario produziert Müll. Qualität steigt mit Schema-Compliance. |
| D5 | Output: `## ⚠ RFL Consistency Flag` Sektion im Workpaper | Kein neuer Ordner, nutzt existierendes Format |
| D6 | Kein Flag bei Konsistenz — Sektion entfällt | Zero Overhead bei konsistenten Sessions |
| D7 | SCIENCE als Konzept → Agent-Loop-Framework, nicht AAMS Spec | Spec = Körper, Framework = Geist |
| D8 | Bestehende Workpapers/Whitepapers werden nicht rückwirkend umbenannt | Pragmatik. Schema gilt ab jetzt. Stufe 2+3 fängt Altbestand auf. |

---

## 9. Next Steps

- [ ] READ-AGENT.md patchen: Naming Schema Sektion einfügen (mit Topic Registry)
- [ ] READ-AGENT.md patchen: RFL-Schritt in `on_session_start` einfügen
- [ ] .agent.json prüfen: Naming Schema referenzieren
- [ ] WP-001 aktualisieren: Naming Schema als Core-Element erwähnen
- [ ] Bestehende Whitepapers: TOPIC-Tag ergänzen (WP-001-ARCH, WP-002-RES, etc.) — oder pragmatisch: erst neue WPs mit Schema
- [ ] Diary-Eintrag: SCIENCE verworfen → RFL + Naming Schema
- [ ] LTM-Ingest dieses Workpapers

---

## File Protocol

| # | Aktion | Datei | Beschreibung |
|---|--------|-------|-------------|
| F1 | CLOSED | `WORKING/WORKPAPER/closed/2026-04-09-science-knowledge-validation-layer.md` | SCIENCE-Workpaper als verworfen geschlossen |
| F2 | CREATED | `WORKING/WORKPAPER/2026-04-09-rfl-reflection-protocol-step.md` | Dieses Workpaper |

---

> **Bereit zum Patchen.** Sag Bescheid und ich setze den RFL-Schritt in READ-AGENT.md um.
