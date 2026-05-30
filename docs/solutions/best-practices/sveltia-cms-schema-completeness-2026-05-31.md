---
title: "Complete CMS Schema Coverage: No Hardcoded Copy in Build Templates"
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
  - Site copy (wordmark, hero text, newsletter body/CTA) is hardcoded in build.js
  - Content editors cannot update strings without touching source code and redeploying
  - CMS collections exist but do not expose all visible-copy fields
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
---

# Complete CMS Schema Coverage: No Hardcoded Copy in Build Templates

## Context

Static site generators that use a build script to assemble HTML from content files create a specific failure mode: strings that *look* like content get written directly into template literals, bypassing the CMS entirely.

This happened in this portfolio — the CMS schema covered the main `theses` collection and minimal `settings`, but left several pieces of copy hardcoded in `scripts/build.js`:

- `"Alejandro<br>Arango"` — wordmark display name
- `"I'm in tech. I care about craftsmanship..."` — hero copy fallback
- `"Insights on digital creation..."` — newsletter body
- `"Subscribe on Substack →"` — newsletter CTA

`content/about.md` also existed on disk but was entirely absent from the CMS schema, making the hero copy unreachable from the admin UI despite being a content file.

---

## Guidance

**The invariant**: every string that renders as visible text and was written by a human belongs in a content file, with a corresponding CMS field. Hardcoded strings in build templates are a CMS coverage gap, not a code simplification.

### Step 1 — Audit for gaps

```bash
# Files the build script reads from content/
grep -o "content/[^'\"]*" scripts/build.js | sort -u

# Files declared in the CMS schema
grep "^\s*file:" admin/config.template.yml | sort -u

# Diff the two lists → any file in build but absent from schema is a gap
```

Also grep for string literals in template literals that contain visible copy:
```bash
grep -n '"[A-Z][a-z].*"' scripts/build.js   # sentences and names
```

### Step 2 — Move strings to content

Add fields to the relevant `content/settings/*.json` file:

```json
// content/settings/site.json — before
{
  "tagline": "Creative Technologist..."
}

// content/settings/site.json — after
{
  "tagline": "Creative Technologist...",
  "wordmark_line1": "Alejandro",
  "wordmark_line2": "Arango",
  "newsletter_body": "Insights on digital creation...",
  "newsletter_cta": "Subscribe on Substack →"
}
```

### Step 3 — Wire build.js to read from content

```javascript
// Before — hardcoded wordmark
<p class="wordmark">Alejandro<br>Arango</p>

// After — from settings (with escHtml required for JSON-sourced strings)
<p class="wordmark">${escHtml(settings.wordmark_line1)}<br>${escHtml(settings.wordmark_line2)}</p>
```

```javascript
// Before — hardcoded newsletter block
<p>Insights on digital creation, technology...</p>
<p><a href="${url}">Subscribe on Substack →</a></p>

// After — from settings
<p>${escHtml(settings.newsletter_body)}</p>
<p><a href="${escHtml(settings.substack)}">${escHtml(settings.newsletter_cta)}</a></p>
```

> **Note:** `escHtml()` is mandatory for any string sourced from JSON/markdown. CMS editors can type `<`, `>`, `&`, or `"` — without escaping, the next CMS save corrupts the HTML output.

### Step 4 — Add orphaned content files to the CMS schema

```yaml
# Before: content/about.md exists on disk, no CMS entry

# After: home collection added
collections:
  - name: home
    label: Home Page
    files:
      - name: about
        label: Hero · About
        file: content/about.md
        fields:
          - label: Hero Copy
            name: body
            widget: markdown
```

### Step 5 — Organise settings fields by concern

Once a `files` collection grows beyond ~4 fields, group them with labels so the admin UI stays navigable:

```yaml
- name: settings
  files:
    - name: site
      file: content/settings/site.json
      fields:
        # ---- Identity ----
        - {label: Full Name, name: full_name, widget: string}
        - {label: Wordmark Line 1, name: wordmark_line1, widget: string, hint: "e.g. Alejandro"}
        - {label: Wordmark Line 2, name: wordmark_line2, widget: string, hint: "e.g. Arango"}
        - {label: Handle, name: author_handle, widget: string}
        - {label: Tagline, name: tagline, widget: string}
        # ---- Social ----
        - {label: GitHub URL, name: github, widget: string}
        - {label: Substack URL, name: substack, widget: string}
        # ---- Newsletter ----
        - {label: Newsletter Body, name: newsletter_body, widget: text}
        - {label: Newsletter CTA, name: newsletter_cta, widget: string}
        # ---- Footer ----
        - {label: Footer Text, name: footer_text, widget: string}
```

Use `hint:` on every field — it appears below the input in the Sveltia UI and saves a developer lookup for every future edit.

---

## Why This Matters

A CMS schema that does not cover all editable copy creates a two-tier content model: some strings are self-service, others require a developer and a deploy. This defeats the purpose of a headless CMS and becomes a maintenance liability — the next developer to read `build.js` won't know which string literals are "permanent" and which are "content that got stranded."

It also creates an implicit gatekeeper: every copy change, however small (a newsletter CTA tweak, a tagline update), requires a code PR, a review, and a Vercel build.

---

## When to Apply

- **Every time a new string is added to a build template**: ask "could an editor ever want to change this?" If yes, move it to a content file and add the CMS field before committing.
- **When creating a new file under `content/`**: immediately add it to the CMS schema — never leave a content file orphaned in the schema.
- **During a CMS schema review**: diff build-script reads vs schema declarations (see audit command above).
- **When a settings file grows**: organize fields into sections with `hint:` annotations.

---

## Examples

**Three gaps in one build script — and the fix**

```javascript
// Before — three hardcoded strings, none reachable from CMS
nav  += `<p class="wordmark">Alejandro<br>Arango</p>`;
hero += `<p>I'm in tech. I care about craftsmanship.</p>`;
nwsl += `<p>Insights on digital creation...</p>
         <p><a href="${url}">Subscribe on Substack →</a></p>`;

// After — all sourced from settings loaded at build time
nav  += `<p class="wordmark">${escHtml(s.wordmark_line1)}<br>${escHtml(s.wordmark_line2)}</p>`;
hero += applyDropcap(marked.parse(about.body));
nwsl += `<p>${escHtml(s.newsletter_body)}</p>
         <p><a href="${escHtml(s.substack)}">${escHtml(s.newsletter_cta)}</a></p>`;
```

---

## Related

- `admin/config.template.yml` — the CMS schema template (source of truth; `admin/config.yml` is generated from this at build time)
- `content/settings/site.json` — all site-wide settings
- `scripts/build.js` — the build template; grep this for string literals when auditing
- `scripts/generate-cms-config.js` — generates `admin/config.yml` from the template using env vars
- `AGENTS.md` — CMS section documents the collection structure and env var requirements
