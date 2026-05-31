# Guideline — Content Schemas Reference

Exact shapes for every editable content file. The build (`build.js`) and the
validator (`validate-content.js`) both depend on these. When in doubt, copy an
existing file and change the values.

---

## `content/settings/site.json`

Global config — appears on every page. Plain JSON object.

**Validator-required keys (build fails if any are missing):**
`title`, `full_name`, `description`, `author`, `email`, `github`, `substack`,
`site_url`.

**Full current key set:**

| Key | Purpose |
|---|---|
| `full_name` | Legal name — copyright, JSON-LD |
| `author` | Required by validator; used in schema/credits |
| `wordmark_line1`, `wordmark_line2` | Two-line display name in the masthead |
| `author_handle` | Alias (e.g. `K41R0N`) — section labels, nav, GitHub metric |
| `tagline` | One-line role — footer + hero fallback |
| `email` | Contact — masthead + footer |
| `github`, `substack`, `instagram` | Social URLs (full `https://…`) |
| `title` | Short site name — browser tab, RSS, `←` nav |
| `description` | SEO meta description |
| `site_url` | Production URL with protocol |
| `thesis_nav_label`, `thesis_links_heading`, `thesis_links_label`, `thesis_next_label` | Thesis-page labels |
| `footer_text`, `substack_embed` | Footer + optional embed |

Rule: edit values freely; keep every required key. Strings rendered into HTML are
escaped by the build, so apostrophes/ampersands are safe.

---

## `content/theses/*.md`

One file per thesis. Drives a home-page TOC row **and** a detail page at
`thesis-NN-<slug>.html` (NN = zero-padded `order`).

```markdown
---
title: "Devices as Co-Creations"      # required — h1 + TOC heading + nav
slug: "devices-as-co-creations"       # required — ^[a-z0-9-]+$, unique
order: 1                               # required — int ≥ 1, unique, sets URL prefix
description: "One sentence."           # required — TOC text + SEO meta ONLY
links:                                 # optional
  - label: "Article"                   # one of: Article, Tool, Podcast,
    title: "Display Title"             #         Project, Video, Curated Compilation
    url: "https://…"
---

Markdown body — rendered as the article. `description` does NOT appear here;
only the body does. Supports `> **Note:**` margin notes and `---` section breaks.
```

Validator enforces: all four required fields present, `slug` matches the regex,
`slug` and `order` unique across the folder.

---

## `content/blog/*.md`

One file per post. Filename convention (CMS): `YYYY-MM-DD-<slug>.md`. Drives the
`/blog/` listing, `/blog/<slug>.html`, and an entry in `/feed.xml`.

```markdown
---
title: "Post Headline"                 # required
slug: "post-slug"                      # required — ^[a-z0-9-]+$ ; sets /blog/<slug>.html
date: "2025-06-04"                     # required — YYYY-MM-DD ; ordering + RSS pubDate
description: "One-sentence summary."    # required — listing, RSS, SEO, llms.txt
cover_image: "/assets/images/x.svg"    # optional — square image; hero + listing
tags:                                  # optional — list of strings; first tag = eyebrow
  - "essay"
---

Markdown body. Same transforms as theses (margin notes, section breaks, dropcap).
Substack-exported images are auto-downsized and lazy-loaded.
```

Notes:
- The **`slug` frontmatter field** (not the filename) determines the URL.
- Posts sort newest-first by `date`.
- Theses are *not* in the RSS feed; only blog posts are.

---

## `content/home.json`

Home-page section headings, sub-labels, newsletter copy, logo. Object with keys
matching the Home · Sections collection: `logo_image`, `logo_alt`,
`section_theses`, `section_theses_label`, `section_writing`,
`section_writing_label`, `section_writing_intro`, `blog_intro`,
`section_newsletter`, `section_newsletter_label`, `newsletter_body`,
`newsletter_cta`. Every key has a build-side fallback, so missing keys degrade
gracefully — but to expose a key in the CMS it must be in the schema.

---

## `content/writing.json`

Curated home-page "Writing" links, independent of thesis links.

```json
{
  "links": [
    { "label": "Article", "title": "Display Title", "url": "https://…" }
  ]
}
```

`label` is one of the same six types as thesis links.

---

## `content/about.md` and `content/pages/about.md`

- `content/about.md` — **no frontmatter.** Body Markdown only → home hero intro.
- `content/pages/about.md` — has frontmatter (`title`, `description`) + body →
  the `/about.html` publication page.

Do not confuse the two. The home hero is `content/about.md`; the standalone
About page is `content/pages/about.md`.

---

## Adding a field that doesn't exist yet

If your task needs a *new* configurable value, you cannot just add a JSON key and
expect it on the site — `build.js` has to read it and (for editability) the CMS
schema has to expose it. That is the four-step procedure in
`skills/add-configurable-field.md`, and it touches Tier 1 paths.
