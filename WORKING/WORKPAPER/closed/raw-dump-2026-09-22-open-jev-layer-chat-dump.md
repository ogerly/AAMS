JEV ist kein offenen Model, nur über API möglich. also für uns und AAMS kommt das nicht in frage. 

deshalb diese gedanken und der weg den wir gehen werden. bzw. dieses weg wollen wir analysieren und schauen ob es für unsere spezifikation interesannt ist oder eher in unser proxy schciht zwischen lm studio, open code und vs code .. 
 
"D:\Entwicklung\Projekte\MANTIS-LLM-PROXY-3"


JV ist nihct offen?

Genau. **Das originale JEV von TypeSafe AI ist kein Open-Source-Modell.** Ich hatte das in meiner vorherigen Antwort zu ungenau formuliert.

Stand **22. September 2026**:

* **Jev selbst:** geschlossenes, gehostetes Modell
* **Weights:** nicht veröffentlicht
* **Self-Hosting des originalen JEV:** nicht möglich
* **API:** Nutzung über TypeSafe
* **Open-Source:** Es gibt inzwischen mehrere **Open-Jev-Reimplementierungen**, aber das sind nicht die originalen JEV-Weights. ([GitHub][1])

### Für dich ist aber der interessante Teil:

Es gibt mittlerweile tatsächlich **lokale Open-Jev-Projekte**, und eines davon verwendet explizit **Qwen3.8-27B**:

[Zefan-Cai/Open-Jev auf GitHub](https://github.com/Zefan-Cai/Open-Jev?utm_source=chatgpt.com)

Dort gibt es bereits:

```text
Qwen3.5-2B
Qwen3.5-9B
Qwen3.8-27B
```

als Basis für eine lokale Jev-artige Entscheidungsarchitektur. Die 2B/9B-Varianten haben bereits veröffentlichte Adapter/Checkpoints; die 27B-Variante befindet sich laut Repository aktuell noch im Training bzw. in Evaluation. ([GitHub][2])

Und das ist für **deinen Rechner wesentlich interessanter** als die originale Cloud-Jev-API.

Du hast:

```text
RTX 5090 32 GB
       │
       └── Qwen3.8-27B
             │
             ├── normales LLM
             │
             └── Open-Jev / Decision Layer
```

Damit könntest du prinzipiell eine **lokale JEV-artige Decision Engine** bauen.

Es gibt sogar noch andere lokale Ansätze wie **OpenSourceJev**, **LLM2Jev** und **Rizzo Flow**, die genau dieses Prinzip mit offenen Modellen umsetzen. ([GitHub][3])

### Und damit korrigiere ich auch meine vorherige Empfehlung

Für **deinen AAMS-Ansatz** würde ich nicht einfach die TypeSafe-API als zusätzliche Cloud-Abhängigkeit einbauen.

Ich würde mir **Open-Jev lokal genauer ansehen**.

Denn dann hätten wir:

```text
              AAMS
               │
               │ State
               ▼
        ┌──────────────┐
        │  Open-Jev    │
        │   lokal      │
        └──────┬───────┘
               │
       Entscheidung
       + Wahrscheinlichkeit
               │
        ┌──────┴──────┐
        ▼             ▼
      Qwen          Tool
     Reasoning     Execution
        │             │
        └──────┬──────┘
               ▼
              AAMS
```

**Das wäre für deine Philosophie „lokal, souverän, Open Source“ erheblich passender.**

Und mit deiner **RTX 5090 + Qwen3.8-27B** könnten wir sogar untersuchen, ob wir deinen bestehenden Qwen nicht direkt zu einer **AAMS Decision Engine** umbauen können, statt ein weiteres Modell daneben zu stellen.

Das wäre meiner Ansicht nach der spannendere Weg.

[1]: https://github.com/kyegomez/open-jev?utm_source=chatgpt.com "GitHub - kyegomez/open-jev: an open-source, from-first-principles reconstruction of the ideas behind TypeSafe AI's Jev, written in pytorch · GitHub"
[2]: https://github.com/Zefan-Cai/Open-Jev?utm_source=chatgpt.com "GitHub - Zefan-Cai/Open-Jev · GitHub"
[3]: https://github.com/sabeel111/OpenSourceJev?utm_source=chatgpt.com "GitHub - sabeel111/OpenSourceJev: Turning an LLM model into a Jev like System. · GitHub"



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

JEV mit API im einsatz würde so aussehen. was wir auch auf die open variante anwenden können. eine cloud / api variante ist keine option für uns. 


Ja. **Jev passt erstaunlich gut zu deinem bestehenden Stack**, aber nicht als Ersatz für Qwen3.8, LM Studio oder OpenCode. Der interessante Punkt ist gerade die Kombination:

> **Qwen denkt und erzeugt. Jev entscheidet. AAMS hält den Zustand und die Wahrheit. OpenCode führt aus.**

Jev ist genau für diese „Entscheidungsschicht“ gebaut: Es erzeugt keinen Text und keinen Code, sondern liefert typisierte Entscheidungen, Scores und Konfidenzen. Ein Request kann mehrere Entscheidungen parallel auswerten. Die dokumentierte Latenz liegt bei etwa 70–500 ms und der aktuelle Preis bei $0,042 pro 1 Mio. Input-Tokens. ([Made with Jev][1])

## Ich würde deinen Stack so erweitern

```text
                         ┌─────────────────────┐
                         │       AAMS          │
                         │                     │
                         │ WHITEPAPER          │
                         │ WORKPAPER           │
                         │ MEMORY              │
                         │ Diary               │
                         └──────────┬──────────┘
                                    │
                                    ▼
┌─────────────┐             ┌───────────────┐
│ OpenCode    │────────────▶│     Qwen      │
│ Agent       │             │ 3.8 27B       │
└──────┬──────┘             │ LM Studio     │
       │                    └───────┬───────┘
       │                            │
       │       "Was soll ich tun?" │
       │                            ▼
       │                    ┌───────────────┐
       └───────────────────▶│     JEV       │
                            │ Decision      │
                            │ Layer         │
                            └───────┬───────┘
                                    │
                         ┌──────────┼──────────┐
                         ▼          ▼          ▼
                       TOOL       MODEL      STOP
```

Das ist für **AAMS sogar konzeptionell sehr interessant**.

---

# 1. Der wichtigste Einsatz: Qwen muss nicht mehr jede Entscheidung selbst treffen

Nehmen wir an, dein OpenCode-Agent arbeitet an einem Projekt.

Qwen bekommt:

> „Ich habe diese Änderung vorgenommen. Was soll ich jetzt tun?“

Normalerweise muss das LLM selbst entscheiden:

```text
Code prüfen?
Tests ausführen?
Recherche?
Dokumentation lesen?
weiter programmieren?
Commit?
User fragen?
```

Das ist eigentlich eine schlechte Verwendung eines generativen LLM.

Mit Jev könntest du daraus machen:

```text
STATE

AAMS:
- aktuelle Aufgabe
- aktueller WORKPAPER
- letzte Aktionen
- Git diff
- Testergebnisse
- offene TODOs

QUESTION

next_action:

[
  "inspect_code",
  "run_tests",
  "search_documentation",
  "continue_implementation",
  "update_aams",
  "ask_user",
  "finish"
]
```

Jev liefert beispielsweise:

```json
{
  "choice": "run_tests",
  "probabilities": {
    "inspect_code": 0.08,
    "run_tests": 0.81,
    "search_documentation": 0.03,
    "continue_implementation": 0.04,
    "update_aams": 0.01,
    "ask_user": 0.01,
    "finish": 0.02
  },
  "confidence": 0.94
}
```

**Dann entscheidet nicht Qwen, sondern dein Orchestrator.**

Qwen schreibt weiterhin den Code.

---

# 2. AAMS + Jev könnte richtig interessant werden

Ich sehe bei deinem AAMS-Konzept sogar eine sehr natürliche Erweiterung.

AAMS beschreibt im Grunde:

```text
Was ist wahr?
Was ist der aktuelle Zustand?
Was wurde gemacht?
Was ist noch offen?
```

Jev beantwortet:

```text
Was soll aufgrund dieses Zustands passieren?
```

Das sind zwei unterschiedliche Dinge.

### AAMS

**State / Memory / Truth**

### Qwen

**Reasoning / Generation**

### Jev

**Decision**

### OpenCode

**Execution**

Damit entsteht ein ziemlich sauberes Agentenmodell:

```text
              AAMS
               │
               │ STATE
               ▼
            ┌───────┐
            │  JEV  │
            └───┬───┘
                │
          DECISION
                │
                ▼
             QWEN
                │
             OUTPUT
                │
                ▼
           OpenCode
                │
             ACTION
                │
                ▼
              AAMS
```

Das ist wesentlich interessanter als einfach „noch ein weiteres LLM in OpenCode einzubauen“.

---

# 3. Zweiter sehr guter Einsatz: Qwen kontrollieren

Das halte ich bei deinem Setup sogar für **einen der besten ersten Tests**.

Qwen erzeugt Code.

Jev bewertet anschließend den Code gegen definierte Kriterien.

Beispielsweise:

```text
STATE:

Git diff:
<aktueller diff>

AAMS rules:
<Projektregeln>

Question 1:
Does the change violate an architecture rule?

Question 2:
Does it introduce unnecessary complexity?

Question 3:
Is the implementation complete?

Question 4:
Should this change be accepted?

Question 5:
Does it require human review?
```

Du bekommst dann mehrere Entscheidungen in **einem Jev-Aufruf**. Genau dieses parallele Fragenmodell ist Teil des Designs von Jev. ([Made with Jev][1])

Damit könnte dein Agent beispielsweise sagen:

```text
Qwen:
    schreibt Code

        ↓

Jev:
    architecture = OK       0.96
    complexity   = LOW      0.91
    complete     = YES      0.88
    human_review = NO       0.94

        ↓

OpenCode:
    git diff
    tests
    commit
```

---

# 4. Noch besser: AAMS als Regelbasis

Das würde ich bei dir **nicht als allgemeine Jev-Konfiguration** bauen.

Sondern projektbezogen.

Zum Beispiel:

```text
.agent.json

WORKING/
├── WHITEPAPER/
├── WORKPAPER/
├── MEMORY/
└── JEV/
    ├── routing.md
    ├── architecture.md
    ├── quality.md
    ├── completion.md
    └── security.md
```

Dann könnte dein Agent aus den AAMS-Regeln Jev-Fragen ableiten.

Zum Beispiel:

```markdown
# architecture.md

- Business logic must not be placed inside Vue components.
- API access must use the service layer.
- No direct Supabase access from UI components.
- No duplicated state management.
```

Jev bekommt dann:

```text
STATE:
Git diff + relevant AAMS rules

QUESTION:
Does this change violate any architecture rule?

OPTIONS:
- yes
- no
```

Das ist **viel robuster**, als Qwen zu sagen:

> „Bitte überprüfe deinen eigenen Code.“

---

# 5. Jev als Gatekeeper für Agenten

Das wird mit mehreren Agents richtig interessant.

Du hast beispielsweise:

```text
             OpenCode
                │
                ▼
             Qwen
                │
                ▼
        ┌───────────────┐
        │      JEV      │
        └───────┬───────┘
                │
       ┌────────┼─────────┐
       ▼        ▼         ▼
    Qwen      Search     User
   Coding     Agent      fragen
```

Jev könnte entscheiden:

```text
Welcher Worker soll die Aufgabe übernehmen?

OPTIONS:

coding
research
documentation
testing
security
human
```

Und das ist genau die Art von Routing, für die Jev gedacht ist. ([Made with Jev][2])

---

# 6. Für deinen lokalen Stack würde ich Jev NICHT als Hauptmodell verwenden

Das ist wichtig.

Deine RTX 5090 bleibt sinnvoll für:

```text
LM Studio
    │
    └── Qwen 3.8 27B
             │
             ├── reasoning
             ├── coding
             ├── planning
             ├── documentation
             └── generation
```

Jev sitzt **außerhalb** davon:

```text
                  INTERNET
                     │
                     ▼
              TypeSafe / Jev API
                     │
                     │ decisions
                     ▼
RTX 5090 ── LM Studio / Qwen
                     │
                     ▼
                  OpenCode
                     │
                     ▼
                    AAMS
```

Jev ist derzeit **kein lokales Modell** und hat keine Open Weights; es wird als Managed API angeboten. ([Jev Agent][3])

Das bedeutet:

**Deine eigentliche Intelligenz bleibt lokal.**

Jev wird nur für die sehr kleinen, gezielten Entscheidungen nach außen gerufen.

---

# 7. Das ist für deinen Datenschutz sogar relativ interessant

Du musst Jev nicht unbedingt dein gesamtes AAMS geben.

Ich würde einen **Decision Context Builder** bauen.

Also:

```text
AAMS
  │
  ▼
Decision Context Builder
  │
  ├── relevante Regeln
  ├── aktueller Git diff
  ├── aktuelle Aufgabe
  ├── letzte Aktion
  └── Testergebnis
          │
          ▼
        JEV
```

Nicht:

```text
Jev bekommt komplettes AAMS
```

sondern:

```text
Jev bekommt nur den Zustand,
der für diese konkrete Entscheidung notwendig ist.
```

Das entspricht auch ziemlich genau dem Gedanken hinter Jev: **State hinein → definierte Fragen → typisierte Entscheidung heraus.** ([Made with Jev][1])

---

# 8. Ein sehr interessanter Einsatz für AAMS: Context-Window-Wechsel

Hier sehe ich bei dir einen besonders schönen Anwendungsfall.

Du benutzt AAMS bereits, um Kontextverluste zwischen Agent-Sessions zu verhindern.

Stell dir vor:

```text
Qwen Agent Session
        │
        ▼
   Aufgabe läuft
        │
        ▼
  Kontext wird voll
        │
        ▼
       AAMS
        │
        ▼
   neuer Context
```

Vor dem Übergang könnte Jev entscheiden:

```text
Is the current AAMS state sufficient
to continue the task?

YES
NO
RECONSTRUCT
ASK USER
```

Oder:

```text
Which information is critical
for the next context window?

architecture
current_task
last_error
decision_history
user_requirement
none
```

Damit könnte AAMS langfristig einen **automatischen Context-Governor** bekommen.

Das wäre für dein System wesentlich spannender als ein simples „Jev MCP“.

---

# 9. Und dann kommt die richtig interessante Ebene: Confidence

Der entscheidende Unterschied zu einem normalen LLM-Routing-Prompt ist die **Konfidenz**.

Du könntest Regeln definieren:

```text
confidence >= 0.90
    → automatisch ausführen

0.70 - 0.90
    → Qwen erneut prüfen lassen

0.50 - 0.70
    → zweiten Entscheidungsweg

< 0.50
    → Mensch
```

Zum Beispiel:

```text
Jev

next_action = "run_tests"
confidence = 0.96

→ automatisch
```

aber:

```text
next_action = "modify_database"
confidence = 0.61

→ NICHT automatisch
→ Qwen analysiert
→ eventuell User fragen
```

Genau diese Art von Confidence-gesteuertem Routing ist einer der vorgesehenen Einsatzzwecke. ([Made with Jev][1])

---

# 10. Ich würde deshalb mit einem einzigen kleinen Projekt anfangen

Nicht gleich dein komplettes OpenCode-System umbauen.

Ich würde einen kleinen **`aams-jev-gate`** bauen.

```text
aams-jev-gate
│
├── state/
│   └── builder
│
├── decisions/
│   ├── routing
│   ├── quality
│   ├── completion
│   └── safety
│
├── thresholds/
│   └── default.json
│
└── index.ts
```

API beispielsweise:

```text
POST /decision
```

Input:

```json
{
  "project": "AAMS",
  "task": "...",
  "state": "...",
  "question": "next_action"
}
```

Output:

```json
{
  "decision": "continue",
  "confidence": 0.94,
  "probabilities": {
    "continue": 0.94,
    "test": 0.03,
    "research": 0.02,
    "human": 0.01
  }
}
```

Dann hängt OpenCode daran.

---

# 11. Noch besser: MCP

Für deinen OpenCode/VS-Code-Workflow würde ich danach **Jev als MCP-Tool** verfügbar machen.

Es gibt bereits ein Community-MCP für Jev, das genau diese Richtung verfolgt. Es stellt u. a. `choice`, `score` und `noul`-artige Entscheidungen für Agenten bereit. ([GitHub][4])

Aber ich würde **nicht einfach blind irgendeinen MCP installieren**.

Ich würde bei dir eher einen sehr kleinen eigenen Adapter bauen:

```text
OpenCode
   │
   ├── read_aams
   ├── edit_file
   ├── run_tests
   ├── git
   │
   └── jev_decide
          │
          ▼
       Jev API
```

Dadurch bleibt deine Architektur unter deiner Kontrolle.

---

# 12. Und daraus könnte etwas ziemlich Eigenständiges entstehen

Ich sehe hier sogar eine mögliche Weiterentwicklung von AAMS:

```text
AAMS
=
Agent Memory / State

+

Jev
=
Agent Decision Layer

+

Qwen
=
Agent Reasoning / Generation

+

OpenCode
=
Agent Execution

+

Git
=
Agent History

```

Also:

> **AAMS speichert, Qwen denkt, Jev entscheidet, OpenCode handelt.**

Das ist wesentlich sauberer als der heute typische Ansatz:

> „Ein großes LLM macht einfach alles.“

Und es passt sehr gut zu deiner bisherigen AAMS-Idee, weil du damit **Reasoning und State ohnehin schon voneinander trennst**.

---

## Mein konkreter Vorschlag für deinen 5090-Rechner

Ich würde es in **drei Stufen** aufbauen:

### Stufe 1 – heute

```text
VS Code
  ↓
OpenCode
  ↓
Qwen 3.8 27B
  ↓
AAMS
```

plus:

```text
Jev API
  ↓
jev_decide()
```

Nur für:

* `next_action`
* `task_complete`
* `needs_human`
* `needs_research`

### Stufe 2

Jev wird zum **Agent Router**:

```text
              JEV
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
     Qwen    Search    Human
```

### Stufe 3

Jev wird zum **AAMS Decision Engine**:

```text
             AAMS
               │
               ▼
         Decision Context
               │
               ▼
              JEV
               │
        ┌──────┼──────┐
        ▼      ▼      ▼
      Qwen   Tool    Human
        │      │
        └──┬───┘
           ▼
          AAMS
```

**Das wäre meiner Meinung nach der wirklich interessante Teil.**

Und noch etwas: Die Jev-Leute selbst beschreiben inzwischen genau dieses Muster als **„LLM writes, Jev decides, code acts“**. ([Made with Jev][2])

Für deinen Stack würde ich es sogar noch etwas erweitern:

> **AAMS remembers → Qwen reasons → Jev decides → OpenCode acts → AAMS records.**

Das ist eine Architektur, die ich tatsächlich einmal sauber als kleines Experiment auf deinem bestehenden AAMS aufbauen würde, statt Jev einfach als weiteres Modell in OpenCode zu hängen.

[1]: https://madewithjev.com/what-is-jev?utm_source=chatgpt.com "What is Jev? TypeSafe AI's System One model — Made with Jev"
[2]: https://madewithjev.com/what-is-jev-engineering?utm_source=chatgpt.com "What is Jev Engineering? — Made with Jev"
[3]: https://jev-agent.com/?utm_source=chatgpt.com "What is Jev? TypeSafe AI's System One decision model explained"
[4]: https://github.com/rajasekharponakala/jev-mcp?utm_source=chatgpt.com "GitHub - rajasekharponakala/jev-mcp: MCP server wrapping TypeSafe's Jev System One models — typed noul/choice/score judgments for AI agents · GitHub"
