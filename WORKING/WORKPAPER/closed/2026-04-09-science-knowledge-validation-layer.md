# Workpaper: SCIENCE — Knowledge Validation Layer

- **Datum:** 2026-04-09
- **Agent:** GitHub Copilot (Claude Opus 4.6)
- **Status:** CLOSED — VERWORFEN
- **Bezug:** Workpaper `2026-04-09-Knowledge Validation Layer.md` (unstrukturierte Gedanken)
- **Ergebnis:** Konzept als eigenständiger Layer in der Spec verworfen. Zu komplex, bricht `local-first` und `curl -sO`-Versprechen. SCIENCE wandert als Feature in das Agent-Loop-Framework (das AAMS als Körper nutzt). Stattdessen: RFL (Reflection) als minimaler Protokollschritt im Agent Contract → siehe Workpaper `2026-04-09-rfl-reflection-protocol-step.md`

---

## Session Goal

Einen neuen Strukturordner `WORKING/SCIENCE/` für AAMS konzipieren und architektonisch durchdenken. SCIENCE ist die fünfte Schicht im Dokumentationsmodell — ein **Knowledge Validation Layer**, der epistemische Prüfung, externe Referenzierung und Differenzanalyse zwischen Idee und Realität ermöglicht.

---

## 1. Ausgangslage

### Aktuelles Vier-Schichten-Modell (WP-001)

| Schicht | Ordner | Funktion | Zeitdimension |
|---------|--------|----------|---------------|
| Workpaper | `WORKING/WORKPAPER/` | Was tue ich jetzt? | Kurzfristig (Session) |
| Whitepaper | `WORKING/WHITEPAPER/` | Wie ist das System aufgebaut? | Langfristig (stabil) |
| Diary | `WORKING/DIARY/` | Warum wurde so entschieden? | Chronologisch |
| Memory | `WORKING/MEMORY/` | Was haben wir gelernt? | Cross-Session |

### Die Lücke

Keine dieser Schichten beantwortet:

- **Stimmt das überhaupt?** (epistemische Validierung)
- **Gibt es das schon?** (externe Einordnung)
- **Wie weit sind wir von der Realität entfernt?** (Differenzanalyse)
- **Was sagt die Forschung dazu?** (wissenschaftlicher Kontext)

Ein Agent kann aktuell planen, bauen, dokumentieren und erinnern — aber nicht **prüfen, ob seine Annahmen valide sind**.

---

## 2. Was SCIENCE ist (und was nicht)

### SCIENCE ist:

> Ein eigenständiger **Validierungs- und Erkenntnislayer** über dem Agentensystem.

Vier Kernfunktionen:

1. **Validierung** — Stimmen die technischen Annahmen?
2. **Einordnung** — Wo steht das im aktuellen Forschungsfeld?
3. **Differenzanalyse** — Delta zwischen Idee, Umsetzung und Realität
4. **Erkenntnisgewinn** — Neue Hypothesen ableiten

### SCIENCE ist nicht:

- ❌ Kein Logging (das ist DIARY)
- ❌ Keine Self-Reflection (das ist Workpaper-Review)
- ❌ Kein Testing (das ist CI/CD)
- ❌ Kein Memory (das ist LTM)

### Analogie

> Workpaper = Laborjournal. Whitepaper = Lehrbuch. Diary = Tagebuch. Memory = Erfahrung. **SCIENCE = Peer Review + Literaturrecherche.**

---

## 3. Geplante Ordnerstruktur

```
WORKING/
├── WHITEPAPER/
├── WORKPAPER/
├── DIARY/
├── MEMORY/
├── GUIDELINES/
├── LOGS/
├── TOOLS/
└── SCIENCE/                    ← NEU: Knowledge Validation Layer
    ├── INDEX.md                ← Verzeichnis aller Science Reports
    ├── sources/                ← Externe Quellen (Papers, Links, Referenzen)
    │   └── {topic}-sources.md
    ├── reviews/                ← Validierungsberichte (Fact-Checking, Konsistenz)
    │   └── {date}-{topic}-review.md
    ├── hypotheses/             ← Offene Hypothesen und Forschungsfragen
    │   └── {topic}-hypotheses.md
    └── diffs/                  ← Differenzanalysen (Ziel vs. Realität)
        └── {date}-{topic}-diff.md
```

### Begründung der Unterordner

| Ordner | Zweck | Lebenszyklus |
|--------|-------|-------------|
| `sources/` | Gesammelte externe Referenzen zu einem Thema. Papers, Doku-Links, Blog-Zitate mit Quellengewichtung. | Wächst kontinuierlich, wird ergänzt |
| `reviews/` | Strukturierte Validierungsberichte. Ein Agent prüft Claims gegen Quellen und interne Konsistenz. | Pro Prüfung eine Datei |
| `hypotheses/` | Offene Fragen und neue Ideen die aus der Analyse entstehen. Nicht bewiesen, aber begründet. | Werden bestätigt, widerlegt oder offen gelassen |
| `diffs/` | Explizite Differenzanalyse: Was sagt das Whitepaper? Was sagt der Code? Was sagt die Forschung? Wo klaffen Lücken? | Pro Analyse eine Datei |

---

## 4. Differenzanalyse-Modell (Delta)

Aus den unstrukturierten Gedanken extrahiert und formalisiert:

```
Delta_1 = Whitepaper vs. Workpaper    → Architekturziel vs. operative Umsetzung
Delta_2 = Workpaper vs. Code/Output   → Plan vs. tatsächliches Ergebnis
Delta_3 = System vs. externe Realität → Eigene Lösung vs. Stand der Forschung/Industrie
```

**SCIENCE adressiert primär Delta_3** — die anderen Deltas sind implizit in Workpaper-Reviews abgedeckt.

Delta_3 ist das, was heute komplett fehlt. Ein Agent kann nie sagen: *"Unsere Architekturentscheidung ist State-of-the-Art"* oder *"Es gibt dafür bereits eine bessere Lösung"*.

---

## 5. Science Report — Output-Struktur

Jeder Review-Bericht in `reviews/` folgt diesem Schema:

```markdown
# SCIENCE REPORT: {Topic}

- **Datum:** {YYYY-MM-DD}
- **Scope:** {Was wurde geprüft}
- **Trigger:** {Warum jetzt — manuell, Architekturentscheidung, Whitepaper-Update}

## 1. Summary
Kurzbewertung (1-3 Sätze)

## 2. Key Claims
Extrahierte Aussagen/Annahmen aus dem Projekt

## 3. Validation
| Claim | Status | Confidence | Evidence | Notes |
|-------|--------|-----------|----------|-------|

Status: confirmed | challenged | unverified | refuted
Confidence: 0.0–1.0
Evidence: A (peer-reviewed) | B (offizielle Doku) | C (Blog/Artikel) | D (Meinung/Erfahrung)

## 4. External Context
Ähnliche Projekte, bekannte Patterns, Stand der Forschung

## 5. Differences (Delta_3)
Eigene Lösung vs. externe Realität

## 6. Risks
Falsche Annahmen, fehlende Teile, blinde Flecken

## 7. Hypotheses
Neue Ideen und Optimierungen die aus der Analyse entstanden

## 8. Sources
Alle referenzierten Quellen mit Gewichtung (A/B/C/D)
```

---

## 6. Quellengewichtung

| Level | Typ | Beispiel |
|-------|-----|---------|
| **A** | Peer-reviewed Paper | arXiv, ACM, IEEE |
| **B** | Offizielle Dokumentation | Framework-Docs, RFCs, Standards |
| **C** | Blog / Artikel / Konferenzvortrag | Heise, Medium, YouTube-Talk |
| **D** | Meinung / Erfahrungsbericht | Reddit, Feldberichte, Agent-Output |

Ein Agent muss seine Quellen gewichten. Nicht alles hat denselben epistemischen Wert.

---

## 7. Unsicherheitsmodell

SCIENCE-Aussagen sind nie binär. Jede Validierung hat:

```
Confidence: 0.0 – 1.0    (wie sicher?)
Evidence:   A | B | C | D  (wie gut belegt?)
Consensus:  high | mixed | low | unknown  (wie breit akzeptiert?)
```

Und bei Widersprüchen:

```
⚠ CONFLICT:
- Source A (Level B): sagt X
- Source B (Level C): sagt Y
→ Resolution: [offen | A bevorzugt | eigene Position begründet]
```

---

## 8. Trigger-Modell: Wann wird SCIENCE ausgelöst?

### Empfehlung: Hybrid (manuell + event-basiert)

| Trigger | Auslöser | Beispiel |
|---------|----------|---------|
| **Manuell** | Agent oder User startet Science-Review | "Prüfe ob unsere LTM-Architektur State-of-the-Art ist" |
| **Whitepaper-Update** | Architekturentscheidung getroffen | WP-001 aktualisiert → Delta_3 prüfen |
| **Neues Thema** | Agent betritt unbekanntes Gebiet | Neues Framework evaluiert → Sources sammeln |
| **Periodisch** | Zeitbasiert (z.B. monatlich) | Gesamtvalidierung aller offenen Hypothesen |

SCIENCE ist **kein Automatismus der bei jedem Commit läuft**. Es ist ein bewusster Schritt:

> `Plan → Build → Science → Refine`

---

## 9. Integration in AAMS

### 9.1 Erweiterung des Dokumentationsmodells

Von vier auf fünf Schichten:

| Schicht | Ordner | Frage | Zeitdimension |
|---------|--------|-------|---------------|
| Workpaper | `WORKPAPER/` | Was tue ich jetzt? | Session |
| Whitepaper | `WHITEPAPER/` | Wie ist das System? | Langfristig |
| Diary | `DIARY/` | Warum so entschieden? | Chronologisch |
| Memory | `MEMORY/` | Was haben wir gelernt? | Cross-Session |
| **Science** | **`SCIENCE/`** | **Stimmt das? Gibt es das? Wo stehen wir?** | **Epistemisch** |

### 9.2 Bezug zu WP-004 (Long-Horizon-Reasoning)

SCIENCE adressiert direkt die LHR-Failure-Modes aus WP-004:

| LHR Failure Mode | SCIENCE-Antwort |
|------------------|-----------------|
| Plan-Drift | Periodische Delta_3-Prüfung gegen externe Realität |
| Session-Amnesie | Sources und Reviews sind persistent, querybar |
| Kontext-Dilution | Strukturierte Kurzberichte statt 200k-Token-Kontexte |

### 9.3 Agent Contract — Erweiterung

Neue optionale Trigger im Agent Contract:

```
### On Science triggers (optional)
1. Before architectural decisions → query SCIENCE/sources/ for existing research
2. After Whitepaper update → create diff in SCIENCE/diffs/
3. On new hypothesis → document in SCIENCE/hypotheses/
4. On explicit request → create full Science Report in SCIENCE/reviews/
```

### 9.4 LTM-Integration

Science Reports werden wie Workpapers in LTM ingestiert:

```
Workpaper closed → LTM ingest
Science Report created → LTM ingest (Tag: SCIENCE)
Hypothesis confirmed/refuted → LTM ingest (Tag: HYPOTHESIS)
```

---

## 10. Kritische Punkte & Grenzen

| Risiko | Mitigation |
|--------|-----------|
| **Overhead** — Science kann zu schwer werden | Nur bei wichtigen Themen. Kein Automatismus. Bewusster Schritt. |
| **Quellenqualität** — LLM liest Müll, Ergebnis Müll | Quellengewichtung (A/B/C/D) + Konflikterkennung |
| **Scope Explosion** — Science kann unendlich werden | Klare Begrenzung: `max_sources: 10`, `max_depth: 2` |
| **Halluzinierte Validierung** — Agent "bestätigt" mit erfundenen Quellen | Unsicherheitsmodell + explizite Source-Referenzen (URLs, DOIs) |
| **Fünfte Schicht = Komplexität** | SCIENCE ist opt-in, nicht mandatory. Minimal-AAMS bleibt 4 Schichten. |

---

## 11. Bezug zum Forschungsfeld

Was wir hier bauen, hat Parallelen zu:

1. **AI Scientist Systeme** (AutoGPT Research Modes) — Hypothesen generieren, Papers vergleichen
2. **Knowledge Verification Systems** — Aussagen gegen externe Daten prüfen, "Truth Layer"
3. **Reflection + Critic Agents** — Aber wir machen es **persistent (Dateien)**, nicht ephemer (Prompt)

Der Unterschied zu bestehenden Ansätzen: AAMS macht daraus ein **dateibasiertes, versionierbares, repo-lokales System**. Kein Cloud-Service. Kein proprietäres Tool. Markdown + Ordnerstruktur.

---

## 12. Decisionen

| # | Entscheidung | Begründung |
|---|-------------|-----------|
| D1 | SCIENCE wird als `WORKING/SCIENCE/` angelegt, nicht als separates Top-Level | Konsistenz mit bestehender WORKING/-Struktur |
| D2 | Vier Unterordner: sources, reviews, hypotheses, diffs | Klare funktionale Trennung, minimale Struktur |
| D3 | Science Reports folgen einem festen Schema | Vergleichbarkeit, Querybarkeit, LTM-Ingest |
| D4 | Quellengewichtung A/B/C/D ist verpflichtend in Reviews | Epistemische Qualität — LLMs halluzinieren sonst "Wahrheit" |
| D5 | SCIENCE ist opt-in, nicht mandatory in AAMS-MINI | Overhead-Kontrolle. Vier-Schichten-Modell bleibt Basis. |
| D6 | Unsicherheitsmodell (Confidence/Evidence/Consensus) in jeder Validierung | Keine binären Wahrheiten. Agent lernt Unsicherheit auszudrücken. |
| D7 | Trigger-Modell: Hybrid (manuell + event-basiert) | Balance zwischen Kontrolle und Automatisierung |

---

## 13. Next Steps

- [ ] Ordner `WORKING/SCIENCE/` mit Unterordnern anlegen
- [ ] `WORKING/SCIENCE/INDEX.md` erstellen (leer, mit Schema-Header)
- [ ] Template für Science Report erstellen (`WORKING/SCIENCE/reviews/_TEMPLATE.md`)
- [ ] Template für Hypothesen erstellen (`WORKING/SCIENCE/hypotheses/_TEMPLATE.md`)
- [ ] Template für Sources erstellen (`WORKING/SCIENCE/sources/_TEMPLATE.md`)
- [ ] Template für Diffs erstellen (`WORKING/SCIENCE/diffs/_TEMPLATE.md`)
- [ ] WP-001 aktualisieren: Fünf-Schichten-Modell dokumentieren
- [ ] READ-AGENT.md aktualisieren: SCIENCE-Ordner in Workspace Structure
- [ ] AGENTS.md aktualisieren: SCIENCE in Workspace-Struktur
- [ ] Ersten Science Report schreiben: AAMS-Selbstvalidierung (Delta_3)
- [ ] LTM-Ingest dieses Workpapers

---

## File Protocol

| # | Aktion | Datei | Beschreibung |
|---|--------|-------|-------------|
| F1 | CREATED | `WORKING/WORKPAPER/2026-04-09-science-knowledge-validation-layer.md` | Dieses Workpaper |

---

> **Dieses Workpaper ist die Planungsgrundlage.** Die Umsetzung (Ordner anlegen, Templates, Spec-Updates) erfolgt als separater Schritt nach Review.
