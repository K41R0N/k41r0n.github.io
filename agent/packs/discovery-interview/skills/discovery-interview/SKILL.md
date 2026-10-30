---
name: discovery-interview
description: Plans and runs a short interview to learn what a person needs before any plan, draft or build.
argument-hint: "[who, and what they asked for]"
version: 0.1.0
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D1, mode: E4, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Discovery interview

## Purpose
Understand before you produce. Find out what the person actually needs, in few questions, before anyone plans or builds.

## Step 0
Read what the person already said. Do not ask what they already answered. List anything you could not read as Unread.

## When to use / not
Use when a request is vague, new, or for someone else. Not when the answer is already in the record: look it up instead.

## Modes
Interactive. One round at a time.

## Procedure by slot
1. Strategize: write the one thing you need to learn.
2. Suspect: list what could mislead you (their words may not match their need).
3. Anticipate: pick at most 3 questions for the round.
4. Act: ask in plain words, in depth order: describe (what happened), explain (why), predict (what if it changes), estimate (how long or how much), delegate (exact steps). No skipping levels.
5. React and recognize: restate what you heard in one line and ask if that is right.
6. Calculate: note what was surprising for the next round.
Rules: no jargon from the harness. Fewer, sharper questions beat a pile. Say what you could not read.

## Output contract
A short plan in the eval's format (rounds, tagged questions, an Unread line) and, after the interview, a one-paragraph summary of the need.

## Delivery contract
Questions go to the person only with the requester's yes when sent in someone's name.

## Quality gates
`python3 evals/run.py discovery-interview`. A pass checks form only, not whether the questions are good.

## Compound step
Log what the person corrected in routines/learnings.md.

## References
packs/discovery-interview/fixtures/
