# Proposal: voice harness lives inside the Kairon site repo

Status: layout and PR approved by Alejandro 2026-10-28. Not merged. Nothing has been pushed to K41R0N/k41r0n.github.io. This folder was built and tested in a throwaway copy of the repo.

## What he asked for
The engine lives inside the Kairon harness so the website is the harness: it speaks like him, knows his content, market and audience, and can be maintained without friction.

## Recommended layout: `agent/voice/` (no new top-level folder)

    agent/
      README.md, ORIENTATION.md, protocols/, guidelines/, skills/   (existing, untouched except 1 routing row)
      voice/                      NEW
        HARNESS.md                charter, approver, maturity MVH-0, tiers
        canon/                    voice-spec.md, do-dont.md, lexicon.md  (all Tier 2 = proposed)
        corpus/                   raw/ holdout/ excluded/  (frozen snapshots + provenance headers)
        routines/                 copy-draft.md (five passes), copy-review.md, blind-test.md
        registers/ thoughts/ refs/ drafts/ reports/ log/
        tools/                    stdlib Python: measure, check, verify
    content/  src/  admin/  scripts/  ...  (untouched)

Why here and not a new top-level folder:
- `PORTFOLIO-WRITE-GUARD-01` already lists "anything inside `agent/`, `docs/`" as Tier 2, free to edit. No guarded path (Tier 1) is touched, so no `PROPOSING PORTFOLIO WRITE` line is needed for the build, CMS schema, `vercel.json`, `package.json` or tokens.
- `agent/` is already where any agent learns how to contribute. Voice is part of "how to contribute copy here".
- Alternative B: a top-level `harness/` folder. Same tests would pass (the build reads only content/, src/, admin/). It is a bigger visible structural change and would sit next to build code. Not recommended, but it is his call.

## Tested before proposing (in a copy of the repo, nothing pushed)
- `npm run build` passes with `agent/voice/` added.
- `dist/` is identical to the baseline build except the generated-at timestamps in `api/content.json`, `llms-full.txt` and `feed.xml` (these also differ between two baseline builds).
- `admin/config.yml` is unchanged, so the Sveltia CMS schema is unaffected.
- Nothing from `agent/voice/` appears in `dist/` (the build copies only css, assets and admin).
- `tools/verify.py` runs in place and reproduces the same report: it reads `content/blog/` for the authenticity cross-check.

## Rules that make it safe to nest (already in HARNESS.md)
1. Drafts go to `agent/voice/drafts/`, never into `content/`. The repo's own record (`docs/solutions/workflow-issues/agent-copy-boundary-violation-2026-05-31.md`) says an agent must never rewrite his prose without an explicit "rewrite the copy". The harness inherits that rule.
2. Publishing a draft is a separate step he takes (or explicitly approves) through the normal CMS or content-edit lane.
3. Git lane: changes go through a pull request, never a direct push to `main`, because `main` auto-deploys.
4. Corpus files are frozen snapshots of his published essays with provenance. If he edits an essay in the CMS, `verify.py` V1 shows the drift and a human decides whether to refresh the snapshot. The holdout is fixed by file name, so it stays stable.

## The small doc edits that would accompany it (all Tier 2)
- `agent/README.md`: add one routing-table row: "Write or review copy in Alejandro's voice | `voice/HARNESS.md`".
- `AGENTS.md`: one line pointing to `agent/voice/HARNESS.md` for anything involving his prose.
Neither is applied yet.

## What "the website is the harness" can grow into (not built, ideas only)
- `canon/audience.md` and `canon/market.md` (who he writes for, in his words), once he supplies them. Not guessed.
- A check that runs on every new `content/blog/*.md` in a pull request and reports drift against `canon/voice-spec.md`. Report only, never blocking and never editing.
- Registers for thesis pages and project pages once he confirms authorship of the existing ones.
Each of these is a later step with its own approval.

## Decisions needed from him
1. APPROVED 2026-10-28: `agent/voice/`.
2. APPROVED 2026-10-28: open a pull request (never a push to main).
3. The open items in HARNESS.md section 8 (authorship of 13 kairon.xyz pages, authorship of the 13 site pages (his 2026-10-28 confirmation covers the 11 essays only), the section B rule decisions, his mimicry notes).
