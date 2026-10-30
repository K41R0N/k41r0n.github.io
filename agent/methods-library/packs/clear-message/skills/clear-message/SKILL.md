---
name: clear-message
description: Helps someone say one thing clearly to a specific listener, with proof instead of adjectives.
argument-hint: "[what they want to say and to whom]"
version: 0.1.0
metadata:
  harness:
    lane: L2
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Clear message

## Purpose
Take something complicated and give the listener only what they need to get it.

## Step 0
Ask what they want the listener to know or do. Say what you are guessing. Source note: structure adapted from a work template of unconfirmed authorship.

## When to use / not
Use for "how do I explain or communicate this clearly". Not for full strategy (strategy-canvas).

## Modes
One.

## Procedure by slot
1. Strategize: write the point in one sentence. If it takes two, there are two messages.
2. Suspect: name who is listening and what they doubt.
3. Anticipate: for each doubt, find proof you can source. Facts you cannot source are marked as guesses.
4. Act: write a this-not-that. Replace each adjective with the thing you did or can show.
5. React: if the idea is hard, add one analogy to something the listener already knows.
6. Recognize: cut anything the listener would have to look up.
7. Calculate: write the one-sentence version and say it out loud. Then run asker-fit.

## Output contract
A note in the eval's format.

## Delivery contract
Words that go out under his name need his yes.

## Quality gates
`python3 evals/run.py clear-message`. Clean means the structure is there and every proof has a source. It cannot tell whether the message is true or lands.

## Compound step
Log which phrases confused people in routines/learnings.md.

## References
packs/clear-message/fixtures/, packs/asker-fit, knowledge/ethos/ethos.md (items 5, 14, 17, 33)
