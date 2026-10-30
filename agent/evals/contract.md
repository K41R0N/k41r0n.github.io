# Eval contract

Rules every pack's checks follow.

1. Deterministic. Same input, same result. No network, no model calls.
2. A check can fail an output. No check certifies voice or advice quality. Those go to Alejandro.
3. Each pack has `evals/` (the check script) and `fixtures/` (input and expected result pairs). At least one fixture must pass and one must fail on purpose.
4. A runner prints one line per check: `PASS` or `FAIL`, the pack, the fixture, the reason. Exit code is nonzero on any unexpected result.
5. Fixtures contain invented, generic examples only. No client material.
6. Checks cover structure: required sections present, required fields filled, banned items absent, numbers cited carry a source marker.
7. A pack with no passing fixtures is marked `draft` in its pack.yaml and cannot be listed as ready in index.md.

8. Consumer verdicts are `PASS | FIX | BLOCK`. A FIX or BLOCK carries the exact offending span; no quotable span means flag-for-review, never asserted. Severity and confidence are separate axes. The governing rule must be locatable in the pack this run.
9. Fail closed: a check that errors, a fixture without its expectation file, or a gate list that will not load is a BLOCK, never a pass.
10. Fewer than 3 findings on a clean text: say it is clean. A verdict is assembled, never a rewrite.
11. A clean run means the mechanical half passed, never that the output is ready. Every scripted check keeps a hand procedure; a script is an accelerant, never a dependency.
12. Every real failure that reached output becomes a new fixture in the same upkeep cycle. The suite is the harness's immune memory. Judgment-half failures (a clean run he still rejects) are recorded in the run log, not faked into a regex.
13. A check that fires on required language is a broken check. Never weaken a gate as a fix.
