# Setup & environments

## 1. Claude Code (laptop / desktop) — the reliable path

```bash
pip install -U yt-dlp                 # the only hard dependency (Python 3.10+)
# optional but recommended: a JS runtime helps yt-dlp with YouTube's challenges
#   macOS: brew install deno      Linux: curl -fsSL https://deno.land/install.sh | sh
python3 scripts/yt_research.py doctor # confirms yt-dlp, network, cookies, API key
```

Install the skill by unpacking the `.skill` package (it is a zip) into `~/.claude/skills/youtube-research/`, or by cloning the repo you push it to. Claude Code picks it up on the next session.

First run: `python3 scripts/yt_research.py run "your query" --mode topic`. Runs land in `./youtube-research-runs/<timestamp>-<mode>-<slug>/` (override with `--out` or `YT_RESEARCH_RUNS`).

**Bot checks.** YouTube sometimes answers "Sign in to confirm you're not a bot", especially after bursts or from VPNs. Fixes, in order: `pip install -U yt-dlp` (counter-fixes ship weekly); add `--cookies-from-browser chrome` (or firefox/edge/brave — uses your logged-in session, read-only); lower `--workers 2 --sleep 1.5`; wait an hour. Metadata-only extraction is challenged far less than downloading, and nothing here downloads media.

## 2. Cowork / claude.ai — what works today and what to ask for

The cloud sandbox is subject to the client product's network policy. On 2026-10-02 both `www.youtube.com` and `www.googleapis.com` were **blocked** (HTTP 403 from the egress proxy), so collection cannot run there yet. Analysis of an uploaded run folder works everywhere (`rescore`, reading transcripts/comments, writing the report) because it needs no network.

Ask an Organization owner to add domains under **Organization settings → Capabilities → network access** (the "package managers + specific domains" level). Request text:

> Could you add these domains to Claude's network allowlist? They let our YouTube research skill collect public video metadata from inside Cowork/claude.ai instead of only from a laptop.
> - `www.youtube.com` (yt-dlp metadata, captions, comments)
> - `www.googleapis.com` and `youtube.googleapis.com` (official YouTube Data API v3 — only used if we add a free API key)
> No media is downloaded; only public titles, statistics, captions and comments are read.

Caveat even after whitelisting: the sandbox's egress IP is a datacenter IP, which YouTube challenges more often. If `doctor` reports a bot check there, the two clean fallbacks are (a) add a free API key — the official API never bot-checks — or (b) collect locally and upload the run folder.

## 3. Optional accelerator: YouTube Data API v3 key (free)

Not required. If present, `--provider auto` uses it for search, video and channel statistics and comments (transcripts still come from yt-dlp). Quota as of Oct 2026: **100 `search.list` calls/day** (50 results each) plus **10,000 units/day** for everything else (video/channel/comment calls cost 1 unit per batch). A typical run uses 5–7 search calls, so ~15 runs/day.

1. console.cloud.google.com → new project → APIs & Services → Enable "YouTube Data API v3".
2. Credentials → Create credentials → API key → restrict it to the YouTube Data API.
3. `export YOUTUBE_API_KEY=...` (shell profile, or Claude Code's env). Never commit it.

## 4. Trusted-channel lists

Seed list: `references/trusted-channels.json` (ships with the skill). Your own additions go in `~/.config/youtube-research/trusted-channels.json` — same shape, merged on top, survives skill updates. Set `YT_RESEARCH_TRUSTED` to point somewhere else (e.g. a shared repo path). Each `report.md` lists which entries matched, so a handle that never matches is easy to spot and fix.

## 5. Keeping the scripts in one place (recommended)

Push the skill folder to a private GitHub repo. The sandbox can read `raw.githubusercontent.com`, so a Cowork session that has the SKILL.md but not the scripts can fetch them:

```bash
mkdir -p scripts references && cd scripts
curl -fsSLO https://raw.githubusercontent.com/<org>/<repo>/main/scripts/yt_research.py
curl -fsSL -o ../references/trusted-channels.json https://raw.githubusercontent.com/<org>/<repo>/main/references/trusted-channels.json
```

Record the repo URL in SKILL.md under "Where the scripts live" once it exists.

## 6. Moving a run between surfaces

A run folder is self-contained. Zip it (`zip -r run.zip youtube-research-runs/<run>`), upload it to the Cowork/claude.ai chat, and ask for the analysis; `rescore` and the write-up need nothing from the network. Transcripts and comments must be collected where YouTube is reachable.
