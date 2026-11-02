---
type: Routine
title: "Copy review pipeline"
confidence: proposed
tier: 2
approver: Alejandro Arango
source: His Copy Review Engine reference doc (K41R0N/candy-cms, docs/research/copy_framework.md, commit ba0dbd9) and its implementation (K41R0N/copywriting-review-flow, commits e5f74f1), read 2026-11-02, generalized in packs/copywriting-methods/sources/copy-review-framework/review-pipeline.md. Mechanical checks from this harness's earlier draft are folded into the passes they belong to. Replaces the 2026-10-30 reconstruction that described seven ordered passes; no source of his carries seven, and that version had dropped the creative passes entirely - the failure he caught on the Tommy page ("you very clearly didn't use the five pass method", "This is still AI copy", 2026-11-02 1:20-1:25 AM).
status: PROPOSED. Not yet graduated (no two identical manual runs). Source-derived structure; run it from the source files, not from memory.
---
# Copy review (every draft, including ones written by an agent, and any outside draft)

Two stages exist: draft from canon (routines/copy-draft.md), then review. New copy runs both. Existing or outside copy runs review only. Never skip review because a draft looks clean. Sources resolve fresh every run; reviewing from remembered rules is the drift this system exists to prevent. The full method text is packs/copywriting-methods/sources/copy-review-framework/review-pipeline.md; this routine is how this harness runs it.

The review judges three fits, and a clean lint never certifies any of them: creative quality (is the idea strong), voice source fit (does it read like him per knowledge/voice/), and reader, audience and offer fit (does it move this reader about this offer). "Five passes ran" is a process statement, not a quality claim.

## Authority ranks (higher rank wins a conflict)
1. What may be said at all: his positioning, his refusals, accuracy of claims (knowledge/voice/do-dont.md section D, knowledge/voice/thoughts/).
2. Sentence mechanics: knowledge/voice/voice-spec.md ranges and knowledge/voice/do-dont.md.
3. Structure: headlines, openings, tonal arc, knowledge/voice/registers/.
A rule that yields an awkward sentence is applied and flagged. A human decides the override.

## The five passes (in order; do not combine, do not skip)
1. **Decontamination.** Remove AI artifacts and tells: slop connectors, inflated vocabulary, tidy ring composition, generic transitions. scripts/local/voice/checks.py carries the deterministic part; the reader's ear carries the rest.
2. **Creative review.** The judgment pass, never scripted. Run the five lenses sequentially (reframe, behavioral economics, cultural tension, metaphor, contrarian - full questions in the review-pipeline reference), then filter the strongest idea through all five of Ogilvy's questions: gasp; wish I'd thought of it; unique; fits the strategy to perfection; usable for 30 years. An idea that fails is pushed harder or replaced, not polished. This pass also judges reader/audience/offer fit: would this reader, at this awareness stage, care.
3. **Tone and voice.** Register first (knowledge/voice/registers/), then voice-spec ranges, do-dont and lexicon, with the quote exemption. Words that work against words that fail. Read aloud.
4. **Compliance.** Claim inventory: every claim listed with its source, each distinct claim appearing once plus one callback at most. Banned phrases, proof-required claims, superlatives, position integrity - a changed position is a flag, never an edit.
5. **Final page review.** Read only the headings in sequence: coherent positioning story alone? "you/your" at least 60%? Tonal arc holds (aspiration, differentiation, function, trust, proof)? H1 and final CTA form a loop? Redundancy against the claim budget is cut or flagged here.

## What comes out, every time
- Polished copy: same structure as the draft, no inline commentary.
- Change log: every edit with its rule source.
- Flags: positioning conflicts, unverifiable claims, rule conflicts, anything blocked. Flags go to him.

The engine polishes. It never invents, expands, deletes sections, or changes position. Systemic problems (wrong tone throughout, wrong reader, drift) send the piece back to drafting. The deterministic gate (packs/copy-five-pass) runs alongside as a checker only; its clean result proves patterns absent, nothing more.
