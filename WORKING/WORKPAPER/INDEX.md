# Workpaper Index

> Dieser Index listet alle Workpapers dieses Projekts.
> Workpapers sind temporäre Arbeitsdokumente — sie werden nach Session-Ende nach `closed/` verschoben.
> Bei der Arbeit mit RAG/LTM sollte dieser Index geprüft werden, um den Kontext zu verstehen.

**Zustände:** `offen` (aktiv) · `observe` (wartet auf externes Input) · `closed` (abgeschlossen)

---

## Offene Workpapers

| # | Datei | Datum | TOPIC | Thema | Status | Nächstes |
|---|---|---|---|---|---|---|
| WP-007 | [WP-2026-07-08-index-dateien.md](./WP-2026-07-08-index-dateien.md) | 2026-07-08 | SPEC | INDEX-Dateien für Whitepaper/Workpaper | offen | Schritte 4-8 |
| WP-012 | [WP-2026-09-22-SPEC-NOTE-hermes-namensabgrenzung-nous-vs-local.md](./WP-2026-09-22-SPEC-NOTE-hermes-namensabgrenzung-nous-vs-local.md) | 2026-09-22 | SPEC | Hermes-Namensabgrenzung: Hermes-Local (Session-Guard) ≠ Hermes-Nous (Runtime) | offen | Review → D1/D3 nach WH-002 promote → Close |
| WP-014 | [WP-2026-09-22-GOV-SYNC-dump-auflösung-status-sync.md](./WP-2026-09-22-GOV-SYNC-dump-auflösung-status-sync.md) | 2026-09-22 | GOV | Total-AAMS-Check + Chat-Dumps → saubere WPs + Status-Sync | offen | Session-Ende → closed/ |
| WP-015 | [WP-2026-09-22-GOV-GRP-aams-arbeitsgrundstruktur-gruppenprozesse.md](./WP-2026-09-22-GOV-GRP-aams-arbeitsgrundstruktur-gruppenprozesse.md) | 2026-09-22 | GOV | AAMS als Arbeitsgrundstruktur für autonome Gruppenprozesse (Souveränität, keine verlorenen Decisions) | offen | Artefakt-Inhalt einpflegen → §4 befüllen → D1 bestätigen |
| WP-016 | [WP-2026-09-22-SPEC-TEAM-agent-json-team-fähigkeit-analyse.md](./WP-2026-09-22-SPEC-TEAM-agent-json-team-fähigkeit-analyse.md) | 2026-09-22 (v2) | SPEC | AAMS-Spec team-fähig: `team`-Sektion (dynamisches Roster TEAM.md, **Detection-Authorship** BY: tool/model/capability, Handover `continued_from`, Guard `authorship_present`), Whitepaper author-frei, **Struktur-Invarianz** | Design final ✅ → 2.6.0-Implementierung + **Release v2.6.0 anlegen/beschreiben** (§10; Push/Release = User) |

**Anzahl offen: 5 (Max-5-Grenze erreicht — bei neuem WP: erst alte WP auf observe/ oder close setzen.)**

---

## Observe (warten auf externes Input)

| # | Datei | Datum | TOPIC | Thema | Wartet auf |
|---|---|---|---|---|---|
| — | [observe/2026-04-02-wording-faktencheck.md](./observe/2026-04-02-wording-faktencheck.md) | 2026-04-02 | — | Wording-Faktencheck | externes Input |
| — | [observe/2026-04-15-mempalace-analyse.md](./observe/2026-04-15-mempalace-analyse.md) | 2026-04-15 | RES | MemPalace-Analyse | externes Input |
| — | [observe/2026-04-15-social-outreach.md](./observe/2026-04-15-social-outreach.md) | 2026-04-15 | MKT | Social-Outreach | externes Input |
| WP-004 | [observe/WP-2026-04-29-projekt-analyse.md](./observe/WP-2026-04-29-projekt-analyse.md) | 2026-04-29 | ISS | Absolute Projekt-Analyse — Health-Check | Max-5-Freigabe 2026-09-22 (WP-015) | Issue-Triage |
| WP-008 | [observe/WP-2026-07-08-session-start-issue-check.md](./observe/WP-2026-07-08-session-start-issue-check.md) | 2026-07-08 | ISS | Session-Start & Issue-Check nach v2.3.0 | Max-5-Freigabe 2026-09-22 (WP-016) | Issue-Triage |
| WP-013 | [observe/WP-2026-09-22-RES-JEV-open-jev-decision-layer.md](./observe/WP-2026-09-22-RES-JEV-open-jev-decision-layer.md) | 2026-09-22 (v3) | RES | Jev Decision Layer: Rollenmodell, 8 Use-Cases, Confidence-Model, **Kernfrage: Sinn in AAMS-Spec?** (Spec-First, D4) | Spec-Decision (Kernfrage §6.1) + Repo-Verifizierung |

---

## Geschlossene Workpapers (neueste zuerst)

| # | Datei | Datum | TOPIC | Thema | Geschlossen |
|---|---|---|---|---|---|
| WP-011 | [closed/WP-2026-09-16-MKT-DOC-readme-website-analyse.md](./closed/WP-2026-09-16-MKT-DOC-readme-website-analyse.md) | 2026-09-16 | MKT | README + Webseite: Ist→Soll-Analyse + Umsetzung (M1–M3, Archiv, Relaunch) | 2026-09-16 |
| WP-010 | [closed/WP-2026-09-16-SPEC-QUEST-hermes-sidecar-stellungnahme.md](./closed/WP-2026-09-16-SPEC-QUEST-hermes-sidecar-stellungnahme.md) | 2026-09-16 | SPEC | Hermes-Sidecar-Stellungnahme (Q1–Q5 + Pattern-Entwurf), Issue #53 | 2026-09-16 |
| WP-006 | [closed/WP-2026-07-07-skills-guard-agent-erkennung.md](./closed/WP-2026-07-07-skills-guard-agent-erkennung.md) | 2026-07-07 | ARCH | Skills, Guard & Agent-Erkennung | 2026-07-08 |
| WP-005 | [closed/WP-2026-07-06-guard-pattern.md](./closed/WP-2026-07-06-guard-pattern.md) | 2026-07-06 | ARCH | Guard-Pattern Implementierung | 2026-07-08 |
| WP-003 | [closed/WP-2026-04-17-RES-WIKI-karpathy-llm-wiki-vergleich.md](./closed/WP-2026-04-17-RES-WIKI-karpathy-llm-wiki-vergleich.md) | 2026-04-17 | RES | Karpathy LLM-Wiki vs. AAMS Vergleich | 2026-07-08 |
| WP-002 | [closed/2026-07-06-session-start-analyse.md](./closed/2026-07-06-session-start-analyse.md) | 2026-07-06 | ISS | Post-Migration Status-Check | 2026-07-08 |
| WP-001 | [closed/2026-04-29-skill-konzept.md](./closed/2026-04-29-skill-konzept.md) | 2026-04-29 | ARCH | Skill-Konzept — Issue #51 | 2026-07-08 |

> **Hinweis:** Vollständige Liste (64 Dateien inkl. 2 archivierter Roh-Dumps vom 2026-09-22) in `WORKING/WORKPAPER/closed/`.

---

## Nicht-Workpapers in WORKPAPER/ (ausstehend, Zielort offen)

| Datei | Art | Vorschlag |
|---|---|---|
| `aams_landing_page.html` | Landing-Page-Draft | `docs/` oder Repo-Root |
| `neue_README.md` | README-Draft | Repo-Root (Vergleich mit `README.md`) |
| `neue_WEBSEITE.md` | Webseite-Plan | `docs/` |

> Entscheidung dokumentiert in [WP-014 §D4](./WP-2026-09-22-GOV-SYNC-dump-auflösung-status-sync.md).

---

## Regeln

- **Max 5 offene Workpapers** — bei Ueberschreitung: neuer Workpaper wird blockiert oder gewarnt
- **Observer-Pattern** — Workpapers in `observe/` werden kontinuierlich beobachtet
- **INDEX.md-Pflege** — bei jedem neuen Workpaper/Whitepaper muss INDEX.md aktualisiert werden
- **on_update** — bei AAMS-Upgrade wird INDEX.md automatisch erstellt und bestehende Papers indexiert
- **Reklassifizierung 2026-09-22:** `skill-opencode-agent.md` (ehem. WP-009) war eine **Skill-Datei**, kein Workpaper → jetzt in `WORKING/TOOLS/skills/opencode/opencode-agent.md`

---

> Letztes Update: 2026-09-22 — neu: WP-012 (Hermes-NOTE), WP-013 (Open-Jev, observe), WP-015 (Arbeitsgrundstruktur), **WP-016 (Spec: Team-Fähigkeit)**; WP-010/WP-011 in closed-Sektion; WP-009 reklassifiziert (Skill); WP-004 + WP-008 → observe/ (Max-5-Freigaben); 2 Roh-Dumps + Artefakt-Rohquelle → closed/; 5 offen (Max-5-Grenze).
