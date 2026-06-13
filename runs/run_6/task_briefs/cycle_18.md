# Cycle 18 — Focus: 工 (Phase 2)

## MMH stroke count: 3

## Strokes (anchors from MMH measurement)
1. heng: ['ML', 0.636, 0.012] → ['TR', 0.528, 0.84]
2. shu: ['C', 0.392, 0.12] → ['BC', 0.42, 0.668]
3. heng: ['BL', -0.124, 0.856] → ['BR', 1.244, 0.84]

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
from shu import draw_shu

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
    draw_heng(t, ('ML', 0.636, 0.012), ('TR', 0.528, 0.84))
    draw_shu(t, ('C', 0.392, 0.12), ('BC', 0.42, 0.668))
    draw_heng(t, ('BL', -0.124, 0.856), ('BR', 1.244, 0.84))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_工.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```

EXACTLY 3 top-level draw calls in task_01.
