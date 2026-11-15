---
name: live-number-answer
description: Answers questions that quote live numbers. Probes source capability first, routes each metric to a canonical source with a pre-decided fallback, refuses instead of substituting when a fetch fails, labels every value with source, as-of, and status, and ends with a human-verify step. All dataset facts live in the dataset's register, not in this method.
argument-hint: "[the question and the dataset register to answer from]"
version: 0.1.0
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Live number answer

## Purpose
A number quoted without a live source, a date, and a status is a liability. This method answers number questions so that every figure is traceable and every failure to fetch is a declared refusal, never a substitute.

## Method and data separation
This skill carries no dataset facts. Each dataset supplies its own register (see datasets/demo/ for two invented examples and the schema): sources with capability classes, and metrics with kind, canonical source, pre-decided fallback, and staleness threshold. Swapping datasets means swapping the register file only; this skill and its checks never change. Derived values are computed from their components, never fetched directly. A derived entry declares formula as the exact ratio "A / B" over its two declared components; malformed formulas, unsupported operators, and cyclic derived inputs are rejected when the register loads, and a zero denominator or a reachable-but-unfetched value defers instead of producing a number.

## Step 0
Say which dataset register you are answering from and run the capability probe: which of the register's sources can this environment actually reach, and which validation levels can run. Unreachable levels are skipped and said so, never silently omitted.

## Procedure by slot
1. Strategize: list the metrics the question needs and read their register entries.
2. Suspect: for each metric, name the canonical source and the pre-decided fallback. Never improvise a fallback at fetch time.
3. Anticipate: run the probe. Record each source as reachable yes, no, or unknown.
4. Act (fetch): fetch from the canonical source. Only an explicit reachable yes counts; unknown fails closed, same as unreachable. If the canonical is unreachable and a fallback was pre-decided, use the fallback and say so. If sources disagree, use the canonical value and note the discrepancy.
5. React: label every value with its status: ok, stale (latest data older than the register's threshold), partial, unavailable, manual, or error. Only ok values may be pasted as final. Never smooth, fill, or estimate.
6. Recognize: when a fetch fails with no pre-decided fallback, issue the fixed deferral: state the metric, that its sources could not be reached, and when to retry. Never substitute a stale, remembered, or invented number.
7. Act (compose): each quoted value carries its source, as-of date, and status. Keep a provenance sidecar per value: method, sources, as-of, and fetch log, so a later reader sees what you saw.
8. Calculate: end with the human-verify step: present each ok value with source and timestamp and name what the human should confirm. A clean mechanical pass is not verification.

## Output contract
An answer note in the eval's format: probe and dataset headers, a Sources section, a Values section, a Refusals section, and a Verify section.

## Delivery contract
Facts first, then explanation, then options, then recommendation. Unverifiable numbers stay out of client-facing copy.

## Quality gates
`python3 evals/run.py live-number-answer` and `python3 packs/live-number-answer/datasets/swap_test.py`. Clean means the discipline is visible in the note, not that the numbers are right.

## Reuse test
The swap test loads two different invented dataset registers and resolves metrics with the same resolver, unedited. It also covers boundary failures: canonical unreachable with pre-decided fallback, all sources unreachable, a derived metric, malformed or unsupported formulas, cyclic derived inputs, a zero denominator, and a reachable-but-unfetched value. Its output is the actual tested behavior of the separation; the paragraphs above are the design.

## References
