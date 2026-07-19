# p2_radical_012_冫 — G3 coord-bank drawer attempt (revision 1)
# 冫 = 点 (top) + 提 (bottom). "Two-drop water" radical, left half.
#
# Revision reasoning after first pass:
#   Pass 1 used two dian primitives. The top dian looked correct
#   (upper-center small dot slanting down-right). The bottom dian was
#   too centered and slanted down-right, but the GT's bottom stroke
#   slants DOWN-LEFT with a small upward flick at the tail (a 提 form).
#   Per TR5, dian's built-in orientation is wrong for the bottom stroke
#   — inline a custom stroke rather than force-transform dian.
#
# Revised layout (300x300 PIL, center=(150,150), math coords via _to_pixel):
#   Top 点 (reuse dian primitive): center ≈ (150, 105), small.
#     dian default center (150,150) → target (150,105). ox=0, oy=+45,
#     scale=0.55.
#   Bottom stroke (inlined 提-like curve):
#     - starts thin at upper-right (~x=155, y=170), curves down-left
#       thickening, ends at lower-left (~x=115, y=225) with a small
#       upward-right flick.
#     - modeled as a quadratic bezier with widening taper then a small
#       hook segment appended.

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from dian import draw_dian  # noqa: E402


def _px(ox, oy):
    return 150 + ox, 150 - oy


def draw_bottom_stroke(t):
    """冫's bottom stroke: down-left slanting curve with upward-right flick.

    Math-coord endpoints:
      head (thin) at (+5, -20)  →  PIL (155, 170)
      tail-body end at (-35, -75)  →  PIL (115, 225)
      hook tip at (-25, -68)   →  PIL (125, 218) (small up-right flick)
    Thickness ramps from 3 (head) → 15 (tail body).
    """
    x0, y0 = 5.0, -20.0
    x1, y1 = -35.0, -75.0
    # Control point pulled slightly right of the chord to bow the curve
    # gently outward (left-belly for a natural water-drop feel).
    mx = (x0 + x1) / 2.0 + 2.0
    my = (y0 + y1) / 2.0 + 3.0

    n_segments = 40
    th_head = 3.0
    th_tail = 15.0

    prev_pt = None
    tail_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _px(bx, by)
        w = th_head * (1 - u) + th_tail * u
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)
        tail_pt = (px, py)

    # Small upward-right hook flick from the tail (~10 px, tapering thin)
    hook_end = _px(-25.0, -68.0)
    n_hook = 10
    for i in range(1, n_hook + 1):
        u = i / n_hook
        hx = tail_pt[0] + (hook_end[0] - tail_pt[0]) * u
        hy = tail_pt[1] + (hook_end[1] - tail_pt[1]) * u
        w = 10.0 * (1 - u) + 2.0 * u
        w_int = max(1, int(round(w)))
        prev = (
            tail_pt
            if i == 1
            else (
                tail_pt[0] + (hook_end[0] - tail_pt[0]) * ((i - 1) / n_hook),
                tail_pt[1] + (hook_end[1] - tail_pt[1]) * ((i - 1) / n_hook),
            )
        )
        t.line([prev, (hx, hy)], fill=(0, 0, 0), width=w_int)
        r = w / 2.0
        t.ellipse([hx - r, hy - r, hx + r, hy + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Top 点 (reuse dian primitive; TR1: deliberate placement)
    # dian default center (150,150) → target (150,105). ox=0, oy=+45.
    draw_dian(t, ox=0, oy=45, scale=0.55)

    # Bottom stroke: inlined 提-form because dian's built-in slant is
    # down-right, but 冫's bottom must slant down-left with an up-right
    # hook (TR5 — inline instead of force-transform).
    draw_bottom_stroke(t)

    out = Path(__file__).parent / "01_冫.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
