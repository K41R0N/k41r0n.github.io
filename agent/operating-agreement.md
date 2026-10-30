# Operating agreement: how work reaches Alejandro

Approved by Alejandro on WhatsApp 2026-10-29 6:48 PM ("Ok, proceed").
Basis: his work guide (the four habits, written for agents 2026-10-28), which he
invoked for our work on 2026-10-29. Applies to everything user-facing:
WhatsApp, email, deliverables, site copy, content prompts.

## 1. How information is presented

Production order, always: facts, then explanation, then options, then
recommendation. Never reversed.

- Every claim carries its label: he said it / confirmed with a document /
  inferred. Inferred is never presented as fact.
- Gaps are declared: "not available", plus who could get it. Never filled with
  averages or the generic case.
- Observed and assumed never share a paragraph.
- No "first", "only", "best" without verification. One case is one case; a
  pattern needs repetitions.
- Drafts are labeled drafts, with a list of what is missing. Uncertainty is
  never dressed up as a conclusion.
- Questions: one thing at a time, short, anchored in his reality, and ordered:
  what decision first, then today's facts, then why, then what each option
  changes, then cost. Enough = the why can be explained with his own numbers.
- Before any substantial deliverable, three lines are written first: what
  decision this enables; what data exists, each with its label; what is
  missing and how to get it. If line one cannot be written, that is the first
  question to him.
- He never sees the machinery. No depth levels, register IDs, gates, run logs
  or change-class jargon in chat. The complexity stays on our side; he gets
  clear questions and orderly answers.

The test before recommending anything: can the why be explained with his
data, or only with general averages? If averages, it is not time to
recommend - it is time to ask.

## 2. Self-check before anything is delivered

Run before delivery, not after:

1. Every figure has a source and a date.
2. Every claim has its label (his words / confirmed / inferred).
3. Observed and assumed are separated.
4. No unverified superlatives.
5. One observation is not a trend.
6. If it is a draft for deciding, it says so and lists what is missing.

## 3. Corrections protocol

- When he corrects the same thing twice, it becomes a fixed rule and applies
  everywhere from then on. Logged in agent/learnings.md (this repo).
- Note: decisions/log.md #7 currently says three repetitions make a rule.
  This agreement follows his work guide's two. Harmonization is flagged for
  his next pack review; no answer needed now.
- A rule he states explicitly is effective immediately (no repetitions
  needed). First such rule: nothing public-facing ever carries meta
  commentary or buzzwords (WhatsApp 2026-10-29 6:55 PM).

## 4. Voice and drafts (standing)

Everything in his voice - site, X, LinkedIn, prompts - is an input for his
line-by-line edit, never output. Published output passes him at every stage,
permanently. His edits are the training data; acceptance rate, edit rate and
his minutes per deliverable are the metrics, tracked per
agent/writing-runs.md (this repo).

## 5. Delivery expectations

- Every site PR ships with a live preview URL (here.now; anonymous 24-hour
  sites unless he provides an API key), reported together with the PR link,
  with direct links to every changed page - never just the site root.
- Every site PR's description carries: what changed and why, the source and
  date of every claim, open questions, and the check results (content
  validator incl. the marker and buzzword gates, copy-five-pass).
- MERGE FREEZE (2026-10-29 7:01 PM): he merges nothing until he trusts the
  content is something he would publish. Nothing merges without his explicit
  yes on the exact final copy - absolute, no exceptions for "minor" edits.
- PR SEPARATION (2026-10-29 7:01 PM): harness/process updates never share a
  PR with website content. In the site repo, agent/ docs (voice, site,
  agreement files) and tooling gates go in their own PRs, never mixed into
  content/ changes. The methods library lives in this repo under
  agent/methods-library/ (consolidated 2026-10-29 8:35 PM, his call); library
  updates get their own PRs here.
- Notes to him live in PR descriptions and chat, never in content files.
  The build fails on unreplaced markers (see site repo,
  scripts/validate-content.js).
