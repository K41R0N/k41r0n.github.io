# Orientation — How This Repository Works

Read this once, fully, before contributing. It is the mental model the rest of
`agent/` assumes you have.

## What this repo is

The source for **kairon.xyz** — Alejandro (Kairon) Arango Giraldo's personal
portfolio and the **Device Economies** publication. It is a static site with no
runtime framework: Markdown and JSON files are compiled by a Node build script
into plain HTML in `dist/`, which Vercel serves.

| Aspect | Detail |
|---|---|
| Type | Static HTML/CSS/JS — no client framework |
| Build | `node scripts/build.js` (via `npm run build`) |
| CMS | Sveltia CMS (Decap/Netlify-compatible), GitHub backend |
| Hosting | Vercel — auto-deploys on push to `main` |
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
                                       Vercel serves dist/
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
  triggers a Vercel rebuild. The CMS only knows about files declared in
  `admin/config.template.yml`. If a content file or frontmatter field is not in
  that schema, the CMS cannot see it — and **on the next CMS save of that file,
  any field missing from the schema is silently stripped.** This is the single
  most important CMS invariant. See `guidelines/cms-safety.md`.

- **Git lane (you, an agent).** You edit files and commit. For *content* this is
  low-risk. For *code, schema, or config* it is higher-risk and goes through a
  pull request — never a direct push to `main`, because `main` auto-deploys. See
  `guidelines/contribution-workflow.md`.

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

## Next

- For the rules on what you may touch: `protocols/PORTFOLIO-WRITE-GUARD-01.md`
- For a concrete task: pick the matching file in `skills/`
- For deeper reference: `guidelines/`
