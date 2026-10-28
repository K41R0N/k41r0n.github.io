# Slop and style tooling (candidates, from the external scan)
Keep and adapt: slop-guard (deterministic linter; its sg-fit calibrates rules against a corpus) https://github.com/eric-tramel/slop-guard ; slop-score (range math, swap generic baseline for his corpus) https://github.com/sam-paech/slop-score ; write-good and proselint as baseline linters; the MDD blind-pair method for approving rules (implemented in routines/blind-test.md).
Mine for ideas only: vale-ai-tells (measured about 4% precision on a real corpus).
Rejected: humanizer wrappers that dodge detectors instead of improving the writing.
Status: slop-guard confirmed to exist, not installed. Candidate second opinion: test it on his own corpus first and compare against tools/checks.py before trusting it. Scanned, not installed or run in phase 1. Installing any of them is a phase 2 decision.
