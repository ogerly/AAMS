# AAMS Upgrade-Anleitung

## Für Consumer-Repos — AAMS upgraden

### Automatischer Upgrade-Befehl (empfohlen)

Gib diesen Prompt an deinen KI-Agenten:

```
Upgrade AAMS in diesem Repo. Führe folgende Schritte aus:

1. VERSION-CHECK: Lies `.aams-version` und vergleiche `installed_version` mit Remote `https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json` → `_contract`
2. WENN Version unterschiedlich:
   a. **Backup:** Kopiere `.agent.json` nach `.agent.json.bak`
   b. **Lade Remote:** `curl -sO https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json`
   c. **Merge:** Vergleiche `.agent.json.bak` mit neuer `.agent.json` — behalte lokale Anpassungen (z.B. identity, runtime, permissions)
   d. Lies CHANGELOG.md von AAMS (Remote: `https://raw.githubusercontent.com/ogerly/AAMS/main/CHANGELOG.md`)
   c. Finde den Abschnitt für die neue Version
   d. Parse "Added" und "Changed" Sektionen für neue workspace.structure-Pfade
   e. MIGRATE: Erstelle alle neuen Pfade in WORKING/ z.B. `WORKING/TOOLS/skills/`, `WORKING/WORKPAPER/observe/`
   f. MIGRATE: Wende neue Konventionen an (Skills-Struktur, tool_detection, etc.)
   g. MIGRATE: Prüfe ob "Removed" Dateien im lokalen Repo existieren — flagge zur Review (kein Auto-Delete)
   h. Aktualisiere `.aams-version`:
      - `installed_version` = neue `_contract` aus `.agent.json`
      - `installed_date` = heute (YYYY-MM-DD)
      - `last_update` = heute
   i. Aktualisiere `_version_date` in `.agent.json` = heute (YYYY-MM-DD)
   j. Schreibe Migration-Log in `DIARY/{YYYY-MM-DD}.md`
   k. **FEEDBACK:** Erstelle anonymisierten Upgrade-Report als GitHub Issue an `ogerly/AAMS` (wenn `GITHUB_TOKEN` in `.env` vorhanden):
      - Titel: `AAMS Upgrade Report — {OLD_VERSION} → {NEW_VERSION}`
      - Body: Version, Datum, migrierte Pfade, angewendete Konventionen, geflaggte Removed-Dateien, Probleme
      - **Anonymisiert:** Kein Repo-Name, keine Secrets, keine Tokens, keine persönlichen Daten
      - Maskierung: `ghp_*`, `gho_*`, `ghs_*`, `*.key`, `*.pem` → `[REDACTED]`
   l. Lösche `.agent.json.bak` nach erfolgreichem Merge
3. WENN keine neue Version: nichts tun

Berichte was passiert ist.
```

### Manuelles Upgrade (wenn Agent nicht migrieren kann)

```bash
# 1. Remote Version prüfen
curl -s https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json | grep '"_contract"'

# 2. Lokale Version prüfen
cat .aams-version | grep 'installed_version'

# 3. Wenn unterschiedlich — Upgrade:
# Backup vor Überschreiben!
cp .agent.json .agent.json.bak
curl -sO https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json
# Diff vergleichen: diff .agent.json.bak .agent.json
# Lokale Anpassungen aus .agent.json.bak übernehmen

# 4. CHANGELOG prüfen für neue Konventionen
curl -s https://raw.githubusercontent.com/ogerly/AAMS/main/CHANGELOG.md | head -100

# 5. Neue Pfade manuell erstellen falls nötig
mkdir -p WORKING/TOOLS/skills
mkdir -p WORKING/WORKPAPER/observe

# 6. .aams-version aktualisieren
# installed_version → neue Version aus .agent.json
# installed_date → heute
# last_update → heute
```

### Wichtige Hinweise

- **Kein `git pull`** — AAMS wird per `curl` bezogen, nicht geklont
- **Kein Auto-Delete** — "Removed" Dateien werden nur flaggt, nicht gelöscht
- **Migration wird geloggt** — Alle Änderungen in `DIARY/{YYYY-MM-DD}.md`
- **`.env` nicht überschreiben** — `.agent.json` enthält keine Secrets
- **`.agent.json.bak` nach Merge löschen** — nur so lange zum Vergleichen nötig
- **FEEDBACK optional** — anonymisierter Report nur wenn `GITHUB_TOKEN` vorhanden
- **`WORKING/` nicht löschen** — nur neue Pfade erstellen
- **Keine Secrets im Feedback** — Pattern-Maskierung für alle Token-Typen

### Troubleshooting

**Agent hat nur `.agent.json` aktualisiert, aber keine Migration durchgeführt:**
- Der alte `on_update`-Contract (vor 2.3.1) migrierte nur Versionsnummern
- Manuell nachholen: Neue Pfade aus CHANGELOG erstellen
- Siehe `CHANGELOG.md` → Abschnitt "MIGRATE"

**Versions-Detection funktioniert nicht:**
- Prüfe: `cat .aams-version` vs `grep _contract .agent.json`
- `version_detection` vergleicht `_contract` UND `_version_date`
- Bei Diskrepanz → `on_update` muss ausgeführt werden
