# kairon.xyz section map (draft for Alejandro's review)

Status: proposal. Read-only review. No site copy changed. Source: repo content files at the time of review (may lag the live deploy; live pages were not rendered). Each "What it's for" line is my reading of the repo's own labels and his essays. He corrects it.

## How the site is built
Every visible string comes from `content/`: `about.md` (home intro), `home.json` (section headings), `settings/site.json` (identity, SEO, footer), `writing.json` (curated links), `theses/*.md`, `projects/*.md`, `blog/*.md`, `pages/about.md`. Edits to these are the only way copy changes. Nothing here is changed by this PR.

## Sections

| Section | What it is for (proposed) | State now | Gap against a buyer reading it |
|---|---|---|---|
| Masthead / wordmark | Who this is, in one glance | "~ Alejandro Arango", tagline "Creative Technologist and Martech Daylighter" | "Daylighter" says a day job, not a practice. Does not say what he does for a client. |
| Hero intro (`about.md`) | The 10-second pitch | 3 lines: "I'm in tech. I care about craftsmanship. I don't like buzzwords." | Voice is his, but a buyer learns nothing about the offer, proof or who it is for. |
| Projects | Proof of work he built himself | 8 repos, ~300-370 words each, 7 link only to GitHub | Buyers vet advisors by "show me one workflow you shipped in your own house". The projects are the best proof asset and read like README summaries. |
| Theses | His worldview, the "why" | 3 theses, 110-135 words each | Thin. They carry his core idea (devices become real through belief; story first, technology second) but do not connect to the work. |
| Media | Appearances, external proof | Heading exists, intro empty | Empty or unclear. Needs his input on what exists. |
| Writing | Essays: voice and thinking | 11 essays, newest 2026-09-20; 17 curated external links, partly Mirror | Strongest voice asset. Not connected to the offer. Intro empty. |
| Newsletter | Owned-audience capture | Generic "when inspiration strikes" blurb, Substack | Weak reason to subscribe. |
| About page (`pages/about.md`) | Who he is and why | 685 words, titled "About Device Economies" | Older brand name (Device Economies); reads as another project. Needs a decision: fold into Kairon, or keep as its own story. |
| Footer | Contact and sign-off | "Made with Love", email, handles | Contact is there. No call to action. |
| Head / SEO | Findable by people and AI answer engines | Title and description from `site.json`; sitemap, robots, llms.txt, structured data not verified | Unverified. See ICP-BRIEF for what buyers' tools look for. |

## Content that must not appear without his explicit OK
- Client names and results from Sky Protocol and River One (client-confidential per earlier notes). Anonymized method write-ups only, and only after his go.
- Anything from the 13 pages in `agent/voice/corpus/excluded/`. They stay excluded.
- Anything from his day job.
- Individuals from the ICP watchlist (it is a watchlist, not an outreach list).

## Upkeep mechanism (proposed, nothing built)
Goal: sections stay in step with what he is actually working on, without us writing his claims for him.
1. A `content/now.json` "Now" block (new section, his approval needed) with 3-5 lines: what he is building, shipping, writing this month. Source for each line: a repo, PR, essay or his own message. No line without a source.
2. A monthly (not weekly) review run by an agent: it reads his repos' recent activity and his latest essays, then opens a PR proposing updates to `now.json`, project descriptions and the writing list. He reviews the exact copy. Nothing is merged or published by the agent.
3. A staleness report in each PR: which sections have not changed in 60+ days, and which projects have no live link.
4. Rules the review must keep: never main, no client-confidential material, no rewriting his essays, placeholders `[ALEJANDRO: ...]` where his take is missing.
Open for him: monthly or other cadence; whether "Now" fits the design.
