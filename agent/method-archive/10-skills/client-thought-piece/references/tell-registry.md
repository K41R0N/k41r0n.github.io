# Tell Registry: What Gets a Draft Clocked as Machine-Written

Compiled from two forensic review rounds on the founding six-piece set (2026-08-19). The lexical layer is table stakes; the structural layer is what actually failed twice and required rebuilds. A skeptical editor "would clock the set within two pieces, and not from vocabulary, which has been scrupulously laundered... The fingerprint is entirely architectural."

## Layer 1: Lexical bans (absolute, grep for these)

- Em dashes (any), "not just X but Y" and all recastings of it
- Sentence-initial connectives: Additionally, Furthermore, Moreover, In conclusion, However-comma as formulaic pivot
- Hashtags
- AI filler verbs/bridges: demonstrating, underscoring, highlighting, reflecting (bridging number to claim), leveraging, harnessing, capitalizing on
- Filler nouns: continued momentum, strong fundamentals, robust performance, sustained growth, key metrics/drivers/takeaways
- Fake-segue frames: "It's worth noting that", "That said,", "With that in mind,", "At the end of the day,", announced structure ("Having examined X, we now turn to Y")
- the client register: profit (loose), AUM, assets under management, bank, deposits, interest, earnings call, tokenized fund; never confirm the central-bank narrative; never hardcode a rate

## Layer 2: Structural tells (the ones that survive word-scrubbing)

Each entry: the tell, why it reads as machine, and the budget.

1. **The shared opening macro.** Six pieces that all open on a dated historical anchor is a template even when every date differs; so is all-thesis-aphorism openings. *Budget: no two pieces in a set share an opening type. Menu: scene, mid-argument, polemic, live moment inside the system, profession, document.*
2. **Ring composition everywhere.** Closing every piece by re-ringing its opening image. Humans ring the bell occasionally and let other essays end somewhere the opening didn't predict. *Budget: at most a third of a set.*
3. **Uniform kicker cadence.** A polished epigram at the end of nearly every paragraph is "the single strongest statistical tell: human paragraphs sometimes just stop." *Budget: 2-3 kickers per piece; several paragraphs end flat on a fact.*
4. **Negation-correction as house style.** "Not X but Y", "isn't X. It's Y.", "was never X. It was Y." The founding set had eleven across six pieces after one scrub. *Budget: one per piece, zero is fine.*
5. **The catechism.** Author poses a question, author answers it. Legal once per set, as a piece's central conceit (the governance piece's "Who decides? What stops them?"). *Budget: one per set.*
6. **Anaphoric spec-lists.** Fragment chains ("How much X. How much Y. What happens Z.") as body paragraphs, in piece after piece. *Budget: one deliberate anaphora per set, where the rhetoric earns it (e.g., enumerating prohibitions).*
7. **Triads, especially with an extended third item** ("some pool, some wrapper, some integration nobody remembered approving"). Fine individually; a tell at one per paragraph. *Budget: roughly one per piece.*
8. **Gradatio / "which means" chains.** "An allocation problem, which means an alignment problem, which is the oldest problem in finance." Keep the best one in a set; flatten the rest.
9. **Demonstrative meta-pointers.** "That is the claim worth making." "This, in the end, is what X amounts to." Tour-guide sentences narrating the essay's own argument. Cut at least half; a strong sentence needs no guide.
10. **Copular epigrams** ("the order of the queue is the ethics of the system"). One per set is a jewel; four is a machine.
11. **Duplicate moves across a set.** The same proof point, metaphor, or sentence shape appearing in two pieces (the rate-cut-as-tradeoff framing, "to the penny" twice, the worst-case-question move twice). One engine wrote everything; don't let it show. Partition material before drafting; sweep for duplicates in review.
12. **Manufactured rhythm.** The short-long-punch wave, twin two-word fragments in one piece ("Nobody did." ... "Some did."), equal-length paragraphs. Real variance includes stretches with no punch.
13. **Meta wrap-up endings.** "Step back and the through-line of every pillar comes into focus." Recap-and-declare closers deflate the piece and break standalone publication.
14. **Cute flourishes and self-narration.** "It's worth pausing on how strange that is", "usually phrased politely", "almost embarrassingly old", strained coinages forced by parallelism ("hope about"), unattributed aphorisms wearing the costume of quotation. His register is declarative; it doesn't narrate its own pauses or decorate mechanisms.
15. **Analogy that proves the opposite.** If the anchor breaks under a hostile reading, concede the asymmetry explicitly; the concession reads human and strengthens the claim.
16. **Rewrite knock-ons.** Edits introduce their own tells: a phrase duplicated into two nearby sentences, the same concession marker in two pieces, "every market regime" twice in one sentence. Always end with a full-file read hunting specifically for these.

17. **Corpus collision.** The same climax shape, punchline, or proof-point framing re-landed in a different artifact or byline. Emerged at artifact four: two sentence shapes reached third use across three bylines before a reviewer caught them. Sweep every draft against `references/corpus-registry.md`; append spent lines at every delivery. *Budget: zero, always.*

18. **Seed-echo.** New material duplicating a seed paragraph's frame verbatim ("published before it took effect" reprinted from the seed's "published before they take effect"). Cohesion wants the motif; detection reads the frame. Keep the payoff, vary the wording. See the seed-echo section of `references/corpus-registry.md`.

19. **Regrowth after a substantive rewrite.** Fix rounds (argument, facts, compliance, voice) regrow structural tells: rewriting under pressure produces signposts, punch-paragraphs, and re-landed favorite lines. The John op-ed's V2 fixed everything else and came out 300 words longer and denser in tells than V1. A fix round that grows the word count is presumptively regrowing tells; the subtraction pass re-runs after every such round, measured per `references/structural-audit.md`.

## The two-question test before shipping

1. Would a skeptical editor who reads LLM output daily clock this, and from what, precisely? (If the answer names anything in Layer 2, keep working.)
2. Does any pattern appear three or more times across the set? (If yes, it's a template, whatever it is, even if it's beautiful.)
