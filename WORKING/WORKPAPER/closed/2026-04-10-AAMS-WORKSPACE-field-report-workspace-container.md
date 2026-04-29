# Field Report + Refactoring Proposal
# AAMS Issue: Missing WORKSPACE Container Layer

**Datum:** 2026-04-10  
**Autor:** @ogerly / DEVmatrose  
**Betrifft:** [AAMS Repository](https://github.com/DEVmatrose/AAMS) — `.agent.json` Bootstrap-Spec  
**Typ:** Architektur-Lücke / Refactoring Proposal  
**Priorität:** Hoch

---

## TL;DR

AAMS erstellt `./WORKING/` direkt im Repo-Root. Sobald ein Projekt weitere nicht-AAMS-Assets braucht (Branding, Tools, Daten, Tests), liegen diese als unstrukturierte Geschwister neben `WORKING/`. Das führt zu Unübersichtlichkeit und Verwirrung darüber, was zu was gehört. Die Community-Lösung (OpenClaw, MantisClaw, Mantis-OS) ist ein `WORKSPACE/`-Container. AAMS muss diesen Suchpfad kennen und selbst vorschlagen.

---

## 1. Empirischer Befund (field-getestet an Mantis-Familie)

Ist-Zustand über 4 Repos:

```
MantisClaw/
├── WORKSPACE/          ← Eigenständig erfunden, nicht von AAMS spezifiziert
│   └── WORKING/        ← AAMS Struktur drin
├── config/
├── core/
└── identity/

Mantis-OS/
├── WORKSPACE/          ← Eigenständig erfunden, erweitert mit Extras
│   ├── WORKING/        ← AAMS Struktur drin
│   ├── AGENDA/         ← Extra: Operations-Memory
│   └── TESTS/          ← Extra: Test-Artefakte
├── config/
└── core/

MantisNostr/
├── WORKING/            ← AAMS flat (kein Container)
├── agent/
└── board/

Mantis-Family/ (Root-Workspace)
├── WORKING/            ← AAMS flat  ← PROBLEM
├── branding/           ← liegt lose rum ← SYMPTOM
├── MantisClaw/
├── MantisNostr/
└── Mantis-OS/
```

**Feststellung:**
- 2 von 4 Repos haben `WORKSPACE/` eigenständig erfunden
- 2 von 4 Repos haben AAMS flat (kein Container)
- Das ist eine dokumentierte Architektur-Inkonsistenz, entstanden durch eine Lücke in der AAMS-Spec

---

## 2. Problem-Analyse

### 2.1 Was fehlt in AAMS

Die `.agent.json` Bootstrap-Spec definiert:
```json
"workspace": {
  "root": "./WORKING",
  ...
}
```

Es gibt keinen Mechanismus für:
- Erkennung eines bestehenden `WORKSPACE/`-Ordners
- Erstellung eines solchen Containers wenn nicht vorhanden
- Ablage anderer Projekt-Assets neben `WORKING/` aber innerhalb eines strukturierten Containers
- Konflikt-Erkennung (existiert `./WORKING/` UND `./WORKSPACE/WORKING/`?)

### 2.2 Warum entsteht das Problem

Wenn ein Agent AAMS bootstrappt:
1. Er legt `./WORKING/` an
2. Später legt er oder der User weitere Assets an: `tools/`, `branding/`, `data/`, etc.
3. Diese landen als Root-Geschwister neben `WORKING/` — kein Container, keine Zugehörigkeit
4. Das Repo-Root wird unübersichtlich

MantisClaw und Mantis-OS haben das **ohne AAMS-Anleitung** eigenständig mit `WORKSPACE/` gelöst. Das ist ein Signal: der Bedarf existiert, AAMS liefert keine Antwort.

### 2.3 OpenClaw-Konvention

OpenClaw (populärstes Agent-Framework) nutzt `workspace/` als Container-Konvention. Viele AAMS-User im OpenClaw-Kontext erwarten dieses Muster bereits. AAMS macht hier keinen Vorschlag — die Lösung entsteht ad-hoc und inkonsistent.

### 2.4 Konflikt-Szenario

```
my-repo/
├── WORKING/            ← von altem AAMS-Bootstrap
├── WORKSPACE/
│   └── WORKING/        ← von neuem Bootstrap nach Refactoring
```

Ein Agent der diesen Zustand vorfindet weiß nicht:
- Welches `WORKING/` ist das aktuelle?
- Welches hat den aktuellen LTM-Stand?
- Wo soll er neue Workpapers ablegen?

**Dieses Szenario tritt in Repos auf, die von flachem auf Container-Modell migrieren.**

---

## 3. Refactoring Proposal

### 3.1 Neue Bootstrap-Logik (Pseudocode)

```
AAMS Bootstrap — Workspace Discovery:

1. Suche nach bestehendem Container:
   - Prüfe ./WORKSPACE/WORKING/ → existiert? → nutze ./WORKSPACE/ als root
   - Prüfe ./workspace/WORKING/ → existiert? → nutze ./workspace/ als root
   - Prüfe ./WORKING/ (direkt) → existiert? → nutze ./ als root (legacy)

2. Kein Container gefunden → Neues Repo:
   - Erstelle ./WORKSPACE/
   - Erstelle ./WORKSPACE/WORKING/ + alle Sub-Ordner

3. Konflikt-Check (NEU):
   - Existiert ./WORKING/ UND ./WORKSPACE/WORKING/?
   → STOP. Schreibe Konflikt-Report nach ./WORKSPACE/WORKING/LOGS/aams-conflict-YYYY-MM-DD.md
   → Frage User: "Welches ist das primäre WORKING?  Migration nötig."
   → Merge-Strategie: neuere Workpapers gewinnen, LTM zusammenführen

4. AAMS-Version-Check (bestehend + erweitert):
   - Prüfe .agent.json._spec auf neue AAMS-Version
   - Prüfe ob workspace.root auf altes Flat-Schema zeigt → Migrationshinweis
```

### 3.2 Änderungen an `.agent.json`

**Aktuell:**
```json
"workspace": {
  "root": "./WORKING",
```

**Vorschlag:**
```json
"workspace": {
  "root": "./WORKSPACE",
  "working": "./WORKSPACE/WORKING",
  "discovery": {
    "search_order": ["./WORKSPACE/WORKING", "./workspace/WORKING", "./WORKING"],
    "preferred_container": "WORKSPACE",
    "legacy_flat": "./WORKING",
    "conflict_check": true
  },
```

### 3.3 Neue `bootstrap_rules`

```json
"bootstrap_rules": {
  ...
  "workspace_discovery": true,
  "workspace_container": "WORKSPACE",
  "workspace_container_note": "All agent-related assets (WORKING, tools, branding, data) go inside WORKSPACE/. This keeps the repo root clean and makes clear what belongs to the agent workspace.",
  "conflict_check": "if both ./WORKING and ./WORKSPACE/WORKING exist, log conflict and halt",
  "migration_check": "if workspace.root points to ./WORKING (legacy), suggest migration to ./WORKSPACE/WORKING"
}
```

### 3.4 Migration-Guide (für bestehende Repos)

```bash
# Repos mit flachem ./WORKING/
mkdir WORKSPACE
mv WORKING WORKSPACE/WORKING

# .agent.json anpassen:
# "root": "./WORKING"  →  "root": "./WORKSPACE"
# + "working": "./WORKSPACE/WORKING"
```

Betrifft in der Mantis-Familie:
- `MantisNostr/` → `WORKING/` → `WORKSPACE/WORKING/`
- `Mantis-Family/` (Root) → `WORKING/` + `branding/` → `WORKSPACE/WORKING/` + `WORKSPACE/branding/`

---

## 4. Testfälle (vor Implementierung zu validieren)

| Szenario | Input | Erwartetes Verhalten |
|----------|-------|---------------------|
| Neues Repo, kein WORKING | leeres Repo | `WORKSPACE/WORKING/` wird erstellt |
| Bestehendes `WORKSPACE/WORKING/` | MantisClaw-like | korrekt erkannt, nichts überschrieben |
| Bestehendes `./WORKING/` (legacy) | MantisNostr-like | Migrationshinweis, legacy wird genutzt bis Migration |
| Konflikt: beide existieren | beide Ordner vorhanden | Halt, Conflict-Report erstellt |
| OpenClaw `workspace/` (lowercase) | OpenClaw-Repo | Case-insensitive Discovery greift |

---

## 5. Impact-Analyse

| Bereich | Impact | Maßnahme |
|---------|--------|----------|
| Neue Repos | Low — bessere Struktur von Anfang an | Neuer Default in .agent.json |
| Bestehende Repos (flat) | Medium — einmalige Migration nötig | Migration-Script + Guide |
| Bestehende Repos (WORKSPACE/) | None — bereits konform | Nur Discovery-Logik nötig |
| OpenClaw-Kompatibilität | Positiv — gleiche Konvention | Case-handling für `workspace/` |
| AAMS-Version | Breaking change → AAMS-MINI/2.0 | Versionierung in `_spec` hochsetzen |

---

## 6. Offene Fragen

1. **Lowercase vs. Uppercase?** `WORKSPACE/` (Mantis-Konvention) vs. `workspace/` (OpenClaw)? → Empfehlung: Discovery case-insensitiv, preferred output `WORKSPACE/`
2. **Was darf in `WORKSPACE/` neben `WORKING/`?** Alles was "agent-owned" ist — Tools, Branding, Daten, Tests. Kein Application-Code.
3. **Rückwärtskompatibilität?** AAMS-MINI/1.0 Repos funktionieren weiterhin mit `./WORKING/` — kein harter Break, nur Deprecation Warning.

---

## 7. Empfehlung

**Sofort (Mantis-Familie):**
- Mantis-Family Root: `WORKING/` + `branding/` → `WORKSPACE/WORKING/` + `WORKSPACE/branding/`
- MantisNostr: `WORKING/` → `WORKSPACE/WORKING/`

**AAMS-Repo:**
- Issue erstellen mit diesem Field Report
- `_spec` auf AAMS-MINI/2.0 hochsetzen
- `.agent.json` Discovery-Logik + Konflikt-Check ergänzen
- Migration-Guide als `MIGRATION.md` im AAMS-Repo

---

*Erstellt auf Basis empirischer Analyse der Mantis-Familie (4 Repos, 2026-04-10)*  
*Autor: @ogerly / DEVmatrose*
