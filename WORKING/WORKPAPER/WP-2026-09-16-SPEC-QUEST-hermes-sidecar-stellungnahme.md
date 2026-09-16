# WP-2026-09-16-SPEC-QUEST-hermes-sidecar-stellungnahme

**Status:** open
**Datum:** 2026-09-16
**TOPIC/SUBTOPIC:** SPEC/QUEST
**Session-Ziel:** Stellungnahme als AAMS-Maintainer-Agent zu einem Hermes-Sidecar-Vorhaben aus fremdem Repo (MANTIS-LLM-PROXY-3, AAMS/2.4.0). Keine Implementierung, keine Commits.

---

## 1. session_goal

Fünf Fragen (Q1–Q5) zum Hermes-Stufe-2 „Sidecar" beantworten: Spec-Konformität (D9, WH-009, Local-Adaptation), F3-Revisit-Bedingungen, Kern-vs-Modul-Einordnung, Risiken (Dual-Writer, Lifecycle), Evidenz-Bedarf. Falls Q2 positiv: Entwurf Pattern-Dokument/RFC-Template.

## 2. Kontext (fremdes Repo, von dort übernommen — keine lokale Verifikation möglich)

- Hermes = **Local Adaptation** (dort WH-013 v0.3): OpenCode-Plugin (`.opencode/plugin/hermes.ts`), misst Context-Füllung (tokens.input/limit.context), injiziert bei 70/85/90 % SOFT/HARD/HANDOFF-Checkpoint-Anweisungen. Agent führt AAMS-Rituale selbst aus, Plugin = nur Trigger. Status dort: produktiv, 12/12 Tests grün, Skill-Doku, Convention „Session = Context-Fenster, Workpaper = Task".
- F3 (RFC an ogerly/AAMS) am 2026-09-13 dort bewusst ABGELEHNT — Hermes bleibt lokale Convention.
- DeepSeek-Harness-Alternative am 2026-09-15 dort verworfen (Agent-Runtime ≠ Session-Guard, Dopplung).
- **Vorhaben (keine Decision, nur Stellungnahme erbeten):** Hermes-Stufe-2 „Sidecar": Hintergrund-Watcher (eigener Prozess oder Plugin-Teil), schreibt bei SOFT Datei-Protokoll + Decisions SELBST ins offene Workpaper — mit kleinem Lokalmodell via LM Studio (:1234, am Proxy vorbei), Toggle an/aus, strikt append-only in eigene HERMES-AUTO-Segmente (Single-Writer-Regel, kein Überschreiben von Agent-Inhalten).
- **Explizit ausgeschlossen:** (a) Inline-Umschreiben von Prompts im Request-Pfad, (b) vollautomatischer Session-Neustart.

## 3. LTM-Abfrage (2026-09-16, Track A — `WORKING/MEMORY/ltm-index.md`)

| Begriff | Treffer im lokalen LTM |
|---|---|
| Hermes | **keine** — rein fremder Kontext (dort WH-013) |
| WH-013 | **keine** — lokale Whitepapers enden bei WH-011 |
| F3 | **keine** — lokale Issues: #43 RFC-Tracker (Spec→Contract), kein Hermes-RFC eingegangen |
| Guard-Pattern (WH-009) | Eintrag #139/#140 (2026-07-06): Zwei-Ebenen-Modell, drei Check-Ebenen, `status: descriptive_only` |
| D9 (Manifest-Prinzip) | Einträge #117, #120, #122, #124–126 (2026-04-29): „AAMS describes, es schreibt kein Verhalten vor" — verankert in `.agent.json`, CONTRACT.md, allen Whitepapers |

## 4. RFL Consistency Check (3-stufig)

- **Stage 1** (Pattern-Match `*-SPEC-*` in `closed/`): keine Hermes-relevanten Decisions.
- **Stage 2** (LTM): keine Hermes/F3-Einträge (s. §3).
- **Stage 3** (letztes geschlossenes WP): kein Bezug.
- **Ergebnis: kein Konflikt. Kein ⚠ RFL Flag nötig.** Hinweis: Dieses Repo hat zu Hermes *keine* Position — die Stellungnahme ist Erstbefassung, kein Revisit lokaler Decisions. Die F3-Ablehnung vom 2026-09-13 ist eine Decision des *fremden* Repos, nicht von ogerly/AAMS — sie bindet uns nicht, ist aber als deren Selbstbindung zu respektieren (wir entscheiden nichts *für* sie, nur *über* Upstream-Kriterien).

## 5. Stellungnahme (Maintainer-Sicht, AAMS/2.4.0)

### Q1 — Spec-Konformität

**Kurz: Nein, kein Verstoß — sofern drei Bedingungen erfüllt sind. Der Sidecar ist als Local Adaptation zulässig; upstream beschreibbar wäre nur das Pattern, nie die Implementierung.**

Begründung Punkt für Punkt:

- **D9 („describes, not prescribes"):** D9 bindet *AAMS*, nicht die Nutzer-Repos. Es verbietet uns, Verhalten vorzuschreiben — es verbietet einem Repo nicht, sich selbst strengere Regeln zu geben. Ein aktiver Sidecar schreibt dem *eigenen* Agenten vor, nicht fremden. D9-Verletzung läge nur vor, wenn (a) AAMS den Sidecar *vorschreiben* würde (Pflicht-Kern ohne Opt-out), oder (b) das fremde Repo seinen Sidecar als AAMS-Pflicht ausgibt. Beides ist nicht der Fall: Toggle Default-off + als lokale Convention deklariert = D9-konform.
- **Guard-Pattern (WH-009):** Kein Verstoß, aber Kategorienfehler wenn man ihn so liest. WH-009 sichert *Contract-Durchsetzung vor* write/edit (manifest_read, workpaper_open, tools_gated — defensiv, blockierend). Hermes-Sidecar ist *Zustandssicherung während* der Session (offensiv, schreibend). Das ist ein **anderes Pattern** (Session-Guard vs. Write-Guard), kein Unterfall von WH-009. Es kollidiert nicht, es ergänzt — muss aber als eigenes Pattern beschrieben werden (s. unten), nicht unter WH-009 subsumiert.
- **Local-Adaptation-Prinzip:** Voll erfüllt. Plugin + Sidecar + LM-Studio-Verdrahtung sind implementierungsspezifisch (OpenCode-API, Port :1234, Modellwahl) — exakt die HOW-Ebene aus dem Zwei-Ebenen-Modell. Upstream gehört nur die WHAT-Ebene.
- **Was als Pattern zu beschreiben wäre** (analog WH-009, WHAT nicht HOW): (1) Trigger-Schwellen als *beschriebene* Konvention (SOFT/HARD/HANDOFF mit dokumentierter Semantik, keine festen Prozentwerte als Pflicht); (2) **Single-Writer-Regel**: Sidecar schreibt ausschließlich append-only in eigene, markierte Segmente (`HERMES-AUTO`), niemals in Agent-Segmente; (3) **Toggle-Default-off** + Fail-open (Sidecar-Ausfall darf die Session nie blockieren); (4) **Provenienz-Markierung**: jede Auto-Segment-Zeile mit Quelle + Zeitstempel; (5) Kein Eingriff in Request-Pfad und kein erzwungener Session-Neustart (die beiden Ausschlüsse als Pattern-Bestandteil festschreiben — sie sind die D9-Schutzplanke).

### Q2 — F3-Revisit: Bedingungen für einen Upstream-Beitrag

**Kurz: Ja, denkbar — aber nicht als Hermes-Implementierung, sondern als generisches Pattern-Dokument („Session-State-Guard" o.ä.). Hermes-spezifisches (Plugin-Code, Prozentwerte, LM-Studio-Port) bleibt Local Adaptation.**

Eintrittsbedingungen (alle kumulativ):

1. **Bewährungszeit + Praxis-Logs (F4-Kalibrierung):** mind. 4–8 Wochen produktiver Betrieb des Sidecars, mit Log-Auswertung: Wie oft feuerte SOFT? Wie viele Auto-Segmente wurden vom Agenten übernommen vs. ignoriert/korrigiert? False-Positive-Rate (SOFT ohne echten Füllungsdruck)? Ohne diese Zahlen ist das Pattern unkalibriert und nicht beschreibbar.
2. **Test-Harness-Pflicht:** analog „12/12 grün" auf Stufe 1 — deterministische Tests für: append-only-Einhaltung (Sidecar überschreibt nie Agent-Text), Segment-Markierung, Toggle-off = Null-Effekt, Fail-open bei totem LM-Studio-Endpunkt.
3. **Toggle-Default-off + Zero-Dependency im Default-Pfad:** `.agent.json` ohne Sidecar-Referenz muss vollständig funktionsfähig bleiben; kein neues Required-Feld in `AGENT_SCHEMA.json`; kein neuer Pflicht-Ordner. Das Pattern darf im CONTRACT nur als `status: descriptive_only`-Sektion landen (wie `guard` heute).
4. **Generalisierung:** RFC beschreibt das Pattern tool-agnostisch (nicht „OpenCode-Plugin", sondern „Session-State-Guard": Trigger → Auto-Segment → Provenienz → Single-Writer). Mind. eine zweite Tool-Implementierungsskizze (z. B. Cursor/Copilot-Regel) als Existenzbeweis, dass es kein OpenCode-Spezifikum ist.
5. **F3-Historie respektieren:** Der RFC muss die Ablehnung vom 2026-09-13 referenzieren und begründen, was sich geändert hat (Stufe 2 = neue Evidenzlage, nicht Wiederaufnahme desselben Antrags). Form: neuer RFC, kein Reopen.

### Q3 — Kern vs. Modul

**Kurz: Eindeutig optionales Modul/Pattern, kein Pflicht-Kern.**

Begründung:

1. **Präzedenz:** `guard` (WH-009), `skills`, `security`, `file_safety` sind alle optional + `descriptive_only` — trotz teils sicherheitsrelevanten Inhalts. Ein Session-Komfort-Automatismus hat geringeres Gewicht als diese und kann daher keinen Kern-Status beanspruchen.
2. **D9-Test:** Kern = was jedes AAMS-Repo *braucht*, um interoperabel zu sein (Workspace-Struktur, Dokumentationsmodell, Naming). Ein Sidecar braucht ein Repo nicht zur Interoperabilität — es ist eine *Betriebsverbesserung* einzelner Repos. Pflicht-Kern würde D9 verletzen (Vorschrift statt Beschreibung).
3. **Abhängigkeits-Test:** Kern muss zero-dependency sein. Der Sidecar braucht per Konstruktion eine Runtime (Watcher-Prozess, Lokalmodell-Endpunkt). Alles mit Runtime-Abhängigkeit ist per Definition Modul.
4. Formulierung analog Guard: „AAMS beschreibt WAS (Auto-Segment-Konvention, Single-Writer, Provenienz), das Repo implementiert WIE (Plugin, Sidecar, Modell, Schwellen)."

### Q4 — Risiken aus Spec-Sicht + vertragliche Einfangung

**R1 — Dual-Writer (Sidecar + Haupt-Agent schreiben dasselbe Workpaper):**
Reales Risiko: Interleaving (beide schreiben gleichzeitig), semantische Drift (Auto-Segment widerspricht Agent-Text), Provenienz-Verlust (nach 3 Sessions unklar, wer was schrieb). Vertragliche Einfangung: (a) **Single-Writer-Regel pro Segment**: Sidecar = alleiniger Writer seiner `HERMES-AUTO`-Segmente, Agent = Writer des Rests; (b) **Append-only**: Sidecar darf nur anhängen, nie editieren/löschen — auch nicht eigene alte Segmente (Korrektur = neues Segment mit Supersede-Verweis); (c) **Provenienz-Pflicht**: jedes Auto-Segment mit `source: hermes-sidecar`, Zeitstempel, Trigger-Level; (d) **Agent-Vorrang**: bei Widerspruch gilt Agent-Text; Agent darf Auto-Segmente per expliziter Zeile verwerfen (`HERMES-AUTO superseded by agent`), Sidecar darf das nie zurückschreiben.

**R2 — Lifecycle-Bruch („created at session start, closed at session end" vs. Session = Context-Fenster):**
Reales Risiko: Wenn dort „Session = Context-Fenster, Workpaper = Task" gilt, überlebt ein Task-Workpaper mehrere Context-Fenster — der Sidecar (pro Fenster gestartet/gestoppt) schreibt dann in ein Workpaper, dessen Lifecycle er nicht besitzt; beim Handoff drohen verwaiste Auto-Segmente oder doppelter SOFT-Feuerstoß im neuen Fenster. Vertragliche Einfangung: (a) **Workpaper-Lifecycle bleibt maßgeblich** (on_session_start/on_session_end aus `.agent.json`): Der Sidecar besitzt keinen eigenen Lifecycle, er ist an den des offenen Workpapers gebunden; (b) **Fenster-Grenze explizit markieren**: erstes Auto-Segment nach Handoff mit `continues_from: <Fenster/Commit>` + Re-Baseline der Füllungsmessung (kein „geerbter" SOFT-Alarm aus dem alten Fenster); (c) **Close-Hook**: bei Workpaper-Close schreibt der Agent (nicht der Sidecar) eine Abschlusszeile über offene Auto-Segmente (übernommen/verworfen/offen) — sonst entsteht Decision-Drift analog Issue #48.

**R3 (zusätzlich, Spec-seitig): Latenz-/Fehlerdomäne des Lokalmodells:** Fail-open-Pflicht (s. Q1) + Auto-Segmente sind Vorschläge mit Provenienz, keine Fakten — der Agent muss sie vor Promotion (WH → LTM) verifizieren (Decision-Promotion-Check in `READ-AGENT.md` gilt auch für Auto-Segmente).

### Q5 — Evidenz-Bedarf (um Q1–Q4 entscheidbar zu machen)

| # | Evidenz | Wofür |
|---|---|---|
| E1 | Feuerungs-Log: Datum, Trigger-Level, tatsächliche Füllung, Session-/Fenster-ID | F4-Kalibrierung der Schwellen (Q2.1) |
| E2 | Übernahme-Quote: Auto-Segmente übernommen / korrigiert / verworfen (Agent-Urteil) | Nutzen-Nachweis; False-Positive-Rate |
| E3 | Test-Harness: append-only-Test, Toggle-off-Test, Fail-open-Test (LM Studio tot), Interleaving-Test | Q2.2, R1-Absicherung |
| E4 | Beispiel-Workpaper mit HERMES-AUTO-Segmenten (anonymisiert, keine Secrets) | Pattern-Beschreibung prüfen (Q1-Forderung) |
| E5 | Handoff-Protokoll: 2–3 dokumentierte Fenster-Wechsel mit Workpaper-Kontinuität | R2-Absicherung |
| E6 | Latenz-/Ressourcen-Messung (Sidecar-Overhead pro Feuerung) | Nachweis „kein Eingriff in Request-Pfad" (Aus schluss a) |
| E7 | F3-Referenz: Link/Datum der Ablehnung + Delta-Begründung | Q2.5 (neuer RFC, kein Reopen) |

Mindest-Umfang für RFC-Reife: E1+E2 über 4–8 Wochen, E3 grün, E4 vorhanden. E5–E7 bei Einreichung.

## 6. Entwurf: Pattern-Dokument- / RFC-Template-Struktur (da Q2 positiv)

Vorgeschlagene Struktur für ein künftiges WH-0xx „Session-State-Guard" (Spiegelung von WH-009) bzw. als RFC-Body:

```
1. Problem (Zustandsverlust bei Context-Druck — was WH-009 nicht abdeckt)
2. Abgrenzung (Write-Guard vs. Session-Guard; ausgeschlossene Optionen: Inline-Rewrite, Auto-Restart)
3. Zwei-Ebenen-Modell (AAMS: WHAT — Trigger-Semantik, Auto-Segment-Konvention, Single-Writer, Provenienz, Toggle-off, Fail-open / Local: HOW — Tool, Modell, Schwellen, Verdrahtung)
4. Segment-Konvention (Marker-Format, Append-only, Provenienz-Felder, Supersede-Mechanik, Agent-Vorrang)
5. Lifecycle-Anbindung (Bindung an Workpaper-Lifecycle, Fenster-Grenzen-Markierung, Close-Hook)
6. Fehlerformate (beschreibend, D9-konform)
7. Schema (optionale `session_guard`-Sektion, status: descriptive_only, keine Required-Felder)
8. Referenzimplementierungen (Tabelle Tool → Pfad → Status; mind. 1 produktiv + 1 Skizze)
9. Evidenz-Anhang (E1–E7 aus §5/Q5)
10. Status-Checkliste (analog WH-009 §Status)
```

## 7. file_protocol

| Aktion | Datei |
|---|---|
| created (open) | `WORKING/WORKPAPER/WP-2026-09-16-SPEC-QUEST-hermes-sidecar-stellungnahme.md` |
| read | `.agent.json`, `READ-AGENT.md`, `WORKING/MEMORY/ltm-index.md`, `WORKING/WHITEPAPER/WH-009-guard-pattern.md`, `reference/CONTRACT.md`, `WORKING/WORKPAPER/INDEX.md` |
| pending (session end) | `WORKING/WORKPAPER/INDEX.md` aktualisieren, LTM-Ingest, Workpaper → `closed/` |
| 2026-09-16 | Issue #53 geprüft (open, 0 Kommentare, Body 2891 Zeichen) via GitHub-API |
| 2026-09-16 | Stellungnahme Q1–Q5 + Pattern-Entwurf als Issue-Kommentar gepostet (ID 5692798068) |

## 8. decisions

- **D1:** Stellungnahme = Erstbefassung, kein Revisit lokaler Decisions (kein RFL-Konflikt; F3-Ablehnung ist fremde Decision, bindet ogerly/AAMS nicht).
- **D2 [PROMOTE-Kandidat]:** Falls das Pattern je upstream kommt → optionales Modul (`descriptive_only`), nie Pflicht-Kern. (Promotion-Ziel noch offen — ggf. WH-001-Nachtrag oder neues WH-0xx bei RFC-Eingang; **Workpaper darf nicht mit offenem PROMOTE-Tag geschlossen werden** → vor Close klären: nur als Workpaper-Position belassen oder in WH-001 als „zugesagte Upstream-Kriterien" vermerken.)

## 9. next_steps

1. Stellungnahme-Antwort an anfragendes Repo übermitteln (Q1–Q5 + Template-Entwurf).
2. D2-Promotion klären (belassen vs. WH-001-Vermerk), dann Session-Close: INDEX.md, LTM-Ingest, → `closed/`.
3. Bei künftigem RFC-Eingang: gegen Q2-Bedingungen + E1–E7 prüfen.
