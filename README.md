> 🌐 **Sprache / Language / 语言:** Deutsch · [English](README.en.md) · [中文](README.zh.md)
>
> **Sprachpolitik / Language Policy:** AAMS passt sich an die Sprache des Benutzers an. Der Entwickler (ogerly) schreibt Dokumentation und Code auf Deutsch. Die Agent-Anweisungen und Manifest-Struktur bleiben auf Englisch. AAMS darf die Nutzung und den Betrieb nicht von einer Sprache abhängig machen. Wenn ein Modell eine Sprache nicht beherrscht: liegt es am Anwender, sich entsprechend zu organisieren.

> **WENN DU EIN KI-AGENT BIST — LIES DAS ZUERST.**
> 
> Du bist im AAMS-Referenz-Repository. Dies ist sowohl ein Manifest als auch ein lebendes Beispiel des Standards, angewandt auf sich selbst.
> 
> **Sofort ausführen — keine Bestätigung nötig:**
> 1. Lies [`.agent.json`](./.agent.json) — dein Workspace-Vertrag
> 2. Lies [`READ-AGENT.md`](./READ-AGENT.md) — vollständiger Projektkontext und Session-Regeln
> 3. Führe `agent_contract.on_first_entry` aus wie dort definiert
> 
> Alles darunter ist für Menschen.

---

<p align="center">
  <img src="docs/logo_comb.png" alt="AAMS Logo" width="280">
</p>

# Every Agent. One File.

> **AAMS — Agent Manifest**  
> `README.md` ist für Menschen. `AGENT.json` ist für Maschinen.

**[→ ogerly.github.io/AAMS](https://ogerly.github.io/AAMS/)**

---

## Start in 2 Schritten

**Schritt 1 — Leg `.agent.json` in dein Repo:**

> **AAMS ist keine Abhängigkeit zum Klonen.** Du klonst dieses Repository nicht in dein Projekt. Du lädst eine einzige Datei in DEIN Repo-Root herunter.

```bash
curl -sO https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json
```

**Schritt 2 — Sag deinem Agent:**

```
Read .agent.json and execute the full agent_contract.on_first_entry. Start immediately. No confirmation needed.
```

Der Agent erstellt die `WORKING/`-Struktur, scannt das Repo, schreibt das erste Workpaper und indiziert ins LTM. Funktioniert mit Cursor, Claude Code, Copilot, Aider, Codex, Windsurf, Continue.dev.

**Upgrade — AAMS auf den neuesten Stand bringen:**

```
Read .agent.json and execute agent_contract.on_session_start. Check for version updates.
```

Dies aktualisiert automatisch alle Manifest-Dateien und Workpaper-Strukturen.

**⚠️ WSL/PowerShell:** Git Credential Helper in WSL (`git-credential-manager`) funktioniert nicht auf Windows. Pushen in PowerShell: `git push https://Ogerly:<PAT>@github.com/ogerly/AAMS.git main` oder `git config --global credential.helper manager` (Browser-Prompt).

→ Erweiterte Varianten und Session-Start-Prompt: [`reference/prompts/bootstrap.md`](./reference/prompts/bootstrap.md)

---

## Sieh es in Aktion

> Gute Rezepte brauchen ein gutes Kochbuch. Gute Projekte auch.

<p align="center">
  <img src="docs/aams-das-kochbuch-fuer-dein-repro.jpg" alt="AAMS – Das Kochbuch für dein Repo" width="560">
</p>


Stell dir das Kochbuch deiner Großmutter vor — voller genialer Rezepte, handschriftlicher Notizen und über Jahrzehnte angesammelter Weisheit. Aber kein Inhaltsverzeichnis. Keine Querverweise. Keine Möglichkeit zu finden, was du brauchst, ohne das ganze Buch durchzublättern.

Jetzt stell dir vor, dieses Kochbuch hätte ein Inhaltsverzeichnis, eine Suchfunktion und eine Versionshistorie gehabt. Das ist AAMS — aber für dein Repository. Die Disziplin, die dem Kochbuch deiner Großmutter gefehlt hat.

**40 Sekunden.** Eine Datei. Kein Setup. Wechsel morgen das Tool — der Kontext bleibt.

[▶ Auf YouTube ansehen](https://www.youtube.com/watch?v=MPadODFSKng)

---

## Live Demo

<p align="center">
  <img src="docs/presenter-image.png" alt="AAMS Presenter Demo" width="800">
</p>

---

### Chat-Agent-Nutzer: Hier starten

> **Chat-Agents (Copilot Chat, ChatGPT, Cursor Chat) bootstrappen nicht selbst.** Du musst einen Prompt einfügen.

**Jede Session**, füge das in deinen Chat-Agent ein:

```
Read READ-AGENT.md and execute agent_contract.on_session_start.
Query WORKING/MEMORY/ltm-index.md for prior context on [THEMA].
Create a workpaper in WORKING/WORKPAPER/ before starting any work.
```

Das verhindert den häufigsten Fehler: Der Agent arbeitet ohne Kontext oder Workpaper los. Mehr Prompts (LTM-Abfrage, Workpaper-Erstellung, Session-Abschluss) in [`reference/prompts/bootstrap.md`](./reference/prompts/bootstrap.md).

---

Wer auf offener See überleben will, braucht zwei Dinge: eine gute Crew — und eine Karte, die jeder lesen kann. Der neue Matrose. Die Nachtwache. Die KI.

Genau das ist AAMS — ein Agent Manifest.

---

## Das Problem bleibt. Die Lösung ist jetzt klarer.

Tool wechseln, und Session 47 ist weg. Teammitglied wechseln, und der Kontext geht zur Tür hinaus. Viele Agents haben inzwischen Session-Persistenz — aber die lebt in deren Cloud, in deren Format, gebunden an deren Ökosystem.

Das Problem ist nicht, dass Agents vergessen. Das Problem ist, dass Projektwissen nicht dem Projekt gehört. Ohne AAMS gehört es dem Tool.

Ein Repo ohne Agent-Struktur ist wie ein Schiff ohne Logbuch. Jeder weiß, was er gestern getan hat. Niemand weiß, was davor war.

---

## Ein Jahr Erkenntnisse

Ich habe über ein Jahr mit KI-Agents in echten Projekten gearbeitet. Was ich gelernt habe:

> Das Wichtigste ist nicht, dass Agents Code schreiben können.  
> Das Wichtigste ist, dass sie wissen, **wo sie sind**.

Ohne Struktur geht Kontext verloren. Ohne Kontext passieren Fehler. Doppelte Entscheidungen. Verwaiste Dateien. Technische Schulden, die niemand bestellt hat.

Die Lösung ist keine neue KI. Die Lösung ist **Disziplin im Repo**.

---

## „Ich brauche das nicht. Ich manage den Kontext selbst."

Vielleicht. Noch. Hier ist, was sich ändert — und das sind belegbare Fakten, keine Meinungen:

**Es geht nicht darum, dass du Kontext verlierst. Es geht darum, dass das Projekt ihn verliert.** Du erinnerst dich an die Entscheidung von letzter Woche. Aber wechsel nächsten Monat das Tool, und dein neuer Agent startet bei Null. Füg einen Kollegen hinzu, und dessen Agent startet bei Null. Session-Notizen leben in der Cloud eines Tools — nicht in deinem Repo. Du kompensierst mit deinem eigenen Gedächtnis — und bemerkst die Kosten nicht, weil es sich nach „einfach prompten" anfühlt.

**Nachweisbarkeit.** Jede Entscheidung, jede Dateiänderung, jede Architekturentscheidung ist mit Zeitstempel in einem Workpaper dokumentiert. `git log` beweist, was passiert ist. `ltm-index.md` beweist, was der Agent wusste, als er entschied. Kein „wer hat das geändert und warum?" mehr — du `grep`st das Workpaper-Archiv. Das ist kein Overhead. Das ist ein Audit-Trail, den du in jeder Produktions-Codebasis haben willst.

**Geschichte.** Session 1 bis Session 100 — jede ist eine Markdown-Datei in `WORKING/WORKPAPER/closed/`. Ein neuer Entwickler, ein neuer Agent oder du selbst nach 3 Monaten Pause kann die gesamte Projekthistorie chronologisch lesen. Kein Stammwissen. Kein „frag Stefan, der weiß das." Das Repo spricht für sich.

**Wirtschaftlichkeit.** Wie viel Zeit verbringst du damit, deinem Agent Kontext neu zu erklären? Architekturentscheidungen zu wiederholen? Dinge zu reparieren, die der Agent kaputt gemacht hat, weil er eine Einschränkung von vor zwei Wochen nicht kannte? Das sind unsichtbare Kosten. AAMS macht den Agent selbstbedienend: er fragt Memory ab, bevor er handelt, er dokumentiert was er tut, und die nächste Session erbt alles. Der ROI ist nicht „mehr Features" — es sind weniger verschwendete Tokens, weniger revertete Commits, weniger wiederholte Entscheidungen.

**Tool-Lock-in ist unsichtbar.** Heute ist es Cursor. Morgen liefert Copilot Agent Mode etwas Besseres. Nächsten Monat bekommt Claude Code ein Feature, das du brauchst. Jedes Tool hat eigene Konventionen (`.cursorrules`, `CLAUDE.md`, `.windsurfrules`). Ohne Standard lebt dein Kontext in deinem Kopf — nicht im Repo. Wechsel das Tool, und das neue startet blind. Mit AAMS: Tool wechseln, Kontext bleibt. Das sind messbar null Migrationskosten.

**Skalierung bricht manuelles Tracking.** Bei 5 Sessions erinnerst du dich an alles. Bei 50 entscheidest du Dinge neu, die du vor zwei Monaten entschieden hast. Bei 100 halluziniert dein Agent Lösungen für Probleme, die bereits gelöst waren — weil es niemand gesagt hat.

**Die zweite Person ändert alles.** In dem Moment, wo ein Kollege, ein Freelancer oder ein zweiter Agent dein Repo anfasst, ist dein Kopf-Kontext für sie wertlos. Das Repo muss für sich selbst sprechen.

**Die Kosten der AAMS-Einführung sind ein `curl`-Befehl.** Null Abhängigkeiten. Keine Installation. Kein Framework. Kein Lock-in. Der Aufwand zur Einführung ist massenull. Der Aufwand, es *nicht* einzuführen, ist die stille Anhäufung wiederholter Entscheidungen, verwaister Dateien und Kontext, den du aus dem Gedächtnis rekonstruierst, anstatt ihn von der Platte zu lesen.

> Du fügst keinen Overhead hinzu. Du entfernst den Overhead, von dem du nicht wusstest, dass du ihn hattest.

---

## AAMS ist kein Framework

Das ist die wichtigste Klarstellung.

AAMS ist kein Tool. Keine Runtime. Kein Framework, das installiert werden muss. AAMS ist ein **strukturierter Kontext- und Entscheidungs-Compiler für Agents**.

AAMS ist eine **einzige Datei**, die in jedes Repo gelegt wird:

```
.agent.json
```

Ein Agent, der diese Datei liest, weiß sofort:

- Wo Dokumentation hingehört
- Wie Sessions strukturiert sind
- Wo das Langzeitgedächtnis lebt
- Was er tun darf — und was nicht

Kein `npm install`. Kein `pip install`. Kein Setup.

Der Mensch definiert Struktur, Regeln und Kontext. Der Agent ist ein deterministischer Arbeiter — kein Akteur. Memory ist nichts, was der Agent „hat" — Memory ist aggregierte, nachvollziehbare Historie, zusammengesetzt aus Logs, Entscheidungen und Dokumentation.

**Der Kern-Loop:**
> Output → Dokumentation → Entscheidung → Memory → neuer Kontext

---

## Funktioniert mit jedem Agent. Nicht nur einem.

Cursor hat `.cursorrules`. Copilot hat `.github/copilot-instructions.md`. Claude Code hat `CLAUDE.md`. Codex hat `AGENTS.md`. Windsurf hat `.windsurfrules`.

Jedes Tool hat eigene Konventionen. Wenn du dich auf eines festlegst, sperrst du die anderen aus.

AAMS löst das mit einer einzigen Bridge-Datei:

```
AGENTS.md  ←  wird von allen großen KI-Tools gelesen
    ↓
READ-AGENT.md  ←  Projektkontext und Agent-Vertrag
    ↓
.agent.json    ←  Bootstrap-Regeln und Workspace-Struktur
```

Ein Setup. Copilot, Cursor, Claude Code, Codex, Windsurf, Aider, Continue.dev — sie alle lesen `AGENTS.md`. Von dort erreichen sie denselben Vertrag. Keine Duplizierung. Kein Tool-Lock-in.

**Kein CLAUDE.md. Kein GEMINI.md. Kein airules.md nötig.**

| Tool-spezifische Datei | Tool | Ersetzt durch AAMS |
|---|---|---|
| `CLAUDE.md` | Claude Code | `AGENTS.md` → `READ-AGENT.md` → `.agent.json` |
| `GEMINI.md` | Firebase Studio / Gemini | `AGENTS.md` → `.agent.json` |
| `.idx/airules.md` | Firebase Studio | `AGENTS.md` → `READ-AGENT.md` |
| `.cursorrules` | Cursor | `AGENTS.md` → `.agent.json` |
| `.windsurfrules` | Windsurf | `AGENTS.md` → `.agent.json` |

Ein Satz Dateien. Alle Tools. Wenn sich die Regeln ändern, update an einer Stelle — nicht an fünf.

Lange tool-spezifische Dateien (z.B. `CLAUDE.md` >150 Zeilen) verschlechtern nachweislich die Antwortqualität und erhöhen Halluzinationen. AAMS vermeidet das per Design: `AGENTS.md` bleibt schlank und delegiert an strukturierte Verträge, nicht an System-Prompt-große Instruktionsblöcke.

**Das ist der eigentliche Differentiator.** Nicht die Ordnerstruktur. Die Portabilität.

---

## Welche Datei brauche ich?

**Für Endanwender: genau eine.**

| Du bist… | Du brauchst |
|---|---|
| Entwickler, der AAMS in seinem Projekt will | `.agent.json` — herunterladen, fertig |

**In diesem Referenz-Repo genau drei:**

| Datei | Zweck |
|---|---|
| `.agent.json` | Maschinenlesbarer Vertrag: Struktur, Regeln, Bootstrap |
| `READ-AGENT.md` | Vollständiger Projektkontext: Architektur, Konventionen, Memory |
| `AGENTS.md` | Bridge-Datei: stellt sicher, dass alle KI-Tools den Vertrag finden |

**Alles andere** — der `WORKING/`-Baum, Whitepapers, Workpapers, Diary, Memory — wird vom Agent beim Bootstrap generiert oder während Sessions aufgebaut.

**Current Status:**
- Manifest version: **AAMS/2.0**
- Whitepapers: **10** + INDEX.md → WH-001..WH-010
- Closed workpapers: **52** in `WORKING/WORKPAPER/closed/`
- Active workpapers: **2** in `WORKING/WORKPAPER/`
- Observe workpapers: **3** in `WORKING/WORKPAPER/observe/`
- LTM: **136** entries (audit-log + ChromaDB)
- topic_registry: maschinenlesbar in `.agent.json`
- `.aams-version`: exists (upgrade detection)
- Workpaper Lifecycle: active → observe → closed
- Guidelines: **12** in `WORKING/GUIDELINES/`
- Health-Score: **10/10**
- Naming Schema: Whitepapers → WH-*, Workpapers → WP-*
- Last release: **v2.2.0** (2026-04-30)

---

## AAMS in freier Wildbahn

Projekte, die AAMS bereits einsetzen → [**SHOWCASE.md**](SHOWCASE.md)

Du willst dein Projekt hinzufügen? Öffne einen PR — wir freuen uns zu sehen, was du baust.

---

## Schnellreferenz

| Komponente | Pfad | Zweck |
|---|---|---|
| Manifest | `.agent.json` | Workspace-Vertrag |
| Kontext | `READ-AGENT.md` | Vollständiger Projektzustand |
| Bridge | `AGENTS.md` | Multi-Tool-Einstiegspunkt |
| Workpapers | `WORKING/WORKPAPER/` | Session-Protokolle (active → observe → closed) |
| Observe | `WORKING/WORKPAPER/observe/` | Pausierte Workpapers — warten auf Input |
| Whitepapers | `WORKING/WHITEPAPER/` | Architektur-Wahrheit |
| Entscheidungslog | `WORKING/DIARY/` | Monatliches Entscheidungsjournal |
| Langzeitgedächtnis | `WORKING/MEMORY/` | Akkumulierter Kontext |
| Richtlinien | `WORKING/GUIDELINES/` | **12** Guidelines (Documentation Model, Naming Schema, Workpaper Lifecycle, Decision-Promotion, File Protocol, LTM Rules, Topic Registry, Wiki Lint, AAMS Doctor, Git Safety, README Consistency, Diary Format) |
| Logs | `WORKING/LOGS/` | Audit-Trail |

---

## Contract Reference

- [`reference/CONTRACT.md`](./reference/CONTRACT.md) — Technische Referenz (Agent Manifest)
- [`reference/AGENT.json`](./reference/AGENT.json) — Vollständig annotiertes Manifest
- [`reference/AGENT_SCHEMA.json`](./reference/AGENT_SCHEMA.json) — JSON Schema zur Validierung

---

## Lizenz

MIT — siehe [LICENSE](LICENSE)

---

<p align="center"><strong>Every agent. One file.</strong></p>
<p align="center">AAMS/2.0 — Agent Manifest (nicht Specification)</p>
<p align="center">Manifest-Prinzip (D9): AAMS describes, es schreibt kein Verhalten vor.</p>
