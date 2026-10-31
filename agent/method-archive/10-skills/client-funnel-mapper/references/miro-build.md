# Building funnels in Miro

## Tool workflow

1. `canvas_search` with `result_mode: overview` on the board to see what's there and find clear space. Place new frames below or beside existing content with at least 160px clearance.
2. `canvas_get_canvas_composer_skill` with `step: "design"` for a new composition (or `step: "edit"` for changes), then `step: "dsl"` for the SVG grammar. Also load the diagramming format skill (`canvas_load_format_skill`, `format_name: diagramming`, `notation: free_form`).
3. `canvas_create_from_svg` with one SVG per frame (or several frames in one SVG).
4. `board_show` with `?moveToWidget=<frame id>` so the user sees the result.
5. For changes: `canvas_update_from_svg`.

If the Miro connector isn't available, draw the flow with the Visualizer or a Mermaid flowchart instead, keeping the same stages, colours and left-to-right direction.

## SVG patterns that work

- Wrap each frame as `<g id="x" transform="translate(X,Y)" data-frame="Name">` with a first child `<rect data-type="frame" .../>`. Child coordinates are frame-relative.
- Write **all `<line>` connectors first**, then shapes, so arrows sit underneath nodes.
- Connectors: `data-start`/`data-end` pointing at local shape ids, plus `data-start-side`/`data-end-side`, `data-shape="elbowed"` or `"straight"`, `data-arrow="end"`, and an optional `data-content` label.
- Node text goes in `data-content` with escaped HTML: `&lt;b&gt;Title&lt;/b&gt;&lt;br&gt;detail`. Links: `&lt;a href=&quot;URL&quot;&gt;label&lt;/a&gt;`.
- Decision points: `data-shape="rhombus"`.
- Tables: `<foreignObject data-type="table">` with a `<table>`. Select columns use `data-type="select" data-options="A:#hex, B:#hex"`. Timelines: `data-type="timeline"` with Title, Start Date, End Date columns.
- Deep link to another frame: `https://miro.com/app/board/<board id>/?moveToWidget=<frame id>`.

## Update gotchas (learned the hard way)

- **New connectors to existing shapes:** declare stub shapes in the same SVG, `<rect id="localA" data-miro-id="<existing id>"/>`, and point `data-start`/`data-end` at the local ids. Referencing `m<id>` directly from a new line fails.
- **Updating an existing connector:** restate it fully (coordinates, stroke, arrow, shape, sides) with `data-start="m<id>"` and `data-end="m<id>"`.
- **Moving shapes:** restate the full box (`x`, `y`, `width`, `height`).
- **Changing a textArea's width** recentres it; send a second update with the `x` you want.
- **Tables auto-size** and can render wider than you planned. Read them back (`canvas_read_as_svg` with `widget_ids`), then resize the frame to fit. Moving a frame may not move the tables inside it, so move tables explicitly.
- **Growing a frame** can overlap the frame below. Check and move the lower frames down.
- **"Locked by another session"** means someone has the item selected. Ask the user to click off it, then retry.
- **Positions or text differ from what you wrote?** The user has edited the board. Keep their layout, update only what you were asked to, and don't re-add things they deleted.
- **Deleting:** `<rect data-miro-id="<id>" data-deleted="true"/>`, and the same for lines. Only delete when the user asked or agreed.
