---
name: asker-fit
description: Fits an advice draft to the person asking, in plain words, with one next step and honest confidence.
argument-hint: "[the question and who is asking]"
version: 0.1.0
metadata:
  harness:
    lane: L2
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D1, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Asker fit

## Purpose
People who ask him questions are not experts. A good answer is one they can act on today.

## Step 0
Say who is asking and what they already know. If you do not know, say so and assume a beginner.

## When to use / not
Use on every advice draft, after advice-answer. Not for notes only he will read.

## Modes
One.

## Procedure by slot
1. Strategize: write the asker's level: beginner, informed or expert.
2. Suspect: find the one question under the question. "How do I make a campaign" is often "where do I start".
3. Anticipate: answer first, then the reason, in short sentences.
4. Act: no buzzwords. A technical word needs plain words next to it, or is dropped.
5. React: give one next step the asker can do today.
6. Recognize: say what you are sure of, what you checked, and what you do not know.
7. Calculate: read it as the asker. Cut anything they would have to look up.

## Output contract
A draft in the eval's format.

## Delivery contract
It goes out only after he approves the words. The checks cannot tell whether the advice is right.

## Quality gates
`python3 evals/run.py asker-fit`. Clean means it is plain and short, not that it is right or sounds like him.

## Compound step
Log the questions people ask most, and where a draft confused them, in routines/learnings.md.

## References
packs/asker-fit/fixtures/, packs/advice-answer, knowledge/ethos/asker-lens.md
