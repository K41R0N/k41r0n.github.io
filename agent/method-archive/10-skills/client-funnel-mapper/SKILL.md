---
name: client-funnel-mapper
description: Map a client's marketing and acquisition funnel as a clear left-to-right flow on a Miro board (arrows, one lane per channel, owners, drop-offs, recommendations), plus separate funnels for each campaign, an email audit, a channel-by-week campaign sequence, pre-call questions and a take-over scope. Use this whenever someone asks to map, audit, draw, rebuild or improve a client's funnel, user journey, signup flow, lead flow, email funnel, onboarding flow or campaign funnel, or wants to work out "who takes over what" between an agency and a client, even if they don't say the word "funnel". Works for any client, not only one account.
---

# Client Funnel Mapper

Build funnel maps that a client can read in one pass: people move left to right along arrows, each step says who runs it, and the weak points and recommendations sit directly under the steps they affect. The map then becomes the basis for scoping what the agency takes over.

The structure below came out of a real engagement where the client asked the agency to take over their email funnel. The user rejected a grid layout ("I want arrows showing how people convert from one stage to the other and what the steps are") and approved the flow layout described here. Keep to it unless the user asks otherwise.

## Workflow

Work through these in order. Show the user the board after each major build and let them correct it before moving on; they know the client's reality better than any document.

### 1. Gather context before asking anything

Search, in this order, and only ask the user about what you still can't find:
- Project knowledge and past chats for the client (funnel, campaigns, tiers, tools, contacts).
- Call transcripts or notes the user attached, and any Slack threads they link.
- Client briefs, campaign pages or dashboards they link (fetch them).
- The user's own inbox, if they signed up to the client's product (see step 5).

Record where each fact came from. When a fact comes from a prototype, a plan or one person's comment, label it as such, because the user may know it has changed. (Example: a prototype said points were airdropped at signup; in reality users earned them by completing quests. The user caught it.)

### 2. Pin down the funnel's goal for this period

Ask or confirm what the funnel is meant to do right now, for example "free signups and activation until Black Friday, paid conversion only at Black Friday". This changes every recommendation: if the goal is signups, never recommend upgrade pushes before the conversion moment, and frame drop-offs around activation, not missing upsells. Put the goal in the subtitle of every funnel frame.

### 3. Split always-on from campaigns

- One **always-on funnel** for the steady-state journey.
- One **separate funnel per campaign** that has its own hook, entry rules or conversion moment (a competition, a launch, a sale).
- In the always-on funnel, keep a single generic step, "Current campaign page: whatever campaign is running", that links to the campaign funnel frame, instead of listing campaign details twice. The user explicitly removed duplicated campaign details.

### 4. Build the always-on funnel

Read `references/funnel-structure.md` for the stage columns, colour code, rows and wording rules, and `references/miro-build.md` for how to draw it with the Miro tools. The essentials:

- Stages as columns: Channels → How we move people → Where we send them → Sign up → Account → Activate → Nurture → Convert → Retain. Rename or drop stages to fit the client, but keep the left-to-right order.
- **Every channel gets its own lane**, with its own specific mechanisms (for example, X: CTA in posts, keyword-reply auto DM, banner offering a report; Instagram: link in bio, comment-to-DM). Don't lump channels together.
- Mark **amplifier channels** (a founder who only reposts, analysts or partners sharing) with an "amplify" label on their arrow, and say what they don't do.
- Discovery channels are top of funnel. Events, festivals and campaigns are **destinations** that channels send people to; they are not channels.
- A channel with no path to signup is shown as a pink drop-off node with a green fix node beside it.
- Put conversion numbers on arrows only when sourced ("about 6%", "about 30 a day").
- Two rows under the flow: **Where people drop off** (pink, evidence-based) and **Agency audit** (take over, recommend changes, hold until [date], after [date]).

### 5. Audit the emails

If the user signed up to the client's product, audit their inbox; see `references/email-audit.md`. Put the full copy and CTAs in a Google Doc (email copy is too long for a board) and link it from the Nurture step on the board. Update the funnel's email steps with what the audit found (streams, cadence, which lists really get what).

### 6. Build each campaign funnel

Same visual language, with campaign-specific stages. Include:
- The campaign's own channel list (confirm it with the user; it's often different from always-on).
- **A teaser or pre-launch phase** if the campaign is announced before it opens. Use it to get people through entry gates early (sign up and activate before day one, join a ready list).
- Eligibility splits as a decision diamond (no account / free / paid).
- The recurring engagement loop (for example weekly results that become content and feed back into step 1).
- A path for people who watch but don't participate.
- The single conversion moment.
- Drop-off and "What [agency] adds" rows.

### 7. Propose the campaign sequence

A separate frame with two native Miro tables:
- **By channel, week by week:** rows are weeks with their moment (tease, reveal, get ready, open, weekly results, final week, winners), columns are the campaign's channels.
- **Email sequence:** date, send type (block inside an existing send vs dedicated), audience segment, subject line idea, job, CTA. Prefer blocks inside existing sends so subscribers aren't flooded, keep dedicated sends for the two or three biggest moments, and respect any quiet dates in the client's brief.

Apply the client's brand and compliance rules to every line (for example no return promises, founder content needs sign-off).

### 8. Keep proposals off the client board when asked

Improvement plans, pricing thinking and internal pitch material often need to come off the board before it's shown to the client. When the user asks, copy the content word for word into a Google Doc, add notes on where it goes back, save a memory pointing to the doc, and offer to delete the frames (only delete after they say yes).

### 9. Scope and pre-call questions

When the user needs to agree scope with the client, produce:
- A **take-over scope** as a bullet list grouped by area (email, landing pages and conversion, lead magnets, top of funnel, measurement), then what stays with the client, then the access needed. Base it on what the client originally asked for, not on everything that could be done.
- A **pre-call question list** the client can prepare answers for, grouped so different client people can each take a section. Use `references/question-bank.md`, drop what's already answered, and replace generic wording with the specific facts you found. Offer a warm and a concise intro line.

## Rules that apply throughout

- **Don't invent.** Anything unconfirmed is grey and dashed, labelled "to confirm", or phrased as a question for the client.
- **Respect the user's edits.** If the board has changed since your last write (moved items, renamed legend, deleted text), keep their layout and wording and work around it. Read before you write if positions come back different.
- **Never delete board items without a clear yes**, except items the user explicitly told you to remove.
- **Client-facing wording.** No internal commercial notes, no agency jargon, no "per the brief". Plain verbs, sentence case, no em dashes.
- **After each build, say what changed in a few bullets** and flag assumptions the user should check. Don't re-describe the whole board; they can see it.

## Reference files

- `references/funnel-structure.md`: stage columns, colour code, row types, node wording, layout coordinates. Read before building any funnel.
- `references/miro-build.md`: Miro tool workflow, SVG patterns, update gotchas. Read before any Miro call.
- `references/email-audit.md`: how to audit a client's emails from an inbox and what to put in the doc.
- `references/question-bank.md`: pre-call questions by area.
