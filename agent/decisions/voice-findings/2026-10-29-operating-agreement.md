# Operating agreement, voice-relevant parts (2026-10-29)

Source: working instructions in `agent/AGENTS.md`; the 2026-10-29 6:48 PM WhatsApp message says “Ok, proceed, are you ready to do your work properly?” and is not specific approval of every clause. Treat unsupported clauses as repo-local proposed safeguards until directly confirmed.
("Ok, proceed"). Canonical copy: agent/operating-agreement.md (this repo).

- Everything written in his voice (site, X, LinkedIn, prompts) is an input for
  his line-by-line edit, never output. Published output passes him at every
  stage, permanently.
- His edits are the training data. Metrics: acceptance rate, edit rate, his
  minutes per deliverable. Tracked in the run log:
  `agent/routines/writing-runs.md` (this repo).
- The same correction twice becomes a fixed rule (his work guide; this
  supersedes the three-repeat default for user-facing work).
- Presentation rules: facts before explanation before options before
  recommendation; every claim labeled (he said it / confirmed / inferred);
  gaps declared, never filled with averages; one question at a time; drafts
  labeled as drafts; he never sees framework machinery in chat.
- Delivery expectation: every site PR ships with a live preview URL
  (here.now, anonymous 24-hour sites unless he provides an API key),
  reported together with the PR link, with direct links to every changed page.

Standing rule, same day (WA 6:55 PM): nothing public-facing ever carries meta
commentary or buzzwords - "literally the opposite of my brand." Effective
immediately on his explicit statement. Enforced by the build gate in
scripts/validate-content.js (unreplaced markers + buzzword register, seeded
from the documented lists in agent/voice/tools/checks.py) and by the voice
checks on anything destined for the public site.

Run 0 is recorded in the run log: the 2026-10-28 voice-engine test draft,
rejected ("not at all my style... reads like slop", WA 17:53:17).
