---
name: "youtube-research"
description: Research any topic, concept, brand or product on YouTube at scale — find the top 10–50 videos for a query ranked by channel trust and tier-normalised engagement instead of raw view counts, pull transcripts and comments, and write up a topic landscape, a learning synthesis, an expert-consensus brief or a brand-perception audit. Use this whenever the user mentions YouTube videos, creators, channels, "what's on YouTube about…", video research, "best videos to learn X", "what do experts say about X" (video sources), or wants to know how a brand/product/protocol is perceived or talked about on YouTube — even if they don't say "YouTube" but ask about video coverage, creator sentiment or share of voice in video. Also use it to re-analyse a previously collected run folder.
---

# YouTube research

Rank YouTube videos for a query by **who is talking** (channel authority + curated trust lists) and **how viewers responded relative to channel size** (tier-normalised engagement), with relevance, recency and format fit — then read the winners (transcripts, comments) and write the analysis. The data engine is `yt-dlp` (no API key); the official YouTube Data API is used automatically only if `YOUTUBE_API_KEY` is set.

Read `references/scoring.md` when you need to explain or defend a ranking; `references/output-templates.md` before writing any deliverable; `references/setup.md` when something is blocked or missing.

## 1. Pick the mode (ask one question only if truly ambiguous)

| User intent | Mode | What it optimises for |
|---|---|---|
| "What's out there on X", landscape, who covers it, angles, trends | `topic` | breadth, channel map, angle clusters |
| "Help me understand X", best explainers, learn | `learn` | trusted explainers, evergreen, 6–45 min, transcripts |
| "What do experts recommend / plan based on expert content" | `expert` | authority-heavy, long-form talks & interviews, transcripts |
| "How is <brand/product> perceived", audit, sentiment, share of voice | `brand` | relevance + recency, critics included, comments, owned vs earned |

Defaults per mode (override when the user asks for more/less):

```bash
S=scripts/yt_research.py   # path relative to this skill folder
python3 $S run "<query>" --mode topic  --n 30
python3 $S run "<query>" --mode learn  --n 20 --transcripts 8
python3 $S run "<query>" --mode expert --n 25 --transcripts 10 --max-minutes 240
python3 $S run "<query>" --mode brand  --n 40 --comments 15 --since <12 months ago> --owned "@BrandHandle" [--compare "Competitor A" "Competitor B"]
```

Useful knobs: `--n 10..50` (size of ranked list), `--domain crypto_defi finance_markets tech_ai marketing_comms` (which trusted lists apply; default all), `--variants "{q} governance" "{q} risks"` (extra search phrasings), `--require "sample-token|the client protocol|makerdao"` (case-insensitive regex that must appear in title/description/tags/channel — essential for ambiguous brand words like the client, a service agent, a client), `--since YYYY-MM-DD`, `--include-shorts`, `--max-per-channel 3`, `--lang en`, `--no-channel-enrich` (faster, less authority signal), `--out <dir>`.

Choose the query like a researcher: nouns the way creators would title them ("sample-token stablecoin", not "the the client sample-token token thing"). For brands, use the name people actually say; add `--variants` for aliases ("the client Protocol", "a competitor") because the brand phrase must appear in title/description to count as relevant, and `--require` when the brand word has unrelated meanings. `--require` can also be applied or cleared (`--require ""`) at `rescore` time.

## 2. Check where you are running (30 seconds, saves a failed run)

```bash
python3 scripts/yt_research.py doctor
```

- **All reachable** → run the collection here.
- **YouTube blocked / bot check** (typical in the Cowork or claude.ai sandbox) → do not retry in a loop. Tell the user plainly, give them the exact `run` command to execute in Claude Code on their machine, and offer to analyse the run folder once they upload it (`rescore` and all write-ups work offline). `references/setup.md` has the admin whitelist request if they want this to work in the sandbox later.
- **Scripts missing next to this SKILL.md** → ask the user for the `.skill` package or the repo URL (see setup.md §5); do not reimplement the pipeline ad hoc — the scoring must stay consistent across runs.

Exit code 3 means a block was detected mid-run; whatever was collected is already saved in the run folder, so score what exists and say what is missing.

## 3. Run, then read the right files

A run folder (`./youtube-research-runs/<timestamp>-<mode>-<slug>/`) contains:

| File | Read it when |
|---|---|
| `report.md` | always — ranked table, channel landscape, data-quality caveats, remaining candidates |
| `results.json` | you need components (R/A/E/V/T/F), flags, hits, engagement vs benchmark per video |
| `videos.csv`, `channels.csv` | the user wants a spreadsheet, or you are building one |
| `transcripts/<id>.txt` | learn/expert modes — timestamped ~30 s blocks; quote with `(mm:ss)` |
| `comments.md`, `comments_summary.json`, `comments/<id>.json` | brand mode — top-liked comments, heuristic tallies, uploader replies |
| `share_of_voice.csv` | brand mode with `--compare` |
| `run.json` | re-scoring with another mode or weights: `python3 $S rescore <dir> --mode expert` |

Collection takes roughly 1–3 minutes for 90 candidates plus 30 channels; transcripts add ~2 s each, comments ~3 s per video. Run long jobs in the background and keep the user posted.

Read the ranked table *and* the flags before drawing conclusions. The flags carry the judgement calls the user asked for:

- `trusted:A|B:<domain>` / `blocked` — curated lists matched; `institutional-pattern` — name looks like a university/foundation/conference
- `shill-pattern` — authority halved because channel name or recent titles use hype patterns
- `likes-hidden`, `low-sample`, `subs-unknown` — engagement or authority defaulted to neutral
- `brand-not-in-metadata` — the brand is not in title/description; may still be spoken about → transcript
- `official-or-affiliated` — owned media in brand mode; `shorts`, `live` — format

## 4. Write the deliverable

Follow the mode template in `references/output-templates.md`. The parts that make these write-ups worth trusting:

- **Cite every claim** with the video link; transcript quotes get timestamps. The user is building strategy and client-facing material on this — an unsourced "experts agree" is worthless to them.
- **Numbers first, interpretation second**, visibly separated. Say how many candidates were searched, how many enriched, which stages were skipped or blocked, how many trusted entries matched.
- **Trust is explicit**: label tiers, owned vs earned, shill and blocked flags. If no trusted-list entry matched, say so — it usually means the lists need handles for this domain.
- **Comment sentiment is read, not counted.** The lexicon tally in `comments.md` is a pointer. Read the top-liked and a random handful per video before characterising reception, and quote the comments that carry each narrative.
- **Default delivery** is the write-up in chat plus the run folder's CSV/JSON. Build a Claude Doc, a Google Sheet / Excel workbook or an HTML dashboard only when asked. For a workbook, the tab layout is in the templates file.
- Anything headed into external communications still goes through the client's normal review gates (for the client: the client a source document + a legal reviewer guidelines). Say so once when relevant.

## 5. Maintain the trust layer as you go

When the user says "we trust X" / "never show Y" / "that channel is a shill", edit `~/.config/youtube-research/trusted-channels.json` (create it from the seed's shape if absent) — handle, name, one-line `why`. Then `rescore` the current run so the change is visible immediately. The seed list in `references/` is a starting point for crypto/DeFi, finance, tech/AI and marketing; the report's "trusted matched" line tells you whether handles are right.

Score disagreements are information: if a video the user considers excellent ranks low, look at its components — usually relevance (title phrasing) or a hidden like count — and say which, rather than hand-waving. Adjust `--variants`, `--domain` or the lists; do not edit weights per run, or results stop being comparable.

## 6. Where the scripts live

`scripts/yt_research.py` next to this file (single file; depends only on `yt-dlp`). Seed lists in `references/trusted-channels.json`. If the skill was installed as SKILL.md only, fetch the scripts from the `youtube-research.skill` package (it is a zip) or the repo recorded here: `<add repo URL once pushed>`.
