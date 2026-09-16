# WP-2026-09-16-MKT-DOC-readme-website-analyse

**Status:** closed (2026-09-16 — umgesetzt, ingested als LTM #141)
**Datum:** 2026-09-16
**TOPIC/SUBTOPIC:** MKT/DOC
**Session-Ziel:** Ist-Zustand von README und Webseite analysieren, gewünschten Soll-Zustand definieren, Gaps mit Maßnahmen priorisieren. Noch keine Umsetzung — nur Analyse + Decision-Vorbereitung.

> ⚠ **Max-5-Regel verletzt:** Mit diesem Workpaper sind **6 Workpapers offen** (WP-004, WP-007, WP-008, skill-opencode-agent.md, WP-2026-09-16-SPEC-QUEST, dieses). Vorschlag: `skill-opencode-agent.md` (Schema-fremder Name, Thema ruht) nach `observe/` verschieben oder WP-004/WP-007 schließen. Entscheidung liegt beim User (s. §8, F5).

---

## 1. session_goal

User-Auftrag: „README und Webseite von AAMS müssen besser gestellt werden." Drei Entwurfsdateien liegen in `WORKING/WORKPAPER/` (`neue_WEBSEITE.md`, `neue_README.md`, `aams_landing_page.html`). Dieses Workpaper stellt den **Ist-Zustand** (alle 6 relevanten Dateien + Bilder + Prior-Work) dem **gewünschten Soll-Zustand** gegenüber und leitet priorisierte Maßnahmen ab. Umsetzung erst nach User-Decisions (§8).

## 2. repository_inventory (Ist-Dateien)

| # | Datei | Umfang | Stand | Rolle heute |
|---|---|---|---|---|
| I1 | `README.md` (Root, DE) | 326 Zeilen | ogerly-URLs ✅, Statusblock **veraltet** | Aktueller Einstieg: Agent-Block + Kochbuch-Narrativ + Tool-Mapping + Upgrade-Prompt |
| I2 | `README.en.md` / `README.zh.md` | 243 / 235 Zeilen | Sync-Status ungeprüft, Divergenz-Risiko | EN/ZH-Spiegel (Guideline: müssen synchron sein) |
| I3 | `docs/index.html` + `docs/en/` + `docs/zh/` | 1332 / 741 / 657 Zeilen | **DEVmatrose-URLs** ❌, Footer „Specification / 1.0" ❌ | Live-Webseite (self-contained CSS, Copy-Buttons ✅) |
| I4 | `WORKING/WORKPAPER/neue_README.md` | 156 Zeilen | Entwurf, **fehlerhaft** (s. F4) | README-Rewrite-Vorschlag (menschlich, „unsichtbare Ordnung") |
| I5 | `WORKING/WORKPAPER/neue_WEBSEITE.md` | 189 Zeilen | Analyse + kaputtes HTML-Gerüst + unbelegte Konsistenz-Behauptung | Webseiten-Analyse + Landing-Anspruch |
| I6 | `WORKING/WORKPAPER/aams_landing_page.html` | 737 Zeilen, Tailwind-CDN | Modernster Entwurf, ogerly ✅, **Naming falsch** (s. F5) | Landing-Kandidat (noch nicht nach `docs/` übernommen) |
| I7 | `docs/aams-structur.jpg` + `docs/aams-structur_mobil.jpg` | vorhanden | **nirgends eingebunden** | Erklärbilder (nur in I5 referenziert) |
| I8 | Prior-Work | — | aktiv | WH-006 + Guideline `readme-consistency.md` + closed `WP-2026-04-30-ARCH-README-consistency-check.md` + closed `2026-04-14-public-presence-relaunch.md` |

Datei-Hinweis: I4–I6 tragen **nicht** das Workpaper-Naming-Schema (`WP-{DATE}-{TOPIC}-{SUBTOPIC}-*.md`). Nach Abschluss dieser Aufgabe: umbenennen oder nach `closed/` archivieren, damit `INDEX.md` + RFL-Pattern-Matching funktionieren.

## 3. key_findings — Ist-Zustand (Befunde F1–F8)

- **F1 — Falscher Produktname in allen 3 Entwürfen:** I4-Z.46, I5-Z.39, I6-`<title>` sagen „Autonomous Agent **Mesh System**"; I6-Z.142 „AAMS **Specification Standard** v2.4.0". Offiziell seit RFCT (2026-04-29/30): **„AAMS — Agent Manifest"** (D9, WH-006, alle Whitepapers). Ein falscher Name auf Landing + README wäre ein 🔴-Verstoß gegen die eigene Consistency-Guideline.
- **F2 — Webseite zeigt auf toten Account:** I3 enthält **durchgehend `DEVmatrose/AAMS`** (Meta-Tag, curl-Befehle, Nav, Showcase, Footer — je Datei ~15 Stellen, DE+EN+ZH). Korrekt wäre `ogerly/AAMS` (I1 ist bereits korrekt). Jeder Copy-Button der Live-Seite installiert das Manifest aus dem **falschen Repo**. Kritischster Einzelfund.
- **F3 — Versionen veraltet:** I3-Footer „Autonomous Agent Manifest **Specification / 1.0**" (aktuell: Agent Manifest / **2.4.0**); I1-Statusblock „AAMS/**2.0**, WH-**010**, 52 closed, v**2.2.0**, LTM **136**" (aktuell: 2.4.0, WH-011, ~50+ closed, v2.4.0, LTM ~140). Exakt die Divergenz-Klasse, die WH-006 verbietet.
- **F4 — `neue_README.md` ist kein übernehmbarer Entwurf:** curl als `[url](url)` im Codeblock (Z.87, rendert kaputt), Lizenz-Link = Google-Suche statt `LICENSE` (Z.146), kein Agent-Block (I1-Z.5–14 fehlt ersatzlos — Agents fänden den Vertrag nicht), kein Statusblock, EN/ZH ignoriert, endet mit Rückfrage statt Decision. Gute Sprache („unsichtbare Ordnung", FAQ), aber technisch nicht mergbar.
- **F5 — `aams_landing_page.html` ist der beste Entwurf, aber mit 3 Hypotheken:** (a) Naming s. F1; (b) **externe CDN-Dependencies** (Tailwind, FontAwesome, Google Fonts) vs. I3-Philosophie (self-contained, zero-dependency — passt zum AAMS-Geist „keine Installation"); (c) I7-Bilder nicht eingebunden, keine EN/ZH-Variante, Zielort (`docs/` ersetzen vs. parallel) unentschieden.
- **F6 — `neue_WEBSEITE.md` widerspricht sich selbst:** Z.59/67 verlinken `DEVmatrose`, Z.178 behauptet „einheitlich ogerly"; Z.33–53 enthalten ein leeres HTML-Gerüst; die „100 % konsistent"-Behauptung (Z.129–187) ist gegen F1/F2/F3 **falsch**. Als Analyse-Basis unbrauchbar, als Anspruch („Vorher-Nachher", „Copy-Buttons", „interaktiver Baum") brauchbar.
- **F7 — I1-Stärken erhalten:** Agent-Block oben, Kochbuch-Narrativ, Tool-Mapping-Tabelle (Differenzierer „Portabilität"), Chat-Agent-Sektion, korrekte ogerly-URLs. Ein Rewrite darf das nicht verlieren. Schwäche: 34-zeiliger Upgrade-Prompt inline (Z.49–82) gehört nach `reference/prompts/`, README verlinkt nur.
- **F8 — EN/ZH sind blinde Flecken:** Weder I4–I6 noch diese Session haben I2/`docs/en`/`docs/zh` inhaltlich geprüft. Guideline `readme-consistency.md` verlangt Synchronität DE/EN/ZH — jede Maßnahme muss alle drei Sprachen mitziehen oder bewusst ausklammern.

## 4. Soll-Zustand (gewünscht — einheitliche Linie)

**Leitlinie:** Ein Name, ein Slogan, ein Start, eine Struktur — in README, Webseite und Entwürfen identisch.

| Element | Soll (Vorschlag) |
|---|---|
| Name | „**AAMS — Agent Manifest**" überall (kein „Mesh System", keine „Specification") |
| Slogan | **Offen (Frage F-A):** „Die unsichtbare Ordnung für deine KI-Projekte." (I4/I6) vs. „Every Agent. One File." (I1/I3) — oder beides (DE-Slogan + EN-Tagline) |
| Start | 2 Schritte, identisch überall: `curl -sO https://raw.githubusercontent.com/ogerly/AAMS/main/.agent.json` + Prompt `Lies .agent.json und führe agent_contract.on_first_entry aus. Starte sofort.` |
| Struktur | `WORKING/`-Baum identisch dargestellt (WORKPAPER / WHITEPAPER / DIARY / MEMORY / + TOOLS, LOGS, GUIDELINES) |
| Tools | Identische Tool-Liste (Copilot, Cursor, Claude Code, Codex, Windsurf, Aider, Continue.dev, LM Studio/Ollama) |
| Version/Status | AAMS/**2.4.0**, WH-**011**, aktuelle Counts, ogerly-URLs — in I1, I2, I3 synchron (WH-006-Kriterien) |
| Webseite | Self-contained (kein CDN im Default — AAMS-Geist), Copy-Buttons ✅ (bereits in I3), I7-Bilder eingebunden, DE/EN/ZH synchron |
| README | Agent-Block oben ✅ behalten, menschlicher Einstieg (I4-Ton), Status aktuell, Upgrade-Prompt ausgelagert |
| Rollen | `README.md` = Einstieg (Mensch + Agent) · `docs/` = öffentliche Seite · `aams_landing_page.html` = Design-Quelle bis zur Landing-Decision · `neue_*` = Entwurfsnotizen, danach archiviert |

## 5. Gap-Analyse Ist → Soll (Maßnahmen M1–M9)

| # | Maßnahme | Schließt Gap | Prio | Aufwand |
|---|---|---|---|---|
| M1 | Naming-Fix „Mesh System"/„Specification Standard" → „Agent Manifest" in I4, I5, I6 | F1 | 🔴 kritisch | klein |
| M2 | `DEVmatrose` → `ogerly` in `docs/{,en,zh}/index.html` (~45 Stellen) + I5-Z.59/67 | F2 | 🔴 kritisch | klein (skriptbar) |
| M3 | Versions-/Status-Sync: I3-Footer → „Agent Manifest / 2.4.0"; I1-Statusblock → 2.4.0/WH-011/aktuelle Counts; I2 prüfen | F3, F8 | 🔴 kritisch | mittel |
| M4 | `neue_README.md` reparieren (curl-Block, LICENSE-Link, Agent-Block, Status) **oder** als Rewrite verwerfen → README-Evolution (Decision F-C) | F4, F7 | 🟡 hoch | mittel |
| M5 | Landing-Decision: I6 bereinigt nach `docs/` migrieren (CDN-Frage klären) **oder** I3 evolutionär aufwerten (Decision F-B) | F5 | 🟡 hoch | groß |
| M6 | I7-Bilder (`aams-structur*.jpg`) in Landing + README einbinden | F5 | 🟢 mittel | klein |
| M7 | EN/ZH-Sync (I2 + `docs/en` + `docs/zh`) nach Guideline | F8 | 🟢 mittel | mittel |
| M8 | Upgrade-Prompt (I1-Z.49–82) nach `reference/prompts/` auslagern, README verlinkt nur | F7 | ⚪ niedrig | klein |
| M9 | Entwurfsdateien (I4–I6) ins Naming-Schema überführen oder nach `closed/` archivieren; INDEX.md pflegen | Prozess | 🟢 mittel | klein |

Empfohlene Reihenfolge: M1+M2 sofort (kritisch, klein, risikolos) → Decisions F-A–F-C → M3–M6 → M7–M9.

## 6. RFL Consistency Check (3-stufig)

- **Stage 1** (Pattern `*-MKT-*` in `closed/`): keine Treffer — kein Vorgänger mit MKT-TAG.
- **Stage 2** (LTM + Guidelines): WH-006 + Guideline `readme-consistency.md` + LTM-Einträge #128/#132 (README-Konsistenz, Health-Score) + closed `WP-2026-04-30-ARCH-README-consistency-check.md` — alle verlangen exakt das, was §4 festschreibt (Name „Agent Manifest", Status-Sync, DE/EN/ZH). Keine widersprechende Decision gefunden.
- **Stage 3** (letztes geschlossenes WP): kein Bezug zu README/Webseite.
- **Ergebnis: kein Konflikt, kein ⚠ RFL Flag.** Dieses Workpaper setzt WH-006 fort, statt es zu revidieren.

## 7. file_protocol

| Aktion | Datei |
|---|---|
| created (open) | `WORKING/WORKPAPER/WP-2026-09-16-MKT-DOC-readme-website-analyse.md` |
| read | `README.md`, `WORKING/WORKPAPER/neue_README.md`, `WORKING/WORKPAPER/neue_WEBSEITE.md`, `WORKING/WORKPAPER/aams_landing_page.html` (teilweise), `docs/index.html` (teilweise), `WORKING/WHITEPAPER/WH-006-readme-consistency.md`, `WORKING/GUIDELINES/readme-consistency.md`, `WORKING/MEMORY/ltm-index.md` (grep), `WORKING/WORKPAPER/INDEX.md` |
| analyzed (read-only) | `README.en.md`, `README.zh.md`, `docs/en/index.html`, `docs/zh/index.html` (Zeilen-Counts + URL-Grep, keine Vollprüfung — s. F8) |
| pending | `WORKING/WORKPAPER/INDEX.md` aktualisieren (WP-011 eintragen, 6-offen-Warnung vermerken) |
| 2026-09-16 umgesetzt | M1 (Naming „Agent Manifest" in I4/I5/Landing), M2 (`DEVmatrose/AAMS`→`ogerly/AAMS` in 13 Live-Dateien inkl. EN/ZH) |
| 2026-09-16 created | `docs/_archive/index-2026-09-16.old.html` (alte Landing), `README.old.md` (alte README) |
| 2026-09-16 created | `docs/index.html` neu (aus Landing + 8 Bereinigungen: Titel, Meta-Tags, Tagline, Badge, Projekt-Manifest, Strukturbild, FAQ, Footer) |
| 2026-09-16 created | `README.md` neu (~165 Zeilen: Hero beides, 3 Säulen, 2 Schritte, Chat-Prompt, Struktur+ Bild, Bridge, FAQ, Status 2.4.0/WH-011/LTM 140, Lizenz-Hinweis) |
| 2026-09-16 verified | Grep: kein `DEVmatrose/AAMS`, kein „Mesh System"/„Specification Standard" in Live-Dateien; curl-URLs ogerly ✅; LICENSE fehlt (Follow-up) |

## 8. decisions (entschieden 2026-09-16, User-Antworten)

- **F-A (Slogan) → Beides:** DE-Hero „Die unsichtbare Ordnung für deine KI-Projekte." + EN-Tagline „Every Agent. One File." — umgesetzt in README-Hero, Landing-Hero (Eyebrow) und Footer.
- **F-B (Landing) → Migrieren:** Alte `docs/index.html` nach `docs/_archive/index-2026-09-16.old.html` gesichert; `aams_landing_page.html` bereinigt als neues `docs/index.html`. `docs/en` + `docs/zh` bleiben vorerst live (nur M2-Fix) → Follow-up M7.
- **F-C (README) → Neu anlegen:** Alte `README.md` nach `README.old.md` gesichert; neue `README.md` im einheitlichen Kontext geschrieben (326 → ~165 Zeilen, Status 2.4.0/WH-011, Strukturbild, FAQ, Agent-Block behalten).
- **F-D (Scope EN/ZH) → Mitziehen bei Fixes:** M1+M2 in allen Live-Dateien inkl. EN/ZH umgesetzt. Inhaltlicher EN/ZH-Rewrite (M7) bleibt Follow-up.
- **F-E (Max-5-Regel) → noch offen.**
- **D-Audit-Ausnahme:** `closed/`, `ltm-index.md`, `WHITEPAPER/`, `observe/`, `README.backup.md` wurden bewusst NICHT umgeschrieben (Audit-Trail-Prinzip; alte Issue-Links resolvieren via GitHub-Redirect). WH-001/WH-004-Links als Follow-up.

## 9. next_steps (Follow-ups)

1. M7: EN/ZH-Rewrite (`README.en/zh`, `docs/en`, `docs/zh`) im neuen Kontext.
2. LICENSE-Datei anlegen (neue README verweist darauf; alter Link war bereits tot).
3. F-E: offene Workpapers auf ≤5 reduzieren.
4. `neue_README.md` / `neue_WEBSEITE.md` / `aams_landing_page.html` ins Naming-Schema überführen oder archivieren.
