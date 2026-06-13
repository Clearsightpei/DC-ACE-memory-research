# Cycle 5 — Focus: 八 (introduces 捺 atomic stroke)

## Phase
1 — atomic stroke mastery (introduces 捺 alongside mastered 撇).

## MMH stroke count
2

## Target
八 (bā) — 2 strokes, separated (no joint): 撇 on left, 捺 on right.

## Strokes (from MMH measurement)
1. pie(from=("ML", 0.78, 0.67), to=("BL", 0.0, 1.0))    # head (-72, -17), tail (-150, -150)
2. na(from=("TC", 0.26, 0.77),  to=("BR", 1.0, 0.6))    # head (-24, +73),  tail (+150, -110)

## Joints
None (strokes are separated at the top).

## What's new: 捺 (right-down diagonal with FLAT KICK)

捺 is the right-down companion to 撇. Width profile is REVERSED:
- head: thin (~5)
- body: thickens 5 → 14 → 18
- tail: a flat kick — press 18 → release 3 over the final 15%

Use TWO Bezier segments stitched at a "kick base" anchor for cleanest output:

- Main sweep: head → kick_base, width 5 → 18.
- Flat kick: kick_base → tail, width 18 → 3 (a short ~15% release segment).

Or keep it simple with a single Bezier + width profile 5 → 14 → 18 → 3 over s ∈ [0, 1] (single-segment 捺).

For c5 just use the single-segment form. Compound 捺 with proper flat kick can be a future entry.

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
from pie import draw_pie

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(90)

def w_na(s):
    # 5 → 14 → 18 → 3
    if s < 0.30: return 5.0 + (s/0.30) * 9.0     # head 5 → 14
    if s < 0.75: return 14.0 + ((s-0.30)/0.45) * 4.0  # 14 → 18
    return 18.0 - ((s-0.75)/0.25) * 15.0   # 18 → 3 (kick release)

def draw_na(t, from_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor); p3 = anchor_to_xy(to_anchor)
    # Concave-up arc: control points BELOW the chord (in math y, that's smaller y → -10)
    p1 = (p0[0] + (p3[0]-p0[0]) * 0.33, p0[1] + (p3[1]-p0[1]) * 0.33 - 10)
    p2 = (p0[0] + (p3[0]-p0[0]) * 0.67, p0[1] + (p3[1]-p0[1]) * 0.67 - 10)
    brushed_bezier(t, p0, p1, p2, p3, w_na, samples=240)

def task_01(t, screen):
    reset(t)
    draw_pie(t, ("ML", 0.78, 0.67), ("BL", 0.0, 1.0))
    draw_na (t, ("TC", 0.26, 0.77), ("BR", 1.0, 0.6))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_八.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```

EXACTLY 2 top-level draw calls (1 draw_pie + 1 draw_na) in task_01.
