# Workpaper: AAMS Update & Install Detection Protocol
# Wie curl-basierte Installs und Updates sauber zwischen Zuständen unterscheiden

**Datum:** 2026-04-10  
**Autor:** @ogerly / DEVmatrose  
**Typ:** Protokoll-Design / Feature-Konzept  
**Priorität:** Hoch — Voraussetzung für AAMS/2.0 Release  
**Abhängigkeiten:**
- `2026-04-10-AAMS-STRAT-reorientation-spec-vs-contract.md` (Entscheidung: Spec → Contract)
- `2026-04-10-AAMS-RFCT-spec-to-contract-refactor-plan.md` (Refactor-Inventar, INV-1/INV-2)
- `2026-04-10-AAMS-WORKSPACE-field-report-workspace-container.md` (WORKSPACE-Discovery)

---

## Session Goal

Konzipieren wie ein Agent der `.agent.json` liest — egal ob erstmalig oder nach einem Update — **deterministisch und sicher** erkennt in welchem Zustand das Zielrepo ist, und genau das tut was nötig ist: nichts mehr, nichts weniger.

Das Update-System ist ein eigenständiger Teil. Es darf nicht in den Spec→Contract-Refactor eingebettet werden.

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-10-AAMS-UPD-update-install-detection-protocol.md` | ✅ |

---

## 1. Das Problem heute

Aktuell kennt `.agent.json` nur zwei Zustände:

```json
"on_first_entry": [...]   // Repo neu — WORKING/ existiert nicht
"on_session_start": [...]  // Repo bekannt — WORKING/ existiert
```

Was fehlt:

| Zustand | Aktuell abgedeckt? |
|---------|--------------------|
| Neues Repo, kein WORKING | ✅ `on_first_entry` |
| Bekanntes Repo, WORKING vorhanden | ✅ `on_session_start` |
| `.agent.json` wurde durch curl **aktualisiert** (neue Version) | ❌ kein Mechanismus |
| WORKING vorhanden aber **unvollständig** (fehlende Unterordner) | ❌ kein Mechanismus |
| WORKSPACE/WORKING UND ./WORKING/ beide vorhanden (Konflikt) | ❌ kein Mechanismus |
| Ordner vorhanden aber mit **anderem AAMS-Version-Stand** | ❌ kein Mechanismus |
| Agent-spezifische Sub-Ordner fehlen (TOOLS/, LOGS/, etc.) | ❌ partiell (create_if_missing) |

Das ist die Lücke die geschlossen werden muss.

---

## 2. Drei Szenarien die klar unterschieden werden müssen

### Szenario A — Fresh Install

```bash
# User holt .agent.json in ein leeres oder AAMS-freies Repo
curl -sO https://raw.githubusercontent.com/DEVmatrose/AAMS/main/.agent.json
```

**Erkennungsmerkmal:** Keine WORKING/, keine WORKSPACE/WORKING/, keine `.aams-version`-Datei.

**Erwartetes Verhalten:** Vollständige Erstinitialisierung. Alle Ordner anlegen. Erste Workpaper schreiben. READ-AGENT.md erstellen.

---

### Szenario B — Update (gleiche Hauptversion)

```bash
# User überschreibt .agent.json mit neuer Patch/Minor-Version
# z.B. AAMS/1.2 → AAMS/1.3  oder  AAMS/2.0 → AAMS/2.1
curl -sO https://raw.githubusercontent.com/DEVmatrose/AAMS/main/.agent.json
```

**Erkennungsmerkmal:**
- WORKING/ (oder WORKSPACE/WORKING/) existiert
- `_contract` (oder `_spec`) Version im neuen File ist **höher** als gespeicherte Version

**Erwartetes Verhalten:**
1. Neu hinzugefügte Ordner anlegen wenn fehlend (create_if_missing → idempotent)
2. Bestehende Dateien **nicht** überschreiben
3. Migrations-Log-Eintrag schreiben
4. Kein on_first_entry — kein on_session_start — stattdessen: `on_update`

---

### Szenario C — Major Version Upgrade (Breaking Change)

```bash
# User wechselt von AAMS/1.x auf AAMS/2.0
curl -sO https://raw.githubusercontent.com/DEVmatrose/AAMS/main/.agent.json
```

**Erkennungsmerkmal:**
- Gespeicherte Version ist `AAMS-MINI/1.x` oder `AAMS/1.x`
- Neue Version ist `AAMS/2.0`

**Erwartetes Verhalten:**
1. **STOPP. Kein automatischer Umbau.**
2. Migration-Report schreiben: `WORKING/LOGS/aams-migration-YYYY-MM-DD.md`
3. User informieren: "Major version change detected. Manual migration recommended. See MIGRATION.md."
4. Legacy-Betrieb weiterlaufen lassen bis explizite Freigabe

---

## 3. Erkennungs-Mechanismus — Versionsanker

Das Problem: woher weiß der Agent welche AAMS-Version das Repo **aktuell hat**?

Aktuell: gar nicht — `.agent.json` kann nur die Soll-Version sagen, nicht die Ist-Version.

### Lösung: `.aams-state` Datei (leichtgewichtig)

Eine minimale State-Datei die nach dem ersten Install geschrieben wird und bei jedem Update aktualisiert wird:

```json
// .aams-state  (im Repo-Root oder in WORKING/ bzw. WORKSPACE/)
{
  "installed_version": "AAMS-MINI/1.0",
  "installed_date": "2026-03-15",
  "workspace_root": "./WORKING",
  "workspace_container": null,
  "last_update": null,
  "install_type": "fresh"
}
```

**Nach Update auf AAMS/2.0:**
```json
{
  "installed_version": "AAMS/2.0",
  "installed_date": "2026-03-15",
  "workspace_root": "./WORKING",
  "workspace_container": "./WORKSPACE",
  "last_update": "2026-04-10",
  "install_type": "update",
  "previous_version": "AAMS-MINI/1.0",
  "migration_status": "pending"
}
```

**Alternativen** (falls `.aams-state` als zu viel empfunden wird):
- Version in `READ-AGENT.md` Header als parsable Zeile: `<!-- aams-version: AAMS-MINI/1.0 -->`
- Version in `WORKING/MEMORY/ltm-index.md` als erstem Eintrag
- Kein State-File — Version wird aus Ordner-Inventory abgeleitet (fragil)

**Empfehlung:** `.aams-state` als explizite Datei. Klein, maschinenlesbar, klar. In `.gitignore` oder commiten — User-Entscheidung.

---

## 4. Ordner-Check-Protokoll

Beim **jedem** Lesen von `.agent.json` — Install, Update, Session-Start — muss der Agent folgende Prüfung durchführen. Diese Prüfung muss **in `.agent.json` vollständig beschrieben** sein, damit sie ohne externe Dokumentation ausgeführt werden kann (INV-1: curl-Invariante).

### 4.1 Workspace-Discovery (Reihenfolge ist wichtig)

```
SCHRITT 1 — Container-Suche:
  IF ./WORKSPACE/WORKING/ exists → workspace_root = ./WORKSPACE/WORKING/
  ELSE IF ./workspace/WORKING/ exists → workspace_root = ./workspace/WORKING/  (case-insensitive)
  ELSE IF ./WORKING/ exists → workspace_root = ./WORKING/  (legacy)
  ELSE → Fresh Install → Goto SCHRITT 4

SCHRITT 2 — Konflikt-Check:
  IF ./WORKING/ exists AND ./WORKSPACE/WORKING/ exists:
    → STOP. Conflict detected.
    → Write: WORKING/LOGS/aams-conflict-YYYY-MM-DD.md
    → Inform user. Do not proceed automatically.

SCHRITT 3 — Version-Check:
  IF .aams-state exists:
    → Read installed_version
    → Compare with _contract (or _spec) in .agent.json
    → IF same version → on_session_start
    → IF higher minor/patch → on_update
    → IF higher major → on_major_upgrade (STOP, inform user)
  ELSE:
    → Assume legacy install (no version tracking)
    → on_session_start (safe fallback)

SCHRITT 4 — Fresh Install:
  → Create workspace_root (preferred: ./WORKSPACE/WORKING/)
  → Create all structure folders
  → Write .aams-state
  → on_first_entry
```

### 4.2 Struktur-Check (für alle Szenarien außer Konflikt)

Nach Workspace-Discovery: prüfe ob alle definierten Unterordner existieren.

```
FOR EACH folder IN workspace.structure:
  IF folder does NOT exist:
    → Create folder  (create_if_missing: true)
    → Log: "Created missing folder: {folder}" in WORKING/LOGS/
  ELSE:
    → Skip (never_delete: true, never_overwrite: true)
```

**Wichtig:** Die Ordner-Liste in `workspace.structure` ist die einzige Wahrheitsquelle. Ein Agent darf keine Ordner anlegen die dort nicht stehen, und darf keine löschen die dort stehen — egal ob sie Inhalt haben oder leer sind.

---

## 5. `on_update` — neuer Contract-Step

Ergänzung zu den bestehenden `on_first_entry` und `on_session_start`:

```json
"on_update": [
  "0. PRE-CHECK: Read .aams-state. Confirm this is an update (installed_version < new version).",
  "1. Run structure check (4.2) — create any missing folders",
  "2. Write update log: WORKING/LOGS/aams-update-YYYY-MM-DD.md with: old version, new version, folders created, folders already present",
  "3. Update .aams-state: installed_version, last_update, install_type=update",
  "4. If MIGRATION.md exists for this version: display migration notes to user",
  "5. Continue with on_session_start"
],
"on_major_upgrade": [
  "0. PRE-CHECK: Confirm major version jump (e.g. 1.x → 2.x).",
  "1. STOP. Do not restructure automatically.",
  "2. Write migration report: WORKING/LOGS/aams-migration-YYYY-MM-DD.md",
  "3. Display: 'AAMS major version change detected. This may require manual migration. See MIGRATION.md before proceeding.'",
  "4. Wait for explicit user confirmation before any structural changes."
]
```

---

## 6. Release-zu-Release Dokumentation

Jedes AAMS-Release braucht eine `MIGRATION.md` (oder versionierte `MIGRATION-vX.Y.md`) die folgendes dokumentiert:

```markdown
# AAMS Migration Guide — vX.Y.Z → vA.B.C

## Ist das ein Breaking Change?
Ja / Nein + Begründung

## Was ändert sich automatisch?
(Agent macht das selbst via on_update)
- Neue Ordner in workspace.structure werden angelegt

## Was muss der User manuell tun?
- Schritt 1...
- Schritt 2...

## Was ändert sich NICHT?
- Bestehende Workpapers bleiben unberührt
- Bestehende WORKING/MEMORY/ bleibt unberührt
- curl-Befehl bleibt identisch

## Backward Compatibility
- Repos mit ./WORKING/ (legacy) funktionieren weiterhin
- _spec:AAMS-MINI/1.0 wird noch X Releases lang erkannt
```

**Speicherort:** `MIGRATION.md` im Repo-Root (neben `.agent.json`).  
**Format:** Menschenlesbar + maschinenlesbar (der Agent liest es in `on_major_upgrade`).

---

## 7. Scope-Abgrenzung

| Feature | In diesem Workpaper | Separates Workpaper |
|---------|--------------------|--------------------|
| Versions-State (`.aams-state`) | ✅ konzipiert | Implementierung in RFCT |
| `on_update` Contract-Step | ✅ konzipiert | Implementierung in RFCT |
| `on_major_upgrade` Contract-Step | ✅ konzipiert | Implementierung in RFCT |
| WORKSPACE-Discovery-Logik | ✅ referenziert | Detail in WORKSPACE Field Report |
| `MIGRATION.md` Format | ✅ Template | Inhalt in RFCT-Workpaper |
| Spec → Contract Umbenennung | ❌ nicht hier | RFCT-Workpaper |
| Neue `.agent.json` Felder konkret | ❌ nicht hier | RFCT-Workpaper |

---

## 8. Offene Fragen

1. **`.aams-state` committen oder gitignoren?**  
   Pro Commit: andere Team-Mitglieder wissen welche Version das Repo hat.  
   Pro Ignore: keine "bot commits" nur für State-Updates.  
   → Empfehlung: commiten — State ist Infrastruktur-Wahrheit, kein Temp-File.

2. **Was wenn `.aams-state` fehlt aber WORKING/ existiert (Legacy-Repos)?**  
   → Fallback: `on_session_start` (sicherster Pfad, kein Datenverlust). State-File beim nächsten `on_session_end` nachschreiben.

3. **Versionierung von `.aams-state` selbst?**  
   Das Schema von `.aams-state` könnte sich ändern. Lösung: `"_schema": "1"` als erstes Feld.

4. **Wo liegt `.aams-state`?**  
   Option A: Repo-Root (neben `.agent.json`) — einfach zu finden.  
   Option B: In `WORKING/` oder `WORKSPACE/` — gehört zum Agent-Workspace.  
   → Empfehlung: Option A — Agent-State gehört zu `.agent.json`, nicht in WORKING.

---

## Key Findings

- **Drei klar unterschiedliche Szenarien** müssen per Protokoll unterschieden werden: Fresh Install, Minor Update, Major Upgrade
- **`.aams-state`** ist das fehlende Bindeglied — ohne Versions-Anker kann kein Agent zwischen Install und Update unterscheiden
- **Ordner-Check ist bereits teilweise da** (`create_if_missing: true`) — fehlt nur die explizite Prüf-Reihenfolge und das Logging
- **`on_update`** als neuer Contract-Step ist minimal und sicher — er erweitert das bestehende Drei-Zustands-Modell auf vier Zustände
- **`MIGRATION.md`** als Release-Artefakt ist notwendig — Agent liest sie in `on_major_upgrade`, User liest sie manuell
- Dieser Teil ist vollständig unabhängig vom Spec→Contract-Refactor und kann parallel entwickelt werden

---

## Next Steps

- [ ] E-6 entscheiden: `.aams-state` Dateiname, Schema, Ablageort (Eigenständige Entscheidung)
- [ ] `on_update` und `on_major_upgrade` in `.agent.json` Entwurf einfügen (RFCT-Phase 1)
- [ ] `MIGRATION.md` Template als `reference/templates/migration-template.md` anlegen
- [ ] WORKSPACE-Discovery-Pseudocode (Schritt 1-4 aus Abschnitt 4.1) in `.agent.json` `bootstrap_rules` übersetzen
- [ ] Workpaper schließen → MEMORY ingesten

---

*Workpaper erstellt: 2026-04-10 — eigenständiger Teil: Update/Install Detection Protocol*
