# AGENTS.md - methods

Read this first. This repo holds Alejandro Arango's methods as reusable packs, each with checks.

## Hard rules
1. Nothing lands on the default branch except through a pull request he merges. Never push to it.
2. Nothing here is written in his name or published without his yes on the exact thing.
3. Method only. No client names, figures, voice rules or credits from client repos. Run `scripts/local/push_gate.sh` before every push.
4. Say plainly what you could not read. Never fill a gap with an invented fact, anecdote or number.
5. Evals can fail an output. They never certify it as his voice or his advice. That judgment is his.
6. Do not edit `knowledge/ethos/` on your own. Propose a change in a pull request and mark it as inferred until he confirms.

## Where things are
- `CHARTER.md` what this repo is for and what it is not.
- `index.md` router: task to pack.
- `knowledge/ethos/` his principles (stub, awaiting his edits).
- `packs/` the modules (added in phase 2).
- `evals/contract.md` what a check must do.
- `decisions/` calls made, goals, open loops.
- `routines/learnings.md` corrections waiting to become rules.
- `scripts/local/push_gate.sh` the push gate.

## Working habits
- Check the real thing before saying anything about it.
- Small calls you can undo: make them, log them as "made, overridable" in `decisions/log.md`.
- Questions to him: plain words, one at a time, only when it needs his judgment.
- A correction seen twice becomes a rule. Log it in `routines/learnings.md` first.
