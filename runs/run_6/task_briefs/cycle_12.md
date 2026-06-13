# Cycle 12 — Focus: 力 (introduces 横折钩 compound stroke)

## Phase 1.5  /  MMH stroke count: 2

## Strokes
1. heng_zhe_gou(from=("ML", 0.36, 0.96), corner=("C", 0.97, 0.66), to=("BC", 0.94, 1.0))
   head (-114, 4), corner (47, -16), tail (-6, -150). NEW PRIMITIVE.
2. pie(from=("TC", 0.36, 0.37), to=("BL", 0.96, 1.34))
   head (-14, 113), tail (-154, -184). Reuse mastered.

## Joints: 1 ⇆ 2 @ C.

## NEW PRIMITIVE: 横折钩 — horizontal + downward bend + short hook (left-up)

```python
def w_main(s):
    if s < 0.10: return 14.0 - (s/0.10)*3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*2.0

def w_hook(s): return 13.0 - s*10.0

def draw_heng_zhe_gou(t, fa, ca, ta):
    p0 = anchor_to_xy(fa); pc = anchor_to_xy(ca); p3 = anchor_to_xy(ta)
    # Segment A: head→corner (horizontal with slight downward slope at end)
    a1 = (p0[0] + (pc[0]-p0[0])*0.33, p0[1] + (pc[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (pc[0]-p0[0])*0.67, p0[1] + (pc[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, pc, w_main, samples=180)
    # Segment B: corner→tail (downward then small left hook)
    b1 = (pc[0] + (p3[0]-pc[0])*0.4, pc[1] + (p3[1]-pc[1])*0.4)
    b2 = (pc[0] + (p3[0]-pc[0])*0.75, pc[1] + (p3[1]-pc[1])*0.75)
    brushed_bezier(t, pc, b1, b2, p3, w_hook, samples=160)
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
from pie import draw_pie

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(90)

def w_main(s):
    if s < 0.10: return 14.0 - (s/0.10)*3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*2.0

def w_hook(s): return 13.0 - s*10.0

def draw_heng_zhe_gou(t, fa, ca, ta):
    p0 = anchor_to_xy(fa); pc = anchor_to_xy(ca); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (pc[0]-p0[0])*0.33, p0[1] + (pc[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (pc[0]-p0[0])*0.67, p0[1] + (pc[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, pc, w_main, samples=180)
    b1 = (pc[0] + (p3[0]-pc[0])*0.4, pc[1] + (p3[1]-pc[1])*0.4)
    b2 = (pc[0] + (p3[0]-pc[0])*0.75, pc[1] + (p3[1]-pc[1])*0.75)
    brushed_bezier(t, pc, b1, b2, p3, w_hook, samples=160)

def task_01(t, screen):
    reset(t)
    draw_heng_zhe_gou(t, ("ML", 0.36, 0.96), ("C", 0.97, 0.66), ("BC", 0.94, 1.0))
    draw_pie(t, ("TC", 0.36, 0.37), ("BL", 0.96, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_力.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```
