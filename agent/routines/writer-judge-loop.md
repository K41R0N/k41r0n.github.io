# Writer/judge loop with sealed edit predictions (Tier 2, proposed)

Source: Nat Eliason's writing-pipeline article, text sent by Alejandro himself. His yes (relayed by Main, Oct 29) covers folding these patterns in. It does not graduate anything, answer the blind-test ask, or reopen the paused writing lane. Nothing here writes in his voice until he says the voice is ready. Draft output goes to `assets/voice-drafts/`, never `content/`.

## Roles
- Writer: drafts from his source notes only. Never sees `assets/voice-corpus/holdout`. Never borrows stories from example pieces. Where the notes lack his take, writes `[ALEJANDRO: your take]` and does not guess framing.
- Judge: a separate pass. Gives the top 3 fixes per round and writes the sealed predictions. Does not rewrite.
- Him: edits to publishable. His edit is the only quality score.

## Inner loop (before he sees anything)
1. Writer drafts. 2. Run `scripts/local/voice/checks.py`, `scripts/local/voice/placeholders.py`, `scripts/local/voice/holdout_guard.py`. 3. Judge: top 3 fixes. 4. Writer revises. Max 3 rounds; more rounds flatten the voice.
5. Judge writes `predictions.md`: the edits it expects him to make, each tagged voice-rule, structure, fidelity or banned-phrase. Then `scripts/local/voice/ledger.py seal DIR`. Judge reports stay hidden from him until he is done editing.

## He edits
He writes his version to `final.md` beside `draft.md`. The draft is untouched. Save the source notes and final as a pair for regression redrafts after any rule change.

## Measure
- `scripts/local/voice/edit_rate.py draft.md final.md --hunks` gives word-level edit rate and numbered hunks.
- A reviewer who is not the writer classifies each hunk in `classes.md` (`H1 | bucket | predicted: yes|no | note`). Judgment step, not scripted.
- `scripts/local/voice/ledger.py score DIR` checks the seal and gives rate, bucket counts and predicted share. The predicted share is the "can step out" number: how much of his editing the judge saw coming.
- Run in batches (1 piece, then 3, then 3). Update rules from his edits between batches. Compare with `ledger.py batch`. Fidelity edits (made-up facts) are always failures, regardless of rate.

## Rules from edits
A single edit is a hypothesis. The judge pushes it as a fix only after it holds across several pieces. It becomes firm after repeated reversals. Rules go to `canon/` as Tier 2 until he says yes.

## Ban list
Only words he never uses in `assets/voice-corpus/raw` (`scripts/local/voice/ban_list.py`). Words he does use are not banned, however "AI" they sound. Small corpus, so he confirms before adoption.

## Corpus hygiene
`scripts/local/voice/corpus_clean_check.py` lists footers and plugs for review. Images become `[image]`, eras get tagged, older voice is structure-only. One shared voice guide, separate format guides.

## Limits
Edit rate cannot certify voice. Tools here are checks on process. Fixtures in `scripts/local/voice/fixtures/` are synthetic. Edit rate definition is ours (words added plus cut over draft words), not the article's.

## Related evidence, not an active pipeline change
The [2026-11-16 taste/voice study](../knowledge/voice/taste-evaluation-study-2026-11-16.md) compares Every's case-linked checks and reference-based guide optimization with this loop. It proposes calibration and test separation without reopening writing, replacing the five drafting/five review passes or treating a model score as author approval. Candidate checks remain separate from confirmed voice rules; private gold and source corrections are not repository fixtures.

## Enforced execution (2026-11-16)

This file is the single run contract for the existing `copy-draft.md` and `copy-review.md` routines. `scripts/local/writing.py` is their entrypoint, not a separate writing method. Diagnostic helpers alone cannot complete a run. Run from repo root or any directory using an absolute script path.

### What can run now

The repository ships with new author-voice writing disabled and no production model executor configured. It makes no model calls, installs nothing, spends nothing and publishes nothing. Those are real blockers, not automatic defaults to guess around. Source preparation, historical evidence import, measurements and evaluation validation work offline. A host adapter may be connected later within its actual account and spending authority; editing a JSON flag is not that authority.

The existing voice-writing hold remains separate from execution capability. Even a configured host cannot start `mode: new` while the hold is set. The current task is the foundational build, not a fresh draft in Alejandro's voice.

### Start and prepare

Keep the entire run outside the repository. Private corpus, corrections, notes, original-message evidence, judge reports and author finals must not enter a public branch. Use explicit absolute input paths.

```
python3 agent/scripts/local/writing.py init /private/run --brief /private/brief.json
python3 agent/scripts/local/writing.py prepare /private/run
python3 agent/scripts/local/writing.py status /private/run
```

`status` returns nonzero while work remains. Successful init/record/execute/revise transitions return zero so set-e drivers can continue; JSON still says blocked with next stage until the process is complete. Rejected transitions return nonzero. Their JSON states distinguish an expected incomplete run from a rejected input. They never claim completion just because a directory was created.

The brief is JSON:

- `mode`: `new` or `review`. Supplied/outside copy uses review, not fabricated drafting receipts.
- `scope`: `personal` or `client`; `voice_target`: `author`; `voice_owner`: the actual intended speaker or brand.
- `reader`, `already-believes`, `action`, `channel`, `register`, `objective`, `risk-owner`: substantive statements, not empty labels.
- `format`: `essay`, `short-post`, `landing-page` or `email`. Unknown formats stop for resolution.
- `review_plan`: exactly five distinct topic/reason/source_ref objects chosen for this piece, in execution order. Available topics: decontaminate, creative, tone, compliance, page, big-idea-review, ogilvy, positioning, clarity, legal, data-accuracy. Source_ref records provenance, not authenticated authority. Nov2 pitch priorities were big idea, Ogilvy, positioning, clarity and LLM-pattern removal; that is not a universal template for every piece.
- `artifact`: the immutable initial draft/source artifact path.
- `inputs`: lists of paths under separate `notes`, `voice`, `register`, `corrections` and `facts` roles. Select and explain relevant sources. A selected correction or sample may not silently disappear from review. No authentic correction is invented to satisfy a field; unresolved input gaps block the run.

Client runs additionally require `inputs.client_policy`, pointing to private JSON with `schema: writing-client-policy/v1`, current `source_ref` and explicit `rule_severities` for every diagnostic rule ID. Only INFO/WARN/FAIL are accepted. This selects which known candidate diagnostics apply; it cannot encode a different numeric rule by pretending it is the existing one. A new rule needs its own sourced implementation/test. Client runs must explicitly set `author_guideline_overlay` (boolean) and `author_overlay_reason` from the current brief/source request. Author-target client copy requires true; a substantive prose rationale cannot opt out of the Nov3 author-guideline requirement. It loads the author guidelines and raw-only measurement verification alongside, never instead of, client brand policy. It does not permit borrowing personal stories or disclosing private corpus. The Nov3 correction requires author guidelines when requested alongside client rules. Client policy review is not a claim of legal safety.

`prepare` creates a hash-bound current-pass packet containing the complete piece, brief, relevant method text and selected role-separated inputs. It excludes prior critiques, hidden predictions and author-final files. The fresh reviewer receives the whole piece and one core review topic, not a previous review to echo. Creating a packet does not prove it was read; its application evidence is checked next.

### Execute, do not self-report completion

```
python3 agent/scripts/local/writing.py execute /private/run
```

This dispatches exactly the next stage through the configured local adapter. The adapter command is an argv list, not shell prose. Its source files are hash-pinned, the executable path is explicit, and shells or inline unpinned commands are rejected. A fresh process receives the prepared packet on stdin with a minimal environment. A pinned bubblewrap executable is required: the root filesystem is read-only, the entire run directory is masked even by its absolute path, and only a new scratch directory is writable. A test worker actively attempts to open a known prior-critique path and fails. This is run-history confinement, not a complete credential/data sandbox: host files elsewhere remain readable, so only approved adapters may be connected. The Claude candidate additionally disables file and other tools, but actual host-managed hooks remain unverified. No session resume is allowed by the adapter contract. Missing confinement blocks dispatch; there is no unconfined fallback. Account secrets, model access and costs belong to an independently approved host integration, not this offline process checker.

The entrypoint records the real process exit status and immutable stdin/output hashes, and assigns the invocation and worker identity itself. Adapter failure, invalid JSON, failed evaluation or missing evidence stops progression. There is no random result, fallback pass or silent skipped review. Writer and reviewer roles cannot share the same worker identity. A pinned adapter still needs a conformance check that it actually opens a fresh model context rather than secretly resuming one; a new operating-system process alone cannot prove remote service behavior. No production adapter has been claimed tested here. The disabled existing-host Claude Code review candidate and its unverified live checks are recorded in `knowledge/voice/claude-host-adapter-2026-11-16.md`. Its tests mock the client; they do not consume the account or generate prose.

For historical/manual evidence only:

```
python3 agent/scripts/local/writing.py record /private/run --receipt /private/receipt.json
```

A caller cannot submit an `execution` field to impersonate a dispatch. Imported receipts are marked attested. Even a complete set ends at `evidence-complete-attested`, never `process-complete`, and cannot produce a handoff packet. This is the boundary between evidence validation and actual staged execution.

### Receipt contract

Every receipt consumes the preceding artifact hash and records a distinct turn, actor, original source reference, fresh-context declaration, pass/fail, substantive rationale, before/after path+SHA256 references, and the prepared packet reference. For a dispatched pass, identities and the prepared packet are assigned by the entrypoint, not trusted from model output.

Each method application records its catalog source ID, an exact method quotation, an exact current-draft quotation and the application rationale. Only methods assigned to the stage and scope are accepted. A factual source cannot substitute for a method; a voice example cannot substantiate a factual claim. Source/stage matching and exact quotes are structural checks, not proof that an interpretation is wise.

Additional fields follow the existing method:

- Orientation: `input_applications` for every selected input, with input key, exact quote and use; `conflicts_resolved` must be true.
- Big idea: a draft-present `big_idea` of at most 15 words. Its strategic quality is still judgment.
- Facts/compliance/legal/data-accuracy/judge: `claim_inventory_complete`, `claims` with exact draft/source spans, fact-role source key, scope/caveat and timezone-aware `verified_at` from the current prepared pass. If there are no factual claims, explain why. Numeric tokens and substantial quotations cannot hide under a no-claims declaration. Full natural-language factual coverage and live-source authenticity still require review; a timestamp alone does not prove retrieval.
- Selected creative review: substantive responses under every `lenses` and `ogilvy` key. Selected big-idea-review or Ogilvy review uses the five Ogilvy questions only; neither forces the creative lens exercise onto unrelated topics. No dropped 'wish I had thought of it' question.
- Structure/page/positioning/clarity: ordered `paragraph_moves`, each bound to the exact paragraph hash. Non-landing formats explain the scope of page-specific CTA/pronoun rules in `page_rule_scope`.
- Voice/tone/judge: comparisons against every selected voice sample, register and correction under `voice_evidence`, plus all eleven `dimensions`, each with score 1-5, exact quote and reason. These dimensions are candidate evaluation questions, not confirmed author style prescriptions.
- Judge: explicit grounded `critical_method_coverage` for LLM-pattern removal, Ogilvy and Sutherland reframe, even where the five selected checks allocate them differently. Every entry binds a draft span and exact method quote; self-authored exemptions are not accepted. Dedicated topics remain selected per piece. Packet exposes the chosen plan and critical-topic allocation. At most three `top_fixes`, explicit `fidelity_failures`, `open_findings`, worst-lines assessment, overall 1-10 and `predicted_edits`. An open fix, fidelity failure or unresolved finding cannot pass, regardless of score. Scoped lint runs in code; each contextual warning needs a human reviewer, count and reason. No source/author placeholder may remain. Shared historical-test 8-grams stop for inspection, not an accusation of copying.

Each critique observes without rewriting the artifact. A substantive fix starts a separate round:

```
python3 agent/scripts/local/writing.py revise /private/run --artifact /private/new-version.md --reason 'The argument required a different structure, not a word swap.'
```

The previous round and failed evidence remain. Downstream review and evaluation are invalidated; the full applicable sequence runs again. Three rounds exhaust the inner budget and require escalation, not endless smoothing. New writing runs orient + five writing passes + five fresh review passes + judge. Supplied-copy review runs orient + five fresh reviews + judge.

### Evaluation and output states

```
python3 agent/scripts/local/writing.py evaluate /private/run --dataset /private/author-eval.json
python3 agent/scripts/local/writing.py packet /private/run --output /private/packet.json
```

Only actual dispatched passes can reach `process-complete`. That is not voice completion. A packet is always `draft-for-author-evaluation`, never approved/final, and contains no hidden judge report for the author to anchor on. It does not send or publish anything.

The private evaluation input is `author-eval/v1`: immutable guide/rubric refs; disjoint train/calibration/test manifests; register; known prior exposure IDs/hashes; guide-training case IDs; imported author choices and reasons with original-message references and quoted original evidence; and both blinded candidate orders with choice, rationale, confidence and immutable judgment evidence. Malformed judgment means fail, not a coin flip. Abstention remains visible. A local file cannot authenticate who wrote a label; original-channel provenance must be verified before import.

The calculator reports author agreement, swapped-order inconsistency, abstentions, uncertainty and Brier score separately. It does not turn any of those into writing accuracy. Thresholds remain unset and shadow-only until calibrated against actual author judgments. Perfect synthetic fixtures therefore still return `calibration-insufficient` and `quality_pass: false`. A final-test-driven change spends that test; do not relabel it as unseen or use it for guide tuning.

For the actual author-edit loop, preserve the untouched draft and use the existing ledger. `seal` now binds both draft and predictions and refuses resealing. A legacy prediction-only seal is not an evaluation-grade untouched pair. Fidelity edit hunks are failures even at a low edit rate. Independent classification and original author provenance remain human checks. No metric automatically lets the author step out, approves copy or graduates the capability.

### Verification and bypass boundaries

Run the normal evaluator:

```
python3 agent/evals/run.py writing
python3 agent/evals/run.py
```

The software tests include a full twelve-stage CLI run through isolated synthetic worker processes. Those workers explicitly do not judge writing. They demonstrate dispatch, binding, sequence and refusal behavior, not author quality. The production executor configuration stays empty.

Changes to selected inputs, raw measurement files, method/rule/code versions, prepared packets or reviewed artifacts invalidate a run. Personal preflight checks fresh JSON and Markdown measurement rebuilds. Missing, irrelevant-role, forged, failed or stale evidence blocks the output path.

Run-history confinement does not make this a general operating-system security sandbox, a GitHub branch-protection rule or a cryptographic identity service. Hashes are self-anchored in local state, not a signed/git-rooted chain; someone who edits both source and recorded hashes can rewrite that evidence. This remains a local process checker, not malicious-local-writer resistance. A person with local write access can edit the runner, policy or run state, or ignore the entrypoint and commit text by another route. That route gains no approval or quality status from this process. Repository contribution/merge rules and the owner's exact approval remain separate safeguards. Structural enforcement must not be described as mind-reading, secure author authentication, or proof that the writing is good.

The same entrypoint closes the author-edit loop with `seal-author /private/run`, then `score-author /private/run --final /private/author-final.md --classes /private/classes.md --provenance /private/provenance.json`. Sealing requires dispatched process completion and binds the actual reviewed artifact plus the judge predictions. Provenance must bind the final SHA256, original evidence quotation, original feedback ID, identity checker, timezone-aware author_edit_at after the seal, and independent classifier. Imported feedback remains explicitly attested, never automatic approval. Duplicate/malformed hunk classes, changed draft/predictions, missing classes or fidelity edits block the result. Nothing is overwritten or resealed.

Run-bound calibration additionally requires `run_binding` with the current artifact SHA256, canonical snapshot SHA256, and exact selected voice/register/correction source hashes, plus matching register and frozen writer/judge/settings versions. A valid but unrelated evaluation cannot be attached to this writing run. This binds applicability; it does not authenticate imported author labels.
