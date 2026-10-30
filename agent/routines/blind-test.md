---
type: Routine
title: "Blind-pair calibration"
confidence: proposed
tier: 2
approver: Alejandro Arango
status: PROPOSED. Not run. Needs about 30 minutes of his time.
---
# Blind-pair calibration

Purpose: find what the spec misses, with evidence instead of argument.
1. Take 3 passages from assets/voice-corpus/holdout/ (his) and 3 written by the engine for the same topics, from the spec only. Strip headers, shuffle, label A to F.
2. He marks each passage "mine" or "not mine" and says why, in one line each.
3. If he can spot the engine's passages every time, the spec misses something. Each reason he gives becomes a rule candidate in log/compound.md.
4. A candidate becomes a rule only after a second blind pair where the rule changes his verdict. He approves each one.
Stop condition: he cannot reliably tell the sets apart across two rounds. Then the spec is good enough for drafts; he still approves every piece.
Note: this requires the engine to write sample passages. That is a separate, explicit approval from him, and the passages are test material, never published.
