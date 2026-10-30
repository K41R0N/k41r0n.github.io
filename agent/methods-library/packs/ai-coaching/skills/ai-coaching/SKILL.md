---
name: ai-coaching
description: Coaches a friend or colleague to use AI better by asking first, then fitting timers, checkers, formats and processes to their tasks.
argument-hint: "[who is asking and what they use AI for]"
version: 0.1.0
metadata:
  harness:
    lane: L2
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# AI coaching

## Purpose
Help someone get more from AI so they spend their time on the 10 percent that is their own insight and taste.

## Step 0
Source: his chat answer, 9:09 PM 2026-10-28, pending his confirmation. Say which parts come from it.

## When to use / not
Use when a person asks how to use AI or a harness better. Not for choosing a tool (use the tool-check path of advice-answer).

## Modes
One.

## Procedure by slot
1. Strategize: ask what they use it for and what is useful to them. Do not recommend anything first.
2. Suspect: find tasks where they need better research, more consistency, or that are repetitive.
3. Anticipate: for each task, pick the aid that fits: a timer, a checker, a format or a process.
4. Act: write the setup in plain words, one aid per line, tied to its task.
5. React: say what stays theirs, the deep insight and taste. Do not offer to replace it.
6. Recognize: give one next step they can do this week.
7. Calculate: run asker-fit on the result.

## Output contract
A note in the eval's format.

## Delivery contract
He approves the words before anything goes out in his name.

## Quality gates
`python3 evals/run.py ai-coaching`. Clean means the note asks first and covers every task. It does not mean the coaching is good.

## Compound step
Log which aids people actually kept using in routines/learnings.md.

## References
packs/ai-coaching/fixtures/, packs/asker-fit, knowledge/voice/chat-samples.md
