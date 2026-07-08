# WP-001 — AAMS Projektübersicht
## Was haben wir vor uns?

- **ID:** WP-001
- **Erstellt:** 2026-02-22
- **Letztes Update:** 2026-04-29
- **Status:** Aktiv
- **Typ:** Architektur / Projektverständnis

---

## 1. Was ist dieses Projekt?

**AAMS** ist ein Agent Manifest — keine Software, keine Runtime, kein Framework.

Es ist ein **deklarativer Manifest** in Form einer JSON-Datei, die in jedes Repository gelegt werden kann und beschreibt, wie ein KI-Agent in diesem Projekt arbeitet.

> **Manifest-Prinzip (D9):** AAMS beschreibt Workspace- und Dokumentationskonventionen. Es schreibt Agenten kein Verhalten vor. Beschreibend, nicht preskriptiv.

Kerngedanke:
> `README.md` ist für Menschen. `AGENT.json` ist für Maschinen.

---

## 2. Das Problem das AAMS löst

Klassische Softwareentwicklung: Entwickler → Git → Issues → PR → Merge.  
Jeder Entwickler hat Kontext im Kopf. Der nächste liest die Commit-History.

Agentisches Arbeiten: Agent → Session → Ergebnis → Context lost.  
Session N+1 weiß nicht was Session N entschieden hat.

Ohne AAMS:
- Kein Gedächtnis über Sessions hinweg
- Keine definierte Struktur wo Dokumentation liegt
- Keine Regeln was der Agent anfassen darf
- Kein Einstiegspunkt für einen neuen Agenten
- Kontextverlust is unvermeidlich

Mit AAMS:
- Jede Session beginnt mit Kontext (LTM-Abfrage)
- Jede Entscheidung ist dokumentiert (Workpaper)
- Stabile Architekturwissen ist persistent (Whitepaper)
- Neue Agenten finden sofort Orientierung (READ-AGENT.md + WORKING/)

---

## 3. Zwei Formen des Standards

### Vollständig: `AGENT.json`
Komplettes Manifest mit allen Sektionen:
- `identity` — Agent-Identität und Versioning
- `runtime` — Modell, Provider, Endpoint
- `skills` — Fähigkeiten und Custom Skills
- `permissions` — was darf der Agent (Filesystem, Network, Process, Data)
- `memory` — Short-term / Long-term / Session
- `session` — Workpaper-Erstellung, Logging, Audit
- `tools` — externe Tools und API-Bindings
- `workspace` — Struktur, Onboarding, Regeln, Code-Hygiene
- `governance` — Contract-Version, Validierung, Review-Intervall

### Minimal: `.agent.json`
Kleinste portable Form. Bootstrap-Contract.  
Enthält nur: `workspace.structure`, `documentation_model`, `bootstrap_rules`, `secrets_policy`, `agent_conventions`.  
Kann in jedes Repo ohne den vollen Manifest gelegt werden.

---

## 4. Vier-Schichten-Dokumentationsmodell

Das Herzstück der AAMS-Architektur (Stand: 2026-03-03):

```
WORKING/
├── WHITEPAPER/     Stabile Systemwahrheit — Was ist dieses System?
│                   Nie löschen. Nur bei Architekturentscheidungen updaten.
│
├── WORKPAPER/      Operative Session-Arbeit — Was tue ich jetzt?
│                   Pro Session eine Datei. Nach Abschluss → closed/
│   └── closed/
│
├── DIARY/          Temporal Context Layer — Warum haben wir das so entschieden?
│                   Chronologisch, narrativ. Monatsweise (2026-03.md).
│                   Für strategische Motive, Blocker, reflexive Erkenntnisse.
│
└── MEMORY/         Langzeitgedächtnis — Was haben wir gelernt?
                    Dual-Track: ltm-index.md (Audit-Log, in Git) +
                    AGENT-MEMORY/ (ChromaDB-Vektorstore, in .gitignore)
```

| Schicht | Zeitdimension | Charakter | Pflicht |
|---------|--------------|-----------|--------|
| Whitepaper | Langfristig | Normativ / strukturell | Ja |
| Workpaper | Kurzfristig (Session) | Operativ / iterativ | Ja |
| Diary | Chronologisch | Narrativ / reflexiv | Ja |
| Memory (LTM) | Cross-Session | Auditierbar + querybar | Ja |

**Warum vier Schichten?**

Ein menschlicher Entwickler hat:
- Notizblock (Workpaper) — was er gerade macht
- Architektur-Doku (Whitepaper) — wie das System aufgebaut ist
- Tagebuch / Entscheidungslog (Diary) — warum so entschieden wurde
- Erfahrung / Gedächtnis (LTM) — was er über die Zeit gelernt hat

Ein Agent braucht dasselbe, aber explizit und persistent.

**Diary Layer** (Temporal Context Layer) wurde 2026-02-24 als verpflichtender dritter Dokumentations-Layer eingeführt. Der Gap: Entscheidungen entstehen *zwischen* Workpaper und Whitepaper. Strategische Motive verschwinden. Das Diary schließt diesen Gap — chronologisch, monatsweise, max. 10 Zeilen pro Eintrag.

### Naming Schema (eingeführt 2026-04-09, aktualisiert 2026-04-30)

Strukturierte Dateinamen ermöglichen thematisches Pattern-Matching über Sessions hinweg:

| Dokument | Schema | Beispiel |
|----------|--------|----------|
| Workpaper | `WP-{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md` | `WP-2026-04-09-ARCH-RFL-reflection-protocol-step.md` |
| Whitepaper | `WH-{NNN}-{TOPIC}-{description}.md` | `WH-005-ARCH-naming-schema.md` |

TOPIC-Tags (3-4 Buchstaben, UPPERCASE) sind der primäre Ordnungsschlüssel. Sie ermöglichen den RFL-Schritt (siehe unten) und Cross-Referenzierung zwischen Workpapers und Whitepapers.

### RFL — Reflection Protocol Step (eingeführt 2026-04-09)

RFL ist ein Konsistenzprüfungs-Schritt im Session-Start-Contract. Er löst das häufigste Failure-Pattern agentischer Sessions:

> Agent entscheidet in Session 47 das Gegenteil von Session 12 — und merkt es nicht.

**Alle vier Layer sind Speicher. Keiner ist Prüfung.** RFL schließt diese Lücke — als Protokollschritt, nicht als Layer.

3-Stufen-Fallback:
1. Pattern-Match auf TOPIC-Tag in Dateinamen (`*-{TOPIC}-*`)
2. LTM-Query-Ergebnisse
3. Letztes geschlossenes Workpaper (chronologisch)

Bei Widerspruch: Flag im neuen Workpaper (`## ⚠ RFL Consistency Flag`). Bei Konsistenz: kein Overhead.

---

## 5. Bootstrap-Ablauf (normativ)

Wenn ein Agent ein Repo mit AAMS betritt:

```
0. State-Check: WORKING/WORKPAPER/ prüfen
   → Enthält Workpapers? → on_session_start (Schritt 4)
   → Leer oder nicht vorhanden? → on_first_entry (Schritt 1)
1. READ-AGENT.md lesen
2. WORKING/-Struktur prüfen → anlegen wenn fehlend (idempotent)
3. Repository scannen → Inventory im ersten Workpaper
4. LTM befragen für Session-Thema
5. Workpaper öffnen / erstellen
6. Arbeiten
7. Workpaper abschließen (File Protocol + Next Steps)
8. LTM ingestieren
9. Workpaper → closed/
```

### WORKSPACE-Discovery (eingeführt 2026-04-12)

Probleme aus Feldberichten: Agenten erkannten `WORKING/`-Verzeichnisse in fremden Repos nicht. Lösung: WORKSPACE-Discovery als expliziter Mechanismus in `.agent.json`.

**Discovery-Logik:**
1. Agent prüft `workspace.structure` aus `.agent.json`
2. Jedes Verzeichnis hat `exists_action` (create / skip / warn)
3. Conflict-Check: Wenn `WORKING/` bereits existiert und Inhalte hat → `on_session_start`, nicht `on_first_entry`

**Implementiert in:** `.agent.json` → `agent_conventions.workspace_discovery`  
**Workpaper:** [2026-04-12-AAMS-WKSP](../WORKPAPER/closed/2026-04-12-AAMS-WKSP-workspace-discovery-implementation.md)  
**Siehe auch:** [WP-003](./WP-003-field-discourse.md) (Feldberichte die das Problem aufzeigten)

---

## 6. Interoperabilität

AAMS ist framework-neutral.  
Jedes Agenten-Framework das `WORKING/`-Struktur erkennt, kann AAMS-Repos direkt nutzen.

- **Eigenes Framework vorhanden:** AAMS-Struktur wird als Subagenten-Workspace erkannt
- **Kein Framework:** `.agent.json` + `READ-AGENT.md` mocken ein Minimal-Framework

Langfristiges Ziel: AAMS wird zu einem **de-facto Standard** den jedes Agenten-Framework versteht.

---

## 7. Kernprinzipien

1. **Deklarativ** — Manifest beschreibt Struktur, Agent handelt
2. **Idempotent** — mehrfaches Lesen ändert nichts
3. **Nie löschen** — Bootstrap-Regeln erzeugen nur, vernichten nie
4. **Secret-frei** — keine Credentials in Manifesten, Workpapers oder LTM
5. **Local-first** — funktioniert ohne Cloud, ohne externe Dienste
6. **Portabel** — eine Datei, funktioniert in jedem Repo

---

## 8. Versioning & Upgrade-Transparenz

> ⚠️ **Konzipiert, teilweise implementiert.** Versioning-System (SemVer + CHANGELOG.md + Git Tags) wurde in [Workpaper 2026-03-27](../WORKPAPER/closed/2026-03-27-versioning-system.md) designed und in [AAMS-UPD](../WORKPAPER/closed/2026-04-10-AAMS-UPD-update-install-detection-protocol.md) weiter ausgearbeitet (Update-Detection-Protocol, MIGRATION.md). CHANGELOG.md + MIGRATION.md existieren. `.aams-version` + Git-Tags ausstehend. Tracking: Issue [#49](https://github.com/DEVmatrose/AAMS/issues/49).

**Geplant:**
- `CHANGELOG.md` im Repo-Root
- Git-Tags pro Release (`v1.0.0`, `v1.3.0`, `v2.0.0`)
- `AAMS_VERSION` in `.env` als lokale Version-Referenz
- `.aams-state` für lokale Install-Detection
- `on_update` Handler in `.agent.json`

---

## 9. Decision-Promotion (eingeführt 2026-04-17)

Kritischer Gap entdeckt: Architektur-Entscheidungen aus Workpapers sickern nicht zuverlässig in Whitepapers durch. Neue Agenten lesen stale Whitepapers und treffen widersprüchliche Entscheidungen.

**Problem (Decision-Kompoundierungs-Leck):**
- Workpaper entscheidet X in Session N
- Whitepaper wird nicht aktualisiert
- Agent in Session N+5 liest altes Whitepaper, entscheidet ¬X

**Lösung:** Explizite Decision-Promotion als Pflichtschritt im Workpaper-Close-Protocol:
1. Jede Workpaper-Decision mit Architektur-Impact bekommt Tag `[PROMOTE→WP-xxx]`
2. Session-Close prüft: Alle PROMOTE-Tags aufgelöst?
3. Nicht-promotete Decisions werden als `⚠️ PENDING PROMOTION` im Diary markiert

**Tracking:** Issue [#48](https://github.com/DEVmatrose/AAMS/issues/48)  
**Guideline:** [WORKING/GUIDELINES/theoretical-stress-testing.md](../GUIDELINES/theoretical-stress-testing.md)

---

## 10. Cross-Referenzen

| Whitepaper | Beziehung |
|---|---|
| [WH-002 — Related Work](./WH-002-related-work.md) | Positionierung AAMS vs. MemGPT, LangChain, DVC, FIPA |
| [WH-003 — Field Discourse](./WH-003-field-discourse.md) | Feldberichte die Bootstrap/Discovery-Probleme aufzeigten |
| [WH-004 — Long-Horizon Reasoning](./WH-004-long-horizon-reasoning.md) | AAMS als LHR-Scaffolding; 4-Schichten als Reasoning-Unterstützung |

---

## 11. Aktueller Stand (2026-04-30)

| Bereich | Status |
|---|---|
| Agent Manifest (CONTRACT.md / SPEC.md Stub) | v2.2.0 — SPEC.md als Redirect-Stub, CONTRACT.md als neue Referenz |
| Referenz-Manifest (AGENT.json) | v2.2.0 — `_contract: AAMS/2.0` + deprecated `_spec` |
| JSON Schema (AGENT_SCHEMA.json) | v2.2.0 — `_contract` required, `_spec` deprecated, `topic_registry` optional |
| Minimal-Bootstrap (.agent.json) | v2.2.0 — `_contract: AAMS/2.0` + deprecated `_spec` + `topic_registry` + `agent_conventions` (descriptive) + `workpapers_observe` |
| READ-AGENT.md | Aktiv — Current Status AAMS/2.0, Topic Registry, Manifest-Prinzip (D9) |
| AGENTS.md | Aktiv — Tagline "agent-contract standard", Pre-Flight Path Check |
| WORKING/-Struktur | Vollständig aktiv inkl. DIARY/ und GUIDELINES/ |
| Workpapers (archived) | 52 in WORKPAPER/closed/ |
| Active workpapers | 2 in WORKING/WORKPAPER/ |
| Observe workpapers | 3 in WORKING/WORKPAPER/observe/ |
| Whitepapers | 8 (WH-001 bis WH-008) + INDEX.md |
| LTM | 136 Einträge ltm-index.md + ChromaDB |
| GitHub Issues #1-#20 | Geschlossen |
| GitHub Issues #21-#26 | #22-#24 geschlossen, #26 Backlog |
| GitHub Issues #41-#44 | #42, #44 Duplikate geschlossen; #41 offen (Field Report), #43 offen (RFC Tracker) |
| GitHub Issues #45 | ✅geschlossen (Duplikat von #43) |
| GitHub Issues #48-#49 | #48 Decision-Leck (teilweise gefixt), #49 Upgrade-Transparenz (teilweise gefixt) |
| GitHub Issues #50-#51 | #50 File Safety (neu), #51 Skill-Konzept (neu) |
| GitHub Pages | Live — devmatrose.github.io/AAMS |
| Field Reports | 5+ unabhängige Berichte |
| AAMS-MINI | ltm_mode markdown (Track A) + vector (Track B) |
| GUIDELINES/ | **12 Guidelines** (Documentation Model, Naming Schema, Workpaper Lifecycle, Decision-Promotion, File Protocol, LTM Rules, Topic Registry, Wiki Lint, AAMS Doctor, Git Safety, README Consistency, Diary Format) |
| Versioning | v2.2.0 — CHANGELOG.md + MIGRATION.md existieren, Git-Tags v2.1.0 + v2.2.0 |
| Decision-Promotion | Checklist in READ-AGENT.md ✅, wiki_lint.py L4b ✅ |
| Manifest-Prinzip (D9) | ✅ **AAMS beschreibt, es schreibt kein Verhalten vor** |
| Workpaper Lifecycle | ✅ active → observe → closed (drei Zustände) |
| Naming Schema | ✅ Whitepapers → WH-*, Workpapers → WP-* |
| **Neu (v2.2.0)** | **observe/ folder, Naming Schema (WH-*, WP-*), 12 Guidelines, Health-Score 10/10** |

---

## 10. Credentials und Secrets

### .env — GitHub Personal Access Token

Im Repository-Root liegt `.env` mit einem GitHub Personal Access Token (`GITHUB_TOKEN`).

**Verwendung:**
- `curl`-Aufrufe gegen die GitHub API (Release-Erstellung, CHANGELOG-Updates, Repo-Abfragen)
- Authentifizierung für `gh` CLI-Befehle

**WICHTIG:**
- Der Token-Wert steht **niemals** in Whitepapers, Workpapers, Memory oder im Manifest
- Der Token ist ein PAT (Personal Access Token) mit Repo-Scope
- Bei Verdacht auf Kompromittierung: Token im GitHub Settings → Developer Settings → Personal Access Tokens → Revoke
- Neue Repos müssen `.env` in `.gitignore` haben
- Dieser Token ist nur für AAMS-Repo-Operationen gedacht, nicht für andere Services

**Referenz:**
- `.agent.json` → `secrets_policy.never_in_workpapers` = true
- `.agent.json` → `secrets_policy.never_in_whitepapers` = true
- `.agent.json` → `secrets_policy.never_in_manifest` = true
- `.agent.json` → `secrets_policy.use` = ".env or external secret manager only"
