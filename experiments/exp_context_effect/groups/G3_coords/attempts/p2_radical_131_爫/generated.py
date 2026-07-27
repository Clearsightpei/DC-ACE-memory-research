# p2_radical_131_爫 — G3 attempt.
# 爫 (zhao) = "claw" radical top-form. 4 strokes:
#   1) leftmost short 撇 (long-ish slash down-left)
#   2) short 撇 (steep, middle)
#   3) short 撇 (steep, right-of-middle)
#   4) top 横撇 (heng turning into pie down-left) — the "roof" that
#      connects rightward and hooks down at right end
#
# GT shows a compact cluster occupying roughly upper-center of the
# canvas (y~140-200 PIL, x~80-220 PIL). Small, upper-band radical.
#
# Approach: inline PIL for all four strokes using math coords
# (center origin, +y up per P5). Use variant_pie from
# _shared_helpers for the three descending 撇.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_HELPERS_DIR = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _HELPERS_DIR not in sys.path:
    sys.path.insert(0, _HELPERS_DIR)

from _shared_helpers import variant_pie, tapered_bezier, to_px  # noqa: E402

CANVAS = 300
OUT_PNG = os.path.join(_HERE, "01_爫.png")


def draw_zhao_top(draw):
    """Render 爫 (claw-top radical). All coords in math convention:
    center=(150,150) PIL, +y up.

    Cluster sits upper-center; roughly y in [+15, +55], x in [-55, +55]."""

    # Stroke 4 first for layering (top 横撇 — will be drawn AFTER pies
    # so it sits on top, but math-wise we can draw in any order).

    # Cluster tightened: GT is smaller/looser than first pass. Reduce
    # overall footprint; top bar is a short arched cap (not a strong
    # horizontal), and the descending pies are shorter and less regular.

    # ---- Stroke 1: leftmost 撇 (longest, most slanted, lower-left) ----
    # Head at (-18, +30), tail at (-38, +8). Softish curve.
    variant_pie(
        draw,
        head=(-18, +30),
        tail=(-38, +8),
        bow_perp=-2.5,
        w_head=6.0,
        w_tail=1.5,
    )

    # ---- Stroke 2: middle short 撇 ----
    # Head at (0, +32), tail at (-10, +12). Short, steep.
    variant_pie(
        draw,
        head=(0, +32),
        tail=(-10, +12),
        bow_perp=-2.0,
        w_head=5.5,
        w_tail=1.2,
    )

    # ---- Stroke 3: right short 撇 ----
    # Head at (+18, +32), tail at (+10, +12). Short, steep.
    variant_pie(
        draw,
        head=(+18, +32),
        tail=(+10, +12),
        bow_perp=-2.0,
        w_head=5.5,
        w_tail=1.2,
    )

    # ---- Stroke 4: top 横撇 — short arched cap turning down-right ----
    # In the GT this is a short arched curve above the descenders,
    # peaking mid, with a short hook down on the right end.
    # Segment A: gentle arch from (-22, +42) to (+22, +46)
    tapered_bezier(
        draw,
        p0=(-22, +42),
        p1=(0, +52),         # arch peak
        p2=(+22, +46),
        w_head=4.5,
        w_tail=5.5,
        n=40,
    )
    # Small corner blob (顿笔) at the right turn
    cx, cy = to_px(+22, +46)
    r = 4
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # Segment B: short pie tail from corner down to (~(+15, +30))
    variant_pie(
        draw,
        head=(+22, +46),
        tail=(+15, +30),
        bow_perp=-1.0,
        w_head=5.5,
        w_tail=1.2,
    )


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_zhao_top(draw)
    img.save(OUT_PNG)
    print(f"Wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
