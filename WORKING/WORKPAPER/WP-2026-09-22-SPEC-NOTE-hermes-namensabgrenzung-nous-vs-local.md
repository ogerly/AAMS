# WP-2026-09-22-SPEC-NOTE-hermes-namensabgrenzung-nous-vs-local

**Status:** open
**Datum:** 2026-09-22
**TOPIC/SUBTOPIC:** SPEC/NOTE
**Session-Ziel:** Namenskollision „Hermes" auflösen: Hermes-Local (Local-Adaptation/Session-Guard, WP-2026-09-16) vs. Hermes-Nous (Nous-Research-Hermes-Agent, externe Runtime). Agenten in AAMS-Repos sollen beides nicht vermischen. Keine Implementierung, kein Upstream-RFC.

**Herkunft:** Aus Chat-Dump anderer Agenten-Sitzung bereinigt (Rohfassung archiviert: `closed/raw-dump-2026-09-22-hermes-namensabgrenzung-chat-dump.md`).

**Bezug:**
- Vorgänger: `WORKING/WORKPAPER/closed/WP-2026-09-16-SPEC-QUEST-hermes-sidecar-stellungnahme.md` (closed, LTM #142, Issue #53)
- Diary: `WORKING/DIARY/2026-09.md` (2026-09-16 Sidecar-Stellungnahme)

---

## 1. session_goal

1. Zwei verschiedene Systeme namens „Hermes" explizit trennen.
2. Mapping: welches Konzept zu welchem AAMS-Handlungsfeld gehört.
3. Lese-/Schreibregeln für Agenten in AAMS-Repos (auch wenn beides parallel vorkommt).
4. Keine Änderung an D1/D2 der Sidecar-Stellungnahme — nur Abgrenzung und optionaler Spec-Hinweis.

---

## 2. Problem

„Hermes" wird in zwei Kontexten verwendet:

| Label (dieses WP) | Was es ist | Typische Artefakte |
|---|---|---|
| **Hermes-Local** | Local Adaptation / Session-Guard (z. B. OpenCode-Plugin, geplanter Sidecar Stufe 2) | Context-Füllung (z. B. 70/85/90 %), SOFT/HARD/HANDOFF, `HERMES-AUTO`-Segmente im Workpaper |
| **Hermes-Nous** | Nous Research Hermes **Agent** (Runtime/Harness) | `$HERMES_HOME/state.db`, `memories/MEMORY.md`, `USER.md`, Skills, Context-Compression, optionale Memory-Provider |

Vermischung führt zu falschen Spec-Schlüssen, z. B.:
- Sidecar-Regeln auf `state.db` anwenden
- Nous-Memory-Pfade als AAMS-Pflichtkern lesen
- F3/Sidecar-Evidenz mit Runtime-Plugin-Fragen vermengen

---

## 3. Abgrenzung (verbindlich für Agenten in diesem Repo)

### 3.1 Hermes-Local (bereits positioniert)

- **Quelle in AAMS:** WP-2026-09-16 (Stellungnahme Q1–Q5).
- **AAMS-Einordnung:** Local Adaptation. Upstream höchstens generisches Pattern „Session-State-Guard" (`descriptive_only`), nie Pflicht-Kern.
- **Schreibt:** optional append-only in markierte Workpaper-Segmente (`HERMES-AUTO`); Single-Writer; Toggle default-off; Fail-open.
- **Schreibt nicht:** Inline-Rewrite im Request-Pfad; erzwungenen Session-Neustart; Überschreiben von Agent-Segmenten.
- **Lifecycle:** an den **Workpaper**-Lifecycle gebunden (`on_session_start` / `on_session_end`), nicht allein an das Context-Fenster.

### 3.2 Hermes-Nous (Runtime, spez-informativ)

- **Quelle:** Nous Research Hermes Agent (Open Source).
- **Home:** `$HERMES_HOME` (Default `~/.hermes`; Profile: `$HERMES_HOME/profiles/<name>/`).
- **AAMS-Einordnung:** **fremde Runtime**, kein AAMS-Modul. AAMS bleibt Manifest + `WORKING/`. Kein Pflicht-Plugin „AAMS für Hermes-Nous".
- **Episodisch:** `state.db` — User-/Assistant-/Tool-Messages, Metadaten, FTS5; lokal; sensibel (Transcript-Charakter).
- **Kuratiert:** `memories/MEMORY.md`, `memories/USER.md` (Zeichen-Limits; Frozen Snapshot am Session-Start).
- **Context:** Compression ändert das Prompt-Fenster, löscht nicht die DB-Historie.
- **Bridge (optional, Local Adaptation):** kuratierte Memory-Dateien gezielt lesen; `state.db` nur gezielt/suche; kein Full-Dump; `.env` nie in AAMS-Dateien spiegeln.

### 3.3 Merksatz

> **Hermes-Local** = Session-/Workpaper-Guard im AAMS-Ritual.
> **Hermes-Nous** = Agent-Runtime mit eigener DB und Memory-Dateien.
> AAMS trägt die **Projektwahrheit** in `WORKING/`; keines von beiden ersetzt AAMS.

---

## 4. Handlungsmatrix

| Situation | Tun | Nicht tun |
|---|---|---|
| Sidecar, SOFT/HARD, `HERMES-AUTO`, F3 | WP-2026-09-16 + dieses WP; Pattern Session-State-Guard | Nous-`state.db` als Sidecar-Spec behandeln |
| Nous Hermes Agent + AAMS im Einsatz | AAMS-Contract + Workpaper-Disziplin; optional `USER.md` / `MEMORY.md` | AAMS als Hermes-Nous-Plugin fordern; ganze `state.db` in den Context laden |
| Beide Begriffe in einer Session | Explizit **Hermes-Local** vs. **Hermes-Nous** labeln | Ein gemeinsames „Hermes-Subsystem" annehmen |
| Upstream-RFC | Nur nach Q2-Bedingungen + E1–E7 (WP-2026-09-16) | Nous-Implementierungsdetails in den AAMS-Kern schreiben |

---

## 5. Optionaler Spec-Hinweis (WHAT only)

Falls später in CONTRACT / GUIDELINES (kein Required-Feld in `AGENT_SCHEMA.json`):

```text
runtime_name_disambiguation:
  hermes_local: session-state-guard / workpaper auto-segments (WP-2026-09-16)
  hermes_nous: external agent runtime (state.db, MEMORY.md); adapter descriptive_only
  aams_core: requires neither
```

Status analog Guard: `descriptive_only`.

---

## 6. Security (Hermes-Nous, kurz)

- `state.db` und `.env`: lokal, hochsensibel — nicht committen, keine Roh-Transcripts in Whitepaper/Diary/MEMORY.
- AAMS-MEMORY/DIARY: nur kuratierte Projektfakten und Decisions.
- Sidecar-Auto-Segmente: Vorschläge mit Provenienz; vor LTM-Promotion prüfen (WP-2026-09-16 R3).

---

## 7. decisions

- **D1:** In diesem Repo ab sofort **Hermes-Local** vs. **Hermes-Nous** (oder ausgeschrieben). Bloßes „Hermes" in neuen WPs vermeiden oder beim ersten Vorkommen disambiguieren.
- **D2:** WP-2026-09-16 (Sidecar Q1–Q5, optionales Modul) bleibt **unverändert**. Dieses WP ist Abgrenzung, kein Revisit.
- **D3:** AAMS wird **nicht** als Nous-Hermes-Plugin definiert. Höchstens optionale Bridge als Local Adaptation.

**Decision-Promotion (vor Close erforderlich):**
- D1 → Whitepaper (Kandidat: WH-002 Related Work, Abschnitt „Nomenklatur externer Runtimes")
- D3 → Whitepaper (Kandidat: WH-002 Related Work, Abschnitt „Grenzen: AAMS ≠ Plugin für fremde Runtimes")
- D2 → keine Promotion (Bestätigung bestehender Decision)

---

## 8. RFL / LTM

- **Kein Konflikt** mit WP-2026-09-16: Ergänzung, keine Gegen-Decision (Stage 1: `*-SPEC-*` Scan closed/).
- Bei Close: LTM-Eintrag sinngemäß „Hermes-Local ≠ Hermes-Nous; WP-2026-09-22".
- Diary: dieses WP + Verweis auf WP-2026-09-16 / LTM #142.

---

## 9. file_protocol

| Aktion | Datei |
|---|---|
| create (open) | `WORKING/WORKPAPER/WP-2026-09-22-SPEC-NOTE-hermes-namensabgrenzung-nous-vs-local.md` |
| read | Roh-Dump, WP-2026-09-16 (Sidecar-Stellungnahme), `WORKING/DIARY/2026-09.md` |
| move (Archiv) | Roh-Dump → `WORKING/WORKPAPER/closed/raw-dump-2026-09-22-hermes-namensabgrenzung-chat-dump.md` |
| pending (session end) | `WORKING/WORKPAPER/INDEX.md`, LTM-Ingest, Decision-Promotion (D1/D3), dann → `closed/` |

---

## 10. next_steps

1. Maintainer-Review: D1/D3 bestätigen oder revidieren.
2. Decision-Promotion: D1 + D3 in WH-002 (oder neues Whitepaper) eintragen, WHITEPAPER/INDEX.md aktualisieren.
3. Close: LTM-Ingest + Workpaper → `closed/`.
4. Bei künftigen Hermes-Themen: Label **Local** oder **Nous** in der ersten Zeile setzen.
5. **Spec-First (User, 2026-09-22, bindend):** Die Hermes-/JEV-Frage ist eine **Spec-Frage** — ob das Session-State-Guard-Pattern in der AAMS-Spezifikation Sinn macht (`descriptive_only`). Gleicher Entscheidungspfad wie WP-013 (JEV, §6.1). MANTIS-Proxy (selbstgebaute Brücke, `opencode.json`, muss bei OpenCode/VS-Code immer laufen) = Infrastruktur, kein Entscheidungsziel. „Die Spezifikation ist das Wichtigste. Kein Abweichen von diesem Pfad."
