# Content Architecture — Kairon Portfolio

Source of truth is `content/`. Build script (`scripts/build.js`) generates `dist/`.
Every visible string on the site traces back to one of three content files.

---

## Content Files

```
content/
├── about.md                        → hero intro copy (body only, no frontmatter)
├── settings/
│   └── site.json                   → all site-wide copy and config
└── theses/
    ├── devices-as-co-creations.md
    ├── future-belongs-to-storytellers.md
    └── better-discovery-engines.md
```

---

## Complete Content Map

### `index.html` (home page)

| Section | Element | Content file | Field |
|---------|---------|--------------|-------|
| Masthead | Wordmark line 1 | `settings/site.json` | `wordmark_line1` |
| Masthead | Wordmark line 2 | `settings/site.json` | `wordmark_line2` |
| Masthead metrics | Instagram URL + handle | `settings/site.json` | `instagram` |
| Masthead metrics | GitHub URL + handle | `settings/site.json` | `github` + `author_handle` |
| Masthead metrics | Substack URL | `settings/site.json` | `substack` |
| Hero intro | Body copy | `about.md` | body (no frontmatter) |
| Theses index | Section heading | `settings/site.json` | `section_theses` |
| Theses index | Each entry title | `theses/*.md` | `title` |
| Theses index | Each entry description | `theses/*.md` | `description` |
| Writing | Section heading | `settings/site.json` | `section_writing` |
| Writing | All links (auto-aggregated) | `theses/*.md` | `links[]` |
| Newsletter | Section heading | `settings/site.json` | `section_newsletter` |
| Newsletter | Body paragraph | `settings/site.json` | `newsletter_body` |
| Newsletter | CTA link text | `settings/site.json` | `newsletter_cta` |
| Newsletter | Subscribe URL | `settings/site.json` | `substack` |
| Footer | Tagline | `settings/site.json` | `tagline` |
| Footer | Email | `settings/site.json` | `email` |
| Footer | Copyright name | `settings/site.json` | `full_name` |
| `<head>` | Browser tab title | `settings/site.json` | `title` |
| `<head>` | Meta description | `settings/site.json` | `description` |

### `thesis-NN-{slug}.html` (each thesis detail page)

| Section | Element | Content file | Field |
|---------|---------|--------------|-------|
| Nav | ← back link text | `settings/site.json` | `title` |
| Nav | "Thesis NN / Title" | `theses/*.md` | `order` + `title` |
| Chapter nav | All thesis nav links | `theses/*.md` | `title` × N |
| Article | Thesis h1 | `theses/*.md` | `title` |
| Article | Article body | `theses/*.md` | body (markdown) |
| Article | Links block | `theses/*.md` | `links[]` |
| `<head>` | Meta description | `theses/*.md` | `description` |
| Footer | Handle | `settings/site.json` | `author_handle` |
| Footer | Copyright name | `settings/site.json` | `full_name` |

> **Note:** `description` in a thesis file is SEO-only. It appears as the dot-leader
> description in the home page TOC and as `<meta name="description">` on the detail
> page. It is NOT rendered as visible body text on the detail page — only `body` is.

---

## CMS Collections → Pages

The CMS has three collections. Here is which pages each one controls:

| CMS Collection | Controls |
|---------------|---------|
| **Home Page** → Hero · About | Hero intro text on `index.html` |
| **Theses** | Every thesis row in the home TOC + every `thesis-NN-*.html` detail page |
| **Settings** → Site Settings | Every page — masthead, nav, footer, section headings, newsletter, SEO |

---

## Thesis Frontmatter Schema

```yaml
---
title: string       # required — display title
slug: string        # required — kebab-case URL identifier
order: integer      # required — 1-based, controls TOC order and URL prefix
description: string # required — one sentence, TOC text + SEO meta only
links:              # optional
  - label: string   # Article | Tool | Podcast | Project | Video | Curated Compilation
    title: string
    url: string
---

Markdown body here — rendered as article content on the detail page.
Supports:
  > **Note:** text   →  margin note aside
  ---                →  section break rule
```

---

## `about.md` Format

No frontmatter — plain markdown body only. The entire file content is rendered
as the hero intro text on the home page.

```markdown
I'm in tech.
I care about craftsmanship.
I don't like buzzwords.
```

Do not add frontmatter to this file — the CMS Home Page collection only
maps to the body, and any frontmatter would be stripped on the next CMS save.

---

## `site.json` Fields

```
Identity:    full_name, wordmark_line1, wordmark_line2, author_handle, tagline, email
Social:      github, substack, instagram
SEO:         title, description, site_url
Headings:    section_theses, section_writing, section_newsletter
Newsletter:  newsletter_body, newsletter_cta
Footer:      footer_text, substack_embed
```

---

## Machine-Readable Endpoints

Every build also outputs:

| File | Purpose |
|------|---------|
| `/llms.txt` | AI agent guidance (llmstxt.org standard) |
| `/llms-full.txt` | Complete content dump |
| `/api/content.json` | All theses with metadata, CORS-enabled |
| `/sitemap.xml` | Search engine sitemap (home + all thesis pages) |
| `/feed.xml` | RSS 2.0 |
| `/robots.txt` | AI crawler allowances |

---

## Adding a New Thesis

1. Create `content/theses/{slug}.md` with required frontmatter
2. Run `npm run build`
3. Verify it appears in `dist/index.html` TOC and `dist/thesis-NN-{slug}.html`
4. Verify it appears in `dist/api/content.json`

Or use the CMS: **Theses** → **New** → fill in all fields → Save → Vercel rebuilds automatically.

---

## Adding a New Configurable Field

1. Add the field to `content/settings/site.json` with a sensible default
2. Add a corresponding entry to `admin/config.template.yml` under the Settings collection
3. Update `scripts/build.js` to read the new field (with a fallback)
4. Run `npm run build`
5. Document it in this file under the appropriate section
