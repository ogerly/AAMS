JEV ist kein offenen Model, nur über API möglich. also für uns und AAMS kommt das nicht in frage. 

deshalb diese gedanken und der weg den wir gehen werden. bzw. dieses weg wollen wir analysieren und schauen ob es für unsere spezifikation interesannt ist oder eher in unser proxy schciht zwischen lm studio, open code und vs code .. 
 
"D:\Entwicklung\Projekte\MANTIS-LLM-PROXY-3"



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
