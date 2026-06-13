# Cycle 26 — Focus: 中 (Phase 2)

## MMH stroke count: 4

## Strokes (anchors from MMH measurement)
1. shu: ['ML', 0.228, 0.156] → ['BL', 0.632, 0.256]
2. heng_zhe: ['ML', 0.5, 0.184] → ['MR', 0.26, 0.764]
3. heng: ['BL', 0.716, 0.148] → ['MR', 0.524, 0.956]
4. shu: ['TC', 0.248, 0.256] → ['BC', 0.448, 1.588]

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
from heng_zhe import draw_heng_zhe
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
    draw_shu(t, ('ML', 0.228, 0.156), ('BL', 0.632, 0.256))
    draw_heng_zhe(t, ('ML', 0.5, 0.184), ('TR', 0.416, 0.996), ('MR', 0.26, 0.764))
    draw_heng(t, ('BL', 0.716, 0.148), ('MR', 0.524, 0.956))
    draw_shu(t, ('TC', 0.248, 0.256), ('BC', 0.448, 1.588))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_中.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```

EXACTLY 4 top-level draw calls in task_01.
