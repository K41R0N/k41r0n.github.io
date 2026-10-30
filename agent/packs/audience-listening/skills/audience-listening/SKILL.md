---
name: audience-listening
description: Builds a listening map for a target audience and runs a daily pass that records sourced hits and reports changes.
argument-hint: "[audience and what the client wants to learn]"
version: 0.1.0
metadata:
  harness:
    lane: L3
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D3, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Audience listening

## Purpose
Find where the people a client wants to reach actually speak, and which words and events mark a real signal, so a daily pass reports what changed instead of how much noise there was.

## Step 0
State what you start from (the client's own audience docs, taken as given) and mark team hypotheses as hypotheses. Say what you could not open.

## When to use / not
Use for a new audience, a new client, or a drifting audience read. Not for one-off news checks.

## Modes
Map (build once, refresh quarterly) and pass (daily).

## Procedure by slot
1. Strategize: write the starting point from the client's docs, labelled given.
2. Suspect: for each role in the audience, find where they publish (format and venue), with a source for each claim. Check the primary source behind any social headline.
3. Anticipate: list recent content that drew a named public response, newest first, and why it counts.
4. Act: write the vocabulary of the audience next to the markers of outsiders. Questions in replies are signal. Price talk is not.
5. React: per channel, write where, signal, ignore.
6. Recognize: flag segmentation problems (groups mixed into one list) and do not resolve them yourself.
7. Calculate: write "not verified" honestly. Then fix a daily checklist of signal types. Record each hit with date, source, who, what was said, and engagement with the time it was read. Count repeated copies once. Report changes, not volume.

## Output contract
A note in the eval's format.

## Delivery contract
Share with the client owner. Nothing here is approved copy.

## Quality gates
`python3 evals/run.py audience-listening`. Clean means every claim has a source and every hit is complete. It does not mean the read is right.

## Compound step
Log new signal types and false alarms in routines/learnings.md.

## References
packs/audience-listening/fixtures/, knowledge/ethos/ethos.md (items 22, 23, 25, 33)
