# WP-2026-09-22-SPEC-TEAM-agent-json-team-fähigkeit-analyse

**Status:** open
**Datum:** 2026-09-22
**TOPIC/SUBTOPIC:** SPEC/TEAM
**Session-Ziel:** Analyse: Wie wird die AAMS-Spezifikation (`.agent.json` + `reference/AGENT.json` + `AGENT_SCHEMA.json`) **team-fähig**? User-Idee: „Fast alles bleibt so. Nur bei Workpapers, MEMORY/LTM und Diary kommt die Komponente dazu, dass ein **anderer Mensch/Agent daran arbeitet oder weiterarbeitet**." — inkl. wer, womit (Tool + Modell), was er arbeitet. Whitepaper: **bleibt author-frei** (Wahrheit-in-Zeit).

**Bezug:**
- Wir arbeiten hier an der **Spezifikation AAMS selbst** (`https://github.com/ogerly/AAMS`) — alle holen sich `.agent.json` via `curl -sO https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json` → **die Spezifikation ist der Distributionskanal** für alle Teams.
- WP-015 (Kreis-Modell): Focalizer delegiert an „jemand aus dem Netzwerk" → braucht Daten über Wer-kann-was-mit-was.
- WP-012/WP-013 (Hermes/JEV): „wer + womit" ist genau der STATE, den Decision-Layer/Kopplung brauchen.
- Prinzipien: Manifest-Prinzip D9 (descriptive, nicht prescriptive), Spec-First (LTM #147).
- Evidenz-Quelle: `reference/AGENT.json` (lokales Original, `_contract: AAMS/2.3.1`) + `reference/AGENT_SCHEMA.json`.

---

## 1. User-Position (bindend für diese Analyse)

1. **Fast alles bleibt so** — keine Umstrukturierung von `WORKING/`, Lifecycle, Guard, Skills & Co.
2. **Zusatz-Komponente** in **Workpaper + MEMORY/LTM + Diary**: wer (Mensch/Agent) arbeitet daran / wer arbeitet **weiter** daran — und **womit** (Tool + Modell).
3. **Zwei Wege** (User):
   - **Weg 1:** `reference/AGENT.json` anpassen → ab dann unterstützt die AAMS-Spezifikation Teamarbeit.
   - **Weg 2:** (implizit) nur Konvention im Workspace, ohne Spec-Änderung.
4. **Whitepaper braucht keine Änderung** — Wahrheit-in-Zeit braucht keine „wer/womit"-Infos. (→ D2)
5. **Modell-Info ist wichtig:** Teammitglied mit starkem Frontier-Modell vs. jemand mit lokalem `qwen/qwen3.8-27b` — das sind **wichtige Infos** (Review-Tiefe, Delegation, Handover-Vertrauen).

### 1.1 User-Antworten auf §8-Fragen (2026-09-22, bindend)

| # | Frage | Antwort |
|---|---|---|
| 1 | Roster statisch/dynamisch? | **Dynamisch.** |
| 2 | Modell-Naming? | **Volle Modell-ID + optionales `capability`-Tag** (local/frontier) |
| 3 | Guard-Extension? | **Ja: Authorship vor Write.** |
| 4 | TEAM.md? | **Ja — aber: „Wir müssen eine Spezifikation bleiben."** TEAM.md muss **von Anfang an da sein, auch ohne Team.** Es darf **keinen Unterschied** geben, ob im Team gearbeitet wird oder nicht. Der AAMS-Check (User oder Hermes-Wächter) muss den Worker **ohne menschliche Antwort** bestimmen: Name unbekannt ist OK, aber **LLM + local/frontier sind erkennbar**. Immer **dasselbe Schema** — ohne sich auf eine richtige Antwort eines Menschen zu verlassen (Erkennung über den Tech-Stack). |
| 5 | Pilot in diesem Repo? | **Nein, erstmal nicht.** Später von GitHub als Upgrade holen und zusätzlich durchchecken. |

**Daraus folgt das Struktur-Invarianz-Prinzip (neu):** *Team oder Solo = dieselbe Struktur, null Unterschied.* — Kein Zweig im Schema, keine Bedingung „wenn Team", keine manuelle Frage an den Menschen.

---

## 2. Ist-Zustand (Evidenz aus `reference/AGENT.json`, `AGENT_SCHEMA.json`, `.agent.json`)

### 2.1 Was bereits multi-agent-fähig ist (gut — bleibt)

| Stelle | Was schon da ist | Bewertung |
|---|---|---|
| `session.workpaper_path` | `{date}-{agent}-session.md` | **Agent-Identität steht schon im Workpaper-Namen** — Multi-Agent ist implizit angenommen |
| `workspace.workpaper_rules.naming_pattern` | `{date}-{agent}-{topic}.md` | dito |
| `identity` (name, version, type, author) | Beschreibung eines einzelnen Agenten | pro-Agent vorhanden, aber **ein Agent = eine Datei** — kein Roster für N |
| `runtime` (model, provider, local) | Modell-Kontext des einen Agenten | Vorlage für Roster-Einträge |
| `skills.capabilities` | pro-Agent-Kapazitäten | Vorlage für Roster-Feld „capability" |
| `security.behavioral_signals` | `trust_score`, `sessions_without_incident` **pro Agent** | **Team-adjazent schon vorhanden!** — Trust ist bereits pro-Agent gedacht |
| `metadata.team_size` | `3` (free-form) | Team-Bewusstsein vorhanden, aber **ungetypt, nicht nutzbare** Struktur |

### 2.2 Was fehlt (Gap für Teamarbeit)

| # | Gap | Konsequenz heute |
|---|---|---|
| G1 | **Kein Roster:** wer sind die Teammitglieder (Menschen + Agenten), mit welchem Tool, welchem Modell | Delegation/Review kann nur mündlich oder per Chat-Zusatz; Focalizer (WP-015) hat keine Datenbasis |
| G2 | **Keine Authorship an Artefakten:** Workpaper/LTM/Diary tragen nicht „wer + womit" | Arbeit von Worker A ist von Worker B nicht unterscheidbar, bis man fragt; Modell-Kontext geht verloren |
| G3 | **Keine Handover-/Weiterarbeits-Komponente:** „ein anderer arbeitet weiter daran" ist nirgends darstellbar (kein `continued_from`, kein Worker-Status) | Weiterarbeit beginnt ohne Provenienz; RFL kann nicht „von wem stammt diese Decision?" prüfen |
| G4 | **Kein Modell-Kontext für Review:** Frontier vs. lokal (qwen3.8-27b) ist in keinem Artefakt sichtbar | Review-Tiefe ist blind; exakt das Problem, das der User nennt |
| G5 | **Spec-Drift:** `reference/AGENT.json` = `AAMS/2.3.1`, Root-`.agent.json` = `AAMS/2.4.0` | Voll-Spec und Mini-Contract laufen auseinander — bei einem Team-Feature wäre das fatal |
| G6 | **Spec-Hygiene:** `reference/AGENT.json` hat **doppelten `skills`-Key** (top-level, Zeile 35 & 423) — JSON-Parser nehmen still das letzte, das erste wird überschrieben | Still-Override = latent fehlerhaft; vor jedem neuen Abschnitt bereinigen |
| G7 | **Schema-Lücke:** `AGENT_SCHEMA.json` kennt weder `team` noch `worker/roster/authorship` (nur `identity.author` + `identity.type`-Enum „worker") | Kein validierbares Ziel für ein Team-Feature |
| G8 | **Tag/Manifest-Drift:** Git-Tag `v2.5.0` **existiert bereits** (zeigt auf `6ed5003`, INDEX/Upgrade-Ära), aber das Manifest dort sagt `AAMS/2.4.0` | `v2.5.0` ist „verbraucht" (Fehl-Tag) → **nächstes Release = v2.6.0**; altes Tag nicht verschieben (Git-Safety) |
| G9 | **GitHub-Release-Status (2026-09-22, `github.com/ogerly/AAMS/releases`):** **Latest-Release = v2.3.2** („on_update migriert Konventionen"). `v2.4.0` + `v2.5.0` existieren **nur als lokale Tags, ohne GitHub-Release** | Team-Release = **erstes Release seit v2.3.2** → Beschreibung muss „seit v2.3.2 neu" abdecken (v2.4.0: Upgrade-Sicherheit/-Report/UPGRADE.md; v2.5.0: INDEX-Pflege/Max-5) + Team-Authorship |

---

## 3. Warum „wer + womit" in der Spec gehören muss (Argumente)

1. **Review-Tiefe (Capability-based Review):** Ein Workpaper, das von einem Frontier-Modell stammt, und eines von `qwen/qwen3.8-27b`, verdienen **unterschiedliche Review-Gewichtung**. Decisions aus der schwächeren Klasse bei komplexen Aufgaben = stärkere Prüfung. Ohne Modell-Info ist Review ein Blindflug. *(User-These, hier verallgemeinert.)*
2. **Delegation & Focalizer (WP-015):** „Die Rolle garantiert, dass etwas passiert — nicht, wer es tut." — aber **wer es tun KANN**, muss bekannt sein. Ein Roster mit Tool/Modell/Kapazität ist genau die Datenbasis, die der Focalizer für „Aufgabe C → jemand aus dem Netzwerk" braucht.
3. **Handover-Vertrauen:** Wer weiterarbeitet, muss wissen, **welche Leistungsklasse das Artefakt erzeugt hat** — was darf ich übernehmen, was muss ich verifizieren? (z. B. Halluzinations-Muster, Context-Limits des erzeugenden Modells).
4. **RFL-Triage:** Eine Consistency-Flag gegen eine fremde Decision wird leichter aufgelöst („confirmed / revised / intentional"), wenn klar ist, wer sie mit welcher Kapazität getroffen hat.
5. **Trust & Audit:** `security.behavioral_signals` denkt **schon** pro-Agent (trust_score). Authorship verbindet Artefakte mit genau diesen Signalen — das fehlt heute nur die Klammer.
6. **Reproduzierbarkeit/Debugging:** „Dieses Workpaper stammt aus Tool X / Modell Y" → bei Auffälligkeiten ist dieCapability-Klasse bekannt, nicht nur das Ergebnis.

---

## 4. Die zwei Wege

### Weg 1 — Spec-Erweiterung (Empfehlung)

Neue **optionale `team`-Sektion** in `.agent.json` + `reference/AGENT.json`, Schema in `AGENT_SCHEMA.json` — alle Felder `descriptive_only` (D9), nichts required, bestehende Repos bleiben 1:1 gültig:

```json
"team": {
  "_doc": "Optionale Team-/Kollaborations-Metadaten. Beschreibend (D9), nichts davon ist required. Weißt du nicht, was ein Feld heißt: lass es weg.",
  "enabled": true,
  "roster": [
    { "id": "tulex", "type": "human", "tool": "opencode", "model": "qwen/qwen3.8-27b", "capability": "local", "note": "Maintainer" },
    { "id": "reviewer-1", "type": "agent", "tool": "claude-code", "model": "claude-opus-4", "capability": "frontier", "note": "Review" }
  ],
  "_roster_doc": "type: human|agent · tool: Arbeitsmittel · model: Leistungsklassen-Kontext (Review-Tiefe, Delegation) · capability: optional (local|frontier|…)",
  "workpaper_authorship": {
    "fields": ["worker", "tool", "model"],
    "location": "Workpaper-Header",
    "_doc": "Jedes Workpaper trägt: wer hat es angefasst, womit. Weiterarbeit = neuer Eintrag + continued_from."
  },
  "handover": {
    "continued_from": "Workpaper-Header-Feld: ID des Vorgänger-Workpapers",
    "waiting": "observe/-Status = wartet auf (menschliche/agentische) Weiterarbeit",
    "single_writer": "pro Workpaper ein aktiver Writer; Übergabe = Statuswechsel, nie paralleles Schreiben"
  },
  "diary_format": "YYYY-MM-DD | BY: {worker} ({tool}/{model}) | WP: {workpaper} | WH: {whitepaper} | {other}",
  "ltm_columns": "# | Datum | Typ | BY | Datei | Inhalt",
  "whitepaper_authorship": "excluded — Whitepaper bleiben author-frei (Wahrheit-in-Zeit)",
  "status": "descriptive_only"
}
```

**Begleitende Schritte:**
1. `AGENT_SCHEMA.json`: `team`-Property ergänzen (alle Felder optional).
2. `reference/AGENT.json`: `team`-Sektion + **G5/G6 bereinigen** (Version auf 2.5.0, `skills`-Duplikat entfernen).
3. `.agent.json`: `team`-Sektion + `_contract: AAMS/2.5.0` + `_version_date`.
4. `CHANGELOG.md`: 2.5.0 — „Team-Authorship (optional)": Roster, Workpaper-Header (worker/tool/model), `continued_from`, Diary/LTM `BY`-Spalte; Whitepaper author-frei (Decision).
5. `on_update`: keine neuen Ordner (nur Felder/Formate) — Migration = null, alte Repos bleiben gültig.
6. Pilot in diesem Repo: WP-Header + `BY`-Spalten ab sofort nutzen.

**Warum der Spec-Kanal:** Alle holen sich `.agent.json` per `curl`. Ein Feld, das nur hier als Konvention lebt (Weg 2), erreichen **andere Teams nie** — und genau für Teams ist es gedacht.

### Weg 2 — Nur Konvention (ohne Spec-Änderung)

- `worker/tool/model`-Header, `BY`-Spalten, `continued_from` **nur in diesem Repo** vereinbaren.
- **Pro:** null Spec-Churn, sofort.
- **Cona:** nicht discoverable, kein Schema, kein Validierungsziel, jedes Team erfindet es neu, Tools (Guard, Lint) können es nicht umsetzen.

### Empfehlung

**Weg 1 mit minimaler Fläche:** eine optionale `team`-Sektion, nichts required, D9-konform. Die Spec ist der Distributionskanal — ein Team-Feature muss dort beschrieben sein, damit es ein Team-Feature für **alle** Teams ist. Gleichzeitig: die Fläche bleibt klein, weil **nur Autorship + Handover** dazukommen und nichts umstrukturiert wird (User-Prinzip „fast alles bleibt so").

### 4.1 Design v2 (finalisiert durch die 5 User-Antworten, §1.1)

**Änderungen gegenüber dem Entwurf in §4:** Roster wandert aus der Spec-Datei in den Workspace (dynamisch), Authorship wird **passiv detektiert** (nie an den Menschen gefragt), Guard-Check `authorship_present` kommt hinzu, Pilot entfällt (Upgrade-Pfad).

```json
"team": {
  "_doc": "Optionale Team-/Kollaborations-Metadaten. Beschreibend (D9), nichts required. TEAM ODER SOLO: GLEICHE STRUKTUR, NULL UNTERSCHIED.",

  "roster": {
    "_doc": "Dynamisches Roster im Workspace — NICHT statisch in dieser Datei. Bootstrap erstellt es idempotent (create_if_missing), es existiert ab Tag 1, auch für Solo.",
    "path": "./WORKING/TEAM.md",
    "bootstrap": "create_if_missing",
    "entry_fields": [
      "name (optional — nur wenn bekannt, sonst '—')",
      "type: human|agent",
      "tool: Arbeitsmittel (z. B. opencode, claude-code, cursor)",
      "model: volle Modell-ID (z. B. qwen/qwen3.8-27b, claude-opus-4)",
      "capability: local|frontier (optional)",
      "note (optional)"
    ]
  },

  "authorship": {
    "workpaper_header": "BY: {name|—} / {tool} / {model} / {capability}",
    "example": "BY: — / opencode / qwen/qwen3.8-27b / local",
    "diary_format": "YYYY-MM-DD | BY: {tool}/{model}/{capability} | WP: {workpaper} | WH: {whitepaper} | {other}",
    "ltm_columns": "# | Datum | Typ | BY | Datei | Inhalt",
    "whitepaper_authorship": "excluded — Whitepaper bleiben author-frei (Wahrheit-in-Zeit, D2)"
  },

  "authorship_detection": {
    "_doc": "Authorship wird PASSIV ERKANNT, niemals an den Menschen gefragt. Der AAMS-Check (User-Aufruf oder Hermes-Wächter) liefert IMMER dasselbe Schema — ohne sich auf eine richtige Antwort eines Menschen zu verlassen.",
    "tool": "via bestehende tool_detection (opencode, cursor, claude-code, copilot, windsurf, aider, lm-studio, ollama, llama.cpp, openai-proxy)",
    "model": "via Runtime-Konfiguration (z. B. opencode.json provider/model, runtime.model)",
    "capability": "via Endpoint/Provider: localhost/LAN/lokale Runtime (ollama, lm-studio, llamacpp, lokales Gateway) → 'local'; Cloud-Provider (openai, anthropic, alibaba, openrouter, …) → 'frontier'",
    "name": "nur wenn bekannt (z. B. Git-User, explizit gesetzt), sonst '—' — NIE Pflicht",
    "_example_this_repo": "opencode.json → Provider 'mantis' (MANTIS LLM Gateway, 172.19.224.1:9876) + Modell 'qwen/qwen3.8-27b' + Label 'LM Studio … (lokal)' → Erkennung: BY: — / opencode / qwen/qwen3.8-27b / local"
  },

  "handover": {
    "continued_from": "Workpaper-Header-Feld: ID des Vorgänger-Workpapers (weiterarbeiten an fremdem WP)",
    "waiting": "observe/-Status = wartet auf Weiterarbeit (menschlich oder agentisch)",
    "single_writer": "pro Workpaper ein aktiver Writer; Übergabe = Statuswechsel, nie paralleles Schreiben"
  },

  "guard_check": {
    "authorship_present": {
      "_doc": "Optionaler Guard-Check VOR Write/Edit: das aktive Workpaper trägt einen BY:-Header (via authorship_detection befüllbar).",
      "order": "manifest_read → workpaper_open → authorship_present → tools_gated",
      "error_format": "GUARD-VERSTOSS: Kein Authorship-Header (BY:) im aktiven Workpaper. Erkennung: tool_detection + Runtime-Konfiguration — keine Eingabe nötig."
    },
    "status": "descriptive_only + optionale Tool-Enforcement (analog bestehender Guard-Checks)"
  },

  "status": "descriptive_only"
}
```

**Warum Detection statt Frage (Antwort 4, vertieft):**
1. **AAMS bleibt Spezifikation:** Ein Schema, das eine menschliche Antwort voraussetzt, ist eine Umfrage — keine Spezifikation. Erkennbare Fakten (Tool, Modell, local/frontier) sind Spezifikations-Material; der Name ist optionaler Zusatz.
2. **Invarianz:** Team oder Solo, erkannt oder genannt — das BY-Schema ist identisch. Es gibt keinen „Team-Zweig", keine Bedingung, kein manuelles Ankreuzen.
3. **Wächter-tauglich:** Der Hermes-Wächter (oder jeder Guard) kann Authorship **ohne Interaktion** bestimmen und prüfen — Fail-open, kein Block auf menschliche Eingabe.
4. **Tech-Stack als Quelle:** Genau das, was Antwort 4 sagt: „durch die Änderung des Techstacks" ist die Autorship erkennbar — der Stack (Provider, Modell, Endpoint) trägt die Information bereits; AAMS liest sie nur ab.

---

## 5. Was NICHT geändert wird (User-Prinzip „fast alles so")

| Baustein | Status |
|---|---|
| **Whitepaper** | **Keine Authorship, keine Änderung** — Wahrheit-in-Zeit bleibt worker-neutral (User-Decision, bindend) |
| `WORKING/`-Struktur, Lifecycle, Max-5, INDEX | unverändert |
| Guard, Skills, Tool-Detection, File-Safety, Security | unverändert (Team-Felder berühren sie nicht) |
| **Diary-Prinzip** (pointer-only) | bleibt — `BY`-Spalte ist ein **Pointer** (wer), kein Content-Duplikat |
| **LTM-Prinzip** (Audit-Log) | bleibt — `BY`-Spalte ist **Provenienz**, kein Content |
| Secrets-Policy | bleibt — Roster-Modelle sind keine Secrets; `apiKey`-Werte gehören **niemals** in Roster/Workpaper |
| **Einzige Struktur-Neuzugabe** | `WORKING/TEAM.md` — von Bootstrap idempotent erstellt (ab Tag 1, auch solo), **kein** Zweig Team-vs-Solo im Schema |

---

## 6. decisions

- **D1 (BESTÄTIGT 2026-09-22):** **Weg 1** — optionale `team`-Sektion (Roster + Authorship + Handover + `BY`-Formate) in `.agent.json` + `reference/AGENT.json` + `AGENT_SCHEMA.json`; Release **AAMS/2.6.0** (minor, additive, backward-kompatibel; v2.5.0-Tag bereits verbraucht — G8).
- **D2 (User, bindend):** **Whitepaper bleiben author-frei.** Wahrheit-in-Zeit trägt keine „wer/womit"-Infos. (Ironie-Freund: diese Decision selbst wird — als Spec-Decision — in ein Whitepaper promoted, ohne dort als „Author" zu erscheinen.)
- **D3 (finalisiert §1.1):** Authorship = **name (optional, sonst `—`) + tool + volle Modell-ID + capability-Tag (local|frontier, optional)** (Workpaper-Header `BY:`) · Handover = `continued_from` + `observe/`-Status · **Single-Writer** pro Workpaper (aus WP-012 Hermes-Local übernommen).
- **D4:** Sämtliche Team-Felder sind `descriptive_only` (D9) — kein Required-Feld, keine Enforcement, bestehende Repos 1:1 gültig.
- **D5 (Max-5):** WP-008 (2026-07-08, „Issue-Triage" pending, 2,5 Monate alt) → `observe/`, damit dieses WP-016 geöffnet werden kann.
- **D6 (Hygiene, folgt aus G5/G6):** Vor dem 2.6.0-Release: `reference/AGENT.json` auf 2.6.0 synchronisieren + `skills`-Duplikat entfernen.
- **D7 (neu, Antwort 1):** Roster ist **dynamisch** → `WORKING/TEAM.md` (Workspace, nicht Spec-Datei); Bootstrap erstellt es idempotent **ab Tag 1 — auch ohne Team**. Struktur-Invarianz: Team oder Solo = null Unterschied im Schema.
- **D8 (neu, Antwort 4):** **Detection-basierte Authorship** — Tool/Modell/capability werden passiv aus dem Tech-Stack erkannt (tool_detection + Runtime-Konfiguration + Endpoint/Provider); Name nur wenn bekannt, sonst `—`. Der AAMS-Check liefert **immer dasselles Schema ohne menschliche Antwort** — „AAMS bleibt Spezifikation".
- **D9-WP (neu, Antwort 3):** Guard-Extension **`authorship_present`** — optionaler Check vor Write/Edit: aktives Workpaper trägt `BY:`-Header (via D8 befüllbar). Reihenfolge: `manifest_read → workpaper_open → authorship_present → tools_gated`. Status: `descriptive_only` + optionale Enforcement (analog WH-009). *(Bewusst „D9-WP" — WP-lokal; das globale D9 = Manifest-Prinzip.)*
- **D10 (neu, Antwort 5):** **Kein Pilot in diesem Repo (erstmal).** Adoption später über den **standardisierten Upgrade-Pfad** (`curl .agent.json` → `on_update`) — testet dabei zugleich das eigene Upgrade-System (WH-011).
- **D11 (neu, User 2026-09-22):** **Neue Release anlegen + beschreiben:** Git-Tag **`v2.6.0`** + **GitHub-Release** mit Beschreibung (Entwurf in §10). Push/Release = **User-Entscheidung** (Agent pusht nicht ohne Auftrag). Altes `v2.5.0`-Tag (G8) bleibt unangetastet. Beschreibung deckt **alles seit v2.3.2** ab (G9: Latest-GitHub-Release = v2.3.2, v2.4.0/v2.5.0 = lokal getaggt, nie released). Stil: wie bestehende Releases (Titel `v2.6.0 — …`, `## Added/Changed/Decisions/Upgrade`, Get-Started-Block).
- **D12 (User 2026-09-23):** **GitHub-Release-Reihenfolge komplettieren:** erst **v2.4.0** + **v2.5.0** nachträglich als GitHub-Releases (Tags existieren bereits, Releases fehlten — G9), dann **v2.6.0 als Latest**. Keine Versionslücke in der öffentlichen Chronik. Notizen-Entwürfe: §12.

**Decision-Promotion (vor Close):** D2 + D3 → Whitepaper (Kandidat: **WH-012 Team-Authorship** oder WH-001-Expansion) — enthält das `team`-Sektion-Design als stabile Wahrheit.

---

## 7. RFL

- Stage 1 (SPEC-Scan closed/): WP-2026-09-16 (Hermes-Sidecar) — Single-Writer-Prinzip dort **bereits** etabliert → wird hier in D3 übernommen, kein Konflikt.
- Stage 1 (GOV-Scan): WP-015 (Kreis-Modell) — **komplementär**: Roster = Datenbasis des Focalizer; keine Gegen-Decision.
- **Kein ⚠ RFL Consistency Flag.**

---

## 8. Offene Fragen — ✅ ALLE BEANTWORTET (2026-09-22, siehe §1.1)

1. Roster → **dynamisch** (D7)
2. Modell → **volle ID + optionales capability-Tag** (D3)
3. Guard → **ja, Authorship vor Write** (D9-WP)
4. TEAM.md → **ja, ab Tag 1, Team/Solo-invariant, Detection statt Frage** (D7/D8)
5. Pilot → **nein, erstmal nicht — später via GitHub-Upgrade** (D10)

---

## 9. file_protocol

| Aktion | Datei |
|---|---|
| create (open) | `WORKING/WORKPAPER/WP-2026-09-22-SPEC-TEAM-agent-json-team-fähigkeit-analyse.md` |
| move (Max-5, D5) | `WORKING/WORKPAPER/WP-2026-07-08-session-start-issue-check.md` (WP-008) → `WORKING/WORKPAPER/observe/` |
| read | `reference/AGENT.json` (2.3.1, `{agent}`-Naming, `behavioral_signals`, `team_size`), `reference/AGENT_SCHEMA.json` (kein team/worker), `.agent.json` (2.4.0), WP-012/013/015 (Kontext) |
| pending (nach D1) | `.agent.json` + `reference/AGENT.json` + `reference/AGENT_SCHEMA.json` + `CHANGELOG.md` + `bootstrap_rules` (TEAM.md) + optional `wiki_lint.py` L8 |
| update (v2) | Dieses WP: §1.1 (5 Antworten), §4.1 (Design v2 final), D1 bestätigt, D3 finalisiert, D7–D10 neu, §8 resolved, §5 TEAM.md-Zeile |
| update (v3) | Dieses WP: G8/G9 (Tag-Drift + GitHub-Release-Status: Latest = v2.3.2, v2.4.0/v2.5.0 nur lokal), D1/D6/D11 → v2.6.0, §10 Release-Plan + Beschreibung-Entwurf + offene Entscheidungen, §11 next_steps aktualisiert |
| update (v4, 2026-09-23) | Dieses WP: D12 (Release-Reihenfolge komplettieren, User-Entscheidung), §10.4-1 resolved, §10.5 retroaktive Release-Notizen v2.4.0/v2.5.0, §11 next_steps aktualisiert |
| update (v4) | `.agent.json` — `_contract` AAMS/2.6.0 + `_version_date`, `team`-Sektion, `bootstrap_rules.team_file`, Guard `authorship_present` + `no_authorship`-Error, `on_update` TEAM.md-MIGRATE |
| update (v4) | `reference/AGENT.json` — AAMS/2.6.0, `skills`-Duplikat vereint (G6), `team`-Sektion, Guard `authorship_present`, `_deviations` → `convention_path` (Schema-Konformität) |
| update (v4) | `reference/AGENT_SCHEMA.json` — Version/$id 2.6.0, `skills`-Duplikat vereint, `team`-Property (optional), Guard `authorship_present` + `no_authorship`, `bootstrap_rules.team_file` |
| update (v4) | `reference/SPEC.md` — `_deviations`-Beispiel → `convention_path` |
| update (v4) | `CHANGELOG.md` — 2.6.0 + retroaktive 2.5.0 + 2.4.0-Einträge (fehlten komplett) |
| update (v4) | `README.md`, `READ-AGENT.md`, `docs/index.html` — Version auf AAMS/2.6.0 synchronisiert |
| validate (v4) | `python3`: JSON-Parser (alle 3 Spec-Dateien, keine doppelten Keys) + `jsonschema` Draft 2020-12: **AGENT.json erfüllt Schema 2.6.0 ✅** (vorher: 4 Fehler durch `spec_path`-Drift, behoben) |

---

## 10. Release v2.6.0 — anlegen & beschreiben (D11)

### 10.1 Faktenbasis (GitHub, 2026-09-22)

| Release (GitHub) | Titel | Status |
|---|---|---|
| **v2.3.2** | „on_update migriert Konventionen" | **Latest** (08.07.04:18) |
| v2.3.1 | „Update-Detection repariert" | released |
| v2.3.0 | „Skill-Baukasten, Passive Tool Detection, Lokale LLMs" | released |
| v1.3.0 / v1.2.0 / v1.0.1 / v1.0.0 | (ältere Releases) | released |
| **v2.4.0** | — | **nur lokales Tag, KEIN GitHub-Release** |
| **v2.5.0** | — | **nur lokales Tag (alter Commit), KEIN GitHub-Release** |

**Konsequenz:** v2.6.0 ist das **erste Release seit v2.3.2** → die Beschreibung muss „alles seit v2.3.2 neu" abdecken. Stil-Vorbilder: v2.3.2/v2.3.1 (`## Fixed/Changed`), v1.2.0/v1.3.0 (`## What's New` + „Closes: #…"), v1.0.0 (Get-Started-Block). Jedes Release hat „Assets 2" (Source-Zip/Tarball — automatisch).

### 10.2 Release-Plan (Schritte)

| Schritt | Aktion | Wer |
|---|---|---|
| 1 | 2.6.0-Implementierung (Spec-Dateien + Schema + CHANGELOG + Bootstrap `TEAM.md`) — §11.3/4 | Agent (auf Auftrag) |
| 2 | Commit auf `main` | Agent (mit User-OK) |
| 3 | `git tag v2.6.0` | Agent (mit User-OK) |
| 4 | `git push origin main && git push origin v2.6.0` | **User-Entscheidung** (Agent pusht nicht ohne Auftrag) |
| 5 | **GitHub-Release anlegen:** Titel + Beschreibung (§10.3) + Source-Assets (Web-UI oder `gh release create`) | **User** (oder Agent mit Token + Auftrag) |
| 6 | (Optional) retroaktive Release-Seiten für v2.4.0/v2.5.0 — nur wenn gewünscht | User-Entscheidung |
| 7 | Später: Adoption in diesem Repo per Upgrade-Pfad (D10) + WH-011-Test | Agent |

### 10.3 Release-Beschreibung (Entwurf, final nach Schritt 1)

**Titel:** `v2.6.0 — Team-Authorship (optional)`

```markdown
**One file. Every repo. Now with team memory: wer + womit — ohne Frage an den Menschen.**

## Added (seit v2.3.2)

### Team-Authorship (optional, backward-kompatibel)
- **`team`-Sektion** in `.agent.json`, `reference/AGENT.json`, `AGENT_SCHEMA.json`
- **Roster:** `WORKING/TEAM.md` — dynamisch, vom Bootstrap idempotent erstellt (ab Tag 1 — Team oder Solo, gleiche Struktur, null Unterschied)
- **Authorship:** `BY: {name|—} / {tool} / {model} / {capability}` in Workpapers, Diary und LTM-Index
- **Detection:** Authorship wird **passiv aus dem Tech-Stack erkannt** (tool_detection + Runtime-Konfiguration + Endpoint → `local`/`frontier`) — niemals an den Menschen gefragt, niemals Pflicht. Beispiel: `BY: — / opencode / qwen/qwen3.8-27b / local`
- **Handover:** `continued_from` + `observe/`-Status + Single-Writer pro Workpaper
- **Guard:** optionaler Check `authorship_present` vor Write/Edit (Reihenfolge: `manifest_read → workpaper_open → authorship_present → tools_gated`)

### Seit v2.3.2 (bisher nur lokale Tags, ohne Release)
- **v2.4.0:** Upgrade-Sicherheit (Backup + Merge statt blindem Überschreiben), anonymisierter Upgrade-Report als GitHub-Issue, UPGRADE.md
- **v2.5.0:** INDEX.md-Pflege (Whitepaper + Workpaper), Max-5-Regel, on_update um INDEX-Schritte erweitert

## Changed
- `reference/AGENT.json` synchronisiert (war 2.3.1, jetzt 2.6.0), `skills`-Duplikat entfernt (Hygiene)
- **Kein** Verhaltenswechsel für bestehende Repos — sämtliche Team-Felder optional

## Decisions
- **Whitepaper bleiben author-frei** (Wahrheit-in-Zeit)
- **Struktur-Invarianz:** Team oder Solo = gleiche Struktur, null Unterschied
- **Detection statt Frage:** AAMS bleibt Spezifikation — erkennbare Fakten (Tool, Modell, local/frontier) statt menschlicher Eingabe

## Upgrade
curl -sO https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json
→ `on_update` läuft automatisch. Neuer Pfad: `WORKING/TEAM.md` (idempotent angelegt). Nichts wird überschrieben.

## Breaking changes
Keine.
```

### 10.4 Release-Entscheidungen (User)

1. ✅ **ENTSCHIEDEN (User 2026-09-23):** **Reihenfolge komplettieren** — zuerst retroaktive GitHub-Releases **v2.4.0** + **v2.5.0** (Tags existieren bereits, Releases fehlen — G9), dann **v2.6.0 als Latest**. → D12
2. Push + Release: selbst, oder Agent mit Token + explizitem Auftrag?
3. Assets: nur Source (wie bisher „Assets 2"), oder zusätzlich ein `aams-2.6.0.zip`-Bundle (`.agent.json` + `AGENTS.md` + `READ-AGENT.md`) für 3-Command-Installation?

### 10.5 Retroaktive Release-Notizen (Entwurf für D12 — basierend auf dem tatsächlichen Commit-Content, 2026-09-23 per `git log/show` geprüft)

> Tags existieren bereits: `v2.4.0` → Commit `5778195`, `v2.5.0` → Commit `6ed5003`. Es fehlt nur die GitHub-Release-Seite.

**v2.4.0 — Titel:** `v2.4.0 — Upgrade-Sicherheit & Upgrade-Report`

```markdown
**Dein Repo wird beim AAMS-Upgrade nicht mehr blind überschrieben — und du siehst, was passiert ist.**

## Added
- **Upgrade-Sicherheit** — Backup (`.agent.json.bak`) + Merge statt blindem Überschreiben
- **Anonymisierter Upgrade-Report** — als GitHub-Issue an `ogerly/AAMS` (nur wenn GITHUB_TOKEN vorhanden; keine Repo-Namen, keine Secrets, keine Personaldaten)
- **UPGRADE.md** — Anleitung für Consumer-Repos (automatischer Upgrade-Befehl + manuelle Schritte)

## Fixed
- **Versioning** — „niemals runter in der Version": CHANGELOG-Konsistenz + `_contract` trägt die reale Version (Basis für Update-Detection)

## Upgrade
curl -sO https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json
→ `on_update` läuft automatisch: Backup + Merge. Nichts wird überschrieben.
```

**v2.5.0 — Titel:** `v2.5.0 — INDEX-Pflege & Max-5-Regel`

```markdown
**Deine Whitepaper- und Workpaper-Sammlung bleibt automatisch nachvollziehbar.**

## Added
- **INDEX.md-Pflege** — `WHITEPAPER/INDEX.md` + `WORKPAPER/INDEX.md`: erstellen wenn fehlend, bestehende Papers indexieren, bei neuem Paper aktualisieren
- **Max-5-Regel** — mehr als 5 offene Workpapers → Warnung + Vorschlag zum Schließen
- **WH-011-upgrade-system.md** — Whitepaper zum Upgrade-System

## Changed
- **`on_update`** — um 4 INDEX-Schritte + Max-5-Prüfung erweitert
```

---

## 11. next_steps

1. ✅ **Erledigt:** D1 bestätigt + §8-Fragen beantwortet (2026-09-22).
2. ✅ **Erledigt:** Design v2 finalisiert (§4.1) — Detection-basiert, invariant, Guard-Check.
3. ✅ **Erledigt (2026-09-23):** **Spec-Implementierung** — `.agent.json` + `reference/AGENT.json` + `AGENT_SCHEMA.json` (alle AAMS/2.6.0, `team`-Sektion/-Property, G5/G6 bereinigt, Guard `authorship_present`, `bootstrap_rules.team_file`, `on_update` TEAM.md-Migration) + `CHANGELOG.md` (2.6.0 + retro 2.5.0/2.4.0) + README/READ-AGENT/docs/index.html synchron. **Validiert: AGENT.json erfüllt Schema 2.6.0 ✅**
4. ⏳ **Release-Reihenfolge (D12):** Commit auf `main` → `git tag v2.6.0` → Push → GitHub-Releases in Reihenfolge: **v2.4.0** (Notiz §10.5) → **v2.5.0** (Notiz §10.5) → **v2.6.0** (Notiz §10.3) als **Latest**. Push/Release = **User-Entscheidung** (§10.4-2/3 noch offen).
5. **Später (D10):** Adoption in diesem Repo über den **standardisierten Upgrade-Pfad** (`curl .agent.json` → `on_update` → legt `./WORKING/TEAM.md` an) + WH-011-Test (Upgrade-System wird dabei mitgetestet).
6. Optional: `WORKING/TOOLS/wiki_lint.py` um L8 „Team-Authorship" (prüft `BY`/Header-Konsistenz, optional — nach Adoption).
7. Close: D2/D3/D7/D8 promote → **WH-012 Team-Authorship** (stabile Wahrheit inkl. Invarianz-Prinzip + Detection-Modell), LTM-Ingest, `docs/aams-arbeitsgrundstruktur-argumente.md` um „Team-Authorship" ergänzen.
