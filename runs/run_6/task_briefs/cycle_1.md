# Cycle 1 — Focus: 一 (the heng atomic stroke)

## Phase
1 — atomic stroke mastery.

## MMH stroke count
1

## Target character
一 (yī, "one") — a single horizontal stroke. MMH GT at `ground_truths/cycle_1/01_一.png`.

## Anchors (from MMH measurement)
The MMH median for 一's single stroke runs:
- **head** ≈ turtle math-coord `(-156, -48)` — left end, slightly below center.
- **tail** ≈ turtle math-coord `(163, -44)` — right end, slightly below center.

For your brief, use the cell-relative form `(ML, 0.06, 0.97)` (translated from (-156, -48)) for the head and `(MR, 1.13, 0.94)` for the tail — *or* use the simpler axis intersection `(V_left, H_mid)` → `(V_right, H_mid)`, which gives `(-150, 0) → (150, 0)`. The 30-px atomic-stroke tolerance accommodates the small offset.

For c1, you may use simpler axis form for clarity: heng from `(V_left, H_mid)` to `(V_right, H_mid)`.

## Strokes
1. heng(from=("V_left", "H_mid"), to=("V_right", "H_mid"))

## Joints
None (1-stroke character).

## Eval gates
- **Stroke count**: must equal 1 (one top-level draw call inside `task_01()`).
- **OCR** (informational): should identify as 一.
- **visual_score** (informational): cross-renderer, typically ≤ 0.9 with brushwork.
- **3-judge panel**: hard gate — unanimous YES required.
- **Curator vision**: informational.

## Self-preview budget
Max 2 iterations. Render → open your PNG and the GT PNG with Read → check the stroke is a clean horizontal line spanning the central horizontal axis with proper brushwork (entry-press, modest shaft, closing-press heavier).

## Required brushwork (atomic stroke c1 — establishes the canonical heng)

Since the Success Bank is empty (only `_anchor.py` is there as a helper), you write the `draw_heng` primitive INLINE in `generated.py`. Use:

- **Centerline**: cubic Bézier from start anchor to end anchor with control points at the 1/3 and 2/3 marks. A slight upward arc (control y > endpoint y by ~5) is the 楷书 convention.
- **Width profile** along arc-length s ∈ [0, 1]:
  - s ∈ [0.00, 0.10]: entry press `16 → 11` (dunbi)
  - s ∈ [0.10, 0.85]: shaft `~11`
  - s ∈ [0.85, 1.00]: closing press `11 → 19` (heaviest)
- **Per-sample pen** (~220 samples): `t.pensize(max(3, w(s))); t.goto(x, y)` — the `max(3, …)` floor is non-negotiable.

The closing-press at the right end is the diagnostic feature of a 楷书 横 — it must be visibly heavier than the entry. If your render's right end is the THINNEST point, the rubric fails.

## Output

`attempts/cycle_1/generated.py` with `task_01()` calling exactly **one** top-level `draw_heng(...)`. PNG saved to `attempts/cycle_1/01_一.png`.

## Code skeleton

```python
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy   # the only file in success_bank/code so far

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(90)

# INLINE primitive — this is what the Curator will promote on success.
def brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=220):
    t.penup(); t.goto(P0); t.pendown()
    for i in range(samples + 1):
        s = i / samples
        x = ((1-s)**3 * P0[0] + 3*(1-s)**2 * s * P1[0]
             + 3*(1-s) * s*s * P2[0] + s**3 * P3[0])
        y = ((1-s)**3 * P0[1] + 3*(1-s)**2 * s * P1[1]
             + 3*(1-s) * s*s * P2[1] + s**3 * P3[1])
        t.pensize(max(3, w_profile(s)))
        t.goto(x, y)
    t.penup()

def w_heng(s):
    if s < 0.10: return 16.0 - (s / 0.10) * 5.0
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 8.0

def draw_heng(t, from_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor)
    p3 = anchor_to_xy(to_anchor)
    # gentle upward bow
    p1 = (p0[0] + (p3[0]-p0[0]) * 0.33, p0[1] + (p3[1]-p0[1]) * 0.33 + 4)
    p2 = (p0[0] + (p3[0]-p0[0]) * 0.67, p0[1] + (p3[1]-p0[1]) * 0.67 + 4)
    brushed_bezier(t, p0, p1, p2, p3, w_heng, samples=220)

def task_01(t, screen):
    reset(t)
    draw_heng(t, ("V_left", "H_mid"), ("V_right", "H_mid"))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_一.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
```

Adapt as you see fit (refine the width profile, adjust the bow, etc.) — but `task_01` must contain exactly ONE top-level `draw_heng(...)` call.
