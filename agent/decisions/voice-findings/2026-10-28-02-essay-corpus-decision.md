---
type: Finding
title: Essay corpus decision (his words)
date: 2026-10-28
source: "His WhatsApp message on 2026-10-28, about 5:09 PM, id wamid.HBgLMzQ2NzYyNDU0MDkVAgASGCBBQzA4MDZFMjRBQTE5NzhEQjg4OUZEQzY1Qzk2M0YyMQA=. Quote: 'All of them are fully my prose, and they're authoritative, you should also lend higher priority to the more recent ones. Proceed'"
status: Decided by him; applied
---
# Essay corpus decision (his words)

- All 11 Substack essays are fully his prose and authoritative. The spec is built from the 9 in corpus/raw. The other 2 are held out for testing (random seed 20261028). He knows the 2025-06-17 essay mentions Claude and confirmed it anyway.
- This covers the 11 essays only. The 13 site pages in corpus/excluded are not covered and stay out of the spec until he confirms them specifically.
- Recency weighting: exponential, half-life 12 months, relative to the newest raw essay (2026-09-20). He asked for recent essays to count more. The 12-month half-life is the engine's choice, not his. It is one constant in tools/build_spec.py and is documented in canon/voice-spec.md.
- Result: the newest essay (Shadow Work, 2026-09-20) carries about 22% of the total weight. The other eight carry 0.41 to 0.49 each relative to 1.0.
