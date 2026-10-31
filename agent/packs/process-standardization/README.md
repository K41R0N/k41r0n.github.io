# process-standardization

A Claude plugin that packages an end-to-end methodology for standardizing how an operations team works. Drop in interview transcripts, follow the pipeline, ship a rollout playbook.

## Pipeline

```
extract → synthesize → manifest → v1 SOPs → (optional v2 overlay, only with a supplied framework) → interviewee review and correction reconciliation → final playbook
```

The plugin assumes a clean run. Patch-mode flows (re-running synthesis after late interviews, mid-project staffing fixes, v3/v4 refactors) are intentionally out of scope. If new evidence arrives after the manifest is built, re-run the pipeline rather than patching. A correction to a source fact must be reconciled across every downstream artifact that carries that fact before the workflow proceeds; do not make an isolated edit to just one copy. If an impacted artifact cannot be safely regenerated in this clean-run workflow, stop and route for a full stage re-run.

## Skills

| Skill | When to use |
|---|---|
| `process-standardization-bootstrap` | Scaffold a new project — folder layout, controller rules, master prompt. Run first. |
| `interview-extraction` | One transcript in, one lossless structured extraction out. Run once per interviewee. |
| `cross-interview-synthesis` | N extractions in. Produces SWOT, action comparison matrix, standardization boundary map. |
| `action-manifest` | Builds the canonical action manifest, source map, and action families. Build only — no patch mode. |
| `sop-drafter` | Two modes: `internal` (v1 from team practice) and `overlay` (v2 layered on a user-supplied external reference framework; framework required for overlay). |
| `interviewee-review-summary` | Two-page verification doc back to each interviewee before the playbook is finalized. |
| `playbook-assembler` | Assembles the final 12-section rollout playbook from manifest, families, the completed SOP set, and reconciled review feedback. |
| `process-standardization-audit` | Inspects an existing project folder, identifies which pipeline stage it is at, recommends the next skill. Read-only. |

## Shared rules

Every skill restates and enforces the six controller rules. The canonical text lives at `CONTROLLER.md` (referenced from each skill as `${CLAUDE_PLUGIN_ROOT}/CONTROLLER.md`):

1. Read files before acting.
2. Preserve evidence traceability to source interviews.
3. Prefer best scalable practice, not best individual practice.
4. Mark ambiguity explicitly; do not invent source material.
5. Distinguish source-grounded fact from reasonable inference from recommendation.
6. Do not flatten useful role-specific differences.

## Parameters every skill accepts

The methodology generalizes — none of these are hardcoded:

- **Role-family taxonomy** — any list. Example family labels are research, content, visual production, reporting, community, and campaigns; your team's list is supplied at bootstrap.
- **External reference framework** — optional. Required only if producing v2 overlay SOPs; otherwise the workflow can remain v1/internal and must say it did not apply an external framework. The completed playbook must identify whether it is based on v1-only SOPs or framework-backed v2 SOPs.

## Setup

Install the plugin, then start a session in the directory you want to scaffold and invoke the bootstrap skill (e.g. "set up a process standardization project for my ops team").
