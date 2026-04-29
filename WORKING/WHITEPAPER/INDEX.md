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

> Letztes Update: 2026-04-29 — Phase 1 RFCT umgesetzt (`.agent.json`, AGENT_SCHEMA.json, AGENT.json, CHANGELOG.md, READ-AGENT.md). WP-001 selbst noch "Specification" — Phase 3 ausstehend. Manifest-Prinzip (D9): AAMS beschreibt, es schreibt kein Verhalten vor.
