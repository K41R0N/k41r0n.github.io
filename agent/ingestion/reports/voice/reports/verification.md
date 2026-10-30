# Verification report (phase 1)

## V1. Every corpus file is his writing

Evidence available: Substack byline via public API, canonical URL, and a second copy of each essay in the kairon.xyz repo. This establishes publication under his byline. It cannot rule out AI assistance (no disclosure statements found in any piece by grep). Tier-2 caveat stands until he confirms.

| file | split | url | byline in header | repo copy match |
|---|---|---|---|---|
| 2025-06-04-why-im-building-things-that-dont.md | raw | https://k41r0n.substack.com/p/why-im-building-things-that-dont | yes (Alejandro "Kairon" Arango) | 0.98 (first 400 words) |
| 2025-06-11-the-future-belongs-to-the-storytellers.md | raw | https://k41r0n.substack.com/p/the-future-belongs-to-the-storytellers | yes (Alejandro "Kairon" Arango) | 1.00 (first 400 words) |
| 2025-06-17-were-not-getting-dumber.md | raw | https://k41r0n.substack.com/p/were-not-getting-dumber | yes (Alejandro "Kairon" Arango) | 0.95 (first 400 words) |
| 2025-06-28-think-of-the-children.md | raw | https://k41r0n.substack.com/p/think-of-the-children | yes (Alejandro "Kairon" Arango) | 0.99 (first 400 words) |
| 2025-07-12-the-myth-of-10x.md | raw | https://k41r0n.substack.com/p/the-myth-of-10x | yes (Alejandro "Kairon" Arango) | 1.00 (first 400 words) |
| 2025-07-29-re-learning-to-trust-each-others.md | raw | https://k41r0n.substack.com/p/re-learning-to-trust-each-others | yes (Alejandro "Kairon" Arango) | 1.00 (first 400 words) |
| 2025-08-21-techno-feudalistic-quixotes.md | raw | https://k41r0n.substack.com/p/techno-feudalistic-quixotes | yes (Alejandro "Kairon" Arango) | 1.00 (first 400 words) |
| 2025-09-11-antitech.md | raw | https://k41r0n.substack.com/p/antitech | yes (Alejandro "Kairon" Arango) | 1.00 (first 400 words) |
| 2026-09-20-shadow-work.md | raw | https://k41r0n.substack.com/p/shadow-work | yes (Alejandro "Kairon" Arango) | 1.00 (first 400 words) |
| 2025-11-21-why-do-devs-get-so-much-free-sht.md | holdout | https://k41r0n.substack.com/p/why-do-devs-get-so-much-free-sht | yes (Alejandro "Kairon" Arango) | 1.00 (first 400 words) |
| 2025-12-31-hic-sunt-dracones.md | holdout | https://k41r0n.substack.com/p/hic-sunt-dracones | yes (Alejandro "Kairon" Arango) | 0.99 (first 400 words) |

Excluded (authorship pending, NOT used anywhere in the spec):

- about.md
- pages__about.md
- projects__interactive-quiz-maker.md
- projects__notion-as-cms.md
- projects__notion-telegram-bot.md
- projects__openclaw-personal-infrastructure.md
- projects__opensource-curriculum.md
- projects__rm-quickshare-bot.md
- projects__threadbot.md
- projects__uh-vibe-checker.md
- theses__better-discovery-engines.md
- theses__devices-as-co-creations.md
- theses__future-belongs-to-storytellers.md

## V2. Spec computations cross-checked with an independent method

| quantity | main method | independent method | relative diff |
|---|---|---|---|
| total words | 14754.00 | 14640.00 | 0.8% |
| total sentences | 736.00 | 707.00 | 4.1% |
| mean sentence length | 20.05 | 20.71 | 3.2% |
| commas per 1000 words (pooled) | 53.48 | 55.19 | 3.1% |
| 'the' per 1000 words | 46.80 | 48.29 | 3.1% |

Result: PASS (all within 5%; per-piece means vs pooled differ slightly by design)

Hand-check sample (first 8 sentences of one raw piece, with computed lengths) - read these against the source:

- [15] You’ve probably heard tech people talk about 10x founders, 10x engineers, 10x marketers, yadda yadda…
- [34] Ever since automation, no-code, and agents became consumer-ready, Silicon Valley types started foaming at the mouth at the prospect of a sin
- [10] But I’m genuinely starting to wonder what that truly means.
- [18] It’s hard to deny that people can do more nowadays than they could five or ten years ago.
- [31] Though, there’s a very real argument to be made about “productivity” being a fool’s errand meant to soothe investors and executives’ egos, r
- [31] I don’t usually jump to conclusions with deconstructing the meaning or intention of the things we’ve come to value, particularly when it com
- [11] But this one has been wracking my brain for a while.
- [24] It may come as a blow to our collective professional ego, and it’s more than likely I’ll gather some Zappier and N8N wizards’ ire.

## V3. Holdout never leaked into the spec

- spec file list contains 9 files; holdout names present: False; holdout hashes present: False
- rebuilt spec with the holdout folder emptied/replaced by junk: identical to the committed build = True
- committed spec equals fresh rebuild = False

## V4. Seeded rules run against his own writing (false-positive rate)

Every one of his published pieces is treated as a known-good "sound like me" sample, so any flag on his own writing is a false positive for the rule as a description of HIM. Rules inherited from a client brand were never promised to match his habits; this test finds which ones do.

11 pieces, 16948 words

| rule | severity | origin | pieces flagged | hits per 1000 words | verdict |
|---|---|---|---|---|---|
| P01 no em dash | FAIL | client-brand | 2/11 | 0.12 | keep (rarely flags him) |
| P02 no en dash | FAIL | client-brand | 1/11 | 0.06 | keep (rarely flags him) |
| P03 no exclamation marks | FAIL | client-brand | 1/11 | 0.06 | keep (rarely flags him) |
| P04 no hashtags | FAIL | client-brand | 0/11 | 0.00 | keep (rarely flags him) |
| W01 banned filler: very, really, quite, just, actually, sim | WARN | client-brand | 11/11 | 6.61 | DO NOT ADOPT as default: flags most of his own pieces, so it describes the client brand or a noisy test, not him |
| W02 banned AI lexicon | WARN | client-brand + craft tell catalog | 4/11 | 0.24 | candidate: ask him |
| W03 soft fillers | WARN | client-brand | 2/11 | 0.18 | keep (rarely flags him) |
| W04 false-depth openers | WARN | craft tell catalog | 0/11 | 0.00 | keep (rarely flags him) |
| W05 interpretive wrapper phrases | WARN | craft tell catalog | 0/11 | 0.00 | keep (rarely flags him) |
| W06 Additionally/Furthermore/Moreover/In conclusion | WARN | client-brand | 0/11 | 0.00 | keep (rarely flags him) |
| W07 hedging stack: 2+ of may/might/could/potentially/arguab | WARN | craft tell catalog | 2/11 | 0.12 | keep (rarely flags him) |
| S01 sentence over 32 words (hard cap) | FAIL | client-brand | 11/11 | 6.25 | DO NOT ADOPT as default: flags most of his own pieces, so it describes the client brand or a noisy test, not him |
| S02 participial significance ending (, reflecting/underscor | WARN | craft tell catalog | 0/11 | 0.00 | keep (rarely flags him) |
| S03 copula avoidance (serves as / stands as / boasts) | WARN | craft tell catalog | 1/11 | 0.06 | keep (rarely flags him) |
| R01 burstiness: has a sentence under 8 words (piece-level,  | FAIL | craft burstiness floor | 0/11 | 0.00 | keep (rarely flags him) |
| R02 burstiness: has a sentence over 25 words (piece-level) | FAIL | craft burstiness floor | 0/11 | 0.00 | keep (rarely flags him) |
| R03 four consecutive sentences each within 3 words of the p | WARN | craft burstiness floor | 4/11 | 0.35 | candidate: ask him |
| R04 paragraph mass uniform: share of 2-4 sentence paragraph | WARN | craft tell catalog | 0/11 | 0.00 | keep (rarely flags him) |
| R05 bold lead-in stacks (3+ "**Lead:** sentence") | WARN | craft tell catalog | 0/11 | 0.00 | keep (rarely flags him) |

## V5. Burrows Delta (stylometry) on the holdout, with different-author controls

**Delta is a SOFT signal, not a gate.** At this corpus size the distributions overlap (see below). Use it as one input to a human judgment.

Delta = mean absolute z-score distance from his raw-corpus profile over his 100 most frequent words. Lower = closer. Texts are scored against the raw corpus only (holdout never in the reference).

- raw LOO: n=9, mean 1.060, min 0.847, max 1.325
- holdout: n=2, mean 1.103, min 1.039, max 1.168
- control: n=20, mean 1.376, min 1.093, max 1.667
  - holdout 2025-11-21-why-do-devs-get-so-much-free-sht.md: 1.039
  - holdout 2025-12-31-hic-sunt-dracones.md: 1.168
- Control chunks (other human author, ~1500 words each) farther than the worst holdout piece: 95%
- Overlap: 3 of his own leave-one-out pieces score as far as or farther than the closest control chunk. That is why Delta cannot gate anything.
- Caveat: n is tiny and chunk length differs from his pieces. This shows the measure separates authors at all; it does not prove the spec captures him. The blind test is the real calibration.

## V6. Range check calibration (leave-one-out on his own pieces)

25 structural features, ranges from the other pieces widened 50%. Features outside range per own piece: [1, 0, 0, 0, 1, 1, 1, 1, 0]. Pieces at or over the 3-feature WARN threshold: 0 of 9.
Strict min-max over all 57 features (with function words) put every one of his own pieces 10 to 20 features out of range, so that version was rejected. Range checks are WARN only and never block.
- holdout 2025-11-21-why-do-devs-get-so-much-free-sht.md: 0 of 25 features outside his own range -> ok
- holdout 2025-12-31-hic-sunt-dracones.md: 2 of 25 features outside his own range -> ok
