# Skill — Add a New Configurable Field

**When to use:** a task needs a value that isn't editable yet — e.g. a new
section heading, a new settings string, a new piece of copy currently hardcoded
in `build.js`.
**Tier:** 1. This touches `admin/config.template.yml` and `scripts/build.js`.
**Emit the `PROPOSING PORTFOLIO WRITE` forcing function before editing those.**

A new JSON/frontmatter key alone does nothing. Three things must move together,
or you get silent failure (value ignored) or silent data loss (field stripped on
CMS save). Do all four steps.

## The four steps

1. **Add the field to the content file with a sensible default.**
   e.g. in `content/settings/site.json`:
   ```json
   "section_projects": "Projects"
   ```

2. **Add it to the CMS schema** in `admin/config.template.yml`, under the right
   collection, with a `hint:` that says *where it appears on the site*
   (Tier 1 — propose first):
   ```yaml
   - label: "Projects — Section Heading"
     name: section_projects
     widget: string
     default: "Projects"
     hint: "The h3 heading above the projects section on the home page."
   ```
   The `name:` must exactly match the key from step 1.

3. **Read it in `build.js` with a fallback** (Tier 1 — propose first):
   ```javascript
   <h3>${escHtml(settings.section_projects || 'Projects')}</h3>
   ```
   Always use `escHtml(...)` for any JSON/frontmatter string rendered into HTML,
   and always provide a `|| 'fallback'` so a missing value never breaks the page.

4. **Document it** — update `../guidelines/content-schemas.md` (and
   `CONTENT_ARCHITECTURE.md` if it changes the content map).

## Then

Build & verify (`build-and-verify.md`). Confirm the default renders, then change
the value in the content file and rebuild to confirm it flows through.

## Why all four are mandatory

- Skip step 2 → the field works on the site but Alejandro can't edit it in the
  CMS, **and** because it's now in the content file but absent from the schema,
  the next CMS save of that file **strips it**. This is the silent-data-loss
  trap from `../guidelines/cms-safety.md`.
- Skip step 3 → the CMS shows the field but it never appears on the site.
- Skip step 1 → no default; the field is undefined until someone fills it in.

## Field naming / removal

- Renaming an existing field is the same operation in reverse — content file,
  schema, and `build.js` must all change in one commit (Tier 1).
- Removing a field: remove from `build.js` first, then the schema, then the
  content file — and confirm nothing else reads it (`grep -rn fieldname scripts/`).
