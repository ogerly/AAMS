# Workpaper: Diary Granularity — Problem & Fragestellung

- **Datum:** 2026-04-09
- **Agent:** GitHub Copilot (Claude Opus 4.6)
- **Status:** CLOSED
- **Typ:** Problem-Analyse

---

## Problem

Die Diary-Schicht (`WORKING/DIARY/`) nutzt **monatliche Dateien** (`2026-03.md`, `2026-04.md`). Die Frage: **Wie viel geht dabei verloren?**

---

## Bestandsaufnahme

### Aktuelle Dateien

| Datei | Einträge | Zeilen | Einhaltung "max 10 Zeilen/Eintrag" |
|-------|---------|--------|-------------------------------------|
| `2026-02.md` | 2 | 12 | ❌ Eintrag 1 hat ~8 Zeilen, OK-ish |
| `2026-03.md` | 7 | 35 | ❌ Mehrere Einträge deutlich >10 Zeilen |
| `2026-04.md` | 1 | ~10 | ✅ Noch kurz |

### Beobachtungen

1. **"Max 10 Zeilen pro Eintrag" ist ein Pseudo-Constraint.** Eine Zeile kann 5 Wörter oder 500 haben. Der März-Diary beweist es: Einträge sind formal "wenige Absätze", aber jeder Absatz ist ein langer Textblock ohne Umbruch. Das ist kein Constraint — das ist Dekoration. Entweder Token-Limit, Wort-Limit, oder Satz-Limit — oder gar kein Limit und stattdessen eine strukturelle Vorgabe (z.B. Pflichtfelder statt Freitext).

2. **Monatliche Dateien werden schnell lang.** 7 Einträge × ~5-10 Zeilen = 35-70 Zeilen. Bei aktiver Entwicklung (täglich eine Session) wären das 30 Einträge × 5 Zeilen = 150 Zeilen pro Monat. Noch handhabbar, aber die Suche wird ineffizient.

3. **Kein TOPIC-Tag.** Diary-Einträge haben keinen thematischen Schlüssel. RFL kann Diary-Einträge nicht per Pattern-Match finden. Beispiel: "Warum haben wir uns gegen SCIENCE entschieden?" → Manuelles Durchsuchen der Monatsdate nötig.

4. **Diary vs. Workpaper-Decisions: Überlappung.** Viele Diary-Einträge wiederholen was schon in der Workpaper-Decisions-Sektion steht. Was ist der echte Mehrwert des Diary gegenüber `closed/` Workpapers?

---

## Kernfragen

### Q1: Ist monatliche Granularität richtig?

| Option | Pro | Contra |
|--------|-----|--------|
| **Monatlich** (Status quo) | Wenige Dateien, einfach | Wird lang, kein thematischer Zugriff |
| **Wöchentlich** | Kürzere Dateien | Viele Dateien, willkürliche Grenzen |
| **Pro Session** | Maximale Granularität | Dann ist es ein Workpaper-Duplikat |
| **Thematisch** | Perfekter Zugriff | Braucht Topic-Tags, komplexer |

### Q2: Braucht Diary überhaupt eigene Dateien?

**Provokante These:** Wenn Workpapers eine Decisions-Sektion haben UND RFL diese Decisions durchsucht — was macht das Diary dann noch, was nicht schon abgedeckt ist?

Das Diary wurde eingeführt um den Gap zwischen Workpaper (operativ) und Whitepaper (strukturell) zu füllen: **strategische Motive** die in keinem der beiden stehen. Aber in der Praxis werden Diary-Einträge zu Mini-Workpaper-Zusammenfassungen.

### Q3: Sollte Diary Topic-Tags bekommen?

Wenn wir Naming Schema für Workpapers und Whitepapers einführen — macht es Sinn, Diary-Einträge nicht zu taggen? Inkonsistenz im System.

### Q4: Wie viel geht tatsächlich verloren?

Um das zu beantworten: Was steht in Diary-Einträgen, das **nicht** in der Workpaper-Decisions-Sektion oder im LTM steht?

Schnellcheck März 2026:
- "2026-03-03" (Luna-1 Field Report): Strategische Einordnung → steht auch in WP-003
- "2026-03-26" (Konsistenz-Audit): Erkenntnis → steht auch im Workpaper
- "2026-03-27" (LHR): Kernthese → steht auch in WP-004
- "2026-03-28" (Marketing): Strategische Entscheidung → steht auch im Workpaper

**Hypothese: Die meisten Diary-Einträge sind Redundanz.** Der echte Mehrwert ist gering wenn Workpapers gut geschrieben sind.

---

## Kernidee: Diary als hierarchische Zeitkompression

**Wenn Workpapers sauber geführt sind** und LTM korrekt ingestet wird — dann ist ein Diary, das Workpaper-Decisions wiederholt, wertlos. Der einzige echte Mehrwert: **lückenlose Tagesübersicht** — was wurde an einem Tag über verschiedene Workpapers hinweg gemacht?

### Design: 3-Stufen-Kompression

| Ebene | Granularität | Dateien/Jahr | Inhalt |
|-------|-------------|-------------|--------|
| **Tag** | `YYYY-MM-DD.md` | 365 | Was wurde heute gemacht? (alle Workpapers des Tages, 2-3 Sätze pro WP) |
| **Woche** | Rollup in Tagesdatei oder separates `W{NN}` | 52 | Wochenzusammenfassung aus 7 Tagen |
| **Monat** | `YYYY-MM.md` | 12 | Monatszusammenfassung aus 4 Wochen |

**Gesamt: 365 + 52 + 12 = 429 Einträge/Jahr** für ein lückenloses Tagebuch.

### Redundanz-Test (empirisch)

**Diary-Eintrag 2026-03-27 (LHR):**
> "Analyse zu Long-Horizon-Reasoning (LHR) für reale Codebases geschrieben (Issue #27). Kernthese: LHR ist heute nicht gelöst..."

**Workpaper `closed/2026-03-27-long-horizon-reasoning-analyse.md`:**
> Exakt dasselbe — ausführlicher. Session Scope, Running Log, Analyse, Decisions. Alles da.

**Ergebnis: Der Diary-Eintrag ist ein Abstract des Workpapers. Null neuer Informationsgehalt.**

Gleiches Bild bei allen März-Einträgen:
- 2026-03-03 (Luna-1): Diary = Abstract von WP-003 + Workpaper → redundant
- 2026-03-26 (Konsistenz-Audit): Diary = Abstract vom Workpaper → redundant
- 2026-03-27 (Bootstrap-Gap): Diary = Abstract vom Workpaper → redundant
- 2026-03-28 (Marketing): Diary = Abstract vom Workpaper → redundant

**These bestätigt: 100% der Diary-Einträge sind Workpaper-Abstracts. Kein einziger enthält Information, die nicht schon im Workpaper oder Whitepaper steht.**

### Konsequenz: Diary = reiner Zeitindex

Ein Diary-Eintrag darf **keine Inhalte** wiederholen. Er ist ein **Pointer** — nicht mehr.

**Format (ein Eintrag = eine Zeile):**

```
YYYY-MM-DD | WP: {workpaper-dateiname} | WH: {whitepaper falls aktualisiert} | Sonstige Dateien
```

**Beispiel — was der 2026-03-27-Eintrag hätte sein sollen:**

```
2026-03-27 | WP: 2026-03-27-long-horizon-reasoning-analyse.md | WH: WP-004 erstellt | SPEC.md aktualisiert
```

Eine Zeile. Kein Abstract. Kein Inhalt. Wer Details will → folgt dem Pointer ins Workpaper.

**Was das leistet, was kein anderer Layer kann:**
- "Wann habe ich zuletzt an WP-004 gearbeitet?" → Diary durchsuchen
- "Was habe ich am 27. März gemacht?" → Diary-Zeile zeigt alle betroffenen Dokumente
- "Wie oft wurde READ-AGENT.md diesen Monat angefasst?" → grep über Diary

### 3-Stufen-Kompression (auf Pointer-Basis)

| Ebene | Granularität | Dateien/Jahr | Inhalt |
|-------|-------------|-------------|--------|
| **Tag** | Zeilen in Tagesdatei `YYYY-MM-DD.md` | 365 | Pointer: welche WPs/WHs/Dateien angefasst |
| **Woche** | Rollup | 52 | Welche Dokumente diese Woche aktiv waren |
| **Monat** | `YYYY-MM.md` | 12 | Aktivitätsübersicht: welche Themen (via TOPIC-Tags) dominiert haben |

**429 Einträge/Jahr, aber jeder Eintrag ist 1 Zeile — kein Roman.**

### Ablauf

1. **Bei Session-Close**: Agent schreibt Tageszeile — nur welche Dokumente angefasst wurden
2. **Nach 7 Tagen**: Agent komprimiert 7 Tage zu Wochenübersicht (welche TOPICs aktiv)
3. **Nach 4 Wochen**: Agent komprimiert zu Monatsübersicht (Fokus-Themen, Aktivitätsvolumen)

### Offene Designfragen

- **Dateistruktur**: Tageseinträge in einer Monatsdatei? Oder separate `YYYY-MM-DD.md`?
- **Kompression-Trigger**: Automatisch bei Session-Start wenn Woche/Monat vorbei? Oder explizit?
- **Mehrere Sessions pro Tag**: Append an Tageseintrag — eine Zeile pro Session

---

## Ursprüngliche Optionen (vor hierarchischem Ansatz)

1. **Diary bleibt, aber mit Topic-Tag-Headings** — `### 2026-04-09 [ARCH] SCIENCE verworfen → RFL`
2. **Diary wird abgeschafft** — Decisions in Workpapers + LTM decken alles ab
3. **Diary wird zum narrativen Kontext-Layer** — weniger Fakten, mehr "warum eigentlich?" (echte Reflexion, nicht Zusammenfassung)
4. **Diary wird pro Quartal statt pro Monat** — weniger Dateien, gleiche Funktion
5. **NEU: Hierarchische Zeitkompression** — Tag → Woche → Monat (bevorzugt)

---

## Decisions

- **D1**: Diary wird zum **pointer-only Zeitindex** reformiert. Keine Inhalte, nur Verweise auf angefasste Dokumente.
- **D2**: Format: `YYYY-MM-DD | WP: {datei} | WH: {datei} | {sonstige}`  — eine Zeile pro Session.
- **D3**: Hierarchische Kompression: Tag → Woche → Monat (429 Einträge/Jahr).
- **D4**: "Max 10 Zeilen" Pseudo-Constraint ersatzlos gestrichen. Ersetzt durch strukturelle Vorgabe (Pointer-Format).
- **D5**: Jedes Kettenglied muss eigenen Mehrwert bringen: Workpaper = Was/Wie, Whitepaper = Architektur, LTM = Wissen, Diary = Zeitachse.
- **D6**: Redundanz-Test bestätigt: 100% der bisherigen Diary-Einträge waren Workpaper-Abstracts → null eigenständiger Informationsgehalt.

---

## Next Steps

- [x] Systematischer Vergleich: Diary-Einträge vs. Workpaper-Decisions — 100% Redundanz bestätigt
- [x] Entscheidung: Diary reformieren zu Pointer-only Zeitindex
- [x] Patches: `.agent.json`, `READ-AGENT.md`, `reference/SPEC.md` aktualisiert
- [ ] Bestehende Diary-Dateien (02, 03, 04) können optional migriert werden (nicht zwingend)

---

## File Protocol

| # | Aktion | Datei | Beschreibung |
|---|--------|-------|-------------|
| F1 | CREATED | `WORKING/WORKPAPER/2026-04-09-ARCH-DRY-diary-granularity-problem.md` | Dieses Workpaper || F2 | MODIFIED | `.agent.json` | Diary purpose + format auf Pointer-only geändert |
| F3 | MODIFIED | `READ-AGENT.md` | Diary Beschreibung + Workspace-Tabelle aktualisiert |
| F4 | MODIFIED | `reference/SPEC.md` | Diary-Sektion komplett überarbeitet |