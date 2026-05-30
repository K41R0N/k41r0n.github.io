# Content Architecture — Kairon Portfolio

Defines the content model. Front-end agnostic — any presentation layer can consume this content.

## Design Principles

1. **Semantic naming** — field names describe WHAT, not WHERE
2. **Content completeness** — content is meaningful without a presentation layer
3. **Single source of truth** — `content/` is the only source; `dist/` is derived
4. **Flat hierarchy** — no nested collections needed
5. **Progressive enhancement** — minimal required fields; optional fields add richness

---

## Content Types

### 1. Site Settings

Global metadata. One file: `content/settings/site.json`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | yes | Short site name (e.g., "Kairon") |
| `full_name` | string | yes | Full legal name |
| `tagline` | string | yes | One-line title |
| `description` | text | yes | SEO meta description |
| `author` | string | yes | Name for JSON-LD |
| `author_handle` | string | yes | GitHub handle / alias |
| `email` | string | yes | Contact email |
| `github` | string | yes | GitHub profile URL |
| `substack` | string | yes | Substack URL |
| `instagram` | string | no | Instagram URL |
| `site_url` | string | yes | Production URL |
| `footer_text` | string | no | Footer tagline |
| `substack_embed` | string | no | Substack embed iframe URL |

### 2. Thesis

A thought-leadership card. Files: `content/theses/{slug}.md`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | yes | Thesis statement / headline |
| `slug` | string | yes | URL-safe anchor ID |
| `order` | integer | yes | Display order (1, 2, 3…) |
| `description` | text | yes | One-sentence summary (SEO + card subtitle) |
| `body` | markdown | no | Expanded body text |
| `links` | list | no | Supporting articles / tools / podcasts |

#### Link Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `label` | string | yes | Type tag: Article, Tool, Podcast… |
| `title` | string | yes | Display title |
| `url` | string | yes | Full URL |

---

## File Structure

```
content/
├── settings/
│   └── site.json         # Global metadata
├── about.md              # Hero copy
└── theses/
    ├── devices-as-co-creations.md
    ├── future-belongs-to-storytellers.md
    └── better-discovery-engines.md

admin/
├── index.html            # Sveltia CMS entry point
└── config.template.yml   # CMS schema template (→ config.yml at build)

scripts/
├── build.js              # Main build
└── generate-cms-config.js

src/
└── css/
    ├── tokens.css
    ├── fonts.css
    ├── base.css
    ├── layout.css
    └── components.css
```

---

## Machine-Readable Endpoints

| Endpoint | Format | Description |
|----------|--------|-------------|
| `/llms.txt` | Text | AI agent guidance (llmstxt.org) |
| `/llms-full.txt` | Text | Full content dump |
| `/api/content.json` | JSON | All theses + metadata, CORS-enabled |
| `/sitemap.xml` | XML | Search engine sitemap |
| `/feed.xml` | RSS 2.0 | Syndication feed |
| `/robots.txt` | Text | Crawler guidance with AI bot allowances |

### JSON API Response (`/api/content.json`)

```json
{
  "$schema": "https://k41r0n.github.io/api/schema.json",
  "version": "1.0",
  "generated": "2026-05-31T00:00:00.000Z",
  "site": {
    "name": "Kairon",
    "url": "https://k41r0n.github.io",
    "description": "...",
    "author": { "name": "...", "email": "...", "github": "..." }
  },
  "theses": [
    {
      "title": "Devices as Co-Creations",
      "slug": "devices-as-co-creations",
      "order": 1,
      "description": "...",
      "links": [...]
    }
  ]
}
```

---

## Adding a New Thesis

1. Create `content/theses/{slug}.md` with required frontmatter
2. Run `npm run build`
3. Verify it appears in `dist/index.html` and `dist/api/content.json`

## Adding a New Field

1. Document it in this file
2. Add to `admin/config.template.yml` (mark `required: false` for existing content safety)
3. Update `scripts/build.js` to read and render the new field
4. Run `npm run build` to verify

---

## Versioning

- **Schema Version:** 1.0
- **Last Updated:** 2026-05-31
