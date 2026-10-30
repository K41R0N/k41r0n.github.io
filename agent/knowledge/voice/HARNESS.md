---
type: Charter
title: "voice-harness"
approver: Alejandro Arango
maturity: MVH-0
created: 2026-10-28
confidence: proposed
---
# voice harness charter

**Location:** `agent/knowledge/voice/` inside the Kairon site repo (K41R0N/k41r0n.github.io). The website is the harness. Paths below are relative to `agent/`. Proposed, not yet merged: see INTEGRATION-PROPOSAL.md.

**Owner and approver:** Alejandro Arango. Nothing graduates a tier without his yes. **Maturity:** MVH-0 (manual runs only, nothing scripted beyond measurement and checks).

## 1. The frame
A voice has a measurable part (word choice, sentence shape, punctuation, rhythm) and an unmeasurable part (what he notices, what he refuses to say, his judgment). Formulas check the first. Only he approves the second. The harness catches drift and polishes. It cannot prove "sounds like Alejandro", and it never replaces his approval.
Stylometry points the same way: the signal sits in habits writers do not control (function words, punctuation, rhythm), not in pet phrases. The checks target habits.

## 2. Tiers
- Tier 0: verified fact about him (his words, quoted, dated).
- Tier 1: rule he confirmed.
- Tier 2: proposed (measured or ported, not yet confirmed). Everything in knowledge/voice/ starts here.
- Tier 3: hypothesis.

## 3. Folders
knowledge/voice/ (voice-spec, do-dont, lexicon) · assets/voice-corpus/raw (spec source) · assets/voice-corpus/holdout (test only, never used to build the spec) · assets/voice-corpus/excluded (AI-assisted, co-written, or authorship unverified) · knowledge/voice/thoughts/ (his raw ideas) · knowledge/voice/refs/ (evidence) · decisions/voice-findings/ (dated findings and decisions, one file per finding, see decisions/voice-findings/README.md) · knowledge/voice/registers/ · assets/voice-drafts/ · ingestion/reports/voice/ · routines/ (copy-draft, copy-review, blind-test) · scripts/local/voice/ (measure and check, stdlib Python) · routines/voice-compound.md.

## 4. Pipeline
thought, brief, draft (five passes), deterministic checks (scripts/local/voice/checks.py, range checks against voice-spec), review (seven passes), checks again, he approves. Corpus, thoughts and refs stay in separate folders so form, content and evidence never contaminate each other.

## 5. Hard rules
1. Nothing is published or sent as him without his explicit approval.
2. Existing writing of his is never rewritten unless he says "rewrite the copy".
3. Spec is built from assets/voice-corpus/raw only. The holdout never touches it (scripts/local/voice/verify.py V3 proves this on every run).
4. Only self-written pieces enter raw. Authorship is unverified for anything without a byline or his confirmation.
5. Judgment steps are never scripted.
6. Client rules ported here are tested against his own writing before adoption.
7. A rule that flags most of his own pieces is not adopted by default.

## 6. Graduation (D1-D5)
Nothing is scripted until two identical manual runs. Judgment steps are never scripted. Each rule needs his approval, ideally with blind-pair evidence (routines/blind-test.md).

## 7. Current state (phase 1)
- Corpus: 11 essays (Substack, cross-checked against content/blog). 9 raw, 2 holdout (chosen by seeded random draw, seed 20261028). 13 kairon.xyz pages in excluded/, authorship unverified.
- Spec v0 measured from raw with recency weighting (12-month half-life, his instruction): knowledge/voice/voice-spec.md (Tier 2).
- Checks v0: scripts/local/voice/checks.py (19 rules, mostly WARN), scripts/local/voice/range_check.py (WARN only, 3+ of 25 features), Burrows Delta in verify.py as a SOFT signal only. Result against his own writing: ingestion/reports/voice/verification.md.

## 7b. Status of every routine
Nothing has graduated. No routine has run twice, so by the D1-D5 rule nothing may be scripted. The AEO pass is a stub: it needs his own AEO plan. Until he supplies it, the format step in copy-draft only names AEO as a form-only pass.
Honest limit on the holdout: it is partly spent. Rule-level false-positive tests, the dash budget, the metronome tightening and the range-check calibration all looked at the 2 holdout essays. For those rules, the holdout is no longer an untouched test. The spec itself never saw it (verified, V3). Fresh untouched samples are needed for real tests.

## 8. Open items for him
1. Confirm which of the 13 kairon.xyz pages he wrote himself (list in assets/voice-corpus/excluded/).
2. RESOLVED 2026-10-28: he confirmed all 11 essays are fully his prose (the 2025-06-17 essay mentions using Claude to organize data and draft initial thoughts; he knows, and confirmed it anyway). Applies to the 11 essays only, not the 13 site pages.
3. Decide the section B rules in knowledge/voice/do-dont.md (32-word cap, banned filler, 20-word target).
4. Blind-test setup (routines/blind-test.md).
5. The handwritten notes on mimicking someone's voice (his guidelines): the original image was never readable by the engine. His wording needs to be added to knowledge/voice/do-dont.md as Tier 0 or 1.
6. More verified samples for registers other than essay.
