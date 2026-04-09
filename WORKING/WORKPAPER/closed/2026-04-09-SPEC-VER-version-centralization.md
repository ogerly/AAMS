# Workpaper: Version Centralization

- **Datum:** 2026-04-09
- **Agent:** GitHub Copilot (Claude Opus 4.6)
- **Status:** CLOSED
- **Typ:** Implementation

---

## Problem

Die Version steht an mehreren Stellen und wird bei jedem Release manuell überall angepasst:
- `READ-AGENT.md` (Current Status → Spec version + Last release)
- `reference/SPEC.md` (Header)
- `.agent.json` (`_spec` Feld)
- `AGENTS.md` (Footer)
- GitHub Release Tag

**Versionsdrift ist der Normalfall, nicht die Ausnahme.** Beweis: v1.2.0 released, aber READ-AGENT.md sagte noch "1.1", SPEC.md sagte "1.1".

---

## Lösung

**Single Source of Truth: `.env`**

```
AAMS_VERSION=1.3.0
```

Dateien die die Version referenzieren werden beim Release-Prozess aktualisiert. `.env` ist die einzige Stelle an der die Version geändert wird.

---

## Betroffene Dateien

| Datei | Was | Aktualisierung |
|-------|-----|---------------|
| `.env` | `AAMS_VERSION=1.3.0` | **Quelle** — hier wird geändert |
| `READ-AGENT.md` | Current Status → Spec version + Last release | Manuell bei Release |
| `reference/SPEC.md` | Header `## Version X.Y` | Manuell bei Release |
| `.agent.json` | bleibt `AAMS-MINI/1.0` (Manifest-Format, nicht Spec-Version) | Nicht betroffen |
| `AGENTS.md` | Footer | Manuell bei Release |

**Hinweis:** `.agent.json` `_spec: AAMS-MINI/1.0` beschreibt das Manifest-Format, nicht die Spec-Version. Das bleibt.

---

## Decisions

- **D1**: `AAMS_VERSION` in `.env` als Single Source of Truth
- **D2**: Bei Release: Version in `.env` ändern, dann in READ-AGENT.md und SPEC.md übernehmen
- **D3**: Kein automatisches Scripting nötig — die Stellen sind überschaubar (2-3 Dateien)
- **D4**: Diary-Reform (Pointer-Only) wird als Teil von v1.3.0 released

---

## File Protocol

| # | Aktion | Datei | Beschreibung |
|---|--------|-------|-------------|
| F1 | CREATED | `WORKING/WORKPAPER/2026-04-09-SPEC-VER-version-centralization.md` | Dieses Workpaper |
| F2 | MODIFIED | `.env` | `AAMS_VERSION=1.3.0` hinzugefügt |
| F3 | MODIFIED | `READ-AGENT.md` | Version auf 1.3, Last release auf v1.3.0 |
| F4 | MODIFIED | `reference/SPEC.md` | Header auf Version 1.3 |
| F5 | MODIFIED | `.agent.json` | Diary-Reform (pointer-only) |
| F6 | MODIFIED | `READ-AGENT.md` | Diary-Beschreibung aktualisiert |
| F7 | MODIFIED | `reference/SPEC.md` | Diary-Sektion komplett überarbeitet |
| F8 | MOVED | `WORKPAPER/2026-04-09-ARCH-DRY-diary-granularity-problem.md` → `closed/` | Diary-Workpaper geschlossen |
| F9 | MOVED | `WORKPAPER/2026-04-09-rfl-reflection-protocol-step.md` → `closed/` | RFL-Workpaper geschlossen |
