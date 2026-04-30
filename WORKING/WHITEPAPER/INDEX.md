# Whitepaper Index
## AAMS — Agent Manifest

> Dieser Index listet alle Whitepapers dieses Projekts.
> Whitepapers sind stabile Dokumente. Sie werden nicht gelöscht.
> Bei Architekturentscheidungen wird das entsprechende Whitepaper aktualisiert und hier vermerkt.

---

| # | Datei | Thema | Stand | Status |
|---|---|---|---|---|
| WP-001 | [WP-001-aams-overview.md](./WP-001-aams-overview.md) | AAMS Projektübersicht — Vier-Schichten-Modell, WORKSPACE-Discovery, Bootstrap, Decision-Promotion, Versioning-Konzept, Cross-Refs | 2026-04-17 | Aktiv |
| WP-002 | [WP-002-related-work.md](./WP-002-related-work.md) | Related Work — AAMS vs. MemGPT, LangChain Memory, DVC, FIPA, per-tool conventions | 2026-02-22 | Aktiv |
| WP-003 | [WP-003-field-discourse.md](./WP-003-field-discourse.md) | Field Discourse — Kritische Bewertungen, Gegenargumente, 5+ Feldberichte (Luna-1, Testcenter, Antigravity, OpenClaw, Blind-Execution, MantisClaw), CodeRabbit-Discovery | 2026-03-31 | Aktiv |
| WP-004 | [WP-004-long-horizon-reasoning.md](./WP-004-long-horizon-reasoning.md) | Long-Horizon-Reasoning — LHR-Diagnose, AAMS als Scaffolding-Layer, Cross-Model-Validierung, Wirtschaft, v1.1-Gaps | 2026-03-27 | Aktiv |
| WP-005 | [WP-005-workpaper-lifecycle-states.md](./WP-005-workpaper-lifecycle-states.md) | Workpaper-Lifecycle — drei Zustände (active, observe, closed) | 2026-04-30 | Aktiv |
| WP-006 | [WP-006-readme-consistency.md](./WP-006-readme-consistency.md) | README-Konsistenz — DE/EN/ZH Reality Check + Fixes | 2026-04-30 | Aktiv |
| WP-007 | [WP-007-spec-contract-stub.md](./WP-007-spec-contract-stub.md) | SPEC.md/CONTRACT.md circular stub problem | 2026-04-30 | Aktiv |
| WP-008 | [WP-008-health-score-10.md](./WP-008-health-score-10.md) | Health-Score 10/10 — `.aams-version` + Git-Tags + Issue #45 | 2026-04-30 | Aktiv |

---

### Cross-Referenzen

```
WP-001 ←→ WP-003: Feldberichte → Bootstrap/Discovery-Lücken → WORKSPACE-Discovery
WP-001 ←→ WP-004: Vier-Schichten → LHR-Scaffolding
WP-002 ←→ WP-003: Related Work → Field Discourse (externe vs. interne Bewertung)
```

### Offene Widersprüche / Pending Decisions

| Bereich | Status | Tracking |
|---|---|---|
| "Spezifikation" → "Agent Manifest" | ✅ **Phase 1 + Phase 2 RFCT abgeschlossen:** `.agent.json` + AGENT_SCHEMA.json + AGENT.json + CHANGELOG.md + READ-AGENT.md + INDEX.md + MIGRATION.md + CONTRACT.md + SPEC.md (Stub) + AGENTS.md + copilot-instructions.md. **WP-001, WP-002, WP-003, WP-004 aktualisiert — "Agent Manifest" überall.** | [STRAT](./2026-04-10-AAMS-STRAT-reorientation-spec-vs-contract.md) + [RFCT](../WORKPAPER/2026-04-10-AAMS-RFCT-spec-to-contract-refactor-plan.md), Issue #43 |
| Versioning / CHANGELOG | ⚠️ CHANGELOG.md ✅, `.aams-version` ❌, Tags ❌, MIGRATION.md ✅ | Issue #49 |
| Decision-Promotion | ✅ Checklist in READ-AGENT.md ✅, wiki_lint.py L4b ✅ | Issue #48 |
| Manifest-Prinzip (D9) | ✅ **AAMS beschreibt, es schreibt kein Verhalten vor.** Imperative "MUST"-Sprache entfernt. | Workpaper `2026-04-29-projekt-analyse.md` |
| WP-001 INDEX vs. Inhalt | ✅ INDEX + WP-001 Text konsistent — "Agent Manifest" | #48 + #43 |
| File Safety (`file_safety`-Sektion) | ⚠️ Konzept aus #50 (mantis-cms) | Issue #50 |
| Skill-Konzept | ⚠️ Konzept aus #51 (Skills als kristallisiertes Wissen) | Issue #51 |

---

> Letztes Update: 2026-04-30 — WP-005 + WP-006 + WP-007 + WP-008 added. README-Konsistenz **done**. 12 Guidelines created. Health-Score **10/10**. Manifest-Prinzip (D9): AAMS describes, es schreibt kein Verhalten vor.
