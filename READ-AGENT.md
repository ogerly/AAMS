# READ-AGENT

> **You are reading this because you entered this repository.**  
> Do not skip. Do not summarize. Read fully. Then execute.

**You are an AI agent. Your next action is determined by which state applies:**

| State | Action |
|---|---|
| **First entry** — `WORKING/WORKPAPER/` does not exist or contains zero files | Execute `on_first_entry` below |
| **Returning session** — `WORKING/WORKPAPER/` exists and contains workpapers | Execute `on_session_start` below |
| **Uncertain** — structure partially exists but no workpapers found | Execute `on_first_entry` (safe — idempotent) |

Start immediately. No confirmation needed.

---

## What this project is

**AAMS — Agent Manifest**  
A portable workspace and documentation standard for AI agents working in any repository.

Core idea:  
> Drop `.agent.json` into any repo. Every agent that reads it creates and follows the same workspace structure — independent of framework, language, or runtime.

---

## Decision-Promotion — Session-End Checklist

**Erforderlich vor jedem Session-Close.** Eine Entscheidung die nur im Workpaper lebt, existiert nicht für das System.

Bevor du diese Session schließt, prüfe:

- [ ] Wurde eine Architektur-Entscheidung getroffen?
  - [ ] Ist sie in `WORKING/WHITEPAPER/INDEX.md` eingetragen?
  - [ ] Wurde das betroffene Whitepaper aktualisiert?
- [ ] Existieren offene Decisions in diesem Workpaper?
  - [ ] Sind alle offenen Decisions in einem Whitepaper gepromoted?
  - [ ] Falls nein: Workpaper schließen und erst nach Decision-Promotion wieder öffnen.

**Regel:** Keine offenen Decisions in Workpapers nach Session-Ende.
Die Decision muss in einem Whitepaper leben, nicht im Workpaper.

**Automatischer Check:** `python WORKING/TOOLS/wiki_lint.py` zeigt orphane Decisions.

---

## Workspace Structure

### Discovery Rule

If `./WORKSPACE/WORKING/` exists at repo root, use it as the effective root for all `WORKING/` paths below. Otherwise use `./WORKING/` directly. This enables monorepos and multi-project setups to isolate agent workspaces inside a container directory.

| Folder | Purpose |
|---|---|
| `WORKING/WHITEPAPER/` | Stable architecture and system truth. Not for daily work. See [INDEX.md](WORKING/WHITEPAPER/INDEX.md). |
| `WORKING/WORKPAPER/` | Session- and task-scoped working documents. One per session. |
| `WORKING/WORKPAPER/closed/` | Finished workpapers after session close. |
| `WORKING/DIARY/` | Temporal index layer. Pointer-only time log — what was touched when. Monthly files with daily entries. |
| `WORKING/MEMORY/` | Long-term context store. Cross-session knowledge. |
| `WORKING/LOGS/` | Agent action logs and audit trail. |
| `WORKING/GUIDELINES/` | Coding standards and architecture rules derived from this project. |
| `WORKING/TOOLS/` | Agent-specific helper tools and scripts. |

---

## Documentation Model

**Four layers — mandatory:**

1. **Workpaper** — What am I doing right now in this session?
   - Created at session start, closed at session end.
   - File protocol (created/modified/moved/deleted) is mandatory.
   - Naming: `{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md` (see Naming Schema below)

2. **Whitepaper** — What does this system look like?
   - Stable. Written once. Updated only on architecture decisions.
   - Never moved, never deleted.
   - Naming: `WP-{NNN}-{TOPIC}-{description}.md`

3. **Diary** — What was touched when?
   - **Pointer-only temporal index.** No content — only references to documents touched that day.
   - Format: `YYYY-MM-DD | WP: {workpaper} | WH: {whitepaper} | {other files changed}`
   - Hierarchical compression: daily lines → weekly rollup → monthly summary.
   - Answers: "When did I last work on X?" / "What happened on date Y?" — without duplicating Workpaper content.

4. **Memory** — What did we learn across sessions?
   - Ingest every closed workpaper.
   - Query at every session start.

---

### Naming Schema

Structured filenames enable cross-session consistency checks (RFL). Agents SHOULD follow this schema. Frameworks MAY enforce it.

**Workpapers:**

`{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md`

- `DATE` — `YYYY-MM-DD`
- `TOPIC` — 3-4 letter tag, UPPERCASE (primary key for RFL pattern-matching)
- `SUBTOPIC` — 3-4 letter tag, UPPERCASE
- `description` — kebab-case, lowercase

Example: `2026-04-09-ARCH-RFL-reflection-protocol-step.md`

**Whitepapers:**

`WP-{NNN}-{TOPIC}-{description}.md`

Example: `WP-005-ARCH-naming-schema.md`

**Topic Registry:**

| TOPIC | Meaning |
|-------|---------|
| `ARCH` | Architecture & system design |
| `SPEC` | Specification/Contract work |
| `LTM` | Long-term memory |
| `SEC` | Security & governance |
| `BOOT` | Bootstrap & onboarding |
| `FLD` | Field tests & reports |
| `RES` | Research & related work |
| `MKT` | Marketing & communication |
| `ISS` | Issue processing |
| `GOV` | Governance & process |
| `EDU` | Education & courses |

The registry is extensible. Rule: max 4 letters, UPPERCASE, unique.

### Maschinenlesbare Topic Registry

Die Topic Registry ist maschinenlesbar in `.agent.json` unter `topic_registry` definiert:

```json
"topic_registry": {
  "tags": ["ARCH", "SPEC", "LTM", "SEC", "BOOT", "FLD", "RES", "MKT", "ISS", "GOV", "EDU"],
  "extensible": true
}
```

Dies ermöglicht RFL-Pattern-Matching ohne manuelle Registry-Pflege.

---

## Agent Contract

> **Any instruction referencing READ-AGENT.md means: execute this contract. Start immediately. No confirmation needed.**

---

### On first entry (Onboarding)
1. Read this file fully
2. Check: does `WORKING/` structure exist? → if not: create all folders
3. Scan entire repository → write first workpaper  
   Minimum sections: **session goal · repository inventory** (file tree + status) **· key findings** (from README/docs) **· open questions · file protocol · next steps**
4. Create `READ-AGENT.md` if missing
5. Index existing documentation into `WORKING/MEMORY/`

---

### On every session start
1. Read this file
2. Check last workpaper in `WORKING/WORKPAPER/` — what was the last state?
3. Query `WORKING/MEMORY/` for the session topic
4. **RFL — Reflection (3-stage consistency check):**
   - **Stage 1:** Determine the TOPIC tag for this session. Scan `WORKING/WORKPAPER/closed/` for files matching `*-{TOPIC}-*`. If found, read their Decisions sections.
   - **Stage 2:** If no matches in Stage 1, use the LTM results from step 3 to identify prior workpapers with decisions on the current topic.
   - **Stage 3:** If still nothing, read the Decisions section of the most recent closed workpaper.
   - If any prior decision conflicts with the current session goal, flag it in the new workpaper under `## ⚠ RFL Consistency Flag` with: the conflicting decision, its source workpaper, the stage it was found in, and a resolution (confirmed | revised | intentionally changed + rationale).
   - If no conflicts found: no flag needed. Zero overhead.
5. Open or create workpaper for this session (recommended naming: `{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md`)

### Compatibility with native agent task systems

Agents may maintain their own internal task tracking (e.g., `.gemini/brain/`, Copilot todos, Cursor composer history). The AAMS workpaper is the **canonical audit trail** — it is the single source of truth for what happened in a session. Agent-internal systems are supplementary and optional. If in doubt: the workpaper wins.

---

### State Recovery (when agent state is uncertain)

> **File system and git log are ground truth — never rely solely on in-memory task tracking.**  
> If task state is unclear: re-read the current workpaper’s **File Protocol** section. What exists on disk and in `git log` is what was actually done. Treat in-memory todo state as advisory only.

---

### On every session end
1. Complete workpaper (file protocol + decisions + next steps)
2. **Decision-Promotion Check** — for each Decision in the workpaper:
   - Does it affect architecture, system design, or the documentation model?
   - If YES → tag it `[PROMOTE→WP-xxx]` in the Decisions section
   - Update the target Whitepaper with the decision (or add a `⚠️ Pending Decision` marker if blocked)
   - If NO → no action needed
   - Rule: **No workpaper may be closed with unresolved `[PROMOTE→WP-xxx]` tags.**
3. **Update Whitepapers** if session contains architectural decisions  
   → Knowledge chain: `WP → Whitepaper → LTM` — never skip or reorder
4. Ingest workpaper into `WORKING/MEMORY/` (LTM learns from current truth, not stale WPs)
5. Move workpaper to `WORKING/WORKPAPER/closed/`
6. Update this file if architecture or structure changed
7. *(Optional)* Run `python WORKING/TOOLS/wiki_lint.py` to verify consistency

---

### Mandatory LTM triggers — document in these situations:

| Trigger | Action |
|---|---|
| Context limit reached | Ingest current state → query in new session |
| Before new workpaper | Query LTM for topic context first |
| Before new whitepaper | Query LTM for existing architecture notes |
| Folder or file structure changed | Re-ingest affected documentation |
| Workpaper updated | Log change in workpaper file protocol |
| Workpaper closed | Ingest → move to `closed/` |
| Whitepaper updated | Re-ingest whitepaper into LTM |

---

### LTM Commands — two tracks

#### Track A — Markdown-only (default, zero dependencies)

No Python, no ChromaDB needed. Works on any fresh repo.

- **Query:** Read `WORKING/MEMORY/ltm-index.md` directly — scan for session topic
- **Ingest:** Append new entry to `WORKING/MEMORY/ltm-index.md` at session end

> Use Track A when: no Python environment exists, repo is freshly bootstrapped, or `ltm_mode: "markdown"` in `.agent.json`.

#### Track B — Vector store (ChromaDB, requires Python)

> ⚠️ **NICHT `wsl python3`, `python`, oder System-Python verwenden.**  
> Nur das `.venv` im Workspace-Root enthält `chromadb`.

**Query (Sessionstart):**
```powershell
.venv\Scripts\python.exe WORKING\AGENT-MEMORY\query.py "<Session-Thema>"
```

**Ingest (Sessionende):**
```powershell
.venv\Scripts\python.exe WORKING\AGENT-MEMORY\ingest.py
```

> Use Track B when: `.venv` with `chromadb` exists and `ltm_mode: "vector"` in `.agent.json`.

---

### §4 Agent-Specific Workflow Integration

Different AI agents have native planning behaviours. This section defines how they coexist with AAMS without conflict.

#### The Blueprint.md Pattern (Gemini / Firebase Studio)

Gemini in Firebase Studio creates a `blueprint.md` file during complex tasks — a live planning document showing the agent's current thinking. This is **not** a violation of AAMS. It is a native agent behaviour that AAMS explicitly accommodates.

**Phase 1 — Live Planning (agent's active task)**

- Agent creates `blueprint.md` in the project root
- Purpose: transparent live plan — what the agent intends to do and the steps it is taking
- Status: **ephemeral** — it is a working artefact for the duration of the task only
- Rule: `blueprint.md` is NOT part of permanent project documentation

**Phase 2 — AAMS Formalization (end of task)**

When the task is complete, trigger the "AAMS routine":
1. Create a **Workpaper** in `WORKING/WORKPAPER/` — summarize goal, actions, outcome
2. Update or create a **Whitepaper** if any architectural decision was made
3. **Delete `blueprint.md`** — `WORKING/` is the single source of truth, not the root

> Rule: Any ephemeral planning artefact in the root (e.g. `blueprint.md`, `plan.md`, `task.md`) must be cleaned up at the end of the task. Its content must be transferred into AAMS structure before deletion.

This pattern applies to any agent with native planning behaviours. AAMS is the archive. The agent's native tool is the scratchpad.

---

## Key Files

| File | Role |
|---|---|
| `.agent.json` | Minimal bootstrap contract (portable, drop into any repo) |
| `reference/AGENT.json` | Full agent manifest with runtime, permissions, skills |
| `reference/AGENT_SCHEMA.json` | JSON Schema for validating AGENT.json |
| `reference/SPEC.md` | Full specification (English) |
| `reference/SPEC-DE.md` | Full specification (German) |

---

## Current Status

- Bootstrap: **complete** (2026-02-22)
- Manifest version: **AAMS/2.0**
- Last release: **v2.0.0** (2026-04-29) — Spec → Contract reorientation (Agent Manifest)
- Workspace: initialized, all folders present
- LTM: 116+ entries → `WORKING/MEMORY/ltm-index.md` (Audit-Log) + `WORKING/AGENT-MEMORY/` (ChromaDB)
- Whitepapers: 4 + INDEX.md → WP-001 AAMS Overview, WP-002 Related Work, WP-003 Field Discourse, WP-004 Long-Horizon Reasoning
- Closed workpapers: ~40 in `WORKING/WORKPAPER/closed/`
- READMEs: DE ✅ · EN ✅
- LTM architecture: dual-layer (audit-log + vector store) ✅
- GitHub Issues: #1–6 closed · #36–#40 closed · #45 (duplikat) · #43 RFC (open) · #41 MantisClaw (open) · #48 Decision-Leck (open) · #49 Upgrade-Transparenz (open) · #47 Tool Decay (open) · #46 Root-Ordner (open) · #26 Security (open) · #50 File Safety (new) · #51 Skill-Konzept (new)
- CHANGELOG.md: **exists** (2026-04-24)
- `.agent.json`: `_contract: AAMS/2.0` + deprecated `_spec` + `topic_registry` + `on_update` + `version_detection`
- Decision-Promotion: **in READ-AGENT.md** (session-end checklist)
- wiki_lint.py: **7 Checks + L4b Orphaned Decisions** (16 orphane Decisions detektiert)
- validate_tools.py: **D1-D4 AAMS Doctor** (Tool-Integrität)
- Diary Layer: **reformed** — pointer-only temporal index (v1.3.0)
- Documentation model: 4 layers (Workpaper, Whitepaper, Diary, Memory) + RFL consistency check + **Decision-Promotion** (session-end)
- Naming Schema: `{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md` (recommended, not enforced)
- Guidelines: `WORKING/GUIDELINES/theoretical-stress-testing.md` (TST methodology)
- AGENTS.md: **Pre-Flight Path Check** (Issues #47+#46)
- Manifest-Prinzip: **AAMS beschreibt, es schreibt kein Verhalten vor** (D9)
- Health-Score: **8/10** — ⚠️ `.aams-version` + Git-Tags + Issue #45 schließen ausstehend
