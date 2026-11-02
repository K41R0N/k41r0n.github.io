---
type: Reference
title: "Copy review pipeline (his review engine, generalized)"
source: "His Copy Review Engine reference doc and its implementation, both in his private tooling repos, read 2026-11-02. Exact source pointers are kept in the owner's private source map (Kairon Drive), not in this public repo. Product- and brand-specific application sections (a CMS landing page, a client voice) are excluded; this is the method only."
status: source-derived. Read this file fresh each run; reviewing from remembered rules is the drift this system exists to prevent.
---
# Copy review pipeline

The review side of his copy method. Pair with the drafting five-pass
(`../20-harnesses/harness-01/routines/copy/five-pass.md`): drafting produces,
this pipeline reviews. Two things combine into the working system: a five-pass
review pipeline and a creative interpretation step (five lenses, then the
Ogilvy filter).

This pipeline judges three kinds of fit, and a person judges the result:

- **Creative quality** - is the idea strong, not merely clean (Pass 2).
- **Voice source fit** - does it read like the actual voice source, not like
  competent generic copy (Pass 3).
- **Reader, audience and offer fit** - does it move this reader, about this
  offer, at this awareness stage (Passes 2 and 5).

A count of passes run is not a certification of any of these. A deterministic
checker (packs/copy-five-pass) can only prove listed patterns were absent;
it never proves the copy is good.

## The five passes

1. **Decontamination.** Remove AI-generated artifacts and tells from the copy.
2. **Creative review.** Apply the five creative lenses and the Big Idea
   filter below. This is the pass that decides whether the piece has an idea
   worth keeping; skipping it and only linting is how "AI copy" ships.
3. **Tone and voice.** Enforce the voice source: words that work, words that
   fail, rhythm, register. For copy as him, that source is
   `knowledge/voice/` in this repo (voice-spec, do-dont, lexicon, registers).
4. **Compliance.** Claims, legal, banned phrases, proof-required checks.
   Every factual or comparative claim traces to current evidence.
5. **Final page review.** Read only the headings in sequence: do they tell a
   coherent positioning story alone? "you/your" ratio holds (>=60%)? Tonal
   arc holds? H1 and final CTA form a coherent loop?

## The creative interpretation step - five lenses (applied sequentially)

1. **Reframe (Sutherland).** Change the context or meaning, not the product.
   Ask: the opposite of the logical solution? What is the problem really
   about? Where is ignored value? How do we make the reader feel clever for
   choosing this?
2. **Behavioral economics (Kahneman).** Loss aversion (frame as avoiding a
   loss), framing effect (re-present the same data), anchoring (first number
   or concept planted), status-quo bias (the hidden cost of doing nothing).
3. **Cultural tension (Big IdeaL).** Elevate from product to protagonist in a
   cultural story. Pick a real debate the work can take a side on; define its
   ideology.
4. **Metaphor (Poet).** "This is not an X, it is a ___." "Using it is like
   ___." If it were an animal, building, tool or sound?
5. **Contrarian (Challenger).** Find the category's sacred cow and shatter
   it. Define the enemy: a system or old way, never a named competitor.

## The final filter - Ogilvy's Big Idea test (five questions)

For each strongest idea, ask all five:

1. Did it make me **gasp** when I first saw it?
2. Do I **wish I'd thought of it** myself?
3. Is it **unique**?
4. Does it **fit the strategy** to perfection?
5. Could it be used for **30 years**?

The filter keeps the direction strategically sound, ownable and a long-term
asset, not clever for its own sake. All five questions are canonical. Known
implementation drift: the deployed review prompt currently lists only four
of the five, dropping question 2; the reference doc and the creative preset
carry all five. When the tool and this file disagree, this file's five win,
and the drift gets fixed at the source (tracked in the owner's private
tooling repo).

## Structural copy rules

- **Competitor test.** Every heading must pass "would a competitor say
  this?" If yes, rewrite until no.
- **Hero H1.** 2-7 words. Imperative, declarative with definite article, or
  noun-phrase-as-outcome. No questions, compound sentences, or-operators or
  hedged claims. Zero jargon: a total outsider must understand it. Numbers
  only when they are the value proposition. Never lead with the product
  name. If the mechanism is the benefit, collapse them into one phrase.
- **Subheadline.** 12-35 words. Expands the H1, never repeats it. Answers at
  least two of: what is this, who is it for, why trust it.
- **CTA.** The verb mirrors or extends the H1's core benefit verb. Never
  default to "Get started."
- **Feature and benefit blocks.** Benefit, then mechanism, then proof -
  never reversed.
- **Positioning through copy.** Differentiate via a category-level
  antagonist ("the old way"), never a named competitor. Imply pain through
  negation or revelation; do not agitate directly. Every section reinforces
  the same positioning from a new angle.
- **Numbers.** Specific unrounded numbers for trust; percentages need
  context; every number answers an implicit objection.
- **Tonal arc (scroll depth).** Top aspirational; middle precise,
  data-backed differentiation and function; bottom grounded, evidence-based,
  invitational. Flow: aspiration, differentiation, function, trust, proof.
- **Banned phrases.** cutting-edge, next-generation, revolutionary,
  game-changing, best-in-class, seamless experience, robust, leverage,
  utilize, empower, unlock the power of, reimagine, at the forefront,
  world-class, innovative, disruptive, synergy, holistic, end-to-end,
  turnkey, frictionless, state-of-the-art, paradigm shift, transform your,
  supercharge your.

## What this reference is not

Not project policy, legal advice, factual authority, or approval to publish.
It does not replace the current brief, the current voice source, or his read
of the final copy.
