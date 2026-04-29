# Guideline: Theoretical Stress Testing (TST)

> **Gültig ab:** 2026-04-17  
> **Herkunft:** Workpaper `2026-04-17-RES-WIKI-karpathy-llm-wiki-vergleich.md`  
> **Typ:** Methodik / Qualitätssicherung

---

## Warum

Architektur-Analysen und Vergleichsstudien produzieren Thesen. Diese Thesen klingen plausibel — sind aber oft **quantitativ falsch**. Erst ein Stresstest gegen echte Projektdaten deckt auf, ob eine Behauptung hält oder übertrieben ist.

**Entdeckung (2026-04-17):** Drei zentrale Thesen der LLM-Wiki-vs-AAMS-Analyse waren quantitativ falsch:

| These | Behauptung | Realität nach Test |
|---|---|---|
| Lint-Token-Kosten | ~30k Tokens | ~3k Tokens (10× überschätzt) |
| Kompoundierungs-Gap | „Wissen akkumuliert langsam" | **Schlimmer als beschrieben** — Decisions versickern in offenen Workpapers |
| Cross-Ref-Aufwand | „Hoch, bei jedem Schreibvorgang" | Fällt in bestehende RFL-Phase, ~zero extra Cost |

Ohne Stresstest wären falsche Prioritäten gesetzt worden (Lint zu niedrig, Promotion zu niedrig, Cross-Ref zu hoch).

---

## Methodik

### Wann durchführen?

- Bei jeder Architektur-Analyse oder Vergleichsstudie
- Bei Empfehlungen die Token-Kosten oder Agent-Aufwand schätzen
- Bei Entscheidungen die auf Annahmen über Projektscale basieren

### Wie durchführen?

1. **Echte Zahlen erheben** — nicht schätzen, sondern messen:
   - Dateianzahl im `WORKING/`-Baum
   - Zeilenanzahl der betroffenen Dokumente
   - Anzahl offener vs. geschlossener Workpapers
   - LTM-Index-Größe

2. **Mindestens 3 Szenarien testen** — jeweils mit konkreten Daten:
   - **Kosten-Szenario:** Was kostet die Empfehlung in Tokens/Zeit?
   - **Evidenz-Szenario:** Gibt es im Repo bereits Fälle die die These stützen oder widerlegen?
   - **Skalierungs-Szenario:** Hält die These bei 2×, 5×, 10× der aktuellen Datenmenge?

3. **Korrekturen dokumentieren** — Abweichungen zwischen Behauptung und Realität explizit festhalten. Prioritäten anpassen.

### Aufwand

- 1 Terminal-Befehl für Dateistatistiken (~30 Sekunden)
- 2-3 gezielte Datei-Reads für Evidenz (~2 Minuten)
- Ergebnis-Zusammenfassung (~5 Minuten)

**Gesamtaufwand: ~10 Minuten.** Verhindert Fehlpriorisierungen die Wochen kosten.

---

## Regel

> **Kein Workpaper mit Architektur-Empfehlungen darf geschlossen werden, ohne dass mindestens ein Theoretical Stress Test gegen echte Projektdaten durchgeführt wurde.**

---

## Entdeckte Core-Gaps (2026-04-17)

Diese Erkenntnisse betreffen den AAMS-Kern, nicht nur das Wiki-Thema:

### Gap 1: Decision-Kompoundierungs-Leck (KRITISCH)

**Problem:** Architektur-Decisions stehen in offenen Workpapers, werden aber nicht in Whitepapers reflektiert. Ein neuer Agent liest WP-001 und weiß nicht, dass „Spec → Contract" beschlossen wurde.

**Evidenz:** `2026-04-10-AAMS-STRAT` + `2026-04-10-AAMS-RFCT` — Option B angenommen, 5 Entscheidungen offen, WP-001 nicht aktualisiert.

**Impact:** Jeder neue Agent-Einstieg operiert auf veralteter Architektur-Wahrheit.

### Gap 2: Kein Lint / Health-Check

**Problem:** Kein Mechanismus erkennt verwaiste Whitepapers, stale LTM-Referenzen oder widersprüchliche Decisions.

**Kosten für Fix:** ~3k Tokens pro Durchlauf (bei aktuellem Scale). Vernachlässigbar.

### Gap 3: Fehlende Cross-Referenzen in Whitepapers

**Problem:** WP-001 bis WP-004 referenzieren sich nicht gegenseitig. Kein Agent kann Zusammenhänge zwischen Whitepapers navigieren ohne alle zu lesen.

**Kosten für Fix:** Zero extra — fällt in bestehende RFL-Lesephase.
