# Writing source inventory and implementation reconciliation

2026-11-16. Implementation record for issue #45, not a claim that voice is calibrated. The existing website repository remains the harness. No site copy, private source originals, chat export, client corpus or author's private edits were added by this change.

## Source inventory

| Source | What was inspected | How it is used | Boundary |
|---|---|---|---|
| Five-pass writing originals | Supplied methods archive; existing generalized five-pass routine and all five individual pass references read | Big idea, factual anchoring, voice, structure, risk, in order | Source-derived methods remain distinct from client facts and brand rules |
| Copy Review Engine | Existing full generalized review source and original framework reference read | Five separate critiques; all five creative lenses and all five Ogilvy questions | Four-versus-five prompt drift is recorded, not silently adopted |
| Client mechanics and craft | Original mechanics and craft read privately; existing personal false-positive report compared | Mechanism/actor/paragraph construction and contextual pattern diagnosis | Client sentence caps, filler bans, legal policy, examples and reader assumptions do not become personal canon |
| Supplied anti-slop standard | Original 18,604-byte standard in the supplied archive read in full | Seven tests, architectural tells, preservation, modes and scope, adapted in refs/anti-pattern-method.md | Its platform budgets are not universal rules; upstream attribution is preserved, not claimed as a fresh code audit |
| External tooling scan | Existing refs/tooling.md plus relevant current slop-guard/slop-score README sections | Candidate corpus fitting and comparison concepts | No install, API call, adopted dependency or measured quality benefit |
| Handwritten mimicry plan | Finding 12 and the recovered source-reading record | Person-specific harness, thoughts/refs separation, linguistic measurements, copy/AEO path | Outline was read; it is not a missing unreadable image or a complete sentence-rule guide |
| Author corpus | Existing raw/holdout/excluded manifests, spec builder, numerical output, voice spec, rules and lexicon inspected | Selected same-register form examples and measurements | Nine raw essays build the spec. Two historical test essays are partly spent for rule calibration. Thirteen unverified pages remain excluded |
| Chat voice and corrections | Existing chat sample, run log, learnings and original writing-related owner messages recovered | Selected sample and correction evidence is mandatory per run | Chat is a register, not automatically an essay target; a rejection is not an edited gold final |
| Nat Eliason | Complete historical reading of the supplied article recovered and read; contemporary mirror compared; original narrow adoption exchange recovered | Writer/judge split, top-three fixes, max-three rounds, source fidelity, sealed predictions, independent edit classification | Original attachment bytes have not been re-retrieved. The historical read is not republished as an original. Reported edit rates are the author's observations, not our measured performance |
| Every experiment 045 | Prior complete source study, captures and methodological caveats retained | Correction-linked checks with separately held-out validation | Check counts and reused cases are not independent author-quality evidence |
| Every write-like-me article and linked implementation | Prior complete article/newsletter, charts, triad method and full linked runner study retained | Frozen guide/rubric, train/calibration/test separation, blinded swapped order and explicit abstention | No random fallback, optimizer adoption, optional pass bypass or unapproved spend |
| Attention Graduation Framework | Canonical document read, especially exact helpers, depth/mode caps, graduation and delivery | Exact evidence checks now; judgment stays D1/E4 and promotion stays separate | Two-run fidelity evidence is not a universal ban on building exact helpers |
| Harness Standard v0.3 | Relevant source sections: confidence/use, decision rules/shadow rollout, 9 capability/script/delivery, 10 lanes, 13 sensitivity | Versioned references, offline rules, scoped execution, branch review, private data outside git | Draft architecture is not a claim that this repo has the full foundry, Jev service, lock enforcement or automatic activation |
| Existing entrypoints and checks | Agent README, route.py, evals/run.py, draft/review/judge routines, corpus/check/ledger scripts, site contribution/write guard | One writing execution entrypoint; existing eval runner and routing point to it | Does not change production build scripts, deployment, packages or merge rules |

The machine catalog is `writing-source-catalog.json`. It carries method IDs and paths, not client examples. A run freezes their actual byte hashes together with its selected notes, voice samples, register, corrections and factual sources. Those are separate roles, not one blended prompt. Full source material is read in the appropriate pass; a reading declaration alone does not satisfy the application gate.

## Reconciled contradictions

### Client lint was acting as personal law

`checks.py` still assigned hard failures to the client 32-word cap, dash/exclamation/hashtag bans and mandatory short/long sentence pattern. Personal `do-dont.md` already said several of those rules failed his own writing or remained proposed. The default personal scope now reports client rules as INFO and unconfirmed craft prescriptions as WARN, never as adopted personal hard bans. The explicit client-candidate scope preserves the older checks for comparison, not as an approved client policy. Context warnings require a recorded human disposition at the final judge step. This change does not newly confirm any voice rule.

### Spec hashes were stale, measurements were not

A fresh rebuild had exactly the same measured numerical values and weighting but different stored file-byte hashes. This implementation updates only those stored hashes to the current raw files. The older spec remains in git history. The available evidence does not establish which historical edit changed each file's bytes, so this note does not invent that cause. `build_spec.py` uses newest-raw-relative recency weighting, not today's clock. It was not a time-dependence bug.

The Markdown generator now opens its sibling spec independent of current directory and emits the present paths and correct table column counts. The committed Markdown is regenerated from that unchanged measurement content. This is measurement, not new prose in the author's voice.

### Test-set claims were too strong

The raw-only spec check proves the numerical builder ignores the historical test folder. It does not restore secrecy to the two essays used for rule false-positive testing. New author-quality testing requires a truly untouched, same-register partition. The overlap helper checks shared 8-grams, not access history or original authorship. Neither a clear overlap scan nor a label saying 'unseen' proves isolation.

### Method versus judgment versus execution

The writing entrypoint enforces prerequisites, source-role applicability, exact evidence quotations, artifact linkage, sequence, actual pinned subprocess dispatch, runner-owned invocation IDs, reviewer/writer separation, complete creative fields, paragraph mapping, complete voice dimension fields, scoped deterministic checks and bounded revisions. It rejects failed and stale evidence rather than counting files.

A file cannot prove its own human authorship, a reviewer having a truly fresh mind or a quotation's semantic interpretation. For imported/manual receipts, turn IDs and identities remain auditable declarations and cannot complete a run. Dispatched invocations have runner-owned process IDs, input/output hashes and exit status. Original-source identity and imported label provenance still need independent verification. The caller must verify their original sources. No claim is made that these checks authenticate an arbitrary local caller or prevent someone with repository write access from editing the runner or policy. Source quotes plus rule-to-stage matching catch wrong/absent evidence; nuanced relevance remains independent review work.

## Evaluation status

`voice/evaluate.py` computes agreement with imported author choices in both blinded orders, order inconsistency, abstentions, a Wilson interval and first-order Brier score. It rejects missing labels, invalid results, changed guides/rubrics, mixed registers, overlapping IDs/bytes and known prior exposure. The evaluator never substitutes a random judgment. Same-case near duplicates and exposure outside its manifest still require independent review.

The evaluator is in shadow. Thresholds are deliberately unset pending author calibration, so no synthetic or imported score can produce a quality pass or publication state. Existing essays, approved links and agent revisions have not been relabeled as author-edited gold. No complete authenticated author-edited pair is present in the current `assets/voice-drafts/` checkout. That is a local inventory finding, not proof that none exists in private history.

The next author-quality experiment needs verified original brief/source, untouched draft, real author-edited final or a real blinded choice, original decision provenance, register, and a frozen rubric/guide. Keep those private. Fit on calibration data only; evaluating and then tuning from a final test spends it. In the live loop, preserve the draft/final pair, seal predictions before author editing and classify all changed hunks independently using the existing ledger. These measurements are distinct from pairwise resemblance agreement and binary check pass rates.

## What is and is not delivered

Delivered: one runnable, fail-closed process around the existing routines, a pinned host-adapter dispatch boundary tested through a complete synthetic CLI run, an offline evaluation importer/calculator, source-role/hash binding, scoped lint reconciliation, reproducible measurements, and adversarial contract tests. No production writing/reviewer host adapter is configured, so actual model execution is blocked rather than replaced by self-reported receipts. Connecting and testing the real host adapter remains open. New author-voice writing remains disabled. No quality claim, author-voice generation, corpus upload, external optimizer, paid run, publication, merge or autonomous graduation occurred.

The tests are explicitly synthetic software contracts, not mock evidence of successful author writing. They demonstrate that the machinery refuses particular invalid states. They cannot show that Alejandro likes a draft.

## Public sources

- Nat original link supplied by the owner: https://x.com/nateliason/status/2115803497773904292?a=pzfF1e8tdhqpCH_Ie10&s=19
- Contemporary mirror used only to compare the recovered historical reading: https://nitter.gq/nateliason/article/2115803497773904292
- https://github.com/eric-tramel/slop-guard
- https://github.com/sam-paech/slop-score
- Full Every primary sources and limitations: [taste-evaluation-study-2026-11-16.md](taste-evaluation-study-2026-11-16.md)

Private originals remain in the owner's existing source archive. This public-readable inventory intentionally omits client repository names, private source excerpts, chat IDs, messages and private source links.

Manual receipt imports can reach only evidence-complete-attested and cannot export a handoff packet. Full dispatched process completion still exports only draft-for-author-evaluation, never final or approved. Exact gate enforcement, worker execution, semantic review, author-label authentication and author taste are distinct claims.
