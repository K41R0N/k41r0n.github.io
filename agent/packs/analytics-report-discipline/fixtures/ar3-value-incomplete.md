report: weekly newsletter metrics
window: 2026-W46
## Period
- period: 2026-W46 | state: closed | comparable: yes
## Numbers
- value: opens = 4120
## Interpretation
- reading: the step on 2026-11-12 matches the subject-line test artifact
## Actions
- action: rerun the subject-line variant | rank: 1
## Thresholds
- flag: unsubscribes breached 60 per week | hypothesis: the new footer link confuses readers
## Open-decisions
- decision: whether bot opens are excluded | default: excluded | alternates: included with a flag
## Corrections
- correction: last week's opens double-counted test sends | fix: exclude seed list at source
## Uncaptured
- source: vendor changelog page | status: uncaptured | capture-plan: hash-pinned capture on each run, eye check otherwise
