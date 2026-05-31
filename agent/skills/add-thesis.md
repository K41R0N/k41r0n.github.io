# Skill — Add or Edit a Thesis

**When to use:** adding a new thesis or editing an existing one. A thesis drives
a home-page TOC row **and** a detail page at `thesis-NN-<slug>.html`.
**Tier:** 2 (content).

## Add a new thesis

1. **Create** `content/theses/<slug>.md`.
2. **Frontmatter** (all four fields required; see
   `../guidelines/content-schemas.md`):
   ```markdown
   ---
   title: "Better Discovery Engines"
   slug: "better-discovery-engines"   # ^[a-z0-9-]+$ , unique
   order: 4                            # int ≥ 1, UNIQUE across all theses
   description: "One sentence — TOC text + SEO meta only (not body text)."
   links:                             # optional
     - label: "Article"               # Article|Tool|Podcast|Project|Video|Curated Compilation
       title: "Display Title"
       url: "https://…"
   ---

   Markdown body — the article prose. `description` is NOT shown here.
   ```
3. **Pick `order` carefully.** It must be unique (the validator rejects
   duplicates) and it sets both the TOC sequence and the URL prefix
   (`thesis-04-...`). To insert between existing theses, you must renumber — see
   below.
4. **Build & verify** (`build-and-verify.md`): confirm
   `dist/thesis-04-<slug>.html`, the new TOC row in `dist/index.html`, and the
   entry in `dist/api/content.json`.

## Edit an existing thesis

Edit the file in place. Note the cost of changing each field:

- `slug` → **changes the URL** and breaks inbound links. Avoid unless intended.
- `order` → changes URL prefix and sequence; must stay unique.
- `title`, `description`, `links`, body → safe content edits.

## Renumbering (inserting/reordering)

`order` must remain unique and contiguous-ish for sensible URLs. If you insert a
thesis, bump the `order` of the ones after it. Each bump renames that thesis's
output file (`thesis-NN-...`), so it is effectively a URL change for those pages
— mention this in your report so Alejandro is aware of the redirect implication.

## Common mistakes

- Duplicate `order` or `slug` → validator fails the build. Check existing files
  first (`grep -h '^order:' content/theses/*.md`).
- Expecting `description` to show as body text on the detail page — it does not.
  Put visible prose in the body.
