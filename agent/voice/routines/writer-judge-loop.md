# Writer/judge loop with sealed edit predictions (Tier 2, proposed)

Source: Nat Eliason's writing-pipeline article, text sent by Alejandro himself. His yes (relayed by Main, Oct 29) covers folding these patterns in. It does not graduate anything, answer the blind-test ask, or reopen the paused writing lane. Nothing here writes in his voice until he says the voice is ready. Draft output goes to `drafts/`, never `content/`.

## Roles
- Writer: drafts from his source notes only. Never sees `corpus/holdout`. Never borrows stories from example pieces. Where the notes lack his take, writes `[ALEJANDRO: your take]` and does not guess framing.
- Judge: a separate pass. Gives the top 3 fixes per round and writes the sealed predictions. Does not rewrite.
- Him: edits to publishable. His edit is the only quality score.

## Inner loop (before he sees anything)
1. Writer drafts. 2. Run `tools/checks.py`, `tools/placeholders.py`, `tools/holdout_guard.py`. 3. Judge: top 3 fixes. 4. Writer revises. Max 3 rounds; more rounds flatten the voice.
5. Judge writes `predictions.md`: the edits it expects him to make, each tagged voice-rule, structure, fidelity or banned-phrase. Then `tools/ledger.py seal DIR`. Judge reports stay hidden from him until he is done editing.

## He edits
He writes his version to `final.md` beside `draft.md`. The draft is untouched. Save the source notes and final as a pair for regression redrafts after any rule change.

## Measure
- `tools/edit_rate.py draft.md final.md --hunks` gives word-level edit rate and numbered hunks.
- A reviewer who is not the writer classifies each hunk in `classes.md` (`H1 | bucket | predicted: yes|no | note`). Judgment step, not scripted.
- `tools/ledger.py score DIR` checks the seal and gives rate, bucket counts and predicted share. The predicted share is the "can step out" number: how much of his editing the judge saw coming.
- Run in batches (1 piece, then 3, then 3). Update rules from his edits between batches. Compare with `ledger.py batch`. Fidelity edits (made-up facts) are always failures, regardless of rate.

## Rules from edits
A single edit is a hypothesis. The judge pushes it as a fix only after it holds across several pieces. It becomes firm after repeated reversals. Rules go to `canon/` as Tier 2 until he says yes.

## Ban list
Only words he never uses in `corpus/raw` (`tools/ban_list.py`). Words he does use are not banned, however "AI" they sound. Small corpus, so he confirms before adoption.

## Corpus hygiene
`tools/corpus_clean_check.py` lists footers and plugs for review. Images become `[image]`, eras get tagged, older voice is structure-only. One shared voice guide, separate format guides.

## Limits
Edit rate cannot certify voice. Tools here are checks on process. Fixtures in `tools/fixtures/` are synthetic. Edit rate definition is ours (words added plus cut over draft words), not the article's.
