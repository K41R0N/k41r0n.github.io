---
name: project-brief-skill
description: Use this skill whenever the user wants to create a project brief. Triggers include any mention of "project brief", "brief a project", "create a project brief", or when a user needs to quickly align a team around what work is happening and how. Also use when a user describes a project, initiative, or deliverable and needs to document it concisely for team alignment. Output is always a one-page Word document (.docx) with six standard questions.
---

# Project Brief Skill

This skill creates concise, one-page project briefs that answer six fundamental questions. The brief is intentionally short — details belong in strategy documents, planning documents, and project management systems.

## Output Format

Always create a Word document (.docx) with exactly these six sections:

### 1. What is it?
A concise description of the project, deliverable, or initiative. 1-3 sentences maximum.

### 2. Why is it happening?
The business reason, problem being solved, or opportunity being pursued. 1-3 sentences maximum.

### 3. Who is involved?
Key people, teams, or stakeholders. List names/roles only. Bullet points are acceptable here if there are multiple parties.

### 4. When is it happening?
Timeline, key dates, or milestones. Be specific but brief.

### 5. Where is it happening?
Physical location, platforms, channels, or systems where the work takes place. Can be literal (office, city) or digital (website, app, social channels).

### 6. How do we plan on doing it?
High-level approach, method, or process. 2-4 sentences maximum describing the execution strategy.

## Critical Constraints

- **One page maximum.** No exceptions. This is not negotiable.
- Keep all answers short. If an answer is getting long, it belongs in a separate document.
- Always include all six questions in the same order.
- Never rename, reorder, or skip questions.

## Closing Reminder

Always end the document with this exact text:

---

**Note:** This brief is intentionally concise. Additional information including detailed strategy, tactical plans, timelines, budgets, and execution details should be provided in:
- Strategy documents
- Planning documents  
- Project management systems

## Implementation

1. Gather information for all six questions from the user (or extract from conversation)
2. Read the docx skill to understand how to create properly formatted Word documents
3. Create a one-page Word document with:
   - Document title: "Project Brief: [Project Name]"
   - All six questions as headings
   - Concise answers under each
   - The closing reminder at the bottom
4. Save to `/mnt/user-data/outputs/` and present to the user

## When the User Provides Too Much Detail

If the user gives you extensive information:
- Distill it down to the essential points
- Stay within the one-page constraint
- Suggest they move detailed information to supplementary documents
- Never apologize for keeping it brief — that's the feature, not a bug
