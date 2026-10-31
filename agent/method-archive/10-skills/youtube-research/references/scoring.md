# Scoring methodology

The goal is to rank *what a careful researcher would want to watch first*, not what the YouTube algorithm pushed hardest. View count is a weak proxy for quality: it rewards clickbait, channel size and age. So the score blends six components, each 0–1, with mode-specific weights, and a curated trust layer sits on top.

```
score = 100 × ( wR·R + wA·A + wE·E + wV·V + wT·T + wF·F )
```

| Component | What it measures | Main inputs |
|---|---|---|
| **R** relevance | Does the video actually address the query? | query-term coverage in title (65%) and description/tags (35%); rank position across query variants; appearing in several variants earns a bonus |
| **A** authority | Is the *channel* a credible source? | log-scaled subscribers (40%), audience health (25%), topical focus (15%), long-form ratio (10%), verified badge (10%); then institutional-pattern bump, shill-pattern halving, and trusted-list floors/caps |
| **E** engagement | Did viewers respond unusually well *for a channel of that size*? | (likes+comments)/views vs. the median for the channel's subscriber tier (75%); comments-per-like discussion depth (25%) |
| **V** reach | How many people saw it (damped) | log10(views)/7 — 10M views → 1.0, 100k → 0.71, 10k → 0.57 |
| **T** recency | How fresh | exponential decay with a mode-specific half-life |
| **F** format fit | Is the length/format right for the job? | duration bands per mode; Shorts and live streams adjusted |

## Mode weights

| Mode | R | A | E | V | T | F | Half-life | Intent |
|---|---|---|---|---|---|---|---|---|
| `topic` | .30 | .25 | .20 | .10 | .10 | .05 | 365 d | map the landscape: who talks about X, from what angles |
| `learn` | .30 | .25 | .20 | .05 | .05 | .15 | 730 d | find the best explainers; evergreen; 6–45 min preferred |
| `expert` | .25 | .35 | .15 | .05 | .10 | .10 | 540 d | authoritative long-form: talks, interviews, panels |
| `brand` | .35 | .10 | .15 | .15 | .20 | .05 | 180 d | perception audit: what people actually see *now*, critics included — authority is deliberately low so critical small channels are not hidden |

## Engagement benchmarks (tier-normalised)

Raw engagement ratios punish big channels and flatter tiny ones, so E compares each video with the median for its channel tier. Benchmarks are the 2026 SociaVault study of 75,000 channels (formula: (likes + comments) / views):

| Tier | Subscribers | Median ER |
|---|---|---|
| nano | < 10k | 5.23 % |
| micro | 10k – 50k | 3.74 % |
| mid | 50k – 100k | 2.81 % |
| macro | 100k – 500k | 2.12 % |
| mega | ≥ 500k | 1.41 % |
| unknown | — | 3.06 % (overall median) |

`E_er = clamp(0.5 + 0.25·log2(ER / benchmark))`: at benchmark → 0.5, 2× → 0.75, 4× → 1.0, ½× → 0.25. Videos under 500 views are capped at 0.6 (`low-sample`); hidden like counts give a neutral 0.5 (`likes-hidden`). Education/how-to content runs ~1.5× the overall median, so expect explainers to cluster above 0.5 — compare within a run, not across runs.

## Authority details

- `subs_score = log10(subs+1)/7` → 1k 0.43 · 10k 0.57 · 100k 0.71 · 1M 0.86 · 10M 1.0
- `audience_health` from channel enrichment: median views of the last ~20 uploads ÷ subscribers, log-mapped so ≥ 30 % → ~1.0, 5 % → 0.6, 1 % → 0.25, < 0.3 % → 0. Catches decayed or bought audiences (huge subs, tiny views).
- `topical_focus`: share of recent upload titles containing a query term. Generalist media score low here by design; their size and the trusted list carry them.
- `longform_ratio`: share of recent uploads over 8 minutes (depth vs. Shorts farms).
- Institutional name patterns (university, foundation, conference, research, central bank…) add +0.05.
- Shill patterns in channel name or recent titles (100x, giveaway, airdrop, guaranteed, get rich, to the moon…) halve A and flag `shill-pattern`.
- Trusted lists: tier A floor 0.92 · tier B floor 0.78 · blocked cap 0.08. Lists are matched by @handle, then normalised channel name. Each report lists which entries matched so unmatched handles can be fixed.
- Without channel enrichment (`--no-channel-enrich`, or when it was blocked) health/focus/long-form fall back to neutral values and the run notes say so.

## Relevance details

Query terms are lower-cased, stop-worded, and matched with a crude prefix stem (so "staking" matches "stake"). In `brand` mode the full brand phrase must appear in the title (coverage 1.0) or description/tags (0.7); otherwise the video is flagged `brand-not-in-metadata` and capped at 0.3 — it may still mention the brand in speech, so transcripts are the fix when that matters.

Rank signal: `1/(1 + rank/8)` for the best position across variants, +0.1 per additional variant hit (max +0.3). A video surfacing for "X explained", "what is X" *and* "X tutorial" is more central to the topic than one that appears once.

## Format fit

| Mode | 1.0 | 0.7–0.8 | ≤ 0.5 |
|---|---|---|---|
| learn | 6–45 min | 3–6 or 45–90 min | > 90 (0.5), < 3 (0.3); live ×0.8 |
| expert | 15–120 min | > 120 (0.8), 6–15 (0.7) | < 6 (0.3) |
| topic | 4–60 min | otherwise 0.7 | Shorts 0.4 |
| brand | everything | — | Shorts 0.6 |

Shorts (≤ 60 s) are excluded from the pool by default (`--include-shorts` to keep them); live/upcoming streams are always dropped at search time; videos longer than `--max-minutes` (default 300) are dropped as streams.

## Diversity cap

At most `--max-per-channel` (default 3) videos per channel enter the top list; the rest remain in `results.json` and the "remaining candidates" table so nothing is lost.

## What the score is not

It is a prioritisation aid for a human-plus-Claude reading, not a verdict on truthfulness or production quality. Two guard-rails follow from that: cite the underlying numbers when a ranking claim matters, and treat the heuristic comment sentiment tally as a pointer to read samples, never as a measured sentiment figure.

Sources for benchmarks: SociaVault, "What Is a Good Engagement Rate on YouTube in 2026" (75k channels); YouTube Data API quota documentation (100 `search.list` calls/day + 10,000 units/day for other endpoints).
