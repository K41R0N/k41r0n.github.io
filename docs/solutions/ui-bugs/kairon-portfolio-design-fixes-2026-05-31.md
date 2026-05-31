---
title: Portfolio UI and Layout Fixes
date: 2026-05-31
category: ui-bugs
module: UI
problem_type: ui_bug
component: frontend
symptoms:
  - Double numbering in Theses and Projects lists
  - Double horizontal lines below section headers
  - Poor mobile responsiveness in masthead and logo
  - Markdown images failing to render inside margin note blockquotes
root_cause: css_conflict
resolution_type: code_fix
severity: low
tags: [css, layout, responsive, markdown, marked]
---

# Portfolio UI and Layout Fixes

## Problem
Several UI components in the Kairon portfolio had layout glitches. These included double numbering on ordered lists, a double horizontal rule below headers, uncentered elements on mobile, and markdown formatting errors inside blockquotes.

## Symptoms
- Ordered lists displaying both `01 ·` custom label and native `1.` browser list item numbering.
- Double horizontal lines separating content headers and blocks, specifically in the `Writing` section and the featured blog post.
- The 3-faced logo floating uncentered on mobile devices.
- Images inside `> **Note:**` margin notes failing to render properly because they weren't being correctly passed through the Markdown parser.
- Navigation link colors in the blog header lost their custom styling (crimson) due to inheriting parent `.site-nav` CSS constraints.

## What Didn't Work
- Using regex to capture HTML directly for blockquotes led to markdown elements (like images or links) becoming literal string text.
- Overloading the `.site-nav` class with extra flex attributes disrupted the default text styling of nested links.

## Solution
1. Stripped `list-style: decimal` and `list-style: disc` from the corresponding `.toc-ms` classes in `layout.css`.
2. Tracked down and removed the overlapping `border-bottom` property from `.blog-featured` in `overrides.css` and adjusted `.site-nav` borders.
3. Adjusted the `.hero-logo` container using `align-self: center` for mobile devices and `align-self: flex-end` for desktop.
4. Refactored the `transformBody` function in `scripts/build.js` to pipe captured blockquote strings through `marked.parse(content, { async: false })` before wrapping them in the `<aside class="margin-note">`.
5. Added a specific CSS constraint `margin-note img { width: 100%; border-radius: 4px; }` in `base.css` to prevent margin images from breaking the layout.
6. Detached the `.live-metrics` component from the `.site-nav` wrapper in the blog template to allow it to retain its native, correct color scheme (`var(--link-color)`).

## Why This Works
- Removing the native list styles prevents browser engines from enforcing arbitrary padding and bullets, deferring entirely to the custom editorial styling.
- Parsing the captured markdown note block before wrapping it in HTML ensures `marked` applies image and link parsing appropriately.

## Prevention
- When applying nested CSS classes for structure (`border-bottom`, etc.), avoid applying them to adjacent stacked components. Use targeted gaps instead.
- Use explicit `@media (max-width: 48rem)` breakpoints for small mobile UI behaviors. 
- Ensure any regex-based text extraction parses the internal content via the Markdown renderer if the content is expected to support Markdown features.

## Related Issues
- None