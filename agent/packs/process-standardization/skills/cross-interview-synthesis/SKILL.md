---
name: cross-interview-synthesis
description: Combines N completed interview extractions into a team-level SWOT, an action comparison matrix, and a standardization boundary map that drive a downstream action manifest. Triggers when the user says "synthesize the interviews", "cross-interview synthesis", "compare interview extractions", "build SWOT from extractions", "standardization boundary map", or "action comparison matrix".
version: 0.1.0
---

# Cross-Interview Synthesis

## Purpose

Take every completed interview extraction for a single operations team and produce three artifacts: a team-level SWOT grounded in interviewee evidence, an action comparison matrix that lines up recurring actions across role-families, and a standardization boundary map that classifies each action as STANDARDIZE, TEMPLATIZE, or PRESERVE-VARIANT. These three artifacts are the inputs the `action-manifest` skill needs to decide what to standardize next.

## When to trigger

Trigger this skill when:

- An interview extraction exists for every planned interviewee on the team.
- No action manifest, SOP set, or playbook has been drafted yet for this team.
- The user asks to compare, synthesize, or roll up the interviews into team-level findings.

Do not trigger this skill when extractions are still missing, when the synthesis already exists and the user is asking for a downstream artifact, or when the request is to patch an existing synthesis after a late interview. Patch-mode synthesis is out of scope.

## Required inputs

Before running, confirm the following with the user:

1. **Folder containing N extractions.** A directory holding one extraction file per interviewee. Read every file in that folder. If the folder is unclear, ask.
2. **Role-family list.** The set of role-families to compare across. The taxonomy is whatever the team uses. A six-family taxonomy (research / content / visual production / reporting / community / campaigns) is one example, not a fixed schema. Accept any list — fewer or more families, different domains, different labels.
3. **Team identifier.** A short label for the team being synthesized so the output title is unambiguous.

If any input is ambiguous, stop and ask before reading. Do not invent a role-family list.

## Outputs

Produce one synthesis document containing the three required artifacts in this order.

### a. Team-level SWOT (evidence-grounded)

Four sections: **Strengths**, **Weaknesses**, **Opportunities**, **Threats**.

For every bullet, include:

- A short description of the pattern.
- The interviewee(s) that show it — by name or pseudonym, matching how they appear in the extractions.
- A direct evidence reference: a quote, a paraphrased observation tagged to the source, or both.
- The operational implication for the team.

A SWOT bullet without a named source is not allowed. If a pattern is supported by inference rather than a direct quote, mark it as inference and say which extraction(s) the inference is drawn from.

### b. Action comparison matrix

Rows are recurring actions (the things people on the team actually do). Columns are role-families, or individual interviewees when the team is small enough that role-family is just one person per family.

Each cell describes how that role-family performs the action: shared steps, tools, decision rules, handoffs, pain points. For every row also call out:

- Where the role-families converge (the shared spine of the action).
- Where they diverge (the role-specific variations).
- Whether the divergence appears intentional and useful, or accidental and harmful.

If an action is only performed by one role-family, keep it in the matrix and mark the other cells as "not performed" rather than dropping it. The reader needs to see the gap.

### c. Standardization boundary map

For every action in the matrix, classify it as exactly one of:

- **STANDARDIZE** — converge on one shared way. Use when the variation is harmful inconsistency, the best scalable practice is clear, and there is no good reason for role-specific variants.
- **TEMPLATIZE** — shared skeleton plus role-specific overlay. Use when the action has a stable structure (template, format, cadence) but the content or inputs legitimately differ by role-family.
- **PRESERVE-VARIANT** — leave the role differences alone. Use when the variation reflects a real and useful specialization that would lose value if flattened (rule 6 below).

For each action, write one or two sentences explaining why it landed in that bucket, citing the matrix evidence.

## Method

1. **Read every extraction file in the folder before writing anything.** If the folder contains files outside the extraction format, ask before including them. Do not summarize from filenames.
2. **Inventory recurring actions.** Walk through every extraction and pull out the actions each person performs. Cluster actions across people that are the same operational thing under different names. Note disagreement on naming — terminology drift is itself a finding.
3. **Build the matrix first.** For each clustered action, fill the cells. The matrix is what the SWOT and boundary map both read from.
4. **Derive the SWOT from the matrix.** Strengths and weaknesses follow from the convergence/divergence pattern. Opportunities follow from cross-pollination candidates (one role-family does it well, others would benefit). Threats follow from key-person dependencies, single points of failure, and unmanaged risk surfaced in the matrix.
5. **Classify each action for the boundary map.** Apply rule 3: pick the best **scalable** practice, not the best **individual** practice. Some practitioners are world-class because of personal skill that does not transfer. The synthesis must distinguish "this works because it is well-designed" from "this works because of who is doing it."
6. **Sanity-check against the controller rules below before finalizing.**

## Anti-patterns

Do not:

- **Default to the senior person's version.** Seniority is not evidence. A strong individual may be doing it the hardest, least transferable way. Pick the version that the rest of the team can actually run.
- **Flatten role-specific differences that exist for a reason.** If a research role-family needs deep boolean filtering and a content role-family needs broad ideation, those are different jobs. Pretending they are the same job because the word "research" appears in both produces SOPs that nobody follows.
- **Score consistency without explaining cost.** "Low consistency" is a description, not a recommendation. The boundary map is where the recommendation lives.
- **Invent supporting quotes.** If you cannot find a direct evidence reference, mark the bullet as inference and name the extractions it is drawn from.
- **Drop solo actions.** An action performed by one person is still in the matrix — that is exactly where key-person risk lives.

## Controller rules (restated inline)

The canonical version lives at `${CLAUDE_PLUGIN_ROOT}/CONTROLLER.md`. Restated here for inline use:

1. **Read files before acting.** Read every extraction file in the input folder before producing any synthesis output. No summary may rely on filename inference.
2. **Preserve evidence traceability to source interviews.** Every SWOT bullet, matrix cell, and boundary classification must be traceable to one or more named interviewees.
3. **Prefer best scalable practice, not best individual practice.** When two practitioners diverge, ask which version a new hire could run on day 30 — not which version produces the best output today in the hands of the most skilled person.
4. **Mark ambiguity explicitly; do not invent source material.** If extractions disagree, say so. If evidence is thin, say so. Do not paper over gaps with confident prose.
5. **Distinguish source-grounded fact from reasonable inference from recommendation.** Tag each finding as `fact` (direct from extraction), `inference` (reasoned from extractions), or `recommendation` (synthesist's judgment). The reader should always know which is which.
6. **Do not flatten useful role-specific differences.** Variation that reflects real specialization is a feature. The boundary map's PRESERVE-VARIANT category exists for exactly this case. Use it.

## Hand-off

The synthesis output (SWOT + action comparison matrix + standardization boundary map) is the input to the `action-manifest` skill. After writing the synthesis, point the user at `action-manifest` as the next step. Do not draft SOPs, playbooks, or rollout plans inside this skill — those are downstream.
