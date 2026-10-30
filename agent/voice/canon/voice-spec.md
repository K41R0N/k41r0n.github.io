---
type: VoiceSpec
title: "Voice spec v0, Alejandro Arango, register: essay"
confidence: proposed
tier: 2
approver: Alejandro Arango
status: PROPOSED. Measured, not yet confirmed by the approver. Nothing here is a rule until he confirms it.
built_from: corpus/raw/ only (9 essays, all confirmed by him as fully his prose on 2026-10-28). Recency weighting applied at his request. Holdout (2 essays) excluded and verified absent (reports/verification.md V3).
generated_by: tools/build_spec.py -> tools/spec_v0.json -> tools/gen_spec_md.py
---
# Voice spec v0 (essay register)

**What this is.** Measured habits from nine of his own Substack essays, about 14754 words and 736 sentences. Each row shows the recency-weighted mean (the headline number, see Weighting), the plain mean, the lowest and highest piece, and the weighted spread between pieces. The range is the point: a draft is "in voice" for a metric when it lands inside his own min-to-max, not when it hits the mean.

**What this is not.** Not a style guide and not proof of voice. It covers the measurable half only (see HARNESS.md section 1). Corpus is small: with n=9 the ranges are wide and will move when more of his writing is added. Registers other than essay (thesis pages, short posts, about copy) have no measured spec yet because no verified self-written samples exist.

## Weighting (his instruction: more recent essays carry higher priority)
Method: exponential recency weight with a 12-month half-life, relative to the newest raw essay. A piece 12 months older than the newest counts half as much. Weights by piece are in `tools/spec_v0.json` under `weighting`. The 12-month half-life is my choice, not his. It is mild on purpose: the corpus is small and one essay (2026-09-20) sits about a year after the rest. He can set a different half-life (one constant in `tools/build_spec.py`). Min and max ranges stay unweighted across all nine pieces, because a range is about what he has done, not what he does most recently.

## Sentence rhythm
| metric | recency-weighted mean | unweighted mean | range across pieces | weighted between-piece sd |
|---|---|---|---|---|
| mean sentence length (words) | 19.96 | 20.20 | 16.76 to 23.39 | 2.07 |
| median sentence length | 18.26 | 18.39 | 14.00 to 23.00 | 2.52 |
| sentence length sd (burstiness) | 10.69 | 10.73 | 8.88 to 12.67 | 1.09 |
| share under 8 words | 0.100 | 0.094 | 0.045 to 0.189 | 0.043 |
| share over 25 words | 0.276 | 0.283 | 0.149 to 0.426 | 0.079 |
| share over 32 words | 0.127 | 0.130 | 0.055 to 0.213 | 0.055 |

Pooled sentence lengths: median 18, 10th percentile 8, 90th percentile 35, longest 62.

## Paragraph shape
| metric | mean | range | sd |
|---|---|---|---|
| sentences per paragraph | 2.04 | 2.03 | 1.63 to 2.55 | 0.27 |
| share of one-sentence paragraphs | 0.361 | 0.359 | 0.179 to 0.488 | 0.092 |
| share of 5+ sentence paragraphs | 0.014 | 0.012 | 0.000 to 0.060 | 0.019 |

## Punctuation and typography (per 1000 words)
| metric | mean | range | sd |
|---|---|---|---|
| em dash | 0.07 | 0.08 | 0.00 to 0.73 | 0.22 |
| en dash | 0.05 | 0.06 | 0.00 to 0.50 | 0.15 |
| spaced hyphen dash | 0.23 | 0.27 | 0.00 to 1.40 | 0.42 |
| comma | 54.61 | 53.48 | 43.76 to 63.92 | 7.76 |
| semicolon | 2.78 | 2.75 | 0.80 to 5.61 | 1.29 |
| colon | 2.65 | 2.75 | 0.73 to 5.21 | 1.38 |
| paren open | 1.72 | 1.73 | 0.00 to 3.64 | 1.10 |
| question | 3.76 | 3.89 | 2.58 to 6.55 | 1.20 |
| exclaim | 0.07 | 0.08 | 0.00 to 0.73 | 0.22 |
| ellipsis | 0.22 | 0.19 | 0.00 to 0.73 | 0.27 |
| curly apos | 26.45 | 26.04 | 6.54 to 40.12 | 10.98 |
| straight apos | 6.43 | 7.36 | 0.00 to 32.27 | 10.54 |
| curly dq | 9.74 | 8.56 | 0.00 to 18.67 | 6.21 |
| straight dq | 3.61 | 4.06 | 0.00 to 11.45 | 4.69 |
| contraction | 32.59 | 33.06 | 25.49 to 40.08 | 4.86 |
| italic marks | 1.74 | 1.79 | 0.52 to 3.23 | 0.86 |
| bold marks | 2.79 | 3.06 | 0.73 to 6.39 | 1.69 |
| headings | 1.15 | 1.33 | 0.00 to 3.52 | 1.31 |
| list items | 0.05 | 0.06 | 0.00 to 0.52 | 0.15 |
| oxford comma per 1000 | 5.88 | 5.92 | 3.20 to 10.57 | 1.86 |

Note: curly and straight apostrophes and quotes both appear, which is a Substack/CMS artifact and not a decision. Do not treat either as voice. Dashes: em dash 0.08 per 1000 words, essentially absent; spaced hyphen as dash 0.27.

## Person, discourse markers, lexical variety
| metric | mean | range | sd |
|---|---|---|---|
| mattr500 | 0.57 | 0.57 | 0.53 to 0.59 | 0.02 |
| hapax ratio | 0.68 | 0.68 | 0.64 to 0.71 | 0.02 |
| first person I per 1000 | 17.24 | 18.01 | 7.05 to 43.96 | 9.76 |
| second person you per 1000 | 13.15 | 12.95 | 3.64 to 26.99 | 7.71 |
| we per 1000 | 18.72 | 18.11 | 9.48 to 31.32 | 7.38 |
| disc but per 1000 | 6.50 | 6.25 | 4.03 to 8.45 | 1.57 |
| disc and per 1000 | 24.82 | 24.40 | 18.92 to 29.67 | 3.69 |
| disc so per 1000 | 2.24 | 2.35 | 1.04 to 3.50 | 0.84 |
| disc however per 1000 | 0.24 | 0.16 | 0.00 to 0.89 | 0.37 |
| disc though per 1000 | 0.43 | 0.49 | 0.00 to 1.46 | 0.44 |
| disc yet per 1000 | 0.88 | 0.90 | 0.00 to 2.40 | 0.56 |
| disc instead per 1000 | 0.49 | 0.58 | 0.00 to 3.20 | 0.94 |
| disc honestly per 1000 | 0.00 | 0.00 | 0.00 to 0.00 | 0.00 |
| disc genuinely per 1000 | 0.07 | 0.08 | 0.00 to 0.73 | 0.22 |
| disc actually per 1000 | 1.14 | 1.31 | 0.00 to 2.52 | 0.89 |
| disc really per 1000 | 0.74 | 0.71 | 0.00 to 2.19 | 0.65 |
| disc maybe per 1000 | 0.24 | 0.26 | 0.00 to 1.01 | 0.38 |
| disc probably per 1000 | 0.56 | 0.59 | 0.00 to 2.07 | 0.57 |
| disc basically per 1000 | 0.00 | 0.00 | 0.00 to 0.00 | 0.00 |
| disc literally per 1000 | 0.00 | 0.00 | 0.00 to 0.00 | 0.00 |
| disc look per 1000 | 0.45 | 0.47 | 0.00 to 1.40 | 0.40 |
| disc sure per 1000 | 0.27 | 0.31 | 0.00 to 1.03 | 0.36 |
| disc still per 1000 | 1.27 | 1.18 | 0.00 to 2.92 | 0.94 |
| disc anyway per 1000 | 0.06 | 0.08 | 0.00 to 0.70 | 0.20 |
| sent start but share | 0.06 | 0.06 | 0.02 to 0.14 | 0.04 |
| sent start and share | 0.05 | 0.05 | 0.02 to 0.08 | 0.02 |
| sent start so share | 0.01 | 0.01 | 0.00 to 0.02 | 0.01 |
| sent start or share | 0.00 | 0.00 | 0.00 to 0.03 | 0.01 |
| sent start because share | 0.00 | 0.00 | 0.00 to 0.01 | 0.00 |
| sent start which share | 0.00 | 0.00 | 0.00 to 0.02 | 0.01 |
| sent start that share | 0.00 | 0.01 | 0.00 to 0.02 | 0.01 |

## Function-word profile (per 1000 words)
Highest-frequency function words with his mean and range. These are the habits stylometry relies on. Full table in tools/spec_v0.json.

| word | mean | range |
|---|---|---|
| the | 46.8 | 28.0 to 58.2 |
| to | 36.2 | 25.5 to 41.9 |
| of | 26.5 | 19.6 to 31.2 |
| a | 24.7 | 17.8 to 35.5 |
| and | 24.4 | 18.9 to 29.7 |
| in | 13.9 | 8.9 to 21.7 |
| i | 12.8 | 3.5 to 34.4 |
| that | 12.1 | 6.5 to 18.9 |
| is | 10.5 | 4.0 to 16.0 |
| it | 8.3 | 5.2 to 11.7 |
| you | 8.0 | 2.1 to 17.5 |
| for | 7.8 | 4.9 to 11.6 |
| we | 7.8 | 3.6 to 16.8 |
| or | 7.0 | 2.4 to 9.8 |
| their | 6.6 | 1.6 to 13.6 |
| as | 6.3 | 4.4 to 11.1 |
| with | 6.3 | 3.1 to 12.4 |
| but | 6.3 | 4.0 to 8.4 |
| be | 6.2 | 3.0 to 10.2 |
| are | 5.5 | 1.6 to 9.3 |
| my | 5.4 | 1.0 to 12.1 |
| when | 5.3 | 4.0 to 7.8 |
| what | 4.9 | 2.4 to 8.1 |
| this | 4.9 | 2.5 to 9.6 |
| how | 4.8 | 2.2 to 8.8 |
| out | 4.5 | 1.5 to 11.7 |
| on | 4.4 | 2.4 to 6.4 |
| more | 4.3 | 2.1 to 7.2 |
| about | 4.1 | 1.5 to 7.2 |
| our | 3.9 | 0.8 to 6.8 |
| like | 3.9 | 1.4 to 6.6 |
| have | 3.9 | 2.2 to 5.6 |
| an | 3.9 | 2.2 to 8.7 |
| at | 3.8 | 1.5 to 5.8 |
| if | 3.7 | 0.8 to 5.8 |
| they | 3.7 | 1.5 to 7.5 |
| all | 3.6 | 2.1 to 5.8 |
| by | 3.4 | 1.3 to 5.7 |
| do | 3.3 | 1.5 to 5.7 |
| not | 3.3 | 1.5 to 5.6 |

## Things that stand out against the client rule set (read before adopting any rule)
- Sentences over 32 words are about 13% of his sentences (range 6% to 21% by piece). A 32-word hard cap would fail every piece he has published.
- "We/our/us" runs 18 per 1000 words and "I" 18. Both are habits to preserve in drafts; why he uses them is for him to say.
- One-sentence paragraphs are 36% of his paragraphs; paragraphs of 5+ sentences are almost absent. His paragraph range is 1 to 4 sentences, not 1 to 8.
- He uses "really", "actually", "just", "very" at a combined rate of about 6.7 per 1000 words (the client banned-filler list). That list does not describe him.
- Semicolons 2.8 and colons 2.8 per 1000 words: both used, moderately.

