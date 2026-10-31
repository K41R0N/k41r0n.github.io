---
type: hub
brand: the-client
tags: [the-client]
---

# Copywriting Guidelines — Routing

**Purpose:** Governs all copy creation for this brand. Every piece of copy (social posts, blogs, PR releases, IR newsletters, AEO content, website copy) must follow the source-gathering step and the 5-pass methodology outlined in these guidelines.

**Last updated:** 2026-05-10  
**Approver:** [[../../../people/the author-arango|the author]] Arango  
**Confidence:** confirmed

---

## How to Use This Protocol

When tasked with writing any copy for this brand, follow this sequence. Do not skip steps. Do not proceed to the next step without completing the previous one.

---

### Step 0: Orientation and Source Gathering

**Before drafting any copy, complete these two sub-steps:**

#### 0a. Read Brand Foundation Files

Read these files in order to understand what this brand is, how it speaks, and what it cannot say:

1. **This file** (Readme) — understand the workflow
2. **[[routines/memory/strategy/concepts/positioning|Positioning]]** — what this brand IS and is NOT
3. **[[routines/memory/strategy/concepts/brand-voice|Brand Voice]]** — tone, aesthetic principles, approved/banned words
4. **[[routines/memory/strategy/concepts/legal-guidelines|Legal Guidelines]]** — what cannot be said, legal triggers, a legal reviewer escalation rules

**If writing for the client product, also read:**
- **[[routines/memory/strategy/concepts/competitive-landscape|Competitive Landscape]]** — differentiation claims vs. Aave, [[../../../memory/strategy/entities/spark|a service agent]], [[../../../memory/strategy/entities/service-agent|a service agent]], [[../../../memory/strategy/entities/service-agent|a service agent]]

**If writing for the client, also read:**
- **[[routines/memory/strategy/concepts/financial-terminology|Financial Terminology]]** — banned financial terms, required terminology, source-of-truth rules
- **[[routines/memory/strategy/concepts/entity-naming|Entity Naming]]** — the client Protocol vs. the client vs. the client Governance vs. [[../../../memory/strategy/entities/sff|a protocol body]]
- **[[routines/memory/strategy/concepts/institutional-messaging|Institutional Messaging]]** — institutional allocator framing

**Rule:** Do not proceed to source gathering without reading these orientation files first. Positioning, voice, and legal boundaries inform every subsequent step.

#### 0b. Gather Source Context

Read **[[00-source-hierarchy|00 Source Hierarchy]]**. This defines where to get factual context for copy and the priority order for sources:

1. a source document ([[../../../people/a reviewer-christensen|a reviewer]]-approved, verbatim) — top-priority source
2. Strategy Blueprint — positioning and product facts
3. Brain entity files (`../../memory/strategy/entities/*.md`) — product details, personnel, dashboards
4. Financial dashboard (https://client-example.invalid) — live numbers, never hardcoded
5. Qdrant `sky_context` — semantic memory, use when Brain doesn't cover the topic
6. the author's direct statements — override all when he corrects

**Rule:** Never invent a number. Never use stale numbers. Verify all financial figures against the live dashboard at the moment of writing.

---

### Step 1: Pass 1 — Big Idea (Ogilvy)

Read and follow **[[01-pass-1-big-idea|01 Pass 1 Big Idea]]**.

**Purpose:** Identify the single compelling idea that anchors all copy. Based on David Ogilvy's principle that every ad should be part of a long-term campaign built on one big idea.

**Output:** A one-sentence statement of the big idea. Everything else serves this idea.

**Rule:** Do not proceed to Pass 2 without a clear big idea. If the big idea is unclear, the copy will be unfocused.

---

### Step 2: Pass 2 — Factual Anchoring

Read and follow **[[02-pass-2-factual-anchoring|02 Pass 2 Factual Anchoring]]**.

**Purpose:** Every claim in the copy must be traced to a verified source. No unsupported assertions. No marketing fluff.

**Output:** A draft where every factual claim has a cited source (Brain file, dashboard URL, a source document quote, etc.).

**Rule:** If you cannot verify a claim, leave a comment marking it as unverified. Do not invent facts.

---

### Step 3: Pass 3 — Voice Matching

Read and follow **[[03-pass-3-voice-matching|03 Pass 3 Voice Matching]]**.

**Purpose:** Ensure the tone, rhythm, and word choice align with [[routines/protocols/copywriting-guidelines/brand-voice|Brand Voice]]. The copy should sound like this brand, not a generic marketing template.

**Output:** A revised draft that matches the brand's voice — direct, specific, no AI filler, no motivational language.

**Rule:** Do not proceed to Pass 4 without confirming voice alignment. Read the draft aloud — does it sound like the brand?

---

### Step 4: Pass 4 — Storytelling Structure

Read and follow **[[04-pass-4-storytelling-structure|04 Pass 4 Storytelling Structure]]**.

**Purpose:** Structure the copy as a narrative, not a bullet list. Explain why numbers moved, not just what they are. Create narrative connection between claims.

**Output:** A draft with narrative flow — each sentence leads to the next, building toward the big idea.

**Rule:** If every paragraph is the same length and shape, rewrite. Storytelling means variation, pacing, and narrative connection.

---

### Step 5: Pass 5 — Compliance Gate

Read and follow **[[05-pass-5-compliance-gate|05 Pass 5 Compliance Gate]]**.

**Purpose:** Final legal and quality check before submission. Verify banned terms, trigger legal review if needed, apply the review standard.

**Output:** A final draft that passes all compliance checks and is ready for the author's approval.

**Rule:** Do not submit a draft that fails any compliance check. Fix it first.

---

### Step 6: Format Adaptation

After completing all 5 passes, adapt the copy for the specific format:

| Format | Key Constraints | Reference |
|---|---|---|
| Social posts (Twitter/X) | 280 char limit, thread structure, visual pairing | [[routines/memory/strategy/concepts/brand-voice|Brand Voice]] |
| Social posts (LinkedIn) | Professional tone, longer form, industry context | [[routines/memory/strategy/concepts/brand-voice|Brand Voice]] |
| PR releases | Press release structure, quote placement, media hook | [[routines/protocols/approval-chains|Approval Chains]] (a reviewer quote chain) |
| IR newsletters | the client Insights format, data viz, [[../../../people/kostas|Kostas]]/a stakeholder review | [[routines/memory/strategy/entities/the client-insights|the client Insights]] |
| AEO copy | LLM citation optimization, entity fact density | `../../memory/strategy/entities/*.md` |
| Blog posts | Long-form structure, SEO, storytelling arc | [[routines/routines/content-workflow|Content Workflow]] |
| Website copy | Page-specific rules, CTA, legal disclaimers | [[routines/memory/strategy/entities/the client-money-platform|the client product Platform]] (the client product) |

**Rule:** Each format has unique constraints. Apply the 5-pass method within the format's boundaries.

---

## Cross-References

| I need to know... | Go here |
|---|---|
| What this brand IS | [[routines/memory/strategy/concepts/positioning|Positioning]] |
| Tone and voice rules | [[routines/memory/strategy/concepts/brand-voice|Brand Voice]] |
| Legal boundaries | [[routines/memory/strategy/concepts/legal-guidelines|Legal Guidelines]] |
| Financial terminology | [[routines/memory/strategy/concepts/financial-terminology|Financial Terminology]] (the-client) |
| Competitive positioning | [[routines/memory/strategy/concepts/competitive-landscape|Competitive Landscape]] (the client-money) |
| Entity naming rules | [[routines/memory/strategy/concepts/entity-naming|Entity Naming]] (the-client) |
| Approval chains | [[routines/protocols/approval-chains|Approval Chains]] |
| Content workflow | [[routines/protocols/content-workflow|Content Workflow]] |
| Storytelling standards, AI filler detection | [[routines/memory/strategy/concepts/storytelling-and-ai-discipline|Storytelling And Ai Discipline]] |
| a source document (top-priority source) | a source document document (a source-reviewed) |
| Live financial data | https://client-example.invalid |

---

## Critical Rules

1. **No Brief = No Work.** If there's no brief in Notion, stop and ask the author.
2. **a source document is supreme.** If anything conflicts with the a source document, the Playbook wins.
3. **5 passes are mandatory.** Do not skip any pass. Do not combine passes.
4. **Source gathering comes first.** Complete Step 0 before executing the 5 passes.
5. **Never invent a number.** Verify against https://client-example.invalid at the moment of writing.
6. **the author is final approver.** All copy requires the author sign-off before publication.
