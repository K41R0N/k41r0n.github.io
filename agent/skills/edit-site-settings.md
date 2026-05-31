# Skill — Edit Site Settings

**When to use:** changing identity, social links, SEO text, footer, or
thesis-page labels — anything global that appears on every page.
**Tier:** 2 (content). The single file is `content/settings/site.json`.

## Steps

1. **Open** `content/settings/site.json`. It is a flat JSON object.
2. **Edit values only.** Keep all keys — and especially never delete a
   validator-required key:
   `title`, `full_name`, `description`, `author`, `email`, `github`, `substack`,
   `site_url`. (Note `author` is required *in addition to* `full_name`.)
3. **Keep it valid JSON.** Quotes, commas, no trailing comma. The build escapes
   these strings into HTML, so apostrophes/ampersands are safe to type literally.
4. **Build & verify** (`build-and-verify.md`). A settings change is global, so
   the new value should appear on multiple `dist/` pages:
   ```bash
   grep -rl "new value" dist/ | head
   ```

## Field → effect quick reference

(Full table in `../guidelines/content-schemas.md`.)

| Want to change… | Edit key |
|---|---|
| Display name in masthead | `wordmark_line1`, `wordmark_line2` |
| Alias shown in labels / nav | `author_handle` |
| Footer role line / hero fallback | `tagline` |
| Contact email | `email` |
| Social links | `github`, `substack`, `instagram` |
| Browser-tab title, RSS title, `←` nav | `title` |
| SEO meta description | `description` |
| Production URL | `site_url` |
| Thesis-page labels | `thesis_nav_label`, `thesis_links_heading`, `thesis_links_label`, `thesis_next_label` |

## Note

To add a setting that does **not** exist yet, a new JSON key is not enough —
`build.js` must read it and the CMS schema must expose it. Use
`add-configurable-field.md` (Tier 1) instead.
