# Agent Instructions — Kairon Portfolio

Instructions for AI agents working on this project. Read before making any changes.

## Project Overview

Personal portfolio for **Alejandro (Kairon) Arango Giraldo** — Creative Technologist and Martech Daylighter.

| Aspect | Details |
|--------|---------|
| Type | Static HTML/CSS/JS portfolio site |
| CMS | Sveltia CMS (Decap/Netlify CMS compatible) |
| Hosting | Vercel (repo: `K41R0N/k41r0n.github.io`) |
| CMS Auth | Cloudflare Worker — `https://sveltia-cms-auth.alejandro-057.workers.dev/` |
| Content | Markdown files + JSON settings |
| Design | Adapted from editorial layout (kairon.xyz grammar) |
| Palette | Warm off-white `#F5F5F5` · black ink · crimson `#bf150f` accent |

### Key Architecture Principle

**Content is the source of truth.** Edit `content/` files — run `npm run build` — done.

```
content/settings/site.json    ──▶ scripts/build.js ──▶ dist/index.html
content/theses/*.md           ──▶ scripts/build.js ──▶ dist/ (SEO + LLM endpoints)
```

---

## Content Structure

| File | Purpose |
|------|---------|
| `content/settings/site.json` | All site metadata (name, email, links, tagline) |
| `content/about.md` | Hero section copy |
| `content/theses/*.md` | Thesis cards (title, description, links) |

### Thesis Frontmatter Schema

```yaml
---
title: "Thesis Title"
slug: "thesis-slug"           # kebab-case, used as HTML anchor ID
order: 1                       # display order
description: "One sentence."  # used in SEO, llms.txt, card subtitle
links:                        # optional list of supporting links
  - label: "Article"
    title: "Display Title"
    url: "https://..."
---

Optional body text in markdown.
```

---

## Critical Files

| File | Purpose | When to Modify |
|------|---------|----------------|
| `content/settings/site.json` | Site metadata | Update personal info |
| `content/theses/*.md` | Thesis content | Add / edit theses |
| `admin/config.template.yml` | CMS schema | Adding new content fields |
| `scripts/build.js` | Build pipeline | Changing output format |
| `scripts/generate-cms-config.js` | CMS config generator | CMS backend changes |
| `src/css/tokens.css` | Design tokens | Color / spacing changes |
| `src/css/layout.css` | Layout + components | UI structure changes |

### Files You Should NOT Modify

| File | Reason |
|------|--------|
| `admin/config.yml` | Generated at build time from template |
| `dist/` | Build output — auto-generated |

---

## Build Pipeline

```bash
npm run build
  ├─ prebuild: generate-cms-config.js  # admin/config.yml from template
  └─ build.js                           # main build
      ├─ Load content/settings/site.json
      ├─ Load content/theses/*.md
      ├─ Render index.html
      ├─ Generate llms.txt + llms-full.txt
      ├─ Generate api/content.json
      ├─ Generate sitemap.xml + feed.xml + robots.txt
      └─ Copy css/ + assets/ + admin/
```

### Build Output

```
dist/
├── index.html          # Portfolio page
├── llms.txt            # AI agent guidance
├── llms-full.txt       # Full content dump
├── api/content.json    # Structured JSON API (CORS-enabled)
├── sitemap.xml         # Search engine sitemap
├── feed.xml            # RSS feed
├── robots.txt          # AI crawler allowances
├── css/                # Stylesheets
├── assets/fonts/       # Self-hosted fonts
└── admin/              # CMS entry point
```

---

## Design System

Design tokens in `src/css/tokens.css`. Only change variable **values**, never names.

- **Background:** `#F5F5F5` (warm off-white)
- **Text:** `#000` (black)
- **Accent:** `#bf150f` (crimson)
- **Font display:** Kyrios (variable sans — self-hosted)
- **Font body:** Merriweather (serif — Google Fonts)
- **Font mono:** Departure Mono / system monospace (technical label voice)
- **Font kairon:** Kairon (custom display glyph — self-hosted)

### Design Patterns (borrowed from Sky / kairon.xyz)

| Pattern | Class | Notes |
|---------|-------|-------|
| Rotated margin label | `.margin-label` | 10px mono, vertical-rl |
| Section heading | `.sec-head` | grid: title · rule · label |
| Chapter marker | `.chapter-marker` | `1fr auto 1fr` with dashed lines |
| Dot-leader TOC | `.toc-row` | `auto 1fr auto` grid |
| Drop cap | `.dropcap` | First letter float |
| Paper rule | `.rule-dotted` | Radial gradient dots |

---

## CMS Configuration (Sveltia CMS)

- **Backend:** GitHub (`K41R0N/k41r0n.github.io`)
- **Auth:** `https://sveltia-cms-auth.alejandro-057.workers.dev/` (hardcoded in template)
- **Collections:** `theses` + `settings`
- **Admin URL:** `/admin`

### Environment Variables (Vercel dashboard)

Only one variable needs to be set. The rest are hardcoded in `admin/config.template.yml`.

| Variable | Value |
|----------|-------|
| `PUBLIC_SITE_URL` | Your Vercel URL or custom domain |
| `GOOGLE_SITE_VERIFICATION` | Google Search Console token (optional) |

> `CMS_REPO` and `CMS_AUTH_URL` are **hardcoded** — no Vercel env vars needed for them.

---

## LLM-Friendly Endpoints

| Endpoint | Purpose |
|----------|---------|
| `/llms.txt` | AI agent guidance (llmstxt.org standard) |
| `/llms-full.txt` | Complete content dump |
| `/api/content.json` | Structured JSON with CORS headers |
| `/sitemap.xml` | Search engine sitemap |
| `/feed.xml` | RSS feed |
| `/robots.txt` | AI crawler allowances (GPTBot, ClaudeBot, etc.) |

---

## Key Commands

```bash
npm install          # Install dependencies (gray-matter, marked)
npm run build        # Production build → dist/
npm run validate     # Validate content only (placeholder)
```

---

## Handover Checklist

Before shipping changes, verify:
- [ ] `npm run build` completes without errors
- [ ] `dist/index.html` renders correctly in browser
- [ ] All 3 theses appear with correct links
- [ ] `dist/llms.txt` contains correct metadata
- [ ] `dist/robots.txt` has AI crawler allowances
- [ ] `dist/api/content.json` is valid JSON
- [ ] Fonts load correctly (no FOUT / invisible text)

---

*Built with clarity, not breadth.*
