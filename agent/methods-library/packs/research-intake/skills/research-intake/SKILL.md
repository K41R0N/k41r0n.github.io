---
name: research-intake
description: Takes in a burst of messages on one topic, keeps one canvas, finds the threads that connect them, and proposes what to do next.
argument-hint: "[topic, and 'binge' when a burst is coming]"
version: 0.1.0
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D1, mode: E4, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Research intake (data binge mode)

## Purpose
When he says "I'll send you a lot of messages, expect them all to be on the same topic", take them in without interrupting him, keep them in one place, and find what connects them.

## Step 0
Open or create the canvas for the topic. Say plainly anything you could not read (a link, a video, a file). Never infer its content from a title.

## When to use / not
Use for a burst of related notes, links and thoughts. Not for a single question (answer it) and not for sources that are confidential to a client: a client item gives method only.

## Modes
Binge: during the burst, reply with at most a one-line receipt. No questions until he signals the burst is over, unless a source cannot be read.

## Procedure by slot
1. Strategize: write the topic in one line.
2. Suspect: some messages may be off-topic. Put them in Unsorted, never silently drop or force-fit them.
3. Anticipate: keep one numbered entry per message, with its source.
4. Act: as entries arrive, sort them into Labels, Topics, Use cases, People and Entities. People are names only, no contact details.
5. React and recognize: when the burst ends, find threads, each tying at least two entries together.
6. Calculate: propose outputs from the threads: next steps, more sources to look at, an action plan, a landing page or a course. Every output is marked proposed.
Hand off: open questions go to discovery-interview, factual claims to claim-verification.

## Output contract
The canvas in the eval's format plus the proposed outputs. Nothing is published, sent or built.

## Delivery contract
Return the canvas and proposals to him. A landing page or course is only a proposal until he says yes to that exact thing.

## Quality gates
`python3 evals/run.py research-intake`. Clean means every entry has a source and a place, threads cite real entries, and nothing is marked published. It does not mean the threads are right.

## Compound step
Log what he corrected about the threads in routines/learnings.md. Three repeats become a rule.

## References
packs/research-intake/fixtures/
