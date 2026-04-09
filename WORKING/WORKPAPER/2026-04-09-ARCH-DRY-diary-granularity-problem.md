# Workpaper: Diary Granularity — Problem & Fragestellung

- **Datum:** 2026-04-09
- **Agent:** GitHub Copilot (Claude Opus 4.6)
- **Status:** OPEN — Offene Frage, nicht gelöst
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

1. **"Max 10 Zeilen pro Eintrag" wird nicht eingehalten.** Der März-Eintrag zu "2026-03-03" ist allein ~10 Zeilen. Der zu "2026-03-26" ebenfalls. Das ist keine Disziplin-Frage — 10 Zeilen sind zu wenig um eine Architekturentscheidung sinnvoll zu kontextualisieren.

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

## Mögliche Richtungen (nicht entschieden)

1. **Diary bleibt, aber mit Topic-Tag-Headings** — `### 2026-04-09 [ARCH] SCIENCE verworfen → RFL`
2. **Diary wird abgeschafft** — Decisions in Workpapers + LTM decken alles ab
3. **Diary wird zum narrativen Kontext-Layer** — weniger Fakten, mehr "warum eigentlich?" (echte Reflexion, nicht Zusammenfassung)
4. **Diary wird pro Quartal statt pro Monat** — weniger Dateien, gleiche Funktion

---

## Decisions

Keine. Dies ist ein offenes Workpaper zur Untersuchung.

---

## Next Steps

- [ ] Systematischer Vergleich: Diary-Einträge vs. Workpaper-Decisions — was ist echte Redundanz?
- [ ] Entscheidung: Diary behalten / reformieren / abschaffen?
- [ ] Falls behalten: Topic-Tags in Diary-Headings?

---

## File Protocol

| # | Aktion | Datei | Beschreibung |
|---|--------|-------|-------------|
| F1 | CREATED | `WORKING/WORKPAPER/2026-04-09-ARCH-DRY-diary-granularity-problem.md` | Dieses Workpaper |
