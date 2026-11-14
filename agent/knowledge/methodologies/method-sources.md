---
type: Reference
title: "Method source map: where each of his processes lives"
confidence: confirmed access rules from his standing instructions
---
# Method source map

Where to find the process that answers a given question. Built after the
2026-11-02 run, where copy, marketing and ICP method locations were treated
as known and then not read. Read the source fresh each run; never cite a
method from memory (his standing rule, 2026-10-29 8:29 PM: re-read the
Marketing-harness and icp-harness whenever anyone asks about his marketing
methodologies, before any positioning, messaging or copy work, and on a
periodic refresh).

Private originals are not located in this public repo. The exact repos,
paths and pinned commits for every private source below live in the owner's
private source map in his Kairon Drive (reference folder). Open that map
when a rule says re-read the private source. If the map itself cannot be
reached, follow the recovery contract at the bottom of this file - do not
ask him to re-identify material that is already logged.

## This repo (public, `agent/`)

The working harness. Writable per the write guard (agent/ docs are Tier 2).

- `packs/` - his methods library, one pack per method, with evals.
- `knowledge/voice/` - the voice canon: voice-spec, do-dont, lexicon,
  registers, corpus pointers. The voice source for anything written as him.
- `routines/copy-draft.md`, `routines/copy-review.md` - how this harness runs
  the drafting five-pass and the review pipeline.
- `skills/pitch-website/` - the pitch-page workflow and its accepted
  examples.

## Copy framework (his review engine)

The five review passes, five creative lenses, Ogilvy's five-question Big
Idea filter and the structural rulebook. Generalized, client-free copies
live in `packs/copywriting-methods/` so everyday work never needs to open
the private sources. The private originals (reference doc and the review
app's implementation) are listed in the private source map. Known drift:
the deployed review prompt currently asks four of the five Ogilvy
questions; the framework's five are canonical and the fix is tracked with
the owner.

## Marketing-harness (private)

His strategy and positioning methods: defining an offering, benchmarking,
tracking competition, identifying a moat, making something marketable;
the Studio Stupid Pipeline Engine. Also holds the canonical Harness
Standard and Attention Graduation Framework.

Answers: what is exciting, important or compelling about an offer; how to
position for a specific company or person. Reference-only for this harness:
read, never push. Re-read fresh per the standing rule; the location is in
the private source map.

## icp-harness (private)

His audience methods: understanding what clicks, resonates, drives
awareness and trust; the named-list ICP method (people, never segments);
the listening map; the OSINT person-research original (a generalized copy
is `packs/prospect-research/`).

Answers: who the reader is, where they speak, their exact words, what they
already accept. Reference-only: read, never push. Location in the private
source map.

## Client harnesses (locked)

Client workspaces and brand harnesses (anything holding client names,
accounts or employer material) are locked. Never read them into public
output, never name them in this repo, never route through them for general
method questions. The push gate enforces this. The generalized five-pass in
`packs/copywriting-methods/` was verified against the locked originals on
2026-11-02 and matches their pass sequence; the originals stay private.

## Routing by question

| The question | Read |
|---|---|
| Who is this person or company, really? | `packs/prospect-research/` first; the private ICP source for audience depth |
| What would be compelling to them? | The private marketing source (positioning, offer, alternatives) + the prospect research |
| What do we say and how? | `packs/copywriting-methods/` (drafting five-pass + review pipeline), voice canon for anything as him |
| Is this copy any good? | Review pipeline: creative quality, voice source fit, reader/audience/offer fit; `packs/copy-five-pass/` as lint only |
| How far can this work be delegated? | `packs/attention-graduation/` + the canonical staged-delegation framework (private source map) |

## Method corpus index (document level)

Every method corpus he has, across all harnesses, at the level an intent
can route to. The machine-readable form is `method-corpus.json` in this
folder; `../../scripts/local/routing_lint.py` keeps the registry complete
and resolvable. Route from here first; open the source fresh before using
any method (his standing re-read rule).

| Area | Access | What it answers | Docs |
|---|---|---|---|
| Packs (this repo, `agent/packs/`) | public, writable via PR | Executable methods with evals: see `../../packs/index.md` for the 16 rows | one folder per pack |
| Ways-of-working corpus (`ways-of-working-corpus.md`) | public | Plain-words answers to common asks, distilled from his 142-method compendium | 1 doc, Q&A form |
| Ethos (`../ethos/`) | public | The principles every answer is judged against | ethos + candidates + asker lens |
| Method archive (`../../method-archive/`) | public | Original wording of imported methods, for provenance questions | source-area folders |
| Voice canon (`../voice/`) | public | How anything in his voice is written and checked | spec, do-don't, lexicon, registers |
| Marketing-method notes (private marketing harness) | private-map | 23 documented methods, each with source status, attribution and limits. Topics: tool fit; content format; strategy and positioning; LinkedIn programme; manual-first agentic research; video research; six-question brief; knowledge governance; thought-piece production; funnel/email audit; reconnaissance and listening; intelligence cards; copywriting and editorial review; content operations; case-study evidence; presentations; analytics and reporting; process standardization; harness knowledge governance; testing and correction loops; website/launch/search; offer economics; value-equation offer framing | routed by the method index in that repo; exact paths in the private source map |
| P-035 import record (private marketing harness) | private-map | What the kairon-methods archive held, what was imported or held, and why | import record + safe-materials map + family disposition map |
| icp-harness (private) | private-map | Named-list ICP method, listening map, what moves the audience, funnel and news sources; OSINT person-research original | routed by its own index; paths in the private source map |
| Harness Standard + Attention Graduation Framework (private marketing harness) | private-map | How any harness is structured; how work graduates from manual to delegated | canonical copies; paths in the private source map |
| Copy framework originals (private) | private-map / locked | The review engine at source; drafting five-pass originals are locked client material - reconcile privately, never copy | paths in the private source map |
| K41R0N/methods | retired | Nothing. Superseded by this repo's `agent/` on 2026-10-29; never route here | deletion is the owner's pending call |

## Recovery contract: when routing fails

1. **No corpus entry matches the ask.** Say plainly that no documented
   method covers it, add an open loop in `../../decisions/open-loops.md`,
   and ask him one sharp question. Never route by nearest name (packs
   index rule, generalized to the whole corpus).
2. **A routed source is inaccessible.** Report the exact locator tried,
   what was checked, and the gap. Check this file and the private source
   map before asking him to re-supply anything - re-asking for logged
   material is the failure this file exists to prevent. Never fill the
   gap from memory; a method not read this run is a method not used.
3. **Routes disagree or smell stale.** The higher-confidence source wins
   (see `../../HOW-TO-USE-THIS-BRAIN.md`), the disagreement becomes an
   open loop, and the stale route is fixed in the same cycle, not worked
   around.
4. **A real routing failure reached him.** It becomes a lint case or a
   registry fix in the same cycle (eval contract rule 12: failures become
   fixtures). The 2026-11-13/14 failures - method library not recognized,
   here.now route not applied - produced this section, the corpus index
   and the routing lint.
