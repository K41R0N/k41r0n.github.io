---
name: campaign-basics
description: Helps a beginner plan a small social media campaign with one thing, one idea, one action and numbers they can check.
argument-hint: "[what they want to promote and who they want to reach]"
version: 0.1.0
metadata:
  harness:
    lane: L2
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Campaign basics

## Purpose
Give a beginner a plan small enough to start this week, and a way to tell if it worked.

## Step 0
Ask what they want to promote and who for. Say what you are guessing. Source note: structure adapted from a work template whose authorship is unconfirmed.

## When to use / not
Use for "how do I make a social media campaign". Not for a big client strategy (use strategy-canvas).

## Modes
One.

## Procedure by slot
1. Strategize: pick the one thing to promote. Everything else waits.
2. Suspect: say who it is for, in one line, and what they want to know before they say yes.
3. Anticipate: write the one idea, a sentence that makes them feel something true, and the one action they take.
4. Act: write what you are not claiming or chasing. This keeps the message clean.
5. React: for each place you will post, give it one job. If you cannot, drop the place.
6. Recognize: keep a steady baseline and leave room for a surprise that works.
7. Calculate: choose measures with a number and a date, using raw counts. Then run asker-fit.

## Output contract
A plan in the eval's format.

## Delivery contract
Words that go out under his name need his yes.

## Quality gates
`python3 evals/run.py campaign-basics`. Clean means the plan is complete and plain, not that it will work.

## Compound step
Log what the campaign taught in routines/learnings.md.

## References
packs/campaign-basics/fixtures/, packs/asker-fit, knowledge/ethos/asker-lens.md
