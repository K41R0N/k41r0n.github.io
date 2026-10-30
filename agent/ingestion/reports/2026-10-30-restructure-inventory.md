# Restructure inventory: agent/ onto Harness Standard v0.3 (2026-10-30)

Generated from `git diff-tree -M -r --name-status` plus sha256 comparison of every file before and after.

**Tally:** 354 files before, 355 after. 315 byte-identical moves (R100, sha256-verified). 34 files with path-reference edits only. 6 added, 5 deleted (see notes). Zero content lost.

| Before | After | Git status | Content |
|---|---|---|---|
|  | .gitignore | A | new file |
|  | CHARTER.md | A | new file |
|  | HOW-TO-USE-THIS-BRAIN.md | A | new file |
|  | MANIFEST.md | A | new file |
| ORIENTATION.md | index.md | R095 | path references only |
| README.md | README.md | M | path references only |
| automation/live-components-foundations.md | harness/specs/live-components-foundations.md | R097 | path references only |
| automation/narrative-auditor-spec.md | harness/specs/narrative-auditor-spec.md | R100 | byte-identical |
| guidelines/cms-safety.md | knowledge/site/cms-safety.md | R100 | byte-identical |
| guidelines/content-schemas.md | knowledge/site/content-schemas.md | R100 | byte-identical |
| guidelines/contribution-workflow.md | knowledge/site/contribution-workflow.md | R100 | byte-identical |
| guidelines/repo-architecture.md | knowledge/site/repo-architecture.md | R098 | path references only |
|  | knowledge/voice/README.md | A | new file |
|  | knowledge/voice/registers/README.md | A | new file |
| learnings.md | routines/learnings.md | R095 | path references only |
| methodologies/threadbot.md | knowledge/methodologies/threadbot.md | R094 | path references only |
| methodologies/ways-of-working-corpus.md | knowledge/methodologies/ways-of-working-corpus.md | R100 | byte-identical |
| methods-library/.gitignore |  | D | see notes |
| methods-library/AGENTS.md | packs/AGENTS.md | R100 | byte-identical |
| methods-library/CHARTER.md | packs/CHARTER.md | R100 | byte-identical |
| methods-library/CLAUDE.md | CLAUDE.md | R100 | byte-identical |
| methods-library/HOW-TO-USE-THIS-BRAIN.md | packs/HOW-TO-USE-THIS-BRAIN.md | R100 | byte-identical |
| methods-library/MANIFEST.md |  | D | see notes |
| methods-library/README.md | packs/README.md | R100 | byte-identical |
| methods-library/SENSITIVE-ROSTER.yaml | SENSITIVE-ROSTER.yaml | R100 | byte-identical |
| methods-library/decisions/goals.md | decisions/goals.md | R100 | byte-identical |
| methods-library/decisions/log.md | decisions/log.md | R100 | byte-identical |
| methods-library/decisions/open-loops.md | decisions/open-loops.md | R100 | byte-identical |
| methods-library/evals/contract.md | evals/contract.md | R100 | byte-identical |
| methods-library/evals/run.py | evals/run.py | R098 | path references only |
| methods-library/harness.yaml | harness.yaml | R100 | byte-identical |
| methods-library/index.md | packs/index.md | R100 | byte-identical |
| methods-library/knowledge/ethos/asker-lens.md | knowledge/ethos/asker-lens.md | R100 | byte-identical |
| methods-library/knowledge/ethos/ethos-candidates-day-job.md | knowledge/ethos/ethos-candidates-day-job.md | R100 | byte-identical |
| methods-library/knowledge/ethos/ethos-candidates.md | knowledge/ethos/ethos-candidates.md | R100 | byte-identical |
| methods-library/knowledge/ethos/ethos.md | knowledge/ethos/ethos.md | R100 | byte-identical |
| methods-library/knowledge/voice/chat-samples.md | knowledge/voice/chat-samples.md | R100 | byte-identical |
| methods-library/log.md | log.md | R100 | byte-identical |
| methods-library/packs/advice-answer/evals/checks.py | packs/advice-answer/evals/checks.py | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/approved-in-his-name.expect | packs/advice-answer/fixtures/approved-in-his-name.expect | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/approved-in-his-name.md | packs/advice-answer/fixtures/approved-in-his-name.md | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/good.expect | packs/advice-answer/fixtures/good.expect | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/good.md | packs/advice-answer/fixtures/good.md | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/in-his-name.expect | packs/advice-answer/fixtures/in-his-name.expect | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/in-his-name.md | packs/advice-answer/fixtures/in-his-name.md | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/jargon.expect | packs/advice-answer/fixtures/jargon.expect | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/jargon.md | packs/advice-answer/fixtures/jargon.md | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/missing-sections.expect | packs/advice-answer/fixtures/missing-sections.expect | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/missing-sections.md | packs/advice-answer/fixtures/missing-sections.md | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/number-no-source.expect | packs/advice-answer/fixtures/number-no-source.expect | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/number-no-source.md | packs/advice-answer/fixtures/number-no-source.md | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/risky-topic.expect | packs/advice-answer/fixtures/risky-topic.expect | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/risky-topic.md | packs/advice-answer/fixtures/risky-topic.md | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/sure-unchecked.expect | packs/advice-answer/fixtures/sure-unchecked.expect | R100 | byte-identical |
| methods-library/packs/advice-answer/fixtures/sure-unchecked.md | packs/advice-answer/fixtures/sure-unchecked.md | R100 | byte-identical |
| methods-library/packs/advice-answer/pack.yaml | packs/advice-answer/pack.yaml | R100 | byte-identical |
| methods-library/packs/advice-answer/skills/advice-answer/SKILL.md | packs/advice-answer/skills/advice-answer/SKILL.md | R100 | byte-identical |
| methods-library/packs/ai-coaching/evals/checks.py | packs/ai-coaching/evals/checks.py | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/bad-aid.expect | packs/ai-coaching/fixtures/bad-aid.expect | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/bad-aid.md | packs/ai-coaching/fixtures/bad-aid.md | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/bad-kind.expect | packs/ai-coaching/fixtures/bad-kind.expect | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/bad-kind.md | packs/ai-coaching/fixtures/bad-kind.md | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/good.expect | packs/ai-coaching/fixtures/good.expect | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/good.md | packs/ai-coaching/fixtures/good.md | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/no-asking.expect | packs/ai-coaching/fixtures/no-asking.expect | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/no-asking.md | packs/ai-coaching/fixtures/no-asking.md | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/no-theirs.expect | packs/ai-coaching/fixtures/no-theirs.expect | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/no-theirs.md | packs/ai-coaching/fixtures/no-theirs.md | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/task-no-setup.expect | packs/ai-coaching/fixtures/task-no-setup.expect | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/task-no-setup.md | packs/ai-coaching/fixtures/task-no-setup.md | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/two-steps.expect | packs/ai-coaching/fixtures/two-steps.expect | R100 | byte-identical |
| methods-library/packs/ai-coaching/fixtures/two-steps.md | packs/ai-coaching/fixtures/two-steps.md | R100 | byte-identical |
| methods-library/packs/ai-coaching/pack.yaml | packs/ai-coaching/pack.yaml | R100 | byte-identical |
| methods-library/packs/ai-coaching/skills/ai-coaching/SKILL.md | packs/ai-coaching/skills/ai-coaching/SKILL.md | R100 | byte-identical |
| methods-library/packs/asker-fit/evals/checks.py | packs/asker-fit/evals/checks.py | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/buzzword.expect | packs/asker-fit/fixtures/buzzword.expect | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/buzzword.md | packs/asker-fit/fixtures/buzzword.md | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/good.expect | packs/asker-fit/fixtures/good.expect | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/good.md | packs/asker-fit/fixtures/good.md | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/jargon.expect | packs/asker-fit/fixtures/jargon.expect | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/jargon.md | packs/asker-fit/fixtures/jargon.md | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/long-sentence.expect | packs/asker-fit/fixtures/long-sentence.expect | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/long-sentence.md | packs/asker-fit/fixtures/long-sentence.md | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/no-level.expect | packs/asker-fit/fixtures/no-level.expect | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/no-level.md | packs/asker-fit/fixtures/no-level.md | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/no-not-known.expect | packs/asker-fit/fixtures/no-not-known.expect | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/no-not-known.md | packs/asker-fit/fixtures/no-not-known.md | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/two-steps.expect | packs/asker-fit/fixtures/two-steps.expect | R100 | byte-identical |
| methods-library/packs/asker-fit/fixtures/two-steps.md | packs/asker-fit/fixtures/two-steps.md | R100 | byte-identical |
| methods-library/packs/asker-fit/pack.yaml | packs/asker-fit/pack.yaml | R100 | byte-identical |
| methods-library/packs/asker-fit/skills/asker-fit/SKILL.md | packs/asker-fit/skills/asker-fit/SKILL.md | R100 | byte-identical |
| methods-library/packs/attention-graduation/evals/checks.py | packs/attention-graduation/evals/checks.py | R100 | byte-identical |
| methods-library/packs/attention-graduation/fixtures/depth-overstated.expect | packs/attention-graduation/fixtures/depth-overstated.expect | R100 | byte-identical |
| methods-library/packs/attention-graduation/fixtures/depth-overstated.md | packs/attention-graduation/fixtures/depth-overstated.md | R100 | byte-identical |
| methods-library/packs/attention-graduation/fixtures/good-d2.expect | packs/attention-graduation/fixtures/good-d2.expect | R100 | byte-identical |
| methods-library/packs/attention-graduation/fixtures/good-d2.md | packs/attention-graduation/fixtures/good-d2.md | R100 | byte-identical |
| methods-library/packs/attention-graduation/fixtures/missing-slot.expect | packs/attention-graduation/fixtures/missing-slot.expect | R100 | byte-identical |
| methods-library/packs/attention-graduation/fixtures/missing-slot.md | packs/attention-graduation/fixtures/missing-slot.md | R100 | byte-identical |
| methods-library/packs/attention-graduation/fixtures/mode-too-low.expect | packs/attention-graduation/fixtures/mode-too-low.expect | R100 | byte-identical |
| methods-library/packs/attention-graduation/fixtures/mode-too-low.md | packs/attention-graduation/fixtures/mode-too-low.md | R100 | byte-identical |
| methods-library/packs/attention-graduation/fixtures/scripted-too-early.expect | packs/attention-graduation/fixtures/scripted-too-early.expect | R100 | byte-identical |
| methods-library/packs/attention-graduation/fixtures/scripted-too-early.md | packs/attention-graduation/fixtures/scripted-too-early.md | R100 | byte-identical |
| methods-library/packs/attention-graduation/pack.yaml | packs/attention-graduation/pack.yaml | R100 | byte-identical |
| methods-library/packs/attention-graduation/skills/attention-graduation/SKILL.md | packs/attention-graduation/skills/attention-graduation/SKILL.md | R100 | byte-identical |
| methods-library/packs/audience-listening/evals/checks.py | packs/audience-listening/evals/checks.py | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/claim-no-source.expect | packs/audience-listening/fixtures/claim-no-source.expect | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/claim-no-source.md | packs/audience-listening/fixtures/claim-no-source.md | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/engagement-no-read-time.expect | packs/audience-listening/fixtures/engagement-no-read-time.expect | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/engagement-no-read-time.md | packs/audience-listening/fixtures/engagement-no-read-time.md | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/good.expect | packs/audience-listening/fixtures/good.expect | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/good.md | packs/audience-listening/fixtures/good.md | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/hit-missing-who.expect | packs/audience-listening/fixtures/hit-missing-who.expect | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/hit-missing-who.md | packs/audience-listening/fixtures/hit-missing-who.md | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/no-not-verified.expect | packs/audience-listening/fixtures/no-not-verified.expect | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/no-not-verified.md | packs/audience-listening/fixtures/no-not-verified.md | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/no-skip.expect | packs/audience-listening/fixtures/no-skip.expect | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/no-skip.md | packs/audience-listening/fixtures/no-skip.md | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/social-no-primary.expect | packs/audience-listening/fixtures/social-no-primary.expect | R100 | byte-identical |
| methods-library/packs/audience-listening/fixtures/social-no-primary.md | packs/audience-listening/fixtures/social-no-primary.md | R100 | byte-identical |
| methods-library/packs/audience-listening/pack.yaml | packs/audience-listening/pack.yaml | R100 | byte-identical |
| methods-library/packs/audience-listening/skills/audience-listening/SKILL.md | packs/audience-listening/skills/audience-listening/SKILL.md | R100 | byte-identical |
| methods-library/packs/campaign-basics/evals/checks.py | packs/campaign-basics/evals/checks.py | R100 | byte-identical |
| methods-library/packs/campaign-basics/fixtures/good.expect | packs/campaign-basics/fixtures/good.expect | R100 | byte-identical |
| methods-library/packs/campaign-basics/fixtures/good.md | packs/campaign-basics/fixtures/good.md | R100 | byte-identical |
| methods-library/packs/campaign-basics/fixtures/jargon.expect | packs/campaign-basics/fixtures/jargon.expect | R100 | byte-identical |
| methods-library/packs/campaign-basics/fixtures/jargon.md | packs/campaign-basics/fixtures/jargon.md | R100 | byte-identical |
| methods-library/packs/campaign-basics/fixtures/no-date.expect | packs/campaign-basics/fixtures/no-date.expect | R100 | byte-identical |
| methods-library/packs/campaign-basics/fixtures/no-date.md | packs/campaign-basics/fixtures/no-date.md | R100 | byte-identical |
| methods-library/packs/campaign-basics/fixtures/no-not.expect | packs/campaign-basics/fixtures/no-not.expect | R100 | byte-identical |
| methods-library/packs/campaign-basics/fixtures/no-not.md | packs/campaign-basics/fixtures/no-not.md | R100 | byte-identical |
| methods-library/packs/campaign-basics/fixtures/two-jobs.expect | packs/campaign-basics/fixtures/two-jobs.expect | R100 | byte-identical |
| methods-library/packs/campaign-basics/fixtures/two-jobs.md | packs/campaign-basics/fixtures/two-jobs.md | R100 | byte-identical |
| methods-library/packs/campaign-basics/fixtures/two-things.expect | packs/campaign-basics/fixtures/two-things.expect | R100 | byte-identical |
| methods-library/packs/campaign-basics/fixtures/two-things.md | packs/campaign-basics/fixtures/two-things.md | R100 | byte-identical |
| methods-library/packs/campaign-basics/pack.yaml | packs/campaign-basics/pack.yaml | R100 | byte-identical |
| methods-library/packs/campaign-basics/skills/campaign-basics/SKILL.md | packs/campaign-basics/skills/campaign-basics/SKILL.md | R100 | byte-identical |
| methods-library/packs/clear-message/evals/checks.py | packs/clear-message/evals/checks.py | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/adjective.expect | packs/clear-message/fixtures/adjective.expect | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/adjective.md | packs/clear-message/fixtures/adjective.md | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/good.expect | packs/clear-message/fixtures/good.expect | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/good.md | packs/clear-message/fixtures/good.md | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/long-sentence.expect | packs/clear-message/fixtures/long-sentence.expect | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/long-sentence.md | packs/clear-message/fixtures/long-sentence.md | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/no-doubts.expect | packs/clear-message/fixtures/no-doubts.expect | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/no-doubts.md | packs/clear-message/fixtures/no-doubts.md | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/no-this-not-that.expect | packs/clear-message/fixtures/no-this-not-that.expect | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/no-this-not-that.md | packs/clear-message/fixtures/no-this-not-that.md | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/proof-no-source.expect | packs/clear-message/fixtures/proof-no-source.expect | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/proof-no-source.md | packs/clear-message/fixtures/proof-no-source.md | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/two-point-sentences.expect | packs/clear-message/fixtures/two-point-sentences.expect | R100 | byte-identical |
| methods-library/packs/clear-message/fixtures/two-point-sentences.md | packs/clear-message/fixtures/two-point-sentences.md | R100 | byte-identical |
| methods-library/packs/clear-message/pack.yaml | packs/clear-message/pack.yaml | R100 | byte-identical |
| methods-library/packs/clear-message/skills/clear-message/SKILL.md | packs/clear-message/skills/clear-message/SKILL.md | R100 | byte-identical |
| methods-library/packs/client-kickoff/evals/checks.py | packs/client-kickoff/evals/checks.py | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/agenda-gap.expect | packs/client-kickoff/fixtures/agenda-gap.expect | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/agenda-gap.md | packs/client-kickoff/fixtures/agenda-gap.md | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/good.expect | packs/client-kickoff/fixtures/good.expect | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/good.md | packs/client-kickoff/fixtures/good.md | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/no-access-preference.expect | packs/client-kickoff/fixtures/no-access-preference.expect | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/no-access-preference.md | packs/client-kickoff/fixtures/no-access-preference.md | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/no-success-question.expect | packs/client-kickoff/fixtures/no-success-question.expect | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/no-success-question.md | packs/client-kickoff/fixtures/no-success-question.md | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/no-summary.expect | packs/client-kickoff/fixtures/no-summary.expect | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/no-summary.md | packs/client-kickoff/fixtures/no-summary.md | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/publishes-early.expect | packs/client-kickoff/fixtures/publishes-early.expect | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/publishes-early.md | packs/client-kickoff/fixtures/publishes-early.md | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/two-approvers.expect | packs/client-kickoff/fixtures/two-approvers.expect | R100 | byte-identical |
| methods-library/packs/client-kickoff/fixtures/two-approvers.md | packs/client-kickoff/fixtures/two-approvers.md | R100 | byte-identical |
| methods-library/packs/client-kickoff/pack.yaml | packs/client-kickoff/pack.yaml | R100 | byte-identical |
| methods-library/packs/client-kickoff/skills/client-kickoff/SKILL.md | packs/client-kickoff/skills/client-kickoff/SKILL.md | R100 | byte-identical |
| methods-library/packs/copy-five-pass/evals/checks.py | packs/copy-five-pass/evals/checks.py | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/clean-internal.expect | packs/copy-five-pass/fixtures/clean-internal.expect | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/clean-internal.md | packs/copy-five-pass/fixtures/clean-internal.md | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/external-approved.expect | packs/copy-five-pass/fixtures/external-approved.expect | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/external-approved.md | packs/copy-five-pass/fixtures/external-approved.md | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/external-unapproved.expect | packs/copy-five-pass/fixtures/external-unapproved.expect | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/external-unapproved.md | packs/copy-five-pass/fixtures/external-unapproved.md | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/filler.expect | packs/copy-five-pass/fixtures/filler.expect | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/filler.md | packs/copy-five-pass/fixtures/filler.md | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/placeholder.expect | packs/copy-five-pass/fixtures/placeholder.expect | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/placeholder.md | packs/copy-five-pass/fixtures/placeholder.md | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/slop-superlative.expect | packs/copy-five-pass/fixtures/slop-superlative.expect | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/slop-superlative.md | packs/copy-five-pass/fixtures/slop-superlative.md | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/unsourced-number.expect | packs/copy-five-pass/fixtures/unsourced-number.expect | R100 | byte-identical |
| methods-library/packs/copy-five-pass/fixtures/unsourced-number.md | packs/copy-five-pass/fixtures/unsourced-number.md | R100 | byte-identical |
| methods-library/packs/copy-five-pass/pack.yaml | packs/copy-five-pass/pack.yaml | R100 | byte-identical |
| methods-library/packs/copy-five-pass/skills/copy-five-pass/SKILL.md | packs/copy-five-pass/skills/copy-five-pass/SKILL.md | R100 | byte-identical |
| methods-library/packs/discovery-interview/evals/checks.py | packs/discovery-interview/evals/checks.py | R100 | byte-identical |
| methods-library/packs/discovery-interview/fixtures/good.expect | packs/discovery-interview/fixtures/good.expect | R100 | byte-identical |
| methods-library/packs/discovery-interview/fixtures/good.md | packs/discovery-interview/fixtures/good.md | R100 | byte-identical |
| methods-library/packs/discovery-interview/fixtures/jargon.expect | packs/discovery-interview/fixtures/jargon.expect | R100 | byte-identical |
| methods-library/packs/discovery-interview/fixtures/jargon.md | packs/discovery-interview/fixtures/jargon.md | R100 | byte-identical |
| methods-library/packs/discovery-interview/fixtures/no-unread-line.expect | packs/discovery-interview/fixtures/no-unread-line.expect | R100 | byte-identical |
| methods-library/packs/discovery-interview/fixtures/no-unread-line.md | packs/discovery-interview/fixtures/no-unread-line.md | R100 | byte-identical |
| methods-library/packs/discovery-interview/fixtures/skips-ladder.expect | packs/discovery-interview/fixtures/skips-ladder.expect | R100 | byte-identical |
| methods-library/packs/discovery-interview/fixtures/skips-ladder.md | packs/discovery-interview/fixtures/skips-ladder.md | R100 | byte-identical |
| methods-library/packs/discovery-interview/fixtures/too-many.expect | packs/discovery-interview/fixtures/too-many.expect | R100 | byte-identical |
| methods-library/packs/discovery-interview/fixtures/too-many.md | packs/discovery-interview/fixtures/too-many.md | R100 | byte-identical |
| methods-library/packs/discovery-interview/pack.yaml | packs/discovery-interview/pack.yaml | R100 | byte-identical |
| methods-library/packs/discovery-interview/skills/discovery-interview/SKILL.md | packs/discovery-interview/skills/discovery-interview/SKILL.md | R100 | byte-identical |
| methods-library/packs/research-intake/evals/checks.py | packs/research-intake/evals/checks.py | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/contact-details.expect | packs/research-intake/fixtures/contact-details.expect | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/contact-details.md | packs/research-intake/fixtures/contact-details.md | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/dangling-id.expect | packs/research-intake/fixtures/dangling-id.expect | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/dangling-id.md | packs/research-intake/fixtures/dangling-id.md | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/entry-dropped.expect | packs/research-intake/fixtures/entry-dropped.expect | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/entry-dropped.md | packs/research-intake/fixtures/entry-dropped.md | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/entry-no-source.expect | packs/research-intake/fixtures/entry-no-source.expect | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/entry-no-source.md | packs/research-intake/fixtures/entry-no-source.md | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/good.expect | packs/research-intake/fixtures/good.expect | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/good.md | packs/research-intake/fixtures/good.md | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/no-topic.expect | packs/research-intake/fixtures/no-topic.expect | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/no-topic.md | packs/research-intake/fixtures/no-topic.md | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/no-unread-line.expect | packs/research-intake/fixtures/no-unread-line.expect | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/no-unread-line.md | packs/research-intake/fixtures/no-unread-line.md | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/output-published.expect | packs/research-intake/fixtures/output-published.expect | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/output-published.md | packs/research-intake/fixtures/output-published.md | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/thread-one-entry.expect | packs/research-intake/fixtures/thread-one-entry.expect | R100 | byte-identical |
| methods-library/packs/research-intake/fixtures/thread-one-entry.md | packs/research-intake/fixtures/thread-one-entry.md | R100 | byte-identical |
| methods-library/packs/research-intake/pack.yaml | packs/research-intake/pack.yaml | R100 | byte-identical |
| methods-library/packs/research-intake/skills/research-intake/SKILL.md | packs/research-intake/skills/research-intake/SKILL.md | R100 | byte-identical |
| methods-library/packs/strategy-canvas/evals/checks.py | packs/strategy-canvas/evals/checks.py | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/approved-no-approver.expect | packs/strategy-canvas/fixtures/approved-no-approver.expect | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/approved-no-approver.md | packs/strategy-canvas/fixtures/approved-no-approver.md | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/goal-no-result.expect | packs/strategy-canvas/fixtures/goal-no-result.expect | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/goal-no-result.md | packs/strategy-canvas/fixtures/goal-no-result.md | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/good.expect | packs/strategy-canvas/fixtures/good.expect | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/good.md | packs/strategy-canvas/fixtures/good.md | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/missing-module.expect | packs/strategy-canvas/fixtures/missing-module.expect | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/missing-module.md | packs/strategy-canvas/fixtures/missing-module.md | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/no-spokesperson.expect | packs/strategy-canvas/fixtures/no-spokesperson.expect | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/no-spokesperson.md | packs/strategy-canvas/fixtures/no-spokesperson.md | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/sourced-no-source.expect | packs/strategy-canvas/fixtures/sourced-no-source.expect | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/sourced-no-source.md | packs/strategy-canvas/fixtures/sourced-no-source.md | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/statement-incomplete.expect | packs/strategy-canvas/fixtures/statement-incomplete.expect | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/statement-incomplete.md | packs/strategy-canvas/fixtures/statement-incomplete.md | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/untagged-bullet.expect | packs/strategy-canvas/fixtures/untagged-bullet.expect | R100 | byte-identical |
| methods-library/packs/strategy-canvas/fixtures/untagged-bullet.md | packs/strategy-canvas/fixtures/untagged-bullet.md | R100 | byte-identical |
| methods-library/packs/strategy-canvas/pack.yaml | packs/strategy-canvas/pack.yaml | R100 | byte-identical |
| methods-library/packs/strategy-canvas/skills/strategy-canvas/SKILL.md | packs/strategy-canvas/skills/strategy-canvas/SKILL.md | R100 | byte-identical |
| methods-library/packs/verify-before-act/evals/checks.py | packs/verify-before-act/evals/checks.py | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/alarm-one-tool.expect | packs/verify-before-act/fixtures/alarm-one-tool.expect | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/alarm-one-tool.md | packs/verify-before-act/fixtures/alarm-one-tool.md | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/change-in-investigation.expect | packs/verify-before-act/fixtures/change-in-investigation.expect | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/change-in-investigation.md | packs/verify-before-act/fixtures/change-in-investigation.md | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/claim-no-check.expect | packs/verify-before-act/fixtures/claim-no-check.expect | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/claim-no-check.md | packs/verify-before-act/fixtures/claim-no-check.md | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/good.expect | packs/verify-before-act/fixtures/good.expect | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/good.md | packs/verify-before-act/fixtures/good.md | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/no-verify.expect | packs/verify-before-act/fixtures/no-verify.expect | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/no-verify.md | packs/verify-before-act/fixtures/no-verify.md | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/signal-unclassified.expect | packs/verify-before-act/fixtures/signal-unclassified.expect | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/signal-unclassified.md | packs/verify-before-act/fixtures/signal-unclassified.md | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/two-changes.expect | packs/verify-before-act/fixtures/two-changes.expect | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/two-changes.md | packs/verify-before-act/fixtures/two-changes.md | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/unverified-basis.expect | packs/verify-before-act/fixtures/unverified-basis.expect | R100 | byte-identical |
| methods-library/packs/verify-before-act/fixtures/unverified-basis.md | packs/verify-before-act/fixtures/unverified-basis.md | R100 | byte-identical |
| methods-library/packs/verify-before-act/pack.yaml | packs/verify-before-act/pack.yaml | R100 | byte-identical |
| methods-library/packs/verify-before-act/skills/verify-before-act/SKILL.md | packs/verify-before-act/skills/verify-before-act/SKILL.md | R100 | byte-identical |
| methods-library/schemas/tags.yaml | schemas/tags.yaml | R100 | byte-identical |
| methods-library/schemas/types.yaml | schemas/types.yaml | R100 | byte-identical |
| methods-library/scripts/local/denylist.example.txt | scripts/local/denylist.example.txt | R100 | byte-identical |
| methods-library/scripts/local/push_gate.sh | scripts/local/push_gate.sh | R091 | path references only |
| methods-library/scripts/local/test_push_gate.sh | scripts/local/test_push_gate.sh | R100 | byte-identical |
| methods-library/scripts/manifest.py | scripts/manifest.py | R096 | path references only |
| operating-agreement.md | AGENTS.md | R097 | path references only |
| protocols/PORTFOLIO-CONTENT-EDIT-01.md | routines/protocols/PORTFOLIO-CONTENT-EDIT-01.md | R092 | path references only |
| protocols/PORTFOLIO-WRITE-GUARD-01.md | routines/protocols/PORTFOLIO-WRITE-GUARD-01.md | R098 | path references only |
| site/ICP-BRIEF.md | knowledge/site/ICP-BRIEF.md | R100 | byte-identical |
| site/SECTION-MAP.md | knowledge/voice/site/SECTION-MAP.md | R100 | byte-identical |
| skills/README.md | skills/README.md | M | path references only |
| skills/add-blog-post.md | skills/add-blog-post/SKILL.md | R091 | path references only |
| skills/add-configurable-field.md | skills/add-configurable-field/SKILL.md | R095 | path references only |
| skills/add-thesis.md | skills/add-thesis/SKILL.md | R097 | path references only |
| skills/build-and-verify.md | skills/build-and-verify/SKILL.md | R100 | byte-identical |
| skills/edit-home-sections.md | skills/edit-home-sections/SKILL.md | R100 | byte-identical |
| skills/edit-site-settings.md | skills/edit-site-settings/SKILL.md | R096 | path references only |
| task-register.md | harness/task-register.md | R100 | byte-identical |
| voice/.gitignore |  | D | see notes |
| voice/HARNESS.md | knowledge/voice/HARNESS.md | R062 | path references only |
| voice/INTEGRATION-PROPOSAL.md | decisions/voice-findings/INTEGRATION-PROPOSAL.md | R100 | byte-identical |
| voice/README.md |  | D | see notes |
| voice/canon/do-dont.md | knowledge/voice/do-dont.md | R100 | byte-identical |
| voice/canon/lexicon.md | knowledge/voice/lexicon.md | R070 | path references only |
| voice/canon/voice-spec.md | knowledge/voice/voice-spec.md | R095 | path references only |
| voice/corpus/excluded/about.md | assets/voice-corpus/excluded/about.md | R100 | byte-identical |
| voice/corpus/excluded/pages__about.md | assets/voice-corpus/excluded/pages__about.md | R100 | byte-identical |
| voice/corpus/excluded/projects__interactive-quiz-maker.md | assets/voice-corpus/excluded/projects__interactive-quiz-maker.md | R100 | byte-identical |
| voice/corpus/excluded/projects__notion-as-cms.md | assets/voice-corpus/excluded/projects__notion-as-cms.md | R100 | byte-identical |
| voice/corpus/excluded/projects__notion-telegram-bot.md | assets/voice-corpus/excluded/projects__notion-telegram-bot.md | R100 | byte-identical |
| voice/corpus/excluded/projects__openclaw-personal-infrastructure.md | assets/voice-corpus/excluded/projects__openclaw-personal-infrastructure.md | R100 | byte-identical |
| voice/corpus/excluded/projects__opensource-curriculum.md | assets/voice-corpus/excluded/projects__opensource-curriculum.md | R100 | byte-identical |
| voice/corpus/excluded/projects__rm-quickshare-bot.md | assets/voice-corpus/excluded/projects__rm-quickshare-bot.md | R100 | byte-identical |
| voice/corpus/excluded/projects__threadbot.md | assets/voice-corpus/excluded/projects__threadbot.md | R100 | byte-identical |
| voice/corpus/excluded/projects__uh-vibe-checker.md | assets/voice-corpus/excluded/projects__uh-vibe-checker.md | R100 | byte-identical |
| voice/corpus/excluded/theses__better-discovery-engines.md | assets/voice-corpus/excluded/theses__better-discovery-engines.md | R100 | byte-identical |
| voice/corpus/excluded/theses__devices-as-co-creations.md | assets/voice-corpus/excluded/theses__devices-as-co-creations.md | R100 | byte-identical |
| voice/corpus/excluded/theses__future-belongs-to-storytellers.md | assets/voice-corpus/excluded/theses__future-belongs-to-storytellers.md | R100 | byte-identical |
| voice/corpus/holdout/2025-11-21-why-do-devs-get-so-much-free-sht.md | assets/voice-corpus/holdout/2025-11-21-why-do-devs-get-so-much-free-sht.md | R100 | byte-identical |
| voice/corpus/holdout/2025-12-31-hic-sunt-dracones.md | assets/voice-corpus/holdout/2025-12-31-hic-sunt-dracones.md | R100 | byte-identical |
| voice/corpus/raw/2025-06-04-why-im-building-things-that-dont.md | assets/voice-corpus/raw/2025-06-04-why-im-building-things-that-dont.md | R100 | byte-identical |
| voice/corpus/raw/2025-06-11-the-future-belongs-to-the-storytellers.md | assets/voice-corpus/raw/2025-06-11-the-future-belongs-to-the-storytellers.md | R100 | byte-identical |
| voice/corpus/raw/2025-06-17-were-not-getting-dumber.md | assets/voice-corpus/raw/2025-06-17-were-not-getting-dumber.md | R100 | byte-identical |
| voice/corpus/raw/2025-06-28-think-of-the-children.md | assets/voice-corpus/raw/2025-06-28-think-of-the-children.md | R100 | byte-identical |
| voice/corpus/raw/2025-07-12-the-myth-of-10x.md | assets/voice-corpus/raw/2025-07-12-the-myth-of-10x.md | R100 | byte-identical |
| voice/corpus/raw/2025-07-29-re-learning-to-trust-each-others.md | assets/voice-corpus/raw/2025-07-29-re-learning-to-trust-each-others.md | R100 | byte-identical |
| voice/corpus/raw/2025-08-21-techno-feudalistic-quixotes.md | assets/voice-corpus/raw/2025-08-21-techno-feudalistic-quixotes.md | R100 | byte-identical |
| voice/corpus/raw/2025-09-11-antitech.md | assets/voice-corpus/raw/2025-09-11-antitech.md | R100 | byte-identical |
| voice/corpus/raw/2026-09-20-shadow-work.md | assets/voice-corpus/raw/2026-09-20-shadow-work.md | R100 | byte-identical |
| voice/drafts/README.md | assets/voice-drafts/README.md | R100 | byte-identical |
| voice/findings/2026-10-28-01-voice-measurements.md | decisions/voice-findings/2026-10-28-01-voice-measurements.md | R100 | byte-identical |
| voice/findings/2026-10-28-02-essay-corpus-decision.md | decisions/voice-findings/2026-10-28-02-essay-corpus-decision.md | R100 | byte-identical |
| voice/findings/2026-10-28-03-icp-watchlist.md | decisions/voice-findings/2026-10-28-03-icp-watchlist.md | R100 | byte-identical |
| voice/findings/2026-10-28-04-posting-platforms.md | decisions/voice-findings/2026-10-28-04-posting-platforms.md | R100 | byte-identical |
| voice/findings/2026-10-28-05-threadbot-replica-steering.md | decisions/voice-findings/2026-10-28-05-threadbot-replica-steering.md | R100 | byte-identical |
| voice/findings/2026-10-28-06-standing-working-rules.md | decisions/voice-findings/2026-10-28-06-standing-working-rules.md | R100 | byte-identical |
| voice/findings/2026-10-28-07-open-items-awaiting-him.md | decisions/voice-findings/2026-10-28-07-open-items-awaiting-him.md | R100 | byte-identical |
| voice/findings/2026-10-28-08-sme-draft-v4-rejected.md | decisions/voice-findings/2026-10-28-08-sme-draft-v4-rejected.md | R100 | byte-identical |
| voice/findings/2026-10-28-09-texture-reread-and-counter-evidence.md | decisions/voice-findings/2026-10-28-09-texture-reread-and-counter-evidence.md | R100 | byte-identical |
| voice/findings/2026-10-28-10-v5-cycle-outcome-and-writing-paused.md | decisions/voice-findings/2026-10-28-10-v5-cycle-outcome-and-writing-paused.md | R100 | byte-identical |
| voice/findings/2026-10-28-11-chat-answers-as-voice-samples.md | decisions/voice-findings/2026-10-28-11-chat-answers-as-voice-samples.md | R100 | byte-identical |
| voice/findings/2026-10-28-12-his-mimicry-notes-read.md | decisions/voice-findings/2026-10-28-12-his-mimicry-notes-read.md | R100 | byte-identical |
| voice/findings/2026-10-29-13-writer-judge-pipeline-folded-in.md | decisions/voice-findings/2026-10-29-13-writer-judge-pipeline-folded-in.md | R100 | byte-identical |
| voice/findings/2026-10-29-operating-agreement.md | decisions/voice-findings/2026-10-29-operating-agreement.md | R100 | byte-identical |
| voice/findings/README.md | decisions/voice-findings/README.md | R100 | byte-identical |
| voice/log/compound.md | routines/voice-compound.md | R082 | path references only |
| voice/refs/README.md | knowledge/voice/refs/README.md | R100 | byte-identical |
| voice/refs/tooling.md | knowledge/voice/refs/tooling.md | R100 | byte-identical |
| voice/registers/README.md |  | D | see notes |
| voice/reports/delta.json | ingestion/reports/voice/reports/delta.json | R100 | byte-identical |
| voice/reports/range_loo.json | ingestion/reports/voice/reports/range_loo.json | R100 | byte-identical |
| voice/reports/rule_fp.json | ingestion/reports/voice/reports/rule_fp.json | R100 | byte-identical |
| voice/reports/verification.md | ingestion/reports/voice/reports/verification.md | R100 | byte-identical |
| voice/routines/blind-test.md | routines/blind-test.md | R084 | path references only |
| voice/routines/copy-draft.md | routines/copy-draft.md | R059 | path references only |
| voice/routines/copy-review.md | routines/copy-review.md | R085 | path references only |
| voice/routines/writer-judge-loop.md | routines/writer-judge-loop.md | R052 | path references only |
| voice/site/ICP-BRIEF.md | knowledge/voice/site/ICP-BRIEF.md | R100 | byte-identical |
| voice/site/SECTION-MAP.md | knowledge/site/SECTION-MAP.md | R097 | path references only |
| voice/thoughts/README.md | knowledge/voice/thoughts/README.md | R100 | byte-identical |
| voice/tools/ban_list.py | scripts/local/voice/ban_list.py | R095 | path references only |
| voice/tools/build_spec.py | scripts/local/voice/build_spec.py | R098 | path references only |
| voice/tools/checks.py | scripts/local/voice/checks.py | R100 | byte-identical |
| voice/tools/corpus_clean_check.py | scripts/local/voice/corpus_clean_check.py | R093 | path references only |
| voice/tools/edit_rate.py | scripts/local/voice/edit_rate.py | R100 | byte-identical |
| voice/tools/fixtures/piece1/SEAL.txt | scripts/local/voice/fixtures/piece1/SEAL.txt | R100 | byte-identical |
| voice/tools/fixtures/piece1/classes.md | scripts/local/voice/fixtures/piece1/classes.md | R100 | byte-identical |
| voice/tools/fixtures/piece1/draft.md | scripts/local/voice/fixtures/piece1/draft.md | R100 | byte-identical |
| voice/tools/fixtures/piece1/final.md | scripts/local/voice/fixtures/piece1/final.md | R100 | byte-identical |
| voice/tools/fixtures/piece1/ledger.md | scripts/local/voice/fixtures/piece1/ledger.md | R100 | byte-identical |
| voice/tools/fixtures/piece1/predictions.md | scripts/local/voice/fixtures/piece1/predictions.md | R100 | byte-identical |
| voice/tools/gen_spec_md.py | scripts/local/voice/gen_spec_md.py | R098 | path references only |
| voice/tools/holdout_guard.py | scripts/local/voice/holdout_guard.py | R095 | path references only |
| voice/tools/ledger.py | scripts/local/voice/ledger.py | R100 | byte-identical |
| voice/tools/placeholders.py | scripts/local/voice/placeholders.py | R100 | byte-identical |
| voice/tools/range_check.py | scripts/local/voice/range_check.py | R095 | path references only |
| voice/tools/spec_v0.json | scripts/local/voice/spec_v0.json | R100 | byte-identical |
| voice/tools/verify.py | scripts/local/voice/verify.py | R084 | path references only |
| voice/tools/vlib.py | scripts/local/voice/vlib.py | R100 | byte-identical |
| writing-runs.md | routines/writing-runs.md | R080 | path references only |

## Notes
- Deleted `methods-library/.gitignore` and `voice/.gitignore`: all 6 rules survive verbatim in the new root `.gitignore` (plus the standard's section 5.4 patterns).
- Deleted `methods-library/MANIFEST.md`: regenerated at root. The committed old manifest was STALE (pack hashes predated later pack edits) - regenerating against the old tree produces exactly the new file, proving pack bytes are untouched.
- `voice/README.md` -> `knowledge/voice/README.md` and `voice/registers/README.md` -> `knowledge/voice/registers/README.md` show as delete+add because path edits pushed similarity below git's rename threshold; both are moves with path-reference edits only.
- `voice/agent/site/ICP-BRIEF.md` and `voice/agent/site/SECTION-MAP.md` are byte-identical duplicates of the `site/` originals; preserved verbatim at `knowledge/voice/agent/site/` and flagged for his decision.
- The one prose-span change beyond pure path tokens: `knowledge/voice/HARNESS.md` location line ("Paths below are relative to this folder" -> "relative to `agent/`").
- Tooling fixes required by the moves: `scripts/manifest.py` and `evals/run.py` skip non-directories in `packs/` (the library's root docs live there now); `scripts/local/push_gate.sh` history exclusions extended to the pre-move paths of its own denylist files.
