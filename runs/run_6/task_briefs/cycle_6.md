# Cycle 6 — Focus: 亅 (竖钩 compound stroke)

## Phase
1.5 — compound stroke mastery.

## MMH stroke count
1

## Target
亅 (jué) — vertical drop + hook at bottom. 1 stroke in MMH (the hook is part of the same stroke).

## Strokes
1. shu_gou(from=("TC", 0.2, 0.37), corner=("BC", 0.4, 0.95), to=("BL", 0.78, 1.17))

  Anchor xy: head (-30, +113), corner (-12, -169), tail (-72, -167). Vertical drop ~280 px, then hook ~60 px left.

## Joints
None (single stroke).

## What's new: TWO-segment stitched stroke

This is the first stroke with an internal corner. The Drawer renders TWO Bezier segments joined at the corner:
- Segment A: head → corner. Width profile like 竖 (entry 16 → shaft 11 → press at corner ~13).
- Segment B: corner → tail (short hook). Width 13 → 3 (rapid taper to fine point).

Each segment is its own brushed_bezier call. The structural check only verifies head and tail — but the corner placement is what makes it look like a 钩.

## Code skeleton

```python
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import brushed_bezier

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(90)

def w_shu_main(s):
    # vertical drop: 16 → 11 → 13 (press at corner)
    if s < 0.10: return 16.0 - (s/0.10) * 5.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15) * 2.0

def w_hook(s):
    # hook taper: 13 → 3
    return 13.0 - s * 10.0

def draw_shu_gou(t, from_anchor, corner_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor)
    pc = anchor_to_xy(corner_anchor)
    p3 = anchor_to_xy(to_anchor)
    # Segment A: head to corner (vertical drop)
    p1 = (p0[0] + (pc[0]-p0[0]) * 0.33, p0[1] + (pc[1]-p0[1]) * 0.33)
    p2 = (p0[0] + (pc[0]-p0[0]) * 0.67, p0[1] + (pc[1]-p0[1]) * 0.67)
    brushed_bezier(t, p0, p1, p2, pc, w_shu_main, samples=200)
    # Segment B: corner to tail (hook)
    # Tangential junction: control point near corner continues the inward direction
    p1b = (pc[0] + (p3[0]-pc[0]) * 0.5, pc[1] + (p3[1]-pc[1]) * 0.5 + 5)  # slight upward arc
    p2b = (pc[0] + (p3[0]-pc[0]) * 0.8, pc[1] + (p3[1]-pc[1]) * 0.8 + 3)
    brushed_bezier(t, pc, p1b, p2b, p3, w_hook, samples=80)

def task_01(t, screen):
    reset(t)
    draw_shu_gou(t, ("TC", 0.2, 0.37), ("BC", 0.4, 0.95), ("BL", 0.78, 1.17))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_亅.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```

EXACTLY 1 top-level draw_shu_gou call. The TWO brushed_bezier calls inside it are implementation details — they count as ONE primitive (one MMH stroke).
