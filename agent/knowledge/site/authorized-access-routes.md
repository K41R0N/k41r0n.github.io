---
type: Note
title: "Authorized access routes"
confidence: operator_reported
tier: 2
approver: Alejandro Arango
source: His explicit 2026-11-24 instruction (private record) that GitHub access for his agent runs through the recorded scoped token, never a browser sign-in. The general rule below is the agent-side generalization logged after the 2026-11-25 access-route failure (routines/learnings.md, 2026-11-25 rows); it is proposed, not his wording.
status: ACTIVE
---
# Authorized access routes

Before signing into, pushing to, or otherwise using an outside system for this
harness, use the route recorded for that system. A route recorded here (or in
the private operations record it points to) is the authorized one. A missing
tool action or a more convenient path does not widen the authorized route.
When the recorded route is unavailable, report the exact blocker - never
substitute a broader-access route such as the owner's interactive account
sign-in.

## Routes

- **GitHub (this repo and his other repositories):** reads and writes use the
  scoped fine-grained token recorded in the private secret store. Browser
  sign-in as him is not an authorized route (his explicit instruction,
  2026-11-24).
- **HTML previews for him:** here.now, per the standing rules in
  `agent/AGENTS.md` section 5.
- **Site content writes:** the lanes in
  `knowledge/site/contribution-workflow.md` and the CMS write guard in
  `routines/protocols/PORTFOLIO-WRITE-GUARD-01.md`.

Secrets never enter this repo. Token labels, scope and rotation notes live in
the private record, not here.
