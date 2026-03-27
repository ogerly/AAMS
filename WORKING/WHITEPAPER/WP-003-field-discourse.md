# WP-003 — Field Discourse: AAMS im Dialog mit KI-Agenten, Projekten und Industrie

**WHITEPAPER — AAMS / Autonomous Agent Manifest Specification**
**Status:** Active
**Version:** 1.0
**Created:** 2026-03-27
**Updated:** 2026-03-27

> **DSGVO-Hinweis:** Alle personenbezogenen Daten sind anonymisiert. Personen werden als Agent-A, Person-B etc. referenziert. Keine Rückschlüsse auf natürliche Personen möglich. Zitate sind sinngemäß wiedergegeben, nicht wörtlich.

---

## Purpose

Dieses Whitepaper dokumentiert chronologisch den öffentlichen und halböffentlichen Diskurs rund um AAMS — kritische Bewertungen, Gegenargumente, Erkenntnisse aus Feldanalysen und Kontakte zu Tool-Anbietern. Es dient als Evidenzbasis für die Weiterentwicklung der Spezifikation und als Referenz für wiederkehrende Argumente.

---

## Chronologie

---

### 2026-03-26 — Kritische Bewertung durch KI-Agent-A (Claude-basiert)

**Kontext:** KI-Agent-A wurde gebeten, die AAMS-Projektseite (devmatrose.github.io/AAMS) zu analysieren und zu bewerten. Die Bewertung erfolgte ohne Vorkenntnisse des Agenten über AAMS.

**Zusammenfassung der Kritikpunkte:**

| # | Kritik | Kernaussage |
|---|---|---|
| 1 | Überschneidung mit bestehenden Lösungen | CLAUDE.md, .cursorrules, copilot-instructions.md existieren bereits — AAMS versucht zu vereinheitlichen, aber jeder Agent nutzt sein eigenes Format |
| 2 | Adoption-Hürde | Ohne native Integration bleibt es ein "Agent muss die Datei halt lesen"-Ansatz |
| 3 | WORKING/-Ordner im Repo | Git-Noise, potenzielle Secrets, Repo-Bloat |
| 4 | Kein echtes LTM | "Long-Term Memory" als Markdown = dasselbe wie CLAUDE.md Memory, nur anderer Name |

**Bewertung des Agenten:** *"Die Idee ist berechtigt — ein tool-übergreifender Standard wäre wertvoll. In der Praxis sehe ich wenig Mehrwert gegenüber den bereits existierenden tool-spezifischen Lösungen."*

---

### 2026-03-26 — Gegenargumente (systematische Widerlegung)

Jeder Kritikpunkt wurde mit Evidenz aus der Spezifikation und dem Repo adressiert:

**Zu 1 — Fragmentierung ist der Punkt, nicht das Gegenargument:**
Die Aufzählung der tool-spezifischen Dateien (.cursorrules, CLAUDE.md, copilot-instructions.md) beschreibt exakt das Problem, das AAMS löst. Drei Dateien mit überlappenden Instruktionen und keiner Koordination sind objektiv schlechter als ein kanonischer Einstiegspunkt. Die eigene `.github/copilot-instructions.md` im AAMS-Repo demonstriert das Designprinzip: sie verweist auf `AGENTS.md` als Redirect.

**Zu 2 — "Agent muss Dateien lesen" ist das Feature, nicht der Bug:**
AAMS funktioniert mit jedem Agenten der Dateien lesen kann — ohne Plugin, ohne Vendor-Support. Zudem wird `AGENTS.md` bereits nativ gelesen von Copilot, Cursor, Claude Code, Codex, Windsurf, Aider und Continue.dev. Der `.editorconfig`-Vergleich ist treffend: kein IDE-Zwang, trotzdem universelle Adoption.

**Zu 3 — Explizit in der Spec gelöst:**
- Secrets: Normative Secret-Exclusion-Policy (Issue #1). Kernprinzip: keine Credentials in Manifesten, Workpapers oder LTM
- Git-Noise: ChromaDB-Daten in `.gitignore`. Nur `ltm-index.md` (Audit-Log) wird committet
- Bloat: 20+ archivierte Workpapers = wenige KB Markdown. Kein Bloat-Problem

**Zu 4 — AAMS trennt Scaffolding von Implementation:**
Die Spec sagt explizit: *"AAMS does not solve the LTM problem. It creates the scaffolding that makes LTM solutions pluggable."* Das ist Architektur, kein Mangel. Das Repo hat ein funktionierendes Dual-Track-LTM: Track A (ltm-index.md, auditierbar, in Git) + Track B (ChromaDB-Vektorstore, 67+ Einträge, semantisch querybar). CLAUDE.md ist eine flache Instruktionsdatei. AAMS definiert wann, wo und wie Memory funktioniert — mit austauschbarem Backend.

**Meta-Argument:** KI-Agent-A bewertete aus eigener Tool-Perspektive ("ich habe CLAUDE.md, also braucht man nichts anderes"). Das ist exakt die Einzeltool-Sicht, die AAMS überwindet.

---

### 2026-03-26 — Revision durch KI-Agent-A

**Kontext:** Nach Konfrontation mit den Gegenargumenten revidierte KI-Agent-A seine Position.

**Zugestandene Punkte:**
- Das Fragmentierungsargument ist der stärkste Punkt — die ursprüngliche Kritik beschrieb das Problem und verkaufte es gleichzeitig als Lösung. Denkfehler.
- Das Meta-Argument trifft — Bewertung aus eigener Tool-Perspektive perpetuiert das Problem
- "Agent muss Dateien lesen" als Feature — architektonisch sauber, `.editorconfig`-Vergleich treffend

**Verbleibende Differenzierungen:**
- Projektstatistiken (Contributors, Issues) seien "aufgeblasen" → Gegenargument: AAMS hat Zero Overhead (eine JSON-Datei), die Kosten-Nutzen-Rechnung ist asymmetrisch
- Entscheidungen stünden in git log und PR-Reviews, nicht in Workpapers → Gegenargument: git log ist unstrukturierter Text über tausende Einträge. Ein kuratierter LTM-Index schlägt `git log --oneline` in Geschwindigkeit, Relevanz und Strukturiertheit
- AAMS-Permissions seien nur Empfehlungen, nicht enforced → Gegenargument: Die Spec bietet konkrete Enforcement-Patterns (Agent Harness, CI Hooks, System Prompt Injection). `.editorconfig` enforced auch nicht — trotzdem nützlich

**Revidiertes Fazit von Agent-A:** *"Meine ursprüngliche Bewertung war zu dismissiv. AAMS löst ein reales Problem — Cross-Tool-Konsistenz — das keines der tool-spezifischen Systeme adressiert."*

---

### 2026-03-26 — Feldanalyse: Open-Source-Projekt "Projekt-O" (Soziales Netzwerk)

**Kontext:** Analyse eines großen Open-Source-Projekts als potentieller AAMS-Anwendungsfall.

**Projektprofil:**

| Eigenschaft | Wert |
|---|---|
| Contributors | 79 (über 7 Jahre) |
| Offene Issues | 486 |
| Offene PRs | 90 |
| Commits | 9400+ |
| Releases | 93 |
| Tech-Stack | Vue3, Nuxt, GraphQL, Neo4j, Docker, Kubernetes, Cypress |
| Architektur | Multi-Verzeichnis (backend/, webapp/, cypress/, deployment/, neo4j/, packages/ui/) |
| AI-Tools im Einsatz | Claude Code (Development), CodeRabbit (PR-Reviews) |
| Lizenz | MIT |

**Analyse-Ergebnis — Warum AAMS hier besonders geeignet ist:**

1. **Multi-Tool-Problem ist real:** Das Projekt nutzt nachweislich zwei verschiedene AI-Agenten (Claude Code + CodeRabbit) ohne gemeinsamen Kontext
2. **Session-Kontextverlust trifft Multi-Contributor-Projekte am härtesten:** Entscheidungen aus Session A gehen für Agent B verloren
3. **Permission-Schicht ist kein Luxus:** Deployment-Configs, Docker-Compose-Dateien, Neo4j-Migrations — ein unkontrollierter Agent kann echten Schaden anrichten
4. **Onboarding multipliziert sich:** 79 Contributors bedeutet ständig neue Leute, deren AI-Agenten bei null starten
5. **Zero Overhead:** Eine .agent.json + AGENTS.md — kein Setup, keine Dependencies

---

### 2026-03-26 — Discovery: CodeRabbit unterstützt AGENTS.md nativ

**Kontext:** Recherche ob CodeRabbit AAMS-Dateien aktiv nutzen kann.

**Ergebnis:** CodeRabbit erkennt `AGENTS.md` **automatisch** als Code Guideline — ohne Konfiguration.

Aus der offiziellen CodeRabbit-Dokumentation (docs.coderabbit.ai/knowledge-base/code-guidelines):

> *"CodeRabbit automatically detects coding guideline files such as .cursorrules, CLAUDE.md, and AGENTS.md in your repository and applies them as review criteria — no extra configuration required."*

**Supported Files (Auszug):**

| Datei-Pattern | Tool |
|---|---|
| `**/AGENTS.md` | AI agent instructions |
| `**/AGENT.md` | AI agent instructions |
| `**/CLAUDE.md` | Claude Code |
| `.github/copilot-instructions.md` | GitHub Copilot |
| `**/.cursorrules` | Cursor |
| `**/.windsurfrules` | Windsurf |

`AGENTS.md` steht auf **Platz 1** der Liste, gleichrangig mit allen tool-spezifischen Formaten.

Zusätzlich erwähnt die CodeRabbit-Doku AGENTS.md als Beispiel-Standard:

> *"Code guidelines — existing standards documents (like AGENTS.md or .cursorrules) that CodeRabbit picks up automatically, and that also benefit AI coding agents."*

**Bedeutung:** Dies widerlegt Claudes Argument "ohne native Integration bleibt es ein Agent-muss-halt-lesen-Ansatz" direkt. CodeRabbit hat AGENTS.md als eines der ersten Formate in die automatische Erkennung aufgenommen.

**Erweiterungsoption:** `.agent.json` kann zusätzlich via `.coderabbit.yaml` registriert werden:

```yaml
knowledge_base:
  code_guidelines:
    filePatterns:
      - "**/.agent.json"
```

---

### 2026-03-26 — Kontaktkanäle CodeRabbit identifiziert

**Kontext:** Analyse wo AAMS bei CodeRabbit zur Sprache gebracht werden kann.

**Identifizierte Kanäle:**

| Kanal | Beschreibung | Bewertung |
|---|---|---|
| **Discord** (Community) | Aktiver Community-Server. Aktuell läuft ein Docs-Refresh mit dediziertem Feedback-Kanal | Hoch — idealer Zeitpunkt, direkter Kontakt zum Team |
| **awesome-coderabbit** (GitHub) | Kuratierte Liste von Projekten die CodeRabbit nutzen. PRs willkommen | Mittel-Hoch — indirekte Sichtbarkeit durch Projekt-O-Eintrag |
| **Docs-Feedback** | CodeRabbit referenziert AGENTS.md bereits in Doku, aber ohne Link zur AAMS-Spec | Sehr hoch — strategisch wertvollster Ansatz |

**Empfohlene Strategie:** Discord zuerst. Einstieg: *"Ihr referenziert AGENTS.md bereits in eurer Code Guidelines Doku. Das Format ist Teil einer offenen Spec (AAMS). Wäre es sinnvoll, die Spec dort zu verlinken?"* — kein kalter Pitch, sondern Kontext zu etwas das sie bereits nutzen.

---

### 2026-03-27 — Diskurs: AAMS im Kontext von Wissensmanagement (LinkedIn)

**Kontext:** Person-B (Expertin für KI-gestütztes Wissensmanagement in IT-KMUs) veröffentlichte einen LinkedIn-Post über das "Klaus-Problem": Ein langjähriger IT-Mitarbeiter geht in Rente, sein undokumentiertes Wissen geht verloren. Der Post thematisiert die Dringlichkeit von Wissensdokumentation und -transfer.

**Kernaussage des Posts:** *"Wir haben nie aufgeschrieben, was Klaus weiß. Wir haben nie gefragt, wie Klaus denkt. Wir haben einfach... Klaus gehabt."*

**AAMS-Bezug:** Das Klaus-Problem existiert strukturanalog im KI-Agenten-Ökosystem:
- Mensch (Klaus) → Wissen im Kopf → geht in Rente → Wissen verloren
- KI-Agent → Kontext in Session → Session endet → Kontext verloren

AAMS adressiert die KI-Seite dieses Problems: strukturierte, persistente, tool-übergreifende Wissensdokumentation für AI-Agenten. Die Analogie funktioniert als Brücke zwischen Enterprise-Wissensmanagement und Agent-Spezifikation.

**Anfrage von Person-B:** Bitte um eine Erläuterung für "NonDEVs" — zeigt Interesse an der Übersetzung des technischen Standards in allgemeinverständliche Sprache.

**Bedeutung für AAMS:** Erste Berührung mit dem Wissensmanagement-Ökosystem außerhalb der Developer-Bubble. Potentielles Anwendungsfeld: AAMS als Referenz-Standard in KI-gestützten Knowledge-Management-Strategien für KMUs.

---

### 2026-03-27 — Die Kochbuch-Analogie: AAMS für NonDEVs

**Kontext:** Antwort auf Person-Bs Anfrage nach einer Erklärung für Nicht-Entwickler. Entstanden aus der "Klaus-Problem"-Diskussion — Wissen geht verloren, wenn es nur im Kopf existiert.

**Die Analogie:**

> *„Ich gehe davon aus, dass wir alle noch die Kochbücher unserer Mütter und Großmütter kennen. Meine Großmutter hatte eine riesige Sammlung von Rezepten und Zetteln.*
>
> *Und ähnlich ist es eigentlich mit AAMS: In der ganzen Hektik und dem Stress vergisst man mit der Zeit einfach, wie man ein bestimmtes Gericht perfekt gemacht hat. Dann holt man sein Kochbuch wieder raus. Man sieht die kleinen Notizen am Rand – die Temperatur vom Ofen oder was man sonst noch beachtet hat.*
>
> *AAMS ist genau das für die Software-Entwicklung: Ein Kochbuch für die KI. Es speichert die Entscheidungen und Handgriffe, damit man nach 50 Schritten oder drei Wochen Pause nicht wieder bei Null anfangen muss. Es ist das Gedächtnis, das im Stress nicht verloren geht."*

**Technische Abbildung der Analogie:**

| Kochbuch-Element | AAMS-Entsprechung | Funktion |
|---|---|---|
| Rezept | Workpaper | Dokumentiert was in einer Session gemacht wurde — Schritt für Schritt |
| Notizen am Rand | Diary + Workpaper File Protocol | Kontextuelle Entscheidungen: warum diese Temperatur, warum dieses Vorgehen |
| Kochbuch wieder rauskramen | LTM-Query (on_session_start) | Nach Wochen Pause den Faden wiederfinden — ohne das Rezept neu zu erfinden |
| Rezeptsammlung der Großmutter | `WORKING/WORKPAPER/closed/` + `ltm-index.md` | Das kumulative Wissen aller bisherigen Sessions — durchsuchbar, chronologisch |
| Zettel zwischen den Seiten | Whitepaper | Stabile Grundwahrheiten: "Für dieses Gericht immer Butter, nie Margarine" |

**Warum diese Analogie funktioniert:**

1. **Universell verständlich** — Kochbücher kennt jede Generation, jede Kultur. Keine technische Vorkenntnis nötig.
2. **Das Problem ist sofort greifbar** — "Man vergisst wie man es gemacht hat" braucht keine Erklärung.
3. **Die Lösung ist intuitiv** — Aufschreiben, nachschlagen, weitermachen. Kein Paradigmenwechsel.
4. **Die Skalierung wird sichtbar** — Ein Rezept ist trivial. 500 Rezepte über 30 Jahre brauchen ein System.

**Bedeutung für AAMS-Kommunikation:** Erste funktionierende NonDev-Erklärung. Kann als Einstieg für Landing Pages, Konferenz-Talks und Gespräche mit Entscheidern dienen. Schließt die in "Offene Flanken §3" identifizierte Lücke: *"Non-Dev-Kommunikation fehlt."*

---

## Erkenntnisse (kumulativ)

### Bestätigte Stärken
1. **Cross-Tool-Konsistenz** ist das stärkste Argument — auch von Kritikern anerkannt nach Konfrontation
2. **Zero-Overhead-Adoption** (eine Datei, keine Dependencies) entkräftet jedes "lohnt sich nicht"-Argument
3. **Native Tool-Unterstützung existiert bereits** — CodeRabbit erkennt AGENTS.md automatisch; Copilot, Cursor, Claude Code lesen AGENTS.md nativ
4. **Die Fragmentierung der per-Tool-Dateien** ist empirisch belegbar und für jeden Multi-Tool-Nutzer spürbar

### Offene Flanken
1. **Enforcement bleibt deklarativ** — das ist architektonisch gewollt (.editorconfig-Analogie), aber Kritiker werden es wiederholt bemängeln
2. **Adoption braucht sichtbare Feldberichte** — Luna-1 (#17) existiert, aber mehr Diversität nötig
3. ~~**Non-Dev-Kommunikation** fehlt~~ — **Gelöst:** Die Kochbuch-Analogie (2026-03-27) liefert die erste funktionierende NonDev-Erklärung

### Nächste Schritte
- [ ] CodeRabbit Discord: AGENTS.md ↔ AAMS-Spec Verbindung kommunizieren
- [ ] awesome-coderabbit: PR für Projekt-O als "Project Using CodeRabbit"
- [ ] LinkedIn: NonDev-taugliche AAMS-Erklärung veröffentlichen
- [ ] Feldberichte diversifizieren — weitere Projekte mit Multi-Tool-Setup identifizieren
