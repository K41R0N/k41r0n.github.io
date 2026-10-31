# the author's Ways of Working

Oct 28, 2026 · @the author

A comprehensive log of the repeatable methods, processes, skills and ways of working found across the author's conversations, memory, project workspaces, skill suites, Notion and Drive. Built as source material for a packaged methodology.

## How this compendium was built

This log catalogs 142 repeatable methods found across five source layers, each entry naming where the method lives so it can be lifted into a package. Raw chat transcripts are not replayable, so the memory distilled from past conversations stands in for them, cross-checked against the artifacts those conversations produced.

**Sources mined (all read in full unless noted):**

- Memory: 33 top-level files (areas, topics, people) plus the memories of 9 Claude projects (the client Brain, the client Brain Auditor, the client product Data, New Business Lead Research, IR Lead Research, the client product Strategy Canvas, Brand Harness, Personal Android Tools, the client & Core Team Offsite).
- Skill suites you built: `client-product-harness` (14 skills plus the brain repo they live in), `river-harness` (8 skills, repo-as-plugin), `process-standardization` (8 skills), and 17 custom standalone skills (li-exec suite of 6, the client-thought-piece, the client-brain-testing-mode, the client-data, the client-observatory-api, presentation-i3, project-brief-skill, three-sentence-framework, youtube-research, todo, client-funnel-mapper, edit-this).
- Notion: the the author dashboard and its Q4 Focuses and Weekly Focus databases, Strategy HQ, the Strategy Toolkit and SOPs database, I3 Leads CRM, the the client product 2026 Playbook, Brief Creation and AM Project Management SOPs, client project trackers, the the client portal and content DB, OOO handover pages, the PR campaign report playbook.
- Google Drive: the the client (All) root with its two client brains, the a client brain, the ingest pipeline folder, the brief-making and copywriting protocol folders, the Strategy Canvas docs, the ICP search instrument, the Social Visibility methodology, the tracking pipeline plan, the Top Metrics SOP, the Q3 figure-check sheet, a source document v3, case-study templates, and the the client recon harness charter.

**What counts as a method here:** a procedure with named steps, a rule set, a gate, a template with fixed fields, or a cadence, either stated by you directly or encoded in an artifact you authored, approved, or maintain. Methods are attributed at the level the sources support. Third-party lineage is flagged where it exists: `edit-this` packages Ryan Law's editing method, the anti-slop gates borrow from no-ai-slop and ce-noslop, the Post-Mortem SOP is a collaborator's, the PR wrap playbook is Kim's, `morning` and `skill-creator` are stock Anthropic and are excluded.

**How to read the entries:** each section groups methods by the question you asked (how you work, do strategy, research, edit and corroborate, build agentic skills, develop team processes). Section 10 is the flat index of every method with its home. Section 11 lists what the sweep could not reach and what to consolidate before packaging. Numbers, counts and step names are quoted from the artifacts, not paraphrased.

## Operating principles and working style

Fifteen standing rules recur in every workstream, from a tweet to a quarterly report to a plugin. They are the layer under every method below, and any package should carry them as the shared preamble.

**1. Never invent. Silence is valid.** A missing fact is reported as a gap, not filled. Conventions: `[TBD]` for unknowns in briefs, `[VERIFY]` or `[verify]` on unconfirmed claims in drafts, `[UNVERIFIED: …]` in copy passes, "Not stated" in extractions. "A document with gaps marked as questions is more shippable than a document filled with generic prose." (storytelling-and-ai-discipline.md). "A missing number reported honestly costs a minute. A wrong number reported confidently costs the account."

**2. Every number carries its provenance.** Source, as-of date, window, surface, unit and scale travel with the figure or it does not ship. Never recall a number from memory, even one seen earlier in the session; anything older than 24 hours is re-verified. Never hardcode rates in evergreen copy. Never sum across platforms (GA4 and PostHog are two labelled series). Only you mark a number `confirmed`; skills and scripts stop at `reference`.

**3. Confidence travels with every claim.** The brain tiers are `conversation → operator_reported → reference → confirmed`, each promotion needing the named approver. The same instinct appears as `[Sourced: X]` / `[Inferred]` / `[Gap]` on strategy canvases, `FACT` / `INFERENCE` / `RECOMMENDATION` on SOP steps, `High / Medium / Low / Folklore` on research evidence, `ok / partial / stale / unavailable / manual` on fetched values, and `Strong / Medium / Weak` on audit findings. "Tier governs how a rule is cited, never whether it is obeyed."

**4. Sources first, in a fixed order.** All the client work starts by fetching live canon from the brain (brain-first protocol). Protocol questions resolve Atlas (verbatim section numbers) → on-chain state → executed spells → client-example.invalid and the BA Labs Observatory; the client product the interface is never a protocol source. Comms questions resolve your direct statements → a source document → Strategy Blueprint → brain files → Qdrant. Slack, call notes and the web are "discovery surfaces, not authority." Triangulate before drafting; attempt retrieval before asking.

**5. Compliance before creativity.** The compliance check runs before any creative suggestion. Brands are hermetic: the client product and the client have separate brains, legal chains, audiences and voices and are never conflated. Pass-through framing is a hard fail. Legal triggers route to Aymeric Guillaume; a legal reviewer escalation goes through David Garcia Rios (Playbook §13); legal takedowns go to Raul.

**6. No Brief = No Work.** Every project starts with a one-page, six-question brief that only you and Raul may create. Extra detail lives in a separate methodology document, never in the brief. "Every line in a brief earns its place by changing what someone does."

**7. House writing rules.** No em dashes anywhere, in copy, documents, decks or messages ("an the client product house rule, not a stylistic preference"). Ogilvy-grade copy: short, specific, active, the strongest true claim as the hook. No LLM-isms: mirrored couplets, symmetric triplets, aphoristic fragments, tie-back closings, structural signposting that headers already handle. Plain human phrasing over jargon; buzzword constructions get pushed back. Headlines state the finding; body copy reads like an analyst's note.

**8. Surface, never paper over.** Discrepancies, embargoed content and open decisions are stated explicitly. Checkpoints and explicit open-item lists beat outputs that look complete but are uncertain. "Surface a contradiction; never resolve it silently in either direction."

**9. If it can be counted, script it; measure before and after.** Rules that can be mechanised become FAIL/WARN checks with fixtures and a self-test. Judgment stays with the human and the call is recorded. "Counting beats judgment. Never claim the pass ran without the numbers." Scripts are "an accelerant, never a dependency": every mechanical check also has a hand procedure.

**10. Manual first, then agent.** "Whenever there's a task I know I'm gonna have to do more than once, I plan out the step-by-step of how I would do it manually," then look at where an agent fits. The planning itself follows three steps: map what information is needed, map the second-degree questions needed to reach the objective, work out how the answers add up to a direction. "I literally build 2-3 of these a week." (the author's Notes, Strategy Foundations).

**11. Corrections cascade and stick.** A correction is routed to every concept carrying the old fact, never patched only in the reply in front of you. Corrections are brief and expect immediate course-correction. When correcting, you point at the authoritative source. "Corrections beat cadence." Rules are recorded with the incident that produced them ("every rule here was learned by getting it wrong first").

**12. Approval is never tacit.** One accountable person per workflow; consultation is a gate, not a courtesy; "attribution is not routing." Asking is not authorizing. Nobody edits canon silently; every canon change gets a Decisions Log entry naming who decided.

**13. Delivery discipline.** Files come to chat for review; nothing is pushed to Drive or the brain without direction. Formal deliverables are `.docx` built via Node and verified with pandoc; data fills are in-chat markdown; curricula and reference lists are no-nonsense source lists with one line on why each matters. Communication is direct and terse, with no preamble or meta-commentary. Paragraph-level rewrites come as two or three tonal variants.

**14. Standardize without flattening.** "Prefer best scalable practice, not best individual practice." "Seniority is not evidence." The test is "which version a new hire could run on day 30." Useful role-specific variants are preserved and named as such.

**15. Repeatable, scalable, clean infra over speed.** Priority is "repeatable, scalable, clean infra, schema and architecture so it can be repurposed; not to be constrained by budget, just sensible." Reproducibility is engineered in: record/replay, provenance files, fixed weights ("do not edit weights per run, or results stop being comparable"), `doctor` commands, and refusal to improvise around missing infrastructure.

## Strategy methodology

Strategy work runs on a fixed hierarchy of goals and a fixed sequence of frameworks, with every claim tagged by where it came from. The frameworks are run completely and in order before any synthesis; the deliverable is the framework with direct answers, not polished prose.

### S1. Goals, workflows, projects, campaigns, narratives

All the client work hangs off three strategic goals: Making the client Legible, Third-Party Coverage, Institutional Leads, each with a measurable definition. Below the goals sit workflows (AEO/SEO, Social, PR, Paid Media/KOL, Web, IR, plus Events and Content/Email). Work items are typed: Projects (clear deliverables with a scoped deadline), Campaigns (multi-project activations that must tie back to one of the three goals), Narratives (long-term outcomes). Strategy itself has four core items with different cadences: Positioning (ideally once), ICP (evolving), Messaging (semi-recurrent), Narratives (recurrent). Source: [\[PLAN\] Full strategic tracking pipeline](https://drive.google.com/file/d/1HMsxlWck-MAAgOYJ7kGp2-br3XZnzb4lQphqkvdkbKg/view).

### S2. Foundational strategy workflow

Research, Analytics and Measurement (research; product data and analytics; market data and company research) → ICP development → Positioning → Narrative and Messaging → Brand Voice, then a Product Strategy workflow and an AEO/SEO/Agentic Visibility workflow. Source: [i3 Strategy Foundations & Blueprint](https://app.notion.com/p/3019bfc98f9f8089961aed6b265090fc).

The same sequence is mapped as an agentic dependency chain in your Agentic Flows database: Initial Dossier → Initial research questions → Researching the questions → Positioning initial recommendation → ICP drilldown → Narratives & Messaging → Tone of Voice → Content Strategy → Targeting and Distribution. Each row names what it depends on (for example, ToV needs ICP drilldown, Positioning and Messaging).

### S3. The the client product Strategy Canvas (eight frameworks, strict order)

The canvas is the system of record for positioning work. Rules you set: read all workshop transcripts in full before populating; build all eight sequentially and completely before synthesis; straightforward copy, direct answers, no meta notes or tags; map existing client material onto the frameworks rather than inventing new language; consult the client brain as canonical first; output a Google Doc with the full canvas, then a Slides deck to present. Structure, exact headings:

1. Strategic Snapshot: Who (ICP, one line); Core tension; Positioning bet; Roof message; Three pillars; Spearhead (tightest fit).
2. Lean Canvas: Problem (top 3, ranked), Solution, UVP, Customer Segments, Channels, Unfair Advantage, Revenue Streams, Cost Structure, Key Metrics, Existing Alternatives.
3. Value Proposition Canvas: Value Map (Products & Services, Pain Relievers → named pain, Gain Creators → named gain); Customer Profile (Jobs functional/social/emotional, Pains ranked, Gains ranked); Tightest-fit point.
4. ICP Definition Canvas: Primary and Parallel profiles with Profile, Holdings/size, Geography, Decision-maker, Champion, Influencers/Blockers, Trigger Event, Budget Signal, Buying Process, Qualifiers, Disqualifiers.
5. Empathy Map: Sees, Hears, Thinks & Feels, Says & Does, Pains, Gains, Core tension (the seed).
6. Positioning Worksheet (Dunford): Competitive Alternatives, Unique Attributes, Value, Best-Fit Customers, Market Category; then a one-sentence Coherence chain with "Weakest links."
7. Positioning Statement (Moore): For / Who / The \[product\] / Is a / That / Unlike / Our product.
8. StoryBrand Narrative (Miller): Character, Problem (external/internal/philosophical), Guide, Plan (3 steps), Call to Action (direct/transitional), Success, Failure.
9. Messaging Pyramid: Overarching value message (the roof); Pillars 1–3 each with theme, benefit and proof points; Audience/Persona | Lead message | Channel/Format table.
10. Open Gaps & Strategic To-Do: # | Gap or assumption | Framework | How to close.

Every bullet carries a provenance tag: `[Sourced: jam]`, `[Sourced: PostHog]`, `[Sourced: GSC]`, `[Inferred]`, `[Gap — not in inputs]`, `[operator-reported — VERIFY + compliance]`, `[Illustrative composite — validate in interviews]`. Sources: [the client product canvas](https://drive.google.com/file/d/1b6zHLZrJVwUb7RSOngV3IMJSpob9ZyOjYBYvsFFWNG8/view), the the client product Strategy Canvas Claude project, a client and Skycast canvases.

### S4. Positioning rulings you apply (a client and the client product precedent)

- Kill the category label when the differentiator sits inside the category ("On-Chain Structured Credit" became "institutional ABF infrastructure for the stablecoin economy").
- Unfair advantage is reputation plus network effects, not proprietary tech, which commoditizes.
- A quality is not a pillar if it is a mechanism of another pillar ("Transparent" sits inside Resilient Capital).
- Messaging describes mechanism and process, never outcomes, guarantees or promise-adjacent claims.
- Keep the primary ICP primary; the secondary side stays a hypothesis until interviews (originators pending interviews).
- Remove anything that belongs to another entity from the value map (NFAT is the client's, not a client's).
- A new pillar waits for proof points (Premium Deal Flow pending Deal 1 and Deal 2).
- Prohibited positioning language carried across engagements: "institutional grade," "risk-adjusted yield," "bridge DeFi and TradFi," guarantee language.

### S5. a source document as the top-level strategy artifact

The a source document (v3 current) is supreme over every other guideline. Its shape: Lead Message (positioning, preferable shorthand, when detail is needed) → non-negotiable clarity statements → Key Talking Points → Ecosystem Terminology (Prime Agents, Counterparties, Infrastructure Agents distinction) → Protocol Terminology (Net Protocol Revenue, Protocol Surplus, Protocol Collateral, Protocol Obligations, the client Reserves; banned financial register) → Messaging Guardrails table (Topic | Why we avoid it | What to say instead) → Narratives We Let Others Own (Narrative | Context | Our position) → For Primes and Agents: how to talk about the client. The a client Communications Playbook was modeled on it: lead messaging, causal chain, per-audience talking points, approved and banned terminology, guardrails table, voice summary. Source: [the client a source document v3](https://drive.google.com/file/d/11UwBVWKgztNmLR_ULyg42O5eVo-zlWtQyzWxMJaklUc/view).

### S6. ICP documentation and persona packs

Approach stated for the the client institutional ICP: first gather every relevant file into one workspace, then clean and organize by relevance and by faithfulness to the real ICP. From that workspace build a persona documentation pack (the HoDA: a composite Head of Digital Assets at a European custodian bank) and load it into a Claude project that gives the team feedback on content and ideas as the ICP would. Treat sheet coverage as incomplete data: a missing X handle does not mean no account. Companion instrument: the [the client product ICP Behavioral Search Instrument](https://drive.google.com/file/d/1ic2AlJVH0dulRceSJcDxMJkNkpczNEvB5HcsbqvnsDI/view), detailed under Research.

### S7. Research-for-persuasion methodology

When a client holds a position you need to move, write the methodology before the research. Structure from the Sustained Visibility doc: (1) restate what is being argued, with Prove A/B/C and Disprove/reframe; (2) rank the data hierarchy by persuasive weight for that audience (Tier 1 their own evidence reframed, Tier 2 independently verifiable public counts, Tier 3 institutional marketing science such as Ehrenberg-Bass, 95:5, Binet & Field, Tier 4 competitor tweet-level data, Tier 5 our own analytics); (3) workstreams each with Question, Method, Expected finding, Output, Why compelling; (4) what we concede and the proposal the data should land on ("a barbell, not a binary"), with a 90-day measurement review so the strategy is falsifiable; (5) execution table and a deck order that mirrors the persuasion hierarchy; (6) risks and caveats ("if a result comes back muddy, we drop that exhibit rather than torture it"). Source: [the client Social Visibility Methodology](https://drive.google.com/file/d/19KO3jFAk3chVQgAI8mA9IU5yO2ipueodZr4eCkYJKhM/view).

### S8. Strategy decks and sessions

- Strategy decks are built in the Skycast pitch deck design language and delivered as Google Slides; copy is to the point with no neat terms or analogies.
- The NYC offsite deck carried one thesis ("the client is ready for institutional capital; the client product is the engine that gets you there") with OKRs pulled from the latest report across IR, PR, Social and Web/AEO.
- The Barcelona offsite session format: strategy deck, audience ("John Doe") slides, then a per-channel workshop with on-the-spot pitches and feedback, run as an interactive HTML presentation with timers (30 min talk, 60 workshop, 60 pitches, 60 discussion); teams split per channel; existing proof images kept as-is.
- A VC-audience deck is told from the capital markets perspective in clear, plain language for people who know the terms (\~10 slides).

### S9. Campaign and thought-leadership scaffolding

- New campaign docs mirror the last proven one (Clear Street mirrored the Galaxy campaign doc structure, owner roster and embargoed tier-1 PR approach).
- Case study series: one the client Agent allocation case study per month, a service agent/Galaxy as the model, drafts in the a service agent page-copy slot format (Hero H1 + subheading, Overview columns A/B, Challenge body + three highlight cards, the client Solution A/B, Key Results A/B, word targets per slot), partner-sourced figures bracketed for partner sign-off.
- Thought-leadership manifestos serve two purposes at once (external publication and internal alignment) and do not ship until three gates clear: written sign-off (verbal is not enough), confirmation of which components are publicly speakable, and the embargo scope on anything stealth.
- Podcast strategy (Skycast) runs the full canvas; the audience is the guests themselves; secondary crypto-native audience still gets clips ("can't preach to the choir"); a format concept frames hosts by side of the market so listeners know why to trust and contact each.

### S10. Strategy folder tree (per client, in Drive)

`0. Research and Intelligence` (evidence only, no opinions) → `1. Core Frameworks` ("the system of record for how we win"; nothing downstream may contradict it) → `2. Briefs` (the translation layer; intent, guardrails, objectives, success metrics; no production work) → `3. Campaigns` (campaign design before channel activation) → `4. Agentic & SEO` (visibility intelligence; no content production or keyword lists). Source: [Google Drive Folder Tree](https://app.notion.com/p/30b9bfc98f9f80859437e13d0b99bbf6).

### S11. Personal strategy practice

- Q4 focuses tracked against a collaborator's outline, reviewed every Tuesday, with issues written as one-sentence problem / root cause / solution and carried until closed.
- Quarterly focus areas declared on the the author dashboard (primary: briefs, reviewing work, goal tracking; secondary: AI implementation, new-business networking).
- Domain fluency is built deliberately: a self-study finance curriculum (7+ hours a week, fundamentals-first, accessible material) so strategy conversations with John and Greg hold up.
- Offsite commitments are turned into one-pagers within days (dream-client one-pager drafted from voice-note reflections).

## Research methodology

Research is run as fixed instruments with a stated output shape, a source ladder, and a kill criterion, so two runs are comparable and every finding traces to a surface. Ten distinct research methods were found.

### R1. BD and IR intelligence cards

Two card formats share one rubric: a contact is researched to a fixed template, scored, and given a confidence rating and a gaps list; biographical summaries are not an acceptable substitute.

- **I3 Intelligence Card** (new business): `WHO THEY ARE` → `THEIR COMPANY` → `COMMUNICATIONS PICTURE` (ends with a bolded entry-point verdict, usually "Narrative is the clear entry point") → `NETWORK VALUE` → `SCORES` (Client Potential and Connector Value, each LOW/MEDIUM/HIGH with rationale, "Lead with \<service>") → `CONFIDENCE & SOURCES` (Confidence level, sources, "Gaps to probe directly"). Next Action is phrased as "Probe: (1)… (2)…". Full domain URLs and X handles for every entity mentioned. Lives in the I3 Leads CRM with Sector, Stage, Service Fit (Narrative / Brand Experience / Growth), Status pipeline New → Researched → Outreach Sent → In Conversation → Meeting Booked → Active → Passed, Source, Next Action, Last Contact. Source: [I3 Leads CRM](https://app.notion.com/p/36e9bfc98f9f81ca8b6dd17158211c89).
- **the client Intelligence Card** (IR): identity and career background, organizational positioning, the client fit lane (`YIELD SEEKER` / `AGENT BUILDER` / `NONE`), capital relevance, narrative influence, conversation entry points, confidence level, sources, research gaps. Capital targets are distinguished from counterparties and narrative peers (Kinexys's Oli Harris is NONE lane with HIGH narrative influence).
- **Working rules:** disambiguate an inbound request via the Slack thread before investing in research (the "Oliver Whyman" case revealed a different opportunity than the surface ask); a minimal record (name, company, email) is an implicit request for the full method; multi-source web research is standard; CRM overlap is a sensitive signal (a prospect competing with an existing contact gets careful handling); competitor maps reflect current positioning, not legacy; when research already exists, build on it without re-explaining; corrections come format first, then substance, and outputs are updated fully.
- **OSINT screening at scale:** a \~90-contact Google Sheet (VCs, asset managers, market makers, media) screened one row per person, anyone with a documented the client/a competitor tie discarded into a separate tab, output as a spreadsheet rather than cards.

### R2. Source ladders and the under-informed gate

For any the client factual question the ladder is Atlas (verbatim section numbers) → on-chain contract state → executed executive spells → client-example.invalid and the BA Labs Observatory. For blog and copy research the protocol splits a verification half (the brain) from a motivation half (Slack `#the client-money-news-narratives` and `#the client-money-iods`, Google Meet notes in Drive, independent web), with a nine-rung source ladder and a maximum confidence per rung; rungs 5–8 are "discovery surfaces, not authority." A finding is claim + surface + tier + consequence. Five triggers make the piece under-informed and stop drafting: no stake, no timing, big idea resting on a tier 5–8 fact, a load-bearing number with no feed, fewer than two independent surfaces. Output is a fact sheet with mandatory Gaps and Proposals raised. Source: `client-product-harness:blog` references/research.md.

### R3. Story tracing (why did a number move)

Evidence chain, strongest first: on-chain transaction → spell source (action blocks with forum/Atlas/poll links) → executive document (hash-checked) → the client.data governance and settlement records → forum post (read raw, never paraphrase a post you have not read) → Atlas section by document number. Procedure: locate the step; classify the mechanism before searching (rate → BEAM; the client Capital moved → Genesis transfer; cash stepped → settlement; the client supply dropped → burn; collateral → agent flows); match on date and an amount within 2% (date-only is a lead, not a match); read and cite; write. "Never state a cause without an artifact." Agents are independent; Slack is at most `operator_reported`. Source: `the client-data` references/story-tracing.md.

### R4. ICP Behavioral Search Instrument

Every keyword seed and every GSC lens is tied to a behavioral hypothesis drawn from wallet data (what they did) and the strategy jam (why); search data "confirms, sizes, or kills it." Pieces: four ICP characteristics (Sovereign; Values clarity; Financially mature; Accountable) with a characteristic-to-cluster map; a behavioral foundation table I1–I11 (Insight | Source | Confidence | Search implication); SEMrush seed clusters A–H each with hypothesis, seeds, ICP-fit signal, kill criterion and compliance notes, plus run rules (US database spine with APAC spot checks, questions on, intent filter, a pass-1 ICP-fit filter); GSC Reads 1–7 (question and modifier mining; competitor and comparison; impressions-without-clicks gap; branded vs non-branded; geo split; risk and safety language audit; page-level intent capture); a routing rule (capture demand exists / thin but present / no demand → "route it to social listening and blog, not to a keyword target"); a synthesis loop; discipline notes (seeds are not copy; US volumes undercount; value per wallet over volume). Source: [ICP Behavioral Search Instrument](https://drive.google.com/file/d/1ic2AlJVH0dulRceSJcDxMJkNkpczNEvB5HcsbqvnsDI/view).

### R5. AEO prompt-universe loop

Build or refresh the prompt universe monthly → score coverage (cited / mentioned / absent, competitors present) → find gaps (P0 and absent) → propose content against gaps → keyword research on the chosen idea ("keyword research happens after the idea is chosen, not before") → build to the surface template, ship, re-score. Columns: Prompt, Bucket, Priority P0/P1/P2, Funnel stage, Coverage, Competitors present, Target URL. The brain holds the methodology only, never the live list. The Top Metrics SOP version: Claude generates 500+ prompts → Momo Oslo runs them → PDFs → Claude Code analysis with a fixed prompt; metrics are Brand Mention Rate, True Share of Voice, Sentiment, Average Rank, Website Citations. Sources: `client-product-harness:aeo-seo` references/04-prompt-universe.md; [Top Metrics SOP](https://drive.google.com/file/d/1L9gOitF6ABhXiOkAt4Jb8qtj7rxPXfV88KI3h-V2ROw/view).

### R6. YouTube research (ranked video research)

Rank by who is talking and how viewers responded relative to channel size, never raw views. Four modes (`topic`, `learn`, `expert`, `brand`) with fixed weights per mode over six components: Relevance, Authority, Engagement, Views, Time decay, Format fit, `score = 100 × Σ w·component`. Authority blends log subscribers, audience health (median recent views ÷ subs), topical focus, long-form ratio and verification, halves on shill patterns, and is floored or capped by curated trusted (tier A 0.92, tier B 0.78) and blocked (0.08) lists you maintain. Engagement is normalized against tier medians (nano 5.23% down to mega 1.41%). Diversity cap of 3 videos per channel. Decisions you made: yt-dlp only, no API key; algorithmic score plus curated lists; weights never edited per run so results stay comparable; must run on both Claude Code and Claude web (org admin asked to whitelist domains). Deliverable rules: every claim cites a video link with `(mm:ss)` transcript quotes; numbers first, interpretation second, visibly separated; coverage and trust stated; "comment sentiment is read, not counted"; `learn` mode ends with "Start here (3 videos)", a learning path and open questions; `brand` mode reports share of voice, owned vs earned, narratives, risk flags. Source: `youtube-research` skill.

### R7. Social listening and reconnaissance

- **Listening platform spec (approved 2026-09-25):** successor to the Apps Script X-listening sheets. Requirements: stored views, a database so tweets are not re-scraped, a Jev enrichment layer on ingest for labelling and spam removal (no LLM labelling anywhere), labels and filters managed in the front end through saved boolean queries as in Meltwater, hybrid scheduled plus on-demand collection, local PostgreSQL first, seeded from existing sheet extracts and reconciled by date and tweet ID to prove coverage. Scope order: X first, then publications (RSS, \~30 named outlets), PR (Google News Apps Script proxy plus Kim's list), Reddit, Medium, YouTube. Metric conventions: reach = sum of views from the X API; baseline from the front-end date range; amplifier identity (RT/quote) in scope. Priority features: saved searches and dashboards per launch or GTM. Source: the client Brain project memory and `claude/Social Listening Platform - Architecture and Specifications v1.0 2026-09-25.md`.
- **Recon harness charter pattern:** a `CHARTER` (Mission, In scope, Out of scope, Kill criteria, Success), an `INDEX` routing table ("If you need to know… | Open"), and a `What to listen for` concept with a listening map (per surface: Where / Signal / Ignore / Rule) and a 12-type daily pass checklist (rating actions, regulatory text, list-member names, collateral acceptance, reserve changes, bank and asset-manager stablecoin moves, role changes, upcoming appearances, headlines naming sample-token/the client, diligence questions in replies, peer launches with a named institution, vocabulary drift). "Record each hit with date, source URL, who, what was said, and engagement at read time. Report changes, not volume." Source: Drive folder `15_zwVBRQPFESpe_8C2VBUTnsOZ9qnL52`.
- **Warm-introduction social graph:** twitterAPI.io + n8n + Postgres to find mutual connections between leads and the the client product network (a stakeholder, Jay, a collaborator, brand account); outputs route through mutuals rather than enabling cold outreach, for GDPR/UWG compliance.

### R8. Knowledge-base auditing (the client Brain Auditor)

Suggest edits only when content is demonstrably wrong, stale or inaccurate, never for style or scope; every change traces to a verifiable source. Findings are weighted Strong (directly contradicted by a confirmed-tier source), Medium (plausible conflict needing an operator decision), Weak (unverifiable this pass). Each finding records current text, conflict source, suggested edit, implementation recommendation. Confirmed-tier operator-authored files win conflicts. Distinguish what is operator-decidable from what needs external verification. The audit is multi-session and cumulative; logs capture resolved and deferred items and name the highest-leverage fix (a 43KB file with deprecated terminology). Files are kept tight (1–2KB). Source: the client Brain Auditor project memory; log at `the-client/_ingest/pending/logs/`.

### R9. Docs and corpus audits

The GitBook docs audit runs an 18-item per-page checklist explicitly ("'Looks fine' is not an audit result"), with a scope table mapping each page to corpus line ranges so the 529KB corpus is never loaded whole, the audit report written before any edit ("a visible n/a is checkable; a silent omission is indistinguishable from having skipped the check"), and every finding sorted into Category A–G before optimization. Canon outranks both the shipped docs and the corpus they were built from. Details under Editing. Source: `client-product-harness:docs-corpus`.

### R10. Research deliverable conventions

- For learning or reference asks: a no-nonsense list of sources with links and one line on why each matters.
- For API reverse-engineering: endpoints extracted from compiled JS bundles (\~60 Observatory, \~280 client-example.invalid) into developer-facing specs; the `star` field never appears, always "Prime Agent."
- For PostHog schema work: full event taxonomy by namespace (`app_`, `marketing_`, `chat_`), batch export configuration, ETL options and ready-to-run queries delivered as an integration guide.
- Research into partner counterparties precedes any partnership press release (Galaxy).

## Editing, corroboration and compliance

Copy moves through a fixed sequence of passes, then a mechanical gate, then a verdict with a named channel and a named approver; none of the three substitutes for another. "The gates are not the review: editorial polish does not clear compliance. Both run."

### E1. The 5-Pass Copywriting Method (canonical, non-negotiable)

Applies to social, blog, PR, IR newsletters, AEO content and website copy; executed, never labelled. Step 0 orientation: read positioning, both voice files, legal guidelines (plus competitive landscape, financial terminology, entity naming, institutional messaging per brand) and the source hierarchy. **Pass 1 Big Idea (Ogilvy):** one sentence, 15 words or fewer, tested simple / compelling / unique / enduring; "if you have two big ideas, you have zero"; written as `BIG IDEA:` at the top of the draft. **Pass 2 Factual Anchoring:** every claim traced through a claim-type-to-source table and cited inline; `[UNVERIFIED]` items resolved before Pass 3; never invent, never stale, quotes verbatim only; "sourcing a claim does not make a banned claim usable." **Pass 3 Voice Matching:** read aloud; register "DeFi assumed, the client explained"; reject both the institutional and the degen voice. **Pass 4 Storytelling Structure:** Hook / Context / Conflict / Resolution / CTA; explain why numbers moved or tag who knows; "if every paragraph is the same length and shape, rewrite." **Pass 5 Compliance Gate:** banned terms, the six a legal reviewer legal-review triggers, exposure and layer check, substantiation, the review standard ("would a reviewer stand behind every sentence" on accuracy, integrity, clarity, restraint), quoted statements verbatim only, number re-verification with timestamp, agent independence, then a submission package (draft, big-idea note, unresolved items, format notes). **Step 6 Format Adaptation** per channel. Sources: brain `routines/protocols/copywriting-guidelines/` ([README](https://drive.google.com/file/d/1cGMQvpNAfo4bUdbQciVIAbPzoxnQNVsz/view)); `client-product-harness:copy-review`; `river-harness:copy-review`.

### E2. Brief-making passes

Step 0 Scope and Sources (confirm brand; one brief = one initiative; context gathered in priority order a source document → Strategy Blueprint → brain entities → brain concepts → financial dashboard → Notion calendar → Slack as `operator_reported` → your direct statements) → Pass 1 Draft the Six → Pass 2 Numbers ("never invent, never stale, verify at the moment of writing") → Pass 3 Framing Check → Pass 4 Cut to One Page → Pass 5 Compliance Gate (banned-terms grep, "yield is reported, never recommended," approval chain). Source: [brief-making README](https://drive.google.com/file/d/1zHhiZfRsZsRB9W7E-dAw9A6iVOFJpEvu/view).

### E3. The craft layer and the anti-LLM standard

The organizing thesis: "AI tells are architectural, not lexical." Lexical bans are round one; the method targets sentence shape, paragraph endings, opening macros, ring composition, negation-correction, catechism, anaphora, triads, meta signposts, duplicate moves across a corpus, seed-echo, and regrowth after rewrites. Your own words, which set the standard: "It's not about the wording. Think in terms of the sentence structure, the way you develop paragraphs, the types of literary figures you use." "Inject human expressions and sentence structures, lead ups, and segues… think structurally instead of randomly peppering them in." "Reads extremely LLM written" means restructure, not re-word.

- **Brief contract (craft §1):** one reader by job title, awareness stage, one core emotion (clarity / control / confidence; a client uses relief / control / defensibility), one action, one big idea; pre-draft big-idea gate (disputable, stage-moving, swap test); post-draft gate (generative, proof-gated, durable).
- **Nineteen drafting rules (craft §3):** claim budget; the second mention is the proof; so-what chain to "a Tuesday"; the Rolls-Royce move; cost of inaction made concrete; procedural scenes; one contrast at consequence; first-sentence contract; seeds of curiosity; headers are assertions; agent-verb floor; elegant-variation ban; endings never recap; 8–10% fact-conserving compression; say-it-to-one-person; five or more headline candidates; length set by fact supply; the cold read; repeat what works verbatim (cleared formulations repeat; openers, closings and anchors never do).
- **Numeric budgets:** at least one sentence under 8 words and one over 25; no three consecutive sentences within ±3 words; paragraph mass 1–8 sentences; paragraph-final aphorisms 2–3 per piece; negation-correction at most 1; triads about 1 per 250 words; meta signposts 0; ring composition at most a third of a set; corpus collisions 0; word count flat or down through a fix round ("a fix round that grows the word count is presumptively regrowing tells").
- **Seeds win.** Your seed paragraphs are load-bearing: thesis and one or two phrases survive, developed never quote-dumped, image never relocated; a reviewer never overrides a seed. When you hand over an edited draft, your prose is the spine and the beats are placed around it.
- **Voice precedence** for ghostwriting: legal and client red lines → the author's own voice and seed material → the anti-slop standard and gate script → the client product house voice ("editorial conscience, not the voice") → platform optimisation. Calibration passages are quoted verbatim, never paraphrased into a persona.
- **Corpus registries** of spent lines and owned anchors are appended at every delivery so pieces in a set never collide ("Boring. Layered. Defensible." is yours; cloning it is "detectable imitation").
- **Connective tissue:** a catalog of 16–20 transition moves (backward-glance pickup, concession turn, fair-objection set piece, zoom, time-jump, deflation, blunt scene cut, confession pivot, hedge-then-commit, question hinge…) with placement rules (hinge paragraphs at most \~2 per 1,000 words; litmus: delete the connective, if nothing changes it was filler). Canon named: Williams, McPhee, Zinsser, Pinker, Strunk & White, Orwell; Levine, Lewis, Buffett, Housel, Economist leaders.

Sources: `the client-thought-piece` (references/craft is inside SKILL.md plus voice-profile, tell-registry, transition-catalog, structural-audit, review-protocol, corpus-registry); `li-exec-*` references 05, 07, 08, 09; `client-product-harness:blog` references/craft.md; `river-harness:copy-review` references/craft.md.

### E4. The review architecture (blind stages, scaled to stakes)

1. Mechanical sweep (gates or grep).
2. Self line-edit and registry sweep.
3. Independent adversarial review by a fresh reviewer with named lenses (forensic structural read, the seven tests, buyer's read, editor's read, voice fidelity, fact/risk/compliance); at most 12 ranked findings with quotes and rewrites; verdict question: "would a skeptical editor who reads LLM output daily clock this, and from what, precisely?"
4. Adjudication: seeds win; verify the reviewer; fix the class not the instance; keep the best instance of a flagged device; beware regression to the mean; document judgment calls.
5. Verification pass by a second fresh reviewer with explicit checkable claims, hunting new tells the rewrite introduced (max 5).
6. Measured subtraction pass, always last, with before/after counts (final-sentence word counts per paragraph, punch paragraphs, negation-correction hits, meta signposts, ring check, corpus grep, word count).
7. Knock-on read for edit artifacts.
8. Delivery note, then executive or client approval, then legal.

Scale: a comment runs steps 1, 2, 6; a standard post 1–4, 6, 7; an article, first post, correction or red-line piece runs all eight. Iterate "as many times as necessary." Verified result on the John op-ed V3: shaped endings 22/35 → 14/31, meta 10 → 0, punch 4 → 1, negation hits 40 → 2, ring broken, words 2,492 → 2,297. Sources: `the client-thought-piece` review-protocol and structural-audit; `li-exec-review`.

### E5. Deterministic gates

- **`run.py` (client-product-harness copy gates):** 26 checks, each with a spec file stating PASS condition, invocation and false-positive notes; checks 01–09 general, 10–18 added "because shipped copy breached them," 19–23 structural draft-only, 24 entity naming, 25–26 the a legal reviewer layer; context `--context=external` is the stricter default; every FAIL fixed, every WARN resolved by hand except the check-26 regulatory-characterization WARN, which no desk may clear. Runs on all shipping copy including metadata, Key Takeaways, alt text and social. Eval fixtures (`expected-pass/`, `expected-fail/checks/`, `expected-fail/gates/`) with a recorded baseline in `harness/evals/expectations.md`; "a check that fires on canon-required language is a broken check."
- **`li_gates.py` (executive LinkedIn):** 31 gates G01–G31 (em dashes; hashtags; AI connectives; filler; AI vocabulary with a soft-exempt regex for "net leverage"; cliché openers; reveal bridges; negation-correction budget; engagement bait; emoji bullets; hook rules; length per form; external links; broetry; rhythm; significance narration; copula avoidance and false depth; meta signposts; scaffolding; restatement; kicker budget; triads; humblebrag; big-idea frontmatter; placeholders; spent lines from the registry; carousel rules; faux insight; passive and portability; density of 3+ tells in one paragraph; client lexicon). Emits a METRICS line before and after. Escape hatches are explicit and logged: `allow:` frontmatter, `waive: G07@L12 reason`, `--lexicon` with ban/allow lines. `selftest.py` runs an expectation table over 18 fixtures including held-out ones "written by an independent reviewer"; a fixture is added whenever a real draft exposes a false positive or a missed tell.
- **`lint.py` (the client-data):** 26 regexes for register bans and traps (profit, AUM, deposits, bank, tokenized fund, earnings call, Prysm, star, Solvency Reserve, MSC, API field names in copy, hardcoded sample-rate %, em dash, Maker proactively, Synome, "not just… but", hashtags, the client Vaults without Morpho attribution…).
- **`deck.py` / `fit.py` (presentation-i3):** refuse unknown layouts or fields, missing images, ragged tables, charts with fewer than two real values; measure Inter advance widths to flag copy that wraps and collides.
- **Shared doctrine:** FAIL is unambiguous (fix or waive explicitly); WARN needs a human and the call is recorded; "a clean runner exit means the mechanical half passed, it never means the post is ready"; "don't grade English with regexes; don't leave mechanical invariants to vibes"; a load-bearing phrase and its lint lock change in the same commit.

### E6. Brand check: the verdict engine

Two complementary passes, mechanical plus manual, over documented coverage gaps. Procedure: put the material in a checkable file → classify context (untyped defaults to external, the stricter) → classify jurisdiction (US / EU / APAC; "global is three markets, checked against the strictest") and channel (short-form social; landing/longform; product UI and APY; partner pack; BD/private; technical/legal/risk) → run the mechanical pass → map every FAIL/WARN to a gate with citation → manual pass (the verb test: "who is the sentence's subject acting for?"; the layer test: is Layer 2 reachable and nameable; substantiation via live data; naming via the rendered artifact; narrative traps) → check the six a legal reviewer triggers independently → check the eight objections before failing a bold-but-true claim → assemble the verdict, never rewrite. Output: `Verdict: PASS | FIX | BLOCK` with jurisdiction, channel, per-gate line with citation, Layer 2 location, substantiation, coverage note, legal-review trigger, WARNs resolved, and "channel-limited, not prohibited" relocations. a client's version adds the evidence gate: a fix or block carries the exact offending span verbatim ("no quotable span → no fix/block verdict"), the governing rule must be locatable in canon this run, "severity and confidence are orthogonal," "fewer than 3 findings on a clean text: say it's clean." Sources: `client-product-harness:brand-check`; `river-harness:brand-check` with gate-checklist and the voice-reviewer / compliance-reviewer personas.

### E7. The five gates and the legal layer

Five absolute gates on every external line: terminology, exposure, number, naming, narrative (a client's instance: named-counterparty, no-promise, number, floor, framing). The legal layer is a four-file a legal reviewer set, cross-linked so reaching one reaches all and lint-enforced from every product entity: which words (allowed / allowed-with-cushion / channel-limited / a 19-item Do-not-use list), on which surface and what must be nearby (Layer 1 hook / 1A substantiated hook / Layer 2 architecture that must exist in the user journey / Layer 3 diligence; per-channel rules; approved copy blocks; residual-risk register), why (case law, baseline facts, the eight answered objections, twelve drafting principles), and brand-specific prohibitions. Review is event-triggered, never calendar; a new phrase is never quietly added to an allowed or banned list; a proposal states whether a change "came from a legal reviewer or from a reading of a legal reviewer." The posture: "substantiation and causal discipline, not avoidance; if the claim is true, use it." "'Aggregate' is load-bearing" in any sample-rate funding sentence. Six legal-review triggers escalate Aymeric → a legal reviewer; forward-looking statements on press releases, quote rewrites that remove banned phrases, and regulatory-status prompts ("Is sample-yield-token regulated?") are always legal items, never drafted.

### E8. Corroborating numbers

- **Live-data two-step:** attempt the API (`fetch_sky_api.py` or `the client.py`), apply the parsing traps (17 traps in three tiers: rates are fractions, decimal strings not floats, `0E-18`, change fields are not deltas, `star` never reaches output, values already denominated, five response envelopes, two pagination conventions, intraday drift, restatement, same-name different-thing), reconcile on the human-facing surface, report value + as-of + endpoint/field + scale + `reference`. On failure, the literal line "I cannot fetch live data from the API. Please check https://the client product or https://info.the client product for the current value," with no retry, web search, scrape, cache or estimate. "A number appearing in output with neither an as-of timestamp nor an explicit fetch-failure deferral is a process violation."
- **Validation ladder (the client-data):** L1 internal identities ($0.01 on statements) → L2 two independent routes agree (tolerances per metric) → L3 on-chain contract state → L4 published register (TIES / RESTATED ≤2% disclose / DRIFT >2% FAIL) → L5 dashboard match via Playwright at the moment of writing. Internal use needs L1+L2; external use adds L5, cites the dashboard not the API, and discloses L4. `summary.ready_for_external_use` only with no FAIL and all L5 passed. What the levels cannot catch is named: a wrong definition applied consistently, restatement after checking, a cause.
- **Report figure-check:** every discrepancy in a quarterly report classified by type with a default owner: Correction (Corey), Rounding (Corey), Ruling needed ("numbers tie; label or method needs a decision" → you), Not in BA data (needs a partner source or is cut → Greg). Checklist columns: # | Done | Type | Section | Figure | Report says | BA says | BA note | What to do | Owner | Status | Resolution. Q3 result: 88 of 123 figures tied with no action. Source: [BA Figure Check Checklist](https://docs.google.com/spreadsheets/d/1ogzeUR54bjnuK-GExP4ltHBW11Guaz-thAnhP4NwL_A/edit).
- **When sources disagree** (sheet, skill, dashboard): report all three values and which one you used; update the known-issues file or the mapping, never the number.

### E9. Feedback triage and iteration

Operator feedback is triaged by type: A framing → restructure; B compliance → sweep the whole draft; C length → cut, do not rewrite; D factual → re-fetch the entity and propose to canon. "Feels robotic" means Pass 4; "reads clumsily" on a lede means offer two or three tonal variants. Change logs and audits carry confidence tags (confirmed / reference / operator\_reported). When you correct, you point at the authoritative source and expect retrieval before questions.

### E10. Storytelling and AI discipline (the pre-gate standard)

The standard in one sentence is the read-aloud test (a reviewer or Vance reading it to a billion-dollar allocator). Filler vs story table; "the rule when you don't know why" (do not write a sentence about why it moved; leave a comment and tag the person who knows); three classes of tells (phrase, structural, hallucination, with the real "the client Poke / the client R / SkySky" example); the use-what-already-exists rule; a 7-item self-review checklist; what to do when a deadline pressures you to fill ("the deadline is wrong, not the document"). Source: [storytelling-and-ai-discipline.md](https://drive.google.com/file/d/1tIAVy4GhZdGTlgZy2QF66Lmuvxs_CQ60/view).

### E11. Third-party editing method you packaged (edit-this)

Ryan Law's hierarchy of editing needs: Strategic (does it solve the intended problem?) → Structural 30% edit (promise delivered, scoped, weighted; MECE, Chekhov's Gun, zoom in, writer's draft vs reader's draft, parallelism, high-concept headers, how-vs-why 80/20) → Line 90% edit (BLUF, weasel-word sweep via five whys, steelman objections, dense words, sentence variation last). Four context questions first (strategy, outcome, audience, scope); read the whole piece before editing; feedback as inline comments with examples and 1–3 overview themes; an 8-step title sprint ending in 20+ raw titles, a shortlist of 5, one recommendation. Not carrying your house rules (uses dashes, no gate script); useful as a stage-diagnosis layer in front of the 5-pass method.

### E12. Docs-corpus audit and PR discipline

The 18-item per-page checklist (duplicate-content scan; FAQ-depth parity; answer-first "X is Y" test; exposure guardrail; ownership relationship; complementary-page cross-check; legal-language grep every section; external verification; orphan pages; proofread; content-removal workflow; ownership and legal framing sweep; section-wide sweep once a fix pattern is confirmed; full corpus footprint, run first; verify a causal claim before propagating it; a universal claim requires enumerating its exceptions, run the inverse grep; cross-section structural completeness; link integrity). Optimize posture: "add and link, don't replace"; "fix only what's broken"; findings in Categories A–G ranked A, B, C/D/E, G. Submit: branch `docs-audit/<section>`, approver reviews the diff before commit, full-diff re-review against the 18 items immediately before commit, one commit per section, PR body in five sections (What this is / What changed per page / Please specifically check / Open, not resolved here / Fastest way to review this). Source: `client-product-harness:docs-corpus`.

## Building agentic skills and harnesses

You build agentic systems in a fixed order: define the manual process, encode the knowledge as a typed brain, spec the skill against a routine, build it with deterministic checks and fixtures, then let a governed correction loop improve it. The pattern has been instantiated at least three times (the-client and the client-money brains in Drive, the a client harness as a repo-as-plugin, the client-product harness as a repo-as-plugin) with only canon, gates, approvers and templates swapped.

&#91;embedded content: brand harness · governance loop around canon\]

Raw material becomes one proposal per fact, a named approver rules on each, and only that ruling edits canon; output skills read canon fresh every run, pass the gates, and hand any new fact they surface back into the loop. Testing mode and the monthly retro are how the loop learns.

### H1. Doctrine: manual first, then the six primitives

Start from the manual step-by-step (principle 10). The the client product 2026 Playbook names six AI primitives to compose from: Prompt, Skill, Memory, Project, Connector, Agent/Workflow, under the rule "you can't automate what you haven't defined"; every service line maps its most important capabilities as SOPs first. SkyBrain was the first instance. Source: [the client product 2026 Playbook](https://app.notion.com/p/3879bfc98f9f808f85e4f673c50d860e).

### H2. The brain (OKF knowledge bundle)

One repo or Drive folder is the brand's operating knowledge base. Four navigability rules: the file path is the identity; frontmatter is the routing surface (`type`, `confidence`, `source`, `approver`, `timestamp`, `review_by`, `supersedes`); links are the graph; routing is compiled, not maintained (a linter regenerates `MANIFEST.md`). Domains: `people/`, `knowledge/{concepts,entities}/` (or `memory/strategy/`), `decisions/` (reverse-chronological log, format `## <date> — <title>` / Decided by / Context / Decision), `assets/{copy,data,design,tools}/`, `routines/` (process authority), `ingestion/` (intake queue and TestLogs), `harness/` (specs, gates, evals; never shipped to a client), `agent/` (SOUL, MEMORY capped at 150 lines with no canon, STARTUP, TEAM), `skills/`. A hub `index.md` holds the routing table keyed on `type`, the source-of-truth hierarchy, the gate summary and the approval chain; `CLAUDE.md` is the operating contract and carries zero canon ("if this file and a concept disagree, the concept wins"). Startup every session: index → MANIFEST → route by question type → open only the pointed concepts → enforce the confidence floor and gates. Progressive disclosure: every folder has an index; agents route, open one concept, follow links, never crawl. Hermeticity: the harness reads nothing outside its own tree at runtime except declared `DataFeed`s; Step 0 in every skill resolves the bundle (current repo → plugin bundle → MCP) and stops if unreachable, never hunting the filesystem. Two brands never share an artifact ("Two Brains, Two Brands"). Entity rule: one file per real thing; names, domains and shells are fields, never entities. Seed-a-concept loop: name by identity (tree at most two levels) → frontmatter first → structural body → place or promote → route → lint. Sources: a client `HOW-TO-USE-THIS-BRAIN.md`, `index.md`, `FUTURE-DEPLOYMENTS.md`; client-product-harness `index.md`, `CLAUDE.md`; the client (All) `HOW-TO-USE-THIS-BRAIN.md`.

### H3. Governance core: ingest → review → testing mode → retro

- **Ingest:** preserve the original in `ingestion/pending/{calls,slack,manual}/` named `<date>-<slug>`; extract one fact per item ("batched edits hide provenance"); match concepts via MANIFEST without opening bodies; assign the arrival tier by who asserts it and whether they are the concept's named approver confirming first-hand; route via the intake table (confirmed decision → `decisions/`; positioning shift → concept; new product → entity; new person → roster and RACI; non-approver fact → `pending/proposed/` as `operator_reported`; live source → a `DataFeed` contract, never numbers); deduplicate (identical → discard; newer → `supersedes`; contradicts → flag, never resolve). "Handoff, not adjudication." Pipeline in Drive: Circleback transcripts → webhook → n8n → `_ingest/pending/calls/`; Slack daily digest → `pending/slack/`.
- **Review proposals (the weekly 10-minute ritual):** list the live queue oldest first; identity first ("never assume the operator is the approver; ask once at the start"); walk one proposal at a time; four rulings: Approve (apply the exact edit, promote, walk the link graph and show the cascade before writing), Approve with edits (approver's words, not paraphrase), Reject (reason verbatim; feeds the retro), Defer (with the unblocker; deferred twice → flag in retro); one decision file per approval plus a log line; lint to green. "The approver approves content, not a count." "An empty queue is reported, not padded."
- **Testing mode (the live correction channel):** command lexicon `TESTING MODE` / `FLAG:` / `PAUSE TESTING` / `RESUME TESTING` / `CHECKPOINT` / `END TESTING`, plus organic corrections ("that's wrong," "the brain says X but actually Y"). Per correction: clarify to a precise checkable statement; establish who states it (domain approver → `confirmed` direct edit; anyone else, Raul included, → one `operator_reported` proposal per concept, "never silently elevate hearsay"); route the full cascade in three passes (routing table by type, link graph of every citing file, prior decisions marked superseded) and show the cascade list before writing; draft the exact edit per file; write through the governed path; log one Decision; lint. One learning per run. "Honesty over polish": production behaviour while observed, self-softening logged as a finding. Output is a `TestLog` with a gap report mapping every unfixable gap to its fix location (routing rule in index; under-specified guideline; a skill's required reads; a new capability spec; the a legal reviewer set as a unit; a stale upstream source; CLAUDE.md). The the client Brain Auditor version tracks eight categories (retrievals, rule adherence, edit scope, citation completeness, confidence-tag handling, operator interactions, output format, reliability) in a nine-section log ending with a one-sentence verdict "Reliable for X, unreliable for Y" and a net adoption rate.
- **Retro (monthly compounding):** window from the last retro; collect TestLog gap reports, decisions, rejected and stale proposals, organic corrections, eval drift; cluster by failure mode not by file; rank by recurrence × cost; "anything that happened twice gets a fix; anything that blocked output gets a fix first"; present clusters before fixing; harness fixes applied directly, canon fixes as proposals; "never weaken a gate as a fix"; re-run the gate runner against every file in the eval baseline and diff check by check; an empty window still gets a decision file ("silence is data"). Every real failure that reached output becomes a new eval fixture ("the suite is the harness's immune memory"). The four stages named: Catch → Adjudicate → Consume → Guard.

### H4. Confidence model and approvals

Tiers `conversation → operator_reported → reference → confirmed` with an explicit external-use column; tags are "deterministic by source, never a judgment call"; `confidence_floor: confirmed` for anything external; fetched numbers are `reference` forever. RACI rules: every workflow has exactly one Accountable; Consulted is a gate, not a courtesy; a person named must exist in the roster; a new workflow means a new RACI row; per-concept `approver:` is attribution, routing lives only in index ("attribution is not routing"). Retired chains are named so they cannot be reinstated. You are the designated approver for both the client brains; Aymeric is the content, legal and canon seat for the client product; a stakeholder and a stakeholder split a client canon by domain.

### H5. Skill anatomy and the skill standard

Every custom skill: a `SKILL.md` that is a router and procedure (frontmatter `name` and a "triage sentence" description with trigger phrases and non-triggers; Trigger → Required reads with Step 0 resolve-the-bundle → Guideline enforcement → numbered Procedure with letter-suffixed inserts like `2b` → Output contract → Quality gates → a references index table `| Reference | Load at | Purpose |`), kept to roughly 25–50 lines of procedure; `references/` for the standard itself (loaded at the phase that needs them, never inlined up front); `scripts/` for anything checkable (stdlib-only Python, no shell-out, FAIL/WARN model, a `doctor` or `selftest` command); `templates/` for every artifact the skill writes; `samples/` or `fixtures/` declared spent. Big methods are decomposed into numbered reference documents (li-exec 01–12) and partitioned per skill by copying identical files so each skill is self-contained. SKILL.md bodies carry a preference log or provenance footer explaining why rules exist. Each built skill has a paired `harness/skill-specs/<name>.md` (status `spec → build-ready → built`) from a template with Trigger, Required reads, Gates, Procedure pointing at a Routine, Output contract, Sources needed before build, Open questions. "The routine is the process; the skill is the executor; change the process → edit the routine, change the automation → edit the spec." Your stated packaging requirement: skills ship with samples, scripts and methodology files, not markdown only.

### H6. Capability-authoring protocol (adding a skill)

Step 0: capability or external process? Litmus: "does the harness need to do it, or just know about it?" (know → a `Tool` / `Config` / `DataFeed` concept, never a skill; "any words that ship externally pass through a skill first"). 1 Spec it, routine first (required reads freeze routing; gates inherited, never opted out). 2 Approve (status build-ready; log line). 3 Build to the skill standard. 4 Register (status built; routing row; lint). 5 Compound (testing mode after first runs). Rules: spec before build; the brain is the only source of truth; new knowledge exits through ingestion; "don't build past an open question." A capability gap felt twice gets specced. Source: a client `harness/skill-standard.md`, capability-authoring routine.

### H7. Deterministic enforcement and evals

Two linters run in CI: `okf-lint.py` (frontmatter conformance, YAML plain-scalar hazards, broken links, orphan types, overdue `review_by`, Person status, the legal-routing check that any file with three or more sample-yield-token/sample-token/sample-rate mentions must link the a legal reviewer set, MANIFEST regeneration) and `harness-lint.py` (self-containment, reference integrity, brain-resolution line present and ordered, the NO-HUNT positive lock and CLONE-HUNTING negative lock, write discipline "never the plugin cache", locked phrases per skill, terminal-line drift against `harness/automation.md`, no permission-bypass instructions). Eval fixtures are typed `EvalFixture`, `canon: false`, carry a NON-CANON banner, "describe the violation, never quote it," and their counts are verified by running the runner, never by inspection. A Monday `weekly-brain-health.yml` digest issue (lint status, `review_by` horizon, proposal ages, TestLogs awaiting retro, unwired feeds) is "the nag." Headless runs have fixed terminal lines (`Corrections encoded`, `Retro report ready`, `Proposal queue ready`, `Verdicts rendered`, `Assets rendered` / `Assets blocked`) and "never make rulings, never edit canon, never weaken a gate; output must land where a human already looks." Versioning: any change under `skills/` bumps the plugin minor; a contract break is major; canon-only changes do not bump.

### H8. Live data as contracts

Numbers never live in canon. A `DataFeed` concept holds the fetch contract only: metric definition, source of truth, query pattern, freshness window, staleness behaviour with approved fallback phrasing, publication rules; `status: unwired` is a demand marker. A Product → Metric Map resolves every figure to feed, endpoint, field, notation and publish-as term; "a field's notation is unrecorded → not publishable." Consumer copy takes the rates API, analysis takes the protocol API; if they disagree, surface both, never average. Field names are not copy (`star` → Prime Agent; `depositors` → suppliers). Sources: `client-product-harness:live-data`; `the client-data`; a client `assets/data/feeds/_contract.md`.

### H9. Personalization and setup skills

A setup skill produces the engagement files all downstream skills read: authority map, voice profile with verbatim calibration passages and an edit log, corpus registry pre-seeded with spent lines, red lines and approvals, client lexicon, baseline signals, a 90-day plan (li-exec-setup). Your own thought-piece skill carries a voice profile built from your op-ed and explainer with your connective kit. YouTube research merges a per-user trusted-channel overlay on top of a seeded list. the client-data carries `manual_inputs.json`, `counterparties.json` and a known-issues file of open decisions assigned to you. The pattern: capture the person's own words verbatim, log their edits as the most valuable training data, and let those outrank the generic standard.

### H10. Environment awareness and reproducibility

Skills state what runs where (Cowork sandbox vs Claude Code; allowlisted domains; `python-pptx` availability; Playwright executable path), include a `doctor` command, define a fallback ("apply the standard by hand and state that the deterministic check did not run"), and refuse to improvise around missing infrastructure (no ad-hoc pipeline re-implementation, no hand-built decks off the master). Reproducibility: `SKYDATA_RECORD` / `SKYDATA_REPLAY`, `.provenance.json` beside every report, a 15-minute cache, exit codes (0 ok, 2 unreachable, 3 validation fail), an offline regression suite on verbatim captured responses, a Node check that the Apps Script registry matches the Python registry, design assets reproducible from template + data JSON + seed + scale.

### H11. Roadmap pattern and the brain MCP

`FUTURE-DEPLOYMENTS.md` sequences: executive skills (one `SKILL.md` per recurring deliverable that hard-wires which concepts it always reads) → a dedicated brain MCP (`search_brain`, `get_concept`, `check_gates` with deterministic rows server-side and judgment rows returned as `needs_review`, `propose_edit` writing only under `pending/proposed/` on a branch with a `correction_id` grouping a cascade into one PR, `log_session`, `fetch_feed`) → live data feeds as contracts → storage backend decision (git vs Drive mirror, as an `Adapter`) → multi-entity expansion → TESTING MODE. "The server never writes to main; say it, merge it." Decided but pending: splitting the the client product and the-client brains into two hermetic harnesses. The the client product harness needs list names the next capabilities (social pillars and alerts, GTM playbook, programmatic visuals, Atlas monitoring TL;DR, landing-page copy, milestone detection, bug-bounty comms, docs optimization, PostHog dashboards).

### H12. Personal tooling practice

One-off personal Android tools are built with Claude Code on the laptop and installed as native APKs directly on the phone (not web apps, not Play Store), for offline use with camera, sensors, NFC, Bluetooth, files, notifications and background tasks. The same "build it only for me first" instinct shows in the listening platform (personal-use version launches first) and the sample-rate card-onboarding prototype (open on-ramp SDK plus permissionless contracts, no custom infra, reputable infrastructure only, Latin America first).

## Processes and artifacts for the team

Every team process you have shipped has the same shape: a fixed template with named fields, a gate that says when it is done, a named owner, and a cadence. They follow, grouped by what they produce.

### P1. Briefs and project setup

- **The one-page, six-question brief.** What is it? Why is it happening? Who is involved? When? Where? How do we plan on doing it? Delivered as a `.docx` titled "Project Brief: \[Project Name\]" with the closing note that extra detail belongs in strategy documents, planning documents and project-management systems. One page, no exceptions; never rename, reorder, skip or merge questions; "never apologize for keeping it brief." Only you and Raul create briefs. Sources: `project-brief-skill`; brain brief-making protocol; 20+ filled examples in Drive (Communications Guidelines V3, Fixed Yield sample-yield-token, sample-rate Rate Drop, a service agent Earn Launch, a service agent Case Study, Buyback Increase, WaPo interview…).
- **Brief Creation SOP (account managers).** Phase 0 trigger (client or internal) → Phase 1 gather the minimum set (Goal, Scope, Deadline, Budget, Stakeholders; identify workstreams) → Phase 2 draft a Google Doc `[Project Name] — Brief v1`, run `/project-brief-skill` with the transcript in the client's Claude project, sanity-check, save under Account Management → Projects, open the thread in the client's `*-all-projects` Slack channel ("one Slack thread = one project"), DM the strategy lead for approval, run `/presentation-i3` for the visual, client sign-off before internal briefing. Done when the brief is strategy-approved before the visual and the visual is client-approved before briefing; "the .docx is the canonical source." Source: [Brief Creation SOP](https://app.notion.com/p/3639bfc98f9f808bbfebcac94e41a160).
- **Three things per project** (the client product commitment): a brief, a Notion project plan, a Slack project thread. AM Project Management SOP: create the Notion project from the standard template (tasks as `[task] — [accountable] — [due date]`, converted to To-Do rows), async brainstorm in the thread, kickoff call, clean task list within 5 working days of a locked brief, daily overdue digest from the PM agent, close-out with Post-Mortem and Case Study SOPs. Client project pages follow `# BRIEF` (embedded Drive brief) → `# LINKS` → `# TASKS`, with tracker status `BRIEFING → ON TRACK / OFF TRACK / BLOCKED / IN REVIEW / ON HOLD → COMPLETE / DID NOT FINISH` and a workstream tag. Source: [AM Project Management SOP](https://app.notion.com/p/3639bfc98f9f81cb9118fc26fade1f50).

### P2. Content production chain

- **Standard approval chain:** Brief → Draft (5-pass) → Review (you) → Legal flag (a legal reviewer via the brand's legal seat) → Approve (you) → Publish → Log. a reviewer quotes run I3 drafts → a stakeholder → PR revises → your deep review → a stakeholder to a reviewer → David Garcia Rios legal. PR runs a weekly Monday rhythm (news topics → a stakeholder R → a reviewer → publish). FUD response: Daniele alerts → you approve → execute. Biweekly cadences with a stakeholder/a reviewer and with the a service agent and a service agent leads. Source: [approval-chains.md](https://drive.google.com/file/d/1KRXnM3nXf5Dhmov7d87zJNAtp1ihOPjf/view).
- **Content Management DB and page template:** status pipeline `Writing → Needs visuals → Ready for internal review → Ready to client review → Needs edits → Scheduled → Ready to Ship → Shipped` (plus `DNQ`), 16 content pillars, 17 channels, a Needs Visuals flag with its own creative status and owner. Each content page: `CONTEXT/BRIEF` → a brand section with numbered `COPY #n` callouts (threads as `1/ 2/`) → a second brand section → `ANNOUNCEMENTS` (LinkedIn, Discord). Source: the client portal content DB and the Transparency Standard template.
- **Blog lifecycle:** 20 stages with two blocking gates (positioning gate owned by Aymeric; legal gate), SLAs (review 2 days, positioning 2, legal 5, partner 3, build 3), four posts a month, measurement wired at draft time, "the approval chain, not drafting, is the bottleneck." Three format protocols: product explainer (keystone; Key Takeaways in the order Identity / Primary product / Range / Governance; five story beats Hook / Stake / Conflict / Resolution / Output), campaign-tied (a beat gate with four written answers before drafting: is the beat confirmed and by whom, which claims depend on it, what is the fallback, what must not be named; refresh date at publish; no forward hook), co-marketing (partner gate: the client side first, partner confirms its own mechanics in writing, comparative section never ranks, simultaneous publish). A published-blog register prevents repeats (differentiation check: target claimed? spent opener? recycled closing? inherited open correction?). Source: `client-product-harness:blog`.
- **Six-deliverable blog output contract:** fact sheet; alignment table; draft with header (AEO target, Big Idea, pillar, UTM requested from a collaborator never invented, title tag, H1, slug, meta, category, word target, legal flags); gate report; handoff note naming the next gate; proposals.

### P3. Launches and campaigns (GTM playbook)

Cadence T−2 weeks → T+30 days: campaign strategy doc (objectives including "establish the product as a recurring content pillar," quantified internal goal, positioning rules, partner audience split, day-by-day timeline with amplification per beat, influencer strategy) → brief, positioning and legal review → AEO target and landing page → entity file drafted in launch week → influencer briefs → T−5 internal review on staging and client greenlight → T−4 assets locked → T−1 product-readiness no-go gate → T+0 pages live early, announcement at a set hour with simultaneous partner publish and the amplification stack (partner RT, ambassador accounts, ecosystem RTs, town-hall ask, micro-influencers within 60 minutes, reply team 3–4 hours) → T+1 explainer video pinned plus macro-KOL long-form → T+2–3 rate beat with live figure and launch blog → T+3–4 proof beat → T+9 adoption baseline and instrumentation audit → T+30 five-section report (Social, KOL/signal, Funnel, SEO/AEO, Mindshare; insights end "repeat / change / stop"). Eleven rules from the Fixed Yield evidence: announcement and explainer both mandatory; readiness gates comms; one consumer name in all copy; explicit partner audience split; no launch KOL post on a weekend (\~12× signal penalty); KOL content is the creator's own thesis briefed with talking points, banned words and a per-creator UTM; judge by signal not impressions; do not expect organic search from a launch; set the day-9 baseline or lose it; entity file in launch week; plan post-peak cadence (mindshare decays to \~zero within two weeks). Influencer brief template: what this is about plus three rules; who you are writing for; 10 talking points; headlines you can use; words you can and cannot say; an IS / IS-NOT table; UTM posted as a comment. Can/cannot lists are rebuilt per campaign from the decisions log, never copied. Source: `client-product-harness:gtm-launch`.

### P4. Reporting

- **Monthly and quarterly report skill:** gather confirmed decisions in the window (date, decision-maker, one line) → metrics via feeds only → check OKRs ("No OKRs on file yet" stated plainly if empty) → assemble `Report period / As-of → OKR status → Confirmed activity → Metrics (value, as-of, feed + field, reference, or deferral) → Deliverables → Gaps flagged`. No projections, ever; GA4 and PostHog never summed; every metric for BD/private use carries as-of, source, methodology, owner and refresh cadence.
- **Top Metrics SOP (per channel):** each channel owner reports 3–5 metrics with a metric definition, type, baseline, numbered steps, owner and due date; the monthly structure is one table with no interpretation, one paragraph per metric, one action item per metric; assembled by Daniel, reviewed by you, by the 7th. PR: TAV weighted Tier 1 ×5, Tier 2 ×2, Tier 3 ×1; key-message penetration in a 60-token window; pillar-alignment share; spokesperson SOV; sentiment. Social: impressions, engagement rate with floors (1.5% / 0.8%), new followers recorded on the 1st, mindshare floor, ICP-quality followers in an ICP Follower Log (Date, Handle, Account Name, Account Type, Source Event, Follow-up Action, Owner) with a 48-hour spike audit and quarterly review by you. "Impressions and engagement are metrics, not KPIs." Source: [Top Metrics SOP](https://drive.google.com/file/d/1L9gOitF6ABhXiOkAt4Jb8qtj7rxPXfV88KI3h-V2ROw/view).
- **Quarterly report cycle:** metrics sheet fed by Apps Script from the client.data; BA figure-check checklist (E8); reviewer comments resolved by you on the report and the Insights Call script; rollout strategy notes; a monthly operational and financial update needing a documented BA greenlight.
- **PR campaign wrap report** (Kim's playbook, reviewed by you): within 5 business days; pull and verify tracker rows (URL, Publication, Date, Language, Country, Sentiment, verified Reach, Tier) → frame → draft to template (header stat box; Executive Summary; Strategy as "the action / the why"; Results with coverage pacing; Post-Mortem with 2–3 sharpenings; coverage tracker appendix) → verify → edit ruthlessly; 11-item pre-send checklist.
- **August report outline pattern:** how decisions are made → shared goals → narratives / campaigns / projects → the six narratives → stakeholder filters (Legal, Engineering, Governance, Primes, Data, BD/CM) each with the artifact that answers it → measurement link → the four key messages → trust proxy.

### P5. Decks and presentations (presentation-i3)

One JSON spec builds either a `.pptx` on the the client product master or an HTML deck; a deck not on the master is off-brand by definition. Workflow: inventory the content one line per slide (takeaway, numbers, proof, relationship) → pick the arc then the rhythm (five arcs with slot tables: weekly-highlights 6–10, problem-evidence-action 8–12, before-after 6–10, proposal 8–12, client-update 5–8; show the plan first if more than 10 slides) → pick each of 17 master layouts → write copy under the writing rules (never round a number; headlines state findings; strip filler, superlatives, hedging, AI starters; no dashes) → build (the build refuses collisions, unknown fields, ragged tables, charts with fewer than two real values) → check (no two neighbours share a silhouette; number above its sentence; accent at most once per slide; logo grids equal). Design system v1.3 (reviewed with a designer): one point per slide, quiet institutional editorial, one accent at a time, 12-column grid, Inter only, 13 principles, chart rules (ink plus one accent, no 3D, pie or donut, bars from zero), motion rules, and 18 review lessons recorded as "what went wrong → rule." Six known master issues are raised with a designer, never worked around.

### P6. Case studies

Monthly the client Agent allocation case studies on client-example.invalid (a service agent/Galaxy as model, a service agent FX Layer next) in the a service agent page-copy slot format with word targets; a 7-question Agent Case Study Questionnaire (consent and sensitivity check → the story → what was solved → what is possible now → the one sentence an institutional reader should remember → capital-flow overview for visuals); a one-slide Case Study Canvas (Situational Overview, Client Problem and Challenge, Our Strategy and Solution with 2–4 tactics, Key Results "numbers first, narrative second"). Partner-sourced figures are bracketed for partner sign-off; the client is framed as issuer and liquidity foundation with governance setting parameters, never as allocator.

### P7. Process standardization (interviews to playbook)

A clean-run pipeline parameterized by a role-family taxonomy and an optional external framework: bootstrap (numbered folders `00_inputs` → `04_prompts`, a controller with six rules, a master project prompt) → one lossless extraction per interview (11 sections; process cards with 18 fixed fields; "when in doubt, keep the quote") → cross-interview synthesis (build the action comparison matrix first, derive the team SWOT from it, classify every action STANDARDIZE / TEMPLATIZE / PRESERVE-VARIANT) → action manifest with permanent slug ids, a source map and action families → SOP v1 from team practice only (14 sections, every step labelled FACT / INFERENCE / RECOMMENDATION, evidence citations table) → SOP v2 overlaying the framework ("an optimization layer, not a rewrite mandate"; change log Validate / Add / Modify / Remove) → a two-page review summary per interviewee ("here is what we wrote down," "your version was preserved as a variant," "please correct anything wrong here") → the 12-section rollout playbook (Executive Summary with a standardization-levels table; Mission and Scope; Role-Family Map; Operating Cadence; Action Families; SOP Catalog; Cross-Family Handoffs; Tools; Definition of Done; Escalation; Onboarding week 1 read / week 2 shadow / week 3 own / day 30 sign-off; Maintenance and Revision) with a five-check QA. An audit skill infers the stage from folder structure alone. No patch mode: new evidence re-runs the stage. Source: `process-standardization` plugin.

### P8. Team rituals and personal operating system

- **Post-Mortem SOP** (a collaborator's, applied by the team): five questions in fixed order (went well / didn't / keep / stop / add), time-boxed, written, shared; "if nothing changes after a post-mortem, it was documentation, not learning."
- **Weekly Focus log:** Week of, Focus (Briefing & Positioning / Reviewing & Alignment / Goal-Tracking / Other), What Went Well, What didn't go Well, related tasks.
- **Q4 Focuses (Tuesday review with a collaborator):** one static row per focus (F1 Reporting & Insights, F2 Briefing & Positioning, F3 Reviews & Alignment, F4 Empowering the Team) with Last Updated (updated every week even when nothing changed), Key Results with dates, Current Issues / Blockers (one sentence each as problem, root cause, solution; carried until closed), Resolved (copied verbatim with close date), Notes. Each focus page holds a goal callout, KR checkboxes and a Week | Date | Issue | Resolved? log. Source: [Q4 Focuses](https://app.notion.com/p/cff68593f5144f529aa5b8ad0c1edc2b).
- **Three-Sentence Framework** (company commitment, `/three-sentence-framework`): Problem → Root Cause → Solution, one sentence each, no clauses joined by "and." Coaching path: find the real problem under the symptom; chase the root cause with the reversal test and the "another why" test, watching for false bottoms ("nobody owns it," "no process," "too busy," "communication is bad"); land one solution. 70% coach, 30% direct. Interpersonal issues are reframed upward to decision rights and role clarity.
- **OOO handover template:** dates away, confirmed replacement, emergency contact; per client "what's happening this week"; a Task | Instructions / Links | Owner table; Notes / Watch-outs; If you want to unblock; Anything that could go sideways; links to legal and comms guidelines, the brain, dashboards; project task views. Source: [the author OOO](https://app.notion.com/p/2fb9bfc98f9f80efb523d9f0b23703ff).
- **the author dashboard:** quarterly primary and secondary focuses, Q4 Focuses, tasks, Weekly Focus, projects, in one Notion page.
- **To-do conventions** (`todo` skill over the company To-Do DB): Priority values Daily Checks / High / Medium / Low / Follow Up / Daily focus; Status buckets DUE TODAY / DUE THIS WEEK / DUE LATER / BLOCKED set only when named, never inferred from dates; Done is a separate checkbox.

### P9. Executive LinkedIn programme (li-exec suite)

Setup → Ideas → Write or Longform → Review → Report, with report feeding back into ideas and setup. Setup gathers six inputs in one message, defines a territory that passes "when \[specific buyer\] has \[specific problem\], they should read \[executive\]," 2–3 pillars plus a human lane (at most 1 post in 5), 20 earned secrets, 5–10 arguable positions each with "what would change their mind," a proof bank, red lines and approvers, a corpus registry, a 90-day plan; voice captured in a 45–60 minute recorded call with ten story-and-decision questions. Ideas pass four tests plus territory (Earned, Arguable, Evidenced, Useful, On-territory), get a Big Idea under 30 words, an archetype (8), a form, a hook type (6), an ending type (4), and obey calendar rules (2–3 posts a week, one long-form a month, never more than one a day, at least half on earned secrets, at most one correction and one prediction a month, no archetype, hook or ending twice in a row, quiet periods blocked, one open news slot a fortnight). Posts run 900–2,000 characters with numeric budgets; comments add the number or counter-case the post lacked; carousels 8–12 slides with slide 1 a claim plus source. Review has Detect, Edit and Full modes. The monthly report reads authority signals against baseline (profile views from target roles, inbound DMs citing a post, invitations, insider saves, 15+ word comments; "impressions and likes are diagnostic only"), what worked by pillar and archetype using medians, repetition and voice-drift checks, and decides at most three changes. Governance covers ghostwriting ethics, approvals by content type, disclosure, a 48-hour news fast track, publishing protocol and account access (agency staff never log in as the exec). An evidence base (researched October 2026, each finding with URL and confidence) separates effects from folklore.

### P10. Client funnel mapping

Map a client's funnel as a left-to-right flow on a Miro board: pin the period's goal in every frame subtitle; split always-on from campaigns; one lane per channel with its mechanism (Channels → How we move people → Where we send them → Sign up → Account → Activate → Nurture → Convert → Retain); amplifier channels labelled; conversion numbers only when sourced; drop-offs in pink with green fixes; two bottom rows (where people drop off; agency audit: take over / recommend / hold until / after). Campaign funnels add teaser phase, an eligibility diamond, an engagement loop and a single conversion moment; a channel-by-week table and an email sequence table; an email audit doc (streams, full copy, nine look-fors including compliance lines); a take-over scope and a 20–30 question pre-call bank grouped so different client people can answer. Colour code: Agency `#FFE86D`, Client `#9CE6FF`, Not confirmed grey dashed, Drop-off `#FD9AE7`, Fix `#B3E65F`. Rules: don't invent (unconfirmed is grey dashed "to confirm"); respect the user's board edits; never delete without a clear yes; client-facing wording, sentence case, no em dashes. Source: `client-funnel-mapper`.

### P11. Design assets, documentation and portals

- **Design assets by slot-filling:** 11 production templates (co-branded with leading / equal / partner-led tiers, social, tagline banner, report cover, wide banner, section divider, insight text, bar chart, table, metric highlight) rendered by a versioned generator; "you fill slots, you never invent layout, colors, type or logo treatment"; any figure needs a filled `source_line` ("a figure from memory is a block, not a render"); co-branded assets need recorded partner sign-off ("a supplied logo is provenance, not permission"); every delivery includes the reproducible command. Design system tokens were extracted from Figma into CSS; an ecosystem map graphic and an the client product performance dashboard were built on the same foundations.
- **Developer documentation:** reverse-engineered API specs; GitBook export linked to `jansko-tech/the client-money-docs-draft`; docs PRs under the 18-item audit (E12); `star` never appears in docs.
- **Client portal (Notion):** Drive links per brand; an Internal Meeting Agenda as an IODS log (Issues, Opportunities, Discussions); external meeting agendas per stakeholder group; project management DB; personal content calendars for John and Greg; the Content Management DB with per-workstream views; creative asset request dashboards; a cross-department KPI and OKR tracker.
- **Personas and ICP packs** (S6) loaded into a Claude project so the team gets ICP-eye feedback on content and ideas.
- **Strategy Toolkit and SOPs database:** the shared shelf (Business Line the client product / Eco / Insights, Created By, Delivers to) holding the folder tree, Post-Mortem SOP, Strategy Foundations, Deck Builder Agent, Agentic Client Research system, Agentic Listening system, Investor Relations services reference, case studies.
- **Brain onboarding:** an all-hands presentation "Client Brain: how to use the brain and how to make it better over time," plus role-based quick-reference workflows in `HOW-TO-USE-THIS-BRAIN.md` for AI agents, social, PR, design, IR, KOL, AEO, community, events and analytics.

## Analytics and measurement

Analytics work is governed by one rule applied everywhere: no number without its window, surface, unit and caveat, and no cause without an artifact. The methods below turn that rule into recipes, defect lists, decision frames and cadences.

### A1. PostHog question method (the client product)

Procedure: find the recipe row for the question (events, dimension, tool, caveat; build one if missing and propose adding it) → verify the schema before querying, even for `$pageview` ("never query a guessed event name") → check whether an insight or dashboard already exists (\~60 insights, 16 dashboards; reuse inherits methodology) → query with the typed tools, `execute-sql` only for entity search, joins, windows and `tx_hash` dedup → apply the defects → answer in the six-part template: number with unit, window (and whether it predates the instrumentation floor), surface, events and dimensions, caveat, `reference`. Three output states: Answered / Answered with a hole / Cannot answer ("'I can't tell you that, and here is the one-line fix' is a decision; a shrug is not"). Dashboards write the caveat into the insight description. Three standing question shapes: time-constrained, module-constrained, segment-constrained. Source: `client-product-harness:posthog-analytics`.

### A2. The eleven known defects (applied before any number ships)

1 Cross-subdomain identity is not bridged, so marketing-to-app conversion is a floor, never the rate. 2 Self-referral overwrite: `the client product` in `$initial_referring_domain` is a bug, not a channel. 3 Fixed Yield `app_widget_flow_started` is not wired. 4 Amounts are token units: break down by token or restrict to stablecoins as USD-approximate; exclude approve artifacts. 5 Dedupe onchain volume by `tx_hash`. 6 Geo is IP-based and VPN-distorted. 7 `net` is observed-since-instrumentation, not a balance. 8 `module` is the taxonomy; `product` only tags campaigns. 9 Bots are in raw data (filter to them for AEO questions). 10 Small-N steps are directional only; a percentage needs N ≥ 100. 11 UTM campaign tagging is not implemented and "fails silently in the direction of it didn't work" (verify population with `coalesce(prop,'<null>')`, never `!= ''`). Earlier findings in the same spirit: a France transaction with an unnormalized token amount; a high null rate on `product` in supply events; amount fields read with `toFloat(toString(properties.amount))` to avoid mixed-type errors; geo fields in bracket notation; pre-built insights discovered via `system.insights`.

### A3. Seven methodology rules and the cross-source doctrine

Name the window and the instrumentation floor; say which surface; unique users are `uniq(person_id)` never `distinct_id`; wallets are `wallet_address` and a wallet is not a user; never sum PostHog and GA4; PostHog measures the interface, not the protocol; attribute conservatively (round down). Cross-source: never present PostHog as protocol or divide one by the other; "sequence, don't merge"; name the source on every number. PostHog data is tagged app-instrumented and flagged for on-chain corroboration (Nansen, Arkham, Dune) rather than cited as ground truth. For AEO measurement the six rules are unit definition (never sum cross-platform), bot exclusion, funnels PostHog-only, N ≥ 100 per cell before any percentage, causality vs correlation with named confounders, reproducibility (source + date range + filter set); Semrush is client-verifiable, Momo Oslo is internal and labelled.

### A4. Segments and the two grains

13 person cohorts with windows baked in versus 7 wallet ICP profiles assigned first-match in order (Institutional/custody; Incentive farmer; Whale net ≥ $1M; Dust gross < $1K; Rotated out; Set-and-forget saver; Active individual) plus `size_tier` and `provider_tier`. "The two grains do not compose freely" (a composition matrix says which combinations are valid). Six rules: name the grain; profiles are heuristic triage; never publish a wallet address; the `net` caveat; small segments are directional; first match wins.

### A5. Six decision frames (when nobody has a question)

1 Did this campaign buy customers or rent volume? (profile mix vs the prior window). 2 Is the funnel leaking at intent or execution? (two intra-domain ratios, never an end-to-end rate). 3 Which channels bring wallets that stay? (net retained per wallet). 4 Growing by new wallets or by existing wallets deepening? 5 Which segment is this page reaching? 6 What did the geo-block cost? Monthly runs frames 1–4; per launch 1, 2, 4; quarterly all six with a baseline refresh. Cadence: a weekly pulse of \~10 minutes ("meant to be boring"; instrumentation before behaviour; "a quiet week is a result"), a monthly review of \~60 minutes ("write the read, not the numbers"), quarterly recalibration (baselines, dashboard audit, schema re-verify), and per launch (baseline, PostHog annotation on launch day, day 9 and day 30 reads).

### A6. Launch and funnel readings established from evidence

Social acts one layer up (site lift, not app referrals); web-to-app conversion is a stable \~50% constant, not a lever; in-app adoption is the scoreboard; branded impressions spike \~3× with no clicks; campaign attribution is a proxy until UTM tagging lands; signal (Cookie3-style quality-weighted attention: 5–10 solid, 30–50 outstanding, 80s–100s a day spike, 200–500+ viral) beats impressions; the majority of peak-week attention should be generated outside the official account (June: own 32% / other projects 44% / KOLs 18% / others 6%). Every retro states which recommendations are evidence-backed and which are extrapolation from one measured launch.

### A7. Protocol numbers (the client-data)

Question shape maps to a command: level (`metric sky_reserves -p QTD`), comparison (`--yoy`), composition, change (`trace`), history (`position service-agent a sample asset --days 365`), quarterly or monthly report fill with `--validate`, governance (`spells --detail`, `settlements`), Atlas lookup, draft wording lint. Period grammar covers `2026-Q3`, `Q4 '25`, `2026-08`, `QTD`, `MTD`, `YTD` and ranges; open periods carry a note and align YoY to the same number of days. A registry of \~70 metric ids, each value carrying unit, status (`ok / partial / stale / unavailable / manual / error`), as-of, method, source URLs and notes; only `ok` may be pasted as final. Answers are prose, not bullets: what the number is and as of when; the last natural reference point; what moved, absolute and relative; what drove it, naming mechanism and artifact with date and link; what to watch next; API field names out; every WARN carried. A "what moves each number" map (the client Reserves, Gross and Net Protocol Revenue, Net Protocol Surplus, sample-yield-token supply, sample-rate via SP-BEAM, the client supply via burns, buybacks paced by prior surplus, counterparty allocations) and a methodology file (surplus waterfall steps, reserve targets, settlement cycle formulas, APY vs APR, restatement rule, on-chain reconciliation path). Source: `the client-data`.

### A8. Historic deep-dive patterns

Traffic spikes are explained by identifying top days by module volume, traffic sources and protocol-level correlation; app-to-marketing-site funnels are measured; modules are ranked across clicks and funds moved. Findings become canon facts only after review (the client staking is effectively app-native; sample-rate is protocol-wide; the cross-domain identity gap needs Kacper and Kuba). Toolchain bugs found along the way are documented, not worked around silently (sign-convention errors, egress-blocked API feeds, misclassified 403s; "never tell an operator the API is down on the strength of a local failure").

### A9. Measurement pipelines you designed

- **Marketing → Revenue Signals Pipeline:** connect marketing analytics to product analytics to show which channels contribute to revenue (Notion project).
- **Full strategic tracking pipeline:** per-workflow ideal flows and what is missing, data sources per workflow, and an ideal stack (SEO: DataForSEO, GSC API, SerpBear, Librecrawl/ScreamingFrog, Semdash; AEO: xSeek, Momo Oslo; Social: X API, Nobody, SocialData; Website: PostHog, GA4, Cookie3; IR: Attio, Airtable; Events: Luma; PR: Mediacloud, GDELT); a prefixed list of metrics currently tracked (SM, CR, SEO, AEO, Web, Blog, IR, PR, IM).
- **SEO/AEO monitoring workbench** (Apps Script, built for Momo Oslo, the client as seed client): PostHog AEO prompt-universe tracking, GSC rank tracking, SerpApi SERP monitoring, Page X-Ray, Core Web Vitals, on an append-only log architecture so it duplicates per client.
- **Social listening metric conventions:** reach = sum of views from the X API; baseline from the front-end date range; amplifier identity in scope; dashboards per launch.
- **PR dashboard and methodology v1** (June 2026) and an AEO prompt-analysis methodology write-up for a collaborator (old vs new ChatGPT chats).
- **Analytics migration checklist** and the plan to replace Observatory reads in the quarterly metrics sheet with the client.data equivalents.

## Tooling and infrastructure

The stack is fixed by the the client product playbook (Slack for communication, Notion for projects and tasks, Drive for files, Claude for intelligence and automation) and extended per workstream. What matters for packaging is the reusable building blocks you have already written and the quirks you have already learned.

### T1. Platforms by job

| Job | Tools | Notes you established |
| --- | --- | --- |
| Knowledge and canon | Google Drive brains (the client All root `1dQjFxrkJAdzIugWr2Fbg7mZ9YLD-uLAT`; the-client `1Wgkdxe82aj4gASSb16hDvUJspNHBR9XA`; the client-money `1A6F4ZKhFkeRXPvboxEVTkWx7nXNSn3Pr`; a client `1RHJNqIlDCGqDol_orXzo52-e3gvC7h2o`; ingest `18zFEwNJh9rL8UVyTgbJpSgD6ZC9-uoKh`), repo-as-plugin harnesses, Qdrant as a second-tier index | Brain files on disk are authoritative; Qdrant second; ask you third. The May 8, 2026 hub compression file is stale and off-limits |
| Protocol data | the client.data.blockanalitica.com (REFERENCE tier), info-the client.blockanalitica.com, api.the client product rates, BA Labs Observatory (no auth), client-example.invalid, Ethereum RPC | the client.data and client-example.invalid are blocked from the sandbox but reachable from Apps Script; consumer copy takes the rates API, analysis the protocol API |
| Product analytics | PostHog EU, project 124805, dashboard 762881; GA4 with cross-domain tracking pending the client product | `execute-sql` for joins and dedup; typed query tools otherwise; GA4 and PostHog never summed |
| Search and AEO | Semrush (`execute_report`; AI Visibility toolkit needs a manual UI pull), GSC, Momo Oslo, SerpApi, Page X-Ray, Core Web Vitals, Google Apps Script workbench | Prompt universe lives outside the brain; tool scores are run-scoped `reference` |
| Social data | twitterAPI.io (snake\_case fields, legacy date format, `next_cursor` pagination), n8n at n8n.the client product.co, Postgres, Jev (TypeSafe) enrichment | No n8n for the listening platform; local PostgreSQL first |
| Project and tasks | Notion (the client product workspace; SQL needs the Business/AI plan, so `notion-search` with `collection://[UUID]`; entries use `data_source_id` as parent; gallery views need both ids), company To-Do DB, Mario PM agent | One Slack thread = one project; Notion tracker with mandatory due dates |
| Comms | Slack the-consultancy (primary the client thread C0B14TGJ202; Soter Labs C0AMAQLFN5S; the client-eco-iods C0AHGJ4DVPB), Circleback transcripts | URL timestamp `p1234567890123456` converts to API `1234567890.123456`; `slack_read_thread` with channel id and timestamp resolves threads reliably |
| Web and docs | Webflow (partial MCP; `get_asset_preview` reliable; fetch the live site for nav; staging `the client-eco-staging.webflow.io`), GitBook linked to `jansko-tech/the client-money-docs-draft`, GitHub | Docs PRs open under confirmed direct-push authorization; Kuba/Johny review gates merge |
| Design | Figma (tokens exported to CSS), Canva, the design-asset generator (Node 18+, Puppeteer or system Chromium), presentation-i3 master `.pptx` | Design evolves in a generator repo verified by overlay-diff, then vendored |
| Documents | Node `docx` library build scripts, pandoc text verification, LibreOffice PDF for layout, `/mnt/skills/public/docx/scripts/office/validate.py` | Table content width 9360 DXA; three-column tables `[3120, 3120, 3120]`; split mixed-span rows into sequential tables; `headerRow` needs an explicit span |
| IR and events | Attio, Airtable, kit.com (investor newsletter), Luma | Newsletter chain: Kostas writes → a stakeholder reviews → VP into kit.com → Kostas final |
| Personal | Framework Laptop 16 on Fedora Workstation (GNOME on Wayland); Claude Code on the laptop; native Android APKs sideloaded | Personal tools are never published |

### T2. Reusable code you own

- `harness/specs/copy-gates/run.py` with 26 gate specs and eval fixtures (client-product-harness).
- `li_gates.py` (31 gates, METRICS line, waivers, lexicon) and `selftest.py` with 18 fixtures (li-exec suite).
- `scripts/skydata/` package of 17 modules with `the client.py` (doctor, metric, trace, position, report, validate, spells, settlements, atlas, lint), `lint.py` (26 regexes), an offline test suite on verbatim captures, and `apps_script/SkyData.gs` kept in sync by a Node check; `fetch_sky_api.py` (736 lines, 61 offline parser checks) in the harness.
- `okf-lint.py` and `harness-lint.py` plus the `weekly-brain-health.yml` and `okf-lint.yml` CI workflows (a client and client-product harnesses).
- `lib/deck.py`, `lib/fit.py`, `lib/regen_layouts.py`, `templates/deck-base.html`, `templates/build-master.js`, `assets/the client product-slides-master.pptx` (presentation-i3).
- `yt_research.py` (71.5KB single file) with `trusted-channels.json` seeds per domain (youtube-research).
- The design-asset generator (`generate.mjs`, `templates.json` v2.0.0, playbooks for quarterly report, data analysis, governance update, metric highlight; `scripts/setup.sh --doctor`).
- `audit_checks.py` (488 lines) covering 10 of the 18 docs-audit items.
- The inline structural-audit counters in `the client-thought-piece` (final-sentence word counts, punch paragraphs, negation-correction, meta signposts, ring check, corpus grep).
- Apps Script: the SEO/AEO monitoring workbench, the BA Labs Observatory metrics fetcher for the quarterly sheet, the Google News PR proxy, the X-listening sheets.
- n8n flows: Circleback → Drive ingest; the warm-introduction graph.

### T3. Drive and Notion mechanics worth keeping

- Drive: `parentId = '[folder-id]'` reliably lists direct children; `title = '_ingest' and mimeType = 'application/vnd.google-apps.folder'` finds folders by name; creating markdown needs `contentMimeType: text/markdown` plus `disableConversionToGoogleType: True` together or it silently becomes a Google Doc; navigate a brain by its index file first, then subfolder ids; file ids come from the string after `/d/` in sharing URLs; the the client product MCP's `docs_replace` works on Google Docs only, Drive markdown is create-only.
- Sheets: `download_file_content` with `exportMimeType: text/csv` captures only the first tab; export other tabs by tab id.
- Brain maintenance: pre-flight audit with `rclone lsf`; no file overwritten without a versioned `_archive/file_YYYY-MM-DD.md` backup; staging in `shared/brain-staging/`; kebab-case names; README routing updated; Qdrant sync tagged `brain-sync-YYYY-MM-DD`; recovery is Stop, Identify, Restore, Report.
- Output location in sandboxed sessions is `/mnt/user-data/outputs/`; deliverables are validated before delivery.

### T4. Sandbox and environment rules

- Domains blocked from the cloud sandbox are reached from Apps Script or Claude Code on the laptop; for the YouTube skill you asked the org admin to whitelist the needed domains.
- Two kinds of 403 are diagnosed separately (CONNECT-tunnel block vs origin WAF) before anyone is told an API is down.
- Skills run `doctor` or `selftest` first and fall back to the hand procedure, stating that the mechanical check did not run.
- Session recovery: compacted sessions are recovered with conversation search on methodology terms (lane names, card structure) rather than by asking you; the active project system prompt outranks framing found in compaction summaries.

## Method index

142 repeatable methods, one line each, grouped by area, with the artifact that holds the full version. Section labels (S, R, E, H, P, A, T) point back to the write-ups above.

| # | Method | What it is | Area | Lives in |
| --- | --- | --- | --- | --- |
| 1 | Goals, workflows, projects, campaigns, narratives | Three strategic goals; typed work items; four strategy cadences (S1) | Strategy | \[PLAN\] tracking pipeline doc (Drive) |
| 2 | Foundational strategy workflow | Research → ICP → Positioning → Narrative & Messaging → Brand Voice (S2) | Strategy | Notion: i3 Strategy Foundations |
| 3 | Agentic Flows dependency map | Dossier → questions → research → positioning → ICP → messaging → ToV → content → distribution (S2) | Strategy | Notion: Agentic Flows DB |
| 4 | the client product Strategy Canvas | Eight frameworks in strict order plus snapshot and gaps (S3) | Strategy | Drive canvases; Strategy Canvas Claude project |
| 5 | Canvas provenance tags | `[Sourced]` / `[Inferred]` / `[Gap]` on every bullet (S3) | Strategy | Canvas docs |
| 6 | Positioning rulings | Category label, unfair advantage, mechanism not outcomes, pillar tests (S4) | Strategy | a client project memory |
| 7 | a source document structure | Lead message → talking points → terminology → guardrails → narratives others own (S5) | Strategy | Drive: the client a source document v3 |
| 8 | ICP workspace and persona pack | Gather, clean, organize by faithfulness; HoDA persona project (S6) | Strategy | the client Brain project |
| 9 | Research-for-persuasion | Prove/disprove, data hierarchy by persuasive weight, concessions, falsifiable review (S7) | Strategy | Drive: Social Visibility Methodology |
| 10 | Strategy deck conventions | Skycast design language; plain copy; offsite session with timers (S8) | Strategy | Memory |
| 11 | Campaign doc mirroring | New campaign docs copy the last proven structure and roster (S9) | Strategy | Memory |
| 12 | Manifesto gates | Written sign-off, speakable components, embargo scope before publication (S9) | Strategy | Memory |
| 13 | Strategy folder tree | 0 Research → 1 Core Frameworks → 2 Briefs → 3 Campaigns → 4 Agentic & SEO (S10) | Strategy | Notion: Google Drive Folder Tree |
| 14 | Agentic Client Research and Positioning System | Dossier agent → \~50 DATA/LISTEN/TEAM questions → research agent → strategy doc (S2) | Strategy | Notion toolkit entry |
| 15 | Manual-first planning (CANs) | Plan the manual steps, then place the agent; three mapping steps (principle 10) | Strategy | Notion: the author's Notes |
| 16 | I3 Intelligence Card and Leads CRM | Fixed card sections, LOW/MEDIUM/HIGH scores, confidence, gaps, CRM schema (R1) | Research | Notion: I3 Leads CRM |
| 17 | the client Intelligence Card | Lane classification YIELD SEEKER / AGENT BUILDER / NONE plus engagement strategy (R1) | Research | IR Lead Research project |
| 18 | Inbound disambiguation | Read the Slack thread before researching the surface ask (R1) | Research | New Business project memory |
| 19 | OSINT lead screening | One row per person, documented the client ties discarded to a separate tab (R1) | Research | Memory |
| 20 | the client source ladder | Atlas → on-chain → spells → dashboards; interface never a protocol source (R2) | Research | the client Brain preferences |
| 21 | Blog research protocol | Verification half vs motivation half, nine-rung ladder, under-informed gate, fact sheet (R2) | Research | client-product-harness:blog research.md |
| 22 | Story tracing | Evidence chain strongest first; classify mechanism before searching; cause needs artifact (R3) | Research | the client-data story-tracing.md |
| 23 | ICP Behavioral Search Instrument | Hypotheses → SEMrush clusters with kill criteria → GSC reads → routing rule (R4) | Research | Drive doc |
| 24 | AEO prompt-universe loop | Monthly refresh, coverage score, gap, idea, keyword research after idea (R5) | Research | aeo-seo; Top Metrics SOP |
| 25 | YouTube research | Four modes, six-component score, trust tiers, fixed weights (R6) | Research | youtube-research skill |
| 26 | Social listening platform spec | Database, Jev enrichment, saved boolean queries, per-launch dashboards (R7) | Research | the client Brain project spec v1.0 |
| 27 | Recon harness charter | Charter, index, listening map, 12-type daily pass, report changes not volume (R7) | Research | Drive recon folder |
| 28 | Warm-intro social graph | Mutual-connection matching routed through mutuals (R7) | Research | Memory |
| 29 | Knowledge-base audit protocol | Strong/Medium/Weak findings, fixed finding format, cumulative logs (R8) | Research | the client Brain Auditor project |
| 30 | API reverse-engineering specs | Endpoints from compiled bundles into developer specs (R10) | Research | Memory |
| 31 | PostHog schema integration guide | Event taxonomy, exports, ETL, dashboard queries (R10) | Research | Memory |
| 32 | Reference-list deliverable | No-nonsense source list with why each matters (R10) | Research | the client Brain preferences |
| 33 | 5-Pass Copywriting Method | Big Idea → Factual Anchoring → Voice → Storytelling → Compliance → Format (E1) | Editing | Brain protocol; copy-review skills |
| 34 | Brief-making passes | Scope → Draft the Six → Numbers → Framing → Cut to one page → Compliance (E2) | Editing | Brain brief-making protocol |
| 35 | Craft layer | Brief contract, big-idea gate, 19 drafting rules, numeric budgets (E3) | Editing | the client-thought-piece; blog; copy-review; li-exec 07 |
| 36 | Tell registry and structural audit | 19 structural tells with budgets; before/after counters (E3, E4) | Editing | the client-thought-piece |
| 37 | Transition catalog | 16–20 connective moves with placement rules (E3) | Editing | the client-thought-piece; li-exec 08 |
| 38 | Review architecture | Sweep → self edit → adversarial → adjudicate → verify → subtract last → knock-on → note (E4) | Editing | the client-thought-piece; li-exec-review |
| 39 | Corpus registry | Spent lines and owned anchors appended at every delivery (E3) | Editing | the client-thought-piece; li-exec |
| 40 | Voice precedence | Red lines → author voice → anti-slop → house voice → platform (E3) | Editing | li-exec 05 |
| 41 | Seeds-win rule | Thesis and phrases survive; your prose is the spine (E3) | Editing | the client-thought-piece |
| 42 | Copy-gate runner | `run.py`, 26 checks, spec per check, eval baseline (E5) | Compliance | client-product-harness harness/ |
| 43 | LinkedIn gate script | `li_gates.py` 31 gates, METRICS, waivers, selftest fixtures (E5) | Editing | li-exec suite |
| 44 | Register lint | `lint.py` 26 regexes for the client terminology and tells (E5) | Compliance | the client-data |
| 45 | Brand-check verdict engine | PASS / FIX / BLOCK with jurisdiction, channel, citation, evidence gate (E6) | Compliance | brand-check skills |
| 46 | Five gates and the a legal reviewer set | Terminology, exposure, number, naming, narrative; four-file legal layer (E7) | Compliance | client-product-harness index and assets/copy |
| 47 | Legal-review triggers and routing | Six triggers; Aymeric → a legal reviewer; David Garcia Rios for a protocol body (E7) | Compliance | Brain legal.md; memory |
| 48 | review standard | Would a reviewer stand behind every sentence read aloud to an allocator (E1) | Compliance | 5-pass Pass 5 |
| 49 | Verb test and layer test | Who is the subject acting for; is Layer 2 reachable (E6) | Compliance | brand-check |
| 50 | Eight objections check | Before failing a bold-but-true claim (E6) | Compliance | legal-reasoning concept |
| 51 | Rate-comms snippet method | Causal chain from Atlas, approved blocks only, annotate every claim (E7) | Compliance | rate-comms skill |
| 52 | Thought-piece compliance patterns | AI-agent three facts; absolute claims; disparagement adjacency; gate-assumption log (E3) | Compliance | the client-thought-piece |
| 53 | Live-data two-step | API → traps → reconcile → as-of; literal deferral line on failure (E8) | Corroboration | live-data; qa-retrieval.md |
| 54 | Parsing traps | 17 traps in three tiers before believing a value (E8) | Corroboration | live-data parsing-and-traps.md |
| 55 | Validation ladder | L1 identities → L2 two routes → L3 on-chain → L4 register → L5 dashboard (E8) | Corroboration | the client-data validation.md |
| 56 | Report figure-check | Correction / Rounding / Ruling needed / Not in BA data with owners (E8) | Corroboration | Drive sheet |
| 57 | Disagreement rule | Report all values and which was used; fix the mapping, never the number (E8) | Corroboration | the client-data known-issues.md |
| 58 | Feedback triage A/B/C/D | Framing, compliance, length, factual → distinct responses (E9) | Editing | client-product-harness:blog |
| 59 | Storytelling and AI discipline | Read-aloud test, filler vs story, don't write why you don't know (E10) | Editing | Drive concept |
| 60 | Ryan Law editing hierarchy | Strategic → 30% structural → 90% line; title sprint (E11) | Editing | edit-this skill |
| 61 | Docs-corpus audit | 18-item per-page checklist, categories A–G, add and link (E12) | Editing | docs-corpus skill |
| 62 | Docs PR submission | Branch per section, five-section PR body, diff re-review (E12) | Editing | docs-corpus pr-submission.md |
| 63 | Format packs | 17 content types B1–B17 with anatomies and eight production gates | Editing | river-harness copy-review formats/ |
| 64 | Case-study consent tree | Named / anonymized / methodology study / illustrative walkthrough | Editing | river-harness case-study pack |
| 65 | Six AI primitives | Prompt, Skill, Memory, Project, Connector, Agent/Workflow (H1) | Agentic | the client product 2026 Playbook |
| 66 | OKF brain architecture | Four rules, domains, typed frontmatter, routing table, MANIFEST (H2) | Agentic | a client and client-product harness; Drive brains |
| 67 | Two Brains, Two Brands | Hermetic brands; no shared artifact (H2) | Agentic | the client (All) README |
| 68 | Source-of-truth hierarchy | Approver → playbook → legal set → blueprint → concepts by tier → feeds (H2) | Agentic | index.md; HOW-TO |
| 69 | Ingest protocol | Preserve → extract → classify → diff → propose → report; intake routing table (H3) | Agentic | ingest skills; brain ingest.md |
| 70 | Confidence tiers | conversation → operator\_reported → reference → confirmed with promotion rules (H4) | Agentic | confidence.md |
| 71 | Review-proposals ritual | Identity first; approve / edit / reject / defer; cascade shown; log (H3) | Agentic | review-proposals skills |
| 72 | Testing mode | Command lexicon; three-pass route(); confidence by speaker; TestLog gap report (H3) | Agentic | testing-mode skills |
| 73 | the client Brain session logging | Eight tracked categories, nine-section log, reliability verdict (H3) | Agentic | the client-brain-testing-mode |
| 74 | Retro compounding loop | Catch → Adjudicate → Consume → Guard; cluster by failure mode; eval delta (H3) | Agentic | retro skills |
| 75 | RACI and approver rules | One A per workflow; C is a gate; attribution is not routing (H4) | Agentic | people/index.md |
| 76 | Skill anatomy and standard | Router SKILL.md, references, scripts, templates, samples; section order (H5) | Agentic | harness/skill-standard.md |
| 77 | SkillSpec template | spec → build-ready → built with required reads, gates, output contract (H5) | Agentic | harness/skill-specs/\_template.md |
| 78 | Capability-authoring protocol | Do or know about? Spec, approve, build, register, compound (H6) | Agentic | a client capability-authoring routine |
| 79 | Routine as process, skill as executor | Change the process in the routine, the automation in the spec (H5) | Agentic | a client harness |
| 80 | Linters and CI | okf-lint, harness-lint, lint workflow, weekly brain-health digest (H7) | Agentic | Harness repos |
| 81 | Eval fixtures | Typed non-canon fixtures with recorded baseline; every failure becomes one (H7) | Agentic | harness/evals |
| 82 | Headless contracts | Fixed terminal lines; never rule, never edit canon (H7) | Agentic | harness/automation.md |
| 83 | DataFeed contracts | Store the fetch contract, never the number; Product → Metric map (H8) | Agentic | live-data; feeds/\_contract.md |
| 84 | Setup and profile skills | Engagement files captured verbatim that downstream skills read (H9) | Agentic | li-exec-setup; voice profiles |
| 85 | Reproducibility kit | doctor, selftest, record/replay, provenance JSON, exit codes (H10) | Agentic | the client-data; youtube-research; design-asset |
| 86 | Brain MCP spec | Six tools; server never writes to main (H11) | Agentic | harness/mcp-spec.md |
| 87 | Roadmap pattern | FUTURE-DEPLOYMENTS sequence from skills to MCP to feeds to testing mode (H11) | Agentic | a client brain |
| 88 | Brain maintenance | Pre-flight audit, versioned backup, staging, post-flight, recovery (T3) | Agentic | Drive brain-maintenance.md |
| 89 | Plugin versioning | Skills change bumps minor; contract break major; canon-only none (H7) | Agentic | a client README |
| 90 | Harness needs list | Capability wishlist per brand as the backlog (H11) | Agentic | Drive: the client product Harness Needs |
| 91 | Personal tool route | Claude Code on laptop; native APK sideloaded; never published (H12) | Agentic | Memory |
| 92 | One-page six-question brief | What / Why / Who / When / Where / How as a `.docx` (P1) | Team | project-brief-skill; brain protocol |
| 93 | Brief Creation SOP | Trigger → gather → draft → approve → visual → client sign-off (P1) | Team | Notion SOP |
| 94 | Three things per project | Brief, Notion plan, Slack thread; one thread = one project (P1) | Team | the client product Playbook; AM PM SOP |
| 95 | Client project page and tracker | BRIEF / LINKS / TASKS; status pipeline; workstream tags (P1) | Team | Notion trackers |
| 96 | Content approval chain | Brief → Draft → Review → Legal → Approve → Publish → Log; a reviewer quote chain (P2) | Team | approval-chains.md |
| 97 | PR Monday rhythm and FUD protocol | Weekly topic cadence; alert → approve → execute (P2) | Team | approval-chains.md |
| 98 | Content Management DB and page template | Status pipeline, pillars, channels, COPY #n callouts (P2) | Team | Notion portal |
| 99 | Blog lifecycle and format protocols | 20 stages, two gates, SLAs; explainer / campaign-tied / co-marketing (P2) | Team | client-product-harness:blog |
| 100 | Published-blog register | Differentiation check against prior posts (P2) | Team | assets/copy/published-blog-register |
| 101 | GTM launch playbook | T−2 weeks → T+30 days; eleven rules; amplification stack (P3) | Team | gtm-launch skill |
| 102 | Influencer brief template | Talking points, can/cannot words, IS/IS-NOT, per-creator UTM (P3) | Team | gtm-launch templates |
| 103 | Launch retro | Day-9 baseline; five-section T+30 report; repeat / change / stop (P3) | Team | gtm-launch checklists |
| 104 | Report skill | OKR-first, confirmed decisions, feeds only, no projections (P4) | Reporting | report skill |
| 105 | Top Metrics SOP | 3–5 metrics per channel; table, paragraph, action per metric; by the 7th (P4) | Reporting | Drive SOP |
| 106 | ICP Follower Log | Date, handle, type, source event, follow-up, owner; spike audit (P4) | Reporting | Top Metrics SOP |
| 107 | PR campaign wrap playbook | Five steps, fixed template, 11-item checklist (P4) | Reporting | Notion (Kim) |
| 108 | Report outline pattern | Decisions → goals → narratives → stakeholder filters → messages (P4) | Reporting | Drive: August Report Outline |
| 109 | Quarterly report cycle | Apps Script metrics sheet, figure check, reviewer comments, Insights Call (P4) | Reporting | Drive; memory |
| 110 | presentation-i3 | JSON spec, five arcs, 17 layouts, writing rules, design system (P5) | Team | presentation-i3 skill |
| 111 | Case study format and questionnaire | a service agent slot format; 7-question questionnaire; one-slide canvas (P6) | Team | Drive templates |
| 112 | Process standardization pipeline | Extract → synthesize → manifest → SOP v1 → v2 → review → playbook (P7) | Team | process-standardization plugin |
| 113 | Lossless interview extraction | 11 sections; 18-field process cards; Not stated never a guess (P7) | Team | interview-extraction |
| 114 | Standardization boundary map | STANDARDIZE / TEMPLATIZE / PRESERVE-VARIANT (P7) | Team | cross-interview-synthesis |
| 115 | 14-section SOP template | FACT / INFERENCE / RECOMMENDATION per step; evidence table (P7) | Team | sop-drafter |
| 116 | 12-section rollout playbook | From executive summary to maintenance policy; five-check QA (P7) | Team | playbook-assembler |
| 117 | Post-Mortem SOP | Five questions in fixed order (P8) | Team | Notion (a collaborator) |
| 118 | Weekly Focus log | Went well / didn't by focus (P8) | Team | Notion DB |
| 119 | Q4 Focuses tracker | One row per focus; Tuesday review; carried one-sentence issues (P8) | Personal | Notion: Q4 Focuses |
| 120 | Three-Sentence Framework | Problem → Root Cause → Solution with coaching path (P8) | Team | three-sentence-framework skill |
| 121 | OOO handover template | Replacement, per-client tasks with owners, watch-outs, links (P8) | Team | Notion |
| 122 | the author dashboard | Focuses, Q4 tracker, tasks, weekly log, projects (P8) | Personal | Notion |
| 123 | To-do conventions | Priority and status vocabularies; done separate (P8) | Personal | todo skill |
| 124 | Executive LinkedIn programme | Setup → ideas → write → review → report with engagement files (P9) | Client | li-exec suite |
| 125 | Voice-capture call | 45–60 min, ten story-and-decision questions (P9) | Client | li-exec 02 |
| 126 | Idea tests and calendar rules | Earned, Arguable, Evidenced, Useful, On-territory; cadence budgets (P9) | Client | li-exec-ideas |
| 127 | Ghostwriting governance | Approvals by content type, disclosure, 48-hour fast track, account access (P9) | Client | li-exec 10 |
| 128 | Client funnel mapper | Miro flow with lanes, colour code, drop-offs and fixes (P10) | Client | client-funnel-mapper |
| 129 | Email audit and pre-call bank | Streams, full copy, nine look-fors; 20–30 grouped questions (P10) | Client | client-funnel-mapper |
| 130 | Design-asset slot filling | 11 templates; source line required; partner sign-off; reproducible command (P11) | Team | river-harness design-asset |
| 131 | Website-seo advisory loop | Site-read Map → Audit → Spec; six-section page audit; corrective before net-new (P11) | Team | river-harness website-seo |
| 132 | AEO surface router and extractability rules | Nine rules; surface templates; pre-publish, page-audit, quarterly checklists | Team | aeo-seo skill |
| 133 | Client portal structure | IODS log, agendas, content DB, creative requests, OKR tracker (P11) | Team | Notion portal |
| 134 | PostHog question method | Recipe → schema → existing insight → query → defects → six-part answer (A1) | Analytics | posthog-analytics |
| 135 | Eleven defects and seven rules | Applied before any number ships; cross-source doctrine (A2, A3) | Analytics | posthog-analytics methodology.md |
| 136 | Segments and decision frames | 13 cohorts, 7 wallet profiles; six frames; weekly, monthly, quarterly, per-launch (A4, A5) | Analytics | segments.md; decision-frames.md; cycle.md |
| 137 | Launch funnel readings | Signal over impressions; 50% web-to-app constant; day-9 baseline (A6) | Analytics | gtm-launch 03-measurement |
| 138 | the client-data command grammar | Question shape → command; period grammar; prose answer shape (A7) | Analytics | the client-data |
| 139 | Strategic tracking pipeline and stack | Per-workflow flows, data sources, ideal tools (A9) | Analytics | Drive plan |
| 140 | SEO/AEO monitoring workbench | Apps Script, append-only log, duplicable per client (A9) | Analytics | Apps Script |
| 141 | docx build and verify workflow | Node build → pandoc verify → LibreOffice PDF → deliver (T1) | Tooling | Strategy Canvas project memory |
| 142 | Platform mechanics | Drive queries, markdown creation flags, Sheets tabs, Notion ids, Slack timestamps (T3) | Tooling | Project memories |

## Gaps and next steps for packaging

The sweep is complete on memory, the four skill suites, Notion and the five Drive brains; the main remaining work is consolidation, not discovery. Several sources were identified but not opened, and nine methods exist in two to four drifted copies that a package should reduce to one.

### Sources not reached in this pass

- Raw conversation transcripts are not replayable; memory covers roughly May to October 2026 and is densest from August onward. Anything you did before May 2026 that never became an artifact is not here.
- Drive, not opened: `[EXT] the client Strategy Foundations Blueprint` (91KB) and the `[EXT] the client Strategy Blueprint v2 [WIP]`; the the client Communications Playbook on the shared drive; brain protocols `live-data-fetching.md`, `confidence-tags.md`, `SHARED-INFRA-WRITE-GUARD-01.md`, `UNAUTHORIZED-CHANGE-ANALYSIS.md`, `atlas-forum-watcher.md`; `routines/experiments/`; the the client-money brain's `routines/` tree; the Analytics Migration Checklist sheet.
- Notion, not opened: the "the client ALL Issues, Opportunities, Discussions" and OKR tracker schemas; `[INT] i3 Core Capability Playbook Development` notes; your v1 PR dashboard and methodology doc (June 2026); the AEO prompt-analysis methodology write-up for a collaborator; the "Client Brain" all-hands deck (its Notion page body is blank, the Google Slides deck exists).
- Methods mentioned in memory without a written artifact found: the sample-token trademark evidence workbook approach; the Moody's response approval chain (Raul → leadership → ALCO → a legal reviewer via David); the finance fluency curriculum itself; the the client product performance dashboard's data flows; the the client design-system token extraction.

### Duplicates to consolidate before packaging

| Method | Copies found | Drift to resolve |
| --- | --- | --- |
| 5-Pass Copywriting | Drive protocol folder; client-product copy-review; a client copy-review (7-pass engine); blog (adds craft pass 8a) | One canonical routine, versioned, with brand overlays for sources and gates |
| Craft layer | the client-thought-piece (inline); blog craft.md; a client craft.md; li-exec 07 and 08 | One craft standard; thought-piece keeps your voice profile as an overlay |
| Testing mode | client-product; a client; the client-brain-testing-mode | Two log schemas (TestLog gap report vs nine-section session log); merge into one with the gap-to-fix table |
| Retro | client-product (eval delta diff) vs a client (cluster by failure mode) | One routine producing both outputs |
| Gate scripts | `run.py` 26 checks; `li_gates.py` 31; `lint.py` 26 | Shared core (em dash, AI connectives, hashtags, placeholders, register) plus per-brand extensions |
| Brief | project-brief-skill (6Q); Task Brief Template (Mar 2026); \[EXT\] the client Brief Template (Apr 2026) | Mark the two older formats retired; keep the \[EXT\] contacts table if still used |
| li-exec references | Byte-identical copies of 11 reference files across six skills | One shared reference bundle or a plugin with shared `references/` |
| Data skills | the client-observatory-api superseded by the client-data | Archive the old skill; keep its nine traps where the client-data does not restate them |
| Confidence vocabularies | Brain tiers; `[Sourced]/[Inferred]/[Gap]`; FACT/INFERENCE/RECOMMENDATION; High/Medium/Low/Folklore; ok/partial/stale | One mapping table in the preamble so every artifact declares which scale it uses |

### A package shape that fits what you have

- **Layer 0, Preamble:** the fifteen operating principles (section 1) and the confidence mapping table, written in the CLAUDE.md register (operating contract, no canon).
- **Layer 1, Core methods (brand-agnostic):** 5-pass and brief-making; craft and the review architecture; the brand-check verdict engine; live-data discipline and the validation ladder; the PostHog question method; the harness governance core (ingest, review, testing mode, retro) with the skill standard and capability-authoring protocol; process standardization; the Strategy Canvas and the research instruments (intelligence cards, ICP search instrument, prompt-universe loop, YouTube research, research-for-persuasion).
- **Layer 2, Brand overlays:** the client, the client product and the client each as canon, gates, approvers, terminology, format packs and templates. The sibling harnesses already prove the split works.
- **Layer 3, Team SOPs (Notion):** brief creation, project management, post-mortem, metrics reporting, OOO handover, trackers, the portal structure.
- **Format:** each method as `SKILL.md` plus `references/`, `scripts/`, `templates/` and spent `samples/`, per your stated requirement; the method index (section 10) becomes the package manifest; each rule keeps its incident-of-origin note so the reasoning stays checkable.

### Decisions only you can make

- Canonical home for the package: a plugin repo (the harness pattern), the Drive brains, or Notion's Strategy Toolkit and SOPs shelf.
- Which third-party methods ship inside it and how they are credited (Ryan Law's edit-this, no-ai-slop, ce-noslop, a collaborator's Post-Mortem SOP, Kim's PR playbook).
- Whether personal practices (Q4 tracker, the author dashboard, Android tools, the finance curriculum) belong in a team package or stay in a personal appendix.

### Next steps

- [ ] Decide the package home and confirm the four-layer shape
- [ ] Consolidate the nine duplicate rows above into single canonical versions
- [ ] Write the confidence-vocabulary mapping table for the preamble
- [ ] Open the unread sources listed above and fold any new methods into sections 2–9 and the index
- [ ] Write the two SOPs your Q4 key results already name: the metrics one-pager and the report process that "spins up in under a day"
- [ ] Turn the method index into the package manifest with a status column (canonical / overlay / retired)
