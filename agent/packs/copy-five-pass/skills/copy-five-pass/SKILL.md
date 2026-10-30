---
name: copy-five-pass
description: Runs five deterministic passes over a draft and reports failures and warnings for a person to judge.
argument-hint: "[path to draft]"
version: 0.1.0
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D1, mode: E4, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Copy five-pass

## Purpose
Catch the mechanical problems in a draft before a person reads it. The person decides whether it is good.

## Step 0
Check the draft has a header with `context: external` or `internal`. Say plainly if any source cited in the draft was not read.

## When to use / not
Use on any draft before review. Not to write or rewrite copy, and never to decide whether it sounds like him.

## Modes
Interactive or headless. Headless ends with a fixed line: `clean`, `warn N` or `fail N`.

## Procedure by slot
1. Evidence: every number and every "first / only / best" carries a source marker.
2. Unresolved: no TODO, TBD or placeholder left.
3. Filler: generic phrases and a dash budget (a budget, not a ban).
4. Plain reading: flag very long sentences. Offer a lay rendering as an addition, marked as one.
5. Authority: external copy needs `approved_by`. Nothing goes out in his name without his yes.
FAIL means fix or escalate. WARN means a person looks. Clean means only that these patterns were absent.

## Output contract
List of ids with the offending text, then the fixed ending line.

## Delivery contract
Report to the requester. Do not edit the draft unless asked.

## Quality gates
`python3 evals/run.py copy-five-pass`.

## Compound step
When a person overrides a warning, log it in routines/learnings.md. Two repeats retune the pass.

## References
packs/copy-five-pass/fixtures/
