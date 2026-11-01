---
name: pitch-website
description: Plans, drafts, deploys, and verifies a reader-specific pitch website grounded in the owner's methods and evidence.
argument-hint: "[reader or organization, decision the page should support, and available source material]"
version: 0.3.0
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Pitch website

## Purpose

Create a concise, reader-specific website that explains a concrete offering and why it may matter to this reader. Ground the page in the owner's actual methods and evidence. Use specific examples to make the work understandable, distinguish facts from hypotheses, and make the next step clear without promising unsupported results.

This skill is a workflow, not a source of strategy or permission. It does not validate an offer, authorize outreach, or approve public claims. The accountable person decides positioning and approves words sent or published in their name.

## When to use / not

Use when preparing a shareable pitch page for a named person, organization, or well-defined audience. It can also produce a draft outline for review.

Do not use it to decide a still-undefined offering by inventing buyer needs, to claim a pilot or client result that has not happened, or to publish/send without the required approval. If the evidence is too thin to state a clear offer or reader value, produce a short source-backed brief with gaps and stop before presenting guesses as a pitch.

## Step 0: orient and read sources

1. Establish the reader, their organization and role, the decision the page should support, the intended channel, the requested next step, and whether this is an example, proposal, or live offer. Use current brief and direct evidence; do not infer a relationship or business need from the name alone.
2. Read the site's contribution instructions and write guard before editing. Inspect current repository state, deploy path, branch rules, and any existing page or template. Never edit generated output.
3. Read the actual canonical Harness Standard and Attention Graduation Framework before describing harness types or attention stages. Use current, relevant sources in the ICP harness for audience signals and audience understanding, and the marketing harness for offering, market, alternatives, positioning, and value. One agent may draw from multiple harnesses; keep those method sources distinct and route by the question being answered.
4. Read the public methods repo's `clear-message`, `copywriting-methods`, `copy-five-pass`, and `strategy-canvas` guidance. Read audience-listening and attention-graduation methods when explaining those methods. Use `prospect-research` as standard pre-work before considering any service, offer, or advice for a company, and as the evidence feeder for reader-specific pitch tailoring. Do not treat it as optional reference material or turn its hypotheses into approved positioning. Read any reader-relevant project evidence and design system. Say what was not available or read.
5. Maintain a claim/source ledger in working notes: sourced fact, owner-reported experience, inference, or open gap. A citation is evidence to check, not blanket permission to disclose it.
6. Confirm the deployment surface and the reader's language before building. Ad-hoc prospect pages go to here.now by default, with the page link, expiry, and claim link reported. Write the page in the reader's own language from the start; translating after drafting ships English structure with local words.

## Goals and completion test

Before building, state a testable page goal (what this reader should understand, decide, or do) and its requested next step. Do not substitute page views or a generic "learn more" for a real decision.

A page is ready for human review when it:

- identifies the reader and makes clear why the page is for them;
- states one clear central idea and a specific, evidence-bounded offering or method;
- explains the reader's relevant problem or context without pretending unknown needs are known;
- shows how the work operates through one or more concrete, clearly labelled examples;
- makes the unique value proposition (UVP) a substantiated difference, not an adjective;
- explains the attention framework and harness structure only as much as needed to understand the offer;
- distinguishes what is established, reported, inferred, illustrative, and unknown;
- includes a specific next step consistent with the actual relationship and offer;
- passes the copy, positioning, privacy, visual, responsive, and deployment checks below.

A clean check means only that the listed checks passed. It does not establish that the offer is strategically right or that the reader will respond.

## Required sections

Adapt order and length to the reader; do not force a long framework glossary. Include the following functions, combining or omitting only when the reason is clear:

1. **Reader-specific opening:** name the reader's situation, with evidence; do not flatter or pretend intimate understanding.
2. **Central idea and offering:** one sentence for the core point, then what is offered, to whom, and what bounded problem it addresses.
3. **Why it matters / UVP:** show the cost, friction, or opportunity the reader may recognize, then the evidence-backed difference from plausible alternatives. Separate the reader's verified facts from hypotheses.
4. **Concrete worked example:** demonstrate the method from input to steps to artifact or decision. Mark it as illustrative when it is not the reader's actual work; do not imply deployment or results that did not occur.
5. **How the method works:** explain the relevant harnesses and attention progression in plain language. Harness types must match the canonical standard. Explain composition: a task-capable agent can consult several relevant harnesses, rather than treating each agent as a single-purpose tool. When relevant, show the five depth rungs (Describe, Explain, Predict, Estimate, Delegate) and all seven attention slots (Strategize, Suspect, Anticipate, Act, React, Recognize, Calculate) through the same concrete task.
6. **Proof and boundaries:** cite inspected examples or sources, state what is not yet proven, and avoid confidential client details without explicit permission.
7. **Next step:** propose one concrete, low-ambiguity action that has actually been discussed or authorized. No invented pricing, pilot commitment, guarantees, or urgency.

The example is the explanation. Avoid leading with repository plumbing, a taxonomy, or broad claims that the page body cannot substantiate. Add technical detail on portability only after showing what the method does; qualify compatibility as a goal or reported experience unless verified for the reader's specific setup.

## Hard rules for every pitch page

- **No meta commentary in reader-facing copy.** The page contains the pitch, not notes about drafting, review, research limits, internal process, or why the page was made. This is a publish-blocking gate, not a style preference.
- **Answer how the work helps this reader.** Explain the actual offering through the prospect's context and business goal. A generic description of the owner's capabilities is not enough.
- **Make the proposal tangible.** Use the prospect research and relevant methods in the library to name the tools, processes, agent harnesses, recurring work and owner-visible outputs that fit this prospect. Separate a proposed setup from anything already deployed; never invent their workflow, priority or results.

## Pre-publish gate

Nine blocking checks. Run them in order on the final page, before any review link goes out, and report the evidence for each. A failure stops the publish; these are gates, not style preferences. Six of the nine owner corrections on the first live run repeated rules that already existed in this skill but were not enforced before publishing.

A gate passes on evidence, not wording. Evidence means the methodology sources were actually read and applied to this reader, the demonstration genuinely shows the method working, and a reader could say what the offer is, why it is for them, and what happens next. A checked-off list proves only that the known failure modes were reviewed; it is not proof that the pitch is good, that the run was faster, or that the page will work. Quality stays with the owner's review.

0. **Deployment surface confirmed.** The page is on the surface confirmed at orientation (default: here.now). Page link, expiry, and claim link reported. Never substitute another hosting surface without saying so.
1. **Reader language.** The page is written in the reader's own language, and the five passes ran on that final language version, not on an earlier draft in another language. Reader-facing copy carries no English terms and no technical vocabulary; method concepts appear as plain questions and everyday words the reader would use.
2. **Why first.** The opening leads with the reader's outcome, before any how. Implementation, tools, and infrastructure stay invisible unless the reader asks.
3. **No meta commentary.** Nothing about drafting, review, research limits, or internal process appears on the page.
4. **Tangible and prospect-specific.** The page explains how the offering helps this reader using the actual method library: named setup, recurring work, and owner-visible outputs grounded in the prospect research. A generic capability description fails.
5. **Ownership.** The page shows what is tangibly the owner's: the perks of his systems and approaches, and the attention framework with its actual steps, in client-facing language. A pitch that could have come from any consultant fails.
6. **Show, don't tell.** When the page explains a method, it includes an interactive demonstration that teaches: the reader moves through the steps and sees what changes. Every element must demonstrate; nothing merely decorates.
7. **Restraint.** No eyebrow components, stickers, stripes, or other superfluous elements. The design pass ran against the prospect's own design language.
8. **Compound gap pass.** Before the first review link goes out, run a compound-engineering review of the draft against the whole method library: which relevant method was not used, which claim lacks grounding, what the reader cannot understand from the page alone. Record the findings and fix them before publishing. See `routines/second-pass.md`.

## Procedure

### 1. Position the page

- Use `strategy-canvas` for the offering, alternatives, audience, and position when the required sources exist. Preserve its sequence and provenance tags; do not cherry-pick a convenient conclusion.
- Use `audience-listening` or the ICP harness's relevant methods to verify the audience context and terminology. Audience monitoring is not the same as market positioning.
- Name the competitor or alternative only when evidence supports it. Ask the strategic question: "Who are you stealing market share from and how is the smartest way to do it?" Treat an unsupported answer as a research gap, not copy.
- Write the central idea, target reader, reader's reason to care, UVP, example, and requested next step in a brief before designing the page.
- Write the method selection record before drafting: for each method from the library this page will use, name the method, the file it was read from during this run, and the section of the page it shapes. The first live run's fluffy draft came from skimming the library instead of selecting from it; the record is the evidence that the whole methodology book was used, not browsed. Attach the record to the review report.

### 2. Build the argument and draft copy

- Follow the five-pass method: big idea; factual anchoring; voice; story structure; compliance. Every factual or comparative claim must trace to current evidence. Leave uncertain claims out or visibly mark them for resolution.
- Use `clear-message` to reduce the explanation to what this reader needs to understand. Replace generic adjectives with actions, examples, and inspectable artifacts.
- Make the worked example answer: what starts the process, what happens, what the reader can inspect or decide, and what remains human judgment.
- Explain the Attention Graduation Framework accurately: Describe what happens, Explain why and what good means, Predict what changes under different conditions, Estimate time/cost from evidence, and only then consider bounded delegation. Do not skip stages or claim the page established automation readiness. Use its canonical framework for exact ladder, seven slots and thresholds.
- For a teaching example, map the same task across the seven slots: Strategize (goal and plan), Suspect (risks and conflicts), Anticipate (inputs and preflight), Act (the work), React (known failures), Recognize (check whether output is valid), Calculate (cause, cost and learning). The task determines the contents; do not force unrelated content into a slot.
- Preserve the difference between a method, a deployed implementation, and a business outcome. Don't turn portability into a universal compatibility guarantee.
- Customize names, examples, visuals, and details from reader-relevant evidence. Never expose another person's private context or confidential client data merely because it would make the pitch persuasive.

### 3. Design and implement

- Use Impeccable for the design review when available; use the target website's current `design.md` or equivalent as the source of truth for palette, typography, and interaction conventions. Do not substitute Impeccable sample colors for the owner's design system. Prefer restraint: every visual element should clarify the offer, example, or next step.
- When a sequential worked example benefits from it, prefer a step-by-step interactive demonstration: let the reader move through the ladder/interview and see how a bounded rule changes an example output. Interaction must teach the method, not decorate it. A control must visibly change the example or progression and remain usable by keyboard and touch. Do not add motion or UI solely for novelty.
- Keep sections scannable, but let the explanation develop enough to connect the reader's problem, the method, evidence, and next step. Public-facing pages must not include internal review notes or meta commentary. Do not add future-facing product or roadmap claims unless the task explicitly calls for a proposal and each statement is clearly framed as uncommitted.
- Implement in the site's source files and follow its repository write guard. Do not edit generated `dist/` files.
- Keep secrets, private source documents, and unrelated client context out of the deployed page, repository history, screenshots, and metadata.

### 4. Deploy

Deployment is repository-specific. Read the target repo's current contribution and deploy instructions, and verify the current hosting source before acting. For this site, use `agent/knowledge/site/contribution-workflow.md` and `agent/knowledge/site/repo-architecture.md`:

1. Make a descriptive branch from the current `main` or the branch assigned to the task, then inspect the diff.
2. For changes under `agent/` or other Tier 2 documentation, use the repository's authorized branch + PR workflow, or an authorized CMS commit only for pure content the owner would otherwise edit in the CMS. Do not use the CMS for harness/process changes. Never infer a push-to-main exception from the existence of a write permission. Tier 1 paths require the forcing function in the portfolio write guard and the approved PR route.
3. For an actual public site page, use the approved content or code path. Run the required site build and validation; never bypass a failed check.
4. Commit one logical change with a descriptive message. Before every push, run `bash agent/scripts/local/push_gate.sh agent` and stop if it fails; then push only to the authorized branch and open a PR when the workflow/request calls for it. Report the exact commit or PR URL and whether it has merged.
5. A commit or PR is not a deployment. For this site, the current documented production path is Cloudflare Workers Builds watching `main`; Vercel is the bare-domain redirect/rollback path. Do not claim live publication until the deployment and page are checked.
6. If no deploy access is available or permission is unclear, prepare the implementation and report the exact remaining step. Do not improvise credentials, alter infrastructure, or publish as a workaround.

## Verification passes

Run and report each applicable check separately; do not claim a pass that did not happen.

### Positioning and fit

- Can a reader explain the offer and why it is relevant after the opening and example?
- Does the page answer who it is for, what problem it addresses, how it works, why it differs, and what happens next?
- Is every comparison grounded? Is the alternative really what this reader might choose instead?
- Does the prose match the page's actual example, or does the opening promise more than the rest delivers?

### Evidence and copy

- Read every cited source. Verify every fact, number, product capability, outcome, quote, comparison, date, and person against its current primary source.
- Mark sourced, owner-reported, inferred, illustrative, and unknown material distinctly in working notes. Remove or resolve unsupported public claims and placeholders.
- Run `clear-message`, then the full five-pass copy method. Run `python3 evals/run.py copy-five-pass` as the separate deterministic checker; its clean result checks patterns only and is not an approval.
- Get the owner’s approval of the exact words and intended recipient before sending or publishing in their name. A request to draft, review, or prepare a page is not permission to send or publish it.

### Harness and method accuracy

- Verify the named harness kinds against Harness Standard v0.3; do not create new ones from analogy.
- Verify the five depth stages, their order and delegation gates against the canonical Attention Graduation Framework. Check that all seven slots are accurately explained where the page purports to show the full attention model.
- Check that the ICP example concerns audience listening/monitoring and funnel movement, while the marketing-method example concerns offer, alternatives, and positioning. Do not conflate their scopes.
- Check that multi-harness use is explained as one agent consulting distinct methods when relevant, not as a set of single-purpose agents.
- Check Impeccable design findings against the target site's design tokens; ensure the palette and type remain consistent and the pass has not introduced an incompatible visual language.

### Visual, responsive, and interaction

- Open the actual deployed preview or local rendered page and inspect pixels on desktop and a narrow mobile viewport (at least 390 CSS px or the closest available).
- Inspect hierarchy, legibility, spacing, contrast, focus states, overflow, section order, and the CTA.
- Exercise each interaction by mouse, keyboard, and touch where supported. Confirm controls change the intended content and that the interaction does not introduce unsupported claims.
- Fix problems and inspect the updated rendering; do not rely on DOM state, source code, or a successful deploy message alone.

### Deployment and live check

- Run the site's documented build, schema/content validation, and tests. Confirm generated output contains the intended content and no private source text.
- Check the deployment record/status and open the actual public URL; verify the page content, links, metadata, and responsive rendering. Record the observation time and any expiry or access limit.
- Check that the published page is the approved revision and audience. Remove or correct a wrong or expired deployment only through an authorized path.
- Report exactly what is committed, merged, deployed, visually checked, and still unverified.

## Output contract

Return a concise implementation report with:

- target reader and decision the page supports;
- links to the page, source/preview, and relevant commit or PR, when available;
- brief section map and what evidence supports the offer/UVP;
- sources read and substantive unresolved gaps;
- the method selection record and the compound gap pass findings;
- build, copy, methodology, responsive, interaction, and live-deployment checks actually performed;
- any approvals still needed before sharing or publishing.

Do not call an example a client case study or a pilot result unless it is one and the evidence supports that description.

## Compound step

Record material reader corrections and recurring failure patterns in the relevant harness learning log. Do not silently turn one reader's preference or one page's performance into a universal rule. The deferred agent capability/case-study library is separate work and remains out of scope until requested.

After each run: write a dated learnings record under `knowledge/site/` with the owner's corrections, the root causes, and what the accepted result did well; log owner corrections in `routines/learnings.md` when they happen; and preserve the accepted example in this repo under `examples/` with its real identity: the verbatim page, the research brief, and the correction record. The case is the regression evidence for the method; it is useless as a loose note outside the repo. Keep genuinely private and client-confidential material out (his personal photos, other clients' data, personal contacts, claim links); when in doubt about a specific item, ask rather than stripping the whole case.

## References

- `knowledge/site/pitch-page-learnings-2026-10-31.md`
- `knowledge/site/pitch-page-learnings-first-live-run-2026-10-31.md`
- `skills/pitch-website/examples/2026-10-31-cafe-retiro/` (first live run: verbatim accepted page, research brief, correction record)
- `knowledge/site/contribution-workflow.md`
- `knowledge/site/repo-architecture.md`
- `routines/protocols/PORTFOLIO-WRITE-GUARD-01.md`
- `packs/clear-message/`
- `packs/copywriting-methods/`
- `packs/copy-five-pass/`
- `packs/prospect-research/`
- `packs/strategy-canvas/`
- `packs/audience-listening/`
- `packs/attention-graduation/`
- Harness Standard v0.3 and Attention Graduation Framework in the canonical private Marketing-harness reference path
