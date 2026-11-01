---
name: prospect-research
description: Research a named business and its relevant people from public sources, verify identities and claims, map how the business works, and identify evidence-backed improvement hypotheses tied to its stated goal.
argument-hint: "[business name and domain; named people if known; stated goal; scope and sources available]"
version: 0.2.1
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Prospect research

## Purpose

This is standard pre-work whenever Alejandro is considering applying his services, offering, or overall advice to a company. Before suggesting anything, understand who the company is, what it is trying to achieve, how its business works, and which people matter to that work. Build a traceable picture of the business and relevant people: business model, observable operations, team background, and the company’s stated goal. Use that evidence to identify possible painful, needed improvements worth validating, then provide grounded context for a pitch, offer, or advice.

This is research, not a sales script or a conclusion that the prospect needs the owner's service. Research findings are not client-approved facts, an audit engagement, or permission to contact anyone. It is a method-only adaptation; the target, sector and business-model hypotheses change by case.

## Use / do not use

Use as the normal first step whenever considering services, an offer, or advice for a company, and whenever asked to research an identified business, its public operations and team, or a named person in relation to that business. Complete enough of this work to understand the company and its goal before suggesting a service, offer, or advice. A bounded initial read can surface open questions, but must not be mistaken for a validated diagnosis.

Do not use to investigate a person without a clear business-related purpose, to gather private or sensitive personal details, to infer private behavior, or to impersonate, contact, follow, connect with, or test access to a prospect. Do not treat public availability as permission to disclose or use sensitive facts. Do not assume the owner has approved outreach, a pitch, or an audit.

If the business or individual cannot be resolved, the goal is missing, or reliable source access is insufficient, report the gap and stop the affected conclusion rather than filling it with a plausible guess.

## Inputs

Minimum inputs for a bounded public-source research brief:

- business's exact name and a primary domain, or enough information to resolve the correct entity;
- the stated business goal, supplied by the owner or a clearly attributed source, or an explicit label that the goal is not yet known;
- the research question and intended decision (for example, whether a possible improvement merits a discovery conversation);
- any named people and their stated relationship to the business, if people research is requested;
- time boundary or recency requirement when the question depends on current operations;
- source, privacy, sector, or confidentiality limits supplied for the assignment.

A reader's name alone is not enough for a business-specific profile. Ask for or verify the business association. If no goal is known, research observable context and open questions, but do not label any issue as a painful priority or write a goal-specific pitch.

## Method

### 1. Frame the question and source plan

- Write the decision the research will support, the entity scope, the business goal and how that goal is known, the time horizon, and the permitted public-source scope.
- Start the brief with an executive summary that distinguishes established findings, provisional interpretations and the key unanswered question. Keep it short enough that a reader can see the evidence boundary before the detail.
- Separate what the owner directly said, what a primary source states, what another source reports, what is inferred, and what is unknown.
- Start with the business's own current pages and materials, regulatory or official records where relevant, named people's professional bios or public work, and credible independent reporting. Follow source links to the underlying record when practical.
- Record the search terms, read/open status, URL, publisher, publication or event date, retrieval date, and any access or recency limits. A search snippet is a lead, not a verified source. Keep a compact source/footprint map showing which relevant surfaces were actually found and checked; distinguish a documented absence in checked sources from a claim that no footprint exists.

### 2. Resolve the business and people before profiling

**Business identity.** Confirm the exact entity by matching its name and domain, and corroborate with an independent current source where possible. Distinguish parent, subsidiary, brand, product and similarly named organizations. If the evidence conflicts or entities cannot be separated, mark the identity unresolved and do not merge facts.

**Person identity.** Confirm a named person's current business, role and relevant professional identity using two sources from independent source groups before treating them as confirmed. A person's own professional profile is one source group; copied bios and syndications are not independent corroboration. Use these statuses:

- `CONFIRMED`: the entity’s official domain/name and business match on two independent source groups; for a person, name, business and relevant role match on two independent source groups.
- `PROBABLE`: one source group supports the match.
- `COLLISION`: plausible same-name people remain; keep them separate.
- `UNRESOLVED`: no adequate match; stop person-specific conclusions.

Only confirmed identities support findings attributed to a specific person. Report probable identity as tentative, never as a fact about the named person.

### 3. Build the evidence ledger

Use one row per claim, with fields such as: `id | claim | evidence label | source(s) | source date | retrieved date | notes / premises`.

Labels:

- `VERIFIED`: supported by at least two independent source groups that were opened and read.
- `REPORTED`: supported by one opened source; attribute the claim to that source.
- `INFERRED`: interpretation derived from cited claim IDs; state the reasoning and keep it distinct from sourced facts.
- `SIGNAL`: weak, ambiguous or indirect indicator; retain only as a lead, never headline it as a finding.
- `UNKNOWN`: a defined question was searched, but no adequate evidence was found; record what was searched.

A claim's date matters. Distinguish when the source was published from when the fact was true. A search result not opened can support at most a lead. Repeated copies of the same underlying statement count as one source group. A missing record means "not found in the sources checked," not that the thing does not exist.

### 4. Map the business and its operating context

Research only dimensions relevant to the stated decision. Typical dimensions:

- **Goal and success:** the organization's stated goal, audience, outcome, constraints and timeframe. Identify whether each came from an owner-provided brief, company statement or inference.
- **Business model:** what it sells or provides; who pays, uses or benefits; value-delivery and revenue model where publicly evidenced; key channels and dependencies; alternatives customers could choose. Do not infer private economics from a business-model label.
- **Operations:** observable workflow, handoffs, channels, tooling or service delivery; evidence of friction, delays, duplication, quality issues, capacity limits or risk. Separate observable facts from possible causes.
- **Team:** relevant leaders and roles; professional background, public responsibilities and work directly connected to the question. Do not create a full employee dossier when only a few roles matter.
- **Market and context:** customer segments, category, competitors/alternatives, public changes or constraints that directly bear on the goal. Use current primary evidence for time-sensitive claims.

For each dimension, report source coverage and gaps. Do not fill a dimension just because a framework has a field for it. Use only relevant categories: identity, offering, market/context, alternatives, history or change, leadership/decision structure, constraints, and strategic context are possible lenses, not mandatory sections. Avoid a full dossier when the decision needs a narrow answer.

Use this goal-first relevance filter before prioritizing research:

1. What core goal does the business state, and what evidence establishes the goal and its timeframe?
2. What does the business provide, for whom, and how does its public evidence show value is delivered and sustained?
3. Which observable customer or internal workflows directly enable that goal?
4. Which relevant people are responsible for decisions or delivery, and what public evidence supports their roles and background?
5. What observed friction, constraint, change, risk, or capability gap may affect the goal, and what alternative explanations exist?
6. What fact would validate or disconfirm that possible connection?

This is a research ordering aid, not a score. If a step lacks evidence, record the gap; don't rank a business as a prospect or infer purchase intent.

### 5. Form improvement hypotheses, not diagnoses

For each candidate, write:

1. **Observed evidence:** the exact sourced facts and their dates.
2. **Possible friction or consequence:** why the facts might matter to the stated goal; label causal links as inference unless a source establishes them.
3. **Hypothesis:** the smallest plausible improvement worth checking, framed conditionally.
4. **What would validate it:** a focused question, measurement, process walkthrough or other evidence needed from the business.
5. **Disconfirming evidence:** what could show the issue is absent, intentional, already solved, or lower priority.
6. **Fit to the goal:** how resolving it could support the stated goal, without promising an outcome.
7. **Owner-method fit:** when this research feeds a pitch, offer or advice, name which of the owner's methods, systems or recurring work could address the hypothesis and what owner-visible output that would produce. A hypothesis with no plausible owner-method connection is a finding to report, not pitch material. This mapping is what lets the later page say concretely how the owner could help; the first live pitch run failed exactly there, with a good brief in hand.

Prioritize using explicit evidence of severity, frequency, affected people, delay/cost/risk, and goal linkage. If impact or frequency is unknown, leave it unranked or mark it a research question. When interpreting sparse or conflicting signals, list plausible benign and adverse explanations in proportion to evidence, then name the next source or question that could distinguish them; do not turn a pattern of missing public evidence into an adverse verdict. Do not label something "painful" merely because it looks inefficient from outside. Do not recommend an offering or pitch unless it is grounded in the owner's current method/offer evidence and the prospect's goal.

### 6. Person-specific professional context

For a confirmed relevant person, report only public professional facts that help explain their role in the business question: current remit, relevant prior roles or work, publicly stated priorities, and decision or delivery responsibilities when evidenced. Use the same claim labels and source rules. Do not infer authority, motives, personality, private relationships, private contact details or willingness to buy from title or social activity. Keep identity evidence separate from relevance inference. Report firm and person profiles separately: the organization’s model, scale indicators, customers, market, channels and operating context belong in its profile; professional background, role and public decision context belong in the person profile. Never fill an organization field with a person’s biography or vice versa.

### 7. Review, check and improve the method

Before any company-directed recommendation, run a check-before-recommendation loop:

1. **Scope:** name the decision, stated goal, time boundary, allowed sources, and a bounded research budget (time or search/fetch limit). Do not start open-ended collection.
2. **Research:** follow the recorded source plan; verify entity and relevant people; capture claims with evidence labels, sources, and dates. Log skipped steps and access failures.
3. **Check-only:** run `python3 agent/packs/prospect-research/scripts/check_brief.py <brief.md>`. A `BLOCK` means fix the missing evidence or narrow/hold the affected conclusion. A `REVIEW` means a human must resolve the warning. The script marks both `BLOCK` and `REVIEW` as not recommendation-ready. Do not apply or recommend first and validate later.
4. **Human review:** inspect source text, independence, entity match, goal source, counterevidence, privacy, freshness, and the specific claim-to-hypothesis chain. Script output cannot authenticate sources or decide whether an opportunity is painful or useful.
5. **Close the loop:** deliver the checked brief with the decision, evidence, gaps, and next validation step. If the owner later supplies corrections or outcome evidence, use it to revise the method/eval fixtures; keep accepted and rejected changes distinguishable. Do not retain prospect records or schedule monitoring unless the task explicitly calls for them and its storage/cadence are authorized.

Define and inspect six process gates in every substantial research run:

- `G-SRC` source integrity: every material factual claim has an opened source and date; verified claims have genuinely independent support; no material claim rests on a snippet alone.
- `G-ID` identity: business and any named person have a resolved identity status; collisions and unresolved matches remain separate, and no attributed person finding is made from an unresolved match.
- `G-GOAL` goal fit: the company goal and source are recorded; no goal-dependent recommendation passes when the goal is missing or only guessed.
- `G-COV` decision coverage: each research dimension needed for the stated decision is marked supported, searched-but-unknown, or not searched; no required dimension is silently omitted.
- `G-COST` bounded effort: planned and actual searches, fetches, elapsed time, and blockers are recorded; work stays within its brief budget or stops for a scope decision.
- `G-USE` validation value: each improvement hypothesis has a goal link, validation step, and disconfirming evidence; at least one next question could materially improve or reject the hypothesis.

Use this bottleneck order for a failed run: `G-SRC` -> `G-ID` -> `G-GOAL` -> `G-COV` -> `G-COST` -> `G-USE`. Fix the earliest failure before increasing breadth or automation. These gates are currently a human-reviewed run checklist plus deterministic brief-format lint; the pack does not yet maintain a case database, measure real cost/precision, schedule collectors, or auto-accept research findings.

### 8. Review, refresh and hand off

- Capture for each run: decision and scope, stated goal/source, time or search/fetch budget, actual searches/fetches and elapsed effort where available, blockers, and status of each applicable process gate. This is a brief-level human record today; there is no collector, shared ledger or cost integration.
- Check every material claim against its cited opened source. Recheck current roles, products, business status and recent events at the point they will be used.
- Read for entity conflation, stale claims, unsupported causal explanations, privacy risk, missing counterevidence and facts drawn from snippets only.
- Keep the report proportional to the decision; include a concise coverage/gaps list and the highest-value next evidence needed.
- When the owner asks for a custom pitch, hand verified facts, hypotheses, the hypothesis-to-method mapping, and open questions into `pitch-website`; do not silently treat a research hypothesis as approved positioning or public copy. For any company-directed service, offer, or advice consideration, this research is standard operating pre-work, not an optional reference lookup. If the work cannot be done first, state the evidence gap and hold any recommendation that depends on it.

## Output contract

Deliver a compact research brief with:

1. a short executive summary of established findings, provisional interpretations and the main open question;
2. decision, scope, goal and how the goal was sourced;
3. business identity and confidence;
4. business-model and operating map, with claims tagged and sourced;
5. relevant people and identity/role status, only when requested;
6. candidate improvement hypotheses with evidence, goal link, validation and disconfirmation questions;
7. a concise source/footprint map noting relevant surfaces found and checked, plus source list and read dates;
8. confidence/uncertainty notes, gaps, conflicts, recency limits, and what was not searched.

Keep external reporting plain and bounded. Do not include unnecessary personal information, raw private identifiers, or a sales script.

## Quality checks

A reviewer should be able to answer:

- Is the business the right entity, and are similarly named people/entities kept separate?
- Can every asserted fact be traced to an opened source and its date? Are independent sources genuinely independent?
- Are facts, source-reported claims, inference, weak signals and unknowns clearly distinguished?
- Does the stated goal have a source? If unknown, are conclusions limited accordingly?
- Does each proposed improvement link to evidence and that goal, with validation and disconfirmation paths?
- Are private or sensitive personal data and unrelated client details absent?
- Are current, role, product and operational claims fresh enough for the decision?

A clean checklist means only that these checks found no listed problem. It does not prove the research is complete, the pain is real, or the proposed change is right.

### Process eval and graduation path

Current support is deliberately bounded to static fixture evals, a zero-dependency CLI linter, offline tests, and a human-run review loop. The six process gates above are criteria, not yet a metrics database or scheduled runner. Do not describe this pack as having automated monitoring, per-business spend telemetry, unattended research, or autonomous decision-making.

Graduation path, only when repeated real cases justify it:

1. **Baseline:** keep the present check-only script, expand fixtures for identity collisions, stale evidence, conflicting sources, missing goal, private data and false pain claims; have the owner review held-out cases.
2. **Explain:** define a case record with scope, goal source, permitted sources, planned/actual budget, claims, gate outcomes, gaps, and owner corrections. Measure gate agreement and edit/reject reasons before setting thresholds.
3. **Bounded workflow:** add optional local, explicit-input work packets with machine-checkable source/claim fields and a check-only/apply split; append run/audit events instead of overwriting prior decisions. Do not add prospect data retention by default.
4. **Measured cadence:** only if asked, design a company-specific budget, source freshness window, review cadence, privacy/retention rules, and stop conditions. Any monitoring should emit candidate changes for review, not silently promote them into facts or advice.
5. **Automation gate:** measure precision, missed changes, cost per decision, source health, coverage and human acceptance over multiple cases. Automate only the narrow checks that meet owner-approved thresholds; keep identity conflicts, pain judgments, strategic fit, and recommendations human-reviewed.

This path is a proposal for future method development, not implemented capability or authorization to monitor companies.

## Hard boundaries

- Public information only, using sources in ways consistent with applicable law and source terms; no pretexting, bypassing access controls, contacting people, or writing to third-party systems as part of this research method.
- No passwords, personal contact details, private social handles, home addresses, sensitive personal data, or inferred sensitive attributes in the report.
- No unsupported claims about results, revenue, costs, intent, internal operations, pain, or buying readiness.
- No mixing facts across same-name people or parent/child/brand entities.
- Research can inform a later reader-specific pitch; it does not authorize contacting anyone, publishing, or retaining a persistent prospect profile. Follow the assignment's approval and retention rules.

## Provenance and limits

The upstream reusable person-research method draws on two earlier source methods: a client-research approach and a professional intelligence-card approach. Its identity-first gate, independent source groups, one-row-per-claim ledger, five evidence labels, ordered relevance filter, public-source restraint, and explicit gaps are the source-method elements retained here. Its client roster, instance configuration, specialized relevance tests and numeric scoring are not retained.

The owner supplied two original OSINT method samples for this generalization: a broad business-research method and a targeted professional intelligence-card method. Their generalizable patterns were used only as structure: a short executive summary; a checked-source footprint map; separation of verified material from inference; an ordered research/source plan; explicit source-quality and uncertainty notes; contextual business lenses (identity, offering, market, alternatives, history, leadership, constraints and strategic context); and explicit data gaps with validation steps. No client facts, sector-specific claims, identifiers, recommendations, or numeric rankings from those documents are included. No target/client names or target-specific facts from either source are reproduced here.

The business-model, operations, team background, goal linkage and improvement-hypothesis sections are general-purpose extensions based on the owner’s direct instruction on 2026-10-31. This adaptation is still draft; it has not been validated as a universal method across businesses.

## References

- `agent/packs/strategy-canvas/skills/strategy-canvas/SKILL.md` for sourced/inferred/gap strategy work.
- `agent/packs/audience-listening/skills/audience-listening/SKILL.md` when the question concerns an audience's public behavior.
- `agent/skills/pitch-website/SKILL.md` for turning verified research into a reader-specific page.
