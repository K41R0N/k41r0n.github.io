# Iteration protocol: make changes, then verify their effects

Use this loop when a draft or system needs more than one revision. Each round should answer a specific question and leave the work in a known state.

## The loop

1. **Capture the current state.** Keep the prior version, current brief, relevant sources, and the feedback being addressed. Identify the change that would count as success.
2. **Classify the problem.** Separate factual, structural, compliance, audience, style, and length issues. Avoid treating every comment as a sentence-level edit.
3. **Choose a bounded change.** State what is changing and what must remain stable. Prefer one coherent change set over unrelated edits bundled together.
4. **Apply the change at the right level.** Repair the root cause: premise before structure, structure before line polish, source before factual wording, and deletion before rewriting for length.
5. **Check the result.** Run deterministic checks first, then review the changed material in context. Verify the requested fix and look for regressions elsewhere.
6. **Reopen invalidated checks.** Any substantive rewrite can invalidate a prior factual, structural, or style review. Re-run the relevant checks after the last meaningful change, not only before it.
7. **Close the round.** Record what changed, what passed, what remains open, and the next decision. Do not call work complete while a required verification is pending.

## Keep revisions controlled

- Compare against the previous version and the brief. A revision should not silently expand scope or replace the user's thesis.
- If an edit creates a new issue, fix it before moving on; don't layer another patch over a broken state.
- For long-form work, measure countable qualities before and after a subtraction or structural pass. Counts inform judgment; they do not replace it.
- For systems and repeatable processes, test each change on a known case and a counterexample. Preserve failures as regression examples.
- Use automation only for rules that can be stated and tested. Keep human judgment visible and keep a manual procedure available if a script cannot run.

## Stop conditions

Stop iterating when the agreed objective is met, the checks relevant to the final changes pass, and remaining findings are either deliberate choices or clearly named blockers. If the brief or evidence is missing, pause the affected work and ask one focused question rather than inventing a direction.
