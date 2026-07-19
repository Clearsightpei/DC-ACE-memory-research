# p2_radical_043_川 — 川 (chuan, "river"), 3 strokes.
#
# GT observation: three vertical-ish strokes, left-to-right.
#   Left stroke:   撇-like curved scoop — starts upper-left, descends with slight
#                  leftward bow. Medium length. Tapered.
#   Middle stroke: short 竖 (uniform), starts a bit below the left stroke's top.
#   Right stroke:  long 竖 (uniform), tallest, extends lowest, starts near
#                  the middle stroke's top height.
#
# Approach: bank has draw_shu for the two verticals. The left stroke is a
# curved 撇-like scoop that's near-vertical (not diagonal), so pie primitive
# is TOO diagonal (see P10 in principle_bank) — INLINE (TR5) a shallow-scoop
# curved stroke instead.
#
# Placements (math coords, +y up, canvas 300x300, center = (150,150) px):
#   Left stroke  center: (-55, -5)   — spans y from +45 to -55, curves slightly left
#   Middle stroke:  ox=0, oy=-15, scale=0.55   (short 竖, length 110 px)
#   Right stroke:   ox=+55, oy=-20, scale=0.75 (long 竖, length 150 px)
# Rationale:
#   TR2: radical-standalone at scale ~1.0 total footprint; three strokes span
#        roughly 110 px wide (-55..+55) and ~150 px tall.
#   TR3: shu center-of-mass at ox chosen to place canvas-center of that shaft.
#   TR6: transforms noted in comments.

import os
import sys
from PIL import Image, ImageDraw

# Ensure success_bank/code is on path so we can import bank primitives.
BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from shu import draw_shu

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_left_curve(t, ox=0.0, oy=0.0, scale=1.0):
    """Inline the left curved stroke of 川. Near-vertical scoop with slight
    leftward bow, tapered slightly at the tail. Not a diagonal 撇 (P10).

    Canonical shape: head at (+5, +55), tail at (-8, -60). Control point
    pulled slightly left of the chord to bow the sweep.
    """
    x0, y0 = 5.0 * scale, 55.0 * scale     # upper-right-ish head
    x1, y1 = -8.0 * scale, -60.0 * scale   # lower-left tail
    mx = (x0 + x1) / 2.0 - 10.0 * scale    # left of chord midpoint
    my = (y0 + y1) / 2.0

    n_segments = 60
    w_head = max(1, 10.0 * scale)
    w_tail = max(1, 4.0 * scale)

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # LEFT stroke: curved scoop, inline (TR5 — pie primitive too diagonal for 川).
    # Head high-left, tail low with slight leftward bow.
    # Center-of-mass target: canvas x = 100, y = 155  ->  math (-50, -5)
    draw_left_curve(t, ox=-50, oy=-5, scale=1.0)

    # MIDDLE stroke: short 竖 (uniform vertical), scale 0.5 -> length 100 px.
    # In GT its top starts BELOW the left stroke's top and its bottom is above
    # the right stroke's bottom. Shift down to match GT proportions.
    # Center-of-mass target: canvas x = 150, y = 180  ->  math (0, -30).
    # TR6: draw_shu default center (150,150) -> target (150,180); ox=0, oy=-30, scale=0.5
    draw_shu(t, ox=0, oy=-30, scale=0.5)

    # RIGHT stroke: long 竖 (uniform vertical), scale 0.85 -> length 170 px.
    # Tallest of the three; extends lowest. Top slightly below the left head.
    # Center-of-mass target: canvas x = 205, y = 175  ->  math (+55, -25).
    # TR6: draw_shu default center (150,150) -> target (205,175); ox=+55, oy=-25, scale=0.85
    draw_shu(t, ox=+55, oy=-25, scale=0.85)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "01_川.png")
    img.save(out_path)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
