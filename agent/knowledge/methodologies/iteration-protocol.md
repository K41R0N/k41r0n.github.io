---
id: 01M69AYGQX4WA81GHC66CA31RG
type: Method
title: "Iteration protocol: make changes, then verify their effects"
description: "Revision loop with bounded edits, invalidated-check reruns, measured subtraction where applicable, and a final knock-on read."
confidence: inferred
source: "10-skills/sky-thought-piece/references/review-protocol.md@e2c6fcdacf32783a72f1ddca06ee0e4edc8038d4"
updated: 2026-10-31
class: S0
tags: [copy, verification]
---
# Iteration protocol: make changes, then verify their effects

Use this loop when a draft or system needs more than one revision. Each round should answer a specific question and leave the work in a known state.

## The loop

1. **Capture the current state.** Keep the prior version, current brief, relevant sources, and the feedback being addressed. Identify the change that would count as success.
2. **Classify the problem.** Separate factual, structural, compliance, audience, style, and length issues. Avoid treating every comment as a sentence-level edit.
3. **Choose a bounded change.** State what is changing and what must remain stable. Prefer one coherent change set over unrelated edits bundled together.
4. **Apply the change at the right level.** Repair the root cause: premise before structure, structure before line polish, source before factual wording, and deletion before rewriting for length.
5. **Check the result.** Run deterministic checks first, then review the changed material in context. Verify the requested fix and look for regressions elsewhere. For long-form writing, compare relevant structural counts and word count before and after a subtraction pass; counts are evidence for review, not an automatic quality score.
6. **Reopen invalidated checks.** Any substantive rewrite can invalidate a prior factual, structural, or style review. Re-run the relevant checks after the last meaningful change, not only before it.
7. **Run the final subtraction and knock-on read.** After the last substantive rewrite, re-run any invalidated review and mechanical checks; for structural writing work, make the measured subtraction pass last, then read the whole artifact for edit seams, repetitions, and broken referents.
8. **Close the round.** Record what changed, what passed, what remains open, and the next decision. Do not call work complete while a required verification is pending.

## Choose the review depth

| Work | Minimum loop |
|---|---|
| Short comment or paragraph | Mechanical check if applicable, self-edit, measured subtraction where the relevant writing checks apply, whole-text read. |
| Standard post | Mechanical sweep, self-edit, independent review/adjudication when stakes warrant, final subtraction, whole-piece read. |
| Article, first post, correction, red-line piece | Full sequence: mechanical sweep, self-edit, independent adversarial review, adjudication, fresh verification, measured subtraction last, knock-on read, delivery note and required approvals. |
| Non-writing process or system | State a testable success condition; test a known case and counterexample; preserve failures as regression examples; keep manual fallback. Do not run essay-shape counters. |

The review protocol uses stakes and artifact type to scale effort; a checklist is not a substitute for judgment or approval.

## Long-form subtraction counters

Use these only for the essay/manifesto forms governed by the source audit. Measure before and after the last substantive revision and include both readings in the delivery note. Reopen the subtraction pass after any later substantive change.

| Counter | Essay / op-ed guide | Manifesto guide |
|---|---:|---:|
| Flat paragraph endings (long, factual, unshaped) | At least 1/3 | At least 1/4 |
| One-sentence punch paragraphs | ≤1; only as answer to hardest objection, not repeated subhead | ≤1 outside deliberate refusals set |
| True negation-corrections in new material | ≤1 | ≤1; seed instances stay |
| Meta signposts | 0 | 0 |
| Ring composition across a set | At most 1/3 | Follow seed / genre call |
| Corpus collisions | 0 | 0 |
| Word count through a fix round | Flat or down; cuts from scaffolding, not argument | Same |

Also count final-sentence word counts, punch paragraphs, negation patterns, and meta signposts; check ring, corpus collisions, and prior-version word-count delta. Counters are prompts for human review. Confirm actual hits by reading them; a regex hit is not automatically a violation. These values come from a specific writing standard and do not transfer to reports, briefs, or systems by default.

## Keep revisions controlled

- Compare against the previous version and the brief. A revision should not silently expand scope or replace the user's thesis.
- If an edit creates a new issue, fix it before moving on; don't layer another patch over a broken state.
- For long-form work, measure countable qualities before and after a subtraction or structural pass. Counts inform judgment; they do not replace it.
- For systems and repeatable processes, test each change on a known case and a counterexample. Preserve failures as regression examples.
- Use automation only for rules that can be stated and tested. Keep human judgment visible and keep a manual procedure available if a script cannot run.

## Scale the loop to the work

A small comment or paragraph can use a short mechanical check, self-edit, and final subtraction/read. A standard post adds an independent review and whole-piece read. An article, first post, correction, or red-line piece warrants the complete sequence: mechanical sweep, self-edit, independent adversarial review, adjudication, verification by fresh eyes, measured subtraction last, knock-on read, then delivery note and required approvals. The specific review lenses should fit the artifact; an essay's structural-tell review is not a substitute for fact checking.

## Evidence basis and limits

The source is `10-skills/sky-thought-piece/references/review-protocol.md`, which records the failure where a substantive revision invalidated an earlier structural review and the final subtraction pass was skipped, then specifies the stages, verification, measurement, and knock-on read. `references/structural-audit.md` gives the counters and genre thresholds above, and documents why the pass reruns after substantive revisions. The compendium E4/E9 supports scaling by artifact stakes. The generic loop is an organizing synthesis; the counters are specific to the cited long-form forms and do not certify quality.

## Stop conditions

Stop iterating when the agreed objective is met, the checks relevant to the final changes pass, and remaining findings are either deliberate choices or clearly named blockers. If the brief or evidence is missing, pause the affected work and ask one focused question rather than inventing a direction.
