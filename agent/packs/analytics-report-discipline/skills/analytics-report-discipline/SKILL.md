---
name: analytics-report-discipline
description: Assembles a metrics report with the discipline the source methods document. Detect the step before searching for a cause, type the period, keep figures apart from interpretation and ranked actions, label every threshold flag as a hypothesis, carry open decisions with their stated defaults, close with corrections, and name uncaptured sources as standing gaps.
argument-hint: "[the report to assemble and the period it covers]"
version: 0.1.0
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Analytics report discipline

## Purpose
A report that blends figures with interpretation hides both. This method keeps each element in its place so the numbers stay clean, causes stay labeled, and the reader can see what is known, what is guessed, and what is still open.

## Method and data separation
This skill names no metrics, sources, thresholds, or periods. Each reporting context supplies its own measure definitions, sources, windows, and baselines. The discipline is identical for any dataset.

## Step 0
Name the report, the period, and whether the period is open or closed. An open period says so wherever its figures appear.

## Procedure by slot
1. Strategize: list the metrics in scope and their typed definitions (kind, source, window).
2. Suspect: for each series, detect mechanically where it actually stepped before asking why. Detection first, cause search second, and every cause carries its evidence artifact.
3. Anticipate: consult the mechanism table for the symptom class before choosing which evidence source to search first.
4. Act (assemble): keep three elements separate. Numbers, with source, as-of, and status. Interpretation, in its own section. Actions, ranked, in theirs.
5. React: every threshold breach is flagged with a one-line likely cause explicitly labeled as a hypothesis. Diagnosis without evidence is prohibited.
6. Recognize: check the open-decisions register. Any answer touching an open item surfaces it, with the competing options and the default currently in use.
7. Act (close): add the corrections section: what the previous version got wrong and the fix for each.
8. Calculate: name any authoritative source that is not captured as a standing gap, with the capture procedure and the rule that uncovered claims are checked by eye on the live surface.

## Output contract
A report note in the eval's format: report and window headers, a Period section, a Numbers section, an Interpretation section, an Actions section, a Thresholds section, an Open-decisions section, a Corrections section, and an Uncaptured section where applicable.

## Delivery contract
Figures stay clean of interpretation. A ranked action list never masquerades as a finding.

## Quality gates
`python3 evals/run.py analytics-report-discipline`. Clean means the separation and labels are visible in the note, not that the analysis is right. A companion terminology lint for number-quoting drafts is declared discipline in the source methods; it is not implemented here and no mechanical enforcement is claimed.

## References
