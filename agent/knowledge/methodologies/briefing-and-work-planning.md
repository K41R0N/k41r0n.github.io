---
id: 01M69AYGQXATDBWGKFQ5DNCNPD
type: Method
title: "Briefing and work-planning method"
description: "Six-question brief and practical plan with explicit sources, gaps, owners, dependencies, approvals, and checks."
confidence: inferred
source: "10-skills/project-brief-skill/SKILL.md@e2c6fcdacf32783a72f1ddca06ee0e4edc8038d4"
updated: 2026-10-31
class: S0
tags: [onboarding, verification]
---
# Briefing and work-planning method

A brief is a decision aid and a working contract. It should be short enough to use, complete enough to prevent avoidable rework, and explicit about what is unknown.

## Write the brief before starting

Answer these six questions in plain language:

1. **What is it?**
2. **Why is it happening?**
3. **Who is involved?**
4. **When is it happening?**
5. **Where is it happening?**
6. **How do we plan on doing it?**

Include only details that change what someone does. Keep the six questions in this order and do not merge or skip them. For a project brief, keep it to one page; put supporting research and background in separate planning material rather than expanding the brief into a repository of everything known.

The brief is an alignment artifact, not the detailed project plan. Do not invent missing answers; mark the gap and who can fill it. When the project-brief skill applies, follow its full output contract as well: a one-page Word document with exactly these six headings, the required closing note, and the prescribed title. This guide does not replace that skill.

## Six-field brief skeleton

For the project brief, fill these headings in order and keep the result to one page. Write only what is known. For a missing answer, write `[Not stated - source or owner needed]`; do not make a likely guess look agreed.

```text
Project Brief: [Project Name]

1. What is it?
[Deliverable or initiative, 1-3 sentences]

2. Why is it happening?
[Business reason, problem, or opportunity, 1-3 sentences]

3. Who is involved?
[Names / roles only]

4. When is it happening?
[Timeline, key dates, or milestones]

5. Where is it happening?
[Place, platform, channel, or system]

6. How do we plan on doing it?
[High-level approach, 2-4 sentences]

**Note:** This brief is intentionally concise. Additional information including detailed strategy, tactical plans, timelines, budgets, and execution details should be provided in:
- Strategy documents
- Planning documents
- Project management systems
```

When a project brief is requested, use the full [project-brief skill](../../method-archive/10-skills/project-brief-skill/SKILL.md): it requires a one-page Word document, the exact headings and order above, title `Project Brief: [Project Name]`, and the closing note shown here. This markdown skeleton helps gather inputs; it is not the final deliverable contract. Keep supporting research, detailed timing, budgets, and task sequencing in the separate plan.

## Turn the brief into a plan

- State the decision this work enables before writing a substantial deliverable.
- List available inputs with their source and confidence. List missing information separately, with the person or source that can resolve it.
- Break work into ordered steps with a clear owner, input, output, and check at each boundary.
- Identify dependencies, approval points, and what must not happen before approval. Consultation is not authorization.
- Define completion using observable artifacts or checks, not vague terms such as "done" or "high quality."
- If a goal has no measurable result or artifact that could show whether it happened, revise the goal or remove it.

Before automating repeated work, write the manual sequence first. Map the information needed, the follow-up questions needed to reach the objective, and how the answers combine into a direction. Only then decide which bounded steps are suitable for an agent or deterministic check; keep judgment and approvals human-owned.

## Find the cause before prescribing a fix

Describe the problem, its likely root cause, and a proposed solution separately. Test whether the stated problem is a symptom by asking what produces it and what evidence would distinguish the candidate causes. Do not settle on familiar explanations like "no process" or "unclear ownership" without checking. If people, decisions, or evidence are missing, mark the gap rather than assigning blame.

## Keep plans useful as work changes

Use one current source for decisions and terminology. When new evidence changes the plan, update the source and every dependent artifact; record the change and its reason. Keep historical versions when the review trail matters, but label the current version clearly. If a scope change affects timing, cost, or approval, surface it before proceeding.

## Evidence basis and limits

The exact six questions, order, one-page Word output, title, and closing note come from `10-skills/project-brief-skill/SKILL.md`; the compendium restates the one-page, six-question contract in E2 and H1. The blank skeleton above reproduces that output contract in a working form. The separate work-plan steps (inputs, gaps, owners, dependencies, approvals, and measurable results) are synthesis from the compendium, not part of that six-question source template. The manual-first sequence and information / second-degree-question / synthesis map are stated in the compendium. Project-specific tools, owners, or client workflow details are intentionally excluded and should not be inferred.

## Compact delivery check

Before sharing, confirm that the brief names the objective, reader, owner, deadline, delivery surface, inputs, gaps, approvals, and completion test. Remove anything that does not change the decision or next action.
