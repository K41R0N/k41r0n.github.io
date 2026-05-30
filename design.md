# Design System — Kairon Portfolio

Adapted from the editorial layout (K41R0N / kairon-portfolio), which itself follows the layout grammar of kairon.xyz. This document is the living reference for design decisions in this project.

---

## Palette

| Token | Value | Role |
|-------|-------|------|
| `--background` | `#F5F5F5` | Warm off-white page canvas |
| `--color-black` | `#000` | Primary ink |
| `--crimson` | `#bf150f` | THE accent — links, wordmark accent, rules |
| `--cobalt` | alias of `--crimson` | compat alias used across CSS |
| `--text-muted` | `oklch(44.6% .03 256)` | Secondary text, labels |
| `--text-faint` | `oklch(55.1% .027 264)` | Captions, mono labels |

One accent colour only. Never use more than one non-neutral colour at a time.

---

## Typography

| Role | Font | Token |
|------|------|-------|
| Wordmark / display | Kyrios (variable sans, self-hosted) | `--font-display` |
| Body / editorial | Merriweather (serif, Google Fonts) | `--font-body` |
| Technical labels | System monospace | `--font-mono` |
| Logotype glyph | Kairon (custom, self-hosted) | `--font-kairon` |

**Rules:**
- Wordmark is the only element that uses Kyrios at heading scale
- Section headings (`h3`) use `--font-body` (Merriweather) via `overrides.css` — subordinate to the wordmark
- Mono voice is used for: nav, labels, eyebrows, captions, TOC page numbers
- Drop cap fires only when the first word is 3+ characters (`applyDropcap()` guard)

---

## Layout Grammar

The Sky / kairon.xyz layout grammar, applied verbatim. CSS lives in `src/css/` — source CSS files are copied as-is; Kairon-specific deviations go in `src/css/overrides.css`.

### Home page (`ms-main`)

```
masthead
  wordmark (left)  |  live-metrics grid (right) — social links as label/value columns
─────────────────────────────────────
intro-flow         — multi-column justified prose, dropcap on first paragraph
─────────────────────────────────────
[kairon-logo.svg]  — centred mark between hero and index
─────────────────────────────────────
sec-head + toc-ms  — Theses index with dot-leader rows
sec-head + intro-flow — Writing links
sec-head + intro-flow — Newsletter
footer-ms          — · · ·  credits  dot-band
```

### Thesis detail pages (`chapter-page`)

```
site-nav           — ← Kairon | Thesis NN / Title
rule-dotted
chapter-nav        — all thesis links, current highlighted
article.article    — margin-label · eyebrow · h1 · dropcap body · margin-note · links
[next thesis link]
chapter-marker
footer-ms
```

---

## CSS Architecture

| File | Origin | Purpose |
|------|--------|---------|
| `src/css/tokens.css` | Kairon | Design tokens — swap blue → crimson throughout |
| `src/css/fonts.css` | Kairon | Font face declarations |
| `src/css/base.css` | source CSS | Reset, editorial type, hairline rules, dropcap, margin note |
| `src/css/layout.css` | source CSS | ms-main, masthead, intro-flow, sec-head, toc-ms, footer-ms |
| `src/css/components.css` | source CSS | wordmark, blueprint figures, TOC, signup, rotated margin label |
| `src/css/animations.css` | source CSS | Blueprint figure entrance animations |
| `src/css/overrides.css` | Kairon | Kairon-specific deviations only — keep minimal |

**Rule:** Never edit the source CSS files. Put all project-specific overrides in `overrides.css`.

---

## Key Components

### Masthead metrics grid (`.live-metrics`)
Three-column grid. In the Sky original: live protocol data. In this portfolio: social platform links.
- Label row: platform name in mono uppercase
- Value row: handle as a link, `--text-4xl` size

### Dot-leader TOC (`.toc-ms` / `.toc-row`)
```
group-title (linked chapter/thesis title)
  toc-row: [title text] .... [page/thesis number]
```
The dots (`span.dots`) use a CSS radial-gradient background — no actual dot characters.

### Section heading (`.sec-head`)
```
[h3 title]  ────────── full rule ──────────  [MONO LABEL]
```
Grid: `auto 1fr auto`. The rule is `<div class="rule-solid">` not an `<hr>`.

### Chapter marker (`.chapter-marker`)
```
- - - - - [MONO LABEL] - - - - -
```
Centred text flanked by dashed rules via CSS `::before`/`::after`.

### Footer (`.footer-ms`)
```
· · ·
[tagline]
[email]
© year name
[dot band — radial-gradient repeat, 15% opacity]
```

### Rotated margin label (`.margin-label`)
```css
writing-mode: vertical-rl;
transform: rotate(180deg);
```
10px mono uppercase. Appears in thesis `article.article` column 1 (hidden on mobile).

---

## Spacing Scale

Derived from Tailwind v4. Base unit `--spacing: .25rem`.

| Token | Value |
|-------|-------|
| Section gaps | `mt-64` = `16rem` between major sections |
| Heading margin | `mt-32` = `8rem` before sec-head |
| Chapter spacing | `mt-24` = `6rem` |
| Paragraph rhythm | `mb-8` = `2rem` |

---

## Content Architecture

Source of truth is `content/`. Build script (`scripts/build.js`) generates `dist/`.

```
content/settings/site.json   → site metadata, social links, email
content/about.md             → hero intro text
content/theses/*.md          → thesis cards (title, description, body, links)
```

Frontmatter schema for theses:
```yaml
title: string       # required
slug: string        # required, kebab-case
order: integer      # required, 1-based
description: string # required, one sentence — feeds SEO + llms.txt
links: []           # optional, [{label, title, url}]
```

---

## Machine-Readable Endpoints

Every build outputs:

| File | Purpose |
|------|---------|
| `/llms.txt` | AI agent guidance (llmstxt.org) |
| `/llms-full.txt` | Full content dump |
| `/api/content.json` | Structured JSON, CORS headers via `vercel.json` |
| `/sitemap.xml` | Search engine sitemap |
| `/feed.xml` | RSS 2.0 |
| `/robots.txt` | Explicit allowances for GPTBot, ClaudeBot, PerplexityBot, etc. |

---

## Anti-Patterns (don't introduce these)

- No gradients, glow effects, glassmorphism
- No additional accent colours beyond crimson
- No cards unless they are interactive units
- No inline styles beyond what the build template already uses — put new rules in `overrides.css`
- No changes to the source CSS CSS files — patch via `overrides.css`
- Never edit `dist/` directly — it is build output
