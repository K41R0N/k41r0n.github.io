---
name: consent-gated-instrumentation
description: Before enabling or changing analytics instrumentation that observes users, check the recorded permission state for that vendor's scope, keep each vendor's consent separate, and migrate prior consent records through a defined review path. Scoped to analytics instrumentation; it is not a product-wide consent system.
argument-hint: "[the instrumentation change and the vendors it touches]"
version: 0.1.0
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Consent-gated instrumentation

## Purpose
An analytics tag that observes users fires whether or not anyone checked consent. This method makes the permission check a named step with a recorded state, so one vendor's yes never silently covers another's.

## Scope and limits
Scoped to analytics instrumentation side effects: tags, SDKs, event capture, and their migration. This is the use case the source documents. It is not a product-wide consent gate, and it invents no new obligations; where the instance has its own consent rules, those rules govern. The eval checks the discipline note's structure only. It does not enforce runtime behavior, and this pack claims none.

## Method and data separation
This skill names no vendors, tools, or consent records. Each instance supplies its own vendor list, scopes, and the store where permission state is recorded.

## Step 0
Name the instrumentation change and every vendor it touches. If the instance's consent rules are unknown to you, stop and ask before any enable.

## Procedure by slot
1. Strategize: list the side effects that observe a user, per vendor.
2. Suspect: for each, name the consent scope it needs. One vendor's permission never implies another's.
3. Anticipate: read the recorded permission state for each scope. Missing record means not granted, never assumed.
4. Act (gate): enable only the side effects whose scope has a recorded grant. Everything else stays off and is listed as blocked, with the missing state named.
5. React: when migrating from a prior platform, route prior consent records through the defined review path before carrying them over; applicability to the new context is decided per record, not in bulk.
6. Recognize: record what was enabled, what stayed blocked, and the permission state each decision rested on.
7. Calculate: log the review so the next migration starts from recorded state, not memory.

## Output contract
A gate note in the eval's format: change header, a Scopes section (per vendor: scope and recorded state), a Decisions section (enabled or blocked, each with the state it rests on), and a Migration section when prior records are carried over.

## Delivery contract
Blocked items are reported with the missing permission state named. Nothing observing a user is enabled on an assumed state.

## Quality gates
`python3 evals/run.py consent-gated-instrumentation`. Clean means the gate note shows per-scope states and per-decision bases; it does not certify the underlying consent facts.

## References
