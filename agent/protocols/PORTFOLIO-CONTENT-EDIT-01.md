# PORTFOLIO-CONTENT-EDIT-01

**Status:** Active
**Applies to:** Any Tier 2 content edit (see `PORTFOLIO-WRITE-GUARD-01.md`).
**Principle:** Verify before reporting. An edit is not "done" until the build is
green and you have confirmed the change reached `dist/`.

This is the standard loop for editing content. Follow it exactly; do not skip the
verification steps.

---

## The loop

### 1. Locate the source

Find which `content/` file drives the thing you want to change. Use the routing
table in `guidelines/repo-architecture.md` or `CONTENT_ARCHITECTURE.md`. If a
visible string is *not* traceable to a `content/` file, it is hardcoded in
`scripts/build.js` — that is a Tier 1 change, stop and read
`skills/add-configurable-field.md`.

### 2. Check the schema before you write

Open `guidelines/content-schemas.md`. Confirm:
- Required frontmatter fields are all present and correctly typed.
- `slug` matches `^[a-z0-9-]+$` and is unique within its collection.
- `order` (theses) is unique.
- You are not introducing a frontmatter field that is absent from the CMS schema
  in `admin/config.template.yml` (that field would be stripped on the next CMS
  save — if you genuinely need it, that is a Tier 1 schema change).

### 3. Make the edit

Edit the `content/` file. Preserve the file's existing shape:
- `content/about.md` — **no frontmatter**, body only.
- JSON files — valid JSON, keep all existing keys (especially validator-required
  keys in `site.json`: `title`, `full_name`, `description`, `author`, `email`,
  `github`, `substack`, `site_url`).

### 4. Build

```bash
npm run build
```

`prebuild` runs `validate-content.js` first. If it exits non-zero, your content
is malformed — fix it; do not work around the validator. A green build prints the
file list and `Build complete → dist/`.

### 5. Verify the change landed

Do not trust the build log alone. Confirm the rendered output:

```bash
grep -r "your new string" dist/        # the change is present
# and, where relevant:
cat dist/api/content.json | head        # structured API reflects it
```

For a new page, confirm the specific file exists in `dist/` (e.g.
`dist/blog/<slug>.html`, `dist/thesis-NN-<slug>.html`).

### 6. Report honestly

State what changed, that the build passed, and what you verified. If the build
failed or you could not verify, say so plainly with the output — do not claim
completion. ("Done" = build green AND change confirmed in `dist/`.)

### 7. Ship

Follow `guidelines/contribution-workflow.md` for branch/commit/PR. Content edits
may also legitimately be made by Alejandro through the CMS; if your edit overlaps
something he manages in `/admin`, prefer a PR so he can review rather than a
direct push to `main`.

---

## Failure handling

If any step errors (validator fails, build fails, grep finds nothing), **stop and
report** with the exact output. Do not silently retry with a different approach,
and do not edit `dist/` to "make it look right." The source is the only thing
worth fixing.
