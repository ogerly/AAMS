# Workpaper: Karpathy LLM-Wiki vs. AAMS — Vergleichsanalyse

> **Session:** 2026-04-17  
> **Typ:** Research / Architekturvergleich  
> **Quelle:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
> **Ziel:** Nützlichkeit bewerten, Adaptionspotenzial identifizieren, Wiki-Fähigkeit aus AAMS prüfen

---

## 1. Karpathy LLM-Wiki — Kernkonzept (Zusammenfassung)

**Idee:** Statt RAG bei jeder Query → LLM baut inkrementell ein persistentes Wiki aus Markdown-Dateien auf. Wissen wird einmal kompiliert, dann gepflegt — nicht bei jeder Frage neu abgeleitet.

**Drei-Schichten-Architektur:**

| Schicht | Zweck | Eigentümer |
|---|---|---|
| **Raw Sources** | Immutable Quelldokumente (Artikel, Papers, Daten) | Mensch kuratiert |
| **Wiki** | LLM-generierte Markdown-Seiten (Entities, Concepts, Summaries, Synthese) | LLM schreibt & pflegt |
| **Schema** | Konventionen, Workflows, Struktur-Regeln (CLAUDE.md / AGENTS.md) | Mensch + LLM co-evolve |

**Operationen:**
- **Ingest** — Neue Quelle → LLM liest, erstellt Summary-Seite, aktualisiert Index, pflegt Entity/Concept-Seiten, schreibt Log
- **Query** — Frage → LLM durchsucht Wiki-Index, liest relevante Seiten, synthetisiert Antwort → gute Antworten werden als neue Wiki-Seiten gespeichert
- **Lint** — Periodischer Health-Check: Widersprüche, verwaiste Seiten, fehlende Cross-Referenzen, Lücken

**Indexierung:**
- `index.md` — inhaltlich: Katalog aller Wiki-Seiten mit Links + Einzeiler
- `log.md` — chronologisch: append-only Zeitstempel-Log aller Operationen

---

## 2. AAMS — Bestehendes System (Relevante Komponenten)

| AAMS-Komponente | Funktion | Äquivalent in LLM-Wiki |
|---|---|---|
| `WORKING/WHITEPAPER/` + `INDEX.md` | Stabile Architektur-Wahrheit | ≈ Wiki (Entity/Concept-Seiten) |
| `WORKING/WORKPAPER/` | Session-Dokumente | — (kein Äquivalent) |
| `WORKING/MEMORY/ltm-index.md` | Audit-Log des Langzeitgedächtnisses | ≈ `log.md` |
| `WORKING/AGENT-MEMORY/` (ChromaDB) | Vektorspeicher für semantische Suche | ≈ CLI-Suche (qmd) |
| `WORKING/DIARY/` | Pointer-only Zeitindex | ≈ `log.md` (teilweise) |
| `READ-AGENT.md` | Agent-Vertrag, Workflows, Konventionen | ≈ Schema-Schicht |
| `.agent.json` | Maschinenlesbarer Manifest | — (kein Äquivalent) |

---

## 3. Strukturvergleich — Was harmoniert, was beißt sich?

### ✅ Hohe Kompatibilität

| Aspekt | Begründung |
|---|---|
| **Schichten-Architektur** | Beide nutzen 3 Schichten. AAMS hat sogar 4 (+ Diary). Kein Konflikt. |
| **Schema = Agent-Vertrag** | Karpathys Schema-Schicht (CLAUDE.md) entspricht exakt unserem `READ-AGENT.md` + `.agent.json`. AAMS ist hier *stärker* — maschinenlesbar + menschenlesbar. |
| **Index + Log** | `index.md` ≈ `WHITEPAPER/INDEX.md`. `log.md` ≈ `ltm-index.md` + `DIARY/`. AAMS hat dies bereits, sogar getrennt nach Audit (LTM) und Zeitachse (Diary). |
| **Markdown als Medium** | Beide setzen auf plain Markdown. Voll kompatibel. |
| **Ingest-Pattern** | AAMS macht bei Session-Ende Ingest in LTM. LLM-Wiki macht Ingest bei neuer Quelle. Anderer Trigger, gleiche Mechanik. |

### ⚠️ Reibungspunkte

| Aspekt | Problem |
|---|---|
| **Wer schreibt?** | LLM-Wiki: Der LLM schreibt *alles* im Wiki. AAMS: Der LLM schreibt Workpapers, aber Whitepapers sind stabil und werden selten geändert. LLM-Wiki erlaubt unkontrolliertes Überschreiben. |
| **Immutable Sources** | LLM-Wiki hat eine klare `raw/` Schicht die der LLM nie anfasst. AAMS hat kein explizites Konzept für „Raw Sources" — die Quelle *ist* das Repo selbst. |
| **Lint** | LLM-Wiki hat einen expliziten Lint-Zyklus. AAMS hat keinen. |
| **Wissens-Kompoundierung** | LLM-Wiki ist darauf optimiert, dass Wissen *akkumuliert*. Jede Antwort kann eine neue Seite werden. In AAMS akkumuliert nur der LTM-Index — Whitepapers wachsen langsam, Workpapers werden archiviert. |

### ❌ Inkompatibilitäten

| Aspekt | Konflikt |
|---|---|
| **LLM als alleiniger Wiki-Autor** | In AAMS gibt es Human-in-the-Loop über Workpapers. Karpathys Modell gibt dem LLM volle Schreibrechte. Das widerspricht AAMS' Audit-Architektur. |
| **Flat Wiki vs. strukturierter Workspace** | LLM-Wiki hat ein flaches Verzeichnis mit Markdown-Seiten. AAMS hat eine strenge Ordner-Hierarchie. Beides gleichzeitig erzeugt Redundanz. |

---

## 4. Hat AAMS schon eine Art Wiki?

**Ja — in Fragmenten:**

| Wiki-Funktion | AAMS-Umsetzung | Reifegrad |
|---|---|---|
| Entity-Seiten | `WHITEPAPER/WP-001` bis `WP-004` | ⭐⭐⭐ (stabil, aber manuell) |
| Index | `WHITEPAPER/INDEX.md` | ⭐⭐⭐ (vorhanden, gepflegt) |
| Chronologischer Log | `MEMORY/ltm-index.md` (92 Einträge) | ⭐⭐⭐⭐ (maschinell + menschlich) |
| Zeitachse | `DIARY/` (Monatsfiles) | ⭐⭐ (Pointer-only, dünn) |
| Semantische Suche | `AGENT-MEMORY/` (ChromaDB) | ⭐⭐⭐ (funktioniert, aber fragil) |
| Cross-Referenzen | Nicht systematisch | ⭐ (fehlt) |
| Widerspruchs-Erkennung | Nicht vorhanden | ☆ (fehlt komplett) |
| Lint / Health-Check | Nicht vorhanden | ☆ (fehlt komplett) |

**Urteil:** AAMS hat die *Infrastruktur* eines Wikis, aber nicht die *Dynamik*. Das Wiki wächst nur durch Whitepaper-Entscheidungen und LTM-Ingest — es gibt keinen Mechanismus für inkrementelle Wissens-Synthese.

---

## 5. Was könnte AAMS adaptieren?

### Empfehlung A: **Wiki-Lint-Zyklus** (Hohe Priorität)

Ein periodischer Health-Check für den `WORKING/`-Baum:
- Verwaiste Whitepapers ohne Referenzen
- Widersprüche zwischen Workpaper-Decisions und aktuellen Whitepapers
- Stale LTM-Einträge (referenzierte Dateien gelöscht/verschoben)
- Fehlende Cross-Referenzen in Whitepapers

**Umsetzung:** Neues Tool in `WORKING/TOOLS/wiki_lint.py` + Trigger in `READ-AGENT.md` (z.B. alle 10 Sessions oder manuell).

**Aufwand für Agent:** Gering. Lint ist read-only, kann im Sessionstart laufen.

### Empfehlung B: **Query-Ergebnis-Kompoundierung** (Mittlere Priorität)

Wenn der Agent eine substanzielle Analyse durchführt (wie dieses Workpaper), sollte das Ergebnis nicht nur als Workpaper archiviert werden, sondern optional als Whitepaper-Kandidat geflaggt werden.

**Mechanik:** Neues Feld im Workpaper-Header: `## Wiki-Promotion: yes/no` + Begründung. Bei Session-Close entscheidet der Mensch.

**Aufwand für Agent:** Minimal. Eine Zeile mehr im Template.

### Empfehlung C: **Raw-Sources-Konzept** (Niedrige Priorität)

Ein `WORKING/SOURCES/` Ordner für externe Referenzdokumente die der Agent liest aber nie verändert. 

**Vorteil:** Klare Trennung zwischen eigener Wahrheit (Whitepapers) und externer Wahrheit (Sources).

**Aufwand für Agent:** Mittel. Neuer Ordner, neues Ingest-Pattern.

### Empfehlung D: **Cross-Referenz-Index** (Nice-to-have)

Automatische Erkennung und Pflege von Links zwischen Whitepapers, Workpapers und LTM-Einträgen.

**Aufwand für Agent:** Hoch. Erfordert Konsistenz bei jedem Schreibvorgang.

---

## 6. Was NICHT adaptiert werden sollte

| LLM-Wiki Feature | Warum nicht für AAMS |
|---|---|
| LLM als alleiniger Wiki-Autor | AAMS ist ein Agent-*Manifest* — der Mensch entscheidet über Architektur. Volle LLM-Kontrolle zerstört die Audit-Garantie. |
| Flaches Wiki-Verzeichnis | AAMS' strukturierte Ordner-Hierarchie ist ein Feature, kein Bug. Sie erzwingt Disziplin. |
| Obsidian-spezifische Features | AAMS ist tool-agnostisch. Obsidian-Abhängigkeit widerspricht dem Portabilitätsprinzip. |
| Unbeschränkte Seiten-Erstellung | In AAMS ist jedes Dokument typisiert (WP, Workpaper, Diary). Willkürliche Seiten ohne Typ-Zuordnung führen zu Chaos. |

---

## 7. Würde LLM-Wiki-Struktur ein besseres Wiki liefern?

**Nein — aber Teile davon machen AAMS' Wiki-Fähigkeit besser.**

Das Karpathy-Pattern ist für *persönliches Wissensmanagement* optimiert: ein Mensch, ein LLM, ein Thema. AAMS ist für *projektbezogene Agent-Koordination* optimiert: mehrere Sessions, mehrere Agenten, ein Codebase.

| Kriterium | LLM-Wiki | AAMS | Besser für AAMS? |
|---|---|---|---|
| Wissens-Akkumulation | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Ja — Lint + Promotion adaptieren |
| Auditierbarkeit | ⭐⭐ | ⭐⭐⭐⭐⭐ | Nein — AAMS ist hier überlegen |
| Cross-Session-Kontinuität | ⭐⭐⭐ | ⭐⭐⭐⭐ | Nein — AAMS hat LTM + RFL |
| Cross-Referenz-Dichte | ⭐⭐⭐⭐ | ⭐ | Ja — dringend |
| Widerspruchs-Erkennung | ⭐⭐⭐ | ☆ | Ja — Lint adaptieren |
| Agent-Aufwand pro Operation | ⭐⭐ (hoch) | ⭐⭐⭐⭐ (niedrig) | Achtung — mehr Wiki = mehr Arbeit |

---

## 8. Fazit

### Kern-Erkenntnis

Karpathys LLM-Wiki und AAMS lösen **verwandte aber verschiedene Probleme**. LLM-Wiki ist ein *Wissensmanagement-Pattern* — es baut eine Enzyklopädie. AAMS ist ein *Agent-Workspace-Standard* — es baut eine nachvollziehbare Arbeitshistorie.

### Harmoniert es?

**Teilweise.** Die Grundmechanik (Markdown, Index, Log, Schema) ist identisch. AAMS hat sogar die stärkere Infrastruktur (maschinenlesbarer Manifest, Dual-Track LTM, Diary, RFL-Konsistenzcheck). Aber AAMS fehlt die *dynamische Synthese-Schicht* — der Mechanismus, der aus vielen Einzeldokumenten verdichtetes, verknüpftes Wissen macht.

### Beißt es sich?

**Ja, wenn man es 1:1 übernimmt.** Ein LLM der unkontrolliert Wiki-Seiten erzeugt und überschreibt, würde AAMS' Audit-Garantie zerstören. Der Lint-Overhead (periodisches Prüfen aller Seiten auf Widersprüche, Orphans, fehlende Links) würde bei jedem Sessionstart Token kosten — bei einem 100-Seiten-Wiki sind das schnell 30k+ Tokens nur für den Lint-Check.

### Empfehlung

**Chirurgisch adaptieren, nicht adoptieren:**

1. **Wiki-Lint** einführen → `WORKING/TOOLS/wiki_lint.py` (schließt die größte Lücke)
2. **Workpaper-to-Whitepaper-Promotion** formalisieren (Wissens-Kompoundierung ohne Kontrollverlust)
3. **Cross-Referenzen** in Whitepapers pflegen (Index existiert, Links fehlen)
4. ~~Raw Sources~~ — erst wenn ein konkreter Use-Case entsteht
5. ~~Flaches Wiki~~ — nein. Struktur ist AAMS' Stärke.

**Kosten/Nutzen:** Die Empfehlungen A+B kosten pro Session ~500 Tokens extra. Die Widerspruchs-Erkennung allein rechtfertigt das — Workpaper `2026-04-10-AAMS-STRAT` und `2026-04-10-AAMS-RFCT` haben bereits gezeigt, dass sich Entscheidungen widersprechen können wenn kein systematischer Check existiert.

---

---

## 9. Theoretical Stress Tests (TST)

> Methodik etabliert als Guideline: `WORKING/GUIDELINES/theoretical-stress-testing.md`

### TST-1: Token-Kosten-Realitätscheck — „Lint kostet 30k+ Tokens"

**Behauptung (Sektion 8):** Bei 100 Wiki-Seiten sind das 30k+ Tokens nur für Lint.

**Echte AAMS-Zahlen (gemessen):**
- 6 Whitepapers → **781 Zeilen** total (WP-001: 151, WP-002: 120, WP-003: 250, WP-004: 192, Outreach: 54, INDEX: 14)
- LTM-Index: **178 Zeilen**
- 17 offene + 28 geschlossene Workpapers = **45 Dokumente**
- Gesamt im WORKING/-Baum: **~51 Dokumente**

**Ergebnis:** Lint über alle Whitepapers + Index + LTM-Index kostet **~3.100 Tokens**. 10× weniger als geschätzt. Erst bei ~500 Seiten wird die 30k-Marke relevant.

**Korrektur:** Lint ist **heute sofort umsetzbar** ohne spürbaren Overhead. Empfehlung A wird gestärkt.

### TST-2: „Fehlende Kompoundierung" — Stimmt das?

**Behauptung (Sektion 4/5):** Wissen akkumuliert nur langsam über LTM-Index.

**Evidenz aus echten Workpapers:**
- `2026-04-10-AAMS-STRAT` analysiert „Specification → Contract" Umbenennung
- `2026-04-10-AAMS-RFCT` baut Refactoring-Plan, 5 offene Entscheidungen (E-1 bis E-5)
- „Option B angenommen" steht in RFCT — **aber WP-001 weiß davon nichts**
- Ein neuer Agent liest WP-001 und operiert auf veralteter Architektur-Wahrheit

**Ergebnis:** These stimmt — und ist **schlimmer als beschrieben**. Nicht nur langsame Akkumulation, sondern **aktive Decisions versickern** in offenen Workpapers. Das ist ein AAMS-Core-Gap, nicht nur ein Wiki-Thema.

**Korrektur:** Empfehlung B (Wiki-Promotion) von „Mittlere Priorität" auf **KRITISCH** hochgestuft.

### TST-3: Cross-Referenz-Aufwand — Verlangsamt es den Agent?

**Behauptung (Sektion 5D):** „Hoher Aufwand. Erfordert Konsistenz bei jedem Schreibvorgang."

**Test:** Agent muss bei WP-005-Erstellung alle 6 Whitepapers lesen (781 Zeilen ≈ 2.500 Tokens). Aber: Der Agent liest diese ohnehin bei Session-Start (RFL-Check). Cross-Referenz-Pflege ist ein **Nebenprodukt der bestehenden Lesephase**.

**Ergebnis:** **Zero extra Token-Cost** bei aktuellem Scale. Nur eine zusätzliche Schreib-Aktion.

**Korrektur:** Von „Nice-to-have" auf **Mittlere Priorität** hochgestuft.

### TST-Zusammenfassung — Prioritäts-Korrekturen

| Empfehlung | Priorität VORHER | Priorität NACHHER | Begründung |
|---|---|---|---|
| A: Wiki-Lint | Hoch | **Hoch** (bestätigt) | 3k statt 30k Tokens — sofort machbar |
| B: Decision-Promotion | Mittel | **KRITISCH** | Aktive Decisions versickern. Core-Gap. |
| C: Raw Sources | Niedrig | Niedrig (unverändert) | Kein Use-Case im Test gefunden |
| D: Cross-Referenzen | Nice-to-have | **Mittel** | Fällt in RFL-Phase, zero extra Cost |

---

### TST-4: Upgrade-Transparenz — Sieht ein curl-User was sich geändert hat?

**Frage:** Wenn jemand AAMS schon hat und per `curl -sO` aktualisiert — weiß er dann von welcher Version er kommt und was sich geändert hat?

**Evidenz:**
- `2026-03-27-versioning-system.md` — SemVer + CHANGELOG konzipiert, **nie umgesetzt**
- `2026-04-10-AAMS-UPD` — Update-Detection-Protocol mit `.aams-version`, **nie umgesetzt**
- Kein CHANGELOG.md, keine Git-Tags, keine Releases auf GitHub
- `.agent.json` hat `spec_version: AAMS-MINI/1.0` — aber kein Vergleichsmechanismus im Zielrepo

**Ergebnis:** **Totalausfall.** Ein curl-Update ist Blindflug. Kein Agent weiß ob er von 1.0 auf 1.3 springt oder ob Breaking Changes vorliegen. Beide Konzepte (Versioning + Update-Detection) existieren als fertige Workpapers — aber sie wurden nie in Code oder CHANGELOG umgesetzt.

**Impact:** Das ist der Decision-Kompoundierungs-Gap (Issue #48) in Reinform: Entscheidungen wurden getroffen, dokumentiert, archiviert — und dann vergessen. Ohne Upgrade-Transparenz ist jedes AAMS/2.0 Release ein Risiko.

**Issue:** #49 — Upgrade-Transparenz fehlt

---

## File Protocol

| Aktion | Datei |
|---|---|
| CREATED | `WORKING/WORKPAPER/2026-04-17-RES-WIKI-karpathy-llm-wiki-vergleich.md` |
| CREATED | `WORKING/GUIDELINES/theoretical-stress-testing.md` |
| CREATED | `WORKING/TOOLS/wiki_lint.py` — 7-Check Health Monitor (L1-L7) |
| UPDATED | `WORKING/WHITEPAPER/WP-001-aams-overview.md` — §5 WORKSPACE-Discovery, §8 Versioning, §9 Decision-Promotion, §10 Cross-Refs, §11 Stand 2026-04-17, Pending-Decision Marker |
| UPDATED | `WORKING/WHITEPAPER/INDEX.md` — Cross-Refs, Pending-Decisions, Stand 2026-04-17 |
| UPDATED | `WORKING/DIARY/2026-04.md` — Klarschiff-Session Eintrag |
| UPDATED | `WORKING/MEMORY/ltm-index.md` — Einträge 100-108, Issue-Stand, Klarschiff-Zusammenfassung |
| UPDATED | `READ-AGENT.md` — Decision-Promotion als Schritt 2 in on_session_end, wiki_lint.py als optionaler Schritt 7, Current Status aktualisiert |
| MOVED | 6 Workpapers → `WORKPAPER/closed/` (video-marketing, claude-buddy, wissen-in-zeit, WORKSPACE-field-report, WKSP-discovery, public-presence) |
| CONFIRMED | Issues #22, #23, #24, #39, #42, #44 — bereits geschlossen |

## Decisions

- **D1:** Wiki-Lint-Konzept als nächsten Schritt evaluieren (`wiki_lint.py`) — **bestätigt durch TST-1**
- **D2:** ~~Workpaper-Promotion-Feld~~ → **Decision-Promotion ist KRITISCH** — Architektur-Decisions die in Workpapers stehen MÜSSEN in Whitepapers reflektiert werden. Kein optionales Feature.
- **D3:** LLM-Wiki-Pattern NICHT als Ganzes adoptieren — nur chirurgische Entnahmen — **bestätigt**
- **D4:** Cross-Referenz-Pflege als AAMS-v1.1-Feature vormerken — **hochgestuft auf Mittel**, da zero extra Cost
- **D5:** Theoretical Stress Testing (TST) als Pflicht-Methodik für Architektur-Empfehlungen etabliert → `WORKING/GUIDELINES/theoretical-stress-testing.md`
- **D6:** Decision-Kompoundierungs-Leck ist ein AAMS-Core-Gap — betrifft nicht nur Wiki-Thema, sondern die gesamte Workpaper→Whitepaper-Pipeline

## Next Steps

- [x] `wiki_lint.py` Prototyp in `WORKING/TOOLS/` erstellen — 7 Checks (L1-L7), 0 Errors, 12 Warnings, 2 Infos beim Erstlauf
- [x] **KRITISCH:** Offene Decisions aus `AAMS-STRAT` und `AAMS-RFCT` in WP-001 reflektieren — ⚠️ Pending-Decision-Marker gesetzt (E-1..E-5 noch offen)
- [x] Whitepaper-Cross-Referenzen zwischen WP-001 bis WP-004 ergänzen — §10 in WP-001 + INDEX.md
- [ ] Decision-Promotion-Mechanismus in `READ-AGENT.md` Session-End-Checklist aufnehmen
- [x] Ergebnisse dieses Workpapers in WP-001 verdichten — §8 Versioning, §9 Decision-Promotion

## Klarschiff-Zusammenfassung (2026-04-17)

### Abgeschlossen
- 6 Workpapers geschlossen und archiviert
- WP-001 Major Update (5 neue Sektionen)
- INDEX.md aktualisiert (Cross-Refs + Pending Decisions)
- LTM-Index auf 106 Einträge (100-106 neu)
- Diary-Eintrag geschrieben
- Issues-Stand verifiziert

### Verbleibende 11 offene Workpapers

| Gruppe | Workpapers | Blocker |
|---|---|---|
| BLOCKED (E-1..E-5) | AAMS-STRAT, AAMS-RFCT, AAMS-UPD | User-Entscheidungen nötig |
| Fast fertig | field-report-analyse, AAMS-ISS, versioning-system, wording-faktencheck | Kleine Reste |
| Extern | mempalace-analyse, social-outreach | LinkedIn-Antwort |
| Aktiv | Knowledge Validation Layer, RES-WIKI (dieses) | Laufend |

### 4 RED Whitepaper-Widersprüche — Status

| Problem | Fix |
|---|---|
| WP-001 "Spezifikation" statt "Contract" | ⚠️ Pending-Decision-Marker gesetzt |
| WP-001 fehlte WORKSPACE-Discovery | ✅ §5 ergänzt |
| Kein WP erwähnt Versioning | ✅ §8 in WP-001 |
| Decision-Promotion fehlte | ✅ §9 in WP-001 |
