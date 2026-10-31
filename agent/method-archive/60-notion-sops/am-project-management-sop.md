---
title: "AM Project Management SOP"
source_url: https://app.notion.com/p/3639bfc98f9f81cb9118fc26fade1f50
notion_id: 3639bfc9-8f9f-81cb-9118-fc26fade1f50
fetched: 2026-10-30
type: page
path: "Personal Dashboards / i3 Personal Dashboards Database / Diana Badea"
page_last_edited_at: 2026-05-20T20:21:00.958Z
notes: "Lives under Diana Badea's personal dashboard. Inline discussion markers preserved as returned; comment threads not fetched."
---

# Properties (verbatim)

```json
{"title":"<p>\nAM Project Management SOP \n</p>"}
```

# Page content (verbatim Notion-flavored Markdown)

<quote color="purple_bg">
Standard operating procedure for how Account Managers project-manage client work end-to-end, starting from a locked, client-approved brief.
</quote>

<b>North star:</b> AMs should never edit Notion task-by-task and never chase teammates by hand. AMs run the brief, align the team, and supervise. Mario does the typing.

<b>Precondition:</b> you have a locked, client-approved brief sitting in the client's Google Drive <code>Projects</code> folder, plus a project thread already open in the client's <code>*-all-projects</code> Slack channel. If you don't, go run the [Brief Creation SOP](https://www.notion.so/3639bfc98f9f808bbfebcac94e41a160) first.

---

## Phase 1 — Create the Notion project

Goal: project lives in the client Project Tracker DB, with the brief and a draft task list. <b>Tasks are NOT in the To-Do DB yet.</b>

- [ ] AM — In the client's Notion Project Tracker DB, create a new project (auto-populates with the <span discussion-urls="discussion://3639bfc9-8f9f-81cb-9118-fc26fade1f50/63594f9f-821c-4229-ba7e-49cf2f097926/3659bfc9-8f9f-806e-9f20-001c268891d1">Standard Project Template</span>)
- [ ] AM — Fill in the project properties: Name, Status, Priority, Accountable AM, Start Date, Deadline, Project Type
- [ ] AM — Drop the <span discussion-urls="discussion://3639bfc9-8f9f-81cb-9118-fc26fade1f50/921ab4c3-8430-410c-a82f-dce71e3ca4b7/3659bfc9-8f9f-8043-a0f0-001c28c547b3">visual</span> brief into the project page
- [ ] AM — In the project page's <code>Details & timelines</code> section, outline every task you think the project needs. <b>Format each task as:</b>
  - [ ] <code>[task] — [accountable] — [due date]</code>
- [ ] AM — Goes to respective client's Claude Project
- [ ] AM — Asks Claude to transform all the listed tasks under <code>Details & timelines</code> in tasks in the "To do" database on the created page

---

## Phase 2 — Async team brainstorm (Slack)

Goal: everyone who'll work on the project has eyes on it before the kickoff call so the call is fast.

- [ ] AM — In the client's <code>*-all-projects</code> Slack channel, open the project thread and tag the full internal team for this project (tag the user group if one exists, otherwise tag people individually)
- [ ] AM — Post: project name + 1–2 sentence summary + link to Notion project page + link to visual brief
- [ ] All (internal team) — Read the brief. Drop ideas, missing tasks, and concerns into the thread
- [ ] AM — Monitor the thread and update the draft task list in Notion <code>Details & timelines</code> as new tasks/ideas land

---

## Phase 3 — Project kickoff call

Goal: leave the call with a final, agreed task list (task / owner / due date).

- [ ] AM — Schedule the kickoff call (or use an existing internal team meeting if timing fits)
- [ ] AM — Send calendar invite + agenda link to the internal team
- [ ] AM — On the call, walk through the brief and the draft task list
- [ ] All — Align on each task: confirm scope, confirm owner, confirm due date

<todo checked="false">
AM — Capture any new tasks or changes live in the Notion project page <code>Details & timelines</code> 
</todo>

---

## Phase 4 — Clean up + create tasks in the To-Do DB

Goal: the To-Do DB has accurate, owned, dated rows for every task.

- [ ] AM — After the kickoff call, pull the call transcript
- [ ] AM — Clean up the task list in the project page <code>Details & timelines</code> against the transcript — add tasks that came up live, remove tasks that got cut, fix owners and dates
- [ ] AM — Sanity-check the format. Each task must have: <b>Task name, Accountable, Due Date.</b> No exceptions
- [ ] AM — Open the project Slack thread, tag <b>Mario</b>, and ask him to create the tasks in the To-Do DB for this project

---

## Phase 5 — Day-to-day project management (DONE BY MARIO)

Goal: the project runs itself. AM supervises status; doesn't chase.

- [ ] Everyone — Complete assigned tasks. Mark <code>Done</code> in the To-Do DB when complete
- [ ] Everyone — Use your Personal Dashboard To-Do view to stay ahead of due dates (so AM / Mario doesn't have to chase you)
- [ ] Mario — Every day, posts a digest in each project Slack channel of any overdue tasks, @-mentioning the owners. Silent if nothing's overdue. De-duped so a task gets chased max 1x/day
- [ ] <span discussion-urls="discussion://3639bfc9-8f9f-81cb-9118-fc26fade1f50/1a8af350-438a-4bdd-b1e0-906420a4f15b/3659bfc9-8f9f-80af-89ad-001cbfe4f568">AM — Use the project Slack thread as the single source of truth. Tag Mario for ad-hoc updates</span> (note that Mario should be tagged for complex questions whose answer takes a bit more to be found out and not for simple information related to tasks that can be easily found in the project tracker. goal: not clog the chat)
  - [ ] <i><span discussion-urls="discussion://3639bfc9-8f9f-81cb-9118-fc26fade1f50/1d327eef-5581-4c29-b04d-2f71fb06cf6a/3659bfc9-8f9f-80af-89ad-001cbfe4f568">"Mario, what's the status of this project?"</span></i><span discussion-urls="discussion://3639bfc9-8f9f-81cb-9118-fc26fade1f50/1d327eef-5581-4c29-b04d-2f71fb06cf6a/3659bfc9-8f9f-80af-89ad-001cbfe4f568"> — Mario summarizes the project page</span>
  - [ ] <i><span discussion-urls="discussion://3639bfc9-8f9f-81cb-9118-fc26fade1f50/d671051c-d18b-49b5-b876-0d170decdf3a/3659bfc9-8f9f-80af-89ad-001cbfe4f568">"Mario, what did we agree on the IR call last Tuesday?"</span></i><span discussion-urls="discussion://3639bfc9-8f9f-81cb-9118-fc26fade1f50/d671051c-d18b-49b5-b876-0d170decdf3a/3659bfc9-8f9f-80af-89ad-001cbfe4f568"> — Mario searches the thread / channel history</span>
- [ ] AM — If a status changed offline (IRL call, Telegram, side conversation), tag Mario in the project thread and tell him — he updates Notion

---

## Phase 6 — Project close-out

- [ ] AM — When all tasks are <code>Done</code>, set project Status = <code>Complete</code> in the Notion project page
- [ ] AM — Post a wrap message in the project Slack thread: outcome vs. goal, key learnings, anything to roll into a case study
- [ ] <span discussion-urls="discussion://3639bfc9-8f9f-81cb-9118-fc26fade1f50/bdb87d57-3ef4-41af-b2e7-bb2ac8947368/3659bfc9-8f9f-80b4-b4a5-001ce618806d">AM — If the project warrants a post-mortem, run </span><span discussion-urls="discussion://3639bfc9-8f9f-81cb-9118-fc26fade1f50/bdb87d57-3ef4-41af-b2e7-bb2ac8947368/3659bfc9-8f9f-80b4-b4a5-001ce618806d"><code>Post Mortem</code></span><span discussion-urls="discussion://3639bfc9-8f9f-81cb-9118-fc26fade1f50/bdb87d57-3ef4-41af-b2e7-bb2ac8947368/3659bfc9-8f9f-80b4-b4a5-001ce618806d"> SOP</span>
- [ ] AM — Check if the project is worth of a case study. If so, run the Case Study SOP
- [ ] AM — Archive the project thread

---

## Done when — how we know it works

- AMs never chase a teammate for a task. Mario does it.
- Everyone uses their Personal Dashboard to stay ahead of their tasks.
- A new project goes from locked brief → kicked-off with a clean task list in the To-Do DB in ≤ 5 working days.

---

## Tooling map

| Tool | What it's for |
| --- | --- |
| Client Notion Project Tracker DB | Project page + <code>Details & timelines</code> task drafting |
| Client's Claude Project | Where the AM asks Claude to transform <code>Details & timelines</code> into rows in the To-Do DB |
| To-Do DB | Single source of truth for tasks. Written to <b>only</b> at end of Phase 4, by Mario / Claude |
| Client <code>*-all-projects</code> Slack channel | One thread per project. All project chatter lives here |
| Mario | Reads/writes Notion when tagged in the project Slack thread. Chases overdue tasks daily |
| Personal Dashboard | Per-AM Notion view: client list, To-Do, case studies, personal focuses |

---

## References

- [Brief Creation SOP](https://www.notion.so/3639bfc98f9f808bbfebcac94e41a160) — the SOP that feeds this one
- Raul's PRD: [Mario: your project management quant](https://www.notion.so/3599bfc98f9f809ba016c222ae3cbe84)
- Standard Project Template: [the client x the client product — Standard Project Template](https://www.notion.so/2b99bfc98f9f80ed8267c08585a8f962)
- Main SOP automation page: [Automating Admin AMs Processes](https://www.notion.so/3599bfc98f9f808eb790ee141cc4a2c4)
