# WP-2026-09-22-RES-JEV-open-jev-decision-layer

**Status:** observe
**Datum:** 2026-09-22 (v2 — 09:30-Dump übernommen)
**TOPIC/SUBTOPIC:** RES/JEV
**Session-Ziel:** Recherche: „Jev"-artige Decision Layer — Einordnung in AAMS-Philosophie (lokal, souverän, Open Source). **Kernfrage (User, Spec-First):** Macht das Pattern in der **AAMS-Spezifikation** Sinn? (MANTIS-Proxy = selbstgebaute Brücke, `opencode.json` — Infrastruktur, kein Entscheidungsziel.)

**Herkunft:** Chat-Antwort (ChatGPT, 2026-09-22) + User-Positionierung.
- v2 (vollständig, 849 Zeilen): `closed/raw-dump-2026-09-22-open-jev-layer-chat-dump.md`
- v1 (ältere Fassung): `closed/raw-dump-2026-09-22-open-jev-layer-chat-dump-v1.md`

**⚠ Evidenz-Hinweis:** Alle Repo-/Modell-/Preis-Claims stammen aus einer Chat-Antwort und sind **nicht lokal verifiziert**. Vor jeder Entscheidung: Repos klonen, prüfen, bauen.

**Bezug:**
- Philosophie: AAMS = lokale Projektwahrheit in `WORKING/` (WH-001)
- Manifest-Prinzip (D9): AAMS beschreibt, schreibt kein Verhalten vor — externe Module sind Local Adaptation
- Verwandt: WP-2026-09-22-SPEC-NOTE (Hermes-Nous als externe Runtime — gleiche Abgrenzungslogik)
- **Infrastruktur-Kontext:** MANTIS-Proxy — selbstgebaute Brücken-Gateway zwischen OpenCode/VS Code und den Modellen (LM Studio). Siehe `opencode.json` (Provider `mantis`, „MANTIS LLM Gateway", OpenAI-kompatibel `/v1`). **Muss immer laufen**, wenn in VS Code mit OpenCode gearbeitet wird. Infrastruktur — **kein Entscheidungsziel**.

---

## 1. Ausgangslage (User-Positionierung, bindend)

- **Jev (original, TypeSafe AI):** geschlossenes, gehostetes Modell. Weights nicht veröffentlicht, Self-Hosting nicht möglich, nur über API.
- **User-Entscheidung (aus Roh-Dump v2):** „JEV ist kein offenes Modell, nur über API möglich. Also für uns und AAMS kommt das nicht in Frage." → **Cloud-/API-Variante ist keine Option.**
- **Offene Kernfrage (User, 2026-09-22):** Machen das Decision-Layer-Pattern (JEV) und das Session-State-Guard-Pattern (Hermes-Local) in der **AAMS-Spezifikation** Sinn? — **Spec-First-Prinzip: „Die Spezifikation ist das Wichtigste. Kein Abweichen von diesem Pfad."**
- **MANTIS-Proxy = Kontext, kein Ziel:** Selbstgebaute Brücke zwischen LM Studio / OpenCode / VS Code, muss immer laufen (siehe `opencode.json`). Dient höchstens später als Umsetzungsort — der Entscheidungspfad weicht von der Spezifikation **nicht** ab.
- **Folgerung:** Lokale Umsetzung = Open-Jev-Reimplementierung **oder** das Pattern mit dem bestehenden Qwen3.8-27B im Proxy umsetzen (statt zweitem Modell).

---

## 2. Optionsraum lokal (ALLE Claims unverifiziert — prüfen vor Einsatz)

| Projekt | Claim (Quelle: Chat-Antwort) | Status laut Claim |
|---|---|---|
| `kyegomez/open-jev` | Open-Source-Rekonstruktion der Jev-Ideen aus first principles, PyTorch | offen |
| `Zefan-Cai/Open-Jev` | Lokale Jev-artige Decision-Architektur; Qwen3.5-2B + Qwen3.5-9B mit Adaptern/Checkpoints; Qwen3.8-27B in Training/Evaluation | offen |
| `sabeel111/OpenSourceJev` | „LLM model into a Jev-like System" | offen |
| LLM2Jev, Rizzo Flow | Weitere lokale Ansätze (keine Details) | offen |
| `rajasekharponakala/jev-mcp` | Community-MCP für Jev-API (choice/score/noul) — nur relevant für API-Variante (für uns: nicht) | offen |

**Lokale Hardware:** RTX 5090 32 GB + `qwen/qwen3.8-27b` (MANTIS-Proxy) → 27B-Klasse locally ausführbar.

---

## 3. Rollenmodell (Kern des Dumps)

> **„AAMS speichert, Qwen denkt, Jev entscheidet, OpenCode handelt."**
> Erweiterung: „AAMS remembers → Qwen reasons → Jev decides → OpenCode acts → AAMS records."

| Rolle | Wer | Aufgabe |
|---|---|---|
| **State / Memory / Truth** | AAMS (`WORKING/`) | Was ist wahr? Zustand, Offenes, Geschichte |
| **Reasoning / Generation** | Qwen3.8-27B (LM Studio) | Code, Texte, Planung |
| **Decision** | Decision Layer (Jev-Pattern) | Typisierte Entscheidungen + Scores + Konfidenz aus State |
| **Execution** | OpenCode | Tool-Aufrufe, Tests, Git |
| **History** | Git | Audit-Trail |

**Prinzip:** Generative LLMs treffen schlecht „Was-ist-nächste-Aktion"-Entscheidungen. Besser: State + definierte Frage + Optionsliste → typisierte Entscheidung + Wahrscheinlichkeiten + Confidence → **Orchestrator entscheidet**, LLM erzeugt.

---

## 4. Use-Cases (aus Dump v2, alle `descriptive_only`)

| # | Use-Case | Pattern |
|---|---|---|
| UC1 | **next_action-Routing:** „Was soll ich jetzt tun?" (inspect_code / run_tests / search_docs / continue / update_aams / ask_user / finish) | STATE (AAMS: Aufgabe, WP, Diff, Tests, TODOs) + QUESTION + OPTIONS → `{choice, probabilities[], confidence}` |
| UC2 | **AAMS-State → Decision:** AAMS = „Was ist wahr?", Decision-Layer = „Was soll daraus passieren?" — zwei getrennte Dinge | State-Abfrage vor jeder Aktion |
| UC3 | **Qwen-Ausgaben kontrollieren:** Git-Diff gegen definierte Kriterien (Architecture-Verstoß? Komplexität? Vollständig? Human-Review nötig?) — mehrere parallele Fragen in einem Call | State: Diff + AAMS-Regeln → 5+ Ja/Nein-Entscheidungen mit Scores |
| UC4 | **AAMS als Regelbasis:** projektbezogene Rules als Jev-Fragen ableiten — Vorschlag: `WORKING/JEV/` mit `routing.md`, `architecture.md`, `quality.md`, `completion.md`, `security.md` | AAMS-Regeln → Decision-Fragen (robuster als „LLM prüfe dich selbst") |
| UC5 | **Multi-Agent-Gatekeeper:** Worker-Routing (coding / research / documentation / testing / security / human) | Entscheidung vor Worker-Dispatch |
| UC6 | **Decision Context Builder (Datenschutz):** nur minimaler State für die Entscheidung (reglevant + Diff + Aufgabe + letzte Aktion + Testergebnis), nie komplettes AAMS | Data-Minimization |
| UC7 | **Context-Governor (Context-Window-Wechsel):** vor Session-/Context-Wechsel: „Ist der AAMS-State ausreichend für Fortsetzung?" (YES / NO / RECONSTRUCT / ASK USER) + „Welche Infos sind kritisch für das nächste Fenster?" | Bindet an Workpaper-Lifecycle (analog Hermes-Local!) |
| UC8 | **Confidence-gesteuertes Routing:** ≥0.90 automatisch · 0.70–0.90 Re-Check · 0.50–0.70 zweiter Weg · <0.50 Mensch | Schwellwerte als Konfiguration (z. B. `thresholds/default.json`) |

**Minimal-Implementation-Skizze (aus Dump):** `aams-jev-gate` — `state/builder` + `decisions/{routing,quality,completion,safety}` + `thresholds/default.json` + `POST /decision` API; danach optional `jev_decide`-Tool im OpenCode-Workflow.

**Drei-Stufen-Plan (aus Dump, lokal anzupassen):**
1. Stufe 1: Decision-Abfragen nur für `next_action`, `task_complete`, `needs_human`, `needs_research`
2. Stufe 2: Agent-Router (Qwen / Search / Human)
3. Stufe 3: AAMS Decision Engine (State → Decision → Qwen/Tool/Human → AAMS)

---

## 5. AAMS-Einordnung (verbindlich)

- Decision Layer = **fremde Runtime / optionales Modul** — analog Hermes-Nous (WP-2026-09-22-SPEC-NOTE).
- AAMS-Kern erfordert **nichts** davon (Manifest-Prinzip D9, `descriptive_only`).
- **Spec-First (User, bindend):** Erst die Frage, ob das Pattern in der AAMS-Spezifikation Sinn macht (`descriptive_only`, D9). MANTIS-Proxy (selbstgebaute Brücke, `opencode.json`) = bestehende Infrastruktur, höchstens späterer Umsetzungsort — **kein Entscheidungsziel**. AAMS liefert das Pattern + die State-Seite (UC2/UC4/UC7).
- `WORKING/JEV/` (UC4) wäre ein **optionaler** Workspace-Pfad — kein Pflicht-Kern, erst nach positiver Decision.
- UC7 (Context-Governor) ist thematisch der engste AAMS-Anker: bindet an `on_session_start`/`on_session_end` (Workpaper-Lifecycle) — stärkste Kandidatin für ein `descriptive_only`-Pattern.
- Security: keine Roh-Transcripts in WHITEPAPER/DIARY/MEMORY; Data-Minimization (UC6); Pfade + Provenienz kuratieren.

---

## 6. offene Fragen (Blocker für observe-Status)

1. **Kernfrage (User, Spec-First):** Macht das Decision-Layer-Pattern (JEV) in der **AAMS-Spezifikation** Sinn (`descriptive_only`, D9)? — gleicher Entscheidungspfad wie Hermes-Local (WP-012). Umsetzung (höchstens in der MANTIS-Proxy-Infrastruktur) ist nachgelagert, nicht Gegenstand der Decision.
2. **Verifizierung:** Existieren die Repos? Laufen die 2B/9B-Adapter? Stand 27B-Training? (D3-Pflicht)
3. **Lokale Alternative:** Bestehenden Qwen3.8-27B direkt als Decision-Engine im Proxy nutzen (STATE→QUESTION→OPTIONS + Kalibrierung) statt zweitem Modell?
4. **Schnittstelle:** Stabiles I/O-Format `STATE/QUESTION/OPTIONS → {choice, probabilities, confidence}` definierbar, das an AAMS-Workpapers anbindbar ist?
5. **UC7-Priorität:** Context-Governor als erster AAMS-nativer Use-Case tauglich?

---

## 7. decisions

- **D1:** Decision Layer wird (falls weiterverfolgt) ausschließlich als **lokale, optionale Local Adaptation** behandelt — nie Pflicht-Kern.
- **D2:** Keine Cloud-Abhängigkeit (TypeSafe-Jev-API) in AAMS-Kern, Standard-Setup oder Proxy-Pflichtpfad. **(User-Positionierung, bindend)**
- **D3:** Vor jeder technischen Entscheidung: Repos verifizieren (Claim-Herkunft: Chat-Antwort, unverifiziert).
- **D4:** **Spec-First (bindend, User 2026-09-22):** Die Diskussion ist, ob das Pattern (JEV/Hermes) in der **AAMS-Spezifikation** Sinn macht. MANTIS-Proxy = selbstgebaute Brücke (`opencode.json`), Infrastruktur — **kein Entscheidungsziel**. Kein Abweichen vom Spec-Pfad. Die Spec-Decision selbst ist offen (siehe §6.1).

**Decision-Promotion (vor Close):** D4 (Spec-First) → Whitepaper (Kandidat: WH-002 Related Work, Abschnitt „Decision Layer / externe Runtimes" — zusammen mit Hermes-Nous-Abgrenzung).

---

## 8. RFL / LTM

- **Kein Konflikt** mit WP-2026-09-16/2026-09-22 (Hermes): gleiche Abgrenzungslogik (fremde Runtime ≠ AAMS-Kern), anderes System (Jev ≠ Hermes).
- UC7 (Context-Governor) ergänzt WP-2026-09-16 Hermes-Local (Session-State-Guard) — komplementär, kein Widerspruch.
- Stage 1 (RES-Scan closed/): WP-2026-04-17-RES-WIKI — thematisch benachbart, kein Konflikt.
- Bei Close: LTM-Ingest + Verweis auf WP-2026-09-22-SPEC-NOTE (gemeinsames Abgrenzungsmuster „fremde Runtimes").

---

## 9. file_protocol

| Aktion | Datei |
|---|---|
| create (observe) | `WORKING/WORKPAPER/observe/WP-2026-09-22-RES-JEV-open-jev-decision-layer.md` |
| read | Roh-Dump v1 (84 Zeilen) |
| move (Archiv) | v1 → `WORKING/WORKPAPER/closed/raw-dump-2026-09-22-open-jev-layer-chat-dump-v1.md` |
| read (v2) | Roh-Dump v2 (849 Zeilen, Save 09:30) — User-Positionierung + 12-Sektionen-Design |
| move (Archiv, kanonisch) | v2 → `WORKING/WORKPAPER/closed/raw-dump-2026-09-22-open-jev-layer-chat-dump.md` |
| update | Dieses WP: §1 User-Positionierung, §3 Rollenmodell, §4 Use-Cases, §5 Einordnung, D4 |
| update (v3) | Dieses WP: **Spec-First-Prinzip** (User), MANTIS-Proxy = Infrastruktur kein Ziel (`opencode.json`), D4 revidiert, Kernfrage = Spec-Sinn (§6.1), Bezug-Kontext |
| pending | INDEX.md-Eintrag (observe), LTM #146, Close nach Decision §6.1 |

---

## 10. next_steps

1. **Spec-Decision (User):** Macht das Decision-Layer-Pattern (JEV) in der AAMS-Spezifikation Sinn (`descriptive_only`)? — gemeinsam mit WP-012 (Hermes) ein Entscheidungspfad. Prinzip: „Die Spezifikation ist das Wichtigste. Kein Abweichen von diesem Pfad."
2. Repos der Tabelle in §2 klonen + READMEs prüfen (Verifizierungspflicht D3).
3. Option „Qwen als Decision-Engine im Proxy" mit minimalem PoC prüfen: `STATE/QUESTION/OPTIONS → choice + confidence` auf einem AAMS-Entscheidungsfall (z. B. UC7 Context-Governor).
4. Bei Positivbescheid: `descriptive_only`-Pattern-Sketch (analog Guard/Skills) + optionaler `WORKING/JEV/`-Pfad dokumentieren.
5. Solange: **observe** — wartet auf User-Entscheidung §6.1 + Repo-Verifizierung.
