---
type: Reference
title: "Method source map: where each of his processes lives"
confidence: confirmed locations (repo list verified 2026-11-02); access rules from his standing instructions
---
# Method source map

Where to find the process that answers a given question. Built after the
2026-11-02 run, where copy, marketing and ICP method locations were treated
as known and then not read. Read the source fresh each run; never cite a
method from memory (his standing rule, 2026-10-29 8:29 PM: re-read the
Marketing-harness and icp-harness whenever anyone asks about his marketing
methodologies, before any positioning, messaging or copy work, and on a
periodic refresh).

## This repo (K41R0N/k41r0n.github.io, public, `agent/`)

The working harness. Writable per the write guard (agent/ docs are Tier 2).

- `packs/` - his methods library, one pack per method, with evals.
- `knowledge/voice/` - the voice canon: voice-spec, do-dont, lexicon,
  registers, corpus pointers. The voice source for anything written as him.
- `routines/copy-draft.md`, `routines/copy-review.md` - how this harness runs
  the drafting five-pass and the review pipeline.
- `skills/pitch-website/` - the pitch-page workflow and its accepted
  examples.

## Copy framework (his review engine)

- Reference doc: private repo K41R0N/candy-cms,
  `docs/research/copy_framework.md`. The five review passes, five creative
  lenses, Ogilvy's five-question Big Idea filter, structural rulebook.
- Implementation: private repo K41R0N/copywriting-review-flow (the review
  engine app). Known drift: `lib/prompts.ts` lists four of the five Ogilvy
  questions; the framework's five are canonical.
- Generalized, client-free copies live in `packs/copywriting-methods/` so
  everyday work never needs to open the private sources.

## Marketing-harness (K41R0N/Marketing-harness, private)

His strategy and positioning methods: defining an offering, benchmarking,
tracking competition, identifying a moat, making something marketable;
the Studio Stupid Pipeline Engine. Also holds the canonical Harness
Standard v0.3 and Attention Graduation Framework under
`docs/references/harness-standard-v0.3/`.

Answers: what is exciting, important or compelling about an offer; how to
position for a specific company or person. Reference-only for this harness:
read, never push.

## icp-harness (K41R0N/icp-harness, private)

His audience methods: understanding what clicks, resonates, drives
awareness and trust; the named-list ICP method (people, never segments);
the listening map; the OSINT person-research original (a generalized copy
is `packs/prospect-research/`).

Answers: who the reader is, where they speak, their exact words, what they
already accept. Reference-only: read, never push.

## Client harnesses (locked)

Client workspaces and brand harnesses (anything holding client names,
accounts or employer material) are locked. Never read them into public
output, never name them in this repo, never route through them for general
method questions. The push gate enforces this.

## Routing by question

| The question | Read |
|---|---|
| Who is this person or company, really? | `packs/prospect-research/` first; icp-harness for audience depth |
| What would be compelling to them? | Marketing-harness (positioning, offer, alternatives) + the prospect research |
| What do we say and how? | `packs/copywriting-methods/` (drafting five-pass + review pipeline), voice canon for anything as him |
| Is this copy any good? | Review pipeline: creative quality, voice source fit, reader/audience/offer fit; `packs/copy-five-pass/` as lint only |
| How far can this work be delegated? | `packs/attention-graduation/` + the canonical AGF |
