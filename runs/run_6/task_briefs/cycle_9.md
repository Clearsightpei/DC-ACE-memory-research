# Cycle 9 — Focus: 乚 (竖折 compound stroke)

## Phase 1.5
## MMH stroke count: 1

## Target
乚 — vertical down then horizontal right. 2-segment L shape (rotated 90° from 横钩).

## Anchors
1. shu_zhe(from=("TL", 0.32, 0.64), corner=("BL", 0.32, 1.04), to=("BR", 0.94, 0.35))
   xy: head (-118, 86), corner (-118, -154), tail (144, -85).

## Two-segment stitched
- A: head → corner (vertical drop, w 16→11→13)
- B: corner → tail (horizontal right, w 13→11→18, with closing press)

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

def w_drop(s):
    if s < 0.10: return 16.0 - (s/0.10)*5.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*2.0

def w_horiz(s):
    if s < 0.05: return 13.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*7.0

def draw_shu_zhe(t, fa, ca, ta):
    p0 = anchor_to_xy(fa); pc = anchor_to_xy(ca); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (pc[0]-p0[0])*0.33, p0[1] + (pc[1]-p0[1])*0.33)
    a2 = (p0[0] + (pc[0]-p0[0])*0.67, p0[1] + (pc[1]-p0[1])*0.67)
    brushed_bezier(t, p0, a1, a2, pc, w_drop, samples=200)
    b1 = (pc[0] + (p3[0]-pc[0])*0.33, pc[1] + (p3[1]-pc[1])*0.33 + 4)
    b2 = (pc[0] + (p3[0]-pc[0])*0.67, pc[1] + (p3[1]-pc[1])*0.67 + 4)
    brushed_bezier(t, pc, b1, b2, p3, w_horiz, samples=160)

def task_01(t, screen):
    reset(t)
    draw_shu_zhe(t, ("TL", 0.32, 0.64), ("BL", 0.32, 1.04), ("BR", 0.94, 0.35))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_乚.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```
