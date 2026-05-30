---
title: "fix: Resolve homepage design critique findings"
type: fix
status: completed
date: 2026-05-31
---

# fix: Resolve homepage design critique findings

## Overview

Five targeted fixes to the portfolio homepage and one CSS override, all identified in the design critique session. No content changes — everything is structural or presentational.

## Problem Frame

The critique scored the design 26/40 (Developing). The layout skeleton is correct but several assembly errors prevent it from reading cleanly: a broken dropcap, a duplicated tagline, semantically broken masthead labels, social links stranded in body copy, and section headings that compete with the wordmark.

## Requirements Trace

- R1. Dropcap must not split contractions or single-letter words
- R2. Tagline must appear exactly once in the masthead area
- R3. Masthead metrics panel must use labels that parse as key → value pairs
- R4. Social links must live in the masthead/nav — not in body prose
- R5. Section headings (`.sec-head h3`) must be visually subordinate to the wordmark

## Scope Boundaries

- No changes to `content/` files — the user's copy is off-limits
- No changes to thesis detail pages — only the home page is in scope
- No layout restructuring beyond what is stated — only the five issues listed

## Context & Research

### Relevant Code and Patterns

- `scripts/build.js` — `renderHomePage()` generates the home page HTML; `transformBody()` applies the dropcap
- `src/css/layout.css` (source CSS) — `.sec-head h3` rule at line 99: `font-family: var(--font-serif)`
- `src/css/tokens.css` — token chain: `--font-serif → --font-display → "Kyrios"` (display font); `--font-body → "Merriweather"` (editorial serif)
- `src/css/base.css` (source CSS) — `h1–h4` base rule at line 96: `font-family: var(--font-serif)` — the section heading override must beat this specificity
- Sky reference `dist/index.html` — the masthead's right panel uses `class="live-metrics"` with three `<div>` children each containing a `.metric-label` and `.metric-value`

### Key Findings

- The dropcap in `transformBody()` (`build.js:116`) blindly replaces the first `<p>` open tag with `<p class="dropcap">`. CSS `::first-letter` then floats the letter `I` from `I'm`, splitting the word visually.
- The same blind dropcap is applied in `renderHomePage()` at line 264 for the `aboutHtml`. Since the about text starts with "I'm", this is the same bug in both paths.
- The tagline is emitted at `build.js:308` as a `<p class="tagline">` directly below the wordmark, and simultaneously decomposed across the two left metrics columns (`Creative Technologist` / `Daylighter`). Same text, twice.
- The masthead metrics labels at `build.js:271–283` use `ROLE`, `MARTECH`, `CONTACT`. "MARTECH" is the industry, not a label for "Daylighter" — it's a value masquerading as a key.
- Social links are emitted inside the `intro-flow` `<section>` at `build.js:315–321` as a `<ul>` mixed into the bio text. They belong in the masthead.
- `.sec-head h3` uses `var(--font-serif)` which resolves to `"Kyrios"` — the same display font as the wordmark. At `var(--text-4xl)` the section headings visually compete with the wordmark rather than reading as subordinate structure.

## Key Technical Decisions

- **Dropcap guard via regex lookahead, not content inspection:** Replace `/<p>/` with `/<p class="dropcap">` only when the first word has 3+ characters. Uses `/<p>([A-Za-z]{3})/` to match before applying the class. Avoids needing to parse the markdown content before HTML conversion.
- **Section heading font override via `src/css/overrides.css`:** Rather than modifying the Sky `layout.css` verbatim copy, add a thin `overrides.css` that targets `.sec-head h3` with `font-family: var(--font-body)`. This isolates Kairon-specific deviations from the source CSS files, making future Sky upstream diffs easier to track.
- **Masthead metrics restructure stays in `renderHomePage()`:** The three metric slots become: `CREATIVE TECHNOLOGIST` (label) / name (value) · `MARTECH DAYLIGHTER` (label) / tagline (value) · `CONTACT` (label) / email link (value). This preserves the three-column structure while making each label a genuine descriptor.
- **Social links move to masthead header:** The `<ul class="social-links">` moves inside the `<header class="masthead">` block, beneath the metrics panel. Renders on the same visual level as the contact info. Removed from `intro-flow` entirely.

## Open Questions

### Resolved During Planning

- *Should the about text dropcap be removed entirely, or guarded?* Guarded — the dropcap is correct for thesis pages (where text starts with full words). On the home page, the guard catches "I'm" and simply renders it as a normal paragraph.
- *Should `layout.css` be modified directly?* No — keep Sky CSS verbatim; use `overrides.css` as a shim.
- *Where do the social links live in the masthead?* Below the metrics panel, inside `<header class="masthead">`, as a flat row using the existing `.social-links` CSS.

### Deferred to Implementation

- Exact `overrides.css` specificity selector needed to beat `layout.css` line 99 — test during implementation by inspecting computed styles.

## Implementation Units

---

- [ ] **Unit 1: Guard dropcap against single-letter and short first words**

**Goal:** Prevent `::first-letter` from splitting contractions like "I'm" or articles like "A"

**Requirements:** R1

**Dependencies:** None

**Files:**
- Modify: `scripts/build.js`

**Approach:**
- In `transformBody()` (line 116), change the blind `/<p>/` replacement to only apply `class="dropcap"` when the first word in the paragraph is 3+ characters long
- Pattern: replace first `<p>` with `<p class="dropcap">` only when followed by 3+ word characters
- Apply the same guard to the `aboutHtml` path in `renderHomePage()` (line 264)

**Patterns to follow:**
- Existing regex in `transformBody()` (lines 108–116) for the transform style

**Test scenarios:**
- Happy path: paragraph starting with "There's" → dropcap renders on "T"
- Edge case: paragraph starting with "I'm" → no dropcap, normal paragraph
- Edge case: paragraph starting with "A " → no dropcap
- Edge case: paragraph starting with "The" → dropcap renders on "T"

**Verification:**
- Home page intro section renders "I'm in tech." without a floating large "I"
- Thesis pages with body starting with full words still render a dropcap

---

- [ ] **Unit 2: Remove duplicate tagline from under the wordmark**

**Goal:** Eliminate the tagline that repeats information already in the metrics panel

**Requirements:** R2

**Dependencies:** None

**Files:**
- Modify: `scripts/build.js`

**Approach:**
- Delete the `<p class="tagline" ...>` line at `build.js:308`
- The metrics panel communicates the same information — no replacement needed

**Test scenarios:**
- Happy path: rebuilt `index.html` contains `class="tagline"` zero times
- Regression: metrics panel still renders all three columns

**Verification:**
- `dist/index.html` does not contain `class="tagline"`
- Masthead still renders correctly without the deleted line

---

- [ ] **Unit 3: Fix masthead metrics labels and move social links into masthead**

**Goal:** Make the metrics panel semantically correct; relocate social links from body prose to masthead

**Requirements:** R3, R4

**Dependencies:** Unit 2

**Files:**
- Modify: `scripts/build.js`

**Approach:**

Metrics panel — replace the three slots with:
1. Label: `Creative Technologist` | Value: field tag (mono, small, muted)
2. Label: `Martech Daylighter` | Value: role tag (mono, small, muted)
3. Label: `<live-dot> Contact` | Value: email link

This makes each slot a genuine label→value pair rather than an industry term standing in as a category.

Social links — move the `<ul class="social-links">` from inside the `intro-flow` section into the `<header class="masthead">` block, as a third row beneath the metrics panel. Use the existing `.social-links` CSS (a flex row of mono uppercase links).

**Patterns to follow:**
- Existing `.live-metrics` / `.metric-label` / `.metric-value` structure in `dist/index.html` (Sky reference, lines 113–127)
- Existing `navLinks` list construction already in `renderHomePage()`

**Test scenarios:**
- Happy path: metrics panel renders three columns with readable label/value pairs
- Happy path: social links appear in masthead, not inside `intro-flow`
- Regression: `intro-flow` section no longer contains the social link `<ul>`

**Verification:**
- In `dist/index.html`, `<ul class="social-links">` appears inside `<header class="masthead">`, not inside `<section class="intro-flow">`
- Each metric column has a `metric-label` element whose text is a genuine descriptor, not an industry category used as a key

---

- [ ] **Unit 4: Add `overrides.css` — section heading font override**

**Goal:** Make `.sec-head h3` use `--font-body` (Merriweather) so section headings are visually subordinate to the wordmark

**Requirements:** R5

**Dependencies:** None (CSS only, no build.js changes)

**Files:**
- Create: `src/css/overrides.css`
- Modify: `scripts/build.js` — add `overrides.css` to the `CSS_LINKS` constant

**Approach:**
- Create `src/css/overrides.css` as a thin shim for Kairon-specific deviations from the source CSS CSS
- Add one rule: `.sec-head h3 { font-family: var(--font-body); }` — Merriweather serif provides clear visual hierarchy below the Kyrios wordmark
- Add `<link rel="stylesheet" href="css/overrides.css">` as the last CSS link in `CSS_LINKS` (must load after `layout.css` to win specificity)

**Patterns to follow:**
- Token usage in `src/css/tokens.css` — `--font-body: "Merriweather", "Times New Roman", serif`

**Test scenarios:**
- Happy path: "Theses", "Writing", "Newsletter" section headings render in Merriweather serif
- Regression: `.sec-head h3` specificity check — the override must beat `layout.css` line 99 (`font-family: var(--font-serif)`)

**Verification:**
- Section headings visually read as subordinate editorial labels rather than display type competing with the wordmark
- `dist/css/overrides.css` exists in the build output

---

- [ ] **Unit 5: Rebuild and verify**

**Goal:** Full build confirming all fixes land together cleanly

**Requirements:** R1–R5

**Dependencies:** Units 1–4

**Files:**
- No file changes — rebuild and visual check only

**Approach:**
- Run `npm run build` — validation + build must pass clean
- Serve `dist/` and check the five fixed points visually

**Test scenarios:**
- Build passes with zero errors
- `dist/index.html` contains `overrides.css` link
- Dropcap absent from "I'm in tech" paragraph
- No `class="tagline"` in `dist/index.html`
- Social links inside masthead header
- Section headings visibly different from the wordmark

**Verification:**
- `npm run build` exits 0
- Visual check confirms all five critique issues resolved

---

## System-Wide Impact

- **Thesis detail pages:** Units 1 guards the dropcap in `transformBody()` — thesis pages with body text starting with full words are unaffected
- **CSS:** `overrides.css` only affects `.sec-head h3`; no other selectors touched
- **LLM/SEO endpoints:** No changes to `llms.txt`, `sitemap.xml`, `feed.xml`, `robots.txt`, or `api/content.json`
- **Unchanged invariants:** TOC dot-leader structure, footer, all Sky layout classes, all thesis page layouts

## Risks & Dependencies

| Risk | Mitigation |
|------|------------|
| `overrides.css` specificity insufficient to beat `layout.css` | Load `overrides.css` last; if needed add `.ms-main .sec-head h3` to increase specificity |
| Dropcap regex misses edge cases in future thesis bodies | Guard only skips dropcap for ≤2 character words — thesis bodies starting with "The", "There's", etc. are unaffected |
