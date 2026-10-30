---
type: DoDont
title: "Do / Don't rules, seeded"
confidence: proposed
tier: 2
approver: Alejandro Arango
status: PROPOSED. Each line becomes Tier 1 only when he confirms it. Source column says where the rule came from. Rules inherited from his client brand harnesses were run against his own essays (reports/verification.md V4); the result is in the last column.
---
# Do / Don't (seeded, unconfirmed)

Ported as methodology only. No client names, product names or legal rules are carried over. "Client rule" means the rule was written for a client brand's voice; it does not describe him unless the test column says so.

## A. Rules that rarely flag his own writing (propose to adopt)
| id | rule | source | own-writing test |
|---|---|---|---|
| A1 | No exclamation marks | client rule | 1 hit in 16.9k words |
| A2 | No hashtags | client rule | 0 hits |
| A3 | Dashes are a budget, not a ban: at most about 1 per 1000 words, never as habitual punctuation. His own use is 6 dash-like marks in 16.9k words (em dash 2, en dash 1, spaced hyphen " - " 3), about 0.35 per 1000. His usual dash is the spaced hyphen, not the em dash. | client rule, loosened | The holdout holds 1 of the 6 (an em dash in "Hic Sunt Dracones"), so the holdout is partly spent for this rule. A second build counted 3 of 4 in the holdout; counting method differs, unresolved. |
| A4 | No Additionally / Furthermore / Moreover / In conclusion transitions | client rule | 0 hits |
| A5 | No soft fillers ("in essence", "at the end of the day", "when it comes to", "it's worth noting") | client rule | 3 hits, 2 of 11 pieces |
| A6 | No false-depth openers ("At its core", "Here's the thing", "The real question is") | craft layer tell catalog | 0 hits |
| A7 | No interpretive wrappers ("This matters because", "a testament to", "marks a shift") | craft layer (named the strongest single tell) | 0 hits |
| A8 | No participial significance endings (", underscoring / highlighting / demonstrating") | craft layer | 0 hits |
| A9 | No copula avoidance ("serves as", "stands as", "boasts") | craft layer | 1 hit |
| A10 | Hedging stacks: not two of may / might / could / potentially / arguably in one sentence | craft layer | 2 hits, 2 of 11 pieces |
| A11 | Burstiness floor: at least one sentence under 8 words and one over 25 per piece | craft layer | passes 11 of 11 |
| A12 | Vary paragraph mass; a page of all 2-to-4-sentence paragraphs reads generated | craft layer, client ruling | his one-sentence share is 36%, uniform-mass test never fires |
| A13 | Not more than 2 bold lead-in stacks per page ("**Lead:** sentence") | craft layer | 0 hits |
| A14 | Accumulation scoring: one tell is a look, two or more on a page is a fail | craft layer | n/a, a scoring policy |

## B. Rules that flag most of his own pieces (do NOT adopt as default)
| id | rule | source | own-writing test | decision for him |
|---|---|---|---|---|
| B1 | Hard cap of 32 words per sentence | client rule | fails 11 of 11 pieces, 13% of his sentences | His mean is 20 words and 28% of sentences run over 25. Use his own range from voice-spec instead. |
| B2 | Banned filler: very, really, quite, just, actually, simply | client rule | 11 of 11 pieces, 6.6 per 1000 words | These are part of how he writes. Keep a narrower list only if he picks it. |
| B3 | Target 20 words or fewer per sentence | client rule | 42% of his sentences are over 20 words (mean 20.2, median 18) | Replace with his measured range. |

## C. Borderline, needs his call
| id | rule | own-writing test |
|---|---|---|
| C1 | Banned AI lexicon (robust, leverage, harness, realm, crucial, pivotal, foster, etc.) | 4 hits in 4 of 11 pieces, all in essays about AI writing where he quotes or names the tell. The rule needs a quote exemption. |
| C2 | Metronome run: four sentences in a row each within 3 words of the previous | 4 of 11 pieces, 0.35 per 1000 words. Tightened from a 3-in-a-row version that flagged 10 of 11 pieces. |

## C3. Range checks
WARN only, never block. Flag a draft only when 3 or more of 25 structural features fall outside his own range widened by 50%. On his own leave-one-out pieces: 0 of 9 reach 3. Function-word ranges are excluded because they are too noisy at this size.

## D. Method rules (how the engine works, not about his sentences)
- D1. Apply a rule that produces an awkward sentence, then flag it. A human decides the override. Never soften silently.
- D2. Every edit carries its rule source in the change log, so any rule can be challenged and not just the edit.
- D3. Never invent a number. Never use a stale number.
- D4. No brief, no work.
- D5. Judgment steps (big idea, what to say, what to refuse to say) are never scripted.
- D6. The engine polishes. It never invents, expands, deletes sections or changes position.
