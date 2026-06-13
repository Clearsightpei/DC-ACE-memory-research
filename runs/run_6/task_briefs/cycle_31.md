# Cycle 31 — Focus: 横折提 (heng_zhe_ti) — compound stroke

## Phase
1.5 — compound stroke mastery.

## MMH stroke count
1 (a single compound stroke counted as one).

## Target
A 横折提 stroke drawn in isolation, large and centered in the 米字格. This stroke is used in the 讠 radical (计, 论). Shape: horizontal segment → corner-down → upper-right rising tail.

  ─┐
   ↗

## Strokes
1. heng_zhe_ti(
     from=("TL", 0.4, 0.3),
     c1  =("TR", 0.3, 0.3),
     c2  =("MR", 0.0, 0.7),
     to  =("MR", 0.7, 0.4)
   )

- `from` is the upper-left starting point of the heng.
- `c1` is the corner after the heng (top of the zhe).
- `c2` is the bottom of the zhe (where the ti begins).
- `to` is the tip of the ti (rising upper-right).

## Joints
None — single compound stroke.

## Eval gates
- **Stroke count**: must equal 1 (one `draw_heng_zhe_ti(...)` call inside `task_01`).
- **Anchor placement**: from + to must each be within 30 px of their declared anchor (atomic-stroke tolerance; compound interior corners c1/c2 not gated geometrically).
- **3-judge panel**: 3 fresh skeptics must each answer YES to "is this unambiguously a 横折提?"
- visual_score: informational.

## Required brushwork

Write `draw_heng_zhe_ti` INLINE in `generated.py`. The stroke is three Bézier segments stitched at c1 and c2:

- **Segment 1 (heng, from→c1)**: same width profile family as `draw_heng_zhe`'s w_main:
  - s ∈ [0, 0.10] entry press: 14 → 11
  - s ∈ [0.10, 0.85] shaft: 11
  - s ∈ [0.85, 1.00] closing arc: 11 → 13
- **Segment 2 (zhe, c1→c2)**: vertical drop, w_main-style:
  - s ∈ [0, 0.10] press: 13
  - s ∈ [0.10, 0.85] shaft: 11
  - s ∈ [0.85, 1.00] light closing: 11 → 12
- **Segment 3 (ti, c2→to)**: rising tapered, like an atomic 提:
  - linear taper from 14 at base → 3 at tip (the `max(3, ...)` floor in `brushed_bezier` handles the tail).

The visual signature of 横折提 vs 横折: the third segment RISES (positive slope upper-right) and TAPERS to a tip — like 提.

Reuse `brushed_bezier` from `success_bank/code/heng.py`.

## Output
- `attempts/cycle_31/generated.py`
- `attempts/cycle_31/01_heng_zhe_ti.png`

Exactly ONE `draw_heng_zhe_ti(...)` call in `task_01`.

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
    t.penup(); t.goto(0,0); t.setheading(0)

def w_heng_seg(s):
    if s < 0.10: return 14.0 - (s/0.10)*3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*2.0

def w_zhe_seg(s):
    if s < 0.10: return 13.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*1.0

def w_ti_seg(s):
    return 14.0 - s * 11.0

def draw_heng_zhe_ti(t, fa, c1a, c2a, ta):
    p0 = anchor_to_xy(fa)
    p1 = anchor_to_xy(c1a)
    p2 = anchor_to_xy(c2a)
    p3 = anchor_to_xy(ta)
    # heng
    a1 = (p0[0] + (p1[0]-p0[0])*0.33, p0[1] + (p1[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (p1[0]-p0[0])*0.67, p0[1] + (p1[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, p1, w_heng_seg, samples=160)
    # zhe
    b1 = (p1[0] + (p2[0]-p1[0])*0.33, p1[1] + (p2[1]-p1[1])*0.33)
    b2 = (p1[0] + (p2[0]-p1[0])*0.67, p1[1] + (p2[1]-p1[1])*0.67)
    brushed_bezier(t, p1, b1, b2, p2, w_zhe_seg, samples=160)
    # ti
    c1 = (p2[0] + (p3[0]-p2[0])*0.33, p2[1] + (p3[1]-p2[1])*0.33)
    c2 = (p2[0] + (p3[0]-p2[0])*0.67, p2[1] + (p3[1]-p2[1])*0.67)
    brushed_bezier(t, p2, c1, c2, p3, w_ti_seg, samples=140)

def task_01(t, screen):
    reset(t)
    draw_heng_zhe_ti(t,
        ("TL", 0.4, 0.3),
        ("TR", 0.3, 0.3),
        ("MR", 0.0, 0.7),
        ("MR", 0.7, 0.4))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_heng_zhe_ti.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```

Drawer: you may use this skeleton verbatim or tune control points / width profiles for cleaner brushwork. Do NOT change the anchor tuples — those are the gate.
