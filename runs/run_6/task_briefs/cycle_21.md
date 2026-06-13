# Cycle 21 — Focus: 大 (Phase 2)

## MMH stroke count: 3

## Strokes (anchors from MMH measurement)
1. heng: ['ML', 0.292, 0.716] → ['MR', 0.692, 0.48]
2. pie: ['TC', 0.116, 0.308] → ['BL', 0.004, 1.384]
3. na: ['C', 0.396, 0.828] → ['BR', 1.264, 1.38]

## Code skeleton

```python
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import draw_heng
from na import draw_na
from pie import draw_pie

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(90)

def task_01(t, screen):
    reset(t)
    draw_heng(t, ('ML', 0.292, 0.716), ('MR', 0.692, 0.48))
    draw_pie(t, ('TC', 0.116, 0.308), ('BL', 0.004, 1.384))
    draw_na(t, ('C', 0.396, 0.828), ('BR', 1.264, 1.38))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_大.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```

EXACTLY 3 top-level draw calls in task_01.
