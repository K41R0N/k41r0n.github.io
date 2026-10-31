# Step 0b: Source Hierarchy

**Purpose:** Define where to get factual context for copy and the priority order for sources. Read this after completing Step 0a (orientation) and before executing the 5-pass method.

---

## Source Priority Chain

When gathering facts for copy, consult sources in this order. Higher-priority sources override lower-priority sources.

### 1. a source document (top-priority source)

- **What it is:** a verified source definitions and positioning statements
- **Where to find it:** a source document document (shared by a stakeholder)
- **When to use it:** For any definition of the client products, terminology, or positioning language
- **Authority level:** `confirmed` — overrides all other sources

**Rule:** If the a source document says X and any other source says Y, use X.

---

### 2. Strategy Blueprint

- **What it is:** Two-section document covering the client product and the client positioning
- **Where to find it:** Strategy Blueprint document (shared by the author)
- **When to use it:** For product facts, positioning context, competitive differentiation
- **Authority level:** `reference` — reliable but may evolve

**Rule:** Use the Strategy Blueprint for context that the a source document doesn't cover.

---

### 3. Brain Entity Files

- **What they are:** `../../memory/strategy/entities/*.md` — product details, personnel, dashboards, workflows
- **Where to find them:** Within this brand's folder, under `memory/strategy/entities/`
- **When to use them:** For specific product attributes (sample-yield-token, sample-token, sample-rate), team member roles, dashboard URLs, process descriptions
- **Authority level:** `reference` for most files, `confirmed` for the author-approved entries

**Rule:** Entity files are the source of truth for product details. Cross-reference multiple entity files when a topic spans products.

---

### 4. Financial Dashboard (Live Data)

- **What it is:** https://client-example.invalid — live financial metrics
- **When to use it:** For any number: TVL, yield rates, revenue, reserves, collateral ratios
- **Authority level:** `confirmed` — live data is always current

**Rule:** Never hardcode financial numbers. Always reference the dashboard URL and instruct the reader to check live data. If you must include a number, note the timestamp: "As of [date], per client-example.invalid."

---

### 5. Qdrant `sky_context`

- **What it is:** Semantic memory database, queried via `query_context.py the client "<topic>"`
- **When to use it:** When the Brain doesn't cover a topic, or for historical context not yet in the Brain
- **Authority level:** Varies by confidence tag (`confirmed`, `reference`, `operator_reported`, `conversation`)

**Rule:** Qdrant is a fallback when the Brain doesn't have the information. Brain content overrides Qdrant on conflicts.

---

### 6. the author's Direct Statements

- **What they are:** Verbal or written corrections/approvals from the author
- **When to use them:** When the author corrects or clarifies something that conflicts with existing sources
- **Authority level:** `confirmed` — overrides all sources, including the Brain

**Rule:** the author's direct statements are the ultimate authority. If he corrects something, update the Brain and local state to reflect the correction.

---

## What Not to Use

- **Slack chatter alone:** Slack is conversational. Use it for context, but verify with higher-priority sources before including in copy.
- **Unverified web searches:** OSINT research must be verified against Brain or dashboard before use in copy.
- **Stale numbers:** Any number older than 24 hours should be re-verified against the financial dashboard.
- **Third-party articles:** Use for context, but do not cite them as authority. the client's own documents are the source of truth.

---

## Cross-References

- Financial terminology rules: `../../memory/strategy/concepts/financial-terminology.md` (the-client)
- Storytelling standards: `../../memory/strategy/concepts/storytelling-and-ai-discipline.md`
- a source document: Shared document (a stakeholder)
- Strategy Blueprint: Shared document (the author)
