# p3_char_0384_疡 (yáng) — G3 attempt
# Composition: 疒 envelope (top+left wrap) + simplified 昜/汤-right in belly.
#
# Interior decomposition from GT (gt/phase3/疡.png):
#   Inside the 疒 belly (roughly x=145..270, y=110..270) sits a
#   simplified 昜 shape:
#     (a) Short 一 (horizontal) near top of belly.
#     (b) 横折钩 (heng-zhe-gou) envelope: a horizontal that turns down
#         then hooks back to the left (like 力/勹 top).
#     (c) A long 撇 (pie) inside sweeping down-left from top of the
#         envelope to lower-left of the belly.
#     (d) A shorter secondary 撇 crossing/parallel to (c).
#
# Bank reuse: envelope 疒 = draw_ne_chuang from ne_sick.py (v9 grad).
# Interior is inlined (bank has no simplified-昜; components differ).
# Not a BANK_DEVIATION — no bank primitive was skipped; the interior
# is a compound not in the bank.

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from ne_sick import draw_ne_chuang, _tapered_line, _tapered_bezier  # noqa: E402

_CANVAS = 300


def draw_yang_interior(draw):
    """Simplified 昜 rendered inline in 疒's belly.

    Belly window (post-疒-envelope): x roughly 150..270, y 110..275.
    """
    # (a) Top short 一 — sits in upper belly, thin, roughly horizontal.
    _tapered_line(draw, (172, 118), (232, 116), w_head=5.0, w_tail=5.0, n=24)

    # (b) 横折钩 envelope — horizontal from left, turns down at shoulder,
    #     then hooks back up-left at bottom-right corner.
    # Horizontal segment.
    _tapered_line(draw, (170, 148), (250, 148), w_head=5.5, w_tail=5.5, n=28)
    # Shoulder + descending shaft (right vertical of the envelope), curving
    # slightly inward at bottom.
    _tapered_bezier(
        draw,
        p0=(250, 148),
        p1=(215, 258),
        ctrl=(258, 210),
        w_head=6.0,
        w_tail=5.5,
        n=60,
    )
    # Hook flick back up-left at the tail.
    _tapered_line(draw, (215, 258), (198, 240), w_head=6.0, w_tail=2.5, n=16)

    # (c) Single long inner 撇 — the diagnostic mark of 昜-simplified
    #     right side. Passes from top of envelope down-left through the
    #     belly, terminating around lower-left of the belly window
    #     (staying to the RIGHT of the 疒's pie shaft so it doesn't
    #     collide). Slight leftward bow.
    _tapered_bezier(
        draw,
        p0=(235, 168),
        p1=(180, 268),
        ctrl=(200, 222),
        w_head=7.0,
        w_tail=3.0,
        n=70,
    )


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Envelope 疒 from bank (v9-rerun graduate).
    draw_ne_chuang(draw)
    # Interior simplified 昜.
    draw_yang_interior(draw)
    out = os.path.join(_HERE, "01_疡.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
