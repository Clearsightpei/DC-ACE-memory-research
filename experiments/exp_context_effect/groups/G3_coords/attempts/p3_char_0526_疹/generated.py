# p3_char_0526_疹 — 疒 envelope + 㐱 interior (人 top + 彡 bottom-right)
#
# Composition analysis from GT:
#   - Outer envelope 疒: reuse bank ne_sick.draw_ne_chuang (v9 graduate).
#   - Interior 㐱 = small 人 (apex + pie + na) at top of belly, then 彡
#     (three cascading pies) filling the belly's right/lower portion.
#
# No BANK_DEVIATION: envelope is used AS-IS from ne_sick. Interior is
# inline PIL because bank shan_radical uses turtle-math coords; mixing
# APIs is messier than a fresh inline render (same posture as
# shan_hernia.py).

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from ne_sick import draw_ne_chuang, _tapered_line, _tapered_bezier  # noqa: E402

_CANVAS = 300


def draw_ren_small(draw, apex=(190, 125), pie_tail=(150, 180),
                   na_tail=(230, 178), w=5):
    """Small 人: pie down-left + na down-right from apex."""
    _tapered_bezier(draw, apex, pie_tail,
                    ctrl=((apex[0] + pie_tail[0]) / 2 - 6,
                          (apex[1] + pie_tail[1]) / 2 + 4),
                    w_head=w, w_tail=w - 1, n=40)
    _tapered_bezier(draw, apex, na_tail,
                    ctrl=((apex[0] + na_tail[0]) / 2 + 3,
                          (apex[1] + na_tail[1]) / 2 - 3),
                    w_head=w - 1, w_tail=w + 1, n=40)


def draw_shan_three(draw):
    """彡: three cascading pies descending in the lower-right belly."""
    # Upper (shortest, highest, rightmost head)
    _tapered_bezier(draw, p0=(225, 195), p1=(185, 230),
                    ctrl=(203, 215),
                    w_head=6, w_tail=3, n=50)
    # Middle
    _tapered_bezier(draw, p0=(235, 225), p1=(190, 265),
                    ctrl=(210, 248),
                    w_head=6.5, w_tail=3, n=50)
    # Lower (longest)
    _tapered_bezier(draw, p0=(245, 255), p1=(195, 290),
                    ctrl=(218, 275),
                    w_head=7, w_tail=3, n=60)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # 疒 envelope from bank.
    draw_ne_chuang(draw)
    # 人 top of interior belly.
    draw_ren_small(draw)
    # 彡 three cascading pies filling lower-right belly.
    draw_shan_three(draw)
    out = os.path.join(_HERE, "01_疹.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
