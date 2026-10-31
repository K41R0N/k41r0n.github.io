# Orientation — How This Repository Works

Read this once, fully, before contributing. It is the mental model the rest of
`agent/` assumes you have.

## What this repo is

The public source repo for **kairon.xyz**, the Device Economies publication, and its methods harness. The site is built to be agentic-first, dynamically updated, and readable by AEO engines. The site itself is statically generated: Markdown and JSON are compiled by a Node build script into plain HTML in `dist/`.

Current architecture and hosting are documented in [`knowledge/site/repo-architecture.md`](knowledge/site/repo-architecture.md); this orientation is the entry point, not a second deployment source of truth.

| Aspect | Detail |
|---|---|
| Type | Static HTML/CSS/JS — no client framework |
| Build | `node scripts/build.js` (via `npm run build`) |
| CMS | Sveltia CMS (Decap/Netlify-compatible), GitHub backend |
| Hosting | Cloudflare Workers serves the `www` site; Vercel remains the bare-domain redirect and rollback path |
| Content | Markdown + JSON under `content/` |

## The data flow (memorize this)

```
            ┌─────────────────────── source of truth ───────────────────────┐
content/about.md            content/home.json         content/writing.json
content/settings/site.json  content/theses/*.md       content/blog/*.md
content/pages/about.md
            └──────────────────────────────┬─────────────────────────────────┘
                                            │
                                npm run build
                                            │
        prebuild ──► generate-cms-config.js  (admin/config.template.yml → admin/config.yml)
        prebuild ──► validate-content.js     (fails the build on bad content)
        build    ──► build.js                (renders everything)
                                            │
                                            ▼
                                          dist/
        index.html · thesis-NN-*.html · blog/*.html · about.html
        llms.txt · llms-full.txt · api/content.json
        sitemap.xml · feed.xml · robots.txt · css/ · assets/ · admin/
                                            │
                                       Cloudflare Workers serves dist/
```

Two facts follow from this diagram and they are the heart of everything:

1. **`dist/` is disposable.** It is deleted and regenerated on every build
   (`fs.rmSync(DIST, …)` at the top of `main()` in `build.js`). Editing it is
   pointless and actively misleading — your change vanishes on the next build.
2. **`admin/config.yml` is disposable.** It is regenerated from
   `admin/config.template.yml` on every build. Edit the **template**, never the
   output.

## The two ways content reaches the site

There are two write lanes into this repo. Know which one you are in.

- **CMS lane (Sveltia, `/admin`).** A human (Alejandro) edits content in a
  browser. Sveltia commits directly to `main` via the GitHub backend, which
  triggers a Cloudflare Workers Build. The CMS only knows about files declared in
  `admin/config.template.yml`. If a content file or frontmatter field is not in
  that schema, the CMS cannot see it — and **on the next CMS save of that file,
  any field missing from the schema is silently stripped.** This is the single
  most important CMS invariant. See `knowledge/site/cms-safety.md`.

- **Git lane (you, an agent).** You edit files and commit. For *content* this is
  low-risk. For *code, schema, or config* it is higher-risk and goes through a
  pull request — never a direct push to `main`, because `main` auto-deploys. See
  `knowledge/site/contribution-workflow.md`.

## What renders from what

The authoritative field-by-field map lives in repo-root
`CONTENT_ARCHITECTURE.md`. The short version:

| File | Drives |
|---|---|
| `content/settings/site.json` | Identity, social, SEO, footer, thesis-page labels — appears on **every** page |
| `content/about.md` | Hero intro copy on the home page (body only, **no frontmatter**) |
| `content/home.json` | Home section headings, sub-labels, newsletter copy, logo |
| `content/writing.json` | Curated "Writing" links on the home page |
| `content/theses/*.md` | Home TOC rows + each `thesis-NN-slug.html` detail page |
| `content/blog/*.md` | `/blog/` listing + each `/blog/slug.html` + the RSS feed |
| `content/pages/about.md` | The `/about.html` publication page |

## Why an agent can break things here

Three failure modes, all preventable:

1. **Editing generated output** (`dist/`, `admin/config.yml`) — wasted work,
   confusion, and divergence from source.
2. **Breaking the CMS schema** — touching `admin/config.template.yml` carelessly
   makes the `/admin` editor unusable for Alejandro, or causes silent content
   loss on the next save.
3. **Breaking the build** — the build *fails closed*: `validate-content.js` runs
   in `prebuild` and exits non-zero on malformed content, so a bad frontmatter
   field or duplicate slug stops the deploy. Always run `npm run build` before
   you ship.

The rest of `agent/` exists to keep you out of all three.

## Methodology lookup

For working preferences and repeatable methods, use the routed guides in
[`README.md`](README.md#routing-table): `knowledge/methodologies/operator-profile.md`
for defaults and limits; `research-method.md` for evidence-led research;
`feedback-and-review.md` for correction and review; `iteration-protocol.md`
for revision and verification; and `briefing-and-work-planning.md` for briefs
and plans. These are inferred procedural syntheses, not owner-approved universal
rules; each file names its source basis and limits. Consult its cited source
when a disputed detail or higher-stakes application depends on it.

## Next

- For the rules on what you may touch: `routines/protocols/PORTFOLIO-WRITE-GUARD-01.md`
- For a concrete task: pick the matching file in `skills/`
- For deeper reference: `knowledge/site/`
