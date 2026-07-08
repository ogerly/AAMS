# Workpaper: Session-Start Analyse — AAMS/2.2 Status & GitHub-Migration

**Datum:** 2026-07-06  
**Typ:** ANALYSE — Session-Start Status-Check  
**Priorität:** HOCH — Post-Migration Check

---

## Session Goal

Post-Migration Status von ogerly/AAMS analysieren: GitHub-Issues, lokale vs. Remote-Sync, offene Lücken, Migration-Check.

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-07-06-session-start-analyse.md` | ✅ |

---

## 1. GitHub — ogerly/AAMS (neuer Account)

### Repo-Status (via Webfetch)

| Metrik | Wert |
|--------|------|
| **Stars** | 5 |
| **Forks** | 0 |
| **Open Issues** | 9 |
| **Pull Requests** | 0 |
| **Releases** | 4 (v1.3.0 als Latest auf GitHub-Seite) |
| **Commits** | 87 |
| **Sprache** | Python 100% |

### Offene Issues (alle 9)

| # | Datum | Titel | Prio | Status |
|---|-------|-------|------|--------|
| **#51** | 2026-04-29 | Kann ein Skill einen Denkprozess auslassen? | Neu | 🔴 Konzept vorhanden, nie umgesetzt |
| **#50** | 2026-04-28 | Feld-Report — File Safety (mantis-cms) | Neu | 🔴 Konzept vorhanden, nie umgesetzt |
| **#49** | 2026-04-17 | Upgrade-Transparenz fehlt | Hoch | 🟡 `.aams-version` existiert, Tags fehlen |
| **#48** | 2026-04-17 | Decision-Kompoundierungs-Leck | KRITISCH | 🟡 Decision-Promotion + wiki_lint.py existieren |
| **#47** | 2026-04-17 | Tool Decay & Relative Path Vulnerability | Mittel | 🟢 validate_tools.py + Pre-Flight Check |
| **#46** | 2026-04-17 | Ordner im Projekt-Root statt WORKING/TOOLS/ | Mittel | 🟢 AGENTS.md Pre-Flight Check |
| **#45** | 2026-04-12 | RFC: AAMS is not a Spec (kurz) | — | 🔴 Duplikat von #43 — manuell schließen |
| **#43** | 2026-04-12 | RFC: AAMS is not a Spec (voll) | Hoch | 🟡 Phase 1+5 RFCT abgeschlossen |
| **#41** | 2026-04-09 | Feldbericht: MantisClaw Upgrade | Hoch | 🟡 4/5 Empfehlungen umgesetzt |
| **#26** | 2026-03-26 | Security Signals in AGENT.json | Mittel | 🔴 Backlog — `security`-Sektion existiert |

### Wichtige Beobachtung: GitHub Releases

Auf GitHub-Seite ist **v1.3.0 (2026-04-09)** als "Latest Release" markiert. Lokal existieren **v2.0.0, v2.1.0, v2.2.0** als Git-Tags. Diese wurden vermutlich nie als GitHub Releases published.

---

## 2. Lokaler vs. Remote-Status

### Remote-URL

| Quelle | URL |
|--------|-----|
| **Lokal konfiguriert** | `https://github.com/DEVmatrose/AAMS.git` |
| **GitHub (Web)** | `https://github.com/ogerly/AAMS` |

**⚠️ MISMATCH:** Die lokale git Remote zeigt noch auf `DEVmatrose/AAMS`, nicht auf `ogerly/AAMS`. Das Repo wurde migriert, aber die Remote-URL wurde nicht aktualisiert.

### Git-Status

| Metrik | Wert |
|--------|------|
| **Branch** | main |
| **Status** | ✅ Synced (git pull durchgeführt) |
| **Commits hinter Remote** | 0 (nach pull) |
| **Uncommitted** | opencode.json (modified), 3 untracked files |
| **Uncommitted files** | `opencode.json`, `WORKING/WORKPAPER/skill-opencode-agent.md`, `WORKING/WORKPAPER/aams-guard-plugin.md`, `docs/video-tump-1.png` |

---

## 3. Workpaper-Status

### Active (2)

| Datei | Datum | Typ | Status |
|-------|-------|-----|--------|
| `2026-04-29-projekt-analyse.md` | 2026-04-29 | ISS | ✅ Analyse abgeschlossen, nächste Steps definiert |
| `2026-04-24-three-tests.md` | 2026-04-24 | TST | ⚠️ 2 P1/P2 Issues — teilweise gelöst |

### Observe (3)

| Datei | Datum | Typ | Status |
|-------|-------|-----|--------|
| `2026-04-02-wording-faktencheck.md` | 2026-04-02 | RES | ⏳ Wartend |
| `2026-04-15-mempalace-analyse.md` | 2026-04-15 | RES | ⏳ Wartend |
| `2026-04-15-social-outreach.md` | 2026-04-15 | MKT | ⏳ Wartend |

### Closed (52)

Letzte Schließung: 2026-04-30 — **~2.5 Monate her.**

---

## 4. Neue Dateien/User-Beitrag

Der User hat 2 neue Dokumente erstellt:

### A. `WORKING/WORKPAPER/skill-opencode-agent.md` (105 Zeilen)

OpenCode-Agent-Skill als Referenz-Dokument. Enthält:
- Config-Hierarchie (Remote → Global → Project)
- MANTIS-Provider-Block mit Modell-Routing
- Permission-System (allow/ask/deny)
- **Plugin-Hooks** (`tool.execute.before`/`after`) — das eigentliche Enforcement
- **AAMS-Guard-Pattern** — Gate für `.agent.json` + `READ-AGENT.md` Lese-Check
- Bekannte Bugs: Subagent-Bypass, SDK-Deny-Bug
- Skill-Discovery-Reihenfolge
- Checkliste für neue AAMS-Projekte mit OpenCode

### B. `WORKING/WORKPAPER/aams-guard-plugin.ts` (69 Zeilen)

Vollständiges TypeScript-Plugin für OpenCode:
- 3-Stufen-Enforcement: Context gelesen → Workpaper open → Tools erlaubt
- Session-State via `Set<string>` pro sessionID
- Regex-Check auf `status: open` in Workpapers
- Bekannte Grenzen: Subagent-Bypass, Session-Neustart-State-Verlust

**⚠️ Diese Dateien sind noch uncommitted und nicht im Git.**

---

## 5. Core-Gaps — Status nach ~2.5 Monaten Pause

### Gap 1: Issue-Triage (🔴)

| Issue | Aktion |
|-------|--------|
| #45 | Manuell als Duplikat von #43 schließen |
| #26 | Entscheden: implementieren oder backlog? (`security`-Sektion existiert bereits) |

### Gap 2: Remote-URL Update (🔴)

Lokal: `DEVmatrose/AAMS` → Sollen: `ogerly/AAMS`

### Gap 3: GitHub Releases (🟡)

v2.0.0, v2.1.0, v2.2.0 existieren als Git-Tags aber nicht als GitHub Releases.

### Gap 4: .aams-version + Upgrade-Transparenz (🟡)

`.aams-version` existiert als JSON-State-File. CHANGELOG.md existiert. Aber:
- Kein automatischer Version-Check in `on_session_start`
- Tags auf GitHub published?

### Gap 5: Uncommitted User-Files (🟡)

skill-opencode-agent.md + aams-guard-plugin.md liegen als uncommitted files in WORKING/WORKPAPER/ — sollten committed oder nach WORKING/TOOLS/ verschoben werden.

### Gap 6: Stale Workpapers in observe/ (🟢)

3 observe-Workpapers seit April wartend. Prüfen ob noch relevant.

---

## 6. Health-Score

| Dimension | Score | Befund |
|-----------|-------|--------|
| **Issue-Abdeckung** | 6/10 | 9 offen, 2 neu (#50/#51), 1 duplikat (#45), 1 backlog (#26) |
| **Workpaper-Leben** | 4/10 | 2 active, 3 observe (stale), 52 closed. Letzte Schließung vor 2.5 Monaten |
| **Whitepaper-Konsistenz** | 9/10 | Alle "Agent Manifest" konsistent. Manifest-Prinzip (D9) verankert |
| **Upgrade-Transparenz** | 6/10 | CHANGELOG + `.aams-version` + Tags existieren. GitHub Releases fehlen |
| **Tool-Integrität** | 9/10 | 4 Tools aktiv, Health-Score 10/10 |
| **RFC-Progress** | 9/10 | Phase 1+5 RFCT abgeschlossen. Manifest-Prinzip überall konsistent |
| **LTM-Health** | 7/10 | 137 Einträge, Vektorspeicher aktiv |
| **Repo-Sync** | 5/10 | ⚠️ Remote-URL zeigt auf altes Repo (DEVmatrose) |
| **Gesamt** | **7/10** | Post-Migration: Core-Funktionalität intakt, aber Remote-Migration unvollständig |

---

## 7. Nächste Steps

### P0 — Sofort

| # | Aktion | Aufwand |
|---|--------|---------|
| 1 | Remote-URL auf `ogerly/AAMS` aktualisieren | 1 min |
| 2 | Issue #45 manuell als Duplikat schließen | 1 min |
| 3 | Uncommitted User-Files committen | 5 min |

### P1 — Dieser Session

| # | Aktion | Aufwand |
|---|--------|---------|
| 4 | `.aams-version` + `on_session_start` Version-Check finalisieren | 15 min |
| 5 | GitHub Releases für v2.0.0/v2.1.0/v2.2.0 erstellen | 10 min |
| 6 | skill-opencode-agent.md + aams-guard-plugin.md nach WORKING/TOOLS/ verschieben | 5 min |
| 7 | Observe-Workpapers prüfen: schließen oder behalten? | 10 min |

### P2 — Nächste Sessions

| # | Aktion |
|---|--------|
| 8 | Issue #51 (Skills) als Whitepaper oder Guideline finalisieren |
| 9 | Issue #50 (File Safety) mit Guard-Plugin integrieren |
| 10 | Issue #49 (Upgrade-Transparenz) mit GitHub Releases schließen |
| 11 | Issue #48 (Decision-Leck) mit WP-001 Update schließen |
| 12 | Issue #41 (Topic Registry) finalisieren |

---

## 8. Decisions

| # | Decision | Begründung |
|---|----------|------------|
| D1 | Remote-URL auf `ogerly/AAMS` aktualisieren | Migration abgeschlossen, alte URL veraltet |
| D2 | skill-opencode-agent.md bleibt in WORKING/WORKPAPER/ | Es ist ein Skill-Dokument, kein Tool-Code |
| D3 | aams-guard-plugin.ts nach WORKING/TOOLS/ verschieben | Es ist Plugin-Code (TypeScript), gehört zu TOOLS/ |
| D4 | Issue #45 sofort als Duplikat schließen | Redundant, gleiche These wie #43 |
| D5 | Observe-Workpapers prüfen | 3 Dateien seit April stale — entweder schließen oder explizit weiternehmen |

---

## Next Steps

**Diese Session:**
1. Remote-URL auf `ogerly/AAMS` aktualisieren
2. Uncommitted files committen
3. Issue #45 schließen
4. GitHub Releases checken (v2.0.0-v2.2.0)
5. aams-guard-plugin.ts nach WORKING/TOOLS/ verschieben
6. Observe-Workpaper-Fate entscheiden

---

> Letztes Update: 2026-07-06 — Session-Start Analyse nach ~2.5 Monaten Pause. Remote-Migration teilweise abgeschlossen (GitHub-Seite auf ogerly, aber lokale git Remote noch DEVmatrose). Core-Funktionalität intakt (Health-Score 10/10), aber Repo-Sync auf 5/10.
