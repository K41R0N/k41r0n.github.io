# packs/README.md

Pointer file. Alejandro's methods as reusable packs with checks, inside the
site repo's `agent/` area; never rendered on the public site.

- Route a task to a pack: `index.md` (kept complete by
  `../scripts/local/routing_lint.py`).
- Run every pack's checks: `python3 ../evals/run.py` from this folder's
  parent, or `python3 evals/run.py` from `agent/`.
- What a check must do: `../evals/contract.md`.
- Operating rules: `AGENTS.md` in this folder (points to the repo-level
  agreement).

Replaced 2026-11-14 (decisions/log.md #34): the previous content carried a
stale pack count and described the retired methods repo.
