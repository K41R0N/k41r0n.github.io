# Task register

AGF section 10.1: the live capabilities, sorted by his minutes x frequency, so
graduation effort goes where it saves him the most attention. Depths are
self-assessed (2026-10-29 audit); telemetry does not exist yet, so
your_minutes is unmeasured unless stated. Depth caps mode (Standard 9.2);
promotions need evidence, not feel (AGF anti-patterns).

| id | activity | frequency | your_minutes | depth | mode | next_gate | evidence | pack |
|---|---|---|---|---|---|---|---|---|
| cap-voice-writing | Site copy and prose in his voice | per deliverable | unmeasured (review per ruling) | D1 (toward D2) | E4 | D2: two consecutive deliverables accepted with at most minor edits (streak 0/2, wr-0000 + wr-0001 both rejected as slop) | agent/writing-runs.md | copy-five-pass |
| cap-message-drafting | Outward messages to people outside his context (Dom test 2026-10-29) | per message | unmeasured | D1 | E4 | D1 fidelity: he rates a drafted sequence as sounding like him; zero-context + root-why rules hold without correction | agent/learnings.md (8:19 PM row), Dom thread | advice-answer |
| cap-changelog-loop | Weekly interview -> his answers -> reviewed upkeep PR prose | weekly | ~5 (the interview answers) | D1 | E4 | First full weekly cycle where the prose ships without rewrite | agent/learnings.md (8:11 PM cadence row) | n/a |
| cap-methodology-explainer | Plain-language explanation of his methodologies for outsiders | on demand | unmeasured | D1 | E4 | First live use he reviews and accepts (Dom's follow-up questions are the first test) | agent/methodologies/threadbot.md | advice-answer |
| cap-site-data-upkeep | Activity feed data refresh (deterministic) | daily | ~0 (merge click only) | D2 | E0 for data; prose excluded by design | n/a for data (exact work); prose belongs to cap-changelog-loop | scripts/update-activity.js, site PR #14 | n/a |

## Notes

- cap-site-data-upkeep sits at the bottom because it costs him the least; the
  register is worked top-down.
- Acceptance, edit distance and his minutes feed from agent/writing-runs.md
  (AGF 5.3). When a capability clears its gate, the promotion rides a PR with
  the evidence attached - never by feel.
- Known measurement gaps (2026-10-29 audit): no telemetry (cost/time per
  run), no decision contracts (schemas/decisions/), no calibration. The
  register is the first fix, per his call.
