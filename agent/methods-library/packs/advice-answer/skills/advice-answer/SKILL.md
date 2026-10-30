---
name: advice-answer
description: Drafts an answer to a question someone put to Alejandro, in plain words, with what is sure, what was checked and what is unknown, and passes money, legal and health questions to him.
argument-hint: "[the question, who asked, what they know]"
version: 0.1.0
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D1, mode: E4, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Advice answer

## Purpose
Answer the people who ask Alejandro for advice the way he actually works: understand before you produce, say what you are sure of, and never paper over a gap. A good answer to his mom or to a client runs on the same rules - the register changes, the honesty does not.

## Step 0
Read the question and everything the asker already said. Work the ladder in order: his words in context first, then harness canon, then live retrieval. Never answer from recall when retrieval is possible, and attempt retrieval before asking. If something pointed at cannot be opened, say so first - never fill the gap from a title.

## When to use / not
Use for any question put to him. Not to send anything: a draft goes to him, and nothing goes out in his name without his yes. Not for money, legal or medical decisions, which are his judgment: draft the framing, mark Needs him: yes.

## Modes
Interactive. Headless only returns the draft and the check result.

## Procedure by slot
1. Strategize: restate the question in one line. Then the gate: name what the answer would rest on. Thin material stops the draft - no stake, no timing, a core claim resting on a weak source, a load-bearing fact that cannot be retrieved, or fewer than two independent sources. Any of those means one sharp question first, never generalities.
2. Suspect: what could the asker be missing or assuming? What would make this advice wrong?
3. Anticipate: choose the asker's level, plain or technical. Family and most friends are plain.
4. Act: write the answer first, short. Then four lines: Sure (what you can stand behind), Checked (what you actually looked at), Not known (the gaps), Needs him (yes or no).
5. React and recognize: run the checks. Fix FAIL items. A WARN is for him to see.
6. Calculate: note what the asker asked that the draft did not cover.

Rules: no invented anecdotes, numbers or sources. Numbers carry a source marker. No harness jargon for plain askers. Fewer, sharper questions. When sources disagree, report every value and which one you used - never resolve a contradiction silently. Outward answers carry his method, never client names, figures or vocabulary. A gap stays marked; it is never filled to meet a deadline.

## Output contract
A draft with header (asker, level, sent_as: draft) and the five sections the eval reads. Every draft lands in one of three states: Answered; Answered with a hole, the hole named; or Cannot answer, with the one-line fix that would make it answerable. A clean cannot-answer is a deliverable. A shrug is not.

## Delivery contract
To him, for review. When he approves a send in his name, add approved_by and set sent_as: him.

## Quality gates
`python3 evals/run.py advice-answer`. A clean result means these patterns were absent. It does not mean the advice is right or sounds like him. That is his call.

## Compound step
When he edits a draft, log what he changed in routines/learnings.md. Two repeats make a rule. Do not use his edits as voice rules until he confirms them.

## References
packs/advice-answer/fixtures/, knowledge/ethos/ethos.md
