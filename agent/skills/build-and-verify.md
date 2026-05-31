# Skill — Build and Verify

**When to use:** at the end of *every* content or code change, before reporting
or shipping. This is the verification gate referenced by every other skill.

## Steps

1. **Install deps** (first run in a fresh clone only):
   ```bash
   npm install
   ```
2. **Build:**
   ```bash
   npm run build
   ```
   This runs, in order: `generate-cms-config.js` → `validate-content.js` →
   `build.js`.
3. **Read the output for failure signals:**
   - Validator failure looks like `✗ <field> is required` followed by
     `Validation failed with N error(s).` and a non-zero exit. **Fix the content;
     do not bypass.**
   - A successful run ends with `Build complete → dist/`.
4. **Confirm the change reached `dist/`** (don't trust the log alone):
   ```bash
   grep -r "the new or changed string" dist/
   ```
   - New blog post → confirm `dist/blog/<slug>.html` exists and appears in
     `dist/blog/index.html` and `dist/feed.xml`.
   - New thesis → confirm `dist/thesis-NN-<slug>.html` exists and appears in
     `dist/index.html` and `dist/api/content.json`.
   - Settings change → `grep` the value across `dist/` (it should appear on
     multiple pages).
5. **Sanity-check the structured API** when you changed theses/posts:
   ```bash
   node -e "JSON.parse(require('fs').readFileSync('dist/api/content.json'))" && echo OK
   ```

## Pass criteria

- `npm run build` exits 0 and prints `Build complete → dist/`.
- The changed string/file is present in `dist/`.
- `dist/api/content.json` is valid JSON.

## If it fails

Stop. Report the exact validator/build output. Do not edit `dist/` to paper over
a source problem, and do not retry a different approach silently — the source
file is the only correct place to fix.
