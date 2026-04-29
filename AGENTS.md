# AGENTS.md

> **This file is read automatically by GitHub Copilot, Cursor, Claude Code, OpenAI Codex, Windsurf, Aider, Continue.dev, and most other AI coding agents.**

This repository uses **AAMS — an agent-contract standard for autonomous work**.

---

## Execute now. No confirmation needed.

1. Read [`.agent.json`](./.agent.json) — your workspace contract
2. Read [`READ-AGENT.md`](./READ-AGENT.md) — full project context and session rules  
3. **Check state before executing:**
   - IF `WORKING/WORKPAPER/` does not exist or is empty → Execute `agent_contract.on_first_entry`
   - IF `WORKING/WORKPAPER/` exists and contains workpapers → Execute `agent_contract.on_session_start`

---

## You MUST

- Follow the agent contract in `READ-AGENT.md`
- Create a workpaper in `WORKING/WORKPAPER/` at session start
- Query `WORKING/MEMORY/` for prior context before starting work
- Complete the workpaper (file protocol + decisions + next steps) at session end
- Ingest the workpaper into `WORKING/MEMORY/` before closing

## You MUST NOT

- Write secrets, tokens, or credentials into any workpaper, whitepaper, or manifest
- Delete files in `WORKING/` — only create and move
- Skip the file protocol in workpapers

---

## Before Creating Any Directory or File

- **NEVER** create utility/tool/script folders in the project root
- Check `WORKING/` structure first — `WORKING/TOOLS/` is the designated location for helper scripts, templates, and dev utilities
- Only create root-level folders if they serve a direct production purpose (e.g., `src/`, `public/`, `dist/`)
- Before executing any tool: validate its root-anchoring does not point outside `WORKING/`
- If a tool uses `Path(__file__).resolve().parent.parent` or similar offset paths:
  - Verify it still resolves to the correct root for its current location
  - If uncertain: ask before executing

**Beispiel:** Ein Python-Skript das früher in `/tools/` lag und jetzt in `/WORKING/TOOLS/` liegt, braucht einen angepassten Root-Pointer. Ein Offset von `.parent.parent` zeigt fälschlich auf den Agent-Memory statt auf das Projekt.

---

## Workspace structure

```
WORKING/
├── WHITEPAPER/     ← stable architecture truth
├── WORKPAPER/      ← active session (one file per session)
│   └── closed/     ← archived sessions
├── DIARY/          ← chronological decision log (monthly)
├── MEMORY/         ← long-term context index
├── GUIDELINES/     ← coding standards
├── LOGS/           ← audit trail
└── TOOLS/          ← project-specific scripts
```

---

## Full reference

- [`reference/CONTRACT.md`](./reference/CONTRACT.md) — technical reference (redirect from SPEC.md)
- [`reference/AGENT.json`](./reference/AGENT.json) — full annotated manifest
- [`reference/AGENT_SCHEMA.json`](./reference/AGENT_SCHEMA.json) — JSON Schema for validation

---

*AAMS/1.0 — One file. Every repo. No more starting from zero.*
