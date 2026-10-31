# process-standardization

A Claude plugin that packages an end-to-end methodology for standardizing how an operations team works. Drop in interview transcripts, follow the pipeline, ship a rollout playbook.

## Pipeline

```
extract → synthesize → manifest → v1 SOPs → v2 overlay → review summaries → final playbook
```

The plugin assumes a clean run. Patch-mode flows (re-running synthesis after late interviews, mid-project staffing fixes, v3/v4 refactors) are intentionally out of scope. If new evidence arrives after the manifest is built, re-run the pipeline rather than patching.

## Skills

| Skill | When to use |
|---|---|
| `process-standardization-bootstrap` | Scaffold a new project — folder layout, controller rules, master prompt. Run first. |
| `interview-extraction` | One transcript in, one lossless structured extraction out. Run once per interviewee. |
| `cross-interview-synthesis` | N extractions in. Produces SWOT, action comparison matrix, standardization boundary map. |
| `action-manifest` | Builds the canonical action manifest, source map, and action families. Build only — no patch mode. |
| `sop-drafter` | Two modes: `internal` (v1 from team practice) and `overlay` (v2 layered on a user-supplied external reference framework). |
| `interviewee-review-summary` | Two-page verification doc back to each interviewee before the playbook is finalized. |
| `playbook-assembler` | Assembles the final 12-section rollout playbook from manifest, families, v2 SOPs, and incorporated review feedback. |
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
- **External reference framework** — any methodology, book, industry standard, or third-party playbook the team wants to overlay in v2. One example framework could be a third-party industry playbook; substitute your own.

## Setup

Install the plugin, then start a session in the directory you want to scaffold and invoke the bootstrap skill (e.g. "set up a process standardization project for my ops team").
