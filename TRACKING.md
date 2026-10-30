# Tracking

The site sends two events to PostHog and nothing else. The pattern mirrors the aves-medellin thesis site (GDPR-first, events counted only when visible).

| Event | When | Properties |
|---|---|---|
| `page_opened` | the page is on screen (sent once, on load if visible, else on first show) | `path`, `visit_id` |
| `visit_ended` | the page is hidden or closed; sent again on every hide with the running total (analyse the largest `visible_seconds` per `visit_id`) | `path`, `visit_id`, `visible_seconds` |

PostHog stamps each event with its arrival time. Every event carries `$process_person_profile: false` (no person profile) and `$geoip_disable: true` (no location lookup), and a random single-use `distinct_id`. `visit_id` lives in memory for the visit only and groups one visit's events.

Nothing else is captured: no autocapture, heatmaps, session replay or web vitals, no browser, OS, device, screen size, referrer or UTM tags. There is no PostHog library on the page: `scripts/build.js` emits a small inline script that posts the events itself, so nothing switched on in PostHog can add to what the page sends. Nothing is stored on the visitor's device: no cookies, no localStorage, no sessionStorage.

**No IP and no location.** The page sends to `/ingest` on this site; vercel.json rewrites that path to `https://eu.i.posthog.com`, so PostHog sees Vercel's server, never the visitor. The project lives on PostHog EU Cloud (event data stored in the EU). Project settings (applied 30 Oct 2026, project 327929): discard client IP data on, GeoIP transformation paused, timezone America/Bogota.

**Key.** `PUBLIC_POSTHOG_KEY` at build time; without it the site builds with analytics off and no script is emitted at all. The key is PostHog's public write-only ingest key (same exposure class as the GA4 ID it replaced). Key and rewrite host are both EU on purpose: PostHog answers 200 to a key sent to the wrong region and drops its events.

GA4 was removed in the same change (previously a default-baked `G-4E1LTHSFX8` in build.js).
