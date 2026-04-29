# Workpaper: Harte Strategische Neuausrichtung
# AAMS — Spezifikation oder Verhaltensvertrag?

**Datum:** 2026-04-10  
**Autor:** @ogerly / DEVmatrose  
**Typ:** Strategische Analyse / Grundsatzentscheidung  
**Priorität:** Kritisch — betrifft Kern-Identität von AAMS  
**Referenz:** `WORKING/WORKPAPER/2026-04-10-AAMS-WORKSPACE-field-report-workspace-container.md`

---

## Session Goal

Scharf analysieren ob AAMS weiterhin als "Spezifikation" bezeichnet werden sollte — oder ob eine ehrliche Umbenennung hin zu **Agent-Contract / Protokoll** strategisch und inhaltlich richtiger ist. Entscheidung herbeiführen. Konsequenzen ableiten.

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-10-AAMS-STRAT-reorientation-spec-vs-contract.md` | ✅ |

---

## 1. Ausgangslage — Was sagt die Kritik?

Die zentrale These aus der strategischen Analyse lautet:

> **AAMS war nie wirklich eine Spezifikation. Es war immer ein Protokoll das sich Spec genannt hat weil der Begriff vertrauter klingt.**

Das ist eine harte Aussage. Sie muss geprüft werden — nicht akzeptiert oder verworfen ohne Evidenz.

---

## 2. Was ist eine "Spezifikation" — präzise Definition

Eine Spezifikation im Software-Kontext (RFC, OpenAPI, JSON Schema) definiert:

- **Struktur** — wie Daten aussehen
- **Schnittstellen** — welche Operationen erlaubt sind
- **Validierbarkeit** — konform vs. nicht-konform ist maschinenprüfbar
- **Keine Verhaltensvorschriften** — *wie* ein System reagiert ist Implementierungssache

Beispiele: JSON Schema sagt "dieses Feld muss ein String sein." Es sagt nicht "wenn das Feld fehlt, erstelle es und logge einen Konflikt."

---

## 3. Was enthält `.agent.json` tatsächlich?

Analyse des aktuellen Inhalts:

| Element | Art |
|---------|-----|
| `workspace.root`, `workspace.directories` | Struktur-Definition ✅ (Spec-Anteil) |
| `naming_conventions` | Struktur-Definition ✅ (Spec-Anteil) |
| `agent_contract.on_first_entry` | **Verhaltensvorschrift** ❌ (kein Spec-Anteil) |
| `agent_contract.on_session_start` | **Verhaltensvorschrift** ❌ (kein Spec-Anteil) |
| `agent_contract.on_session_end` | **Verhaltensvorschrift** ❌ (kein Spec-Anteil) |
| `bootstrap_rules` | **Verhaltensvorschrift** ❌ (kein Spec-Anteil) |
| `policies.secrets` | Verhaltensregel ❌ (kein Spec-Anteil) |
| `_spec: "AAMS-MINI/1.0"` | Meta-Bezeichner (neutral) |

**Ergebnis:** Der Anteil reiner Struktur-Definition in `.agent.json` ist eine Minderheit. Die Mehrheit der Regeln sind **prozedurale Verhaltensvorschriften** — was ein Agent *tun* soll, *wann* er es tun soll, *wie* er auf Zustände reagieren soll.

Das ist per Definition kein Spec. Das ist ein **Protokoll** mit **Verhaltensvertrag**.

---

## 4. Der WORKSPACE-Befund als Beweis

Der Field Report (`2026-04-10-AAMS-WORKSPACE-field-report-workspace-container.md`) liefert den empirischen Beleg:

Das WORKSPACE-Problem zeigt exakt die Lücke zwischen "Spezifikation" und "was AAMS tatsächlich sein muss":

- Eine Spezifikation würde sagen: "WORKING/ muss existieren."
- Ein Protokoll / Verhaltensvertrag muss sagen: "Wenn WORKSPACE/WORKING/ **und** ./WORKING/ existieren → Halt. Conflict-Report. Frage User. Mergestrategie anwenden."

Die Community (MantisClaw, Mantis-OS) hat eigenständig den Container erfunden, weil das **Protokoll** gefehlt hat — nicht weil die **Struktur** unklar war. Das ist der Beweis: AAMS-User brauchen Verhaltensvorschriften, keine Strukturdefinitionen.

---

## 5. Die drei Optionen — kritische Bewertung

### Option A — Saubere Aufteilung (AAMS-Spec / AAMS-Protocol / AAMS-Bootstrap)

**Analyse:**  
Intellektuell sauber. Praktisch toxisch für ein Projekt dessen Kernwert **Einfachheit** ist.

> "One file. Every repo. No more starting from zero."

Drei Artefakte statt eins bricht dieses Versprechen. Option A ist die akademische Antwort, nicht die richtige.

**Urteil: Verwerfen.**

### Option B — AAMS ist ein Agent-Contract, kein Spec

**Analyse:**  
Ehrlich. Präzise. Konsistent mit dem was `.agent.json` tatsächlich tut.

Das Wort "Manifest" im Namen (Autonomous Agent **Manifest** Specification) ist kein Zufall — ein Manifest ist eine Absichtserklärung mit Verbindlichkeit, kein formales Schema. Der Name selbst widerspricht dem Wort "Specification" bereits.

Ein **Verhaltensvertrag** (Agent-Contract) zwischen Agent und Repository ist exakt was AAMS liefert:
- Struktur die eingehalten werden muss ← Vertragsbestandteil
- Verhalten das ausgeführt werden muss ← Vertragsbestandteil  
- Konsequenzen bei Abweichung ← Vertragsbestandteil

Das Schlüsselwort `agent_contract` in `.agent.json` existiert **bereits** — der Vertrag ist da, er heißt nur noch nicht so im Außenauftritt.

**Urteil: Stärkste Option. Sehr wahrscheinlich richtig.**

### Option C — Neudefinition von "Spezifikation"

**Analyse:**  
Sprachlich schwach. "Spezifikation" hat eine etablierte Bedeutung in der Softwareentwicklung. Diesen Begriff umzudeuten erzeugt Verwirrung bei neuen Adoptern und verwässert die Posititionierung.

**Urteil: Verwerfen.**

---

## 6. Test: Hält Option B der Prüfung stand?

Wenn AAMS ein **Verhaltensvertrag** ist — was bedeutet das konkret?

| Frage | Antwort unter "Spec" | Antwort unter "Contract" |
|-------|---------------------|--------------------------|
| Was validiert AAMS? | Dateistruktur | Dateistruktur + Agent-Verhalten |
| Wer ist Vertragspartei? | Dataformat-Consumer | Agent + Repository |
| Was passiert bei Verstoß? | Validierungsfehler | Definiertes Eskalationsverhalten |
| Ist WORKSPACE-Discovery ein Teil davon? | Nein (außerhalb Spec-Scope) | Ja (Protokoll-Verhalten) |
| Ist on_session_start ein Teil davon? | Nein (außerhalb Spec-Scope) | Ja (Vertragsbestandteil) |

Alle Antworten unter "Contract" sind kohärenter mit dem was AAMS tut.

**Befund: Option B besteht die Prüfung.**

---

## 7. Konsequenzen bei Annahme von Option B

### 7.1 Namens- und Selbstbeschreibung

Aktuell:
> *AAMS — Autonomous Agent Manifest Specification*

Vorschlag:
> *AAMS — ein maschinenlesbarer Verhaltensvertrag für agentenbasiertes Arbeiten. Framework-unabhängig. Drop-in für jedes Repo.*

Der Akronym "AAMS" bleibt erhalten (Wiedererkennungswert). Die Bedeutung von "Specification" wird ggf. in "System" oder "Standard" umgedeutet — oder das Akronym wird entkoppelt (AAMS als Eigenname).

### 7.2 Schlüsseländerungen in `.agent.json`

| Aktuell | Vorschlag | Begründung |
|---------|-----------|------------|
| `"_spec": "AAMS-MINI/1.0"` | `"_contract": "AAMS/2.0"` | Ehrlichere Bezeichnung |
| `"agent_contract": {...}` | Bleibt, wird Kern-Konzept | Bereits korrekt benannt |
| `"workspace.root": "./WORKING"` | + Discovery-Logik (WORKSPACE-Proposal) | Contract definiert Verhalten |

### 7.3 Versionierung

Der Wechsel von Spec → Contract ist ein **Breaking Change** in der Selbstdefinition von AAMS.

Empfehlung: AAMS/2.0 als neue Major-Version. Begründung: konzeptuelle Neudefinition, nicht nur Feature-Addition.

### 7.4 Dokumentation

- `reference/SPEC.md` → `reference/CONTRACT.md` oder dual halten (SPEC.md als legacy alias)
- `README.md`: Außendarstellung anpassen
- `AGENTS.md`: "Specification" → "Agent-Contract"

### 7.5 WORKSPACE-Integration

Der WORKSPACE-Proposal aus dem Field Report ist unter dem Contract-Modell **natürlich integrierbar**: Discovery-Logik, Conflict-Check, Migration-Strategie sind alles Verhaltensvorschriften — genau das was ein Contract definiert, aber eine Spec nicht kann.

---

## 8. Gegenargumente — fair bewertet

**"Specification" hat Signalwert für die Tech-Community"**  
→ Stimmt. "Spec" signalisiert "ich bin ein Standard, kein Framework." Das hat Adoptions-Wert.  
→ Gegenfrage: Wer soll adopten? Agents. Agents brauchen Verhaltensregeln, keine Schemas. Der Signalwert zieht falsche Adressaten an.

**"Contract klingt nach Legal, nicht nach Tech"**  
→ Stimmt teilweise. Aber "Agent Contract" hat in der KI-Welt bereits eine semantische Bedeutung (vgl. Principal-Agent-Theorie, Contract-Based Agents in MAS-Literatur).  
→ Gegenfrage: GitHub hat "Actions", Kubernetes hat "Pods" — Tech-Begriffe werden durch Verwendung definiert.

**"Der Aufwand der Umbenennung ist hoch"**  
→ Stimmt. README, Docs, SPEC.md, alle Whitepapers sind betroffen.  
→ Aber: Wenn die Grundidee falsch benannt ist, wächst der Schaden mit jedem neuen Dokument. Früher Schnitt ist billiger.

---

## 9. Offene Fragen

1. **Akronym-Schicksal:** Bleibt "AAMS" ein sinnvolles Akronym wenn "Specification" fällt? Optionen: "Autonomous Agent Management System", "Autonomous Agent Manifest Standard", oder AAMS als reiner Eigenname ohne Auflösung.

2. **Community-Signaling:** Wie kommuniziert man den Wechsel an Repos die AAMS bereits einsetzen (Mantis-Familie etc.)? Sind `.agent.json`-Dateien die v1 benutzen automatisch breaking?

3. **_spec vs. _contract Feld:** Wenn `_contract: "AAMS/2.0"` kommt — soll `_spec` als deprecated field erhalten bleiben für Rückwärtskompatibilität?

4. **Protocol vs. Contract:** Beide Begriffe wurden vorgeschlagen. "Protocol" betont den Ablauf (wie in TCP/IP). "Contract" betont die Verbindlichkeit zwischen zwei Parteien. Für AAMS — wo Agent und Repository beide Vertragsparteien sind — ist **Contract** präziser.

---

## 10. Empfehlung

**Option B annehmen. AAMS neu definieren als Verhaltensvertrag.**

Die Analyse zeigt eindeutig: `.agent.json` ist heute *de facto* bereits ein Verhaltensvertrag. Die Umbenennung ist keine inhaltliche Änderung — sie ist die Korrektur einer unehrlichen Selbstbeschreibung.

Das WORKSPACE-Problem ist kein isoliertes Architekturproblem. Es ist das Symptom eines grundlegenden konzeptuellen Problems: AAMS wurde als Spec designed, muss aber als Contract gedacht werden. Die Lösung für WORKSPACE (Discovery-Logik, Conflict-Check) ist nur möglich wenn AAMS sich erlaubt, Verhalten zu definieren.

**Sofort-Maßnahmen:**
1. Issue im AAMS-Repo erstellen: "Redefine AAMS as Agent-Contract (not Specification)"
2. `_spec` → `_contract` in `.agent.json` vorbereiten
3. WORKSPACE-Discovery als ersten Contract-Verhaltensbaustein spezifizieren
4. AAMS/2.0 Roadmap starten mit Contract-Modell als Grundlage

---

## Key Findings

- `.agent.json` enthält mehrheitlich **Verhaltensvorschriften**, nicht Strukturdefinitionen — das ist per Definition kein Spec
- Das Wort "Manifest" im Namen widerspricht bereits dem Wort "Specification"
- `agent_contract` als Schlüssel existiert bereits — der Contract ist da, er heißt nur außen noch nicht so
- Das WORKSPACE-Problem ist direkte Evidenz: User brauchen Protokoll-Verhalten, nicht Schema-Validierung
- Option B (Agent-Contract) ist die einzige Option die kohärent, ehrlich und praktisch umsetzbar ist
- Der Wechsel ist konzeptuell, nicht technisch — `.agent.json` bleibt das Artefakt, nur die Selbstdefinition ändert sich

---

## Next Steps

- [ ] GitHub Issue: "Strategic Reorientation — AAMS as Agent-Contract" erstellen
- [ ] `.agent.json` Refactoring: `_spec` → `_contract`, Version → `AAMS/2.0`
- [ ] WORKSPACE-Proposal aus Field Report als ersten Contract-Verhaltensbaustein integrieren
- [ ] `reference/SPEC.md` → Umbenennung / Neustrukturierung planen
- [ ] README + AGENTS.md: Außendarstellung "Verhaltensvertrag" schreiben
- [ ] Workpaper schließen → MEMORY ingesten

---

*Workpaper erstellt: 2026-04-10 — harte strategische Analyse, kein Konsens-Dokument*
