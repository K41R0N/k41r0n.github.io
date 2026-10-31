# Output templates per mode

The script produces machine output (`report.md`, `results.json`, CSVs, transcripts, comments). The human-facing write-up is Claude's job. Default delivery is the write-up in chat plus the run folder's CSV/JSON files; produce a Claude Doc, Google Sheet / Excel workbook or HTML dashboard only when asked (or when the user's standing preference says so).

Rules that apply to every template:

- Every substantive claim points at a video: `[Title — Channel](url)`. Quotes from transcripts carry a timestamp, e.g. `(12:40)`; the transcript files already prefix each ~30 s block with one.
- Keep data and interpretation visibly separate: numbers and flags first, then what they suggest.
- State coverage honestly: how many candidates, how many enriched, which stages were skipped or blocked, how many trusted-list entries matched, whether likes were hidden or samples small.
- Mark channel trust visibly: trusted tier (A/B), official/affiliated, shill-pattern, blocked. In brand mode, owned media (the brand's own channel) is always separated from earned media.
- Never present the lexicon sentiment tally as measured sentiment. Read the top-liked and a random handful of comments before characterising reception.
- If anything from the run will be used in external communications, remind the user it goes through the normal review gates for that client (for the client work: the client a source document + a legal reviewer guidelines).

---

## `topic` — Topic landscape

```
# YouTube landscape: <query>
_<n> videos ranked from <pool> candidates · <variants> query variants · collected <date> · mode topic_

## What the data shows
- Volume & freshness: how many videos, how recent, views/day of the leaders
- Who owns the conversation: top 5–8 channels with tier, trust flag, videos in top list
- Angles: 3–6 clusters of how the topic is framed (from titles/descriptions), each with 1–3 example videos
- Engagement standouts: videos far above tier benchmark (and why that might be)

## Ranked list (top <n>)
<table: #, score, video link, channel [tier/trust], published, length, views, ER vs tier, flags>

## Interpretation
- Where the trusted voices agree / disagree
- Gaps: angles nobody credible covers; audiences underserved
- Watch next: 3–5 videos and the reason for each

## Coverage & caveats
<counts, skipped stages, trusted matches, hidden likes, blocked channels>
Files: videos.csv · channels.csv · results.json
```

## `learn` — Understand a concept

```
# Learning <query> from YouTube
_Top explainers ranked for trust, engagement and format · transcripts read for <k> videos_

## Start here (3 videos)
For each: link, channel [tier/trust], length, why it's first (what it explains well), prerequisite level

## The concept, synthesised from the transcripts
A clean explanation in your own words, 3–6 paragraphs, every non-obvious claim cited (video + timestamp).
Call out where sources define terms differently or contradict each other.

## Learning path
Beginner → intermediate → advanced, 2–4 videos each, one line on what each adds.

## Mental models & analogies worth stealing
Short list, each attributed with a timestamp.

## Open questions / disputed points
What the top sources disagree on or leave unanswered.

## Full ranked list + caveats
<table> · files
```

## `expert` — Plan according to expert content

```
# What experts say about <query>
_Authority-weighted ranking · <k> talks/interviews transcribed_

## Who the experts are
Table: speaker/channel, role or affiliation (from description), tier/trust, videos, why they count.

## Consensus
Numbered recommendations/claims that ≥ 2 independent sources make, each with citations (video + timestamp).

## Disagreements and trade-offs
Where credible sources diverge; the strongest version of each side.

## Frameworks, checklists and numbers quoted
Anything operational: steps, thresholds, benchmarks, rules of thumb — with attribution.

## Implications for <user's plan>
Concrete recommendations mapped back to the evidence above. Flag where the evidence is thin or dated.

## Full ranked list + caveats
<table> · files
```

## `brand` — Perception audit

```
# How <brand> shows up on YouTube
_<n> videos ranked (relevance + recency weighted) · <k> videos' comments sampled (<total> comments) · window <since or 'all time'>_

## Share of voice
Volume (videos, views, channels) in the last 12 months; vs. competitors if --compare was used (share_of_voice.csv).

## Owned vs earned
- Owned/affiliated: the brand's own channel(s) — reach, engagement vs tier
- Earned: third-party coverage split into advocates / neutral explainers / critics, with the 2–3 most-seen videos in each

## Narratives
The 4–8 recurring claims or framings in titles, descriptions and comments — each tagged positive / negative / mixed, with evidence links and the most-liked comment that expresses it.

## Risk flags
Critical or allegation-type videos (title patterns: scam, risk, warning, exposed, honest review…), who made them, reach, and whether the brand responded in comments (uploader replies).

## Opportunities
Creators worth briefing, questions people keep asking (question share from comments), misconceptions a piece of content could fix.

## Method & caveats
Heuristic sentiment counts are pointers, not measurements; which videos' comments were read; videos flagged brand-not-in-metadata; trusted-list coverage.
Files: videos.csv · channels.csv · comments.csv · comments.md · share_of_voice.csv
```

---

## Spreadsheet export (when asked)

Tabs: `Videos` (videos.csv with the score columns), `Channels` (channels.csv), `Comments` (comments.csv, if collected), `Method` (mode, weights, half-life, benchmarks, caveats). Freeze headers, number-format views/likes, conditional colour on `score` and `er_vs_benchmark`. Build with the `xlsx` skill or the Sheets artifact type depending on where the user wants it.

## Claude Doc export (when asked)

Use the mode template above as the outline; tables become doc tables; keep the Coverage & caveats section — it is what makes the doc trustworthy when it is forwarded.
