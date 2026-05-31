---
title: "Agent Copy Modification Boundary Violation"
date: 2026-05-31
category: workflow-issues
module: agent-collaboration
problem_type: workflow_issue
component: documentation
severity: high
applies_when:
  - Performing SEO audits
  - Updating technical infrastructure
  - Touching content files for structural reasons
tags: [agent-rules, boundaries, copy, seo, ghostwriting]
---

# Agent Copy Modification Boundary Violation

## Context
During a GEO/SEO audit of the portfolio, the agent was instructed to optimize the site from an "infra perspective." The agent incorrectly conflated "infra/SEO optimization" with "content optimization" and proceeded to completely rewrite the user's `content/pages/about.md` file to be more entity-dense for AI crawlers. 

This was a severe violation of the `SOUL.md` rules and the user's explicit preferences, which state that the agent must never ghostwrite or alter the user's prose.

## Guidance
- **Never modify prose:** When asked to optimize for SEO or infrastructure, the agent must restrict its changes to metadata, JSON-LD schemas, structural HTML, or configuration files (`site.json`, `build.js`). 
- **The text is sacred:** Even if the text is objectively poorly optimized for search engines or AI crawlers, the agent must not rewrite it unless explicitly commanded to "rewrite the copy."
- **Propose, don't execute:** If content changes are necessary for an optimization goal, the agent should output a suggested rewrite in the chat or an outbox file, but leave the source files intact.

## Why This Matters
Trust between the operator and the agent relies on strict adherence to boundaries. Rewriting personal copy without permission breaks this trust, violates the established identity constraints, and forces the user to manually intervene and revert changes, slowing down the workflow.

## When to Apply
- Whenever modifying markdown files in the `content/` directory.
- When performing GEO/AEO/SEO optimizations.
- When adding schema markup or meta tags.

## Examples
**Incorrect:**
User: "Do an SEO audit and optimize the about page from an infra perspective."
Agent: *Rewrites `content/pages/about.md` to add structured lists and remove personal narrative.*

**Correct:**
User: "Do an SEO audit and optimize the about page from an infra perspective."
Agent: *Updates `scripts/build.js` to inject rich `Person` JSON-LD schema into the `<head>` of the about page, leaving `content/pages/about.md` completely untouched.*

## Related
- `~/.openclaw/workspace-research/SOUL.md`
- `agent/README.md`
