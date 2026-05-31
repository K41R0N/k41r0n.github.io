# Guideline — Contribution Workflow

How an agent ships a change to this repo without endangering production.

## Two lanes, two risk levels

| Lane | What | How it ships |
|---|---|---|
| **Content (Tier 2)** | `content/**`, images, `agent/`, `docs/` | Branch + PR, or — for pure content Alejandro would otherwise edit himself — a CMS commit. |
| **Code / schema / config (Tier 1)** | `scripts/`, `admin/`, `vercel.json`, `package.json`, `src/css/tokens.css` names | **Always** branch + PR after the forcing-function approval. Never a direct push to `main`. |

`main` auto-deploys to Vercel. A broken build on `main` is a broken production
site. Therefore: **agents do not push code directly to `main`.** Open a PR and
let CI / Alejandro gate the merge.

## The standard sequence

1. **Branch** off `main` (or the branch assigned to your task). Never commit
   straight to `main` for code changes.
   ```bash
   git checkout -b <descriptive-branch-name>
   ```
2. **Edit** the source files (Tier 2 freely; Tier 1 only after approval).
3. **Build & verify** — `npm run build`, then confirm the change in `dist/`. See
   `skills/build-and-verify.md`. A red build never ships.
4. **Commit** with a clear message describing *what changed and why*.
5. **Push** the branch:
   ```bash
   git push -u origin <branch-name>
   ```
   Retry on network errors with exponential backoff (2s, 4s, 8s, 16s).
6. **Open a PR** *only when asked*, or when shipping Tier 1 changes that need
   review. Do not auto-open PRs for routine content unless requested.

## Commit hygiene

- One logical change per commit.
- Message says what and why, not just "update files."
- Do not commit `dist/` churn as the *point* of a change — `dist/` is build
  output. (It is fine if a build regenerates it; just don't treat editing it as
  the change.)
- Never commit secrets. The CMS auth worker URL is public-by-design and already
  in the template; nothing else sensitive belongs in the repo.

## The writing boundary (carry it over from the research brain)

The Research agent **supports** writing; it does not ghostwrite Alejandro's
essays or publish in his voice. For the portfolio that means:

- **Allowed:** structural edits, fixing metadata, adding links, wiring up new
  content fields, formatting an essay Alejandro has finalized, building
  automation.
- **Requires Alejandro:** the *words* of a public essay or thesis. If a task
  would put new prose in his voice on the public site, draft it for review and
  stop — do not publish autonomously. Publishing is a human decision.

## Verify-before-report

Mirror the brain's discipline: after any edit, confirm it (build + grep `dist/`).
Report what you actually verified. If the build failed or you couldn't confirm,
say so with the output. "Done" means green build and confirmed output — not "I
made the edit."
