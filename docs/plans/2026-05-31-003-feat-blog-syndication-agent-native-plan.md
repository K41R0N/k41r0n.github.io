---
title: "feat: Blog section, content syndication, and Research agent website editing"
type: feat
status: active
date: 2026-05-31
origin: docs/plans/syndication-spec.md
supersedes: docs/plans/2026-05-31-002-feat-ghost-migration-blog-syndication-plan.md
---

# feat: Blog section, content syndication, and Research agent website editing

## Overview

Four-phase project building on the existing Sveltia + Vercel stack (no CMS migration):

1. **Blog section** — `content/blog/*.md` in Sveltia, rendered with the existing `.article` layout, full SEO/LLM endpoint coverage
2. **Content syndication** — Paragraph connected to existing RSS (zero-code), n8n workflow on G14 for Substack notifications
3. **Research agent access** — Repo cloned on G14, fine-grained GitHub PAT scoped to this repo, git credentials configured for the Research agent workspace
4. **Agent-native skills + brain integration** — Website editing skill in Research agent skills folder, operational guidelines in Research brain, synced to Qdrant `research` collection

Ghost CMS evaluated and permanently rejected. Decision recorded in `docs/solutions/best-practices/ghost-cms-rejected-2026-05-31.md`.

---

## Problem Frame

The portfolio is the canonical home for Device Economies writing. It needs:
- A blog section for articles (currently no blog exists, only theses)
- Automated cross-posting to Paragraph (already subscribed) and semi-automated to Substack
- A Research agent that can update the site without human involvement for routine content additions
- All of this without introducing infrastructure that breaks the current zero-downtime, zero-maintenance setup

The G14 already runs n8n (`:5678`), Cloudflare Tunnel, and OpenClaw. The Research brain does not yet exist. The Research agent's website editing capability is the first concrete deliverable of that brain.

---

## Requirements Trace

- R1. Blog posts live at `content/blog/*.md`, editable via Sveltia CMS and committable by the Research agent
- R2. Blog listing page exists at `/blog/index.html`, styled with `.sec-head` + `.toc-ms` dot-leader layout
- R3. Individual blog posts render at `/blog/{slug}.html` using the existing `.article` layout (same as thesis pages)
- R4. `/feed.xml` includes both theses and blog posts. `/llms.txt`, `/llms-full.txt`, `/api/content.json`, `/sitemap.xml` all updated to include blog content
- R5. Paragraph auto-cross-posts from `/feed.xml` with no code changes (RSS import, set-and-forget)
- R6. n8n on G14 polls RSS for new entries and sends a Telegram/email notification to manually publish on Substack after N days
- R7. The portfolio Git repo is cloned on the G14 under a dedicated path in the Research workspace
- R8. A fine-grained GitHub PAT scoped exclusively to `K41R0N/k41r0n.github.io` with Contents: Read/Write is provisioned and stored in the Research workspace, never in chat or logs
- R9. A `website-editor` skill exists in `~/.openclaw/workspace-research/skills/website-editor/` with the full operational protocol for how the Research agent reads and updates site content
- R10. The website editing guidelines (what the agent can/cannot change, content schema, commit conventions) are stored in the Research brain and synced to the `research` Qdrant collection
- R11. The Ghost decision is permanently logged and does not re-surface in future planning sessions

---

## Scope Boundaries

- Blog post frontmatter schema is defined here; the specific list of permissible Research agent edits is deferred to a future session (user will scope this separately)
- No Obsidian-to-site pipeline in this phase — writing workflow stays manual
- No changes to `src/css/`, `scripts/build.js` structure beyond blog support, `admin/config.template.yml` CMS collections, or identity fields in `content/settings/site.json`
- n8n workflow is a notification trigger only — no automated Substack publishing (Substack has no API)
- Research brain full architecture is not scoped here — only the website editing slice is defined

---

## Context & Research

### Current Architecture (unchanged)

Build pipeline: `scripts/build.js` → reads `content/` → writes `dist/`. Sveltia CMS commits to GitHub → Vercel rebuilds `dist/` → serves. Vercel is the single public entry point with zero downtime.

Relevant existing patterns:
- `loadTheses()` in `scripts/build.js` — folder-of-markdown loader pattern to follow for `loadBlog()`
- `renderThesisPage()` — article template to reuse for blog posts (same CSS classes, no redesign)
- `generateFeed()` — RSS generator to extend with blog entries
- Sveltia theses collection in `admin/config.template.yml` — CMS schema pattern to follow for blog collection

### G14 Infrastructure (from OpenClaw spec)

- **Cloudflare Tunnel** (`cloudflared`, systemd root): `n8n.kairon.xyz` → `localhost:5678`. Webhook URL already configured as `webhook.kairon.xyz`. Adding routes: Zero Trust → Networks → Connectors → g14 → Published routes → Add. No CLI needed.
- **n8n** (Podman rootless, `localhost:5678`): PostgreSQL backend, `N8N_WEBHOOK_SECRET` in password manager. RSS polling is a native n8n trigger node.
- **Research workspace**: `~/.openclaw/workspace-research/`. Skills pattern: `~/.openclaw/workspace-setup/skills/` (e.g., `sky-mcp/sky-brain-mcp.py`). Skills folder for Research: `~/.openclaw/workspace-research/skills/`.
- **Qdrant research collection**: `research` (316 points as of S33). Sync via `store_context.py` with `--collection research`.
- **Supply chain**: npm `ignore-scripts=true` globally. All installs need operator approval before running.
- **Git on G14**: Already used for `agent_wiki` (commits 8077d9c, d87832d). Pattern is established.
- **Research brain**: Does not yet exist as a built structure. This plan creates the first slice: website editing guidelines.

### Syndication Reality (confirmed)

- **Paragraph**: Fully automated via RSS. Connect `/feed.xml` once in Paragraph Settings → Import. No code. No maintenance.
- **Substack**: No public API. Best achievable: n8n RSS polling → detect new entry → send notification (Telegram bot or email). Manual publish step by operator.
- **Canonical**: Ghost's `post.published` webhook is not needed. n8n polls RSS on a timer (every 15–30 min).

### Institutional Learnings

- `docs/solutions/best-practices/sveltia-cms-schema-completeness-2026-05-31.md` — every content file needs a CMS collection entry; every CMS field needs a `hint:`; no hardcoded copy in build templates
- `docs/solutions/best-practices/ghost-cms-rejected-2026-05-31.md` — Ghost not for this stack, do not re-evaluate

---

## Key Technical Decisions

- **Blog URL pattern**: `/blog/{slug}.html` matching the existing thesis pattern (`/thesis-NN-{slug}.html`). No subdirectory — all in `dist/` root for Vercel compatibility.

- **Blog frontmatter schema**: Minimal — `title`, `slug`, `date`, `description` required; `tags` optional. No `order` field (blog posts are reverse-chronological by `date`). `body` is the markdown content below frontmatter.

- **Article layout reuse**: `renderBlogPost()` reuses the exact same HTML structure as `renderThesisPage()` with minor differences: eyebrow shows date instead of "Thesis NN · §1", no chapter-nav (blog posts link to `/blog/` listing instead), no margin-label. All the same CSS classes apply — zero design work.

- **Blog listing layout**: Same `.sec-head` + `.toc-ms` dot-leader structure as the thesis TOC on the home page. Date shown as the `.pg` (right-side label) instead of "th. 01".

- **RSS merge**: `generateFeed()` extended to merge theses and blog posts, sorted by date descending. Both appear in `/feed.xml`. This is what Paragraph and the n8n RSS trigger will consume.

- **Research agent Git workflow**: Agent clones the repo to `~/repos/kairon-portfolio/` in the Research workspace (or a path within `~/.openclaw/workspace-research/`). Agent writes/edits markdown files, commits, pushes via HTTPS with the scoped PAT stored in Git credential store. Vercel detects the push and rebuilds. No branch strategy in this phase — agent commits directly to `main` for content-only changes (blog posts, writing links). Code-touching changes (build.js, CSS, config) are explicitly forbidden in the agent skill.

- **Fine-grained PAT scope**: GitHub → Settings → Developer settings → Fine-grained personal access tokens → New token. Repository access: `K41R0N/k41r0n.github.io` only. Permissions: Contents (Read/Write), Metadata (Read). No other repos, no other permissions. Token stored in Git credential helper on G14, not in any agent brain file or chat log.

- **n8n workflow trigger**: RSS trigger node polling `/feed.xml` every 30 minutes. On new item detected: extract title, description, URL → wait N days (configurable, default 3) via n8n Wait node → send notification via Telegram bot (already exists in G14 n8n setup based on `N8N_WEBHOOK_SECRET` env var presence) or email.

- **Website editing skill location**: `~/.openclaw/workspace-research/skills/website-editor/SKILL.md`. This is the operational protocol the Research agent loads when tasked with updating the website.

- **Qdrant sync for website guidelines**: Website editing guidelines stored as facts in the `research` Qdrant collection via `store_context.py --collection research`. Tags: `website`, `editing`, `protocol`. These are long-term operational protocols, not session facts — they belong in Qdrant `research`, not `ops_intelligence`.

---

## High-Level Technical Design

> *Directional guidance for review, not implementation specification.*

```
┌─────────────────────────────────────────────────────────────────┐
│                    Content Flow                                   │
│                                                                   │
│  Human writes        Agent writes        Sveltia CMS             │
│  (Obsidian → paste)  (markdown files)    (browser UI)            │
│         │                  │                    │                 │
│         └──────────────────┴────────────────────┘                │
│                            │                                      │
│                     git push to main                             │
│                            │                                      │
│                     Vercel rebuilds dist/                        │
│                            │                                      │
│              ┌─────────────┴─────────────┐                       │
│              │         kairon.xyz         │                       │
│              │  /index.html (portfolio)   │                       │
│              │  /blog/index.html          │                       │
│              │  /blog/{slug}.html         │                       │
│              │  /feed.xml  ──────────────►│ Paragraph (auto)     │
│              │  /llms.txt                 │                       │
│              └────────────────────────────┘                       │
│                                                                   │
│  n8n on G14 polls /feed.xml every 30min                          │
│    → new entry detected                                           │
│    → Wait 3 days                                                  │
│    → Telegram notification: "Publish on Substack: [title] [url]" │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                 Research Agent → Website                          │
│                                                                   │
│  ~/.openclaw/workspace-research/                                  │
│  ├── skills/                                                      │
│  │   └── website-editor/                                         │
│  │       └── SKILL.md  ← operational protocol                    │
│  └── repos/                                                       │
│      └── kairon-portfolio/  ← git clone of K41R0N/k41r0n.github.io│
│          └── content/                                             │
│              ├── blog/*.md    ← agent can create/edit            │
│              └── writing.json ← agent can update                 │
│                                                                   │
│  Qdrant research collection                                       │
│  ← store_context.py syncs website editing protocol              │
│  ← bootstrapped into agent context via bootstrap_context.py     │
└─────────────────────────────────────────────────────────────────┘
```

---

## Implementation Units

### Phase 1 — Blog Section in Sveltia + Vercel

---

- [ ] **Unit 1: Blog content schema and Sveltia collection**

**Goal:** Blog posts exist as `content/blog/*.md` with defined frontmatter, editable via Sveltia CMS

**Requirements:** R1

**Dependencies:** None

**Files:**
- Create: `content/blog/` directory (with a sample post to seed the collection)
- Modify: `admin/config.template.yml` (add `blog` folder collection)

**Approach:**

Blog post frontmatter schema:
```yaml
---
title: string          # required — display title
slug: string           # required — kebab-case URL identifier
date: YYYY-MM-DD       # required — publication date, used for ordering and RSS
description: string    # required — one-sentence summary for SEO + TOC + llms.txt
tags: [string]         # optional — topic tags, shown in eyebrow
---
Body markdown here.
```

`about.md` pattern: no frontmatter beyond what the build uses — keep it minimal.

Sveltia collection added to `admin/config.template.yml`:
```yaml
- name: blog
  label: Blog
  label_singular: Post
  folder: content/blog
  create: true
  slug: '{{date}}-{{slug}}'
  sortable_fields: ['date', 'title']
  summary: '{{date}} — {{title}}'
  fields:
    - {label: Title, name: title, widget: string}
    - {label: Slug, name: slug, widget: string, pattern: [...]}
    - {label: Date, name: date, widget: datetime, format: YYYY-MM-DD}
    - {label: Description, name: description, widget: text,
       hint: "One sentence. Appears in blog listing, RSS, SEO meta, and llms.txt."}
    - {label: Tags, name: tags, widget: list, required: false}
    - {label: Body, name: body, widget: markdown, required: false,
       hint: "Full article. > **Note:** text → margin note. --- → section break."}
```

**Patterns to follow:**
- Theses collection in `admin/config.template.yml` — identical structure
- `content/theses/*.md` frontmatter — same field approach

**Test scenarios:**
- Happy path: Sveltia CMS shows "Blog" in left nav with a list of posts; creating a new post generates a correctly formatted `content/blog/YYYY-MM-DD-slug.md` file
- Edge case: post with no tags — build handles missing field gracefully (default to empty array)

**Verification:**
- `admin/config.yml` (generated) contains the `blog` collection
- `content/blog/` contains at least one sample post with valid frontmatter

---

- [ ] **Unit 2: Blog build support — loader, listing page, post page**

**Goal:** Build script renders `/blog/index.html` (listing) and `/blog/{slug}.html` (posts) using existing CSS layout

**Requirements:** R2, R3

**Dependencies:** Unit 1

**Files:**
- Modify: `scripts/build.js` (add `loadBlog()`, `renderBlogListing()`, `renderBlogPost()`, update `main()`)

**Approach:**

`loadBlog()` — follows `loadTheses()` pattern:
- Reads `content/blog/*.md`
- Parses frontmatter via `gray-matter`
- Sorts by `date` descending (newest first)
- Returns array of `{title, slug, date, description, tags, body, filename}`

`renderBlogListing()` — generates `/blog/index.html`:
- Same `.ms-main` outer container
- Site nav with `← Kairon` back link
- `.sec-head` with "Blog" heading (from `home.blog_heading` if added to `home.json`, or hardcoded initially)
- `.toc-ms` dot-leader list: each post is a `.toc-group` row with title → dots → date (`DD MMM YYYY`)
- Footer same as home

`renderBlogPost()` — generates `/blog/{slug}.html`:
- Reuses `renderThesisPage()` structure verbatim with these differences:
  - Nav: `← Blog` link to `/blog/index.html` instead of `← Kairon`
  - Eyebrow: `{{primaryTag}} · {{date formatted}}` instead of `Thesis NN · §1`
  - No margin-label (blog posts don't have the rotated sidebar label)
  - No chapter-nav (no equivalent for blog; omitted)
  - Same `.article` three-column grid, dropcap, margin notes, links block

`main()` — calls both new renderers, generates one file per blog post.

**Patterns to follow:**
- `loadTheses()` in `scripts/build.js` — exact pattern for `loadBlog()`
- `renderThesisPage()` in `scripts/build.js` — template to fork for `renderBlogPost()`
- `.toc-ms` / `.toc-group` / `.toc-row` HTML in `renderHomePage()` — reuse for blog listing

**Test scenarios:**
- Happy path: `npm run build` generates `dist/blog/index.html` and `dist/blog/{slug}.html` for each blog post
- Happy path: blog listing shows all posts sorted newest-first with dot-leaders
- Happy path: blog post renders with `.article` grid, dropcap, and correct eyebrow (tag + date)
- Edge case: blog post with no tags — eyebrow shows date only, no tag prefix
- Edge case: `content/blog/` directory empty or missing — build completes with no blog output (no error)

**Verification:**
- `npm run build` exits 0
- `dist/blog/index.html` exists and contains `.toc-ms` markup
- `dist/blog/SLUG.html` exists for each post in `content/blog/`
- Blog post HTML contains `.article` class and `.dropcap` class

---

- [ ] **Unit 3: Update SEO and LLM endpoints to include blog**

**Goal:** `/feed.xml`, `/sitemap.xml`, `/llms.txt`, `/llms-full.txt`, `/api/content.json` all include blog posts

**Requirements:** R4

**Dependencies:** Unit 2

**Files:**
- Modify: `scripts/build.js` (update `generateFeed()`, `generateSitemap()`, `generateLlmsTxt()`, `generateLlmsFullTxt()`, `generateContentJson()`)

**Approach:**

All five generators receive the `blog` array in addition to `theses`. Changes are additive:

- `generateFeed()` — merges theses and blog posts, sorts by date descending. Blog items include `<pubDate>` from the `date` frontmatter field.
- `generateSitemap()` — adds `/blog/index.html` and each `/blog/{slug}.html` URL (priority 0.7, changefreq monthly)
- `generateLlmsTxt()` — adds a "Writing" section listing blog post titles and descriptions below the Theses section
- `generateLlmsFullTxt()` — appends full blog post bodies after theses
- `generateContentJson()` — adds a `posts` array alongside the existing `theses` array

**Test scenarios:**
- Happy path: `/feed.xml` contains both thesis and blog `<item>` entries, newest first
- Happy path: `/llms.txt` contains a "Writing" section with blog post descriptions
- Happy path: `/api/content.json` has both `theses` and `posts` arrays
- Edge case: no blog posts — endpoints render cleanly with empty or absent blog sections

**Verification:**
- `cat dist/feed.xml | grep '<title>'` shows both thesis and blog titles
- `cat dist/sitemap.xml | grep '/blog/'` shows blog URLs

---

### Phase 2 — Content Syndication

---

- [ ] **Unit 4: Paragraph RSS import (no code)**

**Goal:** Every new post on the site auto-appears on Paragraph within ~60 minutes of publication

**Requirements:** R5

**Dependencies:** Unit 3 (RSS feed includes blog posts)

**Files:** None — configuration only in Paragraph dashboard

**Approach:**
1. Log in to `paragraph.com/@kairon-2`
2. Publication Settings → Import/Export
3. Enter feed URL: `https://kairon.xyz/feed.xml`
4. Click Connect

From this point: set-and-forget. Every new entry in `/feed.xml` auto-publishes to Paragraph. The feed already includes attribution info in the description. No maintenance required.

**Test scenarios:**
- Happy path: publish a test blog post → appears on Paragraph within 60 minutes
- Edge case: updating an existing post — Paragraph retains original (no retroactive update via RSS)

**Verification:**
- Paragraph dashboard shows the connected feed URL
- One published post appears on Paragraph after connecting

---

- [ ] **Unit 5: n8n Substack notification workflow on G14**

**Goal:** When a new post appears in `/feed.xml`, n8n sends a Telegram notification after N days reminding operator to publish on Substack

**Requirements:** R6

**Dependencies:** Unit 3 (RSS includes blog posts), n8n running on G14

**Files:**
- Create: `docs/runbooks/n8n-substack-notification-workflow.md` (exported n8n JSON + setup instructions, archived for reproducibility)

**Approach:**

n8n workflow on G14 (`n8n.kairon.xyz`):
1. **RSS Trigger node** — polls `https://kairon.xyz/feed.xml` every 30 minutes
2. **Deduplication** — n8n's RSS trigger node tracks seen GUIDs natively; only new items proceed
3. **Wait node** — waits `SYNDICATION_DELAY_DAYS` (default: 3 days). n8n native Wait node supports this.
4. **Telegram node** — sends message to operator Telegram via existing bot (if configured) OR HTTP Request node to a webhook. Message format:
   ```
   📝 Ready to syndicate on Substack:
   
   Title: {title}
   URL: {url}
   Summary: {description}
   
   → Open Substack draft: https://substack.com/publish/post/new
   ```
5. (Optional) **Set node** — store a record in n8n's static data or append to a Google Sheet for editorial tracking

Operator approves the n8n workflow before activation (per `ask_first` principle from OpenClaw spec).
`SYNDICATION_DELAY_DAYS` as an n8n workflow variable, configurable without editing the workflow.

**Test scenarios:**
- Happy path: new feed entry detected → notification arrives after configured delay with correct title, URL, summary
- Happy path: existing feed entries are not re-notified on n8n restart (deduplication via RSS trigger state)
- Error path: `/feed.xml` unreachable → n8n RSS trigger fails silently; next poll succeeds

**Verification:**
- n8n workflow shows as Active in n8n dashboard
- Test run with a synthetic RSS entry triggers the Telegram notification after the configured wait
- Workflow JSON exported and saved to `docs/runbooks/n8n-substack-notification-workflow.md`

---

### Phase 3 — Research Agent Repo Access

---

- [ ] **Unit 6: Clone portfolio repo on G14 and configure Git credentials**

**Goal:** The portfolio repo is cloned under the Research workspace on the G14, with a fine-grained GitHub PAT configured for push access

**Requirements:** R7, R8

**Dependencies:** None (infrastructure work, no code changes)

**Files:**
- Create: `docs/runbooks/research-agent-git-setup.md` (one-time setup runbook, archived)

**Approach:**

**Step 1 — Provision fine-grained PAT (operator does this in browser):**
- GitHub → Settings → Developer settings → Fine-grained personal access tokens → Generate new token
- Token name: `g14-research-agent-kairon-portfolio`
- Expiration: 1 year (calendar reminder to renew)
- Repository access: **Only selected repositories** → `K41R0N/k41r0n.github.io`
- Permissions:
  - Contents: **Read and Write**
  - Metadata: **Read** (required by GitHub)
  - All other permissions: **No access**
- Copy token value — store in password manager immediately. Do not paste in any chat or log.

**Step 2 — Configure Git credentials on G14 (operator executes in terminal):**
```bash
git config --global credential.helper store
# Then on first push, Git will prompt and store the PAT via credential.helper
```
OR use a dedicated `.netrc` entry for `github.com` in the Research workspace.

**Step 3 — Clone the repo:**
```bash
mkdir -p ~/.openclaw/workspace-research/repos
cd ~/.openclaw/workspace-research/repos
git clone https://github.com/K41R0N/k41r0n.github.io kairon-portfolio
cd kairon-portfolio
git config user.name "Kairon Research Agent"
git config user.email "alejandro@kairon.xyz"
```

**Step 4 — Verify push works:**
Create a scratch file, commit, push, confirm on GitHub, delete the scratch file, commit, push.

**Operational rule (enforced in agent skill):** The Research agent never stores the PAT in plaintext in any brain file, MEMORY.md, AGENTS.md, or session log. The credential helper stores it in `~/.git-credentials` (operator-controlled). The agent references the path, not the token value.

**Test scenarios:**
- Happy path: `git push` from `~/.openclaw/workspace-research/repos/kairon-portfolio/` succeeds and Vercel detects the push and rebuilds
- Error path: PAT expired → push fails with 401; agent skill instructs agent to notify operator rather than attempt a workaround

**Verification:**
- `git remote -v` from the cloned repo shows `origin https://github.com/K41R0N/k41r0n.github.io`
- `git push` succeeds without password prompt (credential helper active)
- Vercel deployment triggered and site rebuilds successfully

---

### Phase 4 — Research Agent Skills + Brain Integration

---

- [ ] **Unit 7: Website editor skill for Research agent**

**Goal:** A formal skill exists in the Research workspace that the Research agent loads when tasked with updating the website. Defines the full operational protocol.

**Requirements:** R9, R10

**Dependencies:** Unit 6 (repo cloned, PAT configured)

**Files:**
- Create: `~/.openclaw/workspace-research/skills/website-editor/SKILL.md`

**Approach:**

`SKILL.md` structure (following OpenClaw's agent-native skill format):

```markdown
# Skill: website-editor

## Purpose
Update kairon.xyz content by editing markdown files and pushing to GitHub.
Vercel auto-rebuilds on every push.

## When to Use
When operator tasks Research agent with:
- Adding a new blog post
- Updating the writing links list
- Correcting a blog post (typo, link, description)

## Repo Location
~/.openclaw/workspace-research/repos/kairon-portfolio/

## Pre-flight (ALWAYS run before any edit)
1. cd ~/.openclaw/workspace-research/repos/kairon-portfolio/
2. git pull origin main  — must succeed before any edit
3. Read the file you intend to edit BEFORE proposing changes
4. Stop and report current state to operator if pull fails

## What the Research Agent CAN Edit

### Blog posts
- Create: content/blog/YYYY-MM-DD-{slug}.md
- Edit: content/blog/*.md (body, description, tags)
- Schema: see content schema section below

### Writing links
- Edit: content/writing.json
- Only add or remove entries from the "links" array
- Never change the JSON structure

## What the Research Agent CANNOT Edit (hard stop)
- scripts/build.js
- src/css/
- admin/config.template.yml
- content/settings/site.json
- content/theses/*.md  (operator's intellectual positions)
- content/home.json
- content/about.md
- vercel.json
- Any file outside content/blog/ and content/writing.json

If a task requires editing a forbidden file, STOP and ask operator.

## Content Schema — Blog Post

Required frontmatter:
  title: string
  slug: string (kebab-case, URL-safe, unique)
  date: YYYY-MM-DD
  description: string (one sentence, used in RSS and llms.txt)

Optional frontmatter:
  tags: [string]

Body: markdown below the frontmatter separator (---).
Supports:
  > **Note:** text   →  renders as margin note aside
  ---                →  section break rule

## Commit Convention
git add content/blog/{filename}.md   (or content/writing.json)
git commit -m "content: {one-line description of change}"
git push origin main

NEVER use git add -A or git add .
Stage only the specific file(s) that are part of the task.

## Verification After Push
Wait 60 seconds, then check:
https://kairon.xyz/blog/{slug}.html  (for new posts)
https://kairon.xyz/blog/index.html   (for listing)

If the page is 404 or shows old content after 120 seconds, report to operator.

## Error Handling
- git pull fails → stop, report to operator, do not edit
- git push fails with 401 → PAT may have expired, stop, report to operator
- git push fails with merge conflict → stop, report to operator, do not force push
- Build error (Vercel shows red) → file likely has invalid frontmatter; check YAML syntax
```

**Test scenarios:**
- Happy path: Research agent asked to add a blog post → follows SKILL.md protocol, creates file, commits, pushes, verifies
- Error path: `git pull` fails → agent stops and reports rather than proceeding

**Verification:**
- File exists at `~/.openclaw/workspace-research/skills/website-editor/SKILL.md`
- Skill file passes a manual read — all required sections present, no ambiguous steps

---

- [ ] **Unit 8: Store website editing guidelines in Research brain + Qdrant**

**Goal:** The operational protocol for website editing is stored as long-term facts in the `research` Qdrant collection, retrievable by the Research agent at bootstrap and during tasks

**Requirements:** R10

**Dependencies:** Unit 7 (SKILL.md exists)

**Files:**
- No new files — uses existing `store_context.py` on G14

**Approach:**

Facts to store via `store_context.py --collection research`:

1. **Website repo location**
   - `--text "Research agent website repo: ~/.openclaw/workspace-research/repos/kairon-portfolio/ — git clone of K41R0N/k41r0n.github.io — push triggers Vercel rebuild"`
   - `--tags website,git,repo`

2. **Editable paths**
   - `--text "Research agent can edit: content/blog/*.md (new posts and corrections) and content/writing.json (writing links list). All other paths in the kairon-portfolio repo are forbidden."`
   - `--tags website,permissions,editing`

3. **Forbidden paths**
   - `--text "Research agent CANNOT edit in kairon-portfolio: scripts/, src/css/, admin/, content/settings/site.json, content/theses/, content/home.json, content/about.md, vercel.json. Stop and ask operator if task requires these."`
   - `--tags website,permissions,forbidden`

4. **Skill location**
   - `--text "Website editor skill: ~/.openclaw/workspace-research/skills/website-editor/SKILL.md — load this before any website editing task"`
   - `--tags website,skills`

5. **Commit convention**
   - `--text "Website editing git commit format: 'content: {description}'. Stage specific files only, never git add -A. Push to origin main only."`
   - `--tags website,git,convention`

6. **Ghost decision (do not revisit)**
   - `--text "Ghost CMS was evaluated and rejected for kairon.xyz. Decision is final. Do not suggest Ghost migration. Stack is: Sveltia CMS + Vercel (static hosting). See docs/solutions/best-practices/ghost-cms-rejected-2026-05-31.md"`
   - `--tags website,ghost,rejected,decision`

Per OpenClaw spec: these are **long-term predictable protocols**, not session facts — correct collection is `research`, not `ops_intelligence`.

All store_context.py commands are presented to operator for approval before execution (supply chain security principle: no automated writes).

**Test scenarios:**
- Happy path: `query_context.py --collection research --query "website editing"` returns the repo path, permissions, and skill location
- Happy path: Research agent bootstrapped with these facts knows where the repo is and what it can edit before receiving any operator instruction

**Verification:**
- `python3 ~/bin/query_context.py --collection research --query "website repo"` returns fact #1
- `python3 ~/bin/query_context.py --collection research --query "ghost cms"` returns fact #6 (Ghost rejected)
- Qdrant `research` collection point count increases by 6 after ingestion

---

### Phase 5 — Cleanup and Decision Logging

---

- [ ] **Unit 9: Log Ghost decision, update superseded plan, commit everything**

**Goal:** Ghost decision is permanently recorded, the superseded plan is clearly marked, all new files are committed

**Requirements:** R11

**Dependencies:** All preceding units

**Files:**
- Already created: `docs/solutions/best-practices/ghost-cms-rejected-2026-05-31.md`
- Already updated: `docs/plans/2026-05-31-002-feat-ghost-migration-blog-syndication-plan.md` (status: superseded)
- Archive: `docs/plans/syndication-spec.md` (stays — origin document)

**Approach:**

Commit all changes from Units 1–3 (code changes to `scripts/build.js`, `admin/config.template.yml`, new `content/blog/` sample) plus the decision record and updated plan status.

Units 4–5 (n8n, Paragraph) have no code outputs — documented in runbooks only.
Units 6–8 (G14 setup) produce no repo changes — all work happens on the G14 directly.

**Verification:**
- `git log --oneline` shows a clean sequence of commits
- `docs/solutions/best-practices/ghost-cms-rejected-2026-05-31.md` exists and is committed
- The Ghost plan has `status: superseded` in its frontmatter

---

## System-Wide Impact

- **`/feed.xml`**: Now includes blog posts. Any existing RSS consumers (Paragraph, if already connected) will see new content types. No breaking change — additional items only.
- **`/api/content.json`**: New `posts` array added alongside `theses`. Existing consumers of the `theses` array are unaffected. Additive change.
- **Vercel build time**: Slightly longer (additional blog posts to render). Negligible for a personal site.
- **G14 n8n**: New workflow added to existing n8n instance. No impact on existing workflows.
- **G14 Research workspace**: New `skills/` and `repos/` paths created. No conflict with existing workspace structure.
- **Qdrant `research` collection**: 6 new facts added. No change to existing 316 points.
- **Sveltia CMS**: New "Blog" collection in `admin/config.yml`. Existing "Home Page", "Theses", "Settings" collections unchanged.
- **Unchanged invariants**: All existing URLs (`/`, `/theses/*.html`, `/llms.txt`, `/api/content.json` schema for `theses`), all CSS, all fonts, all Vercel config.

---

## Risks & Dependencies

| Risk | Mitigation |
|------|------------|
| Research agent edits a forbidden file | SKILL.md has an explicit forbidden list; Qdrant facts reinforce it; scope of edits deferred to operator for final definition |
| Fine-grained PAT expires after 1 year | Set a calendar reminder when provisioning; SKILL.md instructs agent to stop and report on 401 |
| n8n RSS trigger misses entries on restart | n8n RSS trigger stores seen GUIDs in workflow static data — survives restarts |
| G14 offline when agent tries to push | Agent detects push failure, reports to operator. Site is unaffected (push simply didn't happen). |
| Blog post invalid YAML frontmatter breaks build | `validate-content.js` can be extended to cover blog posts; Vercel build failure is visible in dashboard |
| Paragraph cross-posts before the Ghost decision reaches search index | Ghost decision has no effect on Paragraph. The ghost-cms-rejected doc is internal documentation only. |

---

## Phased Delivery

### Phase 1 (Priority — build and ship)
- Units 1–3: Blog section live on kairon.xyz, all endpoints updated
- Unit 9: Decision logged, plan committed

### Phase 2 (This week)
- Unit 4: Paragraph connected to RSS (10 minutes, no code)
- Unit 5: n8n workflow built and activated on G14

### Phase 3 (Next session with G14 access)
- Units 6–8: Research agent repo access, skill created, Qdrant facts stored

---

## Documentation / Operational Notes

- GitHub PAT stored in password manager + Git credential helper. Never in chat, logs, or brain files.
- n8n workflow JSON exported and archived in `docs/runbooks/` for reproducibility
- Research agent's scope of permitted edits (beyond what's defined here) is deferred to operator for a future scoping session

---

## Sources & References

- **Origin document:** `docs/plans/syndication-spec.md`
- **Ghost decision record:** `docs/solutions/best-practices/ghost-cms-rejected-2026-05-31.md`
- **Superseded plan:** `docs/plans/2026-05-31-002-feat-ghost-migration-blog-syndication-plan.md`
- **CMS schema patterns:** `docs/solutions/best-practices/sveltia-cms-schema-completeness-2026-05-31.md`
- **G14 infrastructure:** `docs/plans/Openclaw on Fedora Specs.txt`
- Existing patterns: `scripts/build.js` (`loadTheses()`, `renderThesisPage()`, `generateFeed()`)
- Existing CMS schema: `admin/config.template.yml` (theses collection)
- OpenClaw principles: `ask_first`, `read_before_write`, `verify_before_reporting`, supply chain security (all from OpenClaw spec)
