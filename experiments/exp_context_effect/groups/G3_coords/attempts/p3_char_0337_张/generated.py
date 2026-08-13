# p3_char_0337_张 (zhāng) — 弓 (left) + 长 (right), 7 strokes.
#
# Bank has neither 弓 nor 长. Inlining fresh with PIL using math coords
# and _shared_helpers.py (variant_pie, variant_na, tapered_bezier,
# tapered_line, to_px). This is a fresh derivation (v8: bank is
# REFERENCE ONLY; trust GT).

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import (  # noqa: E402
    variant_pie, variant_na, tapered_bezier, tapered_line, to_px,
)

CANVAS = 300


def draw_zhang(draw, ox=0, oy=0, scale=1.0):
    """张 = 弓 (compressed left ~35%) + 长 (right ~60%).

    Math coords: center origin, +y up.
    Left column centered ~ x=-80, right column centered ~ x=+35.
    """
    def P(x, y):
        return (ox + x * scale, oy + y * scale)

    # ------------ LEFT: 弓 (3 strokes) ------------
    # Stroke 1: 横折 — top heng then fold down on the RIGHT end.
    tapered_line(draw, P(-115, +90), P(-55, +90), w0=5, w1=6)
    tapered_line(draw, P(-55, +90), P(-58, +55), w0=6, w1=5)

    # Stroke 2: middle 横 — short horizontal across (does not touch
    # the outer envelope — it hangs inside).
    tapered_line(draw, P(-110, +32), P(-55, +32), w0=5, w1=5)

    # Stroke 3: 竖折折钩 — starts near the left of stroke 1, drops
    # down, then folds right along the bottom, then rises with hook.
    # Initial vertical drop (left side of 弓)
    tapered_line(draw, P(-110, +85), P(-108, -55), w0=6, w1=6)
    # Bottom horizontal sweeping right
    tapered_line(draw, P(-108, -55), P(-52, -60), w0=6, w1=6)
    # Rising back up (right side going up)
    tapered_line(draw, P(-52, -60), P(-58, -20), w0=6, w1=5)
    # Small hook flick pointing up-left
    tapered_line(draw, P(-58, -20), P(-82, -12), w0=5, w1=1)

    # ------------ RIGHT: 长 (4 strokes) ------------
    # Stroke 1: short 撇 at top-left of 长 (starts high, slants down-left)
    variant_pie(draw, head=P(+10, +100), tail=P(-25, +55),
                bow_perp=-4.0, w_head=7, w_tail=2)

    # Stroke 2: long 横 (horizontal across upper-middle of 长)
    tapered_line(draw, P(-15, +40), P(+100, +38), w0=6, w1=6)

    # Stroke 3: 竖提 — vertical starting above heng, going down,
    # then rising ti at the bottom.
    tapered_line(draw, P(+20, +60), P(+20, -35), w0=6, w1=6)
    # ti flick up-right
    tapered_line(draw, P(+20, -35), P(+55, -22), w0=6, w1=1)

    # Stroke 4: long 捺 — sweeps from the heng-shu crossing area
    # out to bottom-right corner
    variant_na(draw, head=P(+20, +38), tail=P(+130, -115),
               bow_perp=+10.0, w_head=2.0, w_belly=15.0, w_tail=3.0,
               belly_u=0.7)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)
    draw_zhang(draw)
    out = os.path.join(_HERE, "01_张.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
