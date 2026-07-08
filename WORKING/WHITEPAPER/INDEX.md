# Whitepaper Index
## AAMS — Agent Manifest

> Dieser Index listet alle Whitepapers dieses Projekts.
> Whitepapers sind stabile Dokumente. Sie werden nicht gelöscht.
> Bei Architekturentscheidungen wird das entsprechende Whitepaper aktualisiert und hier vermerkt.

---

| # | Datei | Thema | Stand | Status |
|---|---|---|---|---|
| WH-001 | [WH-001-aams-overview.md](./WH-001-aams-overview.md) | AAMS Projektübersicht — Vier-Schichten-Modell, WORKSPACE-Discovery, Bootstrap, Decision-Promotion, Versioning-Konzept, Cross-Refs | 2026-04-17 | Aktiv |
| WH-002 | [WH-002-related-work.md](./WH-002-related-work.md) | Related Work — AAMS vs. MemGPT, LangChain Memory, DVC, FIPA, per-tool conventions | 2026-02-22 | Aktiv |
| WH-003 | [WH-003-field-discourse.md](./WH-003-field-discourse.md) | Field Discourse — Kritische Bewertungen, Gegenargumente, 5+ Feldberichte (Luna-1, Testcenter, Antigravity, OpenClaw, Blind-Execution, MantisClaw), CodeRabbit-Discovery | 2026-03-31 | Aktiv |
| WH-004 | [WH-004-long-horizon-reasoning.md](./WH-004-long-horizon-reasoning.md) | Long-Horizon-Reasoning — LHR-Diagnose, AAMS als Scaffolding-Layer, Cross-Model-Validierung, Wirtschaft, v1.1-Gaps | 2026-03-27 | Aktiv |
| WH-005 | [WH-005-workpaper-lifecycle-states.md](./WH-005-workpaper-lifecycle-states.md) | Workpaper-Lifecycle — drei Zustände (active, observe, closed) | 2026-04-30 | Aktiv |
| WH-006 | [WH-006-readme-consistency.md](./WH-006-readme-consistency.md) | README-Konsistenz — DE/EN/ZH Reality Check + Fixes | 2026-04-30 | Aktiv |
| WH-007 | [WH-007-spec-contract-stub.md](./WH-007-spec-contract-stub.md) | SPEC.md/CONTRACT.md circular stub problem | 2026-04-30 | Aktiv |
| WH-008 | [WH-008-health-score-10.md](./WH-008-health-score-10.md) | Health-Score 10/10 — `.aams-version` + Git-Tags + Issue #45 | 2026-04-30 | Aktiv |
| WH-009 | [WH-009-guard-pattern.md](./WH-009-guard-pattern.md) | Guard-Pattern — Zwei-Ebenen-Modell: AAMS beschreibt Pattern (WHAT), Implementierung ist local_adaptation (HOW) | 2026-07-06 | Aktiv |
| WH-010 | [WH-010-skills.md](./WH-010-skills.md) | Skills — Kristallisiertes Wissen, Tool-Erkennung, Skill-Baukasten, Issue-Vorschlag, Absolute Neutralität, Lokale LLMs (LM Studio + qwen/qwen3.6-35b-a3b) | 2026-07-07 | Aktiv |
| WH-011 | [WH-011-upgrade-system.md](./WH-011-upgrade-system.md) | Upgrade-System — 4-Schichten-Modell: Versions-Detection, Migration, Backup+Merge, Feedback-Loop | 2026-07-08 | Aktiv |

---

### Cross-Referenzen

```
WH-001 ←→ WH-003: Feldberichte → Bootstrap/Discovery-Lücken → WORKSPACE-Discovery
WH-001 ←→ WH-004: Vier-Schichten → LHR-Scaffolding
WH-002 ←→ WH-003: Related Work → Field Discourse (externe vs. interne Bewertung)
```

### Offene Widersprüche / Pending Decisions

| Bereich | Status | Tracking |
|---|---|---|
| "Spezifikation" → "Agent Manifest" | ✅ **Phase 1 + Phase 2 RFCT abgeschlossen:** `.agent.json` + AGENT_SCHEMA.json + AGENT.json + CHANGELOG.md + READ-AGENT.md + INDEX.md + MIGRATION.md + CONTRACT.md + SPEC.md (Stub) + AGENTS.md + copilot-instructions.md. **WP-001, WP-002, WP-003, WP-004 aktualisiert — "Agent Manifest" überall.** | [STRAT](./2026-04-10-AAMS-STRAT-reorientation-spec-vs-contract.md) + [RFCT](../WORKPAPER/2026-04-10-AAMS-RFCT-spec-to-contract-refactor-plan.md), Issue #43 |
| Versioning / CHANGELOG | ⚠️ CHANGELOG.md ✅, `.aams-version` ❌, Tags ❌, MIGRATION.md ✅ | Issue #49 |
| Decision-Promotion | ✅ Checklist in READ-AGENT.md ✅, wiki_lint.py L4b ✅ | Issue #48 |
| Manifest-Prinzip (D9) | ✅ **AAMS beschreibt, es schreibt kein Verhalten vor.** Imperative "MUST"-Sprache entfernt. | Workpaper `2026-04-29-projekt-analyse.md` |
| WH-001 INDEX vs. Inhalt | ✅ INDEX + WH-001 Text konsistent — "Agent Manifest" | #48 + #43 |
| File Safety (`file_safety`-Sektion) | ⚠️ Konzept aus #50 (mantis-cms) | Issue #50 |
| Skill-Konzept | ✅ **WH-010 abgeschlossen.** Skill-Baukasten angelegt. Standard definiert (Metadaten + Struktur). Unabhängig von AAMS. | WH-010 |

---

> Letztes Update: 2026-07-07 — WH-010 Skills (Kristallisiertes Wissen, Tool-Erkennung, Skill-Baukasten, Lokale LLMs). 10 Whitepapers (WH-001..WH-010). AAMS ist neutral und standardlos. Lokale LLMs voll unterstützt (LM Studio + qwen/qwen3.6-35b-a3b). Mitmachen für alle Tools erwünscht. Guard nur als Vorschlag.
