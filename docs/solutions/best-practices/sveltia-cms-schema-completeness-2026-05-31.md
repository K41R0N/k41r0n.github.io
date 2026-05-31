---
title: "Complete CMS Schema Coverage: No Hardcoded Copy, No Orphaned Content Files"
date: 2026-05-31
category: docs/solutions/best-practices
module: cms-schema
problem_type: best_practice
component: tooling
severity: medium
applies_when:
  - Adding or editing copy in a static-site build template
  - Configuring Sveltia CMS (or any Git-based CMS) for the first time
  - Expanding a CMS schema after discovering hardcoded strings in build scripts
  - A content file exists under content/ but is absent from the CMS schema
symptoms:
  - Site copy (wordmark, hero text, section headings, newsletter body/CTA) is hardcoded in build.js
  - Content editors cannot update strings without touching source code and redeploying
  - A content file exists on disk but is not reachable from the CMS admin UI
  - A CMS save strips frontmatter fields that exist in the file but are absent from the schema
  - A field's CMS hint misleads editors about where the content actually appears on the site
root_cause: incomplete_setup
resolution_type: config_change
related_components:
  - documentation
tags:
  - cms
  - sveltia
  - schema
  - static-site
  - content-management
  - hardcoded-strings
  - admin-config
  - frontmatter
---

# Complete CMS Schema Coverage: No Hardcoded Copy, No Orphaned Content Files

## Context

Static site generators that assemble HTML from content files create a specific failure mode: strings that *look* like content get written directly into build script template literals, bypassing the CMS entirely. A second failure mode compounds this: a content file can exist on disk but be absent from the CMS schema, making it unreachable from the admin UI. A third failure mode: a CMS schema can expose a file but omit some of its frontmatter fields — on the next CMS save, those fields are silently stripped.

All three problems occurred in this portfolio's initial CMS setup:

**Hardcoded strings in `scripts/build.js` (not in CMS):**
- `"Alejandro<br>Arango"` — wordmark display name
- `"I'm in tech. I care about craftsmanship..."` — hero copy fallback
- `"Insights on digital creation..."` — newsletter body
- `"Subscribe on Substack →"` — newsletter CTA
- `"Theses"`, `"Writing"`, `"Newsletter"` — section heading labels

**Orphaned content file:**
- `content/about.md` body existed on disk but was absent from the CMS schema

**Frontmatter data-loss risk:**
- The initial `about.md` had frontmatter (`title`, `slug`, `order`, `description`, `layout`) not in the CMS schema — a CMS save would have stripped them silently

**Misleading field hints:**
- The thesis `description` field hint said "appears as the opening paragraph on the thesis page" — it doesn't. It's SEO-only on the detail page.

---

## Guidance

### Rule 1 — No visible string belongs in a build template

Every string that renders as visible text and was written by a human belongs in a content file. Hardcoded strings in build templates are a CMS coverage gap.

**Quick audit:**
```bash
# Find sentences/phrases hardcoded in template literals
grep -n '"[A-Z][a-z].*"' scripts/build.js

# Find content files the build reads
grep -o "content/[^'\"]*" scripts/build.js | sort -u

# Find files declared in the CMS schema
grep "^\s*file:" admin/config.template.yml | sort -u
# Diff the last two → any file in build but absent from schema is a gap
```

**Before → after (wordmark):**
```javascript
// Before: hardcoded
<p class="wordmark">Alejandro<br>Arango</p>

// After: from settings (always use escHtml for JSON-sourced strings)
<p class="wordmark">${escHtml(s.wordmark_line1)}<br>${escHtml(s.wordmark_line2)}</p>
```

**Before → after (section headings):**
```javascript
// Before: hardcoded
<h3>Theses<sup>03</sup></h3>

// After: from settings with fallback
<h3>${escHtml(s.section_theses || 'Theses')}<sup>03</sup></h3>
```

`content/settings/site.json` gains the new fields:
```json
{
  "section_theses": "Theses",
  "section_writing": "Writing",
  "section_newsletter": "Newsletter"
}
```

### Rule 2 — Every content file needs a CMS schema entry

If the build script reads a file from `content/`, that file must have a corresponding `file:` or `folder:` entry in the CMS schema.

**Before:** `content/about.md` existed on disk, no CMS collection for it.

**After:**
```yaml
collections:
  - name: home
    label: Home Page
    files:
      - name: about
        label: Hero · About
        file: content/about.md
        fields:
          - {label: Hero Copy, name: body, widget: markdown}
```

### Rule 3 — The CMS schema must expose ALL frontmatter fields

If a content file has frontmatter fields that are absent from the CMS schema, Sveltia (and Decap/Netlify CMS) will silently strip those fields on the next save.

**The fix for `about.md`:** Since its frontmatter fields (`title`, `slug`, `order`, `description`, `layout`) were vestigial and not used by the build script, the cleanest resolution was to **remove the frontmatter entirely** — leaving a plain body-only file. Now the CMS schema (body only) exactly matches the file, with no risk of data loss.

If frontmatter fields ARE used by the build, they must all appear in the CMS schema. Use `widget: hidden` for fields the editor should not change but the build needs to preserve:
```yaml
- {label: Layout, name: layout, widget: hidden, default: home}
```

### Rule 4 — Field hints must accurately describe WHERE content appears

A misleading hint causes editors to fill in the wrong field or misunderstand the site's content model.

**Before (wrong):**
```yaml
- label: Description
  name: description
  hint: >
    One-sentence summary. Appears in the TOC dot-leader row, the thesis page
    as the opening paragraph, SEO meta description, and llms.txt.
```

**After (correct):**
```yaml
- label: Description
  name: description
  hint: >
    One-sentence summary. Appears as the dot-leader description in the home
    page TOC and as the SEO meta description on the detail page.
    It does NOT render as visible body text on the detail page — use Body for that.
```

### Rule 5 — Organize settings by concern, with hints on every field

Once a settings file grows beyond ~4 fields, organize with YAML comments as section separators and add `hint:` to every field. Editors need to understand where each value appears without reading the source code.

```yaml
fields:
  # ---- Identity -------------------------------------------------------
  - {label: Full Name, name: full_name, widget: string,
     hint: "Legal name — used in copyright and JSON-LD schema."}
  # ---- Section Headings -----------------------------------------------
  - {label: Theses Section Heading, name: section_theses, widget: string,
     default: "Theses",
     hint: "The h3 heading above the thesis index on the home page."}
```

---

## Why This Matters

An incomplete CMS schema creates a two-tier content model: some strings are self-service, others require a developer and a deploy. This defeats the purpose of a headless CMS.

Beyond the UX cost, there are three concrete failure modes:

1. **Silent data loss** — fields absent from the schema are stripped on the next CMS save, destroying data with no warning
2. **Ghost content files** — files in `content/` that the build reads but the CMS doesn't know about are invisible to editors; changes made via CMS to *other* files won't affect them
3. **Editor confusion** — misleading hints cause editors to fill in the wrong field, leading to content appearing in the wrong place or not at all

---

## When to Apply

- **Every time a new string is added to a build template**: ask "could an editor ever want to change this?" If yes, move it to a content file and add the CMS field before committing.
- **Every time a new file is added to `content/`**: immediately add it to the CMS schema.
- **When writing CMS hints**: trace exactly where the field value appears in the rendered HTML; do not summarise from memory.
- **When removing frontmatter fields**: check whether the CMS schema still matches the file exactly.

---

## Complete Content Map for This Site

See `CONTENT_ARCHITECTURE.md` for the authoritative field-by-field map of every visible element to its source file and CMS collection.

### Summary

| CMS Collection | File | What it controls |
|---|---|---|
| Home Page → Hero · About | `content/about.md` | Hero intro on `index.html` |
| Theses | `content/theses/*.md` | Home TOC rows + every `thesis-NN-*.html` detail page |
| Settings → Site Settings | `content/settings/site.json` | All pages: masthead, nav, footer, section headings, newsletter, SEO |

---

## Related

- `CONTENT_ARCHITECTURE.md` — complete field-by-field content map
- `admin/config.template.yml` — CMS schema (source of truth; `admin/config.yml` is generated at build time)
- `content/settings/site.json` — all site-wide settings
- `scripts/build.js` — build template; grep this for string literals when auditing
- `AGENTS.md` — CMS section documents collections, field mapping, and env var requirements
