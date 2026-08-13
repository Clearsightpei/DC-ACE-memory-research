# p3_char_0328_佈 — G3 attempt.
# 佈 = 亻 (left, 2 strokes: pie + shu) + 布 (right, 5 strokes: pie + heng
#     + shu + heng-zhe-gou + inner shu). 7 strokes total.
# GT shows thin, MMH-style lines — widths ~4-6 px. Adapts fu_pay.py's
# 亻 recipe on the left, then hand-inlines 布 on the right.

import os
import math
from PIL import Image, ImageDraw

CANVAS = 300
CX = CY = CANVAS // 2


def to_px(x, y):
    return (CX + x, CY - y)


def bezier_stroke(draw, p0, p1, p2, w_head, w_tail, n=40):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        cur = (bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, cur], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=(0, 0, 0))
        prev = cur


def line_stroke(draw, p0, p1, w_head, w_tail, n=25):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        cur = (x, y)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, cur], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=(0, 0, 0))
        prev = cur


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---------- 亻 (left radical, ~35% width) ----------
    # Stroke 1: 撇 — pie sweep from upper-left, moderate reach.
    bezier_stroke(d,
                  to_px(-55, 95),
                  to_px(-70, 20),
                  to_px(-95, -70),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu meeting pie mid-shaft at ~y=20.
    line_stroke(d,
                to_px(-52, 20),
                to_px(-52, -105),
                w_head=6, w_tail=5, n=40)

    # ---------- 布 (right side, right ~65%) ----------
    # Stroke 3: 丿 — short pie above the heng, upper-right zone.
    bezier_stroke(d,
                  to_px(30, 110),
                  to_px(15, 90),
                  to_px(0, 60),
                  w_head=5, w_tail=2, n=40)

    # Stroke 4: 一 — long heng across the right zone, crossing the pie.
    line_stroke(d,
                to_px(-15, 60),
                to_px(95, 60),
                w_head=5, w_tail=5, n=40)

    # Stroke 5: 丨 — left shu of 巾, from left end of heng downward,
    # slight down-left slant.
    line_stroke(d,
                to_px(-5, 55),
                to_px(-15, -100),
                w_head=6, w_tail=5, n=40)

    # Stroke 6: 横折钩 — top of box (horizontal from mid-left to right),
    # then vertical down, then small hook flick up-left.
    line_stroke(d,
                to_px(-5, 30),
                to_px(75, 30),
                w_head=5, w_tail=5, n=30)
    line_stroke(d,
                to_px(75, 30),
                to_px(75, -85),
                w_head=6, w_tail=6, n=40)
    # Hook flick
    bezier_stroke(d,
                  to_px(75, -85),
                  to_px(65, -80),
                  to_px(50, -72),
                  w_head=6, w_tail=1, n=25)

    # Stroke 7: 丨 — middle vertical inside the box, extending below.
    line_stroke(d,
                to_px(35, 25),
                to_px(35, -115),
                w_head=5, w_tail=4, n=40)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佈.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
