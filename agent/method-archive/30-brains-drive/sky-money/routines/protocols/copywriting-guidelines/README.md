# Copywriting Guidelines — Routing

**Purpose:** Governs all copy creation for this brand. Every piece of copy (social posts, blogs, PR releases, IR newsletters, AEO content, website copy) must follow the source-gathering step and the 5-pass methodology outlined in these guidelines.

**Last updated:** 2026-05-10  
**Approver:** the author  
**Confidence:** confirmed

---

## How to Use This Protocol

When tasked with writing any copy for this brand, follow this sequence. Do not skip steps. Do not proceed to the next step without completing the previous one.

---

### Step 0: Orientation and Source Gathering

**Before drafting any copy, complete these two sub-steps:**

#### 0a. Read Brand Foundation Files

Read these files in order to understand what this brand is, how it speaks, and what it cannot say:

1. **This file** (`routines/protocols/copywriting-guidelines/README.md`) — understand the workflow
2. **`../../memory/strategy/concepts/positioning.md`** — what this brand IS and is NOT
3. **`../../memory/strategy/concepts/brand-voice.md`** — tone, aesthetic principles, approved/banned words
4. **`../../memory/strategy/concepts/legal-guidelines.md`** — what cannot be said, legal triggers, a legal reviewer escalation rules

**If writing for the client product, also read:**
- **`../../memory/strategy/concepts/competitive-landscape.md`** — differentiation claims vs. Aave, a service agent, a service agent, a service agent

**If writing for the client, also read:**
- **`../../memory/strategy/concepts/competitive-landscape.md — differentiation claims vs. Aave, a service agent, a service agent, a service agent
- **`
- **`

**Rule:** Do not proceed to source gathering without reading these orientation files first. Positioning, voice, and legal boundaries inform every subsequent step.

#### 0b. Gather Source Context

Read **`00-source-hierarchy.md`**. This defines where to get factual context for copy and the priority order for sources:

1. a source document (a verified source) — top-priority source
2. Strategy Blueprint — positioning and product facts
3. Brain entity files (`../../memory/strategy/entities/*.md`) — product details, personnel, dashboards
4. Financial dashboard (https://client-example.invalid) — live numbers, never hardcoded
5. Qdrant `sky_context` — semantic memory, use when Brain doesn't cover the topic
6. the author's direct statements — override all when he corrects

**Rule:** Never invent a number. Never use stale numbers. Verify all financial figures against the live dashboard at the moment of writing.

---

### Step 1: Pass 1 — Big Idea (Ogilvy)

Read and follow **`01-pass-1-big-idea.md`**.

**Purpose:** Identify the single compelling idea that anchors all copy. Based on David Ogilvy's principle that every ad should be part of a long-term campaign built on one big idea.

**Output:** A one-sentence statement of the big idea. Everything else serves this idea.

**Rule:** Do not proceed to Pass 2 without a clear big idea. If the big idea is unclear, the copy will be unfocused.

---

### Step 2: Pass 2 — Factual Anchoring

Read and follow **`02-pass-2-factual-anchoring.md`**.

**Purpose:** Every claim in the copy must be traced to a verified source. No unsupported assertions. No marketing fluff.

**Output:** A draft where every factual claim has a cited source (Brain file, dashboard URL, a source document quote, etc.).

**Rule:** If you cannot verify a claim, leave a comment marking it as unverified. Do not invent facts.

---

### Step 3: Pass 3 — Voice Matching

Read and follow **`03-pass-3-voice-matching.md`**.

**Purpose:** Ensure the tone, rhythm, and word choice align with `brand-voice.md`. The copy should sound like this brand, not a generic marketing template.

**Output:** A revised draft that matches the brand's voice — direct, specific, no AI filler, no motivational language.

**Rule:** Do not proceed to Pass 4 without confirming voice alignment. Read the draft aloud — does it sound like the brand?

---

### Step 4: Pass 4 — Storytelling Structure

Read and follow **`04-pass-4-storytelling-structure.md`**.

**Purpose:** Structure the copy as a narrative, not a bullet list. Explain why numbers moved, not just what they are. Create narrative connection between claims.

**Output:** A draft with narrative flow — each sentence leads to the next, building toward the big idea.

**Rule:** If every paragraph is the same length and shape, rewrite. Storytelling means variation, pacing, and narrative connection.

---

### Step 5: Pass 5 — Compliance Gate

Read and follow **`05-pass-5-compliance-gate.md`**.

**Purpose:** Final legal and quality check before submission. Verify banned terms, trigger legal review if needed, apply the review standard.

**Output:** A final draft that passes all compliance checks and is ready for the author's approval.

**Rule:** Do not submit a draft that fails any compliance check. Fix it first.

---

### Step 6: Format Adaptation

After completing all 5 passes, adapt the copy for the specific format:

| Format | Key Constraints | Reference |
|---|---|---|
| Social posts (Twitter/X) | 280 char limit, thread structure, visual pairing | `../../memory/strategy/concepts/brand-voice.md` |
| Social posts (LinkedIn) | Professional tone, longer form, industry context | `../../memory/strategy/concepts/brand-voice.md` |
| PR releases | Press release structure, quote placement, media hook | `../approval-chains.md` (a reviewer quote chain) |
| IR newsletters | the client Insights format, data viz, Kostas/a stakeholder review | `../../memory/strategy/entities/the client-insights.md` |
| AEO copy | LLM citation optimization, entity fact density | `../../memory/strategy/entities/*.md` |
| Blog posts | Long-form structure, SEO, storytelling arc | `../../routines/content-workflow.md` |
| Website copy | Page-specific rules, CTA, legal disclaimers | `../../memory/strategy/entities/the client-money-platform.md` (the client product) |

**Rule:** Each format has unique constraints. Apply the 5-pass method within the format's boundaries.

---

## Cross-References

| I need to know... | Go here |
|---|---|
| What this brand IS | `../../memory/strategy/concepts/positioning.md` |
| Tone and voice rules | `../../memory/strategy/concepts/brand-voice.md` |
| Legal boundaries | `../../memory/strategy/concepts/legal-guidelines.md` |
| Financial terminology | `../../memory/strategy/concepts/financial-terminology.md` (the-client) |
| Competitive positioning | `../../memory/strategy/concepts/competitive-landscape.md` (the client-money) |
| Entity naming rules | `../../memory/strategy/concepts/entity-naming.md` (the-client) |
| Approval chains | `../approval-chains.md` |
| Content workflow | `../content-workflow.md` |
| Storytelling standards, AI filler detection | `../../memory/strategy/concepts/storytelling-and-ai-discipline.md` |
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
