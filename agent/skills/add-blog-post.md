# Skill — Add a Blog Post

**When to use:** publishing a new Device Economies essay/article to `/blog/`.
**Tier:** 2 (content). No forcing function needed.
**Boundary:** if the *prose* is new and in Alejandro's voice, draft for review —
do not publish autonomously (see `../guidelines/contribution-workflow.md`).

## Steps

1. **Create the file** at `content/blog/YYYY-MM-DD-<slug>.md`. The date prefix is
   the convention; the `slug` frontmatter field (below) is what sets the URL.

2. **Write the frontmatter** (exact schema in
   `../guidelines/content-schemas.md`):
   ```markdown
   ---
   title: "The Headline"
   slug: "the-headline"          # ^[a-z0-9-]+$ , unique → /blog/the-headline.html
   date: "2026-05-31"            # YYYY-MM-DD
   description: "One-sentence summary — shows in listing, RSS, SEO, llms.txt."
   cover_image: "/assets/images/the-headline.svg"   # optional, square
   tags:                         # optional; first tag becomes the eyebrow
     - "essay"
   ---

   Body in Markdown.
   ```

3. **Write the body.** Available formatting:
   - `> **Note:** …` → right-margin note (`<aside class="margin-note">`).
   - A line of only `---` → section break.
   - First paragraph auto-gets a drop cap if it opens with 3+ letters.
   - Images: use `/assets/images/...` for local media, or paste Substack CDN
     URLs (auto-downsized to `w_800` and lazy-loaded).

4. **Cover image** (optional): drop a square SVG/image in
   `src/assets/images/` and reference it as `/assets/images/<file>`.

5. **Build & verify** — run `build-and-verify.md`. Confirm:
   - `dist/blog/<slug>.html` exists,
   - the post appears in `dist/blog/index.html` (newest-first),
   - it has an `<item>` in `dist/feed.xml` (the RSS syndication bridge).

6. **Ship** per `../guidelines/contribution-workflow.md`.

## Common mistakes

- Slug with uppercase/spaces → fails the `^[a-z0-9-]+$` expectation. Keep it
  lowercase-hyphenated.
- Missing `date` → ordering and RSS `pubDate` misbehave. Always set it.
- Adding a frontmatter field not in the Blog schema → it will be stripped on the
  next CMS save. Stick to the documented fields, or change the schema via
  `add-configurable-field.md` (Tier 1).
