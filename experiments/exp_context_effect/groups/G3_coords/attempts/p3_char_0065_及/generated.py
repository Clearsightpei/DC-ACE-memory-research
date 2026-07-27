# p3_char_0065_及 — G3 attempt (revised).
# Revision notes vs attempt 1:
#   - Top hook (横折折撇) was too small & floated above the body. Enlarge it,
#     lower it, and extend its final descending sweep so it visually merges
#     with the main 撇.
#   - Main 撇 was too straight; add more bow.
#   - 捺 tail was too short; extend it wider and longer to lower-right, per GT.
#   - Reduce weld u so na starts higher on the pie shaft (GT shows na begins
#     near mid-upper of pie).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import (  # noqa: E402
    variant_pie, variant_na, tapered_bezier, tapered_line, to_px, kiss_apex,
)

CANVAS = 300


def draw_ji_char_2(draw):
    """及 — 3 strokes."""
    # ---- Stroke 1: 撇 (long left-descending arm) ----
    # Head near upper-mid; tail far lower-left. More bow for calligraphic curve.
    pie_head = (+10, +70)
    pie_tail = (-105, -105)
    bow_pie = -14.0

    # ---- Stroke 3: 捺 tail (for kiss_apex calc) ----
    na_tail = (+115, -105)

    # Weld: na starts ~25% down pie shaft (higher intersection, per GT).
    pie_h_used, na_head = kiss_apex(pie_head, pie_tail, na_tail,
                                    u_pie=0.28, bow_pie=bow_pie)

    # Draw main 撇 (thick head → thin tail)
    variant_pie(draw, head=pie_h_used, tail=pie_tail,
                bow_perp=bow_pie, w_head=7.0, w_tail=2.0)

    # ---- Stroke 2: 横折折撇 (top hook) ----
    # Larger, positioned lower/wider so it sits atop the body.
    # Segment A: horizontal top going right.
    A_start = (-55, +115)
    A_end = (+65, +118)
    # Segment B: sharp turn down (short slant down-left).
    B_end = (+50, +85)
    # Segment C: small right-down piece (second fold).
    C_end = (+65, +65)
    # Segment D: final descending 撇 — sweep down-left to meet main body.
    D_end = (-15, +5)

    # A (heng)
    tapered_line(draw, A_start, A_end, 6, 6)
    cx, cy = to_px(*A_end)
    draw.ellipse([cx - 4, cy - 4, cx + 5, cy + 5], fill=(0, 0, 0))
    # B (short slant down-left)
    tapered_line(draw, A_end, B_end, 6, 5)
    cx, cy = to_px(*B_end)
    draw.ellipse([cx - 3, cy - 3, cx + 4, cy + 4], fill=(0, 0, 0))
    # C (short right-down)
    tapered_line(draw, B_end, C_end, 5, 5)
    cx, cy = to_px(*C_end)
    draw.ellipse([cx - 3, cy - 3, cx + 4, cy + 4], fill=(0, 0, 0))
    # D (final 撇 sweep — long tapered bezier, curving left)
    # Control point pulls the curve left and down.
    ctrl_D = ((C_end[0] + D_end[0]) / 2 - 15,
              (C_end[1] + D_end[1]) / 2 + 10)
    tapered_bezier(draw, C_end, ctrl_D, D_end, w_head=5, w_tail=2)

    # ---- 捺 last (on top of the pie crossing) ----
    variant_na(draw, head=na_head, tail=na_tail, bow_perp=+10.0,
               w_head=2.0, w_belly=12.0, w_tail=2.5, belly_u=0.72)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ji_char_2(draw)
    out = os.path.join(os.path.dirname(__file__), "01_及.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
