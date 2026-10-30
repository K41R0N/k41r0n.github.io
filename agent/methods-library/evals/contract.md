# Eval contract

Rules every pack's checks follow.

1. Deterministic. Same input, same result. No network, no model calls.
2. A check can fail an output. No check certifies voice or advice quality. Those go to Alejandro.
3. Each pack has `evals/` (the check script) and `fixtures/` (input and expected result pairs). At least one fixture must pass and one must fail on purpose.
4. A runner prints one line per check: `PASS` or `FAIL`, the pack, the fixture, the reason. Exit code is nonzero on any unexpected result.
5. Fixtures contain invented, generic examples only. No client material.
6. Checks cover structure: required sections present, required fields filled, banned items absent, numbers cited carry a source marker.
7. A pack with no passing fixtures is marked `draft` in its pack.yaml and cannot be listed as ready in index.md.
