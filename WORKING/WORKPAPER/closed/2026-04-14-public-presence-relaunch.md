# WP — Public Presence Relaunch

| Feld           | Wert                                        |
|----------------|---------------------------------------------|
| Datum          | 2026-04-14                                  |
| Status         | DONE                                        |
| Autor          | Agent (Copilot / Claude Opus 4.6)           |
| Scope          | README, GitHub Pages, i18n, Showcase        |

---

## 1. Ausgangslage

### Ist-Zustand
- **README.md**: Englisch, enthält deutsche Bilder (`aams-das-kochbuch-fuer-dein-repro.jpg`), Kochbuch-Analogie auf Deutsch
- **reference/README-DE.md**: Existiert, aber veraltet und nicht verlinkt
- **GitHub Pages** (`docs/index.html`): Einsprachig, kein Sprachschalter
- **Grafiken**: Teils deutsch beschriftet → nicht für EN/CN geeignet
- **Kein Showcase**: Keine Liste von Projekten die AAMS einsetzen
- **Kein Community-Beitrag**: Keine Möglichkeit für GitHub-User, ihr Projekt einzutragen

### Probleme
1. Sprachmix: README englisch, Bilder deutsch, keine klare Sprachstrategie
2. Kein mehrsprachiger Auftritt (DE als Standard fehlt de facto)
3. Kein sozialer Beweis (Social Proof) durch Showcase
4. Grafiken mit deutscher Schrift auf internationalen Seiten
5. Die Flowchart-Loop / AAMS-Architektur-Grafiken (EN) sind besser geeignet

---

## 2. Zielzustand

### Sprachstrategie
- **Standardsprache: Deutsch** (README.md = DE)
- **Englisch**: README.en.md + docs/en/
- **Chinesisch**: README.zh.md + docs/zh/
- Sprachschalter oben in jeder README und auf GitHub Pages

### Devise
> **Every agent. One file.**

### Grafiken
- Die beiden angehängten AAMS-Workflow-Grafiken (EN + DE) als primäre Visualisierung
- EN-Grafik für englische Seiten
- DE-Grafik für deutsche Seiten
- CN: EN-Grafik + chinesische Beschriftungs-Legende (oder spätere Übersetzung)

### Kochbuch-Analogie (international einsetzbar)
- Das Kochbuch der Großmutter: charmant, universell verständlich
- **ABER**: AAMS ≠ chaotisches Kochbuch → AAMS ist der **disziplinierte Weg**
- Framing: "Stell dir vor, Großmutters Kochbuch hätte ein Inhaltsverzeichnis, Querverweise und eine Suchfunktion gehabt."
- International: "Grandmother's cookbook" / "奶奶的食谱" — die Analogie funktioniert kulturübergreifend

### Flowchart-Loop Konzept (aus flowchart-loop.txt)
Kernaussagen für die öffentliche Kommunikation:
- AAMS ist **kein Agent-Framework** — es ist ein **strukturierter Kontext- und Entscheidungs-Compiler für Agents**
- Der Mensch definiert Struktur, Regeln, Kontext → der Agent ist deterministischer Arbeiter
- Memory entsteht nicht implizit — Memory = aggregierte, nachvollziehbare Historie
- Closed-Loop: Output → Dokumentation → Entscheidung → Memory → neuer Kontext

### Showcase / Community
- Datei: `SHOWCASE.md` im Repo-Root
- Struktur: Tabelle mit Projekt, Link, Statement, Einsatz-Typ
- Beiträge via Pull Request (einfache Anleitung)
- Alternativ: GitHub Discussions als Kanal

---

## 3. Umsetzungsplan

### Phase 1: README-Restrukturierung ✅
- [x] README.md → Deutsche Hauptversion (getauscht 2026-04-15)
- [x] README.en.md → Englische Version
- [x] README.zh.md → Chinesische Version (maschinell generiert)
- [x] Sprachnavigation oben in jeder Datei
- [x] AAMS-Workflow-Grafiken statt deutsche Kochbuch-Bilder auf EN/CN

### Phase 2: GitHub Pages ✅
- [x] Sprachschalter auf index.html (DE/EN/中文)
- [x] docs/index.html komplett auf Deutsch umgebaut
- [x] docs/en/index.html erstellt
- [x] docs/zh/index.html erstellt
- [x] Konsistente Grafiken pro Sprache (EN-Grafiken für EN/CN)

### Phase 3: Showcase ✅
- [x] SHOWCASE.md mit 7 Projekten + realen Beschreibungen
- [x] Anleitung für Community-Beiträge
- [x] Link in README + Pages
- [x] Showcase-Tabelle in allen 3 GitHub Pages Versionen

### Phase 4: Verfeinerung ✅
- [x] Kochbuch-Analogie international ausgearbeitet (EN: grandmother's cookbook, CN: 奶奶的食谱)
- [x] Flowchart-Loop in "AAMS ist kein Framework"-Sektion integriert
- [x] CN-Grafiken: aams-function-img.png ist sprachunabhängig — verwendet

### Phase 5: Neues Design + Zentrales Bild + Aufräumen ✅
- [x] Dark-Theme Design implementiert (Oswald/JetBrains Mono, Amber/Cyan)
- [x] docs/index.html (DE), docs/en/index.html, docs/zh/index.html neu gestaltet
- [x] Sprachschalter in allen drei Seiten
- [x] aams-function-img.png als zentrales Funktionsdiagramm in allen 3 Pages integriert
- [x] aams-function-img.png in README.md, README.en.md, README.zh.md eingepflegt
- [x] docs/_archive/ angelegt — nicht verwendete Assets verschoben (14 Dateien)
- [x] docs/_archive/ ins .gitignore aufgenommen

---

## 4. Entscheidungen

| #  | Entscheidung                                                    | Begründung                                      |
|----|----------------------------------------------------------------|------------------------------------------------|
| D1 | DE als README.md Standardsprache                               | Projektsprache ist Deutsch                      |
| D2 | EN/CN als separate Dateien (nicht Ordner)                      | GitHub zeigt README.md automatisch an           |
| D3 | Sprachspezifische Grafiken statt universelle                   | Keine Schrift-auf-Bild-Übersetzung nötig        |
| D4 | SHOWCASE.md statt externe Plattform                            | Im Repo = direkt sichtbar, via PR beitragbar    |
| D5 | Kochbuch-Analogie beibehalten, aber diszipliniert framen       | International verständlich, aber AAMS-würdig    |
| D6 | Flowchart als "AAMS ist kein Framework"-Kommunikation          | Klarstellt was AAMS wirklich ist                |
| D7 | CN-Version maschinell erstellen                                | Effizienz, kann später manuell verfeinert werden |
| D8 | Workflow-Grafiken NICHT ins docs/ — eigenständig halten        | Einfach und simpel, kein Grafik-Overhead        |
| D9 | Showcase-Liste in GitHub Pages einbinden (devmatrose.github.io/AAMS/) | Zentrale Anlaufstelle für Social Proof   |

---

## 5. Dateien

### Erstellt
- `README.en.md` — Englische README mit Sprachschalter
- `README.zh.md` — Chinesische README (maschinell generiert)
- `SHOWCASE.md` — Showcase mit 7 Projekten + Community-Anleitung
- `docs/en/index.html` — Englische GitHub Pages
- `docs/zh/index.html` — Chinesische GitHub Pages
- `README.backup.md` — Backup der ursprünglichen englischen README
- `docs/aams-function-img.png` — Zentrales Funktionsdiagramm (sprachunabhängig)
- `docs/_archive/` — Archivordner für nicht mehr verwendete Assets

### Geändert
- `README.md` — Ersetzt durch deutsche Version (vorher englisch); Bild auf aams-function-img.png aktualisiert
- `README.en.md` — Bild auf aams-function-img.png aktualisiert
- `README.zh.md` — Bild auf aams-function-img.png aktualisiert
- `docs/index.html` — Komplett neu: Dark-Theme, Animationen, Sprachschalter, aams-function-img.png
- `.gitignore` — docs/_archive/ hinzugefügt

---

## 6. Nächste Schritte
- Phase 1 sofort umsetzen (README-Restrukturierung)
- SHOWCASE.md anlegen
- GitHub Pages in Phase 2

---

## 7. Erkenntnisse & Entscheidungen (Update)

### AAMS-Showcase = eigenes Repo
- URL: https://github.com/DEVmatrose/AAMS-Showcase
- Ist selbst ein AAMS-Projekt (dogfooding)
- Dient als drittes reales Testprojekt neben AAMS und MantisClaw
- SHOWCASE.md im AAMS-Haupt-Repo verlinkt dorthin

### Reale AAMS-Projekte
| # | Projekt | Rolle | Status |
|---|---------|-------|--------|
| 1 | AAMS | Die Spezifikation selbst | öffentlich |
| 2 | [MantisClaw](https://github.com/DEVmatrose/MantisClaw) | Agent-Loop-Framework mit emergenter Identität, AAMS als Körper | öffentlich |
| 3 | [MantisNostr](https://github.com/DEVmatrose/MantisNostr) | Mesh-Netzwerk für autonome Agenten über Nostr | noch nicht öffentlich |
| 4 | [Mantis-OS](https://github.com/DEVmatrose/Mantis-OS) | Autonomes Agenten-Betriebssystem (MantisClaw + MantisNostr) | noch nicht öffentlich |
| 5 | [pax](https://github.com/ogerly/pax) | PAX Festival 2026 One-Pager, Agent-Workflow | öffentlich |
| 6 | [Ocelot-Social-aams](https://github.com/ogerly/Ocelot-Social-aams) | AAMS-Fork: 9 Whitepapers, Upgrade-Simulator, Zero-Code-Analyse | öffentlich |
| 7 | [druid](https://github.com/ogerly/druid) | Keltische Entdecker-App mit Karte, POIs, GPS-Tracking | öffentlich |

### Nächster Schritt: AAMS-Showcase Repo aufsetzen
- `.agent.json` ins neue Repo
- Agent bootstrappen lassen
- Showcase-Portal als AAMS-Projekt aufbauen (Selbsttest)

## 8. Entschiedene Fragen
- ✅ CN-Version: maschinell erstellt (README.zh.md liegt bereits vor)
- ✅ AAMS-Workflow-Grafiken: **nicht** ins docs/ — eigenständig, einfach, simpel halten
- ✅ Showcase-Liste wird später in die GitHub Pages eingebunden (https://devmatrose.github.io/AAMS/)
- ✅ MantisClaw: Statement für Showcase-Eintrag ergänzt (*„AAMS gibt dem Agent einen Körper. MantisClaw gibt ihm ein Gehirn."*)
