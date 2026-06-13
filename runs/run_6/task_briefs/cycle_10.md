# Cycle 10 — Focus: 七 (introduces 竖弯钩 compound stroke)

## Phase 1.5
## MMH stroke count: 2

## Target
七 — 2 strokes: 横 + 竖弯钩 (vertical-curve-hook), crossing at center.

## Strokes
1. heng(from=("ML", 0.36, 0.91), to=("MR", 0.98, 0.7))   # head (-164,-69), tail (148,-20)
2. shu_wan_gou(from=("TC", 0.41, 0.55), corner=("BC", 0.4, 0.55), to=("BR", 0.59, 0.41))
   # head (-59,95), corner (-40,-95), tail (109,-160)

## Joints
1. stroke 1 mid(0.40) ⇆ stroke 2 mid(0.38) @ C

## What's new: 竖弯钩 (vertical-curve-hook)

Vertical drop → curve to right → short hook UP at the end.

3-segment primitive:
- Seg A: head → corner (vertical drop, w 14→11→11)
- Seg B: corner → tail-area (curve right, w 11→13)
- Seg C: tail kick (small up-flick at the end)

For c10 simplification: 2 brushed_bezier segments — vertical then curve-right (skip the explicit kick, let the closing widen do the kick illusion).

## Code skeleton

```python
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import brushed_bezier, draw_heng

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(90)

def w_vert(s):
    if s < 0.10: return 14.0 - (s/0.10)*3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*2.0

def w_curve(s):
    if s < 0.20: return 13.0
    if s < 0.80: return 11.0
    return 11.0 + ((s-0.80)/0.20)*7.0  # closing kick

def draw_shu_wan_gou(t, fa, ca, ta):
    p0 = anchor_to_xy(fa); pc = anchor_to_xy(ca); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (pc[0]-p0[0])*0.33, p0[1] + (pc[1]-p0[1])*0.33)
    a2 = (p0[0] + (pc[0]-p0[0])*0.67, p0[1] + (pc[1]-p0[1])*0.67)
    brushed_bezier(t, p0, a1, a2, pc, w_vert, samples=180)
    # Curve segment with sweep down-then-up via control points
    b1 = (pc[0] + (p3[0]-pc[0])*0.4, pc[1] + (p3[1]-pc[1])*0.3 - 10)
    b2 = (pc[0] + (p3[0]-pc[0])*0.85, pc[1] + (p3[1]-pc[1])*0.85 - 5)
    brushed_bezier(t, pc, b1, b2, p3, w_curve, samples=160)

def task_01(t, screen):
    reset(t)
    draw_heng(t, ("ML", 0.36, 0.91), ("MR", 0.98, 0.7))
    draw_shu_wan_gou(t, ("TC", 0.41, 0.55), ("BC", 0.4, 0.55), ("BR", 0.59, 0.41))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_七.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```

EXACTLY 2 top-level draw calls (1 draw_heng + 1 draw_shu_wan_gou).
