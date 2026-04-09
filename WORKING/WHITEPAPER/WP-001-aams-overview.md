# WP-001 — AAMS Projektübersicht
## Was haben wir vor uns?

- **ID:** WP-001
- **Erstellt:** 2026-02-22
- **Letztes Update:** 2026-04-09
- **Status:** Aktiv
- **Typ:** Architektur / Projektverständnis

---

## 1. Was ist dieses Projekt?

**Autonomous Agent Manifest Specification (AAMS)** ist ein offener Standard — keine Software, keine Runtime, kein Framework.

Es ist eine **deklarative Spezifikation** in Form einer JSON-Datei, die in jedes Repository gelegt werden kann und definiert, wie ein KI-Agent in diesem Projekt arbeitet.

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
- `governance` — Spec-Version, Validierung, Review-Intervall

### Minimal: `.agent.json`
Kleinste portable Form. Bootstrap-Contract.  
Enthält nur: `workspace.structure`, `documentation_model`, `bootstrap_rules`, `secrets_policy`, `agent_contract`.  
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

### Naming Schema (eingeführt 2026-04-09)

Strukturierte Dateinamen ermöglichen thematisches Pattern-Matching über Sessions hinweg:

| Dokument | Schema | Beispiel |
|----------|--------|----------|
| Workpaper | `{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md` | `2026-04-09-ARCH-RFL-reflection-protocol-step.md` |
| Whitepaper | `WP-{NNN}-{TOPIC}-{description}.md` | `WP-005-ARCH-naming-schema.md` |

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

## 8. Aktueller Stand (2026-04-09)

| Bereich | Status |
|---|---|
| Spezifikation (SPEC.md / SPEC-DE.md) | Vollständig, AAMS/1.0 |
| Referenz-Manifest (AGENT.json) | Vollständig, annotiert — inkl. `_deviations` |
| JSON Schema (AGENT_SCHEMA.json) | Vollständig — inkl. `_deviations` |
| Minimal-Bootstrap (.agent.json) | Aktiv, AAMS-MINI/1.0 — inkl. Pre-Check Step 0, RFL in on_session_start, Naming Schema |
| READ-AGENT.md | Aktiv — dual-track LTM, Diary Layer, 3-State-Tabelle, Compatibility-Klausel, **Naming Schema**, **RFL Protocol Step** |
| AGENTS.md | Aktiv — Conditional Bootstrap (State-Check vor Execution) |
| WORKING/-Struktur | Vollständig aktiv inkl. DIARY/ und DATABASE/ |
| Workpapers (archived) | 25+ in WORKPAPER/closed/ |
| Whitepapers | 4 (WP-001 bis WP-004) |
| LTM | 67+ Einträge ltm-index.md + ChromaDB |
| GitHub Issues #1-#20 | Geschlossen |
| GitHub Issues #21-#26 | Teils offen |
| GitHub Issues #28-#31 | Field Reports — ausgewertet, Fixes implementiert |
| GitHub Issues #36-#39 | v1.2.0: Naming Schema (#36), RFL (#37), WP-001 Update (#38), Release (#39) |
| GitHub Pages | Live — devmatrose.github.io/AAMS |
| Field Reports | 5 unabhängige Berichte |
| AAMS-MINI | ltm_mode markdown (Track A) + vector (Track B) |
| **Neu (v1.2.0)** | **Naming Schema (Workpapers + Whitepapers), RFL Protocol Step (3-Stufen-Konsistenzprüfung), SCIENCE-Konzept als Framework-Feature verlagert** |
