# p3_char_0144_风 — 风 (feng, "wind"), 4 strokes.
# Structure: outer envelope (撇 + 横斜钩) + inner 乂 (X: 撇 + 乀/点)
#
# Revision 1: original was too calligraphic/thick. GT (MMH) uses uniform
# thin lines (~4px). Reduced all widths, tightened inner X placement.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import (  # noqa: E402
    tapered_bezier,
    tapered_line,
    variant_pie,
    to_px,
)


def draw_feng(draw, ox=0, oy=0, scale=1.0):
    def P(x, y):
        return (ox + x * scale, oy + y * scale)

    W = 4  # uniform thin width per P12 / MMH GT convention

    # === Stroke 1: 撇 — left leg of envelope
    # Starts just under the top-left of the top-bar, curves down-left.
    tapered_bezier(
        draw,
        P(-40, +95), P(-65, 0), P(-100, -110),
        w_head=W + 1, w_tail=W - 1, n=60,
    )

    # === Stroke 2: 横斜钩 (horizontal + slanted descent + hook)
    # A. Top horizontal segment.
    tapered_line(
        draw,
        P(-40, +100), P(+85, +95),
        w0=W, w1=W, n=32,
    )
    # B. Slanted descent, slight rightward bow.
    tapered_bezier(
        draw,
        P(+85, +95), P(+100, 0), P(+105, -95),
        w_head=W, w_tail=W, n=60,
    )
    # C. Hook curve out lower right.
    tapered_bezier(
        draw,
        P(+105, -95), P(+118, -108), P(+128, -100),
        w_head=W, w_tail=W - 1, n=30,
    )
    # D. Small upward flick (钩).
    tapered_line(
        draw,
        P(+128, -100), P(+123, -78),
        w0=W - 1, w1=1, n=16,
    )

    # === Inner 乂 (X-shape) — positioned upper-center of interior
    # Both cross around (~0, -5).
    pie_head = P(+18, +45)
    pie_tail = P(-40, -60)
    na_head = P(-18, +45)
    na_tail = P(+40, -60)

    # Stroke 3: inner 撇
    variant_pie(
        draw,
        head=pie_head, tail=pie_tail,
        bow_perp=-3.0, w_head=W, w_tail=W - 2, n=40,
    )

    # Stroke 4: inner 乀 (na/dot)
    tapered_bezier(
        draw,
        na_head,
        ((na_head[0] + na_tail[0]) / 2 + 2,
         (na_head[1] + na_tail[1]) / 2 - 2),
        na_tail,
        w_head=W - 2, w_tail=W, n=40,
    )


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_feng(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_风.png")
    img.save(out)
    print(f"wrote {out}")
