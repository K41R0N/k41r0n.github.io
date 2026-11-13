# Review Protocol: Adversarial Editing Until It Clears

The founding session took three review rounds to clear the author's bar, and each round caught things the previous one couldn't. The sequence matters: mechanical sweep → line edit → independent adversarial review → adjudication → verification pass → knock-on read. Never collapse these into one pass; each lens is blind to what the others see.

## Round order

1. **Mechanical sweep (grep).** Lexical bans, register bans, hardcoded figures. Cheap, do it first and again last.
2. **Self line-edit.** Read the whole file; fix redundancies across pieces, weak lines, terminology collisions. You will be partially blind to your own patterns; that's what round 3 is for.
3. **Independent adversarial review.** A fresh-context reviewer (subagent) with no drafting history. Give it the draft, the voice samples, and the five lenses below. Demand ranked findings with exact quotes and concrete rewrites, and a final verdict.
4. **Adjudication.** Apply, reject, or modify each finding. Rules below.
5. **Verification pass.** A second fresh reviewer checks explicit pass/fail claims about the fixes and hunts for new tells the rewrite introduced.
6. **Measured subtraction pass (anti-LLM pass), ALWAYS LAST.** Run the counters in `references/structural-audit.md` before and after; report both sets of numbers in the delivery note. Any substantive rewrite in rounds 3-5 re-opens this pass; never ship on the strength of a structural review that predates the last rewrite. This rule exists because the John op-ed shipped a V2 that fixed argument, facts, and compliance and skipped the subtraction; it came back in one read.
7. **Knock-on read.** A full human read of the final file, hunting specifically for edit artifacts: phrases duplicated into adjacent sentences, repeated markers across pieces, broken grammar at edit seams, double colons, referent-before-definition seams (an inserted sentence using a term one clause before the sentence that introduces it), and repeated naming constructions the edits created.

## The five review lenses (give the reviewer all five, in order)

1. **Forensic structural read.** "You are an expert at detecting LLM prose from structure alone. Ignore word choice." Paragraph shapes, sentence-length rhythm, figure inventory, opener/closer symmetry across the set, callbacks. Report every structural pattern repeating across 3+ pieces, with quotes.
2. **Editor's read.** Where does the argument coast, restate, or reach? Which sentences are ornament? Which analogies do real work? What would a great editor cut?
3. **Cross-piece redundancy.** Any fact, metaphor, or sentence shape in more than one piece.
4. **Voice fidelity.** Against the actual samples (op-ed, explainer, seeds), flag imitation flourishes vs the natural register. Cloning a known aphorism of the author's is the most detectable ghostwriting failure.
5. **Fact-check and compliance.** Web-verify historical anchors (names, dates, causation); check the the client gates (pass-through framing, agent attribution, qualified security claims, yield never recommended, Laniakea gate, register bans). Then go one level deeper than the facts, because the worst catch so far lived there: **verify the inference against the standard source on the episode**, not just the data points (the John op-ed's central V1 inference was arithmetically sound and affirmatively contradicted by the canonical decomposition of the same event). Also check: quotation integrity (no ellipsis that deletes a load-bearing clause; a statute quote gets read against the statute); no denominator switching between compared figures; forecast pieces must contain a falsifiable test (a claim that "gets to be right either way" gets rewritten until it can be wrong); time-deixis ("last November") parses correctly at the intended publish date.

Always demand: "a verdict: would a skeptical editor who reads LLM output daily clock this set, and if so from what, precisely." The verdict, not the finding count, is the exit signal.

## Adjudication rules

- **Seeds win.** If a finding attacks material that came from the author's seed (the Maker line, the black-box image, a phrase he wrote), the seed stays. Note the call for him instead of silently applying or silently ignoring.
- **Verify the reviewer.** Reviewers err. Session precedents: one reviewer misattributed which seed owned the black-box image; another over-weighted agent proof points that were actually Playbook-confirmed. Check factual objections against sources before applying.
- **Fix the class, not the instance.** A flagged antithesis is one of a class; sweep the whole set for the class and bring it under budget, don't just patch the quoted line.
- **Beware regression-to-mediocrity.** Applying every stylistic suggestion sands the voice off. Keep the best instance of a flagged pattern; cut the rest.
- **Document judgment calls** in the delivery note so the author can overrule.

## Verification pass template

Give the second reviewer explicit, checkable claims, e.g.: "1. The six openings no longer share one macro (count them). 2. Ring composition is no longer six-for-six (which pieces end off-ring?). 3. Paragraph-final epigram rate has dropped (sample two pieces, count kickers vs flat endings). 4. Negation-corrections ≤1 per piece (count per piece). 5. Duplicate proof points removed (name any). 6. Anchor facts corrected. 7. Lexical bans hold." Include a corpus-collision claim ("no line or shape from references/corpus-registry.md appears") and a seed-echo claim ("no seed phrase is reprinted verbatim in new material"). Then: "List any NEW structural tells the rewrite introduced, max 5, with quotes." Pass/fail per claim, evidence required. Verification catches what the first reviewer's fixes created: on Capital Routes V3 the verifier found three seed-echoes and one referent-before-definition seam that the adversarial round's own repairs had introduced.

## Exit criteria

Ship when: the verdict no longer names a structural pattern; no pattern appears 3+ times across the set; every anchor is fact-verified; every remaining flagged item is a documented judgment call; and the final knock-on read is clean. the author's instruction stands: as many rounds as it takes.
