# Skill — Edit Home Sections & Newsletter

**When to use:** changing the home page's section headings, sub-labels, the
newsletter copy/CTA, the blog intro statement, or the logo.
**Tier:** 2 (content). The file is `content/home.json`.

## Steps

1. **Open** `content/home.json`.
2. **Edit the relevant key** (all keys have build-side fallbacks, so a missing
   key degrades gracefully — but only keys present in the CMS schema are editable
   in `/admin`):

   | Key | Controls |
   |---|---|
   | `logo_image`, `logo_alt` | Logo between hero and theses |
   | `section_theses`, `section_theses_label` | "Theses" heading + mono sub-label |
   | `section_writing`, `section_writing_label`, `section_writing_intro` | "Writing" heading, label, optional intro |
   | `blog_intro` | Publication statement at the top of `/blog/` |
   | `section_newsletter`, `section_newsletter_label` | "Newsletter" heading + sub-label |
   | `newsletter_body` | Paragraph above the subscribe link |
   | `newsletter_cta` | Subscribe link text |

3. **Keep valid JSON.**
4. **Build & verify** (`build-and-verify.md`). Confirm the new copy in
   `dist/index.html` (and `dist/blog/index.html` for `blog_intro`).

## Note

The newsletter *subscribe URL* itself is not here — it comes from
`settings.substack` in `content/settings/site.json`. Edit that via
`edit-site-settings.md`.
