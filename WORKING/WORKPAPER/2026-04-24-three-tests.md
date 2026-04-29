# Workpaper: Drei Tests — Unsere eigenen Überlegungen geprüft

**Datum:** 2026-04-24  
**Autor:** @DEVmatrose  
**Typ:** Theoretical Stress Test — Selbstkritische Validierung  
**Referenz:** `2026-04-24-session-plan.md` (Phase 2 Deliverables)  
**Priorität:** KRITISCH — bevor wir Änderungen committen

---

## Session Goal

Drei systematische Tests unserer heute implementierten Änderungen:
1. **Konsistenz-Test:** Widersprechen sich die Änderungen gegenseitig?
2. **Agent-Verhaltens-Test:** Verhält sich ein Agent korrekt mit den neuen Dateien?
3. **Backward-Compatibility-Test:** Brechen wir bestehende Deployments?

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-24-three-tests.md` | ✅ |

---

## Test 1: Konsistenz-Test — Widersprechen sich die Änderungen gegenseitig?

### Hypothese

Die 7 Deliverables sind konsistent — sie bilden ein kohärentes Upgrade-System.

### Analyse

#### 1.1 `_spec` vs `_contract` in `.agent.json` — Konflikt?

**Änderung:** `.agent.json` hat jetzt BEIDE Felder:
```json
"_spec": "AAMS-MINI/1.0",
"_contract": "AAMS/1.3",
"_version_date": "2026-04-24"
```

**Frage:** Ist das ein Widerspruch oder ein Übergang?

**Analyse:**
- `_spec: "AAMS-MINI/1.0"` — das MINISPEC. Es ist das Bootstrap-File, das per curl runtergeladen wird. Es sagt "ich bin ein AAMS-MINI/1.0 Bootstrap-Contract."
- `_contract: "AAMS/1.3"` — das REFERENZ-SPEC. Es sagt "ich orientiere mich an AAMS/1.3."
- Das ist **kein Konflikt** — es ist ein **Brücken-Muster**. Das MINISPEC bleibt stabil (sonst brechen alle curl-Adoptionen). Das REFERENZ-Contract kann sich entwickeln.

**Aber:** Ein Agent der nur `_contract` prüft (wie unser new `version_detection` in on_update) wird `AAMS/1.3` mit der lokalen `.aams-version` vergleichen. Ein Agent der `_spec` prüft, wird `AAMS-MINI/1.0` sehen — was sich nie ändert.

**Problem:** `version_detection` prüft `_contract` ODER `_spec`. Aber `_spec` ist ein konstanter Wert. Es wird NIE ein Update detektieren wenn nur `_spec` geprüft wird.

**Entscheidung:** `version_detection` muss `_contract` PRIORISIEREN. `_spec` ist nur für backward compat mit alten Agents.

**Befund:** ⚠️ **Konsistenz-Lücke** — `version_detection` muss `_contract > _spec` Priorität haben.

---

#### 1.2 on_update vs on_session_start — Reihenfolge?

**Änderung:** `.agent.json` hat jetzt drei entry-points:
- `on_first_entry`
- `on_session_start`
- `on_update`

**Frage:** Was passiert wenn BOTH `on_update` (Version-Bump) und `on_session_start` (Returning) zutreffen?

**Analyse:**
- Ein curl-Update ist IMMER ein `on_session_start` Fall (WORKING/ existiert).
- Der UPDATE-Check MUSS vor `on_session_start` laufen.
- Aktuell steht `on_update` NICHT in der Reihenfolge-Logik.

**Problem:** Es gibt keine explizite Priorisierung: `on_update` before `on_session_start`.

**Entscheidung:** `on_session_start` muss als ersten Schritt einen Update-Check haben:
```json
"on_session_start": [
    "0. VERSION-CHECK: Vergleiche _contract mit .aams-version. Bei Diskrepanz: on_update ausführen, dann weiter zu Schritt 1.",
    "1. Read READ-AGENT.md",
    ...
]
```

**Befund:** ✅ **Konsistent** — aber `on_update` muss in `on_session_start` als Schritt 0 eingebettet werden.

---

#### 1.3 Decision-Promotion-Checklist vs wiki_lint.py L4b — Redundanz?

**Änderung:** 
- READ-AGENT.md: Manuelles Checkbox-System
- wiki_lint.py: Automatischer Check L4b

**Frage:** Zwei Systeme für dasselbe?

**Analyse:**
- Checklist ist PROZESS — sie erzwingt dass der Agent sich bewusst wird.
- wiki_lint.py ist DETEKTION — sie findet orphane Decisions automatisch.
- Sie ergänzen sich: Checklist sagt "prüfe", wiki_lint.py sagt "hier sind die Ergebnisse."

**Befund:** ✅ **Konsistent** — komplementär, nicht redundant.

---

#### 1.4 validate_tools.py vs wiki_lint.py — Aufgabentrennung?

**Änderung:** Zwei unabhängige Tools:
- `wiki_lint.py`: Dokumentations-Health (L1-L7)
- `validate_tools.py`: Tool-Integrität (D1-D4)

**Frage:** Können sie zusammengefasst werden?

**Analyse:**
- wiki_lint.py prüft DOKUMENTATION (Whitepapers, Workpapers, Cross-Refs).
- validate_tools.py prüft TOOLS (Python-Dateien, Offset-Paths, Ordner-Struktur).
- Getrennte Tools = getrennte Verantwortlichkeiten = besser wartbar.

**Befund:** ✅ **Konsistent** — klare Aufgabentrennung.

---

#### 1.5 AGENTS.md Pre-Flight vs READ-AGENT.md Decision-Promotion — Duplikat?

**Änderung:**
- AGENTS.md hat neuen Abschnitt "Before Creating Any Directory or File"
- READ-AGENT.md hat "Decision-Promotion-Checklist"

**Frage:** Sind beide nötig?

**Analyse:**
- AGENTS.md ist für alle AGENTS.md-kompatiblen Tools (Copilot, Cursor, Claude Code).
- READ-AGENT.md ist spezifisch für AAMS-Workflows.
- Die Pre-Flight-Regel ist eine ROOT-STRUKTUR-Regel — die gehört in AGENTS.md.
- Die Decision-Promotion ist eine SESSION-REGEL — die gehört in READ-AGENT.md.

**Befund:** ✅ **Konsistent** — verschiedene Ebenen (Struktur vs. Session).

---

#### 1.6 CHANGELOG.md im Root vs WORKING/ — Konsistenz?

**Änderung:** CHANGELOG.md im Repo-Root, nicht in WORKING/.

**Frage:** Widerspruch zu "alles in WORKING/"?

**Analyse:**
- CHANGELOG.md ist ein PRODUKTIONS-Artefakt — es gehört ins Repo.
- Es wird von curl-Usern gelesen, die noch KEIN WORKING/ haben.
- Es ist Teil der AAMS-Publizierung, nicht der AAMS-Infrastruktur.

**Befund:** ✅ **Konsistent** — CHANGELOG ist Publikation, nicht Infrastruktur.

---

### Test 1 Ergebnis: Konsistenz

```
Geprüft:  6 Änderungs-Paare
Konsistent: 5/6 ✅
Inkonsistent: 1/6 ⚠️

Problem: version_detection muss _contract PRIORISIEREN über _spec.
Fix: on_update in .agent.json muss _contract als primären Vergleichswert nutzen.
```

---

## Test 2: Agent-Verhaltens-Test — Verhält sich ein Agent korrekt?

### Hypothese

Ein Agent der alle heute geänderten Dateien liest, wird korrekt handeln.

### Test-Szenario A: Fresh Install

```bash
# User cloned ein leeres Repo
# curl -sO https://raw.githubusercontent.com/DEVmatrose/AAMS/main/.agent.json
# .agent.json enthält jetzt _contract + _version_date + on_update
```

**Was der Agent tut:**
1. `.agent.json` lesen → `_spec: "AAMS-MINI/1.0"` → Bootstrap-Vertrag erkannt
2. `_contract: "AAMS/1.3"` → Referenz-Spec, ignoriert bei Fresh Install
3. WORKING/ existiert NICHT → `on_first_entry`
4. Ordner erstellen, READ-AGENT.md lesen
5. READ-AGENT.md hat Decision-Promotion-Checklist → Agent weiß dass er Decisions promoten muss
6. First Workpaper schreiben

**Ergebnis:** ✅ **Korrekt** — `_contract` wird bei Fresh Install ignoriert, kein Problem.

---

### Test-Szenario B: Returning Session (ohne Update)

```bash
# User holt .agent.json bereits in ein bestehendes AAMS-Repo
# WORKING/ existiert, .aams-version = "1.3"
# Remote .agent.json: _contract = "1.3" (gleich)
```

**Was der Agent tut:**
1. `.agent.json` lesen → `_contract: "AAMS/1.3"`
2. WORKING/ existiert → `on_session_start`
3. `on_session_start` Schritt 0: VERSION-CHECK — `.aams-version` == `_contract` → KEIN Update
4. Normaler Session-Start: READ-AGENT.md, LTM, Workpaper

**Ergebnis:** ⚠️ **Problem** — `on_session_start` hat KEINEN version_detection Schritt!

Aktuell steht in `.agent.json`:
```json
"on_session_start": [
    "1. Read READ-AGENT.md",
    "2. Query memory for session topic",
    ...
]
```

Das `version_detection` Feld ist ein SEPARATES Feld, kein Schritt in `on_session_start`. Ein Agent der nur `on_session_start` ausführt, wird NIE ein Update detektieren.

**Fix erforderlich:** Schritt 0 in `on_session_start` muss version_detection aufrufen.

---

### Test-Szenario C: Returning Session (mit Update)

```bash
# User curl't .agent.json
# Remote: _contract = "AAMS/2.0"
# Lokal: .aams-version = "1.3"
```

**Was der Agent tun SOLLTE:**
1. VERSION-CHECK: 2.0 ≠ 1.3 → UPDATE DETECTED
2. on_update ausführen: CHANGELOG lesen, READ-AGENT.md aktualisieren
3. .aams-version auf "2.0" setzen
4. on_session_start fortsetzen

**Was der Agent JETZT tut:**
1. WORKING/ existiert → `on_session_start` (kein Update-Check!)
2. Session normal fortsetzen — UPDATE WIRD NICHT GEMERKT

**Ergebnis:** ❌ **Fehler** — Update wird nicht erkannt wenn kein version_detection Schritt in on_session_start.

---

### Test-Szenario D: Tool-Ausführung nach Pre-Flight Check

```python
# Ein Tool in WORKING/TOOLS/ mit:
# ROOT = Path(__file__).resolve().parent.parent

# Ausgeführt von: WORKING/TOOLS/
# ROOT = WORKING/ (korrekt!)

# Ausgeführt von: Projekt-Root/
# ROOT = Projekt-Root (korrekt!)

# Ausgeführt von: tools/ (falscher Ort!)
# ROOT = Projekt-Root (falsch — sollte Projekt-Root sein, ist aber unklar)
```

**Ergebnis:** ✅ **Konsistent** — Pre-Flight Check in AGENTS.md verhindert genau dieses Problem. Agent prüft vor Execution ob Offset-Path noch korrekt.

---

### Test-Szenario E: wiki_lint.py L4b vs READ-AGENT.md Checklist

**Szenario:** Agent hat in einer Session E-3 entschieden ("_spec als deprecated halten").

**Ohne wiki_lint.py:**
- Agent schließt Session → Checklist sagt "Entscheidung in Whitepaper?" → Agent prüft manuell → WP-001 INDEX.md zeigt "✅ Decision getroffen"
- Aber: Agent hat E-3 in INDEX.md nicht explizit als "gelöst" markiert.

**Mit wiki_lint.py:**
- Agent schließt Session → wiki_lint.py → L4b findet E-3 im RFCT Workpaper
- Prüft INDEX.md → "Decision E-3" steht NICHT explizit als "gelöst"
- WARNUNG: "E-3 nicht in Whitepaper gepromoted"

**Ergebnis:** ✅ **Korrekt** — wiki_lint.py fängt den Fall den die manuelle Checklist verpassen könnte.

---

### Test 2 Ergebnis: Agent-Verhaltens-Test

```
Geprüft: 5 Szenarien
Korrekt: 4/5 ✅
Fehlerhaft: 1/5 ❌

Problem: on_session_start hat KEINEN version_detection Schritt.
Ein curl-Update wird nicht erkannt.
Fix: on_session_start Schritt 0 = version_detection.
```

---

## Test 3: Backward-Compatibility-Test — Brechen wir bestehende Deployments?

### Hypothese

Bestehende AAMS-Deployments funktionieren weiterhin.

### Test 3.1: `_contract` Feld — Breaking für alte Agents?

**Frage:** Was passiert wenn ein alter Agent (der `_contract` nicht kennt) `.agent.json` liest?

**Analyse:**
- JSON-Schema erlaubt `patternProperties: { "^_": true }` — alle `_`-Fields sind erlaubt.
- Alter Agent ignoriert unbekannte Felder.
- `_contract` wird einfach übergangen.
- **Kein Breaking Change.**

**Ergebnis:** ✅ **Kein Breaking Change** — `_contract` ist ein neues optional Feld.

---

### Test 3.2: `on_update` Feld — Breaking für alte Agents?

**Frage:** Was passiert wenn ein alter Agent `on_update` nicht kennt?

**Analyse:**
- `on_update` ist ein neuer entry-point in `agent_contract`.
- Alter Agent führt nur `on_first_entry` und `on_session_start` aus.
- Er ignoriert `on_update` — das ist beabsichtigt.
- **Kein Breaking Change.**

**Aber:** Ein neuer Agent der `on_update` ausführt, wird `.aams-version` lesen und schreiben.
Ein alter Agent der danach kommt, wird `.aams-version` nicht kennen — aber das ist ok, weil es ein optionales Feature ist.

**Ergebnis:** ✅ **Kein Breaking Change** — `on_update` ist ein neuer entry-point, nicht replace.

---

### Test 3.3: version_detection Feld — Breaking?

**Frage:** Was wenn ein alter Agent `version_detection` nicht kennt?

**Analyse:**
- `version_detection` ist ein neues Feld in `agent_contract`.
- Alter Agent ignoriert es.
- **Kein Breaking Change.**

**Aber:** Ein neuer Agent der `version_detection` ausführt, erwartet `.aams-version` im Zielrepo.
Wenn `.aams-version` nicht existiert: Kein Problem — "keine Diskrepanz" = kein Update.

**Ergebnis:** ✅ **Kein Breaking Change** — aber `.aams-version` muss beim ersten curl-Update erstellt werden.

---

### Test 3.4: AGENTS.md Pre-Flight Rule — Breaking für bestehende Repos?

**Frage:** Was wenn ein Repo bereits `tools/` im Root hat?

**Analyse:**
- AGENTS.md sagt: "Never create tool folders in root."
- Es verbietet NICHT das Vorhandensein.
- Es sagt: "Prüfe WORKING/TOOLS/ vor dem Erstellen."
- Bestehende `tools/` im Root bleiben unberührt.
- **Kein Breaking Change.**

**Aber:** validate_tools.py D4 wird `tools/` als "verdächtigen Root-Ordner" melden.
Das ist eine WARNUNG, kein Fehler. Der Agent muss entscheiden: behalte oder verschiebe.

**Ergebnis:** ✅ **Kein Breaking Change** — nur Warnung, keine automatische Bewegung.

---

### Test 3.5: CHANGELOG.md im Root — Breaking für bestehende Repos?

**Frage:** Was wenn ein Repo bereits eine `CHANGELOG.md` hat?

**Analyse:**
- overwrite mit AAMS-CHANGELOG = POTENZIELLER DATA LOSS
- Aber: CHANGELOG.md wird nur in AAMS selbst committed, nicht per curl verteilt.
- curl holt nur `.agent.json`.
- **Kein Breaking Change für Deployments.**

**Ergebnis:** ✅ **Kein Breaking Change** — CHANGELOG.md ist nur im AAMS-Repo.

---

### Test 3.6: Spec→Contract Rename — Breaking?

**Frage:** WP-001 INDEX.md sagt jetzt "✅ Decision getroffen: Option B" — aber das Whitepaper selbst wurde NICHT umbenannt.

**Analyse:**
- WP-001 heißt noch `WP-001-aams-overview.md`
- Es enthält noch "Specification" im Text
- Nur die INDEX.md sagt "Decision getroffen"
- Das ist DER Grund warum wir das Decision-Promotion-Problem haben!

**Ergebnis:** ⚠️ **Teilweise Breaking** — WP-001 INDEX.md ist aktualisiert, aber das Whitepaper selbst ist noch "Spec". Ein Agent der WP-001 LIEST (nicht die INDEX) wird immer noch "Specification" sehen.

**Das ist genau das Problem von #48:** Die Decision ist in der INDEX, aber das Whitepaper selbst widerspricht der INDEX.

**Fix:** WP-001 selbst muss aktualisiert werden (das ist der Spec→Contract Refactor aus Issue #43).

---

### Test 3 Ergebnis: Backward-Compatibility-Test

```
Geprüft: 6 Szenarien
Kein Breaking: 5/6 ✅
Teilweise Breaking: 1/6 ⚠️

Problem: WP-001 INDEX.md sagt "Decision getroffen", aber WP-001 selbst noch "Specification".
Das ist genau das Decision-Kompoundierungs-Leck — die INDEX widerspricht dem Inhalt.
Fix: WP-001 selbst muss Refactor unter #43 durchlaufen.
```

---

## Zusammenfassung der drei Tests

### Test-Ergebnisse

| Test | Geprüft | Bestanden | Problem |
|------|---------|-----------|---------|
| 1. Konsistenz | 6 Paare | 5/6 ✅ | version_detection muss _contract PRIORISIEREN |
| 2. Agent-Verhalten | 5 Szenarien | 4/5 ✅ | on_session_start braucht version_detection Schritt |
| 3. Backward Compat | 6 Szenarien | 5/6 ✅ | WP-001 widerspricht sich selbst (INDEX vs. Inhalt) |

### Kritische Probleme (müssen gefixt werden)

**P1: on_session_start ohne version_detection**
- **Fehler:** curl-Updates werden nicht erkannt
- **Fix:** `on_session_start` Schritt 0 = version_detection + on_update bei Bump
- **Dringlichkeit:** KRITISCH — Issue #49 wird nicht funktionieren

**P2: version_detection _contract vs _spec Priorität**
- **Fehler:** _spec ist konstant, wird nie ein Update detektieren
- **Fix:** _contract PRIORISIEREN, _spec nur für backward compat
- **Dringlichkeit:** HOCH — zusammen mit P1

### Warnungen (sollten gefixt werden)

**W1: WP-001 INDEX vs. Inhalt**
- **Problem:** INDEX sagt "Decision getroffen", Whitepaper sagt noch "Specification"
- **Fix:** WP-001 Refactor unter #43
- **Dringlichkeit:** MEDIUM — wird durch Spec→Contract Refactor automatisch gelöst

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-24-three-tests.md` | ✅ |

---

## Nächste Schritte

1. **P1 + P2 fixen** → `on_session_start` um version_detection Schritt 0 erweitern + `_contract` Priorität in version_detection
2. **P2 auch in `.agent.json` dokumentieren** → `_spec` als legacy-markierung
3. **Committen** nach P1+P2 Fix
4. **Spec→Contract Refactor** als näch großes Feature (#43)
