---
name: the client-thought-piece
description: Editorial methodology for writing thought pieces, essays, editorials, and op-ed-grade long-form about the client (the client, the client Protocol, the Agent Network, the client governance, Laniakea, risk, security). Use this skill whenever the author asks for a thought piece, editorial, essay, narrative piece, op-ed, or "a piece in my voice" on any the client topic, and whenever existing the client long-form drafts need to be rewritten to editorial prose standards or de-AI'd. Also use it when asked to review a the client essay for LLM tells or prose quality. This method layers on top of the brain's 5-pass copy protocol; it does not replace it for social posts, PR, or web copy.
---

# the client Thought Pieces: Editorial Method

This skill codifies the flow the author validated on 2026-08-19 for producing the client thought pieces that meet his prose bar: researched and evidence-defended, written in his voice, structurally human, and adversarially edited before he ever sees them. The core lesson of that session, and the reason this skill exists: **LLM tells are architectural, not lexical.** Scrubbing words is round one; the fingerprint lives in sentence structure, paragraph development, figure inventory, and cross-piece repetition, and it takes deliberate structural work plus independent review to remove.

The bar, in the author's words: pieces must be "proper, well developed and sustained, editorially interesting and non-redundant," written "with rhetoric, editorial prose, Ogilvy's copy guidelines, and every known writing guideline from the greats in mind," with connective tissue applied "structurally instead of randomly peppering." Review as many times as necessary. Lazy drafts get sent back.

## Reference files

Read these when the step calls for them; don't front-load all four.

| File | What it holds | Read when |
|---|---|---|
| `references/voice-profile.md` | the author's voice sources, traits, connective kit, register rules | Before drafting, every time |
| `references/tell-registry.md` | Banned constructs (absolute) + structural tell forensics + per-piece budgets | Before drafting AND during review |
| `references/transition-catalog.md` | The researched 20-move segue taxonomy, placement principles, anti-patterns | During the connective pass |
| `references/review-protocol.md` | Reviewer prompt templates, adjudication rules, verification pass, exit criteria | During review rounds |
| `references/structural-audit.md` | The measurement script, thresholds per form, subtraction-pass-last rule | Before and after the anti-LLM pass, every piece |
| `references/corpus-registry.md` | Spent lines, owned anchors, seed-echo rules | During drafting AND review; append at every delivery |

## Step 0: Preconditions and brain retrieval

These pieces are the client brand by default (institutional register). Before writing a word:

1. Confirm there's a brief or direct instruction from the author. His **seed paragraphs are load-bearing**: each seed carries the piece's thesis and usually one or two phrases that must survive into the final draft (develop them, never quote-dump them, never relocate a seed's image to a different piece). If a reviewer later objects to something that came from a seed, the seed wins; the author's direct statements override all other sources.
2. Fetch from the brain (the-client): `positioning.md`, `brand-voice.md`, `legal-guidelines.md`, `financial-terminology.md`, `storytelling-and-ai-discipline.md`. The project’s current source documents should be checked alongside this method; this method does not establish authority or approval.
3. Apply the confidence floor: external-facing claims come from `confirmed` sources; `reference` with caution; `operator_reported` and `conversation` material never appears as fact in a piece.
4. Numbers: never invent, never hardcode a rate. Draft-stage convention is the author's own: a bracketed `[verify]` on any figure, plus a foot-note that figures verify against client-example.invalid and a protocol body quarterly reports at publish time. Prefer structural claims and historical events over live figures; a thought piece that needs few numbers ages better.

## Step 1: Source and partition

Gather the evidence per piece before drafting: what confirmed facts, published proof points, and historical events defend this thesis? Every claim in the final piece must trace to something.

If writing a **set** of pieces, partition the material first. Assign each shared mechanism to exactly one piece (e.g., the loss waterfall belongs to Risk; the time-delay mechanics to Governance; the settlement scoreboard to Agents) and let other pieces reference it in at most one clause with a different function. The same proof point deployed twice with the same framing is how a set gets clocked as one engine writing six times.

## Step 2: Choose the anchor

Each piece gets **one** concrete anchor: a historical episode, a profession, a document, an institution, a scene. The anchor is the argument's engine, not decoration (Ogilvy: the specific fact does the persuading). Rules learned the hard way:

- Anchor types must vary across a set: a scene, a person, a lost skill, a document, an institution, a live moment inside the machine.
- **Fact-check the anchor with real research before drafting.** Names, dates, causation. Session precedents: the Comet crashes were not all unexplained (only the 1954 pair); Goldman's 1999 IPO does not cause 2008; "ten weeks" between crashes was wrong. A finance-literate reader wincing once costs the whole piece.
- Don't take an anchor already owned by the client canon (a stakeholder owns the shipping container) or reuse one across pieces.
- The anchor must survive a hostile reading. If the analogy proves the opposite on inspection (a flight recorder learns from its *own* crashes; the client's record is other people's), concede the asymmetry in one sentence rather than hoping nobody notices. The concession usually strengthens the piece.

## Step 3: Draft under structural budgets

Read `references/tell-registry.md` first and draft with the budgets in mind, because retrofitting structure is twice the work of building it in:

- One idea per piece, developed without circling. No paragraph restates a previous one.
- Openings vary across a set; no two pieces share an opening macro (and "dated historical cold open" counts as a macro even when the dates differ).
- Ring composition (closer re-rings the opening image) in at most a third of a set.
- Paragraph-final aphorisms: two or three per piece, maximum. Several paragraphs must end flat, on a fact. Humans stop; machines land.
- Negation-correction ("not X but Y", "isn't X. It's Y.") at most once per piece.
- One set-piece rhetorical turn per piece, different per piece (see transition catalog).
- Anaphora and author-answered catechism: each at most once per set, only where load-bearing.
- Real sentence variance: some 35+ word sentences with subordinate clauses that wander, some flat short ones, and stretches with no punch at all.
- At least one person, date, or scene per piece. Abstractions don't move capital and don't read human.
- No meta wrap-ups ("step back and the through-line comes into focus"), no series-aware endings, no summary conclusions.

### Forms: essay, op-ed, manifesto

The budgets above were calibrated on essays. Two other forms have since run through the method and differ:

- **Byline op-ed** (John, a stakeholder-adjacent): first person is the register, not an exception; authority claims must be the author's actual credential (a risk-room byline answers with the committee's questions, never an analyst's market data); the piece must contain a falsifiable test of its own thesis; and the anti-LLM pass matters most here, because a named human's prose gets read closest.
- **Manifesto**: seed-heavy by design (the author's edited draft is verbatim seed and wins over every reviewer instinct); a deliberate anaphora set (the refusals) is legal and load-bearing; declaration density runs higher than essay budgets tolerate, so use the manifesto column in `references/structural-audit.md`; refusals must cost something real and be observable from outside, or they are marketing.

When the author supplies a **beat outline plus his own edited draft**, the workflow inverts: his prose is the spine, new material fills the beats he names, and the only questions to ask up front are gate rulings (what is speakable) and target form. Do not restructure his paragraphs to fit the beats; place the beats around them.

## Step 4: The connective pass

After the draft stands, work the joints using `references/transition-catalog.md`. The principles, compressed: most joints should be invisible (open each paragraph on something the previous one ended with: given before new); edit joints in **pairs**, since half of a segue lives in the previous paragraph's last sentence; a segue must do argumentative work (concede, contrast, escalate, particularize, return) or it's filler; if a joint needs a full sentence of throat-clearing, the paragraphs are in the wrong order, so reorder instead of caulking; and vary the move types so no two pieces share a connective signature. Draw lead-ups from the author's own kit (in `voice-profile.md`) before inventing new ones.

## Step 5: Mechanical sweep

Grep the draft (case-insensitively where sensible) for the absolute bans before any human-judgment review: em dashes, "not just", Additionally/Furthermore/Moreover/In conclusion, hashtags, and the client register bans (profit, AUM, assets under management, bank, deposits, interest, earnings call, tokenized fund, central-bank confirmation). Check no live rate or fluctuating figure is hardcoded. The full list with context is in `references/tell-registry.md`.

## Step 6: Adversarial review, then verification

This is the step that actually produced the quality. Do not skip it and do not soften it. Full templates in `references/review-protocol.md`; the shape:

1. Spawn an **independent reviewer** (fresh context, no drafting history) with five lenses: forensic structural read (LLM-tell detection from structure alone), editor's read (coasting, ornament, weak analogies), cross-piece redundancy, voice fidelity against the samples, and fact-check of anchors plus compliance gates. Demand ranked findings with quotes and concrete fixes, and a verdict: "would a skeptical editor who reads LLM output daily clock this, and from what."
2. **Adjudicate** rather than auto-apply. Reviewers are sometimes wrong (a session precedent: a reviewer misattributed which seed owned the black-box image). Verify factual objections against sources; protect seed material; document each judgment call for the author.
3. After repairs, run a **verification pass**: a second fresh reviewer checks explicit pass/fail claims about the specific fixes, and hunts for *new* tells the rewrite introduced. Rewrites introduce their own repetitions and knock-ons (a phrase edited into two nearby sentences, a duplicated concession marker); end with a full human read of the final file for exactly these.
4. Iterate until the verdict clears or the remaining findings are adjudicated as deliberate. the author's standing instruction: "Review your drafts as many times as necessary... it doesn't matter how many times you have to review them under different criteria and lenses."

## Step 7: Compliance gates specific to thought pieces

Beyond the mechanical bans: no pass-through exposure framing (sample-yield-token holders access the sample-rate, never agent performance); agents allocate, the client never does, and the client never controls agents outside governance/parameters/Atlas framing; yield is reported, never recommended, and nothing reads as a price or return expectation; "Insights Call," never "earnings call"; Maker appears only when the author's seed or instruction explicitly invokes it (his call alone); Laniakea content respects the current publication gate and carries no technical internals (Synome, Sentinels, Beacons, Diamond PAU, auction and settlement mechanics) or public timelines; security claims use the qualified canon form ("zero core exploits that led to user fund losses", "nearly a decade"). When the Playbook is silent on something sensitive, default to silence and flag it.

Four compliance patterns proven since founding, reusable as written:

- **AI-agent claims (the three-facts pattern).** Any sentence about protocol-side software touching capital states, explicitly: it proposes and never executes; proposals travel the normal governance path and wait out the same delay; improving model capability never widens its permissions ("a better watchkeeper slots into the same bounded seat; the seat does not grow"). Anything softer reads as autonomous AI in a financial control plane, and legal strikes it.
- **Absolute claims one exploit can falsify.** "An action with no X cannot be taken" becomes "an action with no X is not part of the standard." Scope the claim to the standard, never to physical impossibility.
- **Disparagement-adjacency.** Referencing third-party failures (the November token collapses) stays nameless and numberless in the body, and still gets a Patrick or legal read, because the products are identifiable from the description.
- **Gate-assumption log.** Every draft that assumes a publication gate has moved (Laniakea external mention, Synome naming) says so in its notes, names who has not yet signed the ruling, and treats the author's session answer as the drafting ruling rather than the legal one.

## Step 8: Deliver

Deliver the piece(s) as a file, save to the project, list the figures needing publish-time verification, and note any judgment calls made against reviewer findings. Report the before/after numbers from the structural audit, and append the piece's spent lines and owned anchors to `references/corpus-registry.md`. Final approval is the author's, always.

## the author's preference log (why the budgets exist)

Captured from the founding session, so future revisions understand the why:

- Round 1 feedback: banned-word scrubbing isn't the job. "It's not about the wording. Think in terms of the sentence structure, the way you develop paragraphs, the types of literary figures you use. Avoid the obvious tells and constructs, they're absolutely banned."
- Round 2 feedback: connective tissue must be researched and structural. "Inject human expressions and sentence structures, lead ups, and segues... think structurally instead of randomly peppering them in."
- Standing: write with Ogilvy and the greats in mind; each section and sentence must earn its keep; pieces in a set must be non-redundant with each other; his seeds define theses and key phrases; being told a draft "reads extremely LLM written" means restructure, not re-word.
- 2026-08-25 addition, from the John op-ed correction ("This didn't follow the anti LLM pass in our methodology"): the anti-LLM pass is not a review lens that runs once; it is a measured subtraction pass that runs LAST, after every substantive rewrite, with before/after counts reported. A structural review that predates the final rewrite counts for nothing.
