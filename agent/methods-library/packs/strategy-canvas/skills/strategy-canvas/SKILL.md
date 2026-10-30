---
name: strategy-canvas
description: Builds a client strategy canvas in seven steps and tags every claim as sourced, inferred or a gap.
argument-hint: "[client or project, and what material exists]"
version: 0.1.0
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Strategy canvas

## Purpose
Turn what is known about a client into one canvas a team can work from, with honest marks on what is evidence and what is a guess.

## Step 0
List the material you have and say plainly what you could not read. Name who speaks publicly for the client. If nobody does, that is the first finding, before positioning or messaging.

## When to use / not
Use at the start of a new client or project, or when a strategy has drifted. Not for single pieces of copy (copy-five-pass) and not to produce client-facing material without his yes.

## Modes
Interactive. One module at a time; confirm before moving on.

## Procedure by slot
Strategize: write the snapshot last, but fill the spokesperson line first.
Suspect: list what could be wrong (thin sources, one voice, stale data).
Anticipate: gather sources and number them.
Act, in order: 1 Lean Canvas (problem, solution, value promise, segments, channels, advantage, revenue, costs, metrics, alternatives). 2 Value Proposition (jobs, ranked pains, gains, relievers). 3 ICP Definition (who to pursue and who not to, with qualifiers and disqualifiers). 4 Empathy Map. 5 Positioning (alternatives, attributes, value, best-fit customers, category). 6 Positioning statement (For ... who ... Unlike ...). 7 Narrative (hero, problem, guide, plan, call to action, success, stakes, messaging pyramid).
Tag every bullet: [Sourced: where], [Inferred], or [Gap]. Call a moat claim a hypothesis until proven.
React and recognize: run the checks. Rank pains. Mark any quiet pain the customer would not say out loud.
Calculate: goals need a measurable result tied to an artifact, or they are dropped. Report raw platform numbers, not abstract scores.

## Output contract
The canvas in the eval's format, status draft or proposed.

## Delivery contract
Nothing client-facing goes out without his yes on the exact thing. Approved needs approved_by.

## Quality gates
`python3 evals/run.py strategy-canvas`. Clean means the structure and tags are present. It does not mean the strategy is right.

## Compound step
Log what he changed in routines/learnings.md. Three repeats become a rule.

## References
packs/strategy-canvas/fixtures/
