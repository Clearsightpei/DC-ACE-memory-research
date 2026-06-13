# Cycle 2 — Focus: 丨 (the shu atomic stroke)

## Phase
1 — atomic stroke mastery.

## MMH stroke count
1

## Target character
丨 (gǔn) — a single vertical stroke. MMH GT at `ground_truths/cycle_2/01_丨.png`.

## Strokes
1. shu(from=("V_mid", "H_top"), to=("V_mid", "H_bot"))

## Joints
None.

## Eval gates
- Stroke count: must equal 1.
- Anchor placement: within 30 px atomic-stroke tolerance.
- visual_score: informational.
- Curator vision: informational.

## Required brushwork (atomic stroke c2 — establishes the canonical shu)

Write `draw_shu` INLINE in `generated.py`. Pattern parallels heng but vertical:

- **Centerline**: cubic Bézier from start to end. Tiny horizontal sway is OK; basically straight.
- **Width profile** along s ∈ [0, 1]:
  - s ∈ [0.00, 0.10] entry press: 16 → 11
  - s ∈ [0.10, 0.80] shaft: ~11
  - s ∈ [0.80, 1.00] closing press: 11 → 18  (垂露 — heavy bottom press)
- Reuse `brushed_bezier` from `success_bank/code/heng.py` (now available — c1 mastered).

The bottom is the heaviest (垂露 droplet). If the top is heaviest, that's wrong direction.

## Output
`attempts/cycle_2/generated.py`, `attempts/cycle_2/01_丨.png`. Exactly ONE `draw_shu(...)` call in `task_01()`.

## Code skeleton

```python
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import brushed_bezier   # mastered c1, now reusable

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(90)

def w_shu(s):
    if s < 0.10: return 16.0 - (s/0.10) * 5.0
    if s < 0.80: return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 7.0

def draw_shu(t, from_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor); p3 = anchor_to_xy(to_anchor)
    p1 = (p0[0] + (p3[0]-p0[0]) * 0.33, p0[1] + (p3[1]-p0[1]) * 0.33)
    p2 = (p0[0] + (p3[0]-p0[0]) * 0.67, p0[1] + (p3[1]-p0[1]) * 0.67)
    brushed_bezier(t, p0, p1, p2, p3, w_shu, samples=220)

def task_01(t, screen):
    reset(t)
    draw_shu(t, ("V_mid", "H_top"), ("V_mid", "H_bot"))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_丨.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```
