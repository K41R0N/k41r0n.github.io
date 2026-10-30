---
name: attention-graduation
description: Rates a way of working by depth and attention slot, then says what may be automated and what must stay with a person.
argument-hint: "[describe the work, or paste its steps]"
version: 0.1.0
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Attention graduation

## Purpose
Turn the way a person works into steps an agent can follow, honestly rated, with nothing automated before it is understood.

## Step 0
Read the work description. If it is only a title, stop and ask for the steps. Say plainly anything you could not read.

## When to use / not
Use to rate or improve a repeatable way of working. Not for judging the quality of one output (that is a person's call).

## Modes
Interactive by default. Headless only if the caller says so.

## Procedure by slot
Depth ladder, in strict order, no skipping: describe (what), explain (why), predict (what if), estimate (how long, how much), delegate (exact steps).
Time slots around the action: strategize, suspect, anticipate (before); act; react, recognize, calculate (after).
1. Write what is done in each slot at its honest depth. D1 is "lists what was done". Do not raise a depth without evidence.
2. Capability depth is the lowest slot depth.
3. Choose the least inference the depth allows: D1 assist only (E4), D2 fixed steps with bounded fills (E3), D3 selection among known options (E2), D4 mostly script (E1), D5 script (E0).
4. A script is written only after two identical manual runs. Judgment steps are never scripted.
5. Name the slot holding the capability back and the one thing that would raise it.

## Output contract
A profile in the format the eval reads (depth, mode, manual_runs, one line per slot) plus the holding-back slot.

## Delivery contract
Return the profile to the person who asked. Nothing is changed or run without their yes.

## Quality gates
Run `python3 evals/run.py attention-graduation`. A pass means the profile is consistent. It does not mean the ratings are right; that is a person's call.

## Compound step
Log a correction in routines/learnings.md. Two repeats make a rule.

## References
packs/attention-graduation/fixtures/
