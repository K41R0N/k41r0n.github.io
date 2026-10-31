# Guideline — Repository Architecture

This is the current architecture and hosting source of truth for the site and attached methods harness. The field-by-field content map remains in repo-root `CONTENT_ARCHITECTURE.md`; it does not own deployment state. Live production state is the Cloudflare Workers configuration and current deployment record. Vercel is retained as a rollback path / bare-domain redirect, not the current `www` host.

## Layout

```
k41r0n.github.io/
├── content/                 ← SOURCE OF TRUTH (edit here)
│   ├── about.md             home hero copy (BODY ONLY, no frontmatter)
│   ├── home.json            home section headings, labels, newsletter, logo
│   ├── writing.json         curated "Writing" links on the home page
│   ├── settings/site.json   global identity / social / SEO / footer / labels
│   ├── theses/*.md          theses → home TOC + thesis-NN-slug.html
│   ├── blog/*.md            blog posts → /blog/ listing + /blog/slug.html + RSS
│   └── pages/about.md       the /about.html publication page
├── admin/
│   ├── config.template.yml  CMS SCHEMA (source — Tier 1, propose before editing)
│   ├── config.yml           GENERATED — never hand-edit
│   └── index.html           CMS entry point (Tier 1)
├── scripts/
│   ├── build.js             the renderer (Tier 1)
│   ├── generate-cms-config.js  template → config.yml (Tier 1)
│   └── validate-content.js  content gate, runs in prebuild (Tier 1)
├── src/
│   ├── css/                 tokens.css (token contract), layout/components/etc.
│   └── assets/              fonts, images
├── dist/                    GENERATED build output — never hand-edit
├── docs/                    plans + documented solutions
├── agent/                   ← you are here
├── package.json             scripts + deps (Tier 1)
├── wrangler.jsonc           Cloudflare Workers config (Tier 1)
├── vercel.json              legacy / rollback and bare-domain redirect config (Tier 1)
└── server.py                local dev server (Tier 1)
```

## The build pipeline, precisely

`npm run build` runs three stages (see `package.json`):

1. **`prebuild` → `generate-cms-config.js`** — reads `admin/config.template.yml`,
   substitutes `${VAR}` placeholders from environment variables, writes
   `admin/config.yml`. If the template is missing it exits silently.
2. **`prebuild` → `validate-content.js`** — validates `site.json` required fields
   and every thesis's frontmatter (required fields, slug regex, unique slug &
   order). **Exits non-zero on any failure, which stops the build and the
   deploy.** This is your safety net — never bypass it.
3. **`build` → `build.js`** — deletes `dist/`, reloads all content, renders:
   - `index.html` (home)
   - `thesis-NN-<slug>.html` for each thesis
   - `blog/index.html` + `blog/<slug>.html` for each post (+ tag pages)
   - `about.html`
   - `llms.txt`, `llms-full.txt`, `api/content.json`
   - `sitemap.xml`, `feed.xml`, `robots.txt`
   - copies `css/`, `assets/`, `admin/`

## Rendering rules worth knowing

These are implemented in `build.js` and affect how your Markdown renders:

- **Margin notes:** a blockquote line `> **Note:** …` (any blockquote, single or
  multi-line) becomes `<aside class="margin-note">` in the right margin.
- **Section break:** a line containing only `---` becomes
  `<hr class="section-break">`.
- **Drop cap:** the first paragraph gets a drop cap *only if* it opens with 3+
  consecutive letters (guards against "I'm" / "A " being mangled).
- **Substack image downsizing:** body `<img>` URLs with `w_1456,c_limit` are
  rewritten to `w_800,c_limit`, and `loading="lazy"` is added — relevant when
  importing Substack content.

## Machine-readable endpoints (already agent-friendly)

The build emits endpoints designed for agents to *read* the site:

| Endpoint | Use |
|---|---|
| `/api/content.json` | Structured JSON: site, theses, posts. CORS-enabled. Best for programmatic reads. |
| `/llms.txt`, `/llms-full.txt` | Human/agent-readable content dumps. |
| `/feed.xml` | RSS 2.0 of blog posts (theses excluded) — the syndication bridge. |
| `/sitemap.xml`, `/robots.txt` | SEO + AI-crawler allowances. |

When you build automation that *reads* published state, prefer
`/api/content.json` over scraping HTML. See
`harness/specs/live-components-foundations.md`.

## Deploy and rollback

Cloudflare Workers serves the `www` site. Workers Builds watches `main`; a push triggers the configured build and deployment. `wrangler.jsonc` is the current Worker configuration; `src/worker.js` serves the generated `dist/` assets and handles the analytics ingest route. The current deployment record is [`agent/decisions/2026-10-30-methodology-advice-and-site-infra.md`](../../decisions/2026-10-30-methodology-advice-and-site-infra.md).

Vercel remains for the bare-domain redirect and as the rollback path. `vercel.json` documents that legacy/fallback configuration; do not describe it as the current `www` host. See also the historical CMS decision [`docs/solutions/best-practices/ghost-cms-rejected-2026-05-31.md`](../../../docs/solutions/best-practices/ghost-cms-rejected-2026-05-31.md), which records the earlier Sveltia + Vercel state.
