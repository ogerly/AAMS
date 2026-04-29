# Workpaper: Issue Triage & Session-Orientierung — Stand 2026-04-24

**Datum:** 2026-04-24  
**Autor:** @DEVmatrose  
**Typ:** Triage / Session-Orientierung  
**Priorität:** Hoch — bestimmt die nächste Arbeitsphase

---

## Session Goal

Alle 7 offenen GitHub-Issues prüfen und gegen den aktuellen Stand der Workpapers mappen. Klare Antwort auf:
1. Was haben wir schon auf dem Schirm?
2. Was ist neu?
3. Was wollen wir als nächstes angehen?

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-24-issue-triage.md` | ✅ |

---

## 1. Issue-Übersicht

| # | Datum | Titel | Prio | Workpaper-Abdeckung | Status |
|---|-------|-------|------|---------------------|--------|
| #49 | 2026-04-17 | Upgrade-Transparenz fehlt: curl-User sehen nicht was sich geaendert hat | Hoch | Konzepte fertig (UPD Workpaper), nicht umgesetzt | 🔴 Offen |
| #48 | 2026-04-17 | Decision-Kompoundierungs-Leck: Architektur-Decisions versickern in Workpapers | KRITISCH | Diagnose fertig, Fix konzipiert, nicht umgesetzt | 🔴 Offen |
| #47 | 2026-04-17 | Tool Decay & Relative Path Execution Context Vulnerability | Mittel | Kein Workpaper — neu | 🔴 Offen |
| #46 | 2026-04-17 | Agent-Fehler: Ordner im Projekt-Root statt WORKING/TOOLS/ | Mittel | Kein Workpaper — neu | 🔴 Offen |
| #45 | 2026-04-12 | RFC: AAMS is not a Spec | — | Duplikat von #43 | 🟡 Schließen |
| #43 | 2026-04-12 | RFC: AAMS is not a Spec | Hoch | ✅ STRAT + RFCT Workpapers | 🟢 Abgedeckt |
| #41 | 2026-04-09 | Feldbericht: MantisClaw Upgrade v1.0.0 → v1.3.0 | Hoch | ✅ Teilweise (3/5 Empfehlungen) | 🟡 Teilweise |
| #26 | 2026-03-26 | Security Signals in AGENT.json | Mittel | Kein Workpaper — alt | 🔴 Offen |

---

## 2. Detailanalyse — was haben wir auf dem Schirm?

### ✅ Vollständig abgedeckt (bereits analysiert)

**#43 — RFC: AAMS is not a Spec — it is an Agent Contract**
- **Workpaper:** `2026-04-10-AAMS-STRAT-reorientation-spec-vs-contract.md` + `2026-04-10-AAMS-RFCT-spec-to-contract-refactor-plan.md`
- **Stand:** Analyse vollständig. Option B (Spec → Contract) angenommen. Refactoring-Plan mit 5 offenen Entscheidungen (E-1 bis E-5).
- **Offen:** Keine weiteren Analysen nötig. Issue dient als öffentlicher RFC-Tracker.
- **Aktion:** Issue offen lassen, aber als "analytisch abgeschlossen" markieren. Nächster Schritt: Implementierung des Refactor-Plans.

---

### ⚠️ Teilweise abgedeckt

**#41 — Feldbericht: MantisClaw Upgrade**
- **Workpaper:** `2026-04-10-AAMS-UPD-update-install-detection-protocol.md`
- **5 Empfehlungen aus dem Feldbericht:**
  - ✅ Empfehlung 1 (UPGRADING.md pro Release) → vollständig konzipiert in UPD Workpaper als MIGRATION.md-Konzept
  - ✅ Empfehlung 2 (`_deviations` in Spec) → bereits implementiert in Commit 3cde55e
  - ❌ Empfehlung 3 (Topic Registry maschinenlesbar) → **NICHT in einem Workpaper** — neue Lücke
  - ✅ Empfehlung 4 (`_spec` vs `AAMS_VERSION` klären) → vollständig in STRAT + RFCT
  - ✅ Empfehlung 5 (Compatibility Matrix) → niedrige Prio, kann warten
- **Offen:** Empfehlung 3 braucht ein eigenes Workpaper.

---

### 🔴 Neu / Unbearbeitet (seit 2026-04-17)

**#48 — Decision-Kompoundierungs-Leck (KRITISCH)**
- **Hintergrund:** Aus `2026-04-17-RES-WIKI-karpathy-llm-wiki-vergleich.md` entdeckt. Architekturschwärze: Entscheidungen in Workpapers versickern, neue Agents arbeiten mit veralteter Wahrheit.
- **Konkreter Befund:** `2026-04-10-AAMS-STRAT` hat Option B (Spec → Contract) angenommen. **WP-001 weiß davon nichts.**
- **Konzipierter Fix:**
  1. Decision-Promotion in `READ-AGENT.md` Session-End-Checklist
  2. `wiki_lint.py` als periodischen Health-Check (existiert bereits in `WORKING/TOOLS/`)
  3. Cross-Referenzen zwischen WP-001 bis WP-004 ergänzen
- **Status:** Diagnose ✅, Fix konzipiert ✅, **nicht umgesetzt**.
- **Aktion:** **Höchste Priorität** — betrifft den AAMS-Kern.

---

**#49 — Upgrade-Transparenz fehlt (Hoch)**
- **Hintergrund:** curl-User sehen nicht, was sich zwischen Updates geändert hat. Blindflug bei jedem Release.
- **Konzepte vorhanden:**
  - Versioning-System (`2026-03-27-versioning-system.md`) — konzipiert, nicht umgesetzt
  - Update-Detection-Protocol (`2026-04-10-AAMS-UPD-update-install-detection-protocol.md`) — konzipiert, nicht umgesetzt
- **Vorgeschlagener Fix:**
  1. CHANGELOG.md im Repo-Root
  2. Git-Tags + GitHub Releases
  3. `.aams-version` Datei im Zielrepo
  4. `on_update` Handler in `.agent.json`
  5. MIGRATIONS.md pro Version
- **Status:** Beide Konzepte ✅, **Implementierung ❌**.
- **Aktion:** Braucht ein Implementierungs-Workpaper. Eng gekoppelt mit #48 (beide sind infrastrukturell).

---

**#47 — Tool Decay & Relative Path Vulnerability (Mittel)**
- **Hintergrund:** Aus PAX Festival-Einsatz. Ein Python-Tool mit `ROOT = Path(__file__).resolve().parent.parent` verschmutzte den AAMS-Namespace, als es von `/tools/` nach `/WORKING/TOOLS/` umgezogen wurde.
- **Konkreter Bug:** Hardcodierter Offset-Pointer warf fälschlich das Agent-Memory als Root auf.
- **Vorgeschlagener Fix:**
  1. Pre-Flight Inspection (Agent Protocol: relative Pfade validieren vor Execution)
  2. Self-Healing Root Anchors (dynamische Root-Erkennung statt Offset-Pfade)
  3. AAMS Doctor (`validate_tools.py`) — periodischer Scan
- **Status:** **Komplett neu.** Kein Workpaper existiert.
- **Aktion:** Eigenständiges Workpaper — Tool-Integritäts-Protokoll.

---

**#46 — Ordner im Projekt-Root statt WORKING/TOOLS/ (Mittel)**
- **Hintergrund:** Zwei Agenten haben `tools/` im Projekt-Root angelegt (Commits `22a4a27` und `77f3f53`), obwohl `WORKING/TOOLS/` bereits existierte.
- **Konkreter Vorschlag:** Regel in `AGENTS.md` ergänzen: "Vor dem Anlegen eines neuen Ordners im Root muss geprüft werden, ob ein passender Ordner unter WORKING/ bereits existiert."
- **Status:** **Komplett neu.** Kein Workpaper existiert.
- **Aktion:** Kann mit #47 gebündelt werden — beide betreffen Agent-Verhaltensregeln.

---

**#26 — Security Signals in AGENT.json (Mittel)**
- **Hintergrund:** Seit 2026-03-26 offen. Optional `security`-Sektion in AGENT.json für Trust-Portabilität.
- **Struktur:** `last_scan`, `scan_type`, `findings`, `deployed_services`, `behavioral_signals`.
- **Status:** **Komplett neu.** Kein Workpaper existiert.
- **Aktion:** Kann warten — niedrige Priorität, kein Blocker.

---

**#45 — RFC: AAMS is not a Spec (Duplikat)**
- **Status:** Dünnerer Content, gleiche These wie #43.
- **Aktion:** Als Duplikat von #43 schließen.

---

## 3. Mappung: Offene Issues vs. bestehende Workpapers

| Issue | Bestehendes Workpaper | Lücke |
|-------|----------------------|-------|
| #43 | STRAT + RFCT | ✅ Keine — analytisch abgeschlossen |
| #41 (Empf. 1) | UPD | ✅ MIGRATION.md-Konzept |
| #41 (Empf. 2) | Commit 3cde55e | ✅ Implementiert |
| #41 (Empf. 3) | — | ❌ Topic Registry maschinenlesbar |
| #41 (Empf. 4) | STRAT + RFCT | ✅ Klärung enthalten |
| #48 | RES-WIKI (Diagnose) | ❌ Fix nicht umgesetzt |
| #49 | UPD + versioning-system | ❌ Konzepte nicht implementiert |
| #47 | — | ❌ Kein Workpaper |
| #46 | — | ❌ Kein Workpaper |
| #26 | — | ❌ Kein Workpaper |

---

## 4. Priorisierte Next-Steps

### Phase 1 — Aufräumen (sofort)

| # | Aktion | Aufwand |
|---|--------|---------|
| 1 | Issue #45 als Duplikat von #43 schließen | 1 min |
| 2 | Issue #42 als Duplikat von #41 schließen (aus vorheriger Triage) | 1 min |

### Phase 2 — Kritische Infrastruktur (nächste Sessions)

| # | Issue | Beschreibung | Aufwand |
|---|-------|-------------|---------|
| **1** | **#48** | **Decision-Promotion implementieren:** WP-001 INDEX.md aktualisieren, Decision-Promotion in READ-AGENT.md aufnehmen, wiki_lint.py Health-Check für Cross-Ref prüfen | 1-2 Sessions |
| **2** | **#49** | **Upgrade-Transparenz implementieren:** CHANGELOG.md anlegen, `.agent.json` um `spec_version` ergänzen, `.aams-version` Konzept finalisieren | 1-2 Sessions |

> Beide sind eng gekoppelt — #48 betrifft die Architekturstimme, #49 die Verteilungsinfrastruktur. Gemeinsam bilden sie die Basis für jedes AAMS/2.0 Release.

### Phase 3 — Tool-Integrität (parallel möglich)

| # | Issue | Beschreibung | Aufwand |
|---|-------|-------------|---------|
| **3** | **#47 + #46** | **Agent-Verhaltensregeln + Tool-Integrität:** AGENTS.md um "Pre-Flight Path Check" ergänzen, Self-Healing Root Pattern dokumentieren, validate_tools.py konzipieren | 1-2 Sessions |

### Phase 4 — Feature-Erweiterung (wenn Infrastruktur steht)

| # | Issue | Beschreibung | Aufwand |
|---|-------|-------------|---------|
| **4** | **#41 (Empf. 3)** | Topic Registry maschinenlesbar machen | 1 Session |
| **5** | **#26** | Security Signals in AGENT.json konzipieren | 1 Session |

---

## 5. Session-Zustand Summary

```
Offene Issues:     7
Davon Duplikate:   2 (#45→#43, #42→#41)
Analytisch fertig: 1 (#43 — RFC, implementierungsreif)
Teilweise abgedeckt: 1 (#41 — 4/5 Empfehlungen)
Komplett neu:      4 (#48, #49, #47, #46, #26)

Priorität:
  KRITISCH: #48 (Decision-Kompoundierung)
  HOCH:     #49 (Upgrade-Transparenz)
  MITTEL:   #47, #46, #26
  SCHLIESSEN: #45 (Duplikat)
```

---

## 6. Nächste Session

**Nächste Session sollte sich mit #48 (Decision-Kompoundierungs-Leck) befassen.**

Konkrete Deliverables:
1. WP-001 INDEX.md aktualisieren — Spec→Contract Decision dokumentieren
2. Decision-Promotion-Checklist in READ-AGENT.md aufnehmen
3. wiki_lint.py prüfen: Kann er Cross-Ref-Integrität zwischen WP-001..WP-004 prüfen?
4. Falls ja: wiki_lint.py erweitern, um "orphaned decisions" zu detektieren

---

> Letztes aktives Workpaper: `2026-04-17-RES-WIKI-karpathy-llm-wiki-vergleich.md` (7 Tage alt)
> Nächste Aktivität empfohlen: Innerhalb von 3 Tagen für Phase 1 (Aufräumen)
