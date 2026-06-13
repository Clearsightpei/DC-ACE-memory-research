# Cycle 4 — Focus: 丶 (the dian atomic stroke)

## Phase
1 — atomic stroke mastery.

## MMH stroke count
1

## Target
丶 (zhǔ) — a single dot/short stroke. MMH GT at `ground_truths/cycle_4/01_丶.png`.

## Strokes
1. dian(from=("C", 0.4, 0.3), to=("C", 0.65, 0.7))

  Anchor xy: from ≈ (-10, 20) to (15, -20). Small down-right dab, ~50 px diagonal.

## Joints
None.

## Required brushwork

点 = brief swelling dot, head fine → middle heavy → tail fine.

- Bezier with concave-down arc (control +5 in y).
- Width profile: head 3 → middle 14 → tail 3. Symmetric bell.
- ~120 samples (short stroke).

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

def w_dian(s):
    # symmetric bell: 3 → 14 → 3
    if s < 0.5: return 3.0 + (s / 0.5) * 11.0
    return 14.0 - ((s - 0.5) / 0.5) * 11.0

def draw_dian(t, from_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor); p3 = anchor_to_xy(to_anchor)
    p1 = (p0[0] + (p3[0]-p0[0]) * 0.33, p0[1] + (p3[1]-p0[1]) * 0.33 + 5)
    p2 = (p0[0] + (p3[0]-p0[0]) * 0.67, p0[1] + (p3[1]-p0[1]) * 0.67 + 5)
    brushed_bezier(t, p0, p1, p2, p3, w_dian, samples=120)

def task_01(t, screen):
    reset(t)
    draw_dian(t, ("C", 0.4, 0.3), ("C", 0.65, 0.7))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_丶.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```
