# AAMS Guard für OpenCode

# source: aams-guard-pattern (WH-010)
# Erstellt: 2026-07-07
# von: ogerly
# Status: experimental
# Tool: opencode
# Version: 0.1.0
# Sprache: Deutsch

---

## AAMS Guard für OpenCode — Beispiel

> **Dies ist ein Beispiel. Keine Empfehlung. Keine Verpflichtung.**

### WAS zu prüfen ist (AAMS-Pattern)

1. **manifest_read** — `.agent.json` und `READ-AGENT.md` gelesen?
2. **workpaper_open** — Aktives Workpaper existiert?
3. **tools_gated** — write/edit/apply_patch/bash erst nach Guard-Check?

### WIE OpenCode das umsetzen KANN

OpenCode hat eigene Hook- und Permission-Mechanismen. AAMS schreibt NICHT vor wie das implementiert wird.

**Mögliche Umsetzung:**

- OpenCode `permissions.json` nutzen
- OpenCode `skills/` als Konfigurationspunkt
- OpenCode `hooks` für Guard-Checks

### Beispiel: OpenCode permissions.json

```json
{
  "aams_guard": {
    "enabled": true,
    "checks": {
      "manifest_read": {
        "required": [".agent.json", "READ-AGENT.md"],
        "before": ["write", "edit", "apply_patch"]
      },
      "workpaper_open": {
        "check": "WORKING/WORKPAPER/ contains open workpaper",
        "before": ["write", "edit", "apply_patch", "bash"]
      }
    }
  }
}
```

### Beispiel: OpenCode skill hook

```typescript
// WORKING/TOOLS/skills/opencode/aams-guard-hook.ts
// Dies ist ein Beispiel. Keine Empfehlung.

interface AAMSGuardCheck {
  manifestRead: boolean;
  workpaperOpen: boolean;
  result: "pass" | "fail";
  reason?: string;
}

export async function checkAAMSGuard(): Promise<AAMSGuardCheck> {
  // OpenCode-spezifische Implementierung
  // AAMS beschreibt nur WAS, nicht WIE
  return { manifestRead: true, workpaperOpen: true, result: "pass" };
}
```

---

## Wichtige Klarstellung

> **Dieser Guard ist ein Beispiel, keine Empfehlung.**
> 
> AAMS beschreibt ein Pattern. Die Implementierung ist lokal.
> 
> - Du kannst Guard ignorieren
> - Du kannst Guard anpassen
> - Du kannst Guard ersetzen
> 
> AAMS schreibt dir nichts vor.

---

> Letztes Update: 2026-07-07 — AAMS Guard für OpenCode. Beispiel. Keine Empfehlung.
