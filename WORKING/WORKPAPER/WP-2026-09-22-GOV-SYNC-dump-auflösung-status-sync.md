# WP-2026-09-22-GOV-SYNC-dump-auflösung-status-sync

**Status:** open
**Datum:** 2026-09-22
**TOPIC/SUBTOPIC:** GOV/SYNC
**Session-Ziel:** (1) Die zwei ungeprüften Chat-Dumps in WORKPAPER/ in saubere Workpapers auflösen. (2) Vollständiger AAMS-Status-Check des AAMS-Tools selbst. (3) Synchronisation: WORKPAPER/INDEX.md, DIARY, LTM, READ-AGENT.md, .agent.json.

**Bezug:**
- Auftrag: „formuliere saubere workpaper von den dumps. und dann synchronisieren."
- Vorheriger Stand: Session 2026-09-16 (WP-010/WP-011 closed, LTM #142, Commits bis `31a2975`)

---

## 1. session_goal

1. Hermes-Dump → sauberes SPEC/NOTE-Workpaper (Decisions D1–D3 erhalten).
2. Jev-Dump → sauberes RES/JEV-Workpaper in `observe/` (Claims als unverifiziert markiert).
3. Skill-Datei `skill-opencode-agent.md` an den vorgesehenen Ort `WORKING/TOOLS/skills/opencode/` verschieben.
4. Roh-Dumps nach `closed/` archivieren (AAMS-Regel: nie löschen, nur erstellen + verschieben).
5. INDEX.md, DIARY, LTM, READ-AGENT.md, .agent.json synchronisieren.
6. wiki_lint-Verlauf vor/nach dokumentieren.

---

## 2. Befund (Total-AAMS-Check 2026-09-22)

| Bereich | Befund |
|---|---|
| Version | `AAMS/2.4.0` (2026-07-08) — `.aams-version` = `_contract` → **kein Drift** |
| Letzte Session | 2026-09-16 sauber geschlossen (WP-010/011, LTM #142) |
| WORKPAPER/ | 2 Chat-Dumps (Hermes, Jev) + `skill-opencode-agent.md` (Skill, falscher Ort) + `aams_landing_page.html`, `neue_README.md`, `neue_WEBSEITE.md` (Dokumente, keine WPs — nicht berührt) |
| Max-5-Regel | 4 alte offene WPs (WP-004/007/008/009) → durch Einordnung der Dumps + Session-WP auf **5 offen** (Grenze eingehalten) |
| wiki_lint | 12 ERROR + 28 WARN — laut Diary 2026-09-16 alle pre-existing |
| WHITEPAPER | WH-007 in INDEX.md gelistet, **Datei fehlt im Ordner** (L1-Finding, pre-existing) |
| LTM | Stand #142 (2026-09-16) — 09-22 noch nicht ingested |
| Git | untracked: Dumps, `docs/logo1-4.png`, `docs/logo_variants.jpg`; modified: `opencode.json` (nicht von dieser Session) |
| `.agent.json` | `topic_registry`-Key doppelt definiert |

---

## 3. decisions

- **D1:** Chat-Dumps werden **nicht gelöscht**, sondern nach `closed/` archiviert (Rohinput mit Provenienz); die sauberen WPs sind die offiziellen Artefakte.
- **D2:** `skill-opencode-agent.md` ist eine **Skill-Datei**, kein Workpaper → Ziel `WORKING/TOOLS/skills/opencode/opencode-agent.md` (Konvention: `WORKING/TOOLS/skills/<tool-name>/`).
- **D3:** Jev-Recherche bleibt in `observe/`, bis Repos verifiziert + Nutzer-Entscheidung vorliegen (Claim-Herkunft Chat-Antwort).
- **D4:** `aams_landing_page.html`, `neue_README.md`, `neue_WEBSEITE.md` in WORKPAPER/ **unberührt gelassen** (Zielordner-Entscheidung bleibt Maintainer-Entscheidung — Vorschlag: Repo-Root/`docs/`).

**Decision-Promotion:** Keine Architektur-Decision dieser Session — alle 4 Decisions sind Prozess-/Hygiene-Entscheidungen, bereits in README-Konventionen (observe, Skills-Ort) verankert. Keine Whitepaper-Änderung nötig.

---

## 4. RFL

- Stage 1 (GOV-Scan closed/): WP-2026-04-30-ARCH-* (Cleanup-Sessions) — Konsistent: „Active/Observe/Closed aufräumen" war bereits etablierte Praxis. Kein Konflikt.
- Stage 1 (SPEC-Scan): WP-2026-09-16 Hermes-Sidecar — dieses WP bestätigt und erweitert (kein Konflikt, siehe WP-2026-09-22-SPEC-NOTE §8).
- Kein `## ⚠ RFL Consistency Flag` erforderlich.

---

## 5. file_protocol

| Aktion | Datei |
|---|---|
| read | `.agent.json`, `READ-AGENT.md`, `WORKING/` (alle Ebenen), `WORKPAPER/INDEX.md`, `DIARY/2026-09.md`, `MEMORY/ltm-index.md` (Tail), `WHITEPAPER/INDEX.md`, `TOOLS/skills/`, beide Roh-Dumps, `skill-opencode-agent.md` |
| create (open) | `WORKING/WORKPAPER/WP-2026-09-22-GOV-SYNC-dump-auflösung-status-sync.md` |
| create (open) | `WORKING/WORKPAPER/WP-2026-09-22-SPEC-NOTE-hermes-namensabgrenzung-nous-vs-local.md` |
| create (observe) | `WORKING/WORKPAPER/observe/WP-2026-09-22-RES-JEV-open-jev-decision-layer.md` |
| move | `WORKING/WORKPAPER/2026-09-22-SPEC-NOTE-hermes-namensabgrenzung-nous-vs-local.md` → `WORKING/WORKPAPER/closed/raw-dump-2026-09-22-hermes-namensabgrenzung-chat-dump.md` |
| move | `WORKING/WORKPAPER/open-jev-layer.md` (v1, 09:13) → `WORKING/WORKPAPER/closed/raw-dump-2026-09-22-open-jev-layer-chat-dump-v1.md` |
| move (v2, 09:30-Save) | `WORKING/WORKPAPER/open-jev-layer.md` (849 Zeilen) → `WORKING/WORKPAPER/closed/raw-dump-2026-09-22-open-jev-layer-chat-dump.md` (kanonisch) |
| update | WP-013 (JEV) → v2: User-Positionierung (Cloud-Jev = keine Option), 8 Use-Cases, D4; LTM #146 |
| update (v3) | WP-013 + WP-012: **Spec-First-Prinzip** (User, bindend), MANTIS-Proxy = Infrastruktur kein Ziel (`opencode.json`), D4 revidiert, Kernfrage = Spec-Sinn; LTM #147 |
| create (open) | `WORKING/WORKPAPER/WP-2026-09-22-GOV-GRP-aams-arbeitsgrundstruktur-gruppenprozesse.md` (WP-015) |
| move (Max-5) | `WORKING/WORKPAPER/WP-2026-04-29-projekt-analyse.md` (WP-004) → `WORKING/WORKPAPER/observe/` |
| sync | `WORKING/WORKPAPER/INDEX.md` (WP-015 offen, WP-004 observe), `DIARY/2026-09.md`, `MEMORY/ltm-index.md` (#148) |
| move | `WORKING/WORKPAPER/skill-opencode-agent.md` → `WORKING/TOOLS/skills/opencode/opencode-agent.md` |
| modify | `WORKING/WORKPAPER/INDEX.md` (Struktur: offen/observe/closed, neue WPs, WP-050-Platzhalter entfernt) |
| modify | `WORKING/DIARY/2026-09.md` (Eintrag 2026-09-22) |
| modify | `WORKING/MEMORY/ltm-index.md` (#143–#145) |
| modify | `READ-AGENT.md` (Current-Status-Zeilen: _contract 2.4.0, LTM 145, Closed-Count, WH-007-Hinweis) |
| modify | `.agent.json` (doppelter `topic_registry`-Key entfernt) |
| run | `python3 WORKING/TOOLS/wiki_lint.py` (vorher: 12 ERROR + 28 WARN → nachher: **12 ERROR + 34 WARN**; +6 = L4b Orphaned Decisions der neuen WPs (Promotion pending, by design) + L3-Naming-Drift (Linter prüft Altschema ohne `WP-`-Präfix, pre-existing)) |

---

## 6. next_steps

1. **Hermes-WP:** Maintainer-Review → D1/D3 in WH-002 promote → Close + LTM.
2. **Jev-WP:** Repos verifizieren (D3-Pflicht) → observe auflösen.
3. **Alte offene WPs:** WP-004 (2026-04-29), WP-007 (2026-07-08), WP-008 (2026-07-08) — 2–3 Monate alt, „Issue-Triage" pending → auf observe/ oder close setzen (wäre die Max-5-Polster).
4. **WH-007:** Datei fehlt, aber in WHITEPAPER/INDEX.md gelistet → entweder wiederherstellen (Git: `git log --all -- WH-007*`) oder INDEX-Zeile als „Archiviert/entfernt" markieren.
5. **Untracked-Dateien:** `docs/logo*.png`, `docs/logo_variants.jpg`, `opencode.json` (modified) → Bewerten + committen oder verwerfen (Maintainer-Entscheidung).
6. **wiki_lint-12-ERRORs:** pre-existing (L1-Pfad-Bug, L3-Altnamen, L4b 16 orphane Decisions, L6 LTM-Lücke 109–115) → eigener ISS-WP vorschlagen.
7. **Session-Ende:** dieses WP → `closed/`, LTM-Ingest #145.
