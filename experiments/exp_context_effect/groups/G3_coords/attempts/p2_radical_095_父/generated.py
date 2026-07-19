# p2_radical_095_父 — G3 coord-bank attempt (revision 2).
#
# Revision reason: attempt 1 was too tall and narrow. GT of 父 is a wide
# X: big 撇 sweeps far left, big 捺 sweeps far right, both quite diagonal.
# The bank pie/na primitives at scale 0.85 rendered as too-vertical
# because their chord aspect (60px wide, 175px tall) doesn't match 父's
# X arms (~130px wide × 145px tall each). Per TR8, inline-fresh both
# big strokes as tapered beziers with hand-picked endpoints.
#
# 父 = 4 strokes:
#   1. Top-left short 撇 (inline-fresh, tapered bezier)
#   2. Top-right short 点 (inline-fresh, drop shape)
#   3. Big 撇: head upper-mid-right, tail lower-left corner
#   4. Big 捺: head upper-mid-left, tail lower-right corner
# Strokes 3 & 4 cross in an X around canvas y=185 PIL.
#
# Endpoints in PIL 300x300 coords (top-left origin):
#   Top-left 撇: (135, 82) head → (95, 135) tail (short, diagonal)
#   Top-right 点: (178, 88) head → (212, 122) tail (short, drop)
#   Big 撇:      (180, 118) head → (55, 268) tail (long, wide sweep)
#   Big 捺:      (120, 118) head → (248, 268) tail (long, wide sweep)
# Big 撇 and big 捺 heads are ~30px apart at top; they cross at approx
# (150, 180) PIL. The two top short strokes sit ABOVE the X arms with
# small visual gap (matches GT — top strokes are visually detached).

import os
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
CANVAS_SIZE = 300


def _tapered_bezier(draw, x0, y0, x1, y1,
                    ctrl_offset_perp=0.0, ctrl_offset_along=0.0,
                    w_head=8, w_tail=1, belly_pos=1.0, w_belly=None,
                    n_segments=60):
    """Tapered stroke rendered as a quadratic bezier.
    Args in PIL pixel coords. `ctrl_offset_perp` bows the curve
    perpendicular to chord (positive = right of travel dir).
    If w_belly is given and belly_pos<1, uses a two-phase width profile
    (head→belly→tail) — for 捺-like strokes."""
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    dx = x1 - x0
    dy = y1 - y0
    length = max(1e-6, (dx * dx + dy * dy) ** 0.5)
    # unit chord vector
    ux = dx / length
    uy = dy / length
    # perpendicular (right of travel)
    nx = -uy
    ny = ux
    cx = mx + nx * ctrl_offset_perp + ux * ctrl_offset_along
    cy = my + ny * ctrl_offset_perp + uy * ctrl_offset_along

    prev = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        if w_belly is not None and belly_pos < 1.0:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_fu(draw):
    """父 = short 撇 + short 点 (top) + big 撇 + big 捺 (crossing X)."""
    # ---- Stroke 1: top-left short 撇 -------------------------------
    # Head upper (135,82), tail lower-left (95,135). Slight left bow.
    # Travel dir is down-left, "right of travel" points down-right, so
    # negative perp bows the curve up-left (concave underside).
    _tapered_bezier(draw, 135, 82, 95, 135,
                    ctrl_offset_perp=-5,
                    w_head=6, w_tail=1, n_segments=35)

    # ---- Stroke 2: top-right short 点 (drop / down-right slash) ------
    # Thin head (178,88), fat tail (210,122). Slight right bow.
    _tapered_bezier(draw, 178, 88, 210, 122,
                    ctrl_offset_perp=3,
                    w_head=2, w_tail=8, n_segments=30)

    # ---- Stroke 3: big 撇 (upper-mid-right → lower-left) -------------
    # Head at (180,118), tail at (55,268). Chord is 125 wide, 150 tall.
    # Pie primitive-style: thick head → tapered tail, slight leftward
    # bow (concave right).
    _tapered_bezier(draw, 180, 118, 55, 268,
                    ctrl_offset_perp=-8,
                    w_head=9, w_tail=1, n_segments=70)

    # ---- Stroke 4: big 捺 (upper-mid-left → lower-right) -------------
    # Head at (120,118), tail at (248,268). Chord 128 wide, 150 tall.
    # Classic na width profile: thin head → belly at u=0.72 → tapered
    # tail. Slight rightward bow (concave left).
    _tapered_bezier(draw, 120, 118, 248, 268,
                    ctrl_offset_perp=8,
                    w_head=2, w_tail=3, belly_pos=0.72, w_belly=15,
                    n_segments=70)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_fu(draw)
    out_path = os.path.join(_HERE, "01_父.png")
    img.save(out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
