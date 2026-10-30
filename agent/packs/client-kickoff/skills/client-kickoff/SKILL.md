---
name: client-kickoff
description: Plans a 60-minute client kickoff call and the first week after it.
argument-hint: "[client and services involved]"
version: 0.1.0
metadata:
  harness:
    lane: L3
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Client kickoff

## Purpose
Start a client engagement with decisions made, not assumed: who decides, what success means, and who gives access.

## Step 0
Say which services are in scope and what the client has already sent. Say what is unknown.

## When to use / not
Use for a new client or a new workstream. Not for a weekly call.

## Modes
One: plan, run, follow up.

## Procedure by slot
1. Strategize: before the call, send a questionnaire and audit the client's existing channels.
2. Suspect: for each service in scope, list what you need from them (brand assets, spokesperson and their calendar if PR is involved).
3. Anticipate: time-box the call to 60 minutes: introductions 10, contract and deliverables 5, how we work together 10, business goals 15, access 10, next steps 10.
4. Act: in "how we work together" name one point of contact, one person who approves, and one spokesperson if PR is involved. The goal is that you run the work within two weeks.
5. React: ask what outcomes in 90 days would make the partnership a success, and which KPIs matter for the next three months.
6. Recognize: ask whether access is delegated or full, and let the client choose.
7. Calculate: right after the call send a summary of next steps and timelines, a walk through of the shared folder and the open projects. Week one is audit and strategy, nothing publishes. Draft a first strategy from what you know and fill gaps on the strategy call, with the document shared 48 hours before it.

## Output contract
A plan in the eval's format.

## Delivery contract
Nothing goes to the client without his yes.

## Quality gates
`python3 evals/run.py client-kickoff`. Clean means the plan has the decisions in it, not that the call will go well.

## Compound step
Log what the client asked that the plan missed in routines/learnings.md.

## References
packs/client-kickoff/fixtures/, knowledge/ethos/ethos.md (items 28, 30)
