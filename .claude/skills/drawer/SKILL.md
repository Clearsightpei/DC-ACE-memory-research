---
name: drawer
description: Role briefing for the Drawer phase of /cycle (run_6). Dispatched to a fresh subagent. Reads the structural brief (米字格 anchors + joint specs) and the GT PNG. Translates anchors to turtle math-coords via _anchor.py. Writes ONE attempts/cycle_<N>/generated.py with ONE task (1-task-per-cycle). Self-previews up to 2 iterations comparing own PNG to GT. Refuses to commit if turtle-call count doesn't match the brief's MMH stroke count.
---

# Drawer role brief — run_6

You are a fresh subagent — you have NO prior conversation context.

You receive ONE task per cycle. Your goal: produce a turtle-rendered
PNG that satisfies the brief's structural specification.

## Working directory

`/Users/peilinwu/Documents/AI memory research/runs/run_6` (or whatever
the orchestrator says).

## Files you may read

- `task_briefs/cycle_<N>.md` — your structural brief (anchors + joints).
- `task_briefs/cycle_<N>_dataset.json` — same info in JSON for parsing.
- `ground_truths/cycle_<N>/01_<char>.png` — the MMH-rendered GT.
- `success_bank/INDEX.md` and `success_bank/code/*.py` — primitives you
  reuse: heng, shu, pie, na, ti, dian and the 7 compound strokes (after
  they're mastered in c7–c13).
- `success_bank/code/_anchor.py` — the orchestrator drops a copy here
  so you can call `anchor_to_xy(...)` without `tools/`.
- `principle_bank.md`, `sandbox.md`, `to_be_learned.md`.
- Your own attempt PNG after rendering.

## Files you MUST NOT read

- `tools/` (physically quarantined — won't exist during your turn).
- Prior `attempts/cycle_*/` (no reading prior generated.py).
- `judge_results/`, `teaching_*`, `cycle_state.json`, `cycle_summary.md`, `dashboard.md`.
- Any other run directory under `runs/`.

## Forbidden code patterns

- `subprocess`, `os.system` — single turtle process, `t.reset()` between
  renders if needed.
- `from runs/run_<x>/...` — never reach into other runs.
- **Magic numbers in your `generated.py`** — every `(ox, oy, scale)`
  must be derived from `anchor_to_xy(anchor)` calls. The brief's
  anchors are the source of truth.

## Anchor → turtle translation

Import the helper:

```python
import sys, os
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                  '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
```

For each declared stroke in the brief:
1. `tx0, ty0 = anchor_to_xy(stroke['from'])`
2. `tx1, ty1 = anchor_to_xy(stroke['to'])`
3. Compute `(ox, oy, scale)` for your primitive call so its rendered
   endpoints land at `(tx0, ty0)` and `(tx1, ty1)`. Each primitive
   documents its canonical endpoints in its docstring.

## Workflow (one task per cycle)

1. **Read the brief**. Note: MMH stroke count, list of strokes with
   anchors, list of joints with cells.
2. **Pre-flight stroke-count check**. Count your planned top-level
   `draw_<primitive>(...)` calls in `task_01()`. They must equal the
   brief's MMH stroke count. If you find yourself wanting to split a
   primitive call into two (e.g. drawing a 横折 as separate 横 + 竖),
   STOP — the brief defines the canonical decomposition. One MMH
   stroke = one primitive call, including compound strokes.
3. **Write `attempts/cycle_<N>/generated.py`**:

   ```python
   import io, os, sys, turtle
   from PIL import Image
   WIDTH, HEIGHT = 800, 600
   OUT_DIR = os.path.dirname(os.path.abspath(__file__))
   SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
   sys.path.insert(0, SB)
   from _anchor import anchor_to_xy
   from heng import draw as draw_heng   # import only what you need
   # other primitives as needed

   def save_canvas_to_png(screen, path):
       canvas = screen.getcanvas()
       ps = canvas.postscript(colormode="color")
       img = Image.open(io.BytesIO(ps.encode("utf-8")))
       img.load(scale=1)
       img.convert("RGBA").save(path, "PNG")

   def reset(t):
       t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
       t.penup(); t.goto(0,0); t.setheading(90)

   def task_01(t, screen):
       reset(t)
       # ONE draw_<primitive>() per MMH stroke.
       # Use anchor_to_xy(...) for every position. No magic numbers.
       ...
       save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_<char>.png"))

   def main():
       screen = turtle.Screen()
       screen.setup(WIDTH, HEIGHT)
       screen.bgcolor("white"); screen.tracer(0)
       t = turtle.Turtle()
       task_01(t, screen); screen.update()

   if __name__ == "__main__":
       main()
   ```
4. **Render**. Save your PNG.
5. **Self-preview**. Open your PNG and the GT PNG with the Read tool.
   For each declared anchor, eyeball: did the rendered endpoint land
   near it? For each declared joint, eyeball: do the participating
   points meet inside the right cell?
6. **Iterate (max 2)**. Adjust anchor-derived offsets if alignment is
   off. After 2 iterations, commit whatever you have.
7. **Return a short summary**: anchor decisions per stroke, self-critique vs GT.

## Hard rules

- Stroke count exactly matches the brief.
- No magic numbers — all positions come from `anchor_to_xy(...)`.
- No subprocess, no os.system.
- No reading prior cycles, no other runs.
