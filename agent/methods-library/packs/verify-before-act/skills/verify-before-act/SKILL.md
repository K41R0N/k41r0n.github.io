---
name: verify-before-act
description: Keeps diagnosis and change apart, checks claims against the live thing, and limits each turn to one verified change.
argument-hint: "[what is being investigated or changed]"
version: 0.1.0
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Verify before act

## Purpose
Stop plausible-but-wrong actions. A claim, a past write-up or an alarming message is not a fact until the live thing confirms it.

## Step 0
Say what you are about to rely on and where it came from. Say plainly what you could not read or reach.

## When to use / not
Use before any change to a system, document, account or plan, and when something looks broken. Not for pure questions with no action behind them.

## Modes
Two, never mixed in one turn: investigate (read only) and change (one change).

## Procedure by slot
1. Strategize: list the claims you would rely on.
2. Suspect: for each, name the live check that would confirm or contradict it.
3. Anticipate: run the checks. Record the result as confirmed, contradicted or unchecked.
4. Act (investigate): name each alarming signal before reacting: expected, consequence, known defect, false alarm, or unknown. Only unknown is a finding, and it stays a hypothesis.
5. React: before calling anything broken, confirm it a second way that does not share the first tool's code.
6. Recognize: if a fix becomes obvious mid-investigation, write it as a proposal. Clarity is not permission.
7. Act (change, next turn): one change. Never on an unchecked or contradicted claim.
8. Calculate: verify the result, then log what was learned. A documented value that disagrees with the live one is a correction to file, not a fault to fix.

## Output contract
A note in the eval's format.

## Delivery contract
Report findings and the one proposed change to the owner of the thing. Changes to anything of his go through his yes.

## Quality gates
`python3 evals/run.py verify-before-act`. Clean means the discipline is visible in the note, not that the diagnosis is right.

## Compound step
Log corrections in routines/learnings.md. Three repeats become a rule.

## References
packs/verify-before-act/fixtures/, knowledge/ethos/ethos.md (items 2, 20, 21)
