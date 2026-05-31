---
topic: "Project AEO/SEO Integration"
date: 2026-05-31
status: "completed"
---

# Requirements: Open Source Projects AEO/SEO Integration

## Problem Frame
The current portfolio site heavily features "Theses" and "Writing" but does not expose Kairon's library of open-source tools and non-web3 projects. This limits discoverability by both human visitors and, crucially, AI agents and LLM crawlers (ChatGPT, Perplexity, Claude, Google AI Overviews). The goal is to make the site a powerful Generative Engine Optimization (GEO/AEO) tool that properly indexes his abilities, projects, and open-source contributions.

## Chosen Approach: The First-Class Section
Projects will be integrated directly into the human-facing UI on the homepage (similar to the Theses section) while simultaneously receiving deep integration into the machine-readable surfaces (`llms.txt`, JSON API, Schema.org). Each project will have its own dedicated detail page to maximize on-site indexable content for AI crawlers.

## Success Criteria
- **Content Backend:** Open source tools and projects exist as individual Markdown entries in `content/projects/*.md` editable via Sveltia CMS.
- **Human UI:** The homepage features a new "Projects" section using the existing editorial design language (e.g., `.sec-head` and dot-leader TOC).
- **Detail Pages:** Clicking a project generates a dedicated `/project-[slug].html` page with full context, documentation, and external links.
- **Machine UI (GEO/AEO):** 
  - The build script (`scripts/build.js`) generates rich Schema.org JSON-LD (e.g. `SoftwareSourceCode`, `SoftwareApplication`, or `CreativeWork`) for the projects.
  - The `llms.txt`, `llms-full.txt`, and `api/content.json` endpoints include the new project data, explicitly formatted to instruct agents on Kairon's capabilities.
- **Parity:** Both humans and agents have full visibility into the project library.

## Scope Boundaries
- **In scope**: New CMS collection for Projects, Schema.org enhancements, `llms.txt` enhancements, homepage UI addition, new project detail pages.
- **Out of scope**: Rewriting the existing theses/blog logic, migrating existing external project documentation into the repo (just writing summaries and linking out is sufficient).

## Key Product Decisions
- **First-Class Section:** The projects will not be hidden in a "Shadow DOM" or just in `llms.txt`; they will be fully visible to humans on the homepage.
- **Dedicated Pages:** Projects will have their own detail pages on the site rather than just linking out to GitHub immediately, maximizing on-site SEO depth.

## Open Questions (Resolve During Planning)
- **Schema Selection:** What specific Schema.org type (`SoftwareSourceCode`, `SoftwareApplication`) provides the strongest signal to AI crawlers for an open-source tool?
- **Layout Mapping:** Should the project detail page reuse the `chapter-page` layout (like Theses) or the `article` layout (like Blog)?