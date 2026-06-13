# Cycle 30 — Focus: 里 (Phase 2)

## MMH stroke count: 7

## Strokes (anchors from MMH measurement)
1. heng: ['TL', 0.416, 0.684] → ['ML', 0.9, 1.0]
2. shu: ['TL', 0.62, 0.696] → ['MR', 0.14, 0.956]
3. heng_zhe: ['C', 0.044, 0.308] → ['C', 0.956, 0.204]
4. heng: ['ML', 0.972, 0.82] → ['C', 0.992, 0.716]
5. shu: ['TC', 0.296, 0.756] → ['BC', 0.364, 1.064]
6. heng: ['BL', 0.76, 0.52] → ['BR', 0.216, 0.396]
7. heng: ['BL', -0.08, 1.28] → ['BR', 1.22, 1.16]

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
    draw_heng(t, ('TL', 0.416, 0.684), ('ML', 0.9, 1.0))
    draw_shu(t, ('TL', 0.62, 0.696), ('MR', 0.14, 0.956))
    draw_heng_zhe(t, ('C', 0.044, 0.308), ('C', 0.86, 0.18), ('C', 0.956, 0.204))
    draw_heng(t, ('ML', 0.972, 0.82), ('C', 0.992, 0.716))
    draw_shu(t, ('TC', 0.296, 0.756), ('BC', 0.364, 1.064))
    draw_heng(t, ('BL', 0.76, 0.52), ('BR', 0.216, 0.396))
    draw_heng(t, ('BL', -0.08, 1.28), ('BR', 1.22, 1.16))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_里.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```

EXACTLY 7 top-level draw calls in task_01.
