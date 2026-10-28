---
type: Log
title: Compound log
---
# Compound log
Append-only. One entry per learning: what happened, what rule or change it suggests, status (candidate / approved / rejected), who approved.

## 2026-10-28 phase 1 build
- Client-derived rules tested against his own essays. Three client rules flagged most of his pieces (32-word cap, banned filler list, 20-word target). Recorded in canon/do-dont.md section B as NOT adopted. Status: candidate, needs his decision.
- Tightened the metronome-run check from 3 to 4 consecutive sentences after v0 flagged 10 of 11 pieces. Status: candidate.
- The 2025-06-17 essay states he uses Claude to "organize data or draft initial thoughts". Moved to excluded/ provisionally, then restored to raw/ after he confirmed all 11 essays are fully his prose (2026-10-28). Spec rebuilt from 9 raw essays with recency weighting (12-month half-life). Status: applied.
- Burrows Delta downgraded to a soft signal: 3 of 9 of his own leave-one-out pieces score as far as the closest different-author control chunk. Status: applied.
- Range checks recalibrated: strict min-max over 57 features put every one of his own pieces 10 to 20 features out. Now 25 structural features, ranges widened 50%, WARN at 3+. Status: candidate.
- Holdout is partly spent for rule-level decisions (dash budget, metronome, range calibration). Status: noted in HARNESS.md section 7b.
- Authorship of kairon.xyz theses, about and project pages is unverified; excluded from the spec. Status: waiting on him.

## 2026-10-28 findings area
- Added findings/ (one dated file per finding, each with source and status; index in findings/README.md). log/compound.md stays the append-only list of build learnings and rule candidates. findings/ holds measurements, his decisions and steering, and open items. Status: candidate, needs his OK on the convention.
