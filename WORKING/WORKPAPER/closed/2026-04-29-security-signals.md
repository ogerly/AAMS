# Workpaper: Security Signals — Issue #26

**Datum:** 2026-04-29  
**Typ:** SEC — Security Signals  
**Referenz:** Issue [#26](https://github.com/DEVmatrose/AAMS/issues/26)  
**Priorität:** Mittel — Backlog  

---

## Session Goal

Security Signals konzipieren: Optional `security`-Sektion in AGENT.json für Trust-Portabilität.

---

## File Protocol

| Aktion | Datei | Status |
|--------|-------|--------|
| CREATED | `WORKING/WORKPAPER/2026-04-29-security-signals.md` | ✅ |

---

## 1. Problem (aus Issue #26)

Das Manifest soll Trust-Portabilität ermöglichen: Security-History reist mit dem Agenten mit. Zwei nahezu identische Issues von AgentGurke (#7 und #8) — #7 Duplikat von #8.

---

## 2. Konzipierte `security`-Sektion

```json
"security": {
  "_doc": "Optional security metadata. Describes the security posture of the agent and its environment. All fields optional.",
  "last_scan": "2026-04-29",
  "scan_type": "dependency-vulnerability",
  "findings": {
    "_doc": "Security findings categorized by severity.",
    "critical": 0,
    "high": 0,
    "medium": 1,
    "low": 3
  },
  "deployed_services": [
    {
      "_doc": "Services deployed by this agent.",
      "name": "my-service",
      "type": "api",
      "version": "1.0.0",
      "last_audit": "2026-04-29"
    }
  ],
  "behavioral_signals": {
    "_doc": "Behavioral indicators of agent trustworthiness.",
    "sessions_without_incident": 48,
    "last_violation": null,
    "trust_score": 0.97
  }
}
```

---

## 3. Manifest-Prinzip (D9)

AAMS ist ein Manifest, kein Regelwerk. Contract darf nichts zwingen oder voraussetzen. Keine Regeln vorgeben. Beschreibt was es ist, nicht was Agenten MÜSSEN tun.

**Konsequenz:** `security`-Sektion muss optional und beschreibend sein. Keine required fields. Keine Enforcement.

---

## 4. DoD (aus Issue #26)

- [x] `reference/AGENT.json` — `security`-Sektion als Beispiel ergänzen
- [x] `reference/AGENT_SCHEMA.json` — Schema für `security`-Objekt mit allen Feldern (alles optional)
- [x] `reference/SPEC.md` — kurze Erwähnung als optionales Trust-Feld

---

## 5. Integration in `.agent.json`

**Wo einfügen:** In `agent_conventions`-Bereich, nach `file_safety`.

---

## 6. Integration in `CONTRACT.md`

**CONTRACT.md:** Kurze Erwähnung als optionales Trust-Feld.

---

## 7. Decisions

| # | Decision | Begründung |
|---|----------|------------|
| D1 | `security` optional, nicht required | Manifest-Prinzip (D9) |
| D2 | Alle Felder optional | Backward compat |
| D3 | Issue #7 schließen als Duplikat von #8 | Identischer Scope |
| D4 | Issue #26 Workpaper schließen nach Integration | Konzept abgeschlossen |

---

## 8. Nächste Steps

1. `security` in `.agent.json` einfügen
2. `security` in `reference/AGENT.json` als Beispiel
3. `security` in `reference/AGENT_SCHEMA.json` als optional field
4. `security` in `CONTRACT.md` erwähnen
5. Workpaper schließen

---

> Letztes Update: 2026-04-29 — Security Signals konzipiert. Manifest-Prinzip (D9) angewendet: optional, beschreibend, keine Enforcement. Trust-Portabilität als Feature.
