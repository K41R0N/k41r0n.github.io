---
source_path: K41R0N/k41r0n.github.io/content/projects/opensource-curriculum.md
venue: kairon.xyz
register: project page
self_written: UNVERIFIED
excluded_reason: authorship unverified: repo documents an agent rewrite of content/pages/about.md (docs/solutions/workflow-issues/agent-copy-boundary-violation-2026-05-31.md); project pages likely agent-assisted
status: pending Alejandro authorship confirmation
---

## Overview

The Open Source Curriculum project is a frontend-driven platform designed to democratize the creation and distribution of self-guided educational content. Built on a serverless architecture, it empowers educators and creators to publish structured courses without managing databases or backend infrastructure. 

By leveraging **Svelte** for reactive UI rendering and **Sveltia CMS** for Git-based content management, the system provides a seamless editorial experience. All curriculum data is stored as flat Markdown and JSON files in the repository, making it perfectly suited for edge deployment via **Netlify CDN**.

## Core Problem Solved

Traditional Learning Management Systems (LMS) are often bloated, expensive, and require significant DevOps overhead. They lock content into proprietary databases, making version control and collaborative editing difficult. This project solves this by treating "Content as Code."

Educators can draft lessons in standard Markdown, define curriculum structures in simple JSON arrays, and rely on Git to track changes over time. Because the output is entirely static, hosting costs are near zero, and page load speeds are instantaneous anywhere in the world.

## Key Features

- **Git-Backed Content Management:** Integrated directly with Sveltia CMS (a modern, lightweight alternative to Decap CMS). Content editors get a clean UI, while developers retain absolute control over the data schema via `config.yml`.
- **Reactive Svelte Architecture:** The frontend is built with Svelte, ensuring minimal bundle sizes and ultra-fast client-side routing.
- **Serverless Edge Delivery:** Pre-configured for Netlify, allowing the entire curriculum to be distributed across global edge nodes for maximum performance.
- **Schema-Driven Syllabi:** Course modules, lessons, and reading materials are dynamically generated from structured JSON schemas, making it trivial to reorder or expand courses.
- **AEO / SEO Optimized Output:** The static build process outputs semantic HTML and JSON-LD structured data, ensuring search engines and AI crawlers can effectively index the educational material.

## Technologies Used

- **Svelte / SvelteKit:** Component framework and static site generation.
- **Sveltia CMS:** Git-based editorial interface.
- **Netlify:** Continuous deployment and edge hosting.
- **Markdown / JSON:** Primary data stores.
