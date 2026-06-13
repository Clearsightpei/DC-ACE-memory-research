# Cycle 3 — Focus: 丿 (the pie atomic stroke)

## Phase
1 — atomic stroke mastery.

## MMH stroke count
1

## Target
丿 (piě) — a single down-left diagonal sweep. MMH GT at `ground_truths/cycle_3/01_丿.png`.

## Strokes
1. pie(from=("TC", 0.5, 0.5), to=("BL", 0.0, 0.5))

  Anchor xy: from ≈ (0, +100), to ≈ (-150, -100). 250 px diagonal sweep.

## Joints
None.

## Required brushwork (atomic c3 — establishes the canonical pie)

撇 is the first **tapered-tip** stroke. Pattern:
- Centerline: cubic Bezier from start to end. Concave-down arc (control points sit ABOVE the chord by ~5-10 px) — the 撇 dips slightly.
- Width profile (s ∈ [0, 1]):
  - [0.00, 0.10] head dunbi: 18 → 14
  - [0.10, 0.85] shaft:      14 → 11
  - [0.85, 1.00] tail taper: 11 → 3   (fine tip — the `max(3, …)` floor kicks in)
- ~240 samples.

The TAIL is the thinnest point (a tapered tip). The HEAD is the heaviest. This is the OPPOSITE of 横 (where tail is heaviest).

Reuse `brushed_bezier` from `heng.py`.

## Output
`attempts/cycle_3/generated.py` + `attempts/cycle_3/01_丿.png`. Exactly ONE `draw_pie(...)` call.

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

def w_pie(s):
    if s < 0.10: return 18.0 - (s/0.10) * 4.0
    if s < 0.85: return 14.0 - ((s-0.10)/0.75) * 3.0
    return 11.0 - ((s-0.85)/0.15) * 8.0

def draw_pie(t, from_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor); p3 = anchor_to_xy(to_anchor)
    # Concave-down arc: control points BELOW the chord by ~10 px (in math y = +10)
    p1 = (p0[0] + (p3[0]-p0[0]) * 0.33, p0[1] + (p3[1]-p0[1]) * 0.33 + 10)
    p2 = (p0[0] + (p3[0]-p0[0]) * 0.67, p0[1] + (p3[1]-p0[1]) * 0.67 + 10)
    brushed_bezier(t, p0, p1, p2, p3, w_pie, samples=240)

def task_01(t, screen):
    reset(t)
    draw_pie(t, ("TC", 0.5, 0.5), ("BL", 0.0, 0.5))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_丿.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```
