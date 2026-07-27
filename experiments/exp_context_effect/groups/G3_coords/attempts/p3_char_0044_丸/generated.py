# p3_char_0044_丸 — 丸 (wan, "pellet"), 3 strokes.
# Structure: 丸 = 九 + inner 丶.
#   Stroke 1: short 撇 at top — from upper-mid down-left, short.
#   Stroke 2: 横斜钩 body — starts near top-right end of the 撇 (or top-mid),
#             goes right briefly as a short 横, then dives down and left,
#             curves along the bottom, ends with an upward hook. This is a
#             single continuous stroke (横斜钩 variant, as in 九).
#   Stroke 3: 点 inside, upper-right region.
#
# Revised (self-check pass): first attempt's body was too closed (like a
# "6"); GT shows the top must start with a short 横 leaning down-right
# before diving into the sweeping arc. Also the dot was too heavy.
#
# Math convention: center origin (150,150), +y up.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import (variant_pie, variant_dian, tapered_bezier,  # noqa
                             to_px, tapered_line)

CANVAS = 300


def draw_wan(draw, ox=0.0, oy=0.0, scale=1.0):
    """丸 = short 撇 (top) + main 横斜钩 body + inner 点."""

    # --- Stroke 1: short 撇 at the top ---
    # From upper-mid (a little right of center) down-and-left, short/steep.
    pie_head = (ox + 5.0 * scale, oy + 95.0 * scale)
    pie_tail = (ox - 40.0 * scale, oy + 45.0 * scale)
    variant_pie(draw, head=pie_head, tail=pie_tail,
                bow_perp=-3.0, w_head=7.0, w_tail=2.0)

    # --- Stroke 2: 横斜钩 body (single continuous stroke) ---
    # Piece (a): short top 横 leaning down-right, from just above the pie
    # head across to the upper-right area.
    heng_start = (ox - 5.0 * scale, oy + 78.0 * scale)
    heng_end = (ox + 78.0 * scale, oy + 55.0 * scale)
    tapered_line(draw, heng_start, heng_end, w0=7.0, w1=8.0, n=20)

    # Piece (b): long diving arc from the top-right end down and left,
    # sweeping along the bottom-left back to the right. Model as one
    # long bezier with control pulled far to the lower-left.
    arc_start = heng_end
    arc_ctrl = (ox - 130.0 * scale, oy - 40.0 * scale)
    arc_end = (ox + 55.0 * scale, oy - 85.0 * scale)
    tapered_bezier(draw, arc_start, arc_ctrl, arc_end,
                   w_head=8.0, w_tail=9.0, n=64)

    # Piece (c): rightward extension along the bottom to the hook base.
    tail_ctrl = (ox + 82.0 * scale, oy - 88.0 * scale)
    tail_end = (ox + 92.0 * scale, oy - 60.0 * scale)
    tapered_bezier(draw, arc_end, tail_ctrl, tail_end,
                   w_head=9.0, w_tail=6.0, n=36)

    # Piece (d): upward hook — from tail_end up-and-slightly-left, tapered.
    hook_base = tail_end
    hook_tip = (ox + 72.0 * scale, oy - 32.0 * scale)
    tapered_line(draw, hook_base, hook_tip, w0=7.0, w1=1.5, n=16)

    # --- Stroke 3: inner 点 (small, upper-right) ---
    dian_head = (ox + 18.0 * scale, oy + 25.0 * scale)
    dian_tail = (ox + 38.0 * scale, oy + 2.0 * scale)
    variant_dian(draw, head=dian_head, tail=dian_tail,
                 w_head=2.0, w_tail=8.0, bow_perp=-2.0)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_wan(draw, ox=0.0, oy=0.0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_丸.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
