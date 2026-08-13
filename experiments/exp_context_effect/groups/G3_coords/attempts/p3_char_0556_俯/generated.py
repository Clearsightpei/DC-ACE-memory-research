# BANK_DEVIATION
# skipped: fu_pay.py
# reason: 府 is 广 + 付 nested (roof envelope over 付), not a bare 付; fu_pay's
#         L-R proportions don't fit the compressed inner 付 sitting under a
#         广 roof, so I inline a fresh 府 (广 roof + inner 亻+寸) on the right.
# fresh_component: fu_roof_for_char_府 (广 envelope + compressed inner 付)
#
# p3_char_0556_俯 — G3 attempt.
# 俯 = 亻 (left) + 府 (right). 府 = 广 (roof: dot + heng + pie) + 付 (亻+寸 inside).
# Total strokes: 2 (亻) + 3 (广) + 2 (inner 亻) + 3 (寸) = 10.
# Uses canonical ren_pang_pil_for_LR_left for the OUTER 亻.
# Right side is built fresh in PIL px coords, thin MMH-style widths ~4-6.

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from ren_pang_pil_for_LR_left import draw_ren_pang_pil_for_LR_left

CANVAS = 300


def bezier_stroke(d, p0, p1, p2, w_head, w_tail, n=45):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (bx, by)
        if prev is not None:
            d.line([prev, cur], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=(0, 0, 0))
        prev = cur


def tapered_line(d, p0, p1, w_head, w_tail, n=30):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (x, y)
        if prev is not None:
            d.line([prev, cur], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=(0, 0, 0))
        prev = cur


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- LEFT: 亻 (canonical PIL bank) ----
    # Left slot ~ x in [20, 100]. Tall.
    draw_ren_pang_pil_for_LR_left(
        d, cx=60, y_top=70, y_bot=250,
        w_pie_head=6, w_pie_tail=2, w_shu=5,
    )

    # ---- RIGHT: 府 ----
    # Right slot ~ x in [110, 285], y in [50, 260].
    #
    # 广 roof:
    # (1) top dot — small dian near top-center of right zone
    # (2) heng — long horizontal starting near dot base, sweeping right
    # (3) pie — long left-sweeping stroke from left end of heng down-left,
    #     forming the roof's left edge (envelope for 付 inside)

    # (1) dot — from upper-left to lower-right, small
    bezier_stroke(d,
                  (168, 55), (176, 62), (185, 72),
                  w_head=3, w_tail=7, n=20)

    # (2) heng — long horizontal top of 广 (starts left of dot, extends far right)
    tapered_line(d,
                 (125, 88), (275, 86),
                 w_head=5, w_tail=5, n=40)

    # (3) pie — big left-down sweep from left end of heng down to lower-left
    bezier_stroke(d,
                  (135, 88),   # head at left end of heng
                  (120, 155),  # control, curving left-down
                  (105, 260),  # tail lower-left
                  w_head=7, w_tail=2, n=55)

    # Inner 付: small 亻 + 寸 tucked under the roof, x in ~[145, 275], y in ~[110, 240]
    # Inner 亻 (compressed):
    # inner pie
    bezier_stroke(d,
                  (170, 118),  # head upper-right of inner-亻 center
                  (160, 155),  # control
                  (148, 220),  # tail lower-left
                  w_head=5, w_tail=2, n=45)
    # inner shu
    tapered_line(d,
                 (168, 155), (168, 235),
                 w_head=5, w_tail=4, n=30)

    # Inner 寸 (right of inner 亻):
    # heng
    tapered_line(d,
                 (188, 145), (270, 145),
                 w_head=5, w_tail=5, n=40)
    # shu-gou (vertical crossing heng, hook at bottom)
    tapered_line(d,
                 (228, 118), (228, 225),
                 w_head=5, w_tail=6, n=40)
    # hook flick at bottom of shu-gou (short bezier lifting left-up)
    bezier_stroke(d,
                  (228, 225), (222, 220), (210, 213),
                  w_head=6, w_tail=1, n=20)
    # dian in lower-left pocket of inner 寸
    bezier_stroke(d,
                  (198, 178), (208, 188), (218, 200),
                  w_head=3, w_tail=7, n=20)

    out = os.path.join(HERE, "01_俯.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
