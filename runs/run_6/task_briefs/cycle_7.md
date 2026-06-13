# Cycle 7 — Focus: 乛 (横钩 compound stroke)

## Phase
1.5 — compound stroke mastery.

## MMH stroke count
1

## Target
乛 (héng gōu) — horizontal then short hook down-left. 1 stroke.

## Strokes
1. heng_gou(from=("ML", 0.52, 0.28), corner=("MR", 0.84, 0.36), to=("MR", 0.03, 0.67))

  Anchor xy: head (-98, 22), corner (84, 14), tail (53, -17). Horizontal then sharp turn down-left.

## Joints
None.

## Two-segment stitched stroke
- Segment A (head → corner): horizontal, width 16 → 11 → 13 (like 横).
- Segment B (corner → tail): short hook, width 13 → 3.

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

def w_heng_main(s):
    if s < 0.10: return 16.0 - (s/0.10) * 5.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15) * 2.0

def w_hook(s):
    return 13.0 - s * 10.0

def draw_heng_gou(t, from_anchor, corner_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor); pc = anchor_to_xy(corner_anchor); p3 = anchor_to_xy(to_anchor)
    # Segment A: horizontal sweep with slight upward bow
    p1 = (p0[0] + (pc[0]-p0[0])*0.33, p0[1] + (pc[1]-p0[1])*0.33 + 4)
    p2 = (p0[0] + (pc[0]-p0[0])*0.67, p0[1] + (pc[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, p1, p2, pc, w_heng_main, samples=200)
    # Segment B: hook down-left
    p1b = (pc[0] + (p3[0]-pc[0])*0.4, pc[1] + (p3[1]-pc[1])*0.5)
    p2b = (pc[0] + (p3[0]-pc[0])*0.75, pc[1] + (p3[1]-pc[1])*0.8)
    brushed_bezier(t, pc, p1b, p2b, p3, w_hook, samples=80)

def task_01(t, screen):
    reset(t)
    draw_heng_gou(t, ("ML", 0.52, 0.28), ("MR", 0.84, 0.36), ("MR", 0.03, 0.67))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_乛.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```
