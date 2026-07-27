# p3_char_0093_弋 (yì) — G3 first attempt
#
# 3 strokes: 横 (short heng, upper-middle) + 斜钩 (long xie-gou
# dominant, sweeping down-right with belly and up-right hook) +
# 点 (dian, upper-right above the heng).
#
# Radical 弋 was in errata (斜钩 lost its belly). Fix per errata:
# inline the 斜钩 as a strong-bow bezier so the belly is preserved.
# Heng crosses the 斜钩 shaft in the upper-mid region. Dian sits
# above-right of the heng end.
#
# Math coord convention (P5): center origin at (150, 150), +y up.

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SB = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
if SB not in sys.path:
    sys.path.insert(0, SB)

from _shared_helpers import tapered_bezier, tapered_line, to_px  # noqa: E402

CANVAS = 300


def draw_yi_ge(t=None, ox=0, oy=0, scale=1.0):
    """Render 弋 into a fresh PIL image and return it."""
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # ----- Stroke 1: 横 (heng) — short horizontal, upper-middle.
    # GT: spans roughly x=-55 to x=+45 at y ~ +12. Slight rise
    # (right-end lifts). Widths ~ 4 px (MMH-thin per P12).
    tapered_line(
        draw,
        (-58 + ox, 12 + oy),
        (48 + ox, 20 + oy),
        4, 4,
    )

    # ----- Stroke 2: 斜钩 (xie-gou) — the dominant stroke.
    # Starts high-left (near where heng crosses it), sweeps down
    # and right with a pronounced belly (bow to the right/down),
    # then hooks up-right at the bottom. Inline as bezier for the
    # bow, then a short hook line segment.
    # GT read: start ~ (-35, +55), belly control ~ (+35, -35),
    # end (before hook) ~ (+45, -95). Hook goes up-right to
    # ~ (+70, -80).
    tapered_bezier(
        draw,
        (-35 + ox, 55 + oy),   # p0 (top-left start)
        (25 + ox, -30 + oy),   # p1 (control — pushes belly out to lower-right)
        (48 + ox, -95 + oy),   # p2 (end at bottom)
        w_head=4, w_tail=5,
        n=64,
    )
    # Hook: from p2 up and to the right.
    tapered_line(
        draw,
        (48 + ox, -95 + oy),
        (72 + ox, -78 + oy),
        5, 3,
    )

    # ----- Stroke 3: 点 (dian) — small dot at upper right, above
    # the right end of the heng. GT shows a short down-right stroke.
    tapered_line(
        draw,
        (32 + ox, 60 + oy),
        (48 + ox, 45 + oy),
        3, 6,
    )

    return img


if __name__ == "__main__":
    img = draw_yi_ge()
    out = os.path.join(HERE, "01_弋.png")
    img.save(out)
    print(f"wrote {out}")
