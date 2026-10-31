# Controller Rules

Shared rules every skill in this plugin must follow. Each skill SKILL.md restates these rules so they stay in context, and may reference this file for the canonical text.

## The Six Rules

1. **Read files before acting.** Always inspect the actual contents of inputs (transcripts, prior outputs, prompts) before generating anything. Do not act on filenames or summaries alone.

2. **Preserve evidence traceability to source interviews.** Every claim, action, SWOT item, or recommendation must carry an attribution back to the interview(s) it came from (interviewee name + transcript section or quote where possible).

3. **Prefer best scalable practice, not best individual practice.** When team members do similar work differently, the standard is the version that scales across the team — not the most senior person's version, the fastest version, or the most polished version.

4. **Mark ambiguity explicitly; do not invent source material.** When evidence is missing, contradictory, or unclear, flag it (e.g., `[AMBIGUOUS — see review]`, `[NOT IN SOURCE]`). Never fabricate quotes, decisions, tools, or process steps.

5. **Distinguish source-grounded fact from reasonable inference from recommendation.** Use consistent labels in outputs: `FACT` (verbatim or near-verbatim from source), `INFERENCE` (synthesized from multiple sources), `RECOMMENDATION` (best-practice guidance not present in source). Never blur the three.

6. **Do not flatten useful role-specific differences.** When two roles legitimately need different versions of an action (e.g., research vs. content), keep both. Standardization is not homogenization.

## Out of Scope

Patch-mode and mid-stream refactor flows (re-running synthesis after late-arriving interviews, regenerating manifests after staffing changes) are explicitly **out of scope** for this plugin. The pipeline assumes a clean run: extract → synthesize → manifest → v1 SOPs → v2 overlay → review summaries → final playbook.
