# BANK_DEVIATION
# skipped: bao_gai_tou.py, kou.py
# reason: bao_gai_tou.py's internal draw_henggou uses raw PIL coords and
#   does not shift consistently with its oy parameter, so scaling+moving
#   the roof to sit at the top of a tall stacked char (容) broke geometry.
#   kou.py's baked (ox,oy,scale) also mis-sized at bottom slot.
# fresh_component: rong_roof_and_kou_inline (宀 roof + 口 box hand-rendered
#   in math coords so all four zones — roof, 八, 人, 口 — align cleanly.)
#
# p3_char_0547_容 — 宀 + 谷 (八 + 人 + 口). Everything inline in math coords.
import os
from PIL import Image, ImageDraw
import sys

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "../../success_bank/code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import (variant_pie, variant_na, kiss_apex,
                             tapered_line, to_px)  # noqa: E402


def _stroke(t, p0, p1, w0, w1, n=32):
    tapered_line(t, p0, p1, w0=w0, w1=w1, n=n)


def draw_roof(t):
    """宀 — 点 chimney + 横钩 (with a small hook at right end) + short left dian.
    Math coords, roof band roughly y=+80..+118."""
    # 1) 点 chimney at top center.
    _stroke(t, (-2, +130), (+6, +115), w0=3, w1=6, n=16)
    # 2) short left inner dian (the pi-tick under the left corner).
    _stroke(t, (-60, +95), (-70, +75), w0=3, w1=5, n=18)
    # 3) 横钩: long horizontal + small downward hook at right end.
    #    horizontal from (-80,+95) → (+80,+95), then hook to (+78,+80).
    _stroke(t, (-82, +95), (+80, +95), w0=4, w1=4, n=48)
    _stroke(t, (+80, +95), (+70, +78), w0=4, w1=2, n=14)


def draw_ba_top(t):
    """八 at top of 谷 — small splay just under the roof."""
    variant_pie(t, head=(-16, +55), tail=(-40, +25),
                bow_perp=-3.0, w_head=4.0, w_tail=2.0, n=28)
    variant_na(t, head=(+16, +55), tail=(+42, +25),
               bow_perp=+3.0, w_head=2.5, w_belly=4.0, w_tail=2.0,
               belly_u=0.7, n=28)


def draw_ren_middle(t):
    """人 — inverted V spanning middle band, kissing at apex ~y=+15."""
    pie_head = (-2, +18)
    pie_tail = (-60, -40)
    na_tail  = (+60, -40)
    pie_h, na_h = kiss_apex(pie_head, pie_tail, na_tail,
                            u_pie=0.0, bow_pie=-6.0)
    variant_pie(t, head=pie_h, tail=pie_tail,
                bow_perp=-5.0, w_head=5.0, w_tail=2.5, n=40)
    variant_na(t,  head=na_h, tail=na_tail,
               bow_perp=+7.0, w_head=3.0, w_belly=6.0, w_tail=3.0,
               belly_u=0.7, n=40)


def draw_kou_bottom(t):
    """口 at bottom slot, math coords, ~ x=[-30,+30], y=[-95,-55]."""
    # left 竖
    _stroke(t, (-30, -55), (-30, -95), w0=4, w1=4, n=20)
    # top 横 + right 竖 (as 横折) — draw as two segments for a clean corner.
    _stroke(t, (-30, -55), (+32, -55), w0=4, w1=4, n=24)
    _stroke(t, (+32, -55), (+32, -95), w0=4, w1=4, n=20)
    # bottom 横
    _stroke(t, (-30, -95), (+32, -95), w0=4, w1=4, n=24)


def draw_rong(t):
    draw_roof(t)
    draw_ba_top(t)
    draw_ren_middle(t)
    draw_kou_bottom(t)


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    draw_rong(t)
    out = os.path.join(os.path.dirname(__file__), "01_容.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
