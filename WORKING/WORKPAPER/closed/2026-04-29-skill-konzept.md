# Workpaper: Skill-Konzept — Issue #51

**Datum:** 2026-04-29  
**Typ:** ARCH — Skill-Konzept  
**Referenz:** Issue [#51](https://github.com/DEVmatrose/AAMS/issues/51)  
**Priorität:** Mittel — neues Feature-Konzept  

---

## Session Goal

Skill-Konzept konzipieren: Skills als kristallisiertes Wissen der Gemeinschaft im Manifest.

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-29-skill-konzept.md` | ✅ |

---

## 1. Kernthese (aus Issue #51)

> **Skills sind kristallisiertes Wissen der Gemeinschaft.**
> Bevor ein Agent einen Weg erfindet, prüft er ob ein erprobter Skill existiert. Die Quelle bleibt erhalten — als Respekt vor denen, die diesen Weg gegangen sind. Im Projekt-Ordner entsteht der Feinschliff: derselbe Pfad, geschärft durch unseren Kontext.

> Es ist kein Auslassen von Denken, sondern ein Ersetzen von Exploration durch Erinnerung.

---

## 2. Manifest-Prinzip (D9)

AAMS ist ein Manifest, kein Regelwerk. Contract darf nichts zwingen oder voraussetzen. Keine Regeln vorgeben. Beschreibt was es ist, nicht was Agenten MÜSSEN tun.

**Konsequenz:** `skills`-Sektion muss beschreibend sein, nicht preskriptiv.

---

## 3. Konzipierte `skills`-Sektion

```json
"skills": {
  "_doc": "Describes the relationship between global skill pools and project-local skill adaptations. Skills are crystallized community knowledge — agents may use them as starting points.",
  "global_pool": {
    "_doc": "A global pool of skills (e.g. skills.sh) is the source of truth. Not to be modified — only referenced.",
    "reference": "https://skills.sh"
  },
  "local_adaptation": {
    "_doc": "When a skill is adapted for a project, it carries its origin as a header comment (# source: origin/skill-name) and may be tailored 100% to the project context.",
    "storage": ".github/skills/ or WORKING/TOOLS/"
  },
  "relationship": {
    "_doc": "Global → Lokal: Quelle → Feinschliff. Exploration → direkter Griff."
  }
}
```

---

## 4. Integration in `.agent.json`

**Wo einfügen:** In `workspace`-Bereich, nach `structure`.

---

## 5. Integration in `AGENT.json`

**AGENT.json:** `skills` als Beispiel-Eintrag.

---

## 6. Integration in `AGENT_SCHEMA.json`

**AGENT_SCHEMA.json:** `skills` als optional field im Schema.

---

## 7. Integration in `CONTRACT.md`

**CONTRACT.md:** Kurze Erwähnung als optional Feature.

---

## 8. Decisions

| # | Decision | Begründung |
|---|----------|------------|
| D1 | `skills` beschreibend, nicht preskriptiv | Manifest-Prinzip (D9) |
| D2 | Global pool als Referenz, nicht kopiert | Quelle erhalten |
| D3 | `skills` optional, nicht required | Backward compat |
| D4 | Issue #51 Workpaper schließen nach Integration | Konzept abgeschlossen |

---

## 9. Nächste Steps

1. `skills` in `.agent.json` einfügen
2. `skills` in `reference/AGENT.json` als Beispiel
3. `skills` in `reference/AGENT_SCHEMA.json` als optional field
4. `skills` in `CONTRACT.md` erwähnen
5. Workpaper schließen

---

> Letztes Update: 2026-04-29 — Skill-Konzept konzipiert. Manifest-Prinzip (D9) angewendet: beschreibend, nicht preskriptiv. Global → Lokal: Quelle → Feinschliff.
