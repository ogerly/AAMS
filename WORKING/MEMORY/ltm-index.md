# LTM — Audit-Log
## Autonomous Agent Manifest Specification

> **Dieses Dokument ist das menschenlesbare Audit-Log des LTM.**  
> Das query-fähige LTM liegt unter `WORKING/AGENT-MEMORY/` (ChromaDB oder kompatibel).  
> Jeder Agent ingested nach jeder Session in beide: den Audit-Log (hier) und den Vektorspeicher.

---

## LTM-Architektur

| Komponente | Pfad | Zweck |
|---|---|---|
| Audit-Log | `WORKING/MEMORY/ltm-index.md` | Menschenlesbar. Was wurde wann ingested. Immer im Git. |
| Vektorspeicher | `WORKING/AGENT-MEMORY/` | Querybar. Semantische Suche. Ab Session 1 aktiv. In `.gitignore`. |

**Warum beides:** Der Audit-Log ist die Wahrheit die Menschen lesen können. Der Vektorspeicher ist die Wahrheit die Agenten effizient abfragen können. Ohne Vektorspeicher degradiert jede LTM-Abfrage ab ~100 Einträgen zur Blindheit.

**Empfohlenes Backend:** ChromaDB (lokal, kein API-Key, Open Source)  
**Setup:** `pip install chromadb` → `WORKING/AGENT-MEMORY/` wird automatisch angelegt beim ersten Ingest.

**Fallback ohne Vektorspeicher:**

| Einträge | Zustand | Was der Agent tut |
|---|---|---|
| < 90 | Normal | Audit-Log vollständig laden |
| ≥ 90 | **Warnung** | Agent meldet: Vektorspeicher fehlt, Kontext wird bald blind |
| ≥ 100 | **Blind** | Agent lädt nur die letzten 20 Einträge — ohne Vektorspeicher gibt es keine andere Option |

**Agent-Pflicht ab Eintrag 90 (wenn kein Vektorspeicher vorhanden):**
> *„Der LTM-Audit-Log hat aktuell N Einträge. Kein Vektorspeicher gefunden unter `WORKING/AGENT-MEMORY/`. Ab 100 Einträgen ist älterer Kontext blind. Bitte `pip install chromadb` ausführen — der Agent ingested beim nächsten Sessionstart automatisch."*

---

## Status

- **Initialisiert:** 2026-02-22
- **Letzter Ingest:** 2026-07-06 (WH-009 Guard-Pattern)
- **Einträge gesamt:** 140

---

## Index

| # | Datum | Typ | Datei | Inhalt |
|---|---|---|---|---|
| 001 | 2026-02-22 | SPEC | `SPEC.md` | Vollständige AAMS-Spezifikation (englisch). |
| 002 | 2026-02-22 | SPEC | `SPEC-DE.md` | Vollständige AAMS-Spezifikation (deutsch). |
| 003 | 2026-02-22 | MANIFEST | `AGENT.json` | Referenz-Manifest AAMS/1.0. Fix: `whitepapers` auf `./WORKING/WHITEPAPER`. |
| 004 | 2026-02-22 | SCHEMA | `AGENT_SCHEMA.json` | JSON Schema für AGENT.json Validierung. |
| 005 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-bootstrap-session.md` | Bootstrap-Session. Workspace-Struktur angelegt. |
| 006 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-repo-analyse.md` | Repo-Analyse. Inventar, Issues #1-#3 gelöst. |
| 007 | 2026-02-22 | WHITEPAPER | `WORKING/WHITEPAPER/WP-001-aams-overview.md` | Erstes Whitepaper. Projektübersicht, Dreischichtenmodell, Bootstrap-Ablauf. |
| 008 | 2026-02-22 | ENTRY | `READ-AGENT.md` | Agent-Einstiegspunkt mit vollem Agent Contract und LTM-Trigger-Tabelle. |
| 009 | 2026-02-22 | README | `README-DE.md` | Neue README (deutsch). Positionierung, kein technisches Overload. Verweist auf SPEC-DE. |
| 010 | 2026-02-22 | README | `README.md` | Neue README (englisch). Exakte Übersetzung von README-DE. |
| 011 | 2026-02-22 | README | `README-CH.md` | Neue README (Mandarin). Exakte Übersetzung. |
| 012 | 2026-02-22 | TEMPLATE | `templates/read-agent-template.md` | Pfade korrigiert, Agent Contract + LTM-Trigger ergänzt. |
| 013 | 2026-02-22 | BRIDGE | `AGENTS.md` | Tool-Bridge. Single Source of Truth für Copilot, Cursor, Claude Code, Codex, Windsurf, Aider, Continue.dev. Verweist auf READ-AGENT.md + AGENT.json. |
| 014 | 2026-02-22 | CONFIG | `.github/copilot-instructions.md` | Thin redirect zu AGENTS.md. Existiert nur weil Copilot dort sucht. |
| 015 | 2026-02-22 | SKILL | `AGENT.json` (`skills.custom_skills`) | `bootstrap_workspace` Skill eingetragen. Input: `{repo_root, dry_run}`. Output: `{created_dirs, created_files, skipped, warnings}`. Idempotent. |
| 016 | 2026-02-22 | ARCHIVE | `archive/blog-artikel.md` | `blog-artikel.md` archiviert. Inhalt funktional ersetzt durch README-DE.md. Kein aktiver Teil des Standards. |
| 017 | 2026-02-22 | SESSION | `WORKING/WORKPAPER/closed/` | Session-Close: beide Workpaper (bootstrap-session + repo-analyse) nach closed/ verschoben. LTM auf 17 Einträge. |
| 018 | 2026-02-22 | REVIEW | root | Hartes Review: README-CH.md nach archive/ verschoben. 6 Pfadfehler in SPEC.md + SPEC-DE.md korrigiert: `./WORKING/docs`→`WHITEPAPER`, `close`→`closed`, `AGENT-MEMORY`→`MEMORY`. |
| 019 | 2026-02-22 | DECISION | `.gitignore` + `.agent.json` | Gitignore-Architekturentscheidung: `WORKING/MEMORY/` nicht mehr ignoriert (ltm-index.md ist Kollaborationsartefakt). `WORKING/LOGS/` bleibt ignoriert. Vektorspeicher-Patterns auskommentiert vorbereitet. Stale-Einträge entfernt. |
| 020 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-hartes-review-v1.md` | Hartes Review erfasst und bewertet. 8 Kritikpunkte gewichtet, 4 rote Prioritäten identifiziert. |
| 021 | 2026-02-22 | README | `README.md` + `README-DE.md` | 4 rote Prioritäten umgesetzt: Tagline geändert, Cross-Tool-Sektion als Lead, Hierarchie-Tabelle, Proof-Abschnitt ehrlich umformuliert. DE von EN abgeleitet. |
| 022 | 2026-02-22 | DECISION | `ltm-index.md` + `.agent.json` + `AGENT.json` | Dual-Layer-LTM-Architektur: `ltm-index.md` = Audit-Log (Git), `WORKING/AGENT-MEMORY/` = ChromaDB (Sessions 1+). ChromaDB als Disziplin ab Session 1, nicht als Fallback. |
| 023 | 2026-02-22 | SPEC | `SPEC-DE.md` | Alle ~10 fehlenden Abschnitte vs. SPEC.md ergänzt: governance-Hinweis, auto_create false-Modus, Whitepaper-Index/Guidelines-Empfehlungen, Schritt-Reihenfolge, workpaper_rules (template_file_quick, Vollversion/Kurzvorlage, Nesting, Metadata-Header), file_tracking (track_moved, track_archived), _ref-Linting, Schema-Striktheitstabelle, Zukünftige Profile Vorbedingungen. 727→809 Zeilen. |
| 024 | 2026-02-22 | SESSION | `WORKING/WORKPAPER/closed/2026-02-22-hartes-review-v1.md` | Session-Close: hartes-review Workpaper abgeschlossen und nach closed/ verschoben. `AGENT.json` `_spec_url_status: planned` ergänzt. LTM auf 24 Einträge. |
| 025 | 2026-02-22 | TOOL | `WORKING/TOOLS/ltm_chroma.py` | ChromaDB Tool implementiert. Hash-128 Embedding (kein ML, kein Download). Bug gefixt: Endlosschleife in `chunk_by_size`. Bulk-Ingest: 11 Dateien, 114 Chunks. Query-Test erfolgreich. AGENT-MEMORY aktiv. |
| 026 | 2026-02-22 | PAGES | `docs/index.html` | GitHub Pages One-Pager erstellt. Dark theme, zero dependencies, Copy-Button, mobile-ready. 7 Sektionen: Problem, curl, Steps, Tools, Proof, Get started, Footer. GitHub Pages Setup ausstehend (manuell). |
| 027 | 2026-02-22 | SESSION | `WORKING/WORKPAPER/closed/2026-02-22-github-pages-onepager.md` | GitHub Pages Session abgeschlossen. `docs/index.html` fertig, abgenommen. Workpaper nach closed/. |
| 028 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-feldtest-independentes-repo.md` | Feldtest-Workpaper angelegt. Testplan, Hypothesen, Beobachtungs-Tabelle. Ausstehend: echtes externes Repo. |
| 029 | 2026-02-22 | COMMIT | `600f40c` | Repo umbenannt zu `AAMS---Autonomous-Agent-Manifest-Specification`. Git remote aktualisiert. Alle placeholder URLs (`aams-spec/aams`) ersetzt. GitHub Pages Link in README.md + README-DE.md an zentraler Stelle eingefügt. `_spec_url_status` entfernt (URL live). |
| 030 | 2026-02-22 | DECISION | `WORKING/WORKPAPER/closed/2026-02-22-ltm-versionierung-git-chroma-sync.md` | Entscheidung: kein Git-in-Git. Git ist bereits als Versionierung vorhanden (`ltm-index.md` in Git = vollständige History). Echter Gap: ChromaDB-Rebuild nach Datenverlust. Lösung: `ltm-rebuild.py` in `WORKING/TOOLS/` — deterministischer Rebuild aus `ltm-index.md`. Workpaper geschlossen. |
| 031 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-issue-1-security-secret-exclusion-policy.md` | Workpaper für Issue #1 angelegt. 7 DoD-Punkte: gitignore_patterns erweitern, permissions härten, ltm_triggers Pre-Save-Scan, AGENT_SCHEMA.json output_validation, SPEC.md Sektion, Templates-Update, .gitignore prüfen. |
| 032 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-issue-2-project-analysis-template.md` | Workpaper für Issue #2 angelegt. 5 DoD-Punkte: project-analysis-template.md erstellen, SPEC.md "Before You Write a Manifest", onboarding Step 0, README Verweis, AGENT_SCHEMA.json project_analysis_path. |
| 033 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-issue-3-spec-luecken.md` | Workpaper für Issue #3 angelegt. 8 Lücken analysiert und priorisiert: _doc-Convention, onboarding Action-Enum, workpaper_path Variablen, closing_checklist Registry, fallback_providers Priorität, session.workpaper_template, LTM-Migration, capabilities-Registry. |
| 034 | 2026-02-22 | SECURITY | `AGENT.json` + `AGENT_SCHEMA.json` + `SPEC.md` + `templates/` + `.gitignore` | Issue #1 umgesetzt: 7 DoD gescored. gitignore_patterns (+8 Secret-Muster), restricted_write für .gitignore, ltm_triggers workpaper_pre_save+scan_secrets, AGENT_SCHEMA output_validation+forbidden_patterns, SPEC.md output_validation-Untersektion + H2 "Absolute Secret Exclusion Policy" (3-Layer-Modell, Risk-Matrix, Pre-Commit-Hook-Implementierung), beide Templates aktualisiert. |
| 035 | 2026-02-22 | TEMPLATE | `templates/project-analysis-template.md` + `SPEC.md` + `AGENT.json` + `AGENT_SCHEMA.json` + `README.md` | Issue #2 umgesetzt: 5 DoD. Neues Template (9 Sektionen, Tabellen-Format, Affects-Hinweise). SPEC.md: H2 "Before You Write a Manifest" vor Structure Overview. AGENT.json: onboarding Step 0 read_project_analysis (condition: file_exists, priority: mandatory_if_present). AGENT_SCHEMA.json: project_analysis_path optional field. README.md: Verweis für Existing-Project-Onboarding. |
| 036 | 2026-02-22 | SPEC | `SPEC.md` + `AGENT_SCHEMA.json` + `registry/capabilities.md` | Issue #3 umgesetzt: 8 Lücken. L1: _doc-Convention-Abschnitt. L2: read_project_analysis+file_exists in Enum+Tabelle, priority-Feld. L3: Template-Variable-Tabelle ({date}=YYYY-MM-DD, {agent}=kebab, {topic}=kebab). L4: 7 Standard-Closing-Checklist-Items. L5: fallback_providers (Array-Pos=Priorität) in SPEC+Schema. L6: bereits implementiert (template_file). L7: LTM-Migration-Prozedur (5 Schritte, _migration-Annotation, ltm-rebuild.py-Verweis). L8: registry/capabilities.md erstellt (9 Kategorien, 30+ Capabilities, URL in SPEC aktualisiert). |
| 037 | 2026-02-22 | TOOL | `WORKING/TOOLS/_selfcheck.py` | 34-Check Automated Self-Validation Tool. JSON-Syntax, Schema-Validierung, Pfade, Workpaper-Status, Git-Cleanliness, SPEC-Dokumentation, Schema-Vollständigkeit. Alle 34 Checks grün. |
| 038 | 2026-02-22 | POSITIONING | `SPEC.md` | Positionierungsabschnitt nach Philosophy eingefügt: "AAMS does not solve the LTM problem. It creates the scaffolding that makes LTM solutions pluggable." Extension-Point `memory.long_term.backend` dokumentiert. |
| 039 | 2026-02-22 | CONFIG | `.agent.json` | P2-Fix: `ltm_store_backend` → `ltm_store_backend_recommended` + `_ltm_store_backend_note`. Zero-dependency-Konsistenz wiederhergestellt: ChromaDB ist Empfehlung, kein implizites Requirement. |
| 040 | 2026-02-22 | WHITEPAPER | `WORKING/WHITEPAPER/WP-002-related-work.md` | Related Work Whitepaper erstellt. AAMS vs. MemGPT/Letta, LangChain Memory, DVC, FIPA ACL, `.cursorrules`/`CLAUDE.md`/per-tool-files. Gap-Analyse: 8 unique AAMS capabilities. Positioning: "the interface layer on top of which those systems operate." |
| 041 | 2026-02-22 | SESSION | `WORKING/WORKPAPER/closed/2026-02-22-review-analyse-und-forschungsebene.md` | Review-Analyse Session abgeschlossen. Commit 0ad66d6. CLOSED + archiviert. |
| 042 | 2026-02-22 | RENAME | `AGENT.json` + `docs/index.html` + `registry/capabilities.md` + `README.md` + `README-DE.md` | Repo umbenannt zu `DEVmatrose/AAMS`. Alle URLs aktualisiert: AGENT.json (3x), index.html (curl + footer + proof + repo-url), capabilities.md, README.md + README-DE.md (GitHub Pages → devmatrose.github.io/AAMS). git remote aktualisiert. Commit 5aa8f8c. |
| 043 | 2026-02-22 | ASSET | `docs/logo_comb.png` + `docs/logo_visual.png` + `docs/logo_text.png` | Logo in Repo aufgenommen (3 Varianten). Primär: logo_comb.png (Text+Bild). Eingebaut in docs/index.html (200px, über Badge) + README.md + README-DE.md (zentriert, 280px). Commit ef3aea3. |
| 044 | 2026-02-22 | FIX | `prompts/system.md` | Backslash-Korruption entfernt (`\runtime.system_prompt_file\`, `\READ-AGENT.md\`n`). Echter Minimal-System-Prompt als Template eingefügt (MUST/MUST NOT Regeln, Hinweis auf Anpassung). Commit 23d8899. |
| 045 | 2026-02-22 | FIX | `.agent.json` + `AGENTS.md` + `AGENT_SCHEMA.json` | Konsistenz-Fixes: `_source` aams-spec/aams → DEVmatrose/AAMS; AGENTS.md Footer-Tagline "No context loss" → "No more starting from zero"; AGENT_SCHEMA.json `$id` URL aktualisiert. |
| 046 | 2026-02-22 | SCHEMA | `AGENT_SCHEMA.json` | `bootstrap_rules` als neues Top-Level-Property eingeführt. 7 Felder: `ltm_markdown_threshold`, `ltm_warning_at`, `ltm_exceeded_behavior`, `ltm_store`, `ltm_store_backend_recommended`, `ltm_store_setup`, `ltm_audit_log`. Validierung: 0 Errors. Schliesst die Schema-Lücke für .agent.json LTM-Felder. |
| 047 | 2026-02-22 | RESEARCH | `WORKING/WHITEPAPER/WP-002-related-work.md` | Gas Town (Yegge, 2026) als neue Related Work Sektion aufgenommen. WP-002 v1.0 → v1.1. Vergleichstabelle: neuer Eintrag (Git Worktrees + Beads + 10-30+ Parallel-Agenten). Detailsektion: Architektur (Mayor/Deacon/Polecats/Witness/Refinery/Sweeps), Cattle-not-Pets, Mailboxes/Handoffs/Convoys/Beads. Kritischer Fund: Heise-Artikel zitiert Gas Town als Empfehlung für Rule-Dateien (AGENT.md/CLAUDE.md) — direkte In-the-wild-Validierung der AAMS-Prämisse. AAMS-Positioning: Execution-Layer (Gas Town) vs. Repo-Contract-Layer (AAMS). Gap Analysis: neue Zeile für Multi-Agent-Repo-Contract. Conclusion: Gas Town als stärkstes Argument für AAMS ergänzt. Referenzen: Yegge 2026 + Eichhorst/heise 2026. |
| 048 | 2026-02-25 | ISSUES | `prompts/bootstrap.md` + `README.md` + `templates/workpaper-template.md` + `SPEC.md` | Issues #4, #5, #6 implementiert. #4 (Bootstrap-Adoption): `prompts/bootstrap.md` neu erstellt mit Bootstrap-Prompt, Tool-Varianten (Claude Code, Copilot, Cursor, Aider), Session-Start-Prompt. README.md: "Start in 2 Steps" Sektion mit curl + Bootstrap-Prompt. #5 (Live-Dokumentation): `templates/workpaper-template.md` um Sektion 2 "Running Log" erweitert mit Inline-Checkpoint-Regel; alle Sektionen umnummeriert (2→3…7→8). #6 (Agent-Onboarding-Feedback): SPEC.md ergänzt um: index_ltm-Setup (ChromaDB pip install), Fallback-Verhalten (skip + Markdown-Fallback), WORKING/-Pfad-Klarheit (immer relativ zum Repo-Root), Template-Hinweis (aus AAMS-Repo kopieren oder inline generieren), incremental-write-Note für Agents ohne persistent memory. |
| 049 | 2026-02-26 | UX-FIX | `docs/index.html` | Entry-Point-Klarheit: "Get started"-Sektion komplett umgebaut. `.agent.json` als THE one file mit eigenem curl-Block als erstem CTA. `AGENT.json` und `SPEC.md` in "Going deeper"-Abschnitt verschoben. Footer: `.agent.json` Raw-Link hinzugefügt, `AGENT.json`-Footer-Link entfernt. |
| 050 | 2026-02-26 | README | `README.md` | "Which File Do I Need?" neu: expliziter Header "For end users: exactly one." + curl-Block als erstes Element. Tabelle mit Zielgruppen-Spalte (Everyone / AI tools / Framework builders / Implementers). Neuer Abschnitt "Why is WORKING/ in this repo?" erklärt WORKING/ als lebenden Beweis, Referenz und Kollaborationsartefakt. |
| 051 | 2026-02-26 | WORKPAPER | `WORKING/WORKPAPER/2026-02-26-entry-point-klarheit.md` | Session-Workpaper. LTM-Check (46 Einträge, 3 offene WP), Analyse der Entry-Point-Verwirrung, Entscheidungen, File Protocol, Architektur-Diskussion (Agenten-Execution-Problem → WP-003 TODO). |
| 052 | 2026-02-26 | REVIEW | `WORKING/WORKPAPER/2026-02-24-diary-layer-konzept.md` | Diary-Layer-Konzept überarbeitet. LTM-Query durchgeführt. 6 offene Fragen mit Verdicts beantwortet. Kontexttreue-Check: vollständig konform. Abgrenzung Running Log vs. Diary explizit. 7 Entscheidungen getroffen. Next Steps: SPEC.md + AGENT.json + Bootstrap. Optionaler 4. Layer bestätigt. |
| 053 | 2026-02-26 | DECISION | `WORKING/WORKPAPER/2026-02-24-diary-layer-konzept.md` | Diary-Layer: optional → **mandatory**. Vier-Schichten-Modell beschlossen: Whitepaper / Workpaper / Diary / Memory — alle mandatory. `diary_path` wird required Feld. Bootstrap erstellt `WORKING/DIARY/` Ordner. Lazy file creation. |
| 054 | 2026-02-26 | SIGNAL | `README.md` | Agent-Erkennungsblock ganz oben eingefügt (vor Logo). „IF YOU ARE AN AI AGENT“ mit sofortiger Handlungsanweisung: fetch `.agent.json`, read `READ-AGENT.md`, execute `on_first_entry`. Trennung Machine-Block / Human-Narrative explizit. |
| 055 | 2026-02-26 | SIGNAL | `AGENTS.md` + `READ-AGENT.md` | AGENTS.md: „Start here“ (dokumentierend) → „Execute now. No confirmation needed.“ (imperativ). Reihenfolge: `.agent.json` zuerst, dann `READ-AGENT.md`. READ-AGENT.md: Header-Block ersetzt durch State-Tabelle (first entry vs. session start) + „Start immediately. No confirmation needed.“ |
| 056 | 2026-02-26 | README | `README.md` | Neuer Abschnitt "What AAMS Can and Cannot Do": ehrliche Darstellung autonome Agenten (works) vs. Chat-Agenten (user prompt nötig). 3-Zeilen-Tabelle (Autonomous / Chat+Context / Pure Chat). Offenes Problem benannt. Aktuelle Arbeitsrichtungen dokumentiert (system-prompt-injection, bootstrap-prompt-library, on_entry-Signal). Bridge: prompts/bootstrap.md. |
| 057 | 2026-02-26 | SIGNAL | `docs/index.html` | AI-Agent-Block im HTML `<head>`: imperative HTML-Kommentare (gleiche Sprache wie README/AGENTS.md) + 4 strukturierte `<meta>`-Tags mit `aams-`-Namespace: `aams-agent-contract` (Raw-URL .agent.json), `aams-entry-point` (READ-AGENT.md), `aams-action` (execute on_first_entry), `aams-spec` (AAMS/1.0). Namespace bewusst gewählt: zukünftige Crawler/Runtimes können `aams-`-Tags als Erkennungsmuster nutzen. |
| 058 | 2026-02-26 | SESSION | `WORKING/WORKPAPER/2026-02-26-entry-point-klarheit.md` | Session-Dokumentation vervollständigt. Running Log + File Protocol aktualisiert (README Ehrlichkeits-Sektion + HTML-Meta-Tags). LTM-Ingest abgeschlossen. |
| 059 | 2026-02-28 | FIX | `SPEC.md` | 3× stale URL `aams-spec/aams` → `DEVmatrose/AAMS` korrigiert (L4, L495, L1089). |
| 060 | 2026-02-28 | SESSION | `WORKING/WORKPAPER/closed/2026-02-23-fix-ltm-python-interpreter.md` | WP 2026-02-23 geschlossen. Fix (LTM Commands Block in READ-AGENT.md) war bereits implementiert — WP nur nicht archiviert. Status → CLOSED, nach closed/ verschoben. |
| 061 | 2026-02-28 | FEATURE | `SPEC.md` | Diary Layer (Temporal Context Layer) implementiert. Neuer `#### diary` Abschnitt im workspace-Bereich: Vier-Schichten-Modell (Whitepaper/Workpaper/Diary/Memory), drei Regeln, monatliche Dateien, lazy creation, LTM-Integration, Section Interplay aktualisiert. `diary_path` in Base Fields und Folder Roles Tables ergänzt. |
| 062 | 2026-02-28 | FEATURE | `AGENT.json` | `workspace.structure.diary: "./WORKING/DIARY"` hinzugefügt. Vier-Schichten-Modell im Manifest verankert. |
| 063 | 2026-02-28 | FEATURE | `AGENT_SCHEMA.json` | `diary` in `workspace.structure.properties` ergänzt mit Description (Temporal Context Layer). |
| 064 | 2026-02-28 | DIARY | `WORKING/DIARY/2026-02.md` | Erstes Diary-File angelegt. Zwei Einträge: (1) Repo-Review-Erkenntnisse + Lehre über "Entschieden aber nicht umgesetzt". (2) Sicherheitsvorfall Access-Token im Chat. |
| 065 | 2026-02-28 | SESSION | `WORKING/WORKPAPER/closed/2026-02-24-diary-layer-konzept.md` | WP 2026-02-24 CLOSED. Alle 5 Next Steps implementiert. Vier-Schichten-Modell vollständig. Nach closed/ verschoben. |
| 066 | 2026-02-28 | FIX | `READ-AGENT.md` | Current Status Sektion aktualisiert: LTM 28→58 Einträge, Whitepapers 1→2, offene WPs korrigiert, Diary Layer ergänzt, Issues #1-6 Status. |
| 067 | 2026-02-28 | SESSION | `WORKING/WORKPAPER/closed/2026-02-28-repo-issue-review.md` | Repo-Issue-Review Session abgeschlossen. 5 Issues identified, 4 vollständig gelöst, 1 suspended (Feldtest). Diary Layer implementiert. LTM-Ingest abgeschlossen. |
| 068 | 2026-03-26 | SESSION | `WORKING/WORKPAPER/2026-03-26-issue-analyse-und-umsetzungsplan.md` | AAMS Self-Check + vollständiger GitHub Issue Review (9 offene Issues). Konsolidierter Umsetzungsplan mit 7 Tasks (T1-T7). |
| 069 | 2026-03-26 | FEATURE | `reference/AGENT_SCHEMA.json` | T1: `_deviations` Array-Property im Schema hinzugefügt. Objekte mit `spec_path`, `actual_path`, `reason` (alle required). |
| 070 | 2026-03-26 | FEATURE | `reference/AGENT.json` | T1: `_deviations` Beispiel-Einträge aus Luna-1 Feldreport eingefügt. |
| 071 | 2026-03-26 | FEATURE | `reference/SPEC.md` | T1: `_deviations — Intentional Deviations` Sektion vor `_ Annotation Convention` eingefügt mit Regeln und JSON-Beispiel. |
| 072 | 2026-03-26 | FEATURE | `README.md` | T2: LTM Setup Order Tabelle (ltm-index.md first, ChromaDB optional). T3: "No CLAUDE.md. No GEMINI.md." Mapping-Tabelle — AAMS ersetzt tool-spezifische Dateien. |
| 073 | 2026-03-26 | FEATURE | `READ-AGENT.md` | T4: §4 Agent-Specific Workflow Integration — Blueprint.md 2-Phase Pattern für Gemini/Firebase Studio. |
| 074 | 2026-03-26 | GITHUB | Issues #21-#26 | 6 neue Issues aus Workpaper-Analyse erstellt. #21 _deviations, #22 LTM hero, #23 CLAUDE.md positioning, #24 Blueprint.md, #25 Session-Start Prompts, #26 Security Signals. |
| 075 | 2026-03-26 | GITHUB | Issues #7,#8,#14-#20 | Alle 9 Legacy-Issues geschlossen mit Kommentaren. Superseded durch T1-T4 oder durch neue Issues #21-#26 abgedeckt. |
| 076 | 2026-03-26 | FIX | `.agent.json` | Vier-Schichten-Modell: `diary` in `workspace.structure` + `documentation_model` aufgenommen. Von "Three-layer" auf "Four-layer" korrigiert. |
| 077 | 2026-03-26 | FIX | `AGENTS.md` | `DIARY/` in Workspace-Baumdarstellung ergänzt. |
| 078 | 2026-03-26 | FIX | `reference/templates/read-agent-template.md` | `DIARY/` in Template-Baumstruktur eingefügt — neue Bootstraps erzeugen jetzt Vier-Schichten READ-AGENT.md. |
| 079 | 2026-03-26 | FIX | `docs/index.html` | LTM-Zahlen aktualisiert (46→67+), `prompts/bootstrap.md` → `reference/prompts/bootstrap.md`, Footer SPEC-Link → `reference/SPEC.md`. |
| 080 | 2026-03-26 | UPDATE | `WORKING/WHITEPAPER/WP-001-aams-overview.md` | Stand 2026-03-26: T1-T4 Features dokumentiert, Issue-Status, LTM-Zahlen, neue Features-Zeile. |
| 081 | 2026-03-26 | CLEANUP | `WORKING/DATABASE/` | Geistordner entfernt — Artefakt aus Selfcheck-Commit 8259553, nie in `.agent.json` deklariert. |
| 082 | 2026-03-27 | ANALYSE | `WORKING/WORKPAPER/2026-03-27-long-horizon-reasoning-analyse.md` | Long-Horizon-Reasoning (LHR) Analyse für reale Codebases. Kernthese: AAMS löst LHR nicht, sondern liefert das Scaffolding (unterste lösbare Schicht im LHR-Stack). Geschichte CoT→MemGPT→Voyager→SWE-bench→Gas Town→AAMS. Wirtschaftlich: asymmetrisch positiv (Zero Cost, -90% Token-Wiederholung, -96% Onboarding-Zeit). Wahrheit: LLMs können nicht autonom langfristig planen, aber mit Scaffolding bei jeder Session wissen wo sie stehen. Open Source: Pflicht, nicht Option. Issue #27. |
| 083 | 2026-03-27 | ANALYSE | `WORKING/WORKPAPER/2026-03-27-long-horizon-reasoning-analyse.md` | Cross-Model-Validierung: Kimi, ChatGPT, Grok, Claude bestätigen unabhängig: LHR = Infrastruktur-Problem, nicht Modell-Problem. Konvergente Selbstdiagnose. 4 Gaps für v1.1: G1 LTM-Query-Protokoll, G2 Auto-Kompression, G3 CI-Enforcement, G4 Intent-Awareness. |
| 084 | 2026-03-27 | WHITEPAPER | `WORKING/WHITEPAPER/WP-004-long-horizon-reasoning.md` | WP-004 erstellt. LHR-Analyse aus Workpaper zu stabilem Whitepaper promoviert. 11 Sektionen, Cross-Model-Validierung, 5 identifizierte Gaps, Referenzen. |
| 085 | 2026-03-27 | SPEC | `reference/SPEC.md` | LHR-Positionierungsabsatz nach Philosophy: "AAMS is the lowest solvable layer in the LHR stack." Verweis auf WP-004. |
| 086 | 2026-03-27 | SESSION | `WORKING/WORKPAPER/closed/2026-03-27-long-horizon-reasoning-analyse.md` | Session CLOSED. WP-004 erstellt, SPEC.md aktualisiert, Cross-Model-Validierung dokumentiert. Offene Items: G1-G4 als Issues, v1.1-Roadmap. |
| 087 | 2026-03-27 | GITHUB | Issues #28-#31 (vorbereitet) | 4 Issue-Bodies für v1.1-Gaps erstellt: #28 Standardisiertes LTM-Query-Protokoll (query_ltm), #29 Automatische Workpaper-Kompression, #30 CI-Enforcement-Hooks, #31 Intent-Awareness im Diary. Alle referenzieren WP-004 + Issue #27. |
| 088 | 2026-03-27 | UX | `reference/prompts/bootstrap.md` | Issue #25: Bootstrap-Gap geschlossen. Komplette Überarbeitung: 7 Sektionen (Quick Reference, Bootstrap, Session Start, LTM Query, Workpaper, Session Close, Tool-Variants + VS Code Snippets). Kernänderung: "before starting any work" im Session-Start-Prompt gegen 30% Workpaper-Failure. |
| 089 | 2026-03-27 | UX | `README.md` | "Chat Agent Users: Start Here" Abschnitt nach Quick Start eingefügt. Session-Start-Prompt direkt kopierbar. Verweis auf bootstrap.md für weitere Prompts. |
| 090 | 2026-03-27 | SESSION | `WORKING/WORKPAPER/2026-03-27-issue-25-bootstrap-gap.md` | Session CLOSED. Issue #25 vollständig umgesetzt: bootstrap.md überarbeitet, README.md ergänzt, VS Code Snippet dokumentiert. |
| 091 | 2026-03-27 | FIELD-REPORT | `WORKING/WHITEPAPER/WP-003-field-discourse.md` | Issue #28: Antigravity (Google DeepMind AI Agent) evaluiert AAMS auf qa-agent v4. Fazit: "zwingend notwendige Projekt-Hygiene". Initialer Fehlstart (Repo geklont statt .agent.json geladen) bestätigt Bootstrap-Gap auch für autonome Agents. Friktionen: doppelte Buchführung (natives Task-System vs. AAMS Workpaper), LTM-Abruf braucht expliziten Trigger. Vorschlag: agent-entrypoint.json. Junior-Developer-Metapher. |
| 092 | 2026-03-28 | MARKETING | `WORKING/WORKPAPER/2026-03-28-video-marketing-kochbuch.md` | Erstes Marketing-Paket dokumentiert. Video-Drehbuch „Das Kochbuch für dein Repo" (40 Sek., Oma-Metapher, 4 Szenen). Social-Media-Texte: LinkedIn (2 Varianten: Problem-fokus/Metapher), X/Twitter (2 Varianten). Strategische Einordnung mit Feldbericht-Validierung (#17 Luna-1, #20 Copilot, #28 Antigravity). Kampagnen-Assets vollständig. |
| 093 | 2026-04-09 | DECISION | `WORKING/WORKPAPER/closed/2026-04-09-science-knowledge-validation-layer.md` | SCIENCE (Knowledge Validation Layer) als fünfter Dokumentations-Layer konzipiert und VERWORFEN. Zu komplex für Spec, bricht local-first. Konzept wandert ins Agent-Loop-Framework. Spec = Körper, Framework = Geist. |
| 094 | 2026-04-09 | ARCHITECTURE | `WORKING/WORKPAPER/2026-04-09-rfl-reflection-protocol-step.md` | RFL (Reflection Protocol Step) eingeführt als Schritt 4 in on_session_start. 3-Stufen-Konsistenzprüfung: Stage 1 Pattern-Match auf TOPIC-Tag (*-{TOPIC}-*), Stage 2 LTM-Query, Stage 3 letztes Workpaper chronologisch. Löst: Agent widerspricht sich über Sessions. Output: ⚠ RFL Consistency Flag im Workpaper. Kein neuer Layer, kein neuer Ordner. |
| 095 | 2026-04-09 | ARCHITECTURE | `.agent.json` + `READ-AGENT.md` | Naming Schema eingeführt. Workpapers: {DATE}-{TOPIC}-{SUBTOPIC}-{description}.md. Whitepapers: WP-{NNN}-{TOPIC}-{description}.md. TOPIC-Tags (ARCH, SPEC, LTM, SEC, etc.) als primärer Ordnungsschlüssel für RFL Pattern-Matching. Hybrid-Ansatz: Spec empfiehlt, Framework erzwingt. Topic Registry erweiterbar. |
| 096 | 2026-04-09 | WHITEPAPER | `WORKING/WHITEPAPER/WP-001-aams-overview.md` | WP-001 aktualisiert auf 2026-04-09. Naming Schema und RFL als Core-Elemente ergänzt. Aktueller Stand: Issues #36-#39, v1.2.0 Release. |
| 097 | 2026-04-09 | ARCHITECTURE | `WORKING/WORKPAPER/closed/2026-04-09-ARCH-DRY-diary-granularity-problem.md` | Diary-Layer reformiert: Pointer-only Zeitindex statt Workpaper-Abstracts. Redundanz-Test: 100% der Diary-Einträge waren Dubletten. Neues Format: `YYYY-MM-DD \| WP: {datei} \| WH: {datei}`. Hierarchische Kompression: Tag→Woche→Monat (429/Jahr). "Max 10 Zeilen" ersatzlos gestrichen. |
| 098 | 2026-04-09 | ARCHITECTURE | `.env` + `READ-AGENT.md` + `reference/SPEC.md` | Version-Zentralisierung: `AAMS_VERSION` in `.env` als Single Source of Truth. Löst Versionsdrift (v1.2.0 released aber 1.1 in Dateien). v1.3.0 released. |
| 099 | 2026-04-09 | SESSION | `WORKING/WORKPAPER/closed/2026-04-09-rfl-reflection-protocol-step.md` | RFL-Workpaper geschlossen (war seit v1.2.0 erledigt aber noch offen). |

---

## Kernerkenntnis (extrahiert aus allen Quellen)

### Was AAMS ist
- Kein Framework. Kein Tool. Kein Runtime.
- Ein **deklarativer Architekturstandard** der in jedem Repo als Datei existiert.
- Besteht aus zwei Dateien: `AGENT.json` (voll) + `.agent.json` (minimal/portabel).

### Vier-Schichten-Dokumentationsmodell
1. **Workpaper** — sessiongebunden, operativ, wird nach Abschluss archiviert
2. **Whitepaper** — stabile Systemwahrheit, architektonisch, nie gelöscht
3. **Diary** — chronologischer Entscheidungslog, monatsweise, max 10 Zeilen pro Eintrag
4. **Memory (LTM)** — persistenter Kontextspeicher über Sessions hinweg

### Offene Issues (Stand 2026-04-17)
- **Issues #1-#20:** Alle geschlossen.
- **Issues #21-#25:** Alle geschlossen (T1-T4 implementiert, Prompts überarbeitet).
- **Issue #26 — Security Signals:** Offen (Backlog, post AAMS/2.0).
- **Issue #39 — v1.2.0 Release:** Geschlossen.
- **Issue #41 — MantisClaw Field Report:** Offen (Topic Registry + Compat Matrix ausstehend).
- **Issue #43 — RFC Spec→Contract:** Offen als RFC-Tracker.
- **Issue #48 — Decision-Kompoundierungs-Leck:** Offen, CRITICAL.
- **Issue #49 — Upgrade-Transparenz:** Offen, HIGH.

### Bootstrap-Ablauf (normativ)
1. `.agent.json` lesen
2. Struktur prüfen / anlegen
3. Repository scannen
4. READ-AGENT.md lesen/erstellen
5. Erstes Workpaper mit Analyse erstellen
6. LTM initial befüllen

---

## Backend-Status

| Backend | Status | Pfad |
|---|---|---|
| Markdown-Index | ✅ Aktiv | `WORKING/MEMORY/ltm-index.md` |
| Vektorspeicher | ✅ Aktiv | `WORKING/AGENT-MEMORY/` — 114 Chunks, Hash-128 Embedding |

> Hash-128 Embedding (pure Python, kein ML). Wechsel zu semantischem Embedding: `reset` + `bulk-ingest`.

---

## 2026-04-17 — Klarschiff-Session: Karpathy LLM-Wiki + Workpaper-Audit + Whitepaper-Fix

**Workpaper:** `2026-04-17-RES-WIKI-karpathy-llm-wiki-vergleich.md`  
**Themen:** Karpathy LLM-Wiki Vergleich, TST-Methodik, Decision-Promotion, Workpaper-Audit, Whitepaper-Widersprüche

**Was wurde getan:**

### Phase 1: Karpathy LLM-Wiki Vergleich
- Gist analysiert: 3-Schichten-Wiki (Raw Sources / Wiki / Schema) vs. AAMS 4-Schichten
- Adaptions-Assessment: Wiki-Lint (Mittel), Decision-Promotion (CRITICAL), kein wholesale adoption
- **TST-Methodik** (Theoretical Stress Testing) als GUIDELINE etabliert
  - `WORKING/GUIDELINES/theoretical-stress-testing.md` — erste Guideline überhaupt
  - Regel: "Kein Workpaper mit Architektur-Empfehlungen darf geschlossen werden, ohne TST"
  - 3 Core-Gaps dokumentiert (CG-1 Decision-Kompoundierung, CG-2 Upgrade-Transparenz, CG-3 Lint-Äquivalent)

### Phase 2: Issues erstellt
- **Issue #48** — Decision-Kompoundierungs-Leck (CRITICAL): Architektur-Decisions versickern in Workpapers
- **Issue #49** — Upgrade-Transparenz fehlt (HIGH): CHANGELOG, Git-Tags, MIGRATION.md

### Phase 3: Klarschiff — Workpaper-Audit
- 17 offene Workpapers analysiert
- **6 Workpapers → closed/** (video-marketing, claude-buddy, wissen-in-zeit, WORKSPACE-field-report, WKSP-discovery, public-presence)
- 11 verbleiben: 3 BLOCKED (E-1..E-5), 4 fast fertig, 2 extern, 2 aktiv

### Phase 4: Whitepaper-Konsistenz
- 10 Prüffragen → 4 RED, 3 YELLOW, 3 GREEN
- **WP-001 aktualisiert:**
  - §5: WORKSPACE-Discovery ergänzt (implementiert 2026-04-12)
  - §8: Versioning & Upgrade-Transparenz (konzipiert, nicht implementiert)
  - §9: Decision-Promotion als neues Konzept
  - §10: Cross-Referenzen WP-001↔WP-002↔WP-003↔WP-004
  - §11: Aktueller Stand auf 2026-04-17 (Issues, GUIDELINES/, Versioning-Status)
  - ⚠️ Pending-Decision-Marker: "Spezifikation" → "Agent Contract" (E-1..E-5 offen)
- **INDEX.md aktualisiert:**
  - WP-001 Stand + Themen aktualisiert
  - Cross-Referenzen-Block hinzugefügt
  - Pending-Decisions-Block hinzugefügt
  - Stand: 2026-04-17

### Phase 5: GitHub Issues bestätigt
- Issues #22, #23, #24, #39, #42, #44 — alle waren bereits geschlossen (konsistent mit Triage-Empfehlung)

**Offene Issues:** #26 (Security, Backlog), #41 (MantisClaw), #43 (RFC Tracker), #48 (Decision-Leck), #49 (Upgrade-Transparenz)

| # | Datum | Typ | Datei | Inhalt |
|---|---|---|---|---|
| 100 | 2026-04-17 | RESEARCH | `WORKING/WORKPAPER/2026-04-17-RES-WIKI-karpathy-llm-wiki-vergleich.md` | Karpathy LLM-Wiki vs. AAMS Vergleich. 3-Schichten → 4-Schichten Mapping. Adaptions-Assessment: Decision-Promotion CRITICAL, Wiki-Lint Mittel. |
| 101 | 2026-04-17 | GUIDELINE | `WORKING/GUIDELINES/theoretical-stress-testing.md` | TST-Methodik: Theoretical Stress Testing als Pflichtschritt für Architektur-Workpapers. 3 Core-Gaps (Decision-Kompoundierung, Upgrade-Transparenz, Lint-Äquivalent). |
| 102 | 2026-04-17 | GITHUB | Issues #48, #49 | #48 Decision-Kompoundierungs-Leck (CRITICAL), #49 Upgrade-Transparenz (HIGH). Beide aus TST-Stress-Tests entstanden. |
| 103 | 2026-04-17 | AUDIT | `WORKING/WORKPAPER/` | 17 offene Workpapers auditiert. 6 → closed/. 11 verbleiben (3 BLOCKED, 4 fast fertig, 2 extern, 2 aktiv). |
| 104 | 2026-04-17 | WHITEPAPER | `WORKING/WHITEPAPER/WP-001-aams-overview.md` | Majored Update: WORKSPACE-Discovery §5, Versioning §8, Decision-Promotion §9, Cross-Refs §10, Stand §11. Pending-Decision für Spec→Contract. |
| 105 | 2026-04-17 | WHITEPAPER | `WORKING/WHITEPAPER/INDEX.md` | Cross-Referenzen + Pending-Decisions-Block. WP-001 Stand auf 2026-04-17. |
| 106 | 2026-04-17 | DIARY | `WORKING/DIARY/2026-04.md` | Klarschiff-Session Eintrag: alle Aktionen zusammengefasst. |
| 107 | 2026-04-19 | TOOL | `WORKING/TOOLS/wiki_lint.py` | Wiki-Lint Health-Check: 7 Checks (L1 Index-Konsistenz, L2 Stale WPs, L3 Naming-Schema, L4 Decision-Promotion, L5 Cross-Refs, L6 LTM-Nummerierung, L7 Pending-Decisions). Erstlauf: 0 Errors, 12 Warnings, 2 Infos. ~3k Tokens. Inspiriert von Karpathy LLM-Wiki Lint-Konzept. |
| 108 | 2026-04-19 | ARCHITECTURE | `READ-AGENT.md` | Decision-Promotion als Schritt 2 in on_session_end verankert. Regel: Kein Workpaper darf mit ungelösten [PROMOTE→WP-xxx] Tags geschlossen werden. wiki_lint.py als optionaler Schritt 7. Current Status aktualisiert (LTM 106+, Issues, Guidelines, Tools). |

---

## Nächster geplanter Ingest

Nach Abschluss der laufenden Session.

| # | Datum | Typ | Datei | Inhalt |
|---|---|---|---|---|
| 116 | 2026-04-29 | ANALYSE | `WORKING/WORKPAPER/2026-04-29-projekt-analyse.md` | Absolute Projekt-Analyse: 8 offene Issues, 11 aktive Workpapers, 6 Whitepapers. Health-Score 5/10. Core-Gaps: #48 teilweise, #49 teilweise, #43 blockiert (E-1..E-5), #50/#51 neu. Decisions D1-D7. GitHub-API-Token invalid. |
| 117 | 2026-04-29 | RFCT | `.agent.json` + AGENT_SCHEMA.json + AGENT.json + CHANGELOG.md + READ-AGENT.md + INDEX.md | Phase 1 RFCT: AAMS/2.0 Manifest-Prinzip. `_contract: AAMS/2.0` + deprecated `_spec` + `topic_registry` + `agent_conventions` (descriptive). Schema: `_contract` required, `_spec` deprecated. CHANGELOG.md v2.0.0. READ-AGENT.md Current Status + Topic Registry. INDEX.md Pending Decisions + Manifest-Prinzip. |
| 118 | 2026-04-29 | RFCT | `AGENTS.md` + `copilot-instructions.md` + `CONTRACT.md` + `SPEC.md` (Stub) + `MIGRATION.md` | Phase 2 RFCT: AGENTS.md + copilot-instructions.md Tagline-Updates. CONTRACT.md (Stub) + SPEC.md (Stub). MIGRATION.md v1.x→v2.0. |
| 119 | 2026-04-29 | RFCT | STRAT + RFCT Workpapers → closed/ | E-1..E-5 beschlossen. Phase 1 RFCT abgeschlossen. STRAT + RFCT Workpapers archiviert. |
| 120 | 2026-04-29 | RFCT | WP-001, WP-002, WP-003, WP-004, INDEX.md | Phase 2 RFCT: Alle Whitepapers "Specification" → "Agent Manifest". WP-001 Header + Pending Decision + Current Status + governance + agent_contract. WP-002 Header + "AAMS declares" → "AAMS describes". WP-003 Header + AAMS-Spec → AAMS-Contract. WP-004 Header + Reference. INDEX.md Header + Pending Decisions. WP-001 INDEX vs. Inhalt Widerspruch gelöst. Manifest-Prinzip (D9) in WP-001 + INDEX.md. |
| 121 | 2026-04-29 | RFCT | README.md, README.en.md, README.zh.md, reference/README-DE.md, docs/outreach | Phase 2 RFCT: Alle READMEs + Outreach "Specification" → "Agent Manifest". README.md: "Spezifikation" → "Manifest", Tagline, Kernsatz. README.en.md: "Specification" → "Agent Manifest", Header → "Contract Reference". README.zh.md: "Specification" → "Agent Manifest". reference/README-DE.md: "Specification" → "Agent Manifest". Outreach-Templates aktualisiert. |
| 122 | 2026-04-29 | COMMIT | `93322b7` | feat: AAMS/2.0 — Spec→Contract reorientation + Phase 1+2 RFCT (60 files changed). `.agent.json` + AGENT_SCHEMA.json + AGENT.json + CHANGELOG.md + MIGRATION.md + CONTRACT.md + SPEC.md (Stub) + alle Whitepapers + READMEs + INDEX + Outreach + READ-AGENT.md + AGENTS.md + copilot-instructions.md. Manifest-Prinzip (D9) verankert. 8 Workpapers → closed/. wiki_lint.py + validate_tools.py + theoretical-stress-testing.md. Docs cleanup. |
| 123 | 2026-04-29 | COMMIT | `943928b` | feat: add .aams-version state file for upgrade detection. Minimal JSON state file tracking AAMS installation version, date, workspace root. Enables on_update handler to detect version bumps. |
| 124 | 2026-04-29 | SEC | `file_safety` | Issue #50 konzipiert + implementiert. `file_safety` in `.agent.json` + AGENT.json + AGENT_SCHEMA.json + CONTRACT.md. Manifest-Prinzip (D9): beschreibend, nicht preskriptiv. Git history als Quelle der Wahrheit. Workpaper → closed/. |
| 125 | 2026-04-29 | ARCH | `skills` | Issue #51 konzipiert + implementiert. `skills` in `.agent.json` + AGENT.json + AGENT_SCHEMA.json + CONTRACT.md. Manifest-Prinzip (D9): beschreibend, nicht preskriptiv. Global → Lokal: Quelle → Feinschliff. Workpaper → closed/. |
 | 126 | 2026-04-29 | SEC | `security` | Issue #26 konzipiert + implementiert. `security`-Sektion für Trust-Portabilität in `.agent.json` + AGENT.json + AGENT_SCHEMA.json + CONTRACT.md. Manifest-Prinzip (D9): optional, beschreibend, keine Enforcement. Trust-Portabilität als Feature. Workpaper → closed/. |
 | 127 | 2026-04-30 | ARCH | WP-005 | Workpaper-Lifecycle erweitert: active → observe → closed. `WORKING/WORKPAPER/observe/` erstellt. Drei Zustände: active (abgearbeitet), observe (beobachten/waiting), closed (finished). `.agent.json` + READ-AGENT.md + INDEX.md aktualisiert. |
 | 128 | 2026-04-30 | ARCH | WP-006 | README-Konsistenz: Reality Check — 9+ divergenzen zwischen READMEs (DE/EN/ZH) und disk. README.md: AAMS/2.0 + Manifest-Prinzip + observe/ + topic_registry + Current Status + CONTRACT.md reference. README.en.md: same fixes. README.zh.md: "规范" → Manifest + same fixes. READ-AGENT.md Current Status updated. INDEX.md footer updated. CHANGELOG.md [Unreleased] updated. |
 | 129 | 2026-04-30 | ARCH | Cleanup | 3 Workpapers → closed/ (versioning-system, field-report-analyse, three-tests) | Active: 2, Observe: 3, Closed: 50 |
 | 130 | 2026-04-30 | ARCH | Guidelines | **12 Guidelines** created: Documentation Model, Naming Schema, Workpaper Lifecycle, Decision-Promotion, File Protocol, LTM Rules, Topic Registry, Wiki Lint, AAMS Doctor, Git Safety, README Consistency, Diary Format | Health-Score 9/10 |
 | 131 | 2026-04-30 | ARCH | WP-007 | SPEC.md/CONTRACT.md circular stub problem dokumentiert. Beide Stubs, circular redirect. README now references CONTRACT.md. → WP-007-spec-contract-stub.md |
 | 132 | 2026-04-30 | ARCH | WP-008 | Health-Score 10/10: `.aams-version` updated, Git-Tag v2.1.0 created, Issue #45 closed (duplikat). README-Konsistenz **done**. 12 Guidelines **done**. |
 | 133 | 2026-04-30 | README | `docs/presenter-image.png` | presenter-image.png in README.md + README.en.md (Live Demo section) | Commit `b52ea5e` |
 | 134 | 2026-04-30 | LTM | `ltm-index.md` | LTM ingest — entry 134. LTM: 133 entries (audit-log + ChromaDB). Health-Score 10/10. Whitepapers 8 + INDEX.md. Guidelines 12. Active: 2, Observe: 3, Closed: 51. Git-Tag v2.1.0 (10 Commits). |
 | 135 | 2026-04-30 | ARCH | git-cleanup | Git status cleanup — .agent.json + workpaper moves + docs/presenter-image.png | Commit `e43e252` |
 | 136 | 2026-04-30 | ARCH | Naming Schema | Whitepapers → WH-*, Workpapers → WP-* — alle Whitepapers umbenannt (WH-001..WH-008), alle Workpapers umbenannt (WP-DATE-*) | `.agent.json` + `READ-AGENT.md` + `INDEX.md` + `naming-schema.md` + CHANGELOG.md update |
 | 137 | 2026-04-30 | ARCH | Version v2.2.0 | WH-001 stale references fixed, WH-008 stale data fixed, Diary format updated, `.agent.json` `_version_date` updated, CHANGELOG.md v2.2.0 section, Git-Tag v2.2.0 | Health-Score 10/10 |
 | 138 | 2026-07-06 | ANALYSE | `WORKING/WORKPAPER/2026-07-06-session-start-analyse.md` | Session-Start-Analyse nach ~2.5 Monaten Pause. GitHub: ogelry/AAMS — 9 offene Issues, Remote-URL MISMATCH (DEVmatrose), Health-Score 7/10. 5 P0/P1 Patches identifiziert. |
 | 139 | 2026-07-06 | WHITEPAPER | `WORKING/WHITEPAPER/WH-009-guard-pattern.md` | WH-009 Guard-Pattern: Zwei-Ebenen-Modell (AAMS beschreibt Pattern, Implementierung = local_adaptation). Drei Check-Ebenen (manifest_read, workpaper_open, tools_gated). Tool-agnostic. Fehlerformate beschreibend. AGENT_SCHEMA.json guard-Schema. |
 | 140 | 2026-07-06 | WHITEPAPER | `WORKING/WHITEPAPER/INDEX.md` + `.agent.json` + `AGENT_SCHEMA.json` + `CONTRACT.md` + `READ-AGENT.md` | WH-009 in INDEX.md + Manifest synchronisiert. .agent.json guard-Sektion. AGENT_SCHEMA.json guard-Schema. CONTRACT.md guard-Erwähnung. READ-AGENT.md Current Status (Whitepapers 9, guard). |
