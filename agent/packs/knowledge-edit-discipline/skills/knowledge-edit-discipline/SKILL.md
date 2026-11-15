---
name: knowledge-edit-discipline
description: Governs edits to shared knowledge files. Audit before writing, never overwrite unread, archive before replacing, verify after writing, and recover by name when verification fails. The method holds no instance facts; each knowledge base supplies its own paths and indexes.
argument-hint: "[the knowledge file to change and why]"
version: 0.1.0
metadata:
  harness:
    lane: L5
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D2, mode: E3, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Knowledge edit discipline

## Purpose
A blind overwrite destroys work you cannot see. Every edit to a shared knowledge file proves the destination was understood before the write and verified after it.

## Method and data separation
This skill names no instance paths, folders, or index files. Each knowledge base supplies its own destinations, routing index, and retrieval index. The discipline is identical for any instance.

## Step 0
State the destination file, the reason for the change, and the approval route that covers it. If any of the three is missing, stop.

## Procedure by slot
1. Strategize: name the exact file and the change in one sentence.
2. Suspect: audit the destination first. Never assume a folder or file exists; list it.
3. Anticipate: read the existing file in full before any overwrite. Where existing content is stronger, keep it and merge rather than replace.
4. Act (archive): take a versioned dated archive copy of the current file before writing.
5. React (write): make the change. One declared change, not a sweep.
6. Recognize (verify): re-read the written file and confirm the change landed and nothing else moved. On failed verification: stop, restore from the archive copy, and report. Never retry blindly.
7. Act (indexes): update the routing index and refresh the retrieval index, each with a dated source tag.
8. Calculate: log the edit: file, reason, archive copy location, verification result. Two repeats of the same correction make a rule.

## Output contract
An edit note in the eval's format: destination and reason headers, an Audit section, an Archive section, a Change section, a Verify section, and an Indexes section.

## Delivery contract
Report the edit note to the owner of the knowledge base. A failed verification is reported, not retried silently.

## Quality gates
`python3 evals/run.py knowledge-edit-discipline`. Clean means the discipline is visible in the note, not that the edit was right.

## References
