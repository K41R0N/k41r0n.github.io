---
type: Routine
title: "Copy review engine"
confidence: proposed
tier: 2
approver: Alejandro Arango
source: Structure adapted from the review engine in one of his brand harnesses (seven ordered passes, authority ranks, polished copy plus change log plus flags). Rewritten for this harness.
status: PROPOSED. Not run yet.
---
# Copy review (every draft, including ones written by an agent, and any outside draft)

Two stages exist: draft from canon (routines/copy-draft.md), then review. New copy runs both. Existing or outside copy runs review only. Never skip review because a draft looks clean. Sources resolve fresh every run; reviewing from remembered rules is the drift this system exists to prevent.

## Authority ranks (higher rank wins a conflict)
1. What may be said at all: his positioning, his refusals, accuracy of claims (canon/do-dont section D, thoughts/).
2. Sentence mechanics: canon/voice-spec.md ranges and canon/do-dont.md.
3. Structure: headlines, openings, tonal arc, registers/.
A rule that yields an awkward sentence is applied and flagged. A human decides the override.

## Seven ordered passes
0. **Claim inventory.** List every claim in the draft with its source. Set a claim budget: each distinct claim may appear once, plus one callback at most.
1. **Terminology.** Lexicon and banned words, with the quote exemption.
2. **Sentence mechanics.** tools/checks.py S and P rules, plus range checks against voice-spec.
3. **Structure.** Opening, headings, paragraph mass and shape.
4. **Redundancy and density.** Anything stated twice against the Pass 0 inventory is cut or flagged.
5. **Position integrity.** Does the draft still say what he says? A changed position is a flag, never an edit.
6. **Craft integrity.** Big idea derivable from every section, awareness stage respected (do not re-argue what the reader already accepts), rhythm, emotional core, register.

## What comes out, every time
- Polished copy: same structure as the draft, no inline commentary.
- Change log: every edit with its rule source.
- Flags: positioning conflicts, unverifiable claims, rule conflicts, anything blocked. Flags go to him.

The engine polishes. It never invents, expands, deletes sections, or changes position. Systemic problems (wrong tone throughout, wrong reader, drift) send the piece back to drafting.
