# Cycle 11 — Focus: 又 (introduces 横撇 compound stroke)

## Phase 1.5  /  MMH stroke count: 2

## Strokes
1. heng_pie(from=("ML", 0.52, 0.55), corner=("TC", 0.5, 1.0), to=("BL", 0.03, 1.22))
   head (-98, 45), corner (0, -50), tail (-147, -172). NEW PRIMITIVE.
2. na(from=("ML", 0.54, 0.86), to=("BR", 1.35, 0.94))
   head (-96, 14), tail (185, -176). Reuse mastered draw_na.

## Joints: 1 ⇆ 2 mid-mid @ BC.

## What's new: 横撇 — horizontal then tapered down-left (撇-style tail).

```python
def w_hengpie_main(s):
    if s < 0.10: return 14.0 - (s/0.10)*3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*2.0

def w_hengpie_tail(s):
    return 13.0 - s*10.0  # taper to point

def draw_heng_pie(t, fa, ca, ta):
    p0 = anchor_to_xy(fa); pc = anchor_to_xy(ca); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (pc[0]-p0[0])*0.33, p0[1] + (pc[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (pc[0]-p0[0])*0.67, p0[1] + (pc[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, pc, w_hengpie_main, samples=180)
    b1 = (pc[0] + (p3[0]-pc[0])*0.4, pc[1] + (p3[1]-pc[1])*0.4 + 5)
    b2 = (pc[0] + (p3[0]-pc[0])*0.75, pc[1] + (p3[1]-pc[1])*0.75 + 5)
    brushed_bezier(t, pc, b1, b2, p3, w_hengpie_tail, samples=160)
```

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
from na import draw_na

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(90)

# [paste w_hengpie_main, w_hengpie_tail, draw_heng_pie above]
def w_hengpie_main(s):
    if s < 0.10: return 14.0 - (s/0.10)*3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*2.0

def w_hengpie_tail(s): return 13.0 - s*10.0

def draw_heng_pie(t, fa, ca, ta):
    p0 = anchor_to_xy(fa); pc = anchor_to_xy(ca); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (pc[0]-p0[0])*0.33, p0[1] + (pc[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (pc[0]-p0[0])*0.67, p0[1] + (pc[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, pc, w_hengpie_main, samples=180)
    b1 = (pc[0] + (p3[0]-pc[0])*0.4, pc[1] + (p3[1]-pc[1])*0.4 + 5)
    b2 = (pc[0] + (p3[0]-pc[0])*0.75, pc[1] + (p3[1]-pc[1])*0.75 + 5)
    brushed_bezier(t, pc, b1, b2, p3, w_hengpie_tail, samples=160)

def task_01(t, screen):
    reset(t)
    draw_heng_pie(t, ("ML", 0.52, 0.55), ("TC", 0.5, 1.0), ("BL", 0.03, 1.22))
    draw_na(t, ("ML", 0.54, 0.86), ("BR", 1.35, 0.94))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_又.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```
