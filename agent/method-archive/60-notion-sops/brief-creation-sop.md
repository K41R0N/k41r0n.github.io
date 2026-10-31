---
title: "Brief Creation"
source_url: https://app.notion.com/p/3639bfc98f9f808bbfebcac94e41a160
notion_id: 3639bfc9-8f9f-808b-bfeb-cac94e41a160
fetched: 2026-10-30
type: page
path: "Vault (NEVER DELETE) / the client product Resources"
parent_data_source: collection://26d9bfc9-8f9f-803a-9dfb-000bfee3f1d7 (the client product Resources, under the client product Academy)
page_last_edited_at: 2026-05-20T08:31:29.922Z
notes: "Inline discussion markers (discussion-urls spans) preserved as returned; comment threads themselves not fetched."
---

# Properties (verbatim)

```json
{"Date created":"2026-05-17T18:28:07.177Z","Department":["https://app.notion.com/p/2889bfc98f9f80d4bc36e2c799220d0b"],"Last updated":"2026-05-20T08:31:29.922Z","Name":"<p>\nBrief Creation \n</p>","Owner":["user://922d063f-b0c0-44b5-9125-d07e670fbabc"],"Role":["Account Manager"],"Status":"Up To Date","Type":["SOP"],"date:Date:is_datetime":0,"url":"https://app.notion.com/p/3639bfc98f9f808bbfebcac94e41a160"}
```

Parent data source schema (the client product Resources):

```sql
CREATE TABLE IF NOT EXISTS "collection://26d9bfc9-8f9f-803a-9dfb-000bfee3f1d7" (
	url TEXT UNIQUE,
	createdTime TEXT, -- ISO-8601 datetime string, automatically set. This is the canonical time for when the page was created.
	"Platform " TEXT, -- JSON array with zero or more of ["Notion", "ChatGPT", "Discord", "Claude", "Twitter / X", "TweetHunter", "YouTube", "cookie3", "LinkedIn", "1Pass", "Canva", "Facebook", "Reddit", "Google Ads", "Google Analytics", "Google Tag Manager", "TikTok Ads", "Webflow", "Figma"]
	"date:Date:start" TEXT, -- ISO-8601 date or datetime string. Use the expanded property (date:<column_name>:start) to set this value.
	"date:Date:end" TEXT, -- ISO-8601 date or datetime string, can be empty. Must be NULL if the date is a single date, and must be present if the date is a range. Use the expanded property (date:<column_name>:end) to set this value.
	"date:Date:is_datetime" INTEGER, -- 1 if the date is a datetime, 0 if it is a date, NULL defaults to 0. Use the expanded property (date:<column_name>:is_datetime) to set this value.
	"Task" TEXT, -- JSON array of page URLs relating to {{collection://eaf1bd06-b97e-4f31-b5af-a74ce80a096c}} data source, you must "view" {{collection://eaf1bd06-b97e-4f31-b5af-a74ce80a096c}} to query this column
	"Type" TEXT, -- JSON array with zero or more of ["SOP", "Case Study", "Playbook", "New Hire Onboarding", "Template", "Reference", "Brain Dump", "ICP", "Client Onboarding", "Tools", "Campaign Review", "AM Onboarding"]
	"CLIENT" TEXT, -- JSON array of page URLs relating to {{collection://3309bfc9-8f9f-8016-8388-000b1a575e1f}} data source, you must "view" {{collection://3309bfc9-8f9f-8016-8388-000b1a575e1f}} to query this column
	"Owner" TEXT, -- JSON array of zero or more user IDs
	"Department" TEXT, -- JSON array of page URLs relating to {{collection://a8499273-fd57-4cc4-b9c9-6bc6fb30799e}} data source, you must "view" {{collection://a8499273-fd57-4cc4-b9c9-6bc6fb30799e}} to query this column
	"DEPARTMENT" TEXT, -- JSON array of page URLs relating to {{collection://3309bfc9-8f9f-8005-b769-000be1ed02ac}} data source, you must "view" {{collection://3309bfc9-8f9f-8005-b769-000be1ed02ac}} to query this column
	"Role" TEXT, -- JSON array with zero or more of ["Social Media Manager", "Video Editor", "Graphic Designer", "Account Manager", "Business Development Manager", "Strategy", "Paid Media", "Public Relations", "Web developer"]
	"Date created" TEXT NOT NULL, -- ISO-8601 datetime string, automatically set. This is the canonical time for when the page was created.
	"Status" TEXT, -- one of ["To Be Built...", "Underway", "In Review", "Up To Date", "Archived/Old"] Default: "To Be Built...".
	"Last updated" TEXT NOT NULL, -- ISO-8601 datetime string, automatically set. This is the canonical time for when the page was last edited.
	"Name" TEXT,
	"Lead" TEXT -- JSON array of zero or more user IDs
)
```

# Page content (verbatim Notion-flavored Markdown)

<quote color="purple_bg">
Standard operating procedure for how Account Managers create briefs at the client product. A brief is a brief — same format, same flow, every time. Canonical output is the one-page, 6-question <code>.docx</code> produced by the <code>project-brief-skill</code> in Claude.
</quote>

<b>North star:</b> every piece of work at the client product starts with a brief. Briefs are short on purpose — strategy, tactics, and execution details live downstream in the Notion project page. The AM's job is to get the brief written, approved by strategy, signed off by the client, and locked.

---

## Phase 0 — Project trigger

Projects are born one of two ways. Either path lands the AM in Phase 1.

- [ ] AM — Capture the trigger:
  - [ ] <b>Client-driven</b> — new ask surfaced on a client call, Slack, email, or Telegram (e.g., "we want to do an earnings campaign")
  - [ ] <b>Internal-driven</b> — idea from internal brainstorming, retro, or strategy session

---

## Phase 1 — Gather project info

Goal: leave Phase 1 with enough context to write the brief.

- [ ] AM — Gather all relevant info from the trigger source (call transcript, notes, Slack, email)
- [ ] AM — Ask the client (or the internal proposer) clarifying questions async if anything is missing. Minimum set:
  - [ ] Goal — what does success look like
  - [ ] Scope — what's in / what's out
  - [ ] Deadline — hard date or rough window
  - [ ] Budget — if applicable
  - [ ] Stakeholders — who on the client side owns this
- [ ] AM — Identify which the client product workstreams the project needs (e.g., earnings campaign → IR + SMM + PR + Creatives). This determines the project's internal team

---

## Phase 2 — Draft the brief

Goal: produce a v1 brief, get it approved by strategy, turn it into a visual, and get the client to sign off.

- [ ] AM — Open a Google Doc in the client's <code>Projects</code> folder, named <code>[Project Name] — Brief v1</code>
- [ ] AM — Goes to respective client's Claude Project
- [ ] AM — Creates new task in the respective client's Claude Project
- [ ] AM — Triggers <code>/project-brief-skill</code> and feeds Claude the transcript of the call / message with the trigger of the campaign
- [ ] AM — Sanity checks the brief provided by Claude and makes edits as needed
- [ ] <span discussion-urls="discussion://3639bfc9-8f9f-808b-bfeb-cac94e41a160/f32e6ae5-b26d-4c5a-bb92-340677931b85/3659bfc9-8f9f-8081-8f19-001cfce0b69f">AM — Saves brief in the Google Drive folder of the respective client under </span><span discussion-urls="discussion://3639bfc9-8f9f-808b-bfeb-cac94e41a160/f32e6ae5-b26d-4c5a-bb92-340677931b85/3659bfc9-8f9f-8081-8f19-001cfce0b69f"><code>Account Management</code></span><span discussion-urls="discussion://3639bfc9-8f9f-808b-bfeb-cac94e41a160/f32e6ae5-b26d-4c5a-bb92-340677931b85/3659bfc9-8f9f-8081-8f19-001cfce0b69f"> → </span><span discussion-urls="discussion://3639bfc9-8f9f-808b-bfeb-cac94e41a160/f32e6ae5-b26d-4c5a-bb92-340677931b85/3659bfc9-8f9f-8081-8f19-001cfce0b69f"><code>Projects</code></span>
- [ ] AM — Open a thread in the client's <code>*-all-projects</code> Slack channel for this project. <b>One Slack thread = one project.</b> Every project conversation lives in that thread from now on
- [ ] AM — Send the brief to Strategy for approval (Slack DM the strategy lead with the doc link + 1-line context)
- [ ] Strategy — Edits and approves
- [ ] AM — Run the approved brief through the <s><b><span discussion-urls="discussion://3639bfc9-8f9f-808b-bfeb-cac94e41a160/7661c5c9-703c-416d-9cb5-0e639f9fea2d/3659bfc9-8f9f-8006-b8b5-001cccb69086">brief-to-visual Claude skill</span></b></s><s> </s><code>/presentation-i3</code> skill to produce a visual version
- [ ] AM — Show the visual brief to the client for sign-off <b>before</b> briefing the internal team

---

## Handoff

Brief is locked + client-approved → run the [AM Project Management SOP](https://www.notion.so/3639bfc98f9f81cb9118fc26fade1f50) starting at Phase 1 (Create the Notion project).

---

## Done when — how we know it works

- Every piece of work at the client product starts with a 1-page, 6-question <code>.docx</code> brief produced via <code>project-brief-skill</code>.
- The brief is strategy-approved before the visual gets made.
- The visual is client-approved before the internal team gets briefed.
- <span discussion-urls="discussion://3639bfc9-8f9f-808b-bfeb-cac94e41a160/5d292c80-52c3-4e25-b172-898b3c75ce11/3659bfc9-8f9f-808a-b391-001c5451a481">The brief and the visual never drift out of sync — the </span><span discussion-urls="discussion://3639bfc9-8f9f-808b-bfeb-cac94e41a160/5d292c80-52c3-4e25-b172-898b3c75ce11/3659bfc9-8f9f-808a-b391-001c5451a481"><code>.docx</code></span><span discussion-urls="discussion://3639bfc9-8f9f-808b-bfeb-cac94e41a160/5d292c80-52c3-4e25-b172-898b3c75ce11/3659bfc9-8f9f-808a-b391-001c5451a481"> is the canonical source.</span>

---

## Tooling map

| Tool | What it's for |
| --- | --- |
| Client's Claude Project | Where the AM triggers <code>/project-brief-skill</code> so Claude has full client context |
| <code>project-brief-skill</code> (Claude) | Produces the canonical one-page 6Q <code>.docx</code> |
| Brief-to-visual Claude skill | Turns the approved <code>.docx</code> into a client-ready visual |
| Google Drive (Client <code>Projects</code> folder) | Where the <code>.docx</code>  • visual live. Source of truth |
| Client <code>*-all-projects</code> Slack channel | Project thread opens here during brief drafting. One thread = one project |

---

## References

- [AM Project Management SOP](https://www.notion.so/3639bfc98f9f81cb9118fc26fade1f50) — the SOP this one hands off to

<p />
