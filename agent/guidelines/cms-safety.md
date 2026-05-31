# Guideline — CMS Safety (Do Not Break Sveltia)

This is the most important guideline in `agent/`. The CMS is how Alejandro edits
his own site without touching code. Breaking it is a high-cost, low-visibility
failure — it surfaces later, to him, in the browser. Read this fully before you
go anywhere near `admin/`.

## How the CMS is wired

- **Engine:** Sveltia CMS (a drop-in replacement for Decap/Netlify CMS; same
  config format).
- **Backend:** GitHub, repo `K41R0N/k41r0n.github.io`, branch `main`. The CMS
  commits content **directly to `main`**, which auto-deploys via Vercel.
- **Auth:** a Cloudflare Worker (`base_url` in the template). This and the `repo`
  line are identity-critical — breaking them logs Alejandro out of his CMS.
- **Schema source:** `admin/config.template.yml`. The live
  `admin/config.yml` is **generated** from it by `generate-cms-config.js` at
  build time (substituting `${VAR}` placeholders). **Always edit the template;
  the output is disposable.**

## The five invariants

### 1. The schema is generated — edit the template, never the output

`admin/config.yml` is rebuilt every `npm run build`. Hand-edits are destroyed.
All schema changes go into `admin/config.template.yml`, which is a **Tier 1**
path (propose via the forcing function in `PORTFOLIO-WRITE-GUARD-01.md`).

### 2. Every content file the build reads must be in the schema

If `build.js` reads a file from `content/` but it has no `file:`/`folder:` entry
in the schema, it is invisible to the CMS — Alejandro can't edit it in `/admin`.
The current collections are:

| Collection | Maps to |
|---|---|
| Home Page → Hero · About | `content/about.md` |
| Home Page → Home · Sections & Newsletter | `content/home.json` |
| Home Page → Writing Links | `content/writing.json` |
| Blog | `content/blog/*.md` (folder collection, `create: true`) |
| Theses | `content/theses/*.md` (folder collection, `create: true`) |
| Settings → Site Settings | `content/settings/site.json` |

If you add a new content file the build reads, you must add a matching collection
(Tier 1).

### 3. The schema must expose ALL frontmatter fields a file uses — or they vanish

This is the silent-data-loss trap. Sveltia maps a file to the fields declared in
the schema. **On the next CMS save, any frontmatter field present in the file but
absent from the schema is stripped.** So:

- Never add a frontmatter field to a content file without also adding it to the
  schema (Tier 1), **or** be certain the field is build-irrelevant and accept it
  will not survive a CMS save.
- For fields the build needs but the editor shouldn't change, use
  `widget: hidden` in the schema so the value is preserved.

This is documented in depth in
`docs/solutions/best-practices/sveltia-cms-schema-completeness-2026-05-31.md`.

### 4. `content/about.md` has NO frontmatter — keep it that way

The Home → Hero · About collection maps to the **body only**. If you add
frontmatter to `about.md`, the CMS will strip it on the next save. The build also
expects body-only here. Plain Markdown, nothing above it.

### 5. Field names are a contract with `build.js`

The schema field `name:` must match the JSON key / frontmatter key that
`build.js` reads. Renaming a field in the schema without updating `build.js`
(and the content file) silently drops the value to its fallback. Field renames
are Tier 1 and require all three to move together: content file → schema →
`build.js`.

## Validator coupling (don't forget this one)

`validate-content.js` independently requires these `site.json` keys, regardless
of the CMS schema:

```
title · full_name · description · author · email · github · substack · site_url
```

Note `author` is required *in addition to* `full_name`. Removing any of these
fails the build. If you restructure `site.json`, keep every required key.

## Safe CMS-adjacent tasks (still Tier 2)

- Editing the **values** in `content/*.json` and `content/**/*.md`.
- Adding a new blog post or thesis file whose frontmatter exactly matches the
  existing schema (Blog / Theses collections already allow `create: true`).

## Tasks that are Tier 1 (propose first)

- Adding/removing/renaming any field in `admin/config.template.yml`.
- Adding a new collection or `file:`/`folder:` entry.
- Changing `backend`, `repo`, `branch`, or `base_url`.
- Adding a new configurable string to the build — see
  `skills/add-configurable-field.md` for the correct end-to-end procedure.
