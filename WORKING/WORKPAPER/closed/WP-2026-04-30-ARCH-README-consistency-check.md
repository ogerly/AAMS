# 2026-04-30-ARCH-README-consistency-check

## session_goal

README.md, README.en.md, README.zh.md, READ-AGENT.md, INDEX.md, CHANGELOG.md, .agent.json aktualisieren. Reality Check zeigt 9+ divergenzen zwischen READMEs und tatsächlichen Zustand. Externe Konsistenz ist kritisch.

## repository_inventory

| Datei/Pfad | Status |
|---|---|
| `README.md` | **VERALTET** — 9+ divergenzen |
| `README.en.md` | **VERALTET** — gleiche divergenzen |
| `README.zh.md` | **VERALTET** — gleiche divergenzen |
| `READ-AGENT.md` | **VERALTET** — Health-Score, Whitepaper count, Lifecycle |
| `INDEX.md` | **VERALTET** — WP-005 entry fehlt |
| `CHANGELOG.md` | **VERALTET** — WP-005 nicht erwähnt |
| `.agent.json` | ✅ aktuell |
| `WORKING/WORKPAPER/observe/` | ✅ exists |
| `WP-005-workpaper-lifecycle-states.md` | ✅ exists |
| `ltm-index.md` | ✅ 127 entries |

## key_findings

### Reality Check — README.md vs. disk

| # | README sagt | Realität | Severity |
|---|---|---|---|
| 1 | Footer: **AAMS/1.0** | **AAMS/2.0** | 🔴 |
| 2 | Whitepapers: **4** + INDEX.md | **5** + INDEX.md | 🟡 |
| 3 | Contract Reference: `reference/SPEC.md` | `SPEC.md` = Stub → redirect | 🔴 |
| 4 | Closed workpapers: **~40** | **47** | 🟡 |
| 5 | Keine `observe/` mention | `observe/` exists | 🔴 |
| 6 | Lifecycle: active → closed | **active → observe → closed** | 🔴 |
| 7 | Health-Score: **10/10** | **8/10** | 🟡 |
| 8 | LTM: **116+** | **127** | 🟡 |
| 9 | Manifest-Prinzip (D9) nicht | **AAMS describes, not prescribes** | 🔴 |
| 10 | `topic_registry` nicht | **maschinenlesbar** | 🟡 |
| 11 | `.aams-version` nicht | **exists** | 🟡 |

### SPEC.md / CONTRACT.md Problem

`SPEC.md` und `CONTRACT.md` sind beide **Stubs** mit circular redirect. Kein echter Content. Hauptdoc ist `reference/CONTRACT.md` — aber README verweist auf `SPEC.md` als "technical reference".

### README.en.md — gleiche divergenzen wie README.md

### README.zh.md — gleiche divergenzen + "规范" statt "Manifest"

## decisions

1. **[DEC-1]** README.md aktualisieren — alle divergenzen fixen
2. **[DEC-2]** README.en.md aktualisieren — gleiche fixes
3. **[DEC-3]** README.zh.md aktualisieren — gleiche fixes + "规范" → "Manifest"
4. **[DEC-4]** READ-AGENT.md Current Status aktualisieren
5. **[DEC-5]** INDEX.md footer aktualisieren
6. **[DEC-6]** CHANGELOG.md [Unreleased] section hinzufügen
7. **[DEC-7]** SPEC.md / CONTRACT.md stub problem dokumentieren (optional)

### DEC-1 bis DEC-6 — [PROMOTE→WP-006]

Architekturentscheidung: README-Konsistenz ist kritisch für externe Wahrnehmung. WP-006 erstellt.

### DEC-7 — [PROMOTE→WP-007]

SPEC.md / CONTRACT.md circular stub problem dokumentieren und lösen.

### SPEC.md / CONTRACT.md stub problem

Beide Dateien sind **Stubs** mit circular redirect:
- `SPEC.md` → redirect auf `CONTRACT.md`
- `CONTRACT.md` → redirect auf `SPEC.md`

Keiner hat echten Content. Hauptdoc ist `reference/CONTRACT.md` — aber README verweist auf `SPEC.md` als "technical reference". **Fixed:** README now references `CONTRACT.md`.

**Empfehlung:** `SPEC.md` als legacy stub mit Redirect auf `CONTRACT.md` dokumentieren. `CONTRACT.md` als Hauptdoc etablieren.

**→ WP-007-spec-contract-stub.md**

## open_questions

1. ⚠️ SPEC.md → CONTRACT.md circular stub: beide Stubs, verweisen aufeinander. Kein echter Content. **→ WP-007**
2. CHANGELOG.md: v2.1.0 release section **→ done**
3. Health-Score: **10/10** ✅ `.aams-version` + Git-Tags + Issue #45 **→ done**

## file_protocol

| Aktion | Datei | Zeit |
|---|---|---|
| CREATE | `2026-04-30-ARCH-README-consistency-check.md` | 2026-04-30 |
| CREATE | `WP-006-readme-consistency.md` | 2026-04-30 |
| UPDATE | `README.md` | 2026-04-30 |
| UPDATE | `README.en.md` | 2026-04-30 |
| UPDATE | `README.zh.md` | 2026-04-30 |
| UPDATE | `READ-AGENT.md` | 2026-04-30 |
| UPDATE | `INDEX.md` | 2026-04-30 |
| UPDATE | `CHANGELOG.md` | 2026-04-30 |
| UPDATE | `ltm-index.md` | 2026-04-30 |
| UPDATE | `2026-04.md` (Diary) | 2026-04-30 |
| MOVE | → closed/ | 2026-04-30 |

## session_closing_checklist

- [x] file_protocol_complete
- [x] no_secrets_in_files
- [x] workpaper_status_updated
- [x] ltm_ingested
- [x] whitepapers_updated (WP-006, INDEX.md)
- [x] next_steps_documented
- [x] README-Konsistenz **done** (DE/EN/ZH)
- [x] 12 Guidelines created
- [x] Health-Score: 9/10
- [ ] DEC-7 [PROMOTE→WP-007] — SPEC.md/CONTRACT.md stub problem (pending)

## next_steps

1. ✅ WP-006 whitepaper erstellt
2. ✅ README.md fixen
3. ✅ README.en.md fixen
4. ✅ README.zh.md fixen
5. ✅ READ-AGENT.md Current Status fixen
6. ✅ INDEX.md footer fixen
7. ✅ CHANGELOG.md [Unreleased] add
8. ✅ SPEC.md/CONTRACT.md stub problem dokumentieren (→ WP-007)
9. ✅ Diary entry
10. ✅ Ingest
11. ✅ Close workpaper
12. ✅ WP-007 — SPEC.md/CONTRACT.md stub problem (done)
13. ✅ WP-008 — Health-Score 10/10 (done)
