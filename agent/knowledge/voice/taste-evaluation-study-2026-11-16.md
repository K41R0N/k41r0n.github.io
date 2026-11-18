---
type: Research
status: candidate, not adopted
source: Every / Michael Taylor and Dan Shipper, read 2026-11-16
---
# Taste checks and reference-based voice evaluation

## Decision
Keep the existing writing method. Add this as evidence for its next calibration, not a replacement pipeline. The useful combination is case-linked checks for recurring corrections plus a reference-based comparison for the qualities a checklist misses. Neither proves the author approves a draft. No writing, optimization run, installation or publication is authorized by this study.

The two Every pieces answer different questions:
- Experiment 045: can explicit editorial corrections improve a short-summary instruction set against those corrections?
- How I Finally Got AI to Write Like Me: can optimized instructions generate drafts judged closer to an author's actual essays than a one-shot style guide?

Passing binary checks, winning a resemblance comparison, and receiving the author's approval are different outcomes. Report them separately.

## 1. What was actually reported

### Dan Shipper: newsletter corrections into checks
Eight real Context Window cases yielded 74 yes/no checks. Prompt, desired final and feedback were retained. Instructions evolved v1 to v9. The publisher reports isolated zero-context runs on four models, blind-graded by Sonnet 5.5. Final counts: Gemini 4 Hydrogen 60/74, Opus 5.5 58/74, GPT-6 Astra 58/74, Sonnet 5.5 56/74. These are their reported check-pass counts, not independently reproduced results or a probability that an editor accepts the output.

Limits: v1's 34-56% range is on seven initial cases; v9 is on the full eight-case/74-check set. The published page links no raw case lab, full checks, outputs, v1/v9 instructions, run counts, uncertainty or independent human grades. Its 25+ point headline is not an inspectable paired same-test effect. Seventy-four checks on eight cases are not 74 independent examples. Repeatedly optimizing on the same corrections tests regression, not generalization. The named models/settings are publisher labels, not a recommendation to switch models here.

### Michael Taylor: style-free briefs, reference gold, optimized guide
Author reports 185 posts / 335,000 words / 13 publications, with 54 held back; a later narrower run uses 30 recent Every articles. Suggested 12-25 same-format pieces is advice, not a validated universal minimum. Substance-only briefs retain thesis, outline, facts, experiences and sources but exclude hooks, phrasing and jokes. A fixed judge sees a real post and two drafts from the same brief; candidates swap order. Feedback tunes the guide, not the gold reference or judge mid-comparison.

The first chart shows 30 held-out posts, same writer model on both sides, averaged across Opus and Sonnet judges. Compared with the one-shot guide: no-guide wins 61% for Opus and 42% for Sonnet; autoresearch 95%/81%, GEPA 80%/89%, ce-optimize 86%/89%. These are relative wins, not voice accuracy. Optimizers beat that weak baseline, not a human editor. An important result is that no guide can beat the guide.

The second chart is a different experiment: 11 held-out Every posts, expected win rate against Opus 5.5 with the one-shot guide. Its 16% no-guide and 93% optimized Opus bars are not a 77-point increase in absolute writing quality or directly comparable to the first chart's 61%. Text says six writer models; the shown chart labels five. Underlying per-post results and the expected-win-rate fitting details were not linked in the newsletter. The reported 86% vs 70% order consistency is judge stability, not agreement with the author. Reported $27-$53 optimization cost and one-hour drafting turnaround are this author's observations, not a budget or forecast for this work. The author rewrote his own introduction and still uses human editors.

## 2. Evidence checked beyond the articles

- Pairwise Gold Triad source: keeps judge and gold fixed, compares challenger/incumbent, and proposes fill-in-the-middle tests. That older paragraph-completion task exposes surrounding author prose; it is not the same as style-free whole-essay reconstruction. Stable measurement does not guarantee a calibrated judge or global optimum. Win rates against changing incumbents are not absolute scores on a common scale.
- Linked write-like-me gist: README, skill and complete Python runner read, not executed or installed. Learn/tune/test split; style-free briefs; fixed one-shot opponent; swapped-order judgments; cached drafts; keep/revert guide optimization; held-out evaluation; optional no-guide comparison. This package implements its own autoresearch loop, not all three optimizers in the article.
- Code caveats: `compare` returns a random A/B verdict after three parse failures, contaminating scores instead of abstaining. `cmd_export` can export/install without a passing held-out gate. The no-guide test is optional. `prepare` randomly shuffles rather than reserving newest posts. Cached single drafts per prompt do not measure generation variation. README 20-40 ideal / eight minimum and skill's '>60% on 8+' success wording are package heuristics, not statistical guarantees. Do not import this runner unchanged.
- Every's personal-benchmark guide and Evals for Everyone require fixed inputs, first outputs saved, specific checks, human grades kept hidden from the judge, evidence for judgments, disagreement diagnosis, regrading all compared outputs after a check change, and another example. These support calibration, not 'all checks pass, author can leave'.
- MT-Bench paper sections 3.3-3.4 document position/verbosity/self-preference risks and swapped-order comparisons. This motivates calibration; its model-specific measurements do not establish today's judge accuracy for this author.
- Adaptive-data-analysis literature explains why reusing test feedback can overfit. No claim that a formal reusable-holdout algorithm is implemented here.

## 3. Fit against the actual existing work

| Existing source/work | Already present | Specific addition worth testing |
|---|---|---|
| `routines/copy-draft.md` and source-derived five-pass | Brief, one idea, current factual evidence, voice, structure, final gate | Freeze substance-only evaluation briefs so style changes are tested without changing the argument. Do not strip authored seed wording from live writing by default. |
| `routines/copy-review.md` and full review-pipeline source | Five separate reviews; creative lenses and all five Ogilvy questions; reader/offer fit; no lint-as-quality claim | Reusable regression cases for repeated corrections within relevant passes. Taste checks do not replace creative review or become a sixth/seventh pipeline. |
| `routines/writer-judge-loop.md` | Untouched draft + author's final, sealed edit predictions, independent hunk classification, max three inner rounds, edit-rate tracking | Turn evidenced edit deltas into scoped check candidates; compare old/new instructions on identical cases and private gold. Keep prediction quality separate from check pass rate and author edit burden. |
| `knowledge/voice/HARNESS.md`, voice-spec, do-dont, lexicon, registers | Form/content/evidence separate; client rules tested against own writing; measured essay traits, not proof | Model-specific guide evaluation against no guide, existing guide and candidate; register/language/version explicit. No Every-specific newsletter opener requirement in an essay guide. |
| `scripts/local/voice/checks.py` | Regex/mechanical warnings and failures, including proposed client rules | Code remains for exact checks. Interpretive yes/no checks need a calibrated judge and cited evidence, not a claim of determinism. The 32-word cap is still executable despite documentation rejecting it as a personal default; log this as pre-existing conflict, do not silently promote it. |
| `ledger.py`, `edit_rate.py`, `holdout_guard.py` | Seals prediction file; class coverage; added+cut/draft-words formula; 8-gram overlap check | These do not run a model benchmark or prove secrecy. A clean n-gram scan is not proof the writer never saw gold. Preserve independent access separation. |
| Existing verification report and compound log | False positives identified on own prose; old holdout partly spent | Fresh untouched recent samples needed for honest final tests. Do not relabel old calibration samples as unseen. |

Current work includes measurement scripts and synthetic ledger fixtures. That is not completed human calibration or an approved voice. The verification report also records a committed-spec/fresh-rebuild mismatch. This study records the gap; it does not certify or repair unrelated implementation.

## 4. Proposed bounded test, not started

Use the existing writer/judge loop's case folders, not a separate product or service. Keep reusable evaluation logic separate from author/client facts, examples, corrections and approval data. Public method documentation can explain the protocol; private cases and gold stay private.

1. Audit available historical pairs without generating new prose. A pair needs the original brief/source, untouched draft, actual author's edited final, dated feedback, reader, language/register and decision provenance. An approved delivery link, an agent-generated revision, a rejection or a general essay is not automatically an author-edited gold pair. Unknown final remains unknown.
2. Freeze disjoint learning/tuning/final-test manifests before any optimization. Group near-duplicates and revisions in one split. Reserve recent untouched same-register samples if available; otherwise state that generalization cannot yet be measured. Do not manufacture a target case count from a package minimum.
3. Each check candidate records correction source, scope, question, pass/fail examples, quote exemption, applicability, evaluator type and status. One requirement per check. Invalid output, missing context and not-applicable must not become passes or coin-flip scores. A vague 'sounds like me' check is not useful by itself.
4. Calibrate on known accept/reject judgments with the author's verdict hidden. Measure false passes and false alarms separately. Mechanical checks run in code; judgment checks cite text. Fix the check or judge when they disagree with the source verdict. Do not rewrite the author's verdict to fit the evaluator.
5. Only after the writing hold is explicitly lifted: compare no guide / existing guide / candidate with the same complete brief, writer, model version/settings and independent repeated samples. Judge against gold with identities hidden, both orders, frozen rubric; keep splits/abstentions visible. Optimize on tuning cases only; predeclare a bounded round/cost budget. No spending or subscription consumption assumed here.
6. Final readout: case-level wins/losses/splits and judge-order agreement; evidence-check failures; author's blinded preference and edit burden; same-register and cross-register results separate. A higher check score with worse human preference or invented substance fails. Any final-test-driven revision spends that test set and needs a fresh final test. No numeric result auto-publishes, graduates a process or lifts approval.

Possible first candidate: a recurring correction about inflated interpretive prose, grounded in its original correction and an actual accepted contrast. Keep long sentences that the author uses well as negative controls, so a 'crispness' check cannot become another universal length cap. This is a candidate design, not a newly confirmed voice rule.

## 5. What remains unchanged
Five writing passes and five separate review passes. Current factual sourcing. Author's opinions and experiences never invented. Reusable method versus dataset/context separation. Voice-writing hold and approval of outgoing copy. No installation, new account, optimizer run, commercial adoption, corpus upload to Every or promised benchmark transfer.

## Source ledger and coverage

Full supplied experiment read in live page, original response and rendered capture preserved privately. Second supplied Frontier reader route redirected to sign-in; complete publisher-delivered newsletter recovered from the owner's connected inbox, preserved privately and read in full. Canonical article also fetched; charts downloaded and inspected directly. No third-party mirror used. Full linked triad article and gist read; no tool installed. Companion experiments 031/030/024/028 exposed abstracts only; 031's live sign-in gate confirmed, so no unobserved findings attributed to them.

- https://frontier.every.to/experiments/turn-your-daily-newsletter-edits-into-ai-checks-and-watch-every-frontier-model-jump-25-points
- https://frontier.every.to/read/how-i-finally-got-ai-to-write-like-me
- https://every.to/also-true-for-humans/how-i-finally-got-ai-to-write-like-me
- https://www.saxifrage.xyz/post/pairwise-gold-triad-eval
- https://gist.github.com/hammer-mt/200d26db9beebc42b6c81486c48cd4a1
- https://every.to/also-true-for-humans/how-to-create-your-own-personal-ai-benchmark
- https://every.to/context-window/evals-for-everyone
- https://checks.every.to/p/mikes-checks (score semantics only, not experiment045's missing lab)
- https://arxiv.org/html/2306.05685v4 (sections3.3-3.4 read for evaluator limitations)
- https://cacm.acm.org/research/guilt-free-data-reuse/ (introduction read for adaptive-reuse caveat)

Research interpretation, not the authors' original source. Original captures are private; raw mail, personal tracking links, private corpus and client examples are excluded from this public-readable repository note.
