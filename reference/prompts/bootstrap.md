# AAMS Bootstrap & Session Prompts

> The missing handoff: copy-paste prompts that turn a repo with `.agent.json` into a running AAMS workspace.
>
> **Why this file exists:** Chat agents don't self-bootstrap. ~30% of observed sessions created the workpaper *after* the work instead of before. These prompts close that gap.

---

## Quick Reference — Copy-Paste Prompts

| Situation | Prompt |
|---|---|
| **First time in this repo** | `Read .agent.json and execute the full agent_contract.on_first_entry. Start immediately. No confirmation needed.` |
| **New session (repo already bootstrapped)** | `Read READ-AGENT.md and execute agent_contract.on_session_start. Query WORKING/MEMORY/ltm-index.md for prior context on [TOPIC]. Create a workpaper before starting any work.` |
| **Need context from previous sessions** | `Query WORKING/MEMORY/ltm-index.md for all entries related to [TOPIC]. Summarize what was decided, what's open, and what was tried.` |
| **Create workpaper mid-session** | `Create a workpaper in WORKING/WORKPAPER/ for this session. Include: session goal, file protocol, decisions, next steps. Use format {date}-{topic}.md.` |
| **Close session** | `Complete the current workpaper: finalize file protocol, decisions, and next steps. Ingest into WORKING/MEMORY/ltm-index.md. Move workpaper to WORKING/WORKPAPER/closed/.` |

---

## 1 — First-Time Bootstrap

### Minimal (works with all tools)

```
Read .agent.json and execute the full agent_contract.on_first_entry. Start immediately. No confirmation needed.
```

Paste this into any agent that reads `.agent.json` or `AGENTS.md`:
Cursor, Claude Code, GitHub Copilot, Aider, Continue.dev, Codex, Windsurf.

### Two-Step Onboarding (new repo)

**Step 1 — Drop `.agent.json` into your repo:**

```bash
curl -sO https://raw.githubusercontent.com/DEVmatrose/AAMS/main/.agent.json
```

**Step 2 — Tell your agent:**

```
Read .agent.json and execute the full agent_contract.on_first_entry. Start immediately. No confirmation needed.
```

The agent creates the `WORKING/` structure, scans the repo, writes the first workpaper, and indexes into LTM.

**Idempotent:** Running bootstrap on an existing AAMS workspace is safe. Existing files are not overwritten.

### What the agent does after bootstrap

1. Reads `READ-AGENT.md` — full project context
2. Creates `WORKING/` folder structure
3. Scans the repository
4. Creates `READ-AGENT.md` if missing
5. Derives coding guidelines
6. Indexes documentation into LTM
7. Creates first workpaper with scan results

---

## 2 — Session Start Prompt (every session after bootstrap)

> **This is the most important prompt.** If you paste nothing else, paste this.
> It prevents the #1 observed failure: agent starts working without context or workpaper.

```
Read READ-AGENT.md and execute agent_contract.on_session_start.
Query WORKING/MEMORY/ltm-index.md for prior context on [TOPIC].
Create a workpaper in WORKING/WORKPAPER/ before starting any work.
```

Replace `[TOPIC]` with your session goal (e.g. "authentication refactor", "CI pipeline", "issue #42").

### Why "before starting any work" matters

Without that explicit instruction, chat agents tend to jump into the task and create the workpaper retroactively — losing the file protocol and decision trail. The phrase forces workpaper-first behaviour.

---

## 3 — LTM Query Prompt

Use this when you need context from previous sessions without starting a full session:

```
Query WORKING/MEMORY/ltm-index.md for all entries related to [TOPIC].
Summarize: what was decided, what's still open, and what approaches were tried.
```

For vector-store queries (if ChromaDB is set up):

```
Run: .venv/Scripts/python.exe WORKING/TOOLS/ltm_chroma.py query "[TOPIC]"
Summarize the results with session dates and key decisions.
```

---

## 4 — Workpaper Prompt

Force workpaper creation when the agent forgot or skipped it:

```
Create a workpaper in WORKING/WORKPAPER/ for this session.
Filename: {YYYY-MM-DD}-{topic}.md
Required sections: Session Goal, File Protocol, Decisions, Next Steps.
Start tracking all file changes from this point.
```

---

## 5 — Session Close Prompt

```
Complete the current workpaper:
1. Finalize the file protocol (all created/modified/moved/deleted files)
2. Document decisions made in this session
3. Write next steps for the following session
4. Append a summary entry to WORKING/MEMORY/ltm-index.md
5. Move the workpaper to WORKING/WORKPAPER/closed/
```

---

## 6 — Tool-Specific Variants

### GitHub Copilot (Chat / Agent Mode)
```
Read .agent.json and AGENTS.md, then execute the agent_contract defined in READ-AGENT.md. Start with on_first_entry. No confirmation needed.
```

> Copilot reads `.github/copilot-instructions.md` and `AGENTS.md` automatically. The bootstrap prompt is a fallback for chat mode where auto-execution doesn't trigger.

### Claude Code / Claude Desktop
```
Read .agent.json and execute the full agent_contract.on_first_entry. Start immediately. No confirmation needed.
```

### Cursor
```
Read .agent.json and execute the agent_contract.on_first_entry as documented in READ-AGENT.md. Start immediately.
```

### Aider / Continue.dev / Codex / Windsurf
```
Read .agent.json and execute the full agent_contract.on_first_entry. Start immediately. No confirmation needed.
```

---

## The Bootstrap Gap — Why This File Exists

| Agent type | Auto-bootstraps? | What you need to do |
|---|---|---|
| Autonomous (Aider, Claude Code, Codex) | ✅ Yes | Nothing — reads repo and acts |
| Chat + workspace (Copilot Agent, Cursor) | ⚠ Sometimes | Paste session-start prompt (§2) |
| Pure chat (Copilot Chat, ChatGPT) | ❌ No | Always paste bootstrap (§1) or session-start (§2) |

**Observed failure modes without explicit prompting:**
- Workpaper created after work instead of before (~30% of sessions)
- LTM not queried → agent re-decides things decided 5 sessions ago
- File protocol missing → no audit trail for the session
- Session closed without LTM ingest → knowledge lost

All of these are prevented by pasting the session-start prompt from §2.

---

## 7 — VS Code Workspace Snippet (Optional)

Add this to `.vscode/aams.code-snippets` for one-keystroke session start:

```json
{
  "AAMS Session Start": {
    "scope": "markdown",
    "prefix": "aams-start",
    "body": [
      "Read READ-AGENT.md and execute agent_contract.on_session_start.",
      "Query WORKING/MEMORY/ltm-index.md for prior context on ${1:TOPIC}.",
      "Create a workpaper in WORKING/WORKPAPER/ before starting any work."
    ],
    "description": "AAMS session-start prompt for chat agents"
  },
  "AAMS Session Close": {
    "scope": "markdown",
    "prefix": "aams-close",
    "body": [
      "Complete the current workpaper:",
      "1. Finalize the file protocol (all created/modified/moved/deleted files)",
      "2. Document decisions made in this session",
      "3. Write next steps for the following session",
      "4. Append a summary entry to WORKING/MEMORY/ltm-index.md",
      "5. Move the workpaper to WORKING/WORKPAPER/closed/"
    ],
    "description": "AAMS session-close prompt for chat agents"
  }
}
```

Type `aams-start` in any markdown file or chat input, tab-complete, and you have the session prompt with a cursor on the topic placeholder.

---

*AAMS/1.0 — prompts/bootstrap.md*
