# WP-2026-07-08-INDEX-DATEIEN-FUER-WHITEPAPER-UND-WORKPAPER

## session_goal

INDEX.md-Dateien fuer WHITEPAPER/ und WORKPAPER/ anlegen + Schema definieren + `.agent.json` on_update erweitern fuer automatische Index-Erstellung.

## repository_inventory

### WHITEPAPER/
- `INDEX.md` ✅ existiert (48 Zeilen, gut strukturiert)
- 11 Whitepapers (WH-001..WH-011)

### WORKPAPER/
- `INDEX.md` ❌ fehlt
- 8 offene Workpapers
- `closed/` ✅ existiert
- `observe/` ✅ existiert

### MEMORY/
- `ltm-index.md` ✅ existiert

### DIARY/
- Monthly files ✅ existieren

## key_findings

### 1. WHITEPAPER/INDEX.md — existiert, Schema analysiert

**Aktuelles Schema (WHITEPAPER/INDEX.md):**

| Spalte | Inhalt |
|--------|--------|
| `#` | Whitepaper-Nummer (WH-001) |
| `Datei` | Link zur Datei |
| `Thema` | Kurzbeschreibung des Inhalts |
| `Stand` | Erstellungsdatum |
| `Status` | Aktiv / Archiviert |

**Zusaetzliche Sektionen:**
- Cross-Referenzen (merkt Whitepaper zueinander)
- Offene Widersprueche / Pending Decisions (Bereich, Status, Tracking)

### 2. WORKPAPER/INDEX.md — muss angelegt werden

**Vorschlag Schema:**

| Spalte | Inhalt |
|--------|--------|
| `#` | Workpaper-Nummer (WP-NNN) |
| `Datei` | Link zur Datei |
| `Datum` | Erstellungsdatum |
| `TOPIC` | Topic-Tag (ARCH, SPEC, LTM, etc.) |
| `Thema` | Kurzbeschreibung (1-2 Zeilen) |
| `Status` | offen / observe / closed |
| `Naechstes` | Offene To-Dos / naechste Schritte |

### 3. `.agent.json` — on_update erweitern

**Neue on_update-Schritte:**
- Prüfen ob WHITEPAPER/INDEX.md existiert → falls nicht, erstellen + bestehende Whitepapers indexieren
- Prüfen ob WORKPAPER/INDEX.md existiert → falls nicht, erstellen + bestehende Workpapers indexieren
- Bei neuem Whitepaper/Workpaper: INDEX.md aktualisieren
- Max 5 offene Workpapers prüfen → bei Ueberschreitung: Warnung

### 4. Max 5 offene Workpapers

**Regel:**
- Wenn mehr als 5 Workpapers offen → neuer Workpaper-Erstellung blockieren oder warnen
- Alte Workpapers auf `observe` setzen oder nach `closed/` verschieben

### 5. Observer-Pattern

**Konzept:**
- Kontinuierliche Beobachtung statt manueller Abfrage
- WORKPAPER/observe/ als Zwischenzustand
- Observer prueft automatisch:
  - Gibt es INDEX.md? Falls nicht → erstellen
  - Sind alle Whitepapers im INDEX? Falls nein → aktualisieren
  - Mehr als 5 offene Workpapers? Falls ja → warnen
  - Closed Workpapers noch im INDEX? Falls nein → entfernen oder markieren

## file_protocol

### Neue Dateien
- `WORKING/WORKPAPER/INDEX.md` — Workpaper-Index (Schema s.u.)
- `WORKING/WHITEPAPER/INDEX.md` — existiert bereits, bleibt unveraendert

### Geaenderte Dateien
- `.agent.json` — `on_update` erweitern (INDEX-Erstellung + Maintenance)
- `READ-AGENT.md` — INDEX-Pflege-Konventionen dokumentieren

### Schema WORKPAPER/INDEX.md

```markdown
# Workpaper Index

| # | Datei | Datum | TOPIC | Thema | Status | Nächstes |
|---|---|---|---|---|---|---|
| WP-001 | [WP-2026-07-08-xxx.md](./WP-2026-07-08-xxx.md) | 2026-07-08 | ARCH | Beschreibung | offen | Next Step |
```

**Status-Werte:** `offen`, `observe`, `closed`

**Max 5 offene Workpapers** — bei Ueberschreitung: Warnung + Vorschlag zum Schliessen

## decisions

1. **WHITEPAPER/INDEX.md bleibt wie sie ist** — Schema ist gut, wird nicht geaendert
2. **WORKPAPER/INDEX.md wird neu angelegt** — Schema analog WHITEPAPER, aber mit Status-Spalte
3. **`.agent.json` on_update erweitert** — automatische INDEX-Erstellung und Maintenance
4. **Max 5 offene Workpapers** — als Konvention in `.agent.json` dokumentiert
5. **Observer-Pattern** — automatische INDEX-Pflege statt manueller Abfrage

## next_steps

1. ✅ WORKPAPER/INDEX.md anlegen
2. ✅ `.agent.json` on_update erweitern
3. ✅ READ-AGENT.md INDEX-Pflege-Konventionen ergaenzen
4. ❌ Committen
5. ❌ Release hochsetzen
6. ❌ AAMS on_update im eigenen Repo ausfuehren
7. ❌ Workpaper-Status pruefen (Max-5-Regel)
8. ❌ Offene Workpapers pruefen — Schliessen anbieten

---

## Session-Ende: AAMS on_update im eigenen Repo

### Auszufuehrende Schritte (s.u.)

1. **INDEX-Pflege:** WHITEPAPER/INDEX.md und WORKPAPER/INDEX.md pruefen
2. **Workpaper-Check:** Max-5-Regel pruefen, offene Papers auflisten
3. **Schliessen-Angebot:** Fuer jedes Paper: Grossteil erledigt? → Schliessen anbieten
4. **Release-Check:** Aendert sich etwas am Contract? → Release hochsetzen
5. **Committen:** Alles commiten
