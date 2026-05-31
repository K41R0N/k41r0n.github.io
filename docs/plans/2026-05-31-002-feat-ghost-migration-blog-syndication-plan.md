---
title: "feat: Ghost CMS migration, blog page, and content syndication foundation"
type: feat
status: superseded
superseded_by: docs/plans/2026-05-31-003-feat-blog-syndication-agent-native-plan.md
superseded_reason: >
  Ghost migration evaluated and rejected. Ghost adds infrastructure complexity
  with no benefit for an agent-driven site. Sveltia + Vercel retained.
  See docs/solutions/best-practices/ghost-cms-rejected-2026-05-31.md for the
  full decision record.
date: 2026-05-31
origin: docs/plans/syndication-spec.md
---

# feat: Ghost CMS migration, blog page, and content syndication foundation

## Overview

Three-phase project to:
1. Migrate the portfolio from a static Node.js build system to Ghost CMS (open source, self-hosted), porting the existing design verbatim as a Ghost Handlebars theme
2. Add a blog section fed by Ghost posts, styled with the existing article layout, with automated syndication to Paragraph via RSS and a semi-automated flow to Substack
3. Run a full review pass to ensure SEO foundations, LLM-friendly endpoints, and canonicalisation are correct before going into the active content syndication phase

Ghost becomes the CMS. Vercel stays in the infrastructure as the edge/serverless layer for custom endpoints and the syndication automation receiver. The existing design (CSS tokens, fonts, layout classes, crimson palette) is carried over unchanged — only the templating language changes from JavaScript template literals to Handlebars.

---

## Problem Frame

The current static site uses Sveltia CMS (Git-based, push-to-rebuild) which is adequate for configuration but poor for writing. There is no blog, no article archive, and no automated cross-posting. The site is the intended canonical home for Device Economies writing — a place to generate citations, surface thinking, and flow leads — but it has none of the infrastructure for that. (see origin: `docs/plans/syndication-spec.md`)

---

## Requirements Trace

- R1. Ghost OSS (self-hosted) replaces Sveltia as the CMS. Ghost Admin is the editorial interface.
- R2. The existing design (CSS, fonts, palette, layout classes) is preserved exactly — no visual regression.
- R3. A blog section exists at `/blog/` showing Ghost posts styled with the existing article layout.
- R4. Theses continue to exist as a distinct section on the home page, fed by Ghost posts tagged `thesis`.
- R5. Writing links on the home page are curated in Ghost Admin, not auto-aggregated.
- R6. Ghost posts auto-cross-post to Paragraph via RSS (set-and-forget after initial connection).
- R7. Ghost `post.published` webhook triggers a Vercel edge function that sends a timed notification to manually publish on Substack (Substack has no API — manual step is unavoidable).
- R8. All existing machine-readable endpoints are preserved or replaced with equivalent: `/llms.txt`, `/llms-full.txt`, `/api/content.json`, `/sitemap.xml`, `/feed.xml` (→ `/rss/`), `/robots.txt`.
- R9. Canonical URL for every post is the Ghost URL. Paragraph and Substack receive visible attribution text.
- R10. GA4 (`G-4E1LTHSFX8`) continues firing on all pages.
- R11. Vercel stays in the stack as the primary public entry point (Option A) — proxies to Ghost for all page routes, serves custom endpoints directly.
- R12. Substack remains the email channel throughout. Ghost's native newsletter feature stays disabled.
- R13. The current static site config is tagged and preserved in Git. Vercel can roll back to the pre-Ghost static build at any time by reverting to the tag.

---

## Scope Boundaries

- No Ghost membership or paid subscriptions in this phase — members features disabled
- No Ghost newsletter (native email sending) — Substack remains the email channel indefinitely until explicitly re-evaluated
- No Obsidian-to-Ghost pipeline — writing workflow stays as-is; content is pasted into Ghost Admin
- No migration of Mirror-era articles in this phase — Paragraph archive is handled by RSS import from Ghost
- No custom Koenig editor extensions — margin notes will be authored as HTML cards in Ghost Admin
- The Cloudflare Worker for Sveltia auth is decommissioned (Ghost Admin has its own auth)
- `admin/config.template.yml` and `scripts/build.js` are replaced and archived, not migrated

---

## Context & Research

### Current Architecture (what's being replaced)

- **Build:** `scripts/build.js` — 640 lines of vanilla Node.js generating static HTML from `content/` files
- **CMS:** Sveltia CMS (Git-based, browser UI at `/admin`, commits to GitHub, triggers Vercel rebuild)
- **Hosting:** Vercel serves `dist/` (static)
- **Content:** markdown + JSON files in `content/` (3 theses, about.md, home.json, writing.json, settings/site.json)
- **CSS:** 7 files in `src/css/` — fully portable vanilla CSS, no framework dependency
- **Fonts:** `AT-Kyrios-Variable.woff2` (Kyrios) and `KaironFont.otf` (Kairon) — self-hosted

### Ghost Theme Architecture (confirmed from Ghost OSS repo v6.43.2)

A Ghost theme requires exactly three files: `index.hbs`, `post.hbs`, `package.json`. Everything else is optional. The Handlebars template inheritance is: `post.hbs` → `{{!< default}}` → `default.hbs`. CSS, fonts, and images are placed in `assets/` and referenced via the `{{asset}}` helper which handles cache-busting automatically.

Ghost's `routes.yaml` supports custom collections and URL structures. The portfolio home page (`/`) will use a custom template (not the default post feed) defined via `routes.yaml`.

Custom theme settings are declared in `package.json` under `config.custom`. These become editable fields in Ghost Admin → Design → Customize. This is where configurable labels (`thesis_nav_label`, section headings, etc.) that currently live in `home.json` and `site.json` will live.

Ghost webhooks (confirmed from `ghost/core/core/server/services/webhooks/listen.js`) support `post.published`, `post.published.edited`, `post.scheduled`, and `site.changed` events. These fire a JSON POST to a registered endpoint.

### Vercel's Role Going Forward

Vercel is NOT replaced. Its role shifts:
- **Previously:** Static hosting + build runner
- **Going forward:** Serverless/edge layer for:
  - `/llms.txt` — Vercel edge function querying Ghost Content API → formats as llms.txt
  - `/llms-full.txt` — Same pattern, full content dump
  - `/api/content.json` — Thin proxy that reshapes Ghost Content API to existing schema
  - Syndication webhook receiver — Ghost fires `post.published` → Vercel function handles delay + notification logic

Ghost and Vercel coexist: Ghost serves `kairon.xyz` (the website), Vercel handles specific routes and automation. DNS routes `kairon.xyz` to the Ghost instance. Specific paths (`/llms*.txt`, `/api/*`) are reverse-proxied from Ghost to Vercel functions OR served directly from Vercel with Ghost as origin for all other routes.

### Syndication Reality (confirmed from Paragraph docs + Ghost webhook source)

- **Paragraph:** Fully automated via RSS. Connect once in Paragraph Settings → Import. Every Ghost post auto-appears on Paragraph. No API needed.
- **Substack:** No public API. Ongoing auto-publish is not possible. Best achievable: Ghost `post.published` webhook → Vercel function → sends a Slack/email notification with the post content and a reminder to publish on Substack after N days.
- **Canonical:** Ghost sets `rel="canonical"` to its own URL automatically. Paragraph cross-posts have no canonical field — add "Originally published at [URL]" as the first line of each piece.

### LLM/SEO Endpoint Mapping

| Current endpoint | Ghost native | Vercel function needed |
|---|---|---|
| `/llms.txt` | None | Yes — query Ghost Content API, format as llms.txt |
| `/llms-full.txt` | None | Yes — same, include full post HTML |
| `/api/content.json` | Ghost Content API (different schema/URL/auth) | Yes — thin proxy to reshape |
| `/sitemap.xml` | Native (Ghost generates automatically) | No |
| `/feed.xml` | Native at `/rss/` | Redirect only (`/feed.xml` → `/rss/`) |
| `/robots.txt` | Basic (Ghost generates) | Override via routes.yaml + static file |

### Institutional Learnings

- `docs/solutions/best-practices/sveltia-cms-schema-completeness-2026-05-31.md` — all content fields must have a CMS equivalent. In Ghost, this means: custom theme settings for structural labels, Ghost posts/pages for content, Ghost Admin settings for site identity.

---

## Key Technical Decisions

- **Ghost hosting:** Railway using Ghost's official `Dockerfile.production` (confirmed in the Ghost OSS repo). Railway runs the container with a persistent volume for Ghost's content directory (uploads, themes, SQLite database). No server to manage — Railway handles TLS, process supervision, and restarts. Estimated cost: $5–15/mo usage-based. SQLite is used (Railway persistent disk; MySQL is not needed for personal site traffic). **Resolved: Railway + Docker is the hosting path.**

- **One domain, two roles:** Ghost serves `kairon.xyz`. Vercel serves specific paths (`/llms*.txt`, `/api/*`) via serverless functions. DNS routes all traffic to Ghost; Ghost's routes.yaml passes `/api/*` and `/llms*.txt` to Vercel functions via HTTP proxy OR Vercel is configured with Ghost as the origin and intercepts specific paths.

- **Vercel as single entry point (confirmed — Option A):** `kairon.xyz` stays pointed at Vercel. Vercel `vercel.json` rewrites: `/llms*.txt` → Vercel function, `/api/*` → Vercel function, `/robots.txt` → Vercel function, everything else → Ghost instance on Railway via `rewrites` destination. Vercel's edge network provides CDN caching globally in front of Ghost. No DNS change required.

- **Theme name:** `kairon` — stored in the Git repo under `ghost/` directory. Ghost Admin installs it via zip upload or symlink.

- **Theses in Ghost:** Ghost posts tagged `thesis` with a custom internal tag `#portfolio`. The routes.yaml defines a `theses` collection at `/theses/{slug}/`. The home page `index.hbs` queries `{{#get "posts" filter="tag:thesis" limit="all"}}` to render the dot-leader TOC. Existing slugs (`devices-as-co-creations`, etc.) are preserved — no redirect needed.

- **Writing links in Ghost:** A Ghost Page titled "Writing" with a custom Handlebars template (`writing.hbs`) that iterates a list. Since Ghost has no native "curated external links" type, this will be managed as a JSON file inside the theme (`assets/data/writing.json`) loaded via a theme partial. Ghost's Code Injection or a custom theme setting can override the path. Simpler than building a custom integration.

- **Margin notes:** In the current build, `> **Note:** text` in markdown becomes `<aside class="margin-note">`. Ghost's Koenig editor has an HTML card. Authors will use the HTML card to insert `<aside class="margin-note"><p>text</p></aside>` directly. The build.js regex transform is not replicated in Ghost — it's a manual editorial step. A Ghost editor documentation note covers this.

- **Drop cap:** CSS `::first-letter` on `.gh-content > p:first-of-type` applied in `post.hbs`. The `applyDropcap()` guard (skips single-letter words) is replaced by a simpler CSS rule — acceptable regression.

- **Custom theme settings for configurable labels:** All labels currently in `home.json` and `site.json` that are structural (section headings, sub-labels, nav label prefix) move to Ghost theme `config.custom` in `package.json`. These appear in Ghost Admin → Design → Customize. Sensible defaults mean they work out of the box.

---

## High-Level Technical Design

> *This illustrates the intended approach and is directional guidance for review, not implementation specification.*

```
┌─────────────────────────────────────────────────────────────┐
│                    kairon.xyz (DNS)                          │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────▼───────────────┐
        │         Vercel Edge            │
        │  /llms*.txt  →  edge fn        │
        │  /api/*      →  edge fn        │
        │  /*          →  proxy to Ghost │
        └───────────────┬───────────────┘
                        │ proxy
        ┌───────────────▼───────────────┐
        │    Ghost OSS (VPS, Caddy)      │
        │    routes.yaml:               │
        │      /          → index.hbs   │
        │      /theses/*  → post.hbs    │
        │      /blog/*    → post.hbs    │
        │      /rss/      → native      │
        │      /sitemap   → native      │
        │    Ghost Admin at /ghost/     │
        └───────────────────────────────┘

Syndication flow:
  Ghost post.published webhook
        │
        ▼
  Vercel webhook receiver fn
        │  immediately
        ├──→ Paragraph: already connected via RSS (automatic)
        │  after N days (configurable)
        └──→ Notification (email/Slack) to manually publish on Substack
```

---

## Implementation Units

### Phase 0 — Rollback Safeguard (run before any other work)

---

- [ ] **Unit 0: Tag current stable state and document rollback procedure**

**Goal:** The pre-Ghost static site is permanently tagged in Git and Vercel can return to it in under 5 minutes if anything in Phases 1–3 fails

**Requirements:** R13

**Dependencies:** None — this runs first, before any other unit

**Files:**
- No code changes — Git tag + documentation only
- Create: `docs/runbooks/rollback-to-static.md`

**Approach:**

Tag the current commit in Git:
```
git tag pre-ghost-stable
git push origin pre-ghost-stable
```

This tag captures the entire working static site: `scripts/build.js`, `content/`, `src/css/`, `admin/config.template.yml`, `vercel.json`. At any point, running `git checkout pre-ghost-stable` + a Vercel redeploy restores the site exactly as it was before this project started.

`docs/runbooks/rollback-to-static.md` documents:
1. How to revert Vercel to the tagged deployment (Vercel dashboard → Deployments → find the `pre-ghost-stable` deploy → Redeploy)
2. How to revert via Git (`git revert` back to the tag, push, Vercel redeploys automatically)
3. What DNS changes (if any) need to be reversed
4. How to reconnect the Cloudflare Worker if Sveltia CMS is needed again

**Critically:** `scripts/build.js`, `content/`, and `src/` are **never deleted** from the repo during this project — they are archived in place. The Ghost theme lives in a new `ghost/` directory. If Ghost is abandoned, the static build is still intact and executable.

**Test scenarios:**
- Happy path: `git checkout pre-ghost-stable && npm run build` produces a working `dist/` identical to the current live site

**Verification:**
- `git tag -l` shows `pre-ghost-stable`
- `git push origin pre-ghost-stable` confirms the tag is on the remote
- `npm run build` from the tag produces the current site without errors

---

### Phase 1 — Ghost CMS Migration

---

- [ ] **Unit 1: Deploy Ghost on Railway**

**Goal:** Ghost OSS running on Railway at an internal Railway URL, accessible for theme development and content entry — `kairon.xyz` is not yet affected

**Requirements:** R1, R11

**Dependencies:** Unit 0

**Files:**
- Create: `ghost/railway.toml`
- Create: `ghost/README.md` (Railway setup runbook + env var reference)

**Approach:**
- Create a Railway project. Deploy Ghost using the official `ghost:latest` Docker image (Railway has a Ghost template, or deploy from image directly)
- Mount a Railway Volume at `/var/lib/ghost/content` — this persists the SQLite database, uploaded images, and installed themes across container restarts
- Railway environment variables:
  - `url` → Railway staging URL initially (e.g. `https://kairon-ghost.up.railway.app`); updated to `https://kairon.xyz` only at DNS cutover (Unit 6)
  - `database__client` → `sqlite3`
  - `database__connection__filename` → `content/data/ghost.db`
  - `NODE_ENV` → `production`
  - `mail__transport` → `SMTP` with Mailgun or Postmark credentials (needed for Ghost Admin password resets)
- Ghost Admin accessible at `[railway-url]/ghost/`
- In Ghost Admin → Settings: disable Portal (member signup), disable Comments, disable Newsletter (email sending) — reduces injected JS and scope
- Initial content setup: site title "Kairon", site URL, author profile (name, email, bio)

**Test scenarios:**
- Happy path: Ghost Admin loads, can create a draft post, post renders at `[railway-url]/test-post/` with default theme
- Happy path: Railway container restarts → SQLite database and uploaded files persist via the mounted volume
- Error path: Ghost container OOM → Railway restarts it; verify restart policy is configured

**Verification:**
- Ghost Admin accessible at the Railway URL
- `[railway-url]/ghost/api/admin/site/` returns 200
- Test post publishes and renders correctly

---

- [ ] **Unit 2: Build the Kairon Ghost theme**

**Goal:** A Ghost theme that renders the current portfolio design exactly — same CSS, same fonts, same layout classes — across home page, thesis/article pages, and blog listing

**Requirements:** R2, R3, R4

**Dependencies:** Unit 1

**Files:**
- Create: `ghost/themes/kairon/package.json`
- Create: `ghost/themes/kairon/default.hbs`
- Create: `ghost/themes/kairon/index.hbs`
- Create: `ghost/themes/kairon/post.hbs`
- Create: `ghost/themes/kairon/page.hbs`
- Create: `ghost/themes/kairon/partials/masthead.hbs`
- Create: `ghost/themes/kairon/partials/toc-entry.hbs`
- Create: `ghost/themes/kairon/partials/footer.hbs`
- Create: `ghost/themes/kairon/assets/css/` (copy all 7 CSS files verbatim)
- Create: `ghost/themes/kairon/assets/fonts/` (copy Kyrios + Kairon fonts)
- Create: `ghost/themes/kairon/assets/img/kairon-logo.svg`
- Create: `ghost/themes/kairon/assets/data/writing.json` (copy content/writing.json)

**Approach:**

`default.hbs` — replaces `sharedHead()`:
- Same `<head>` structure with Ghost's `{{ghost_head}}` replacing the hardcoded meta tags
- GA4 injected via Ghost Admin Code Injection (not hardcoded in theme)
- CSS links via `{{asset}}` helper with cache-busting

`index.hbs` — replaces `renderHomePage()`:
- Masthead (wordmark + social metrics) — identical HTML/CSS
- Intro flow section — pulls content from a Ghost Page titled "About" via `{{#get "pages" filter="slug:about"}}`
- Theses TOC — `{{#get "posts" filter="tag:thesis" limit="all" order="published_at asc"}}` iterates to build dot-leader rows
- Writing links section — loaded from `assets/data/writing.json` via inline script fetch (theme-managed JSON file, editable via Ghost's file manager or theme zip update)
- Newsletter section — static HTML in the template, copy from current build
- Footer — `footer-ms` with `{{@site.title}}`, `{{date format="YYYY"}}`, etc.

`post.hbs` — replaces `renderThesisPage()`:
- Site nav with `← {{@site.title}}` back link and `{{title}}` breadcrumb
- Chapter nav — `{{#get "posts" filter="tag:thesis" limit="all"}}` for theses posts; tag-aware (shows all tags in the same primary tag for blog posts)
- Article layout with `.article` three-column grid, `.margin-label`, `.eyebrow` (tag name + post number)
- `{{content}}` renders Ghost post body inside the article grid
- `.margin-note` asides — authored as HTML cards in Ghost Admin
- Links section — authored in the post body as HTML card or a structured section
- Footer with `footer-ms`

`package.json` `config.custom` — all configurable labels from `home.json` and `settings/site.json`:
- `section_theses` (text, default "Theses")
- `section_theses_label` (text, default "index")
- `section_writing` (text, default "Writing")
- `section_newsletter` (text, default "Newsletter")
- `newsletter_body` (text)
- `newsletter_cta` (text, default "Subscribe on Substack →")
- `thesis_nav_label` (text, default "Thesis")
- Accessed in templates via `{{@custom.section_theses}}` etc.

**Patterns to follow:**
- `scripts/build.js` — the exact HTML structure to replicate in Handlebars
- `src/css/` — all files copy verbatim, zero edits
- Casper theme `/tmp/casper-theme/default.hbs` — reference for `{{ghost_head}}` / `{{ghost_foot}}` placement

**Test scenarios:**
- Happy path: home page renders with correct masthead, theses TOC with dot leaders, writing section, newsletter section — visual match to current `dist/index.html`
- Happy path: thesis detail page renders with `.article` three-column grid, `.margin-label`, drop cap on first paragraph
- Happy path: blog post renders with article layout, chapter nav showing other posts with same primary tag
- Edge case: thesis with no body (description-only) — post.hbs renders without article body section
- Edge case: post with no `<aside class="margin-note">` — third column of article grid is empty, layout does not break
- Error path: `{{#get}}` fails due to Ghost API error — page still renders without the TOC section (Handlebars fails silently on empty blocks)

**Verification:**
- Theme passes `gscan` validation with no fatal or error-level issues
- Home page visual comparison to current site shows no regressions
- All CSS classes from the current site (`.masthead`, `.toc-ms`, `.article`, `.footer-ms`) are present in the rendered DOM

---

- [ ] **Unit 3: Configure Ghost routes.yaml**

**Goal:** Correct URL structure for portfolio home, thesis collection, and blog collection

**Requirements:** R2, R3, R4

**Dependencies:** Unit 2

**Files:**
- Create: `ghost/themes/kairon/routes.yaml`

**Approach:**

```
routes:
  /:
    template: home         # custom home page template, not post feed
  /about/:
    data: page.about       # Ghost Page with slug "about"
    template: page

collections:
  /theses/:
    permalink: /theses/{slug}/
    filter: tag:thesis
    template: post
    data: tag.thesis

  /blog/:
    permalink: /blog/{slug}/
    filter: tag:blog
    template: post

taxonomies:
  tag: /tag/{slug}/
  author: /author/{slug}/
```

The current `thesis-NN-{slug}.html` URL pattern is not preserved (Ghost doesn't support `.html` extensions or numeric prefixes). Existing thesis URLs will 301 redirect to `/theses/{slug}/`. No inbound links currently exist, so SEO impact is minimal.

**Test scenarios:**
- Happy path: `kairon.xyz/` renders home page template (not default post feed)
- Happy path: `kairon.xyz/theses/devices-as-co-creations/` renders the thesis post with post.hbs
- Happy path: `kairon.xyz/blog/article-slug/` renders a blog post
- Edge case: old `thesis-01-devices-as-co-creations.html` URL returns 301 → configured via Ghost Admin Redirects

**Verification:**
- All routes return expected templates with correct data
- Ghost Admin → Labs → Routes shows custom routes active

---

- [ ] **Unit 4: Migrate existing content to Ghost**

**Goal:** All current portfolio content (3 theses, about page) exists in Ghost Admin as posts and pages, with correct tags, slugs, and metadata

**Requirements:** R1, R4, R5

**Dependencies:** Unit 1

**Files:**
- No code files — content migration via Ghost Admin UI
- Create: `ghost/import/kairon-export.json` (Ghost import format, generated once, archived)

**Approach:**
- Create Ghost Page: "About" (slug: `about`) — paste `content/about.md` body
- Create Ghost Post: "Devices as Co-Creations" (slug: `devices-as-co-creations`, tag: `thesis`) — paste thesis body, use HTML card for margin note, HTML card for links section
- Create Ghost Post: "The Future Belongs to the Storytellers" — same pattern
- Create Ghost Post: "Better Discovery Engines for Digital Culture" — same pattern
- For each thesis: set Custom Excerpt to the `description` field (this is the SEO meta description and TOC description)
- Verify publish dates are set (Ghost uses publish date for ordering within collections)
- For the writing links: update `ghost/themes/kairon/assets/data/writing.json` from `content/writing.json` (already identical)
- Configure Ghost Admin: site title "Kairon", site URL, navigation, author profile (full name, email, bio, social links)
- Migrate GA4 tag to Ghost Admin → Code Injection → Site Header (remove from theme)

**Test scenarios:**
- Happy path: all 3 theses appear in the home page TOC in correct order
- Happy path: each thesis detail page renders with correct body, margin note, and links
- Happy path: about page content matches current site

**Verification:**
- Ghost Admin → Posts shows 3 published posts tagged "thesis"
- Home page TOC shows all 3 theses with correct descriptions (dot-leader rows)

---

- [ ] **Unit 5: Vercel edge functions for LLM/SEO endpoints**

**Goal:** `/llms.txt`, `/llms-full.txt`, and `/api/content.json` continue to return correct responses, auto-updated from Ghost Content API on each request

**Requirements:** R8, R11

**Dependencies:** Unit 1 (Ghost Content API key needed)

**Files:**
- Create: `vercel/api/llms.js` (or `vercel/api/llms.ts`)
- Create: `vercel/api/llms-full.js`
- Create: `vercel/api/content.json.js`
- Create: `vercel/vercel.json`
- Modify: `vercel.json` (in repo root — update routing)

**Approach:**

Each Vercel function:
1. Fetches `https://kairon.xyz/ghost/api/content/posts/?key={GHOST_CONTENT_API_KEY}&filter=tag:thesis&include=tags&fields=title,slug,excerpt,custom_excerpt,html,published_at`
2. Formats the response
3. Returns with appropriate `Content-Type` and `Cache-Control` headers

`/llms.txt` response format matches current output exactly (site description, thesis list with descriptions, contact info, endpoint index, usage guidelines).

`/api/content.json` response matches the current custom schema (not Ghost's native schema) so any existing consumers of this endpoint continue to work.

`/robots.txt` — Ghost generates a basic one. Override by serving a static `robots.txt` from Vercel (same content as current, with AI crawler allowances) and having Vercel return it before the Ghost proxy for that path.

Ghost Content API key stored as a Vercel environment variable `GHOST_CONTENT_API_KEY`.

**Test scenarios:**
- Happy path: `GET /llms.txt` returns text with site description, 3 thesis entries with descriptions, contact links
- Happy path: `GET /api/content.json` returns JSON matching current schema (`version`, `site`, `theses` array)
- Happy path: after publishing a 4th thesis in Ghost, `/llms.txt` includes the 4th thesis within Vercel's cache TTL (1 hour)
- Error path: Ghost Content API returns 503 — Vercel function returns 502 with error body (no stale data served)

**Verification:**
- `curl https://kairon.xyz/llms.txt` returns correctly formatted content including all thesis titles
- `curl https://kairon.xyz/api/content.json` returns valid JSON matching the existing schema
- `curl https://kairon.xyz/robots.txt` includes AI crawler allowances

---

- [ ] **Unit 6: Vercel proxy configuration and redirect setup**

**Goal:** Vercel rewrites traffic to Ghost on Railway. No DNS change. Old thesis URLs 301 to new paths. All endpoints respond.

**Requirements:** R2, R8, R11, R13

**Dependencies:** Units 1–5 (Ghost running on Railway, theme installed, content migrated, Vercel functions deployed)

**Files:**
- Modify: `vercel.json` (add rewrites — Ghost Railway URL as destination)
- Create: `ghost/redirects.json` (old URL redirects, loaded into Ghost Admin)

**Approach:**

`vercel.json` updated to add rewrites (order matters — specific paths first):

```json
{
  "rewrites": [
    { "source": "/llms.txt",       "destination": "/api/llms" },
    { "source": "/llms-full.txt",  "destination": "/api/llms-full" },
    { "source": "/robots.txt",     "destination": "/api/robots" },
    { "source": "/api/(.*)",       "destination": "/api/$1" },
    { "source": "/(.*)",           "destination": "https://kairon-ghost.up.railway.app/$1" }
  ]
}
```

The last rule proxies everything else through to Ghost on Railway. DNS is not changed — `kairon.xyz` stays pointed at Vercel. Vercel acts as both CDN and entry point.

**Rollback:** Removing the last rewrite rule from `vercel.json` instantly restores the static site served from the `pre-ghost-stable` tag (or current build output). The Ghost instance keeps running but receives no traffic.

Old URL redirects (loaded via Ghost Admin → Settings → Labs → Redirects as JSON):
```json
[
  {"from": "/thesis-01-devices-as-co-creations.html", "to": "/theses/devices-as-co-creations/", "permanent": true},
  {"from": "/thesis-02-future-belongs-to-storytellers.html", "to": "/theses/future-belongs-to-storytellers/", "permanent": true},
  {"from": "/thesis-03-better-discovery-engines.html", "to": "/theses/better-discovery-engines/", "permanent": true},
  {"from": "/feed.xml", "to": "/rss/", "permanent": true}
]
```

Update the Ghost `url` environment variable in Railway to `https://kairon.xyz` (so Ghost generates correct canonical and sitemap URLs).

**Test scenarios:**
- Happy path: `curl https://kairon.xyz/` returns Ghost-rendered home page HTML (Kairon theme)
- Happy path: old thesis HTML URLs return 301 to correct `/theses/` paths
- Happy path: `/llms.txt` returns Vercel function response (not Ghost 404)
- Happy path: `/ghost/` returns Ghost Admin (proxied through Vercel to Railway)
- **Rollback test:** Remove last rewrite rule from `vercel.json` → `kairon.xyz` returns static site immediately

**Verification:**
- `curl -I https://kairon.xyz` returns 200, `Server` header from Ghost
- `curl https://kairon.xyz/llms.txt` returns correctly formatted content
- All 6 machine-readable endpoints respond correctly
- `curl -I https://kairon.xyz/thesis-01-devices-as-co-creations.html` returns 301

---

### Phase 2 — Blog Page + Content Syndication

---

- [ ] **Unit 7: Blog listing page and article template**

**Goal:** `/blog/` shows a paginated list of articles styled with the editorial layout; individual articles use the existing `.article` class with drop cap, margin notes, and links block

**Requirements:** R3

**Dependencies:** Unit 2 (theme), Unit 3 (routes)

**Files:**
- Create: `ghost/themes/kairon/blog.hbs` (blog collection listing template)
- Modify: `ghost/themes/kairon/post.hbs` (blog-vs-thesis conditional via `{{#has tag="thesis"}}`)
- Modify: `ghost/themes/kairon/index.hbs` (add "Latest Writing" preview section showing 3 most recent blog posts)

**Approach:**

`blog.hbs` — lists blog posts using the `toc-ms` / `toc-row` pattern from the home page, or a variant with publication dates. The existing `.sec-head` + dot-leader style translates directly to a blog listing.

`post.hbs` updates:
- `{{#has tag="thesis"}}` → show thesis-specific chapter nav (all theses); else show blog-specific nav (recent posts in same primary tag)
- Eyebrow: thesis posts show "Thesis NN · §1"; blog posts show "{{primary_tag.name}} · {{date format="DD MMM YYYY"}}"
- The `.article` grid, drop cap, and margin note structure is identical for both

Import a sample article (one existing Substack/Mirror piece) to validate the blog article layout before connecting the full syndication pipeline.

**Test scenarios:**
- Happy path: `GET /blog/` returns list of published blog posts in toc-ms style
- Happy path: blog post at `/blog/{slug}/` renders with `.article` layout, drop cap, date in eyebrow
- Happy path: thesis post at `/theses/{slug}/` renders with chapter nav showing all 3 theses
- Edge case: blog post with feature image — image renders in article header without breaking grid
- Edge case: very long post — margin-note column does not overflow or overflow-clip

**Verification:**
- `/blog/` returns a page with at least one article entry
- A blog post visually matches the thesis detail page layout (same CSS classes applied)

---

- [ ] **Unit 8: Import existing articles into Ghost**

**Goal:** All published Device Economies articles (from Substack and Mirror/Paragraph) exist in Ghost as published posts tagged `blog`, with correct canonical URLs

**Requirements:** R3, R9

**Dependencies:** Unit 7

**Files:**
- No code — content import via Ghost Admin (JSON import or manual paste)
- Create: `ghost/import/articles-archive.json` (Ghost import file, archived)

**Approach:**

Ghost Admin → Settings → Advanced → Import — supports importing from a Ghost-format JSON file. For Substack: export via Substack Settings → Exports (gives a zip with HTML files). Ghost's free concierge migration service handles Substack exports.

For Mirror articles (no native Ghost importer):
- Manual: copy HTML from Mirror post → paste into Ghost Koenig editor (handles HTML paste)
- Set canonical URL via Ghost Admin post settings → "Canonical URL" field (points to Mirror URL during transition; update to Ghost URL after publish)
- Set publish date to original publication date

Tag all imported articles `blog`. Set appropriate Custom Excerpt (used as SEO meta description).

**Test scenarios:**
- Happy path: imported Substack article renders correctly in Ghost with original publish date
- Happy path: Mirror article with canonical set to Ghost URL does not show Paragraph as canonical
- Edge case: article with embedded tweets — render as HTML card or remove embed (Twitter embeds may not load in Ghost)

**Verification:**
- Ghost Admin → Posts shows all imported articles as published
- `/blog/` listing shows imported articles in reverse chronological order

---

- [ ] **Unit 9: Paragraph RSS cross-posting (automated)**

**Goal:** Every new Ghost post auto-appears on Paragraph within ~1 hour of publication

**Requirements:** R6

**Dependencies:** Unit 1 (Ghost RSS feed available at `/rss/`)

**Files:**
- No code — configuration in Paragraph dashboard only

**Approach:**

1. Log in to Paragraph (`paragraph.com/@kairon-2`)
2. Go to Publication Settings → Import/Export
3. Enter Ghost RSS URL: `https://kairon.xyz/rss/`
4. Click Connect

Paragraph polls the RSS feed and auto-publishes any new items. The delay is typically 15–60 minutes.

Add a standard attribution line to every Ghost post template: the theme's `post.hbs` can inject a hidden or styled line:
```
{{! Injected attribution for syndication }}
<p class="syndication-note">Originally published at <a href="{{url absolute="true"}}">{{url absolute="true"}}</a></p>
```
This line is included in the RSS item HTML, so Paragraph displays it on every cross-post.

**Test scenarios:**
- Happy path: publish a test post in Ghost → within 60 minutes it appears on Paragraph with attribution line
- Happy path: editing a published post in Ghost → Paragraph reflects the update within the next poll cycle
- Edge case: deleting a Ghost post → Paragraph retains its copy (Paragraph does not support deletion via RSS)

**Verification:**
- Paragraph dashboard shows the connected RSS feed
- A test post published in Ghost appears on Paragraph within 60 minutes

---

- [ ] **Unit 10: Substack syndication notification (semi-automated)**

**Goal:** When a Ghost post is published, a timed notification fires after N days (default: 3) reminding the author to manually publish on Substack with the post content ready

**Requirements:** R7

**Dependencies:** Unit 1 (Ghost webhooks), Unit 5 (Vercel)

**Files:**
- Create: `vercel/api/syndication-webhook.js`
- Modify: `vercel/vercel.json` (add `/api/syndication-webhook` route)
- Create: `vercel/api/lib/notify.js` (send notification via email or Slack)

**Approach:**

Ghost Admin → Settings → Integrations → Add Custom Integration → "Syndication":
- Webhook URL: `https://kairon.xyz/api/syndication-webhook`
- Events: `post.published`
- Secret: stored as Vercel env var `GHOST_WEBHOOK_SECRET`

Vercel function (`syndication-webhook.js`):
1. Verify HMAC-SHA256 signature using `GHOST_WEBHOOK_SECRET`
2. Extract post title, excerpt, and canonical URL from the webhook payload
3. Schedule a delayed notification (use Vercel's `waitUntil` or a simple `setTimeout` → send email/Slack after N days delay). For production reliability, use a queue (Upstash QStash or similar) to deliver the notification after the configured delay.
4. Notification content: post title, canonical URL, formatted excerpt, "Time to publish on Substack" reminder

The notification includes everything needed to publish on Substack quickly: title, excerpt (for the email preview), full post URL for the "read more" link, and a direct link to draft a new Substack post.

**Test scenarios:**
- Happy path: Ghost publishes a post → Vercel function receives webhook → notification sent after N days with correct post data
- Error path: invalid HMAC signature → 401 returned, no notification sent
- Error path: Vercel function times out → use queue-based delivery (QStash) with at-least-once delivery guarantee

**Verification:**
- Ghost Admin → Integrations shows the webhook as active
- Publishing a test post triggers the Vercel function (visible in Vercel function logs)
- Notification arrives after the configured delay with correct post title and URL

---

### Phase 3 — Review Pass

---

- [ ] **Unit 11: SEO and canonical audit**

**Goal:** Every page has correct canonical URL, structured data, and sitemap inclusion. Ghost URL is the canonical for all content.

**Requirements:** R9

**Dependencies:** Units 1–10

**Files:**
- Modify: `ghost/themes/kairon/default.hbs` (verify `{{ghost_head}}` outputs correct canonicals)
- No code otherwise — configuration in Ghost Admin and Google Search Console

**Approach:**
- Ghost sets canonical on every page automatically via `{{ghost_head}}`. Verify with `curl` + grep for `rel="canonical"`.
- Submit `https://kairon.xyz/sitemap.xml` to Google Search Console
- Submit `https://kairon.xyz/sitemap-authors.xml`, `sitemap-tags.xml` (Ghost generates these automatically)
- Verify JSON-LD structured data on posts: Ghost injects Article schema via `{{ghost_head}}`. Supplement with `Person` and `WebSite` schema via Ghost Admin → Code Injection → Site Header (can be added as a static JSON-LD `<script>` tag).
- Verify `og:type`, `og:title`, `og:description`, `og:url` are set correctly on all page types
- Check that Paragraph and Substack cross-posts have visible "Originally published at" attribution

**Test scenarios:**
- Happy path: thesis post has `<link rel="canonical" href="https://kairon.xyz/theses/devices-as-co-creations/">` in its `<head>`
- Happy path: `https://kairon.xyz/sitemap.xml` returns valid XML listing all thesis and blog pages
- Happy path: Google Search Console shows no coverage errors after 48h
- Integration: Paragraph cross-post has attribution text visible to readers

**Verification:**
- Every published post's canonical points to `kairon.xyz`, not Paragraph or Substack
- Sitemap submitted to and accepted by Google Search Console

---

- [ ] **Unit 12: LLM endpoint verification and llms.txt update**

**Goal:** All machine-readable endpoints return accurate content reflecting the Ghost content, with correct format and schema

**Requirements:** R8

**Dependencies:** Units 5, 7, 8

**Files:**
- Modify: `vercel/api/llms.js` (update template to reflect Ghost-sourced blog posts in addition to theses)
- Modify: `vercel/api/content.json.js` (include blog posts in the `theses` array or a new `posts` array)

**Approach:**
- Update `llms.txt` to include the blog section and all imported articles
- Update `api/content.json` schema to include a `posts` array alongside `theses`
- Verify `robots.txt` explicitly allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended
- Verify `llms-full.txt` includes full HTML of all public posts from Ghost Content API

**Test scenarios:**
- Happy path: `/llms.txt` lists all thesis and blog posts with descriptions
- Happy path: `/api/content.json` has correct `version`, `site`, `theses`, and `posts` arrays
- Happy path: `robots.txt` allows all documented AI crawlers

**Verification:**
- `curl https://kairon.xyz/llms.txt | grep "Devices as Co-Creations"` returns a match
- `curl https://kairon.xyz/api/content.json | python3 -m json.tool` parses without error

---

- [ ] **Unit 13: Analytics and performance verification**

**Goal:** GA4 fires on all page types, Core Web Vitals are acceptable, no console errors

**Requirements:** R10

**Dependencies:** Unit 4 (GA4 moved to Code Injection)

**Files:**
- No code — configuration in Ghost Admin and GA4 dashboard

**Approach:**
- Verify GA4 fires on home, thesis, blog, and 404 pages by checking GA4 Real-time dashboard
- Run Lighthouse on home page and a blog post page. Target: Performance ≥ 80, Accessibility ≥ 90
- The existing CSS is already lean (no framework). Ghost adds its own scripts via `{{ghost_foot}}` — ensure unused Ghost scripts (portal, comments) are disabled in Ghost Admin if not used
- Disable Ghost Portal (member signup UI) in Ghost Admin → Settings → Access → Portal → turn off (reduces injected JS)
- Disable Ghost Comments if not used

**Test scenarios:**
- Happy path: GA4 Real-time shows a pageview event when visiting the home page
- Happy path: Lighthouse performance score ≥ 80 on home page
- Happy path: no JS console errors on any page type

**Verification:**
- GA4 Real-time shows active users when pages are manually visited
- Lighthouse report saved and benchmarked for future comparison

---

## System-Wide Impact

- **Sveltia CMS → decommissioned:** The Cloudflare Worker for OAuth (`sveltia-cms-auth.alejandro-057.workers.dev`) can be left running (low cost, no harm) or deleted. The `admin/` directory in the Git repo becomes unused.
- **`scripts/build.js` → archived:** The build system is replaced by Ghost's theme renderer. The `package.json` `build` script and Vercel build command are updated to do nothing (or removed from Vercel — Ghost serves the site directly).
- **Git repo role changes:** The repo (`K41R0N/k41r0n.github.io`) changes from "content + build system" to "theme source + Vercel functions". The `content/` directory is archived (content now lives in Ghost's database). Ghost Admin commits are not made to Git — Ghost stores content in its DB.
- **`/feed.xml` URL changes to `/rss/`:** One redirect. Any existing RSS subscribers using the old URL are redirected automatically.
- **Thesis URLs change:** `thesis-NN-{slug}.html` → `/theses/{slug}/`. Redirects configured. No existing inbound links known.
- **Unchanged:** GA4 measurement ID, kairon.xyz domain, Kyrios/Merriweather fonts, crimson palette, all layout CSS classes, Substack newsletter (remains independent email channel).

---

## Alternative Approaches Considered

- **Headless Ghost at `blog.kairon.xyz`:** Lower risk but splits domain authority. Rejected — user wants full Ghost migration, and path-based architecture under one domain is achievable with Ghost routes.yaml.

- **Ghost(Pro) instead of self-hosted:** $9–$25/month managed vs ~$5–6/month self-hosted VPS. Ghost(Pro) removes server maintenance burden and auto-patches CVEs. Viable alternative — decision deferred to user.

- **Keep Sveltia for non-blog content:** Would eliminate the need to port `home.json` / `site.json` field structures to Ghost custom theme settings. Rejected — user explicitly wants Ghost as the single CMS.

- **Zapier/Make automation for Substack:** Substack has no public API. Any "automation" that creates Substack posts would use unsupported private endpoints (fragile, ToS risk). Rejected. Notification-based semi-automation is the correct approach.

---

## Risks & Dependencies

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Ghost CVE during self-hosting (e.g. CVE-2026-26980) | Medium | High | Keep Ghost updated; consider Ghost(Pro) for auto-patching |
| Ghost `{{#get}}` helper performance on home page (3+ API calls) | Low | Medium | Cache results at theme level or use Ghost's native `{{posts}}` helper with filter |
| Margin note UX in Ghost Admin (HTML card required) | High | Low | Document the HTML snippet clearly; add a Ghost Admin bookmark to the snippet |
| Paragraph cross-posting delay >1 hour | Low | Low | Monitor first few posts; acceptable delay for syndication |
| Substack subscribers not seeing Ghost content | Medium | Medium | Maintain Substack as primary email channel during transition; Ghost newsletter opt-in later |
| DNS cutover causes downtime | Low | High | Keep Vercel serving old static site until Ghost is fully tested; flip DNS only after all Units 1–6 verified |

---

## Phased Delivery

### Phase 1 (Weeks 1–2): Ghost live, design matched, content migrated
- Units 1–6 complete
- `kairon.xyz` served by Ghost with Kairon theme
- 3 theses, about page in Ghost Admin
- LLM/SEO endpoints restored via Vercel functions

### Phase 2 (Weeks 3–4): Blog live, syndication active
- Units 7–10 complete
- `/blog/` page live with imported articles
- Paragraph connected and auto-posting
- Substack notification flow active

### Phase 3 (Week 5): Review pass complete
- Units 11–13 complete
- SEO audit done, canonicals verified, Search Console submitted
- Analytics confirmed working
- Site ready for active content syndication

---

## Documentation / Operational Notes

- Ghost Admin credentials stored securely (not in Git)
- Ghost Content API key stored as Vercel env var `GHOST_CONTENT_API_KEY`
- Ghost Webhook secret stored as Vercel env var `GHOST_WEBHOOK_SECRET`
- Syndication delay (days before Substack notification) stored as Vercel env var `SYNDICATION_DELAY_DAYS` (default: 3)
- Ghost backups: configure automated database export weekly via Ghost Admin → Settings → Advanced → Export
- Theme updates: zip the `ghost/themes/kairon/` directory and upload via Ghost Admin → Design → Upload theme

---

## Sources & References

- **Origin document:** `docs/plans/syndication-spec.md`
- **Ghost OSS repo:** https://github.com/TryGhost/Ghost (cloned at `/tmp/ghost-repo`, v6.43.2)
- **Casper reference theme:** https://github.com/TryGhost/Casper (cloned at `/tmp/casper-theme`)
- **Ghost webhook events:** `/tmp/ghost-repo/ghost/core/core/server/services/webhooks/listen.js`
- **Ghost routes.yaml defaults:** `/tmp/ghost-repo/ghost/core/core/server/services/route-settings/default-routes.yaml`
- **Paragraph cross-posting docs:** https://paragraph.com/docs/getting-started/cross-posting
- **Ghost custom theme settings API:** `config.custom` in Casper `package.json`
- Related code: `scripts/build.js` (the JS templates being ported to Handlebars)
- Related code: `src/css/` (all CSS files, carried over verbatim)
