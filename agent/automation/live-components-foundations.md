# Automation Foundations — Live Components

**Purpose:** lay the groundwork for the automation flows Alejandro plans to wire
into the Research agent — flows that add *live* components to the site (e.g. a
"now reading," a research feed, latest-essay cards, a dynamically updated
reading list) without breaking the CMS or the build.

This document is a **design contract for future work**, not an implemented
feature. It defines the safe pattern so that when automation arrives, it slots in
cleanly.

---

## The core constraint

The site is **statically built**. There is no server at request time — Vercel
serves pre-rendered files from `dist/`. So "live" here means *rebuilt on a
trigger*, not *fetched in the browser at view time* (unless you deliberately add
client-side fetch). Every automation pattern below respects the existing
`content/ → build.js → dist/` flow rather than fighting it.

## Three viable patterns (in order of preference)

### Pattern A — Data file in `content/`, rendered at build time (preferred)

The automation writes a **data file** into `content/` (e.g.
`content/live/now-reading.json`), then triggers a rebuild. `build.js` reads it
and renders a component. This keeps a single source of truth, stays inside the
existing pipeline, and the output is cached/CDN-friendly.

```
automation flow ──writes──► content/live/<feed>.json
                                   │
                          triggers npm run build (or a push to main)
                                   │
                       build.js renders the component into dist/
```

**Rules for this pattern:**
- Put machine-generated data under a dedicated dir, e.g. `content/live/`, so it
  is visibly distinct from human-edited content.
- **Decide CMS visibility deliberately.** If a file lives in `content/` but is
  *not* in the CMS schema, it is invisible to `/admin` — which is *correct* for
  machine-owned data Alejandro shouldn't hand-edit. Document that choice. (It
  does not risk the silent-strip trap as long as the CMS never opens that file.)
- Adding the `build.js` read path and the render is a **Tier 1** change (propose
  via the forcing function in `../protocols/PORTFOLIO-WRITE-GUARD-01.md`), done
  once. After that, the automation only writes the data file (Tier 2) and
  rebuilds — no further Tier 1 writes.

### Pattern B — Client-side fetch of `/api/content.json` or an external API

For genuinely real-time data, add a small progressive-enhancement script that
fetches JSON in the browser and hydrates a placeholder. The build already emits a
CORS-enabled `/api/content.json`; an external automation service could publish a
similar JSON endpoint the page fetches.

- Use only as progressive enhancement: render a sensible static fallback at build
  time, then enhance. Never make core content depend on client JS.
- Adding the script is a Tier 1 change to `build.js`/templates.

### Pattern C — Build-time fetch from an external source

`build.js` (or a new prebuild step) fetches from an API during the build and
renders the result. "Live" = as fresh as the last build/trigger.

- Add it as a **separate prebuild script**, not buried inside `build.js`, so a
  fetch failure can fail gracefully (use cached/last-known data; never fail the
  whole deploy on a flaky upstream).
- New script + wiring = Tier 1.

---

## Non-negotiables for any live component

1. **Never bypass the source-of-truth model.** No automation writes to `dist/`
   directly. It writes to `content/` (or an external API) and triggers a build.
2. **Fail gracefully.** A live component that can't load its data must degrade to
   a static fallback or render nothing — it must never break the page or fail the
   build. Mirror the existing `|| fallback` discipline in `build.js`.
3. **Respect the validator.** If a live data file is required for the build,
   extend `validate-content.js` to check it (Tier 1) so a malformed automation
   write fails fast and loud at build time, not silently in production.
4. **Keep machine data out of the human CMS** unless Alejandro should edit it.
   Decide and document per feed.
5. **The trigger is a rebuild.** A new build is the deploy. Wire the automation
   to either (a) commit the data file to `main` (CMS-style) or (b) open a PR for
   review. Direct production writes follow the same `main`-auto-deploys rule as
   everything else — see `../guidelines/contribution-workflow.md`.

---

## Recommended first build-out (when Alejandro green-lights it)

A minimal, safe reference implementation to validate the pattern end-to-end:

1. Create `content/live/` and a sample `now-reading.json`.
2. Add a `loadLive()` reader + a small render block in `build.js` (Tier 1, one
   proposal).
3. Add an optional `validate-content.js` check for the file shape (Tier 1).
4. Leave it **out** of the CMS schema (machine-owned) and document that.
5. The Research agent's automation then only ever: writes
   `content/live/now-reading.json` → triggers build. Steady-state is pure
   Tier 2.

This gives a proven, low-blast-radius template every subsequent live component
can copy — the whole point of establishing the foundation now.

---

## Cross-reference: the research brain

This complements, and does not replace, the syndication thinking already in the
brain (`docs/plans/syndication-spec.md`, `docs/plans/2026-05-31-003-feat-blog-syndication-agent-native-plan.md`).
Those cover *content out* (Obsidian → Substack/Paragraph/Ghost). This covers
*data in* (automation → live components on kairon.xyz). Both share one rule: a
single canonical source, derivatives generated, nothing hand-edited downstream.
