# Workpaper: File Safety — Issue #50

**Datum:** 2026-04-29  
**Typ:** SEC — File Safety  
**Referenz:** Issue [#50](https://github.com/DEVmatrose/AAMS/issues/50) (Feld-Report mantis-cms)  
**Priorität:** Mittel — neue Sicherheits-Erweiterung  

---

## Session Goal

File Safety konzipieren: Regel im Manifest für Datei-Löschungen außerhalb WORKING/.

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-29-file-safety.md` | ✅ |

---

## 1. Problem (aus Issue #50)

Agenten die AAMS lesen bereinigen Repositories (z.B. Template-Transformation). Dabei können Dateien versehentlich gelöscht werden, die noch relevant sind — weil der Agent sie nicht kennt.

Das Manifest hat `never_delete` für die Workspace-Struktur (`WORKING/`), aber keine Guidance für das Repository-Wurzelverzeichnis.

---

## 2. Feld-Report (mantis-cms, 2026-04-28)

**Agent:** Opencode CLI  
**Modell:** 100% lokal (LM Studio)  
**Plattform:** Linux (WSL2)

**Vorschlag:** `file_safety`-Sektion im Manifest:

```json
"file_safety": {
  "_doc": "Before deleting any file outside WORKING/, agents MUST check git history.",
  "pre_delete_check": "git log --all --diff-filter=D -- <file>",
  "if_history_found": "do not delete — ask user for confirmation",
  "if_no_history": "safe to delete",
  "never_delete_manually": "Never use rm -rf with manual file lists without git verification"
}
```

**Begründung:**
- Prozess statt Liste: Eine statische Schutzliste ist unvollständig und wartungsintensiv
- Minimal: Fügt keine neuen Dateien/Ordner hinzu
- Universal: Funktioniert für jedes Repo, egal wie viele Dateien
- Git-native: Nutzt Git als Quelle der Wahrheit, nicht eine externe Liste

---

## 3. Manifest-Prinzip (D9)

AAMS ist ein Manifest, kein Regelwerk. Contract darf nichts zwingen oder voraussetzen. Keine Regeln vorgeben. Beschreibt was es ist, nicht was Agenten MÜSSEN tun.

**Konsequenz:** `file_safety` muss beschreibend sein, nicht preskriptiv.

---

## 4. Konzipierte `file_safety`-Sektion

```json
"file_safety": {
  "_doc": "Describes how agents may handle file deletions outside the workspace. Git history is the source of truth for file relevance.",
  "outside_workspace": {
    "_doc": "Files outside WORKING/ should be treated with caution before deletion.",
    "check_git_history": "git log --all --diff-filter=D -- <file> examines whether a file has been committed in any branch.",
    "if_history_found": "Files with git history may be relevant. Agents should inform the user before deletion.",
    "if_no_history": "Files without git history may be safe to delete. Agents may proceed with caution.",
    "manual_rm_rf": "Never use rm -rf with manual file lists without git verification."
  }
}
```

---

## 5. Integration in `.agent.json`

**Wo einfügen:** Nach `secrets_policy`, vor `gitignore_patterns`.

**Änderung:** Neue `file_safety`-Sektion in `.agent.json` unter `workspace`.

---

## 6. Integration in `AGENT.json` und `AGENT_SCHEMA.json`

**AGENT.json:** `file_safety` als Beispiel-Eintrag in `reference/AGENT.json`.

**AGENT_SCHEMA.json:** `file_safety` als optional field im Schema.

---

## 7. Integration in `SPEC.md` / `CONTRACT.md`

**CONTRACT.md:** Kurze Erwähnung als optionales Trust-Security-Feld.

---

## 8. Decisions

| # | Decision | Begründung |
|---|----------|------------|
| D1 | `file_safety` beschreibend, nicht preskriptiv | Manifest-Prinzip (D9) |
| D2 | Git history als Quelle der Wahrheit | Git-native, universal |
| D3 | `file_safety` optional, nicht required | Backward compat |
| D4 | Issue #50 Workpaper schließen nach Integration | Konzept abgeschlossen |

---

## 9. Nächste Steps

1. `file_safety` in `.agent.json` einfügen
2. `file_safety` in `reference/AGENT.json` als Beispiel
3. `file_safety` in `reference/AGENT_SCHEMA.json` als optional field
4. `file_safety` in `CONTRACT.md` erwähnen
5. Workpaper schließen

---

> Letztes Update: 2026-04-29 — File Safety konzipiert. Manifest-Prinzip (D9) angewendet: beschreibend, nicht preskriptiv. Git history als Quelle der Wahrheit.
