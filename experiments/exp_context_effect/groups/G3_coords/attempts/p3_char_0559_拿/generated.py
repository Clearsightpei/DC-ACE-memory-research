# BANK_DEVIATION
# skipped: ji_meet_char.py (top 人 + heng of 合)
# reason: 拿's top 人-roof + short heng sits in the upper third only; ji_meet_char's
#         proportions occupy the full canvas and would overpower the 手 stack below.
# fresh_component: he_top_stack_for_na (人-roof + short heng + small 口, sized for top half)
#
# 拿 = 合 (top: 人 + 一 + 口) stacked over 手 (bottom: 撇 + 二 + 亅 hook).
# Rendered fresh with PIL + shared helpers (kiss_apex, tapered_line, variant_pie, variant_na).

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.normpath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import (  # noqa: E402
    variant_pie, variant_na, kiss_apex, tapered_line, to_px,
)


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- Top 人-roof (wide apex, sits in upper region) ----
    pie_head = (0, +130)
    pie_tail = (-95, +55)
    na_tail = (+95, +55)
    ph, nh = kiss_apex(pie_head, pie_tail, na_tail, u_pie=0.0, bow_pie=-5.0)
    variant_pie(d, head=ph, tail=pie_tail, bow_perp=-5.0, w_head=4.0, w_tail=2.5)
    variant_na(d, head=nh, tail=na_tail, bow_perp=+5.0,
               w_head=3.0, w_belly=4.0, w_tail=2.5, belly_u=0.7)

    # ---- Short heng under the roof (合's middle 一) ----
    tapered_line(d, (-45, +45), (+45, +45), w0=3, w1=3, n=24)

    # ---- 口 (small mouth of 合) ----
    left, right, top, bot = -30, +30, +35, +5
    tapered_line(d, (left, top), (left, bot), w0=3, w1=3, n=16)      # left 竖
    tapered_line(d, (left, top), (right, top), w0=3, w1=3, n=16)     # top 横
    tapered_line(d, (right, top), (right, bot), w0=3, w1=3, n=16)    # right 竖 (heng-zhe would be one stroke, but visually fine)
    tapered_line(d, (left, bot), (right, bot), w0=3, w1=3, n=16)     # bottom 横

    # ---- 手 (bottom: 撇 + 横 + 横 + 竖钩) — 4 strokes ----
    # 撇 sweeping down-left from upper-right
    variant_pie(d, head=(+20, -10), tail=(-70, -40),
                bow_perp=-6.0, w_head=4.0, w_tail=2.0)

    # Upper heng of 手 (short, sits under the pie's tail region)
    tapered_line(d, (-50, -45), (+55, -45), w0=3, w1=3, n=28)

    # Longer bottom heng of 手 (the one crossing 竖钩)
    tapered_line(d, (-80, -85), (+80, -85), w0=3, w1=3, n=32)

    # 竖钩: vertical shaft from top of pie region down, centered
    tapered_line(d, (0, -30), (0, -130), w0=3.5, w1=3.0, n=32)
    # hook (little curl to the left at the bottom)
    variant_pie(d, head=(0, -130), tail=(-22, -138),
                bow_perp=+2.0, w_head=3.0, w_tail=1.5)

    out = os.path.join(_HERE, "01_拿.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
