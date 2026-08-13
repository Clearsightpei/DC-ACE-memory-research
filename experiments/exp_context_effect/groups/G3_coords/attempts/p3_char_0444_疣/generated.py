# p3_char_0444_疣 (yóu) — 疒 envelope + 尤 (you2) interior.
#
# Composition (from gt/phase3/疣.png):
#   Left/top: 疒 (nè) envelope — reuse bank ne_sick.draw_ne_chuang.
#   Interior (belly, right of pie shaft, below heng):
#     尤 (you2) — 4 strokes:
#       1. short heng, slightly rising
#       2. long 撇 sweeping down-left from mid-heng
#       3. 竖弯钩 — down then curve right to hook up
#       4. small 点 at upper-right
#
# Bank reuse: envelope from ne_sick (identity). Interior 尤 is inline —
# there is no 尤 bank entry (wang_go.py is 往, not 尤 as a standalone
# radical), so no bank primitive is being skipped; nothing to note as
# BANK_DEVIATION.

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from ne_sick import draw_ne_chuang, _tapered_line, _tapered_bezier  # noqa: E402

_CANVAS = 300


def draw_you_interior(draw):
    """尤 rendered inline in the belly of 疒 (right of pie shaft)."""

    # Stroke 1: short heng — slight rise left-to-right.
    # Sits under the 疒 heng roof, in the belly's upper band.
    # Kept clear of 疒 pie shaft (starts ~x=158, not touching pie at x≈125).
    _tapered_line(draw, (158, 170), (235, 160), w_head=5.0, w_tail=5.0, n=30)

    # Stroke 2: 撇 — sweep from mid-heng down-left, contained in belly.
    _tapered_bezier(
        draw,
        p0=(185, 160),
        p1=(150, 270),
        ctrl=(160, 220),
        w_head=6.5,
        w_tail=3.5,
        n=80,
    )

    # Stroke 3: 竖弯钩 — down from heng's right end, curve right, hook up.
    # Down segment
    _tapered_bezier(
        draw,
        p0=(222, 158),
        p1=(230, 240),
        ctrl=(224, 200),
        w_head=5.5,
        w_tail=5.5,
        n=40,
    )
    # Curve right and slight rise
    _tapered_bezier(
        draw,
        p0=(230, 240),
        p1=(275, 258),
        ctrl=(255, 262),
        w_head=5.5,
        w_tail=6.0,
        n=40,
    )
    # Short upward hook
    _tapered_line(draw, (275, 258), (275, 232), w_head=6.0, w_tail=3.0, n=20)

    # Stroke 4: small 点 at upper-right corner.
    _tapered_line(draw, (247, 128), (260, 148), w_head=3.0, w_tail=6.5, n=18)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Envelope 疒 from bank (identity reuse).
    draw_ne_chuang(draw)
    # Interior 尤 inline.
    draw_you_interior(draw)
    out = os.path.join(_HERE, "01_疣.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
