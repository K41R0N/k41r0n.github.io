---
type: Routine
title: "Copy drafting: five-pass method"
confidence: proposed
tier: 2
approver: Alejandro Arango
source: Rewritten for this harness from his five-pass copywriting method (drafting workflow in two of his brand harnesses). Brand-specific material removed. His own voice is the brand here.
status: PROPOSED. Not run yet. Graduation rule: no scripting until two identical manual runs (D1-D5).
---
# Copy drafting: five passes

Governs every piece of copy written for or as him. Do not skip a step. Do not start the next step before the previous one is done. Do not combine passes.

**Hard limit:** this routine produces drafts for his approval. Nothing is published, posted or sent under his name without him reading it first. The text of his existing writing is never rewritten without an explicit "rewrite the copy" from him.

## Step 0. Orient and gather (before any drafting)
0a. Read, in order: HARNESS.md, canon/voice-spec.md, canon/lexicon.md, canon/do-dont.md, the register file in registers/ for this piece, and the thought file in thoughts/ that holds his raw idea.
0b. Gather sources by hierarchy: his own thoughts/ and refs/ first, then primary public sources, then secondary. Cached or stale retrieval stores are never a citable source. Never invent a number. Never use a stale number.
0c. Brief or stop. One reader (a job title or a specific person, not a segment), what they already accept, one action, channel. No brief, no work: ask him.

## Pass 1. Big idea
One sentence, 15 words or fewer, written at the top of the draft. It must be simple, worth reading, different from what others say, and able to carry more than one piece. Tests: can you say it in 15 words, would the reader care, does it fit his positioning in canon. Two big ideas is zero. A vague idea ("this matters") is zero. If it is unclear, stop and fix it. Judgment step: he approves the idea before Pass 2 when the piece is longer than a short post.

## Pass 2. Factual anchoring
List every factual claim: numbers, product features, people, dates, comparisons, superlatives. Trace each to a source in refs/ or a live source and cite it next to the claim. Cannot verify: mark [UNVERIFIED]. An [UNVERIFIED] mark blocks Pass 3. Sourcing a claim does not make a bad claim usable.

## Pass 3. Voice matching
Register first (registers/), then his measured ranges (canon/voice-spec.md), then do-dont and lexicon. Read aloud. Run the reader test: would the person this is for find it precise, not patronizing, and worth their time? Run tools/checks.py on the draft and fix FAILs. Then run the blind-pair test when the piece matters (routines/blind-test.md).

## Pass 4. Storytelling structure
Narrative, not a bulleted report of the piece. Explain why things moved, not only what they are. Each paragraph does one move: a claim, an objection met, a consequence, a mechanism. If every paragraph has the same length and shape, rewrite. Questions where the reader would ask them. No restating a claim in a new shape (claim budget: each claim appears once and is then built on).

## Pass 5. Final gate
Re-run tools/checks.py after all edits and re-verify every number against its source at this moment. Check: banned words, tells, range checks against his essay ranges, no claim bigger than its proof. Output: final draft, change log (every edit with its rule source), flags (anything the engine may not decide alone). Fails any check: fix it first. He approves. The engine does not.

## Format adaptation (after the five passes)
Social post, essay, newsletter, page copy, AEO copy: apply the format's constraints inside the five-pass output. AEO pass: STUB. It waits for his own AEO plan and is not defined here. Working principle only: it would be a form pass, never a content pass, with no change to what he says.

## Outputs
drafts/<date>-<slug>/ with: draft.md, changelog.md, flags.md, checks.txt.
