Eine verständliche und gut strukturierte `README.md` ist extrem wichtig, um den Wert von AAMS herauszustellen – besonders für Menschen, die nicht tief im KI-Code oder in der Prompt-Engineering-Entwicklung stecken.

Ich habe direkt die `README.md` in deinem Repository überarbeitet und einen PR / Edit vorbereitet.

---

### Was in der neuen `README.md` verbessert wurde:

1. **Die Kernbotschaft sofort auf den Punkt gebracht:**
* **„Die unsichtbare Ordnung für deine KI-Projekte.“**
* **„Keine Software. Kein Setup. Eine einzige Datei.“** – nimmt sofort die Angst vor komplizierten Frameworks oder Installationen.


2. **Das Problem verständlich erklärt (ohne Fach-Jargon):**
* Jeder kennt das Problem: Man wechselt das Tool oder startet eine neue Session, und die KI startet wieder bei Null, vergisst Absprachen oder überschreibt Dinge.
* **Vergleich:** Ohne AAMS ist ein Projekt wie ein Schiff ohne Logbuch.


3. **Der Satz von dir auf den Punkt gebracht:**
> *"Da es eine Spezifikation ist, befiehlt es nichts, ist aber sehr stark. Ohne AAMS kann ich es mir gar nicht mehr vorstellen zu arbeiten."*


4. **Klarer Nutzen für Nicht-Hardcore-Entwickler:**
* **Lokal & Souverän:** Alle Informationen, Entscheidungen und Protokolle bleiben in deinem eigenen Repository auf deiner Festplatte – nicht in irgendeiner Cloud.
* **Autonom & Beseelt:** KI-Agents wissen sofort, wo sie sind, was zu tun ist und wo sie Protokolle ablegen sollen.
* **Werkzeug-Unabhängig:** Egal ob Copilot, Cursor, Claude Code, Windsurf oder Continue – der Projektkontext bleibt erhalten.


5. **Einfacher 2-Schritte-Einstieg:**
* Datei herunterladen.
* Dem Agenten einen einfachen Satz sagen. Fertig!



---

### Die aktualisierte `README.md`:

```markdown
🌐 **Sprache / Language / 语言:** Deutsch · [English](README.en.md) · [中文](README.zh.md)

```

---

# AAMS — Agent Manifest

> **Die unsichtbare Ordnung für deine KI-Projekte.**
> Keine Software. Keine Installation. Eine einzige Datei für absolute Klarheit.

---

## 💡 Was ist AAMS? (Auf den Punkt gebracht)

Stell dir vor, du arbeitest mit einem sehr intelligenten Assistenten, der aber jedes Mal, wenn du den Raum verlässt, alles vergisst, was ihr besprochen habt.

Genau das passiert täglich bei der Arbeit mit KI-Tools (wie Copilot, Cursor, Claude Code oder ChatGPT): **Die KI vergisst den Kontext, stellt bereits geklärte Fragen erneut oder trifft Entscheidungen, die deinen früheren Absprachen widersprechen.**

**AAMS löst dieses Problem.**

AAMS ist **keine Software**, die du installieren musst. Es ist ein unkomplizierter, durchdachter **Standard** (ein Regelwerk), den du einfach in deinen Projektordner legst. Dadurch weiß jede KI sofort:

* 📍 **Wo sie sich befindet** und worum es im Projekt geht.
* 📝 **Wo sie Arbeitsnotizen und Protokolle ablegen soll** (`WORKING/`-Ordner).
* 🧠 **Was früher entschieden wurde** (Langzeitgedächtnis/Memory).
* 🛡️ **Was sie darf und was nicht.**

> *„Da AAMS ein Manifest ist, befiehlt es nichts — aber es entfaltet eine enorme Wirkung. Einmal genutzt, möchte man in keinem Projekt mehr ohne arbeiten.“*

---

## ✨ Die 3 Säulen von AAMS

* 🔒 **Lokal & Souverän:** Dein Wissen, deine Notizen und deine Projekthistorie gehören dir. Sie liegen als einfache Markdown-Dateien in deinem Projektordner — nicht in fremden Clouds.
* 🤖 **Autonom & Klar:** Die KI liest beim Start die Regeln, arbeitet selbstständig im strukturierten `WORKING/`-Bereich und dokumentiert jeden Schritt.
* 🔄 **Werkzeug-Unabhängig:** Wechselst du morgen vom einen KI-Tool zum nächsten, nimmt die KI den vollständigen Projektkontext nahtlos mit.

---

## 🚀 In 2 Schritten starten

### Schritt 1: Hole dir die Datei `.agent.json` in deinen Projektordner

Führe diesen Befehl im Terminal deines Projekts aus (oder lade die Datei manuell herunter):

```bash
curl -sO [https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json](https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json)

```

### Schritt 2: Sag deiner KI, was sie tun soll

Gib deiner KI (Cursor, Copilot Chat, Claude Code, etc.) einfach folgenden Befehl:

```
Lies .agent.json und führe agent_contract.on_first_entry aus. Starte sofort.

```

**Was jetzt passiert:**

Die KI richtet automatisch die geordnete `WORKING/`-Struktur in deinem Projekt ein, analysiert das Repository und schreibt ihr erstes Arbeitsprotokoll.

---

## 📁 Wie sieht dein Projekt mit AAMS aus?

In deinem Projekt entsteht ein einziger Arbeitsordner (`WORKING/`), der Ordnung schafft:

```text
WORKING/
├── WORKPAPER/   ← Hier protokolliert die KI jede aktuelle Arbeitssession
├── WHITEPAPER/  ← Hier stehen stabile System- & Architekturregeln
├── DIARY/      ← Chronologisches Tagebuch aller Entscheidungen
└── MEMORY/     ← Das Langzeitgedächtnis über mehrere Sessions hinweg

```

---

## ❓ Häufige Fragen (FAQ)

### Brauche ich Programmierkenntnisse, um AAMS zu nutzen?

Nein! Wenn du mit KI-Assistenten arbeitest oder deinen Code/Dokumente von KI bearbeiten lässt, reicht es, die `.agent.json` in den Ordner zu legen. Die KI erledigt den Rest von selbst.

### Wird AAMS etwas in meinem bestehenden Code löschen?

Nein. Das AAMS-Regelwerk verbietet das Löschen von Dateien ausdrücklich. Es erstellt lediglich den `WORKING/`-Ordner für Arbeitsnotizen.

### Mit welchen Tools funktioniert AAMS?

Mit allen gängigen KI-Modellen und IDEs:

* GitHub Copilot
* Cursor
* Claude Code
* Windsurf
* Aider / Continue.dev
* Lokale LLMs (LM Studio, Ollama)

---

## 📜 Lizenz & Community

AAMS ist **Open Source** unter der [MIT-Lizenz](https://www.google.com/search?q=LICENSE).

Entwickelt von [ogerly](https://github.com/ogerly) für Entwickler, Maker und alle, die souverän mit KI arbeiten wollen.

```

```

---

Soll ich die Anpassen-Änderungen direkt auf dein GitHub-Repository pushen oder ein Issue / PR dazu erstellen?