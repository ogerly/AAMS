# Guideline: Naming Schema

> **Gültig ab:** 2026-04-30  
> **Herkunft:** AAMS/2.0 Contract + READ-AGENT.md + `.agent.json`  
> **Typ:** Core Konvention / Filename-Konvention

---

## Warum

Strukturierte Filenamen ermöglichen:

- Cross-session consistency checks (RFL)
- Pattern-matching für Agenten
- Chronologische Ordnung
- Topic-basierte Navigation

---

## Workpaper Naming

```
WP-{DATE}-{TOPIC}-{SUBTOPIC}-{description}.md
```

| Variable | Format | Beispiel |
|---|---|---|
| `DATE` | `YYYY-MM-DD` | `2026-04-30` |
| `TOPIC` | 3-4 letters, UPPERCASE | `ARCH`, `SPEC`, `LTM` |
| `SUBTOPIC` | 3-4 letters, UPPERCASE | `WPSTRUCT`, `RFL`, `LTM` |
| `description` | kebab-case, lowercase | `workpaper-observe-folder` |

**Beispiel:** `WP-2026-04-30-ARCH-WPSTRUCT-workpaper-observe-folder.md`

---

## Whitepaper Naming

```
WH-{NNN}-{TOPIC}-{description}.md
```

| Variable | Format | Beispiel |
|---|---|---|
| `WP` | Prefix | `WP-` |
| `NNN` | 3-digit number | `001`, `005` |
| `TOPIC` | 3-4 letters, UPPERCASE | `ARCH`, `SPEC` |
| `description` | kebab-case, lowercase | `aams-overview` |

**Beispiel:** `WH-005-workpaper-lifecycle-states.md`

---

## Topic Registry

| TOPIC | Meaning |
|---|---|
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

**Extensible:** max 4 letters, UPPERCASE, unique.

**Maschinenlesbar:** `.agent.json` `topic_registry` + `READ-AGENT.md` Topic Registry table.

---

## Regeln

1. **TOPIC first:** Enables RFL pattern-matching.
2. **SUBTOPIC optional:** For sub-areas of TOPIC.
3. **kebab-case description:** Lowercase, hyphens.
4. **No spaces in filenames.**
5. **No special characters.**

---

## Regel

> **Namen sind ein Ordnungsschlüssel, nicht eine Beschreibung.**  
> **TOPIC enables RFL pattern-matching — priorität.**

---

> Letztes Update: 2026-04-30 — Initial creation. AAMS/2.0 Naming Schema.
