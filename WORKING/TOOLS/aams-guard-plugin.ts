# AAMS-Guard-Plugin — vollständiges Muster

Datei: `.opencode/plugin/aams-guard.ts`

Erzwingt den vollständigen AAMS-Kreislauf in drei Stufen:
1. Agent-Kontext gelesen (`.agent.json`, `READ-AGENT.md`)
2. Aktives Workpaper vorhanden (`WORKING/workpaper-*.md`, Status `open`)
3. Erst dann: `write`/`edit`/`apply_patch`/`bash` erlaubt

```typescript
import type { Plugin } from "@opencode-ai/plugin"
import { existsSync, readdirSync, readFileSync } from "fs"
import { join } from "path"

const contextRead = new Set<string>()
const AAMS_REQUIRED_FILES = [".agent.json", "READ-AGENT.md"]
const GATED_TOOLS = ["write", "edit", "apply_patch", "bash"]

function hasOpenWorkpaper(projectRoot: string): boolean {
  const dir = join(projectRoot, "WORKING")
  if (!existsSync(dir)) return false
  return readdirSync(dir)
    .filter(f => f.startsWith("workpaper-") && f.endsWith(".md"))
    .some(f => {
      const content = readFileSync(join(dir, f), "utf-8")
      return /status:\s*open/i.test(content)
    })
}

export const AAMSGuard: Plugin = async ({ project }) => {
  return {
    "tool.execute.after": async (input, output) => {
      if (input.tool === "read") {
        const path = output?.args?.filePath ?? ""
        if (AAMS_REQUIRED_FILES.some(f => path.endsWith(f))) {
          contextRead.add(input.sessionID)
        }
      }
    },
    "tool.execute.before": async (input) => {
      if (!GATED_TOOLS.includes(input.tool)) return

      if (!contextRead.has(input.sessionID)) {
        throw new Error(
          "AAMS-VERSTOSS: Lies zuerst .agent.json und READ-AGENT.md, " +
          "bevor du Änderungen vornimmst."
        )
      }
      if (!hasOpenWorkpaper(project.path)) {
        throw new Error(
          "AAMS-VERSTOSS: Kein offenes Workpaper unter WORKING/. " +
          "Lege zuerst ein Workpaper mit status: open an."
        )
      }
    },
  }
}
```

## Bekannte Grenzen

- Greift nicht bei Subagent-Tool-Calls über den Task-Tool (offener Bug in
  OpenCode, Stand Ende 2025/Anfang 2026 — vor Einsatz mit Subagents prüfen,
  ob noch aktuell).
- Regex-Check auf `status: open` ist bewusst simpel gehalten. Bei Bedarf durch
  echten YAML-Frontmatter-Parser ersetzen, falls Workpaper-Format komplexer wird.
- Session-State (`contextRead`) lebt nur im Plugin-Prozess-Speicher. Bei
  OpenCode-Neustart mitten in einer Session geht der Zustand verloren — das
  ist gewollt (erzwingt erneutes Lesen nach Neustart).