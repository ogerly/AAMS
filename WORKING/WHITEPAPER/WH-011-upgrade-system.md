# WH-011: Upgrade-System — Versions-Detection, Migration und Feedback-Loop

**Datum:** 2026-07-08  
**Status:** Aktiv  
**Referenz:** Issue #49 (Upgrade-Transparenz), CHANGELOG v2.3.1 + v2.3.2

---

## Problem

AAMS-Consumer-Repos konnten keine Upgrades korrekt durchführen:

1. **Update-Detection kaputt** — `_contract` war immer `AAMS/2.0`, Consumer-Repos merkten nie ein Upgrade
2. **on_update zu mechanisch** — Nur Versionsnummern geändert, keine Migration der neuen Konventionen
3. **Blindes Überschreiben** — `curl -sO .agent.json` überschreibt lokale Anpassungen (identity, runtime, permissions)
4. **Kein Feedback-Loop** — Consumer-Repos senden keine Upgrades an AAMS zurück

---

## Lösung: 4-Schichten-Upgrade-System

### Schicht 1: Versions-Detection

**Mechanismus:** `version_detection` in `.agent.json`

```json
"version_detection": {
  "local_version_file": "./.aams-version",
  "check": "if exists(local_version_file) and (local_version != _contract OR local_date != _version_date): trigger on_update",
  "fallback_check": "if exists(local_version_file) and _contract not present and local_version != _spec: trigger on_update (legacy)"
}
```

**Was verglichen wird:**
- `installed_version` (`.aams-version`) vs `_contract` (`.agent.json`)
- `installed_date` (`.aams-version`) vs `_version_date` (`.agent.json`)

**Bei Diskrepanz:** `on_update` wird ausgeführt

### Schicht 2: on_update-Contract

**Neuer Flow (ab v2.3.1):**

1. **VERSION-CHECK** — Vergleiche `_contract` + `_version_date` mit `.aams-version`
2. **Backup** — `.agent.json` → `.agent.json.bak`
3. **Lade Remote** — `curl -sO https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json`
4. **Merge** — Vergleiche `.agent.json.bak` mit neuer `.agent.json`, behalte lokale Anpassungen
5. **CHANGELOG lesen** — Remote: `https://raw.githubusercontent.com/ogerly/AAMS/main/CHANGELOG.md`
6. **Parse "Added"/"Changed"** — Neue workspace.structure-Pfade und Konventionen extrahieren
7. **MIGRATE** — Erstelle neue Pfade im Consumer-Repo wenn fehlend
8. **MIGRATE** — Wende neue Konventionen an
9. **MIGRATE** — Prüfe tool_detection-Beispiele auf Relevanz
10. **MIGRATE** — Flagge "Removed"-Dateien zur Review (kein Auto-Delete)
11. **Aktualisiere** — `.aams-version` und `_version_date`
12. **FEEDBACK** — Erstelle anonymisierten Upgrade-Report als GitHub Issue an `ogerly/AAMS`
13. **Cleanup** — Lösche `.agent.json.bak` nach erfolgreichem Merge

### Schicht 3: Backup + Merge

**Warum Backup?** Consumer-Repos haben lokale Anpassungen in `.agent.json`:
- `identity.name`, `identity.version` — Agent-Identität
- `runtime.model`, `runtime.provider` — LLM-Konfiguration
- `permissions` — Zugriffsrechte
- `memory` — LTM-Konfiguration

**Blindes `curl -sO` würde alle Anpassungen löschen.**

**Neuer Flow:**
1. `.agent.json` → `.agent.json.bak` (Backup)
2. Remote laden
3. Diff: `.agent.json.bak` vs neue `.agent.json`
4. Lokale Anpassungen zurückkopieren
5. `.agent.json.bak` löschen

### Schicht 4: Feedback-Loop

**Anonymisierter Upgrade-Report als GitHub Issue an `ogerly/AAMS`**

**Titel:** `AAMS Upgrade Report — {OLD_VERSION} → {NEW_VERSION}`

**Body:**
```markdown
### Upgrade Summary

- **Installed Version:** {OLD_VERSION}
- **New Version:** {NEW_VERSION}
- **Upgrade Date:** {DATE}
- **Migration:** {MIGRATION_SUMMARY}
- **New Paths Created:** {PATHS_LIST}
- **Convention Changes:** {CONVENTION_CHANGES}
- **Removed Files Flagged:** {REMOVED_FILES_LIST}
- **Issues Encountered:** {ISSUES}

---

> This report is anonymized. No repository name, secrets, tokens, or personal data is included.
```

**Anonymisierung:**
- **Ausschließen:** `repo_name`, `repo_url`, `author`, `GITHUB_TOKEN`, `secrets`, `api_keys`, `passwords`
- **Maskieren:** `ghp_*`, `gho_*`, `ghs_*`, `ghr_*`, `*.key`, `*.pem` → `[REDACTED]`
- **Optional:** Nur wenn `GITHUB_TOKEN` in `.env` vorhanden
- **Niemals:** Repo-Name, Secrets, Tokens, persönliche Daten

---

## Consumer-Upgrade-Prompt

**Für KI-Agenten in Consumer-Repos:**

```
Upgrade AAMS in diesem Repo. Führe folgende Schritte aus:

1. VERSION-CHECK: Lies `.aams-version` und vergleiche `installed_version` mit Remote `https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json` → `_contract`
2. WENN Version unterschiedlich:
   a. **Backup:** Kopiere lokale `.agent.json` nach `.agent.json.bak`
   b. **Lade Remote:** `curl -sO https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json`
   c. **Merge:** Vergleiche `.agent.json.bak` mit neuer `.agent.json` — behalte lokale Anpassungen (z.B. identity, runtime, permissions)
   d. Lies CHANGELOG.md von AAMS (Remote: `https://raw.githubusercontent.com/ogerly/AAMS/main/CHANGELOG.md`)
   e. Finde den Abschnitt für die neue Version
   f. Parse "Added" und "Changed" Sektionen für neue workspace.structure-Pfade
   g. MIGRATE: Erstelle alle neuen Pfade in WORKING/ z.B. `WORKING/TOOLS/skills/`, `WORKING/WORKPAPER/observe/`
   h. MIGRATE: Wende neue Konventionen an (Skills-Struktur, tool_detection, etc.)
   i. MIGRATE: Prüfe ob "Removed" Dateien im lokalen Repo existieren — flagge zur Review (kein Auto-Delete)
   j. Aktualisiere `.aams-version`:
      - `installed_version` = neue `_contract` aus `.agent.json`
      - `installed_date` = heute (YYYY-MM-DD)
      - `last_update` = heute
   k. Aktualisiere `_version_date` in `.agent.json` = heute (YYYY-MM-DD)
   l. **FEEDBACK:** Erstelle anonymisierten Upgrade-Report als GitHub Issue an `ogerly/AAMS` (wenn `GITHUB_TOKEN` in `.env` vorhanden)
   m. Lösche `.agent.json.bak` nach erfolgreichem Merge
3. WENN keine neue Version: nichts tun

Berichte was passiert ist.
```

---

## CHANGELOG v2.3.1 — Fix: Update-Detection

### Fixed

- **Update-Detection kaputt** — `version_detection` verglich nur `_contract` mit `.aams-version`. Da `_contract` immer `AAMS/2.0` war, merkten Consumer-Repos keine Änderung. Jetzt: `_contract` trägt Patch-Version (`AAMS/2.3.1`), `version_detection` vergleicht zusätzlich `_version_date` mit `.aams-version.installed_date`. Bei Diskrepanz → `on_update` wird ausgeführt.
- **`_version_date` nicht in `on_update`** — Der `on_update`-Contract hat `_version_date` in `.agent.json` nicht aktualisiert. Neue Zeile hinzugefügt: "Update `_version_date` in `.agent.json` to current date (YYYY-MM-DD)".
- **Andere Consumer-Repos blind** — Ohne Patch-Version im `_contract` und ohne `_version_date`-Vergleich bleibt ein Upgrade für alle Repos unsichtbar. Fix: semver im `_contract` + `_version_date`-Vergleich in `version_detection`.

### Changed

- **`_contract`** — `AAMS/2.0` → `AAMS/2.3.1` (Patch-Version für Update-Detection)
- **`.aams-version`** — `installed_version` → `AAMS/2.3.1`, `install_type` → `upgrade`
- **`version_detection.check`** — Erweitert: vergleicht nun `_contract` UND `_version_date` mit `.aams-version`
- **`reference/AGENT_SCHEMA.json`** — `$id` und `version` auf `2.3.0` aktualisiert
- **`reference/AGENT.json`** — `_version_date: 2026-07-08` hinzugefügt
- **`on_update` erweitert** — Migriert jetzt Konventionen, nicht nur Zahlen:
  - Parse CHANGELOG "Added"/"Changed" für neue workspace.structure-Pfade
  - MIGRATE: Erstelle neue Pfade im Consumer-Repo wenn fehlend
  - MIGRATE: Wende neue Konventionen an
  - MIGRATE: Prüfe tool_detection-Beispiele auf Relevanz
  - MIGRATE: Flagge "Removed"-Dateien zur Review (kein Auto-Delete)
  - Logge Migration-Aktionen in DIARY/
  - Aktualisiert `_version_date` in `.agent.json`

---

## CHANGELOG v2.3.2 — Fix: on_update migriert Konventionen

### Fixed

- **on_update zu mechanisch** — Consumer-Repos erhielten nur Versionsnummer-Änderungen, aber keine Migration der neuen Konventionen. Beispiel: Nach `curl .agent.json` wurde `WORKING/TOOLS/skills/` nicht erstellt, obwohl CHANGELOG v2.3.0 "Skill-Baukasten" als Added auflistet.
- **on_update ignorierte CHANGELOG-Inhalte** — Der Contract las CHANGELOG, führte aber nur Versions-Updates aus. Neue workspace.structure-Pfade, neue Sektionen und neue Konventionen wurden nicht migriert.
- **Keine Migration neuer Pfade** — Consumer-Repos wussten nicht, dass sie neue Ordner anlegen müssen.

### Changed

- **`on_update` erweitert** — Neue Schritte:
  - Parse CHANGELOG "Added" und "Changed" für neue workspace.structure-Pfade
  - MIGRATE: Erstelle alle neuen workspace.structure-Pfade im Consumer-Repo wenn fehlend
  - MIGRATE: Wende neue Konventionen aus CHANGELOG an (Folder-Strukturen, Skill-Definitionen, Detection-Patterns)
  - MIGRATE: Prüfe ob neue tool_detection-Beispiele relevant sind
  - MIGRATE: Flagge "Removed"-Dateien im lokalen Repo zur Review (kein Auto-Delete)
  - Log Migration-Aktionen in DIARY/{YYYY-MM-DD}.md
- **`on_update` schreibt jetzt Migrationen statt nur Zahlen**

---

## Design-Prinzipien

1. **Nie blind überschreiben** — Immer Backup + Merge
2. **Konventionen migrieren, nicht nur Zahlen** — Parse CHANGELOG "Added"/"Changed"
3. **Feedback-Loop anonymisiert** — Kein Repo-Name, keine Secrets, keine Tokens
4. **Semver: nie runter** — Patch-Versionen für Bugfixes (2.3.0 → 2.3.1 → 2.3.2)
5. **Kein Auto-Delete** — "Removed"-Dateien nur flaggen, nicht löschen
6. **Migration loggen** — Alle Änderungen in DIARY/{YYYY-MM-DD}.md

---

## Status

- [x] WH-011 Whitepaper erstellt
- [x] `version_detection` erweitert (2.3.1)
- [x] `on_update` migriert Konventionen (2.3.2)
- [x] Backup + Merge statt blindem Überschreiben
- [x] Anonymisierter Feedback-Loop implementiert
- [x] UPGRADE.md für Consumer-Repos erstellt
- [x] README.md Upgrade-Prompt aktualisiert
- [ ] Consumer-Repos testen mit neuem Upgrade-Prompt
- [ ] Feedback-Issues sammeln von Consumer-Repos

---

> Letztes Update: 2026-07-08 — WH-011 Upgrade-System: 4-Schichten-Modell (Detection, Migration, Backup+Merge, Feedback). AAMS ist standardlos, beschreibt aber wie Consumer-Repos upgraden müssen. Semver: nie runter.
