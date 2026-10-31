---
title: "Agentic Flows"
source_url: https://app.notion.com/p/3069bfc98f9f80df856ed15966d6bae7
notion_id: 3069bfc9-8f9f-80df-856e-d15966d6bae7
data_source: collection://3069bfc9-8f9f-80b2-b2a2-000b85ddca9a
fetched: 2026-10-30
type: database
parent_page: https://app.notion.com/p/3029bfc98f9f80cdae44d213d68eb0a7 (the author’s Notes, under i3 Strategy Foundations & Blueprint)
row_count_exported: 12 (all rows; has_more=false)
notes: "Row page bodies were not fetched; the export captures schema plus each row's title, Multi-select tag and Dependency text, as requested."
---

# Data source (verbatim fetch output)

<data-source url="{{collection://3069bfc9-8f9f-80b2-b2a2-000b85ddca9a}}">
The title of this Data Source is: Agentic Flows

Here is the database's configurable state:
Properties with `readOnly: true` are synced or system-managed. Do not try to update their values with page update tools.
<data-source-state>
{"name":"Agentic Flows","schema":{"Dependency":{"description":"","name":"Dependency","type":"text"},"Multi-select":{"description":"","name":"Multi-select","options":[{"color":"green","description":"","name":"Foundational","url":"collectionPropertyOption://3069bfc9-8f9f-80b2-b2a2-000b85ddca9a/TWw_Wg/ODU5ODE1MjgtYjg5Yy00MmZlLWEyMWQtNjY0ZTI1NTBkYmRh"},{"color":"gray","description":"","name":"ideation","url":"collectionPropertyOption://3069bfc9-8f9f-80b2-b2a2-000b85ddca9a/TWw_Wg/YjllZmE3NjgtYzUyYy00NjMzLWFmN2UtOWYxMjgzNjhhZDE5"},{"color":"purple","description":"","name":"data","url":"collectionPropertyOption://3069bfc9-8f9f-80b2-b2a2-000b85ddca9a/TWw_Wg/N2IzMmZkM2EtZGMyMS00NGM1LWI5OWYtZjk4MWY1OWQzZmFm"},{"color":"orange","description":"","name":"Tool","url":"collectionPropertyOption://3069bfc9-8f9f-80b2-b2a2-000b85ddca9a/TWw_Wg/MTFkMDExMjYtMTJlOC00NzIyLTg0ODQtNmY0MjUxNDJkY2M1"}],"type":"multi_select"},"Name":{"description":"","name":"Name","type":"title"}},"url":"collection://3069bfc9-8f9f-80b2-b2a2-000b85ddca9a"}
</data-source-state>

Here is the SQLite table definition for this data source.
<sqlite-table>
CREATE TABLE IF NOT EXISTS "collection://3069bfc9-8f9f-80b2-b2a2-000b85ddca9a" (
	url TEXT UNIQUE,
	createdTime TEXT, -- ISO-8601 datetime string, automatically set. This is the canonical time for when the page was created.
	"Multi-select" TEXT, -- JSON array with zero or more of ["Foundational", "ideation", "data", "Tool"]
	"Dependency" TEXT,
	"Name" TEXT
)
</sqlite-table>
</data-source>

# Rows (verbatim, rows mode, all 12 rows)

```json
{"results":[{"Multi-select":"[\"Foundational\"]","Dependency":"","Name":"Initial Dossier","url":"https://app.notion.com/p/3069bfc98f9f805f827bfc80b270b69d"},{"Multi-select":"[\"data\"]","Dependency":"","Name":"Finding out who owns a crypto wallet","url":"https://app.notion.com/p/3069bfc98f9f80d9baf0fa0512e794ed"},{"Multi-select":"[\"Foundational\"]","Dependency":"Dossier","Name":"Initial research on a client (questions)","url":"https://app.notion.com/p/3069bfc98f9f80058fc6f93047d48a3a"},{"Multi-select":"[\"data\"]","Dependency":"Questions","Name":"Researching the initial questions","url":"https://app.notion.com/p/3069bfc98f9f8063b8a8c58e73837125"},{"Multi-select":"[\"ideation\"]","Dependency":"Needs the initial research and the answers to the research","Name":"Positioning initial recommendation","url":"https://app.notion.com/p/3069bfc98f9f8076a402d671ab969320"},{"Multi-select":"[\"data\"]","Dependency":"Positioning, initial research, and any extra context","Name":"ICP drilldown","url":"https://app.notion.com/p/3069bfc98f9f80fa8558d27ed31c558d"},{"Multi-select":"[\"ideation\"]","Dependency":"ICP drilldown, Positioning","Name":"Narratives & Messaging","url":"https://app.notion.com/p/3069bfc98f9f80fc84d4df56265d36b0"},{"Multi-select":"[\"ideation\"]","Dependency":"ICP Drilldown, Positioning, Messaging","Name":"ToV","url":"https://app.notion.com/p/3069bfc98f9f80d2ba4dcfbd7fc959ee"},{"Multi-select":"[\"ideation\"]","Dependency":"ICP Drilldown, Positioning, Messaging, ToV","Name":"Content Strategy","url":"https://app.notion.com/p/3069bfc98f9f8005a088cb5aeacb6291"},{"Multi-select":"[\"ideation\"]","Dependency":"ICP, Messaging, Positioning","Name":"Targetting and Distribution","url":"https://app.notion.com/p/3069bfc98f9f80c9b5a1e97b6ee8c97e"},{"Multi-select":"[\"Tool\"]","Dependency":"","Name":"Slides designer","url":"https://app.notion.com/p/3069bfc98f9f803794f8e5a355dcbeb3"},{"Multi-select":"[\"Tool\"]","Dependency":"","Name":"Website Structure audit","url":"https://app.notion.com/p/3069bfc98f9f80dab9d6cb533587bd16"}],"has_more":false}
```
