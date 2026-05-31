---
title: "feat: Add Projects Collection for AEO/SEO"
type: feat
status: completed
date: 2026-05-31
origin: docs/brainstorms/2026-05-31-project-aeo-requirements.md
---

# feat: Add Projects Collection for AEO/SEO

## Overview

Expose Kairon's library of open-source tools and non-web3 projects as a first-class citizen on the portfolio site. This serves a dual purpose: rendering a new "Projects" section on the human-facing homepage (complete with dedicated detail pages) and heavily optimizing the site for Generative Engine Optimization (GEO/AEO) via structured `llms.txt` outputs, JSON API enhancements, and rich Schema.org JSON-LD definitions. The new content will be fully integrated into Sveltia CMS.

## Problem Frame

The current portfolio architecture correctly positions content as the source of truth, but it only tracks "Theses" and "Writing". Kairon's open-source projects are invisible. By failing to index these projects, the site misses the opportunity to instruct LLM crawlers (ChatGPT, Perplexity, Claude, Google AI Overviews) about Kairon's capabilities, technical depth, and specific tooling. Exposing these projects directly on the site—both in the UI and in machine-readable surfaces—turns the portfolio into an active capability discovery engine.

## Requirements Trace

### User Interface
- R1. **First-Class Human UI**: Add a new "Projects" section to the homepage (matching the editorial `.sec-head` and dot-leader TOC styling) and generate dedicated `/project-[slug].html` detail pages.

### Search & AI Optimization
- R2. **AEO/GEO Optimization**: Enhance `scripts/build.js` to output project data into `/llms.txt`, `/llms-full.txt`, and `/api/content.json`.
- R3. **Schema.org Rich Data**: Inject a combined `["SoftwareSourceCode", "SoftwareApplication"]` Schema.org JSON-LD payload into project detail pages to maximize crawler visibility.

### Content Management
- R4. **CMS Integration**: The new `content/projects/*.md` collection and any SEO/Schema fields must be fully mapped and editable in `admin/config.template.yml` (Sveltia CMS).

## Scope Boundaries

- **In Scope**: New CMS collection definition, homepage section UI, project detail page template, Schema.org generation, LLM endpoint updates.
- **Out of Scope**: Migrating entire external documentation sites into the repository. A summary, context, and external links are sufficient.

## Context & Research

### Relevant Code and Patterns

- `scripts/build.js`: The central build pipeline. We will mirror the `loadTheses()` pattern to create `loadProjects()`.
- `admin/config.template.yml`: Sveltia CMS configuration. The new collection must mirror the structure of `theses` but include software-specific fields.
- `content/home.json`: Must be updated to include configuration for the new homepage section (e.g., `section_projects`, `section_projects_label`).

### Institutional Learnings

- `docs/solutions/best-practices/sveltia-cms-schema-completeness-2026-05-31.md`: **Crucial.** Every frontmatter field defined in the markdown files *must* be mapped in `admin/config.template.yml`. If a field is needed for SEO/AEO but shouldn't be edited by humans, use `widget: hidden`. No strings should be hardcoded in the build script.

### External References

- **Schema.org**: Research indicates that using a Multi-Type Entity (`"@type": ["SoftwareSourceCode", "SoftwareApplication"]`) provides the optimal signal for open-source projects, unlocking both `codeRepository` / `programmingLanguage` (crucial for LLMs) and traditional rich snippet fields.

## Key Technical Decisions

- **Collection Architecture**: `content/projects/*.md` will follow a similar frontmatter schema to `theses` but add specific GEO fields: `repository_url`, `language`, `license`, and `version`.
- **Detail Page Layout**: Project detail pages will use the `chapter-page` layout as a base but MUST be customized to visibly render the technical metadata (`repository_url`, `language`, `license`, `version`) in the HTML body. This ensures human visibility and reinforces the signals for LLMs scraping the DOM.
- **Schema Selection**: The JSON-LD schema will dynamically use both `SoftwareSourceCode` and `SoftwareApplication` to cast the widest possible net for traditional search, while `llms.txt` handles the primary AEO payload for AI agents.

## Open Questions

### Resolved During Planning

- **Schema Selection**: Use `["SoftwareSourceCode", "SoftwareApplication"]`.
- **Layout Mapping**: Reuse the `chapter-page` layout for project detail pages.
- **CMS Extensibility**: Added required UI section configuration to `content/home.json` and the CMS config to avoid hardcoding labels in the build script.

### Deferred to Implementation

- **CSS Tweaks**: Whether the dot-leader TOC needs minor CSS adjustments to accommodate longer project names or version numbers.

## Implementation Units

- [x] **Unit 1: CMS Schema and Content Foundation**

**Goal:** Define the data model for Projects and update Sveltia CMS configuration.

**Requirements:** R4

**Dependencies:** None

**Files:**
- Modify: `admin/config.template.yml`
- Modify: `content/home.json`

**Approach:**
- In `content/home.json`, add properties for the homepage section: `section_projects`, `section_projects_label`.
- In `admin/config.template.yml`, update the "Home Page" collection to expose the new `home.json` fields.
- In `admin/config.template.yml`, create a new folder collection named "Projects" targeting `content/projects` with `preview_path: 'project-{{slug}}.html'`. Include fields: `title` (required), `slug` (required), `order` (required), `description` (required), `body` (optional), `repository_url` (required), `language` (required), `license` (optional, default: 'MIT'), `version` (optional). Ensure all fields are explicitly defined to prevent data loss.

**Patterns to follow:**
- The existing `Theses` collection definition in `admin/config.template.yml`.

**Test scenarios:**
- Test expectation: none -- configuration only.

- [x] **Unit 2: Build Script - Content Loading and LLM Endpoints**

**Goal:** Load the new projects collection in the build pipeline and inject it into AEO/SEO endpoints.

**Requirements:** R2

**Dependencies:** Unit 1

**Files:**
- Modify: `scripts/build.js`

**Approach:**
- Implement `loadProjects()` mirroring `loadTheses()`. Read from `content/projects/*.md`, parse frontmatter with `gray-matter`, and sort by `order`.
- Update `generateLlmsTxt()`, `generateLlmsFullTxt()`, and `generateContentJson()` to accept the `projects` array.
- Append a new "Projects" section to the text endpoints. Include the `repository_url`, `language`, and `description`.
- Append the `projects` array to the JSON API output.
- Add project URLs to the `generateSitemap()` output.

**Patterns to follow:**
- `loadTheses()` function in `scripts/build.js`.

**Test scenarios:**
- Happy path: `loadProjects()` correctly parses frontmatter and sorts by `order`.
- Happy path: `llms.txt` and `llms-full.txt` contain the new Projects section with repo URLs.
- Happy path: `api/content.json` includes the projects array.
- Edge case: Empty `content/projects` directory does not crash the build.

- [x] **Unit 3: Build Script - Schema.org and UI Generation**

**Goal:** Render the new homepage section and individual project detail pages with rich JSON-LD.

**Requirements:** R1, R3

**Dependencies:** Unit 2

**Files:**
- Modify: `scripts/build.js`

**Approach:**
- Implement `projectSchema(project, settings)` returning the combined `["SoftwareSourceCode", "SoftwareApplication"]` JSON-LD payload. Connect it to the `Person` and `WebSite` entities. Gracefully omit optional fields if absent.
- Implement `renderProjectPage(project, allProjects, settings)` mirroring `renderThesisPage()`. Inject the new schema into the `<head>`. Render the technical metadata (`repository_url`, `language`, `license`, `version`) visibly in the HTML body immediately below the `h1`, using a definition list or a row with `.mono` and `.eyebrow` classes. Output HTML files to `dist/project-[slug].html`.
- Update `renderHomePage()`: Conditionally render a new `.sec-head` for Projects (using labels from `home.json`) directly below the Theses section if `projects.length > 0`. Iterate over the `projects` array to build the dot-leader list, using `pr.` as the prefix for the page number equivalent.
- Update `main()` to execute the new page generation loops.

**Patterns to follow:**
- `renderThesisPage()` and `renderHomePage()` structure.
- `thesisSchema()` for JSON-LD linking.

**Test scenarios:**
- Happy path: Homepage renders the new `.sec-head` and `.toc-ms` list for projects.
- Happy path: Detail pages (`dist/project-[slug].html`) are generated correctly.
- Happy path: The `<head>` of a project detail page contains valid JSON-LD with `"@type": ["SoftwareSourceCode", "SoftwareApplication"]` and the `codeRepository` property.

## System-Wide Impact

- **API surface parity**: The `api/content.json` schema will change to include a top-level `projects` array. Any external consumers (like the OpenClaw agent) will immediately have access to this new data structure.
- **Unchanged invariants**: The core build pipeline sequence (`load -> render -> generate endpoints -> copy assets`) remains identical. Existing Theses and Blog Post processing is untouched.

## Risks & Dependencies

| Risk | Mitigation |
|------|------------|
| Sveltia CMS stripping unmapped frontmatter. | Strict adherence to the institutional learning: absolutely every field used in `content/projects/*.md` is mapped in `admin/config.template.yml`. |
| Vercel build failure due to missing directory. | `loadProjects()` will include an `fs.existsSync(dir)` check and return an empty array if `content/projects` doesn't exist yet, preventing crashes. |