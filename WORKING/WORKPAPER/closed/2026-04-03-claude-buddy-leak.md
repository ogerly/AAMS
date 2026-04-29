# Workpaper — Wissenspaper: Claude Code Source-Leak (April 2026)

- **Datum:** 2026-04-03
- **Typ:** Wissenspaper / Marktbeobachtung / Architekturanalyse
- **Thema:** Anthropic Claude Code — Source-Map-Leak enthüllt vollständiges Memory-System (KAIROS), Konfigurationsarchitektur und "Buddy"-Easter-Egg

---

## Was passiert ist

Anthropic hatte für den **1. April 2026** ein Easter-Egg-Feature namens **"Claude Buddy"** als Aprilscherz geplant. Es wurde jedoch **einen Tag zu früh** versehentlich veröffentlicht:

- **Version 2.1.88** des `@anthropic-ai/claude-code` npm-Pakets wurde mit einem **59,8 MB großen `.map`-File** ausgeliefert
- Dieses Source-Map-File enthüllte über **512.000 Zeilen TypeScript-Quellcode** von Claude Code
- Damit wurde das gesamte Buddy-System öffentlich einsehbar, bevor es offiziell enthüllt werden sollte

---

## Was "Buddy" ist (der Aprilscherz)

Ein verstecktes `/buddy`-System — ein vollständiger **ASCII-Begleiter**, der im Terminal lebt. Im Vergleich zur Memory-Architektur ein Nebenprodukt, aber kulturell interessant.

### Kernmechanik

- Das Haustier wird **deterministisch aus der User-ID generiert** (kein Zufall, jeder User bekommt konsistent dasselbe)
- **Gacha-Seltenheitssystem** — wie in Mobile Games
- Animierte ASCII-Sprites im Terminal
- Hüte (Accessories)
- Stats-System
- Reaktionen auf Coding-Aktivität des Users

### 18 Spezies

Duck, Goose, Blob, Cat, Dragon, Octopus, Owl, Penguin, Turtle, Snail, **Ghost**, Axolotl, Capybara, Cactus, Robot, Rabbit, Mushroom, Chonk

### Seltenheitsstufen

| Stufe | Wahrscheinlichkeit |
|---|---|
| Common | 60% |
| Uncommon | (k.A.) |
| Rare | (k.A.) |
| Epic | (k.A.) |
| Legendary | 1% |

### Stat-System

Jeder Buddy hat 5 Stats:

| Stat | Konzept |
|---|---|
| **DEBUGGING** | Wie gut der Buddy beim Debugging „hilft" |
| **PATIENCE** | Geduld |
| **CHAOS** | Chaos-Faktor |
| **WISDOM** | Weisheit |
| **SNARK** | Sarkasmus-Level |

### Beispiel

"Flintwick" — ein **Ghost**-Buddy (Spezies: Ghost, Seltenheit: unbekannt)

---

## Warum das interessant ist

### 1. Source-Leak als Nebeneffekt

Ein `.map`-File in einem npm-Paket ist ein klassischer Deployment-Fehler. Dass über eine halbe Million Zeilen TypeScript-Source damit öffentlich wurden, zeigt:
- Claude Code ist eine **massive TypeScript-Codebase**
- Die Release-Pipeline hatte keine Prüfung auf Source-Map-Leaks
- Anthropic baut deutlich mehr Features als öffentlich sichtbar (versteckte Systeme, Easter Eggs)

### 2. Gamification in Developer Tools

Anthropic baut bewusst **emotionale Bindung** in ein Terminal-Tool:
- Deterministisch pro User → „das ist MEIN Buddy" (Identifikation)
- Gacha-System → Seltenheit erzeugt Wert und Gesprächsstoff
- Stats mit Humor (CHAOS, SNARK) → Community-Kultur
- Reaktionen auf Coding → das Tool „lebt" und beobachtet

Das ist kein Zufall — das ist **Retention-Engineering**. Je mehr emotionale Bindung an Claude Code, desto weniger Wechselbereitschaft zu Cursor, Copilot etc.

### 3. Relevanz für AAMS

Dieses Feature illustriert exakt unser Argument aus dem Wording-Faktencheck (→ Workpaper 2026-04-02):

> Jeder Agent baut sein eigenes Ökosystem, um Nutzer zu binden — mit proprietären Features, die nicht portabel sind.

Ein Buddy, der an die User-ID gebunden ist und nur in Claude Code lebt, ist das Gegenteil von Portabilität. Das Projektwissen (und jetzt auch die emotionale Bindung) leben beim Anbieter, nicht beim Projekt.

**AAMS-Gegenposition:** Das Wissen über ein Projekt gehört ins Repository. Emotionale Features sind legitim — aber sie dürfen nicht das Lock-in-Instrument sein.

---

## Quellen

- npm-Paket `@anthropic-ai/claude-code` Version 2.1.88
- Community-Analyse des Source-Map-Leaks (GitHub, diverse Threads)
- Claude Code Changelog / Anthropic-Kommunikation

---

## File Protocol

| Aktion | Datei |
|--------|-------|
| CREATED | `WORKING/WORKPAPER/2026-04-03-claude-buddy-leak.md` |

---

## Tags

`#marktbeobachtung` `#anthropic` `#claude-code` `#gamification` `#source-leak` `#retention` `#portabilität`



Die MD-Dateien im Detail — was der Leak enthüllte:
CLAUDE.md (project root) ist die wichtigste Konfig-Datei. Sie wird in jeden einzelnen Prompt-Turn injiziert und gibt dir bis zu 40.000 Zeichen, um das Verhalten von Claude Code für dein Projekt zu steuern — Coding-Standards, Architektur, verbotene Patterns, bevorzugte Libraries, Build-Befehle. Die meisten Entwickler nutzen sie kaum; der Leak zeigt, dass sie eigentlich das Herzstück der Produktivität ist.
CLAUDE.md (personal, ~/.claude/) gilt user-global. Sie überschreibt nichts im Projekt, sondern ergänzt persönliche Vorlieben (Tonalität, Stil, generelle Arbeitsweise), die über alle Projekte hinweg gelten sollen.
CLAUDE.md (org/enterprise) ist eine von der Organisation verwaltete Variante. Diese Dateien können nicht ausgeschlossen werden — sie stellen sicher, dass unternehmensweite Anweisungen immer gelten, unabhängig von individuellen Einstellungen.
.claude/rules/*.md sind modulare Regelfiles für Teams. Jede Datei sollte ein Thema abdecken, mit einem beschreibenden Dateinamen wie testing.md oder api-design.md. Alle .md-Dateien werden rekursiv gefunden, können also in Unterverzeichnisse wie frontend/ oder backend/ organisiert werden. Regeln können auch auf bestimmte Dateipfade beschränkt werden und laden nur dann in den Kontext, wenn Claude mit passenden Dateien arbeitet.
MEMORY.md ist das Herzstück des Speichersystems und das architektonisch interessanteste Element. Es ist der Einstiegspunkt — ein Index, bei dem jede Zeile unter 150 Zeichen bleibt, mit Pointern statt Inhalten. Die ersten 200 Zeilen von MEMORY.md werden beim Sessionstart in den Kontext injiziert. Das eigentliche Wissen liegt verteilt in Topic-Files und wird bei Bedarf geladen. Entscheidend: Der Agent ist angewiesen, seine eigene Erinnerung nur als "Hinweis" zu behandeln — Fakten müssen immer gegen die tatsächliche Codebasis verifiziert werden, bevor gehandelt wird.
Topic Files (user_role.md, project_auth_rewrite.md usw.) sind die zweite Speicherschicht. Diese Dateien leben in ~/.claude/projects/<project-path>/memory/. Jede ist eine eigenständige Markdown-Datei mit Frontmatter, das Typ und Beschreibung angibt. Sie werden nie alle gleichzeitig geladen — nur bei Bedarf.
Daily Logs (daily-YYYY-MM-DD.md) sind append-only Tagesdateien. KAIROS führt append-only Tagesprotokolle aller Beobachtungen, Entscheidungen und Aktionen. Es kann seine eigene Geschichte nicht löschen. Diese werden zur Rohquelle für autoDream.
Session Transcripts sind die dritte Speicherschicht. Rohe Transkripte werden nie vollständig in den Kontext geladen — sie werden nur per grep nach spezifischen Identifikatoren durchsucht.

Das autoDream-Zusammenspiel (4 Phasen):
Phase 1 "Orient": ls auf das Memory-Verzeichnis, MEMORY.md lesen, vorhandene Topic-Files überfliegen. Phase 2 "Gather": neue relevante Informationen finden — Priorität: Daily Logs → driftende Erinnerungen → Transkript-Suche. Phase 3 "Consolidate": Topic-Files schreiben oder aktualisieren. Phase 4: MEMORY.md-Index synchronisieren. Der autoDream-Prozess legt Beobachtungen zusammen, entfernt Widersprüche und befördert vage Erkenntnisse zu verifizierten Fakten — er läuft als geforkter Subagent, damit er den Haupt-Kontext des Agenten nicht korrumpieren kann.
