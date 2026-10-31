---
type: protocol
brand: the-client
tags: [the-client]
---

# Pass 2: Factual Anchoring

**Purpose:** Every claim in the copy must be traced to a verified source. No unsupported assertions. No marketing fluff.

**When to use:** After Pass 1 (Big Idea) is complete. Apply to every factual claim in the draft.

---

## The Rule

Every factual claim must have a source. If you cannot verify a claim, mark it as unverified and flag it for [[../../../people/the author-arango|the author]].

**Factual claims include:**
- Numbers (TVL, yield rates, revenue, user counts)
- Product features (what sample-yield-token does, how [[../../../memory/strategy/atlas/mechanisms/ssr|sample-rate]] works)
- Personnel (who does what, who approves what)
- Timelines (launch dates, governance votes)
- Competitive claims ("safest," "best risk-adjusted yield")
- Regulatory statements ("compliant with X regulation")

---

## How to Anchor Facts

### Step 1: Identify Every Claim

Read through the draft and highlight every factual claim. Ask: "Can I prove this?"

### Step 2: Trace to Source

For each claim, identify the source using the source hierarchy (see [[00-source-hierarchy|00 Source Hierarchy]]):

| Claim Type | Source |
|---|---|
| Yield rates, TVL, revenue | https://client-example.invalid (live dashboard) |
| Product definitions | a source document or Strategy Blueprint |
| Personnel roles | Brain entity files (`../../memory/strategy/entities/*.md`) or `../../people/*.md` |
| Positioning statements | a source document (supreme) or [[routines/protocols/copywriting-guidelines/positioning|Positioning]] |
| Legal boundaries | [[routines/protocols/copywriting-guidelines/legal-guidelines|Legal Guidelines]] |
| Competitive claims | [[routines/protocols/copywriting-guidelines/competitive-landscape|Competitive Landscape]] (the client product) or verified OSINT |

### Step 3: Cite the Source

Add a comment or footnote for each claim showing the source. Example:

```
sample-yield-token offers the best risk-adjusted yield in DeFi. [Source: a source document, p. 3; client-example.invalid, checked 2026-05-10]
```

### Step 4: Flag Unverified Claims

If you cannot verify a claim, mark it clearly:

```
[UNVERIFIED: Need a stakeholder confirmation on this claim about sample-rate governance mechanism]
```

Do not proceed to Pass 3 with unverified claims still in the draft. Resolve them first.

---

## What Not to Do

- **Do not invent numbers.** If the dashboard doesn't show it, escalate — do not estimate.
- **Do not paraphrase [[../../../people/a reviewer-christensen|a reviewer]] quotes.** Use verbatim quotes only, with attribution.
- **Do not use stale numbers.** Any number older than 24 hours should be re-verified.
- **Do not attribute statements to people who didn't say them.** Verify quotes with the source.
- **Do not claim product features that don't exist.** Cross-reference entity files.

---

## Output of Pass 2

A draft where every factual claim has a cited source. Unverified claims are flagged and pending resolution.

---

## Cross-References

- Source hierarchy: [[00-source-hierarchy|00 Source Hierarchy]]
- Financial terminology: [[routines/memory/strategy/concepts/financial-terminology|Financial Terminology]] (the-client)
- Storytelling standards: [[routines/memory/strategy/concepts/storytelling-and-ai-discipline|Storytelling And Ai Discipline]]
