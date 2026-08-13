# BANK_DEVIATION
# skipped: shan_radical.py — 㐱 = 人-top + 3 diagonal descending 撇; not a plain 彡
# reason: right side is 㐱 (compound: pie+na of 人 above three descending 撇), not a bank entry
# fresh_component: zhen_right_zhen (㐱 for LR-right slot, PIL pixel inline)

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from quan_tian_for_LR_left import draw_quan_tian_for_LR_left  # type: ignore


def _bow_curve(d, p0, p1, bow=6.0, perp_sign=+1, width=5, taper=None, black=(0, 0, 0)):
    """Draw a slightly bowed segment from p0 to p1 via many short lines.
    perp_sign +1 pushes to left of the p0->p1 direction, -1 to right.
    If taper=(w_head, w_tail) it linearly ramps width; else uses `width`.
    """
    import math
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    L = math.hypot(dx, dy) or 1.0
    # unit perpendicular
    px, py = -dy / L * perp_sign, dx / L * perp_sign
    steps = 26
    prev = None
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) * p0[0] + t * p1[0]
        y = (1 - t) * p0[1] + t * p1[1]
        off = bow * (4 * t * (1 - t))
        x += px * off
        y += py * off
        cur = (x, y)
        if prev is not None:
            if taper is not None:
                w_head, w_tail = taper
                w = int(round(w_head + (w_tail - w_head) * t))
                w = max(2, w)
            else:
                w = width
            d.line([prev, cur], fill=black, width=w)
        prev = cur


def draw_zhen_right(d, black=(0, 0, 0)):
    """㐱 in the right slot of 畛.

    Layout (px on 300x300):
      人 apex near (215, 90); pie tail (170, 175); na tail (285, 175).
      Three descending 撇 stepping down-right below the 人.
    """
    apex = (215, 90)
    pie_tail = (170, 175)
    na_tail = (288, 178)

    # 人 pie (down-left, slight leftward bow); taper thick->thin
    _bow_curve(d, apex, pie_tail, bow=8.0, perp_sign=+1,
               taper=(5, 3), black=black)
    # 人 na (down-right, slight downward bow); taper thin->thick
    _bow_curve(d, apex, na_tail, bow=7.0, perp_sign=-1,
               taper=(3, 6), black=black)

    # 三撇 (三 = 彡-like cluster): three descending 撇 stepping down-right,
    # under and to the right of the 人-pie tail.
    pies = [
        ((195, 175), (160, 218)),   # top
        ((215, 210), (180, 253)),   # middle
        ((235, 245), (200, 288)),   # bottom
    ]
    for (h, t) in pies:
        _bow_curve(d, h, t, bow=5.0, perp_sign=+1,
                   taper=(5, 3), black=black)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # LEFT: compressed 田, taller box to match GT vertical span
    draw_quan_tian_for_LR_left(
        d,
        x_left=25, x_right=130,
        y_top=95, y_bot=250,
        w=5, wm=4,
    )

    # RIGHT: 㐱
    draw_zhen_right(d)

    out = os.path.join(os.path.dirname(__file__), "01_畛.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
