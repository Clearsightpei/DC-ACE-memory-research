# BANK_DEVIATION
# skipped: (no bank entry exists for 舟 or 殳)
# reason: 般 = 舟 (LR-left) + 殳 (LR-right). Neither radical has a bank
#   entry; both must be inlined fresh. Using PIL px coords in the style
#   of ren_pang_pil_for_LR_left.py (thin MMH-style ~4-5px ink).
# fresh_component: zhou_boat_for_LR_left, shu_weapon_for_LR_right
#
# GT observation: 舟 left ~x 35-135, 殳 right ~x 145-275.
# 舟: top 撇 + 竖 (left body) + 横折钩 (right body + hook) + 2 crossing 横 + inner dot.
# 殳: top 几-form (撇 + 横折弯钩) + bottom 又 (横撇 + 捺).

import math
import os
from PIL import Image, ImageDraw


def bezier(d, p0, p1, p2, w_head, w_tail, n=50, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (bx, by)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=black)
        prev = cur


def tapered(d, p0, p1, w_head, w_tail, n=35, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (x, y)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=black)
        prev = cur


def polyline(d, pts, w, black=(0, 0, 0)):
    """Fixed-width polyline through pts."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=black, width=w)
        r = w / 2.0
        for p in [pts[i], pts[i + 1]]:
            d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=black)


def draw_zhou_boat_for_LR_left(d, black=(0, 0, 0)):
    """舟 in the LR-left slot (~x 35-135)."""
    # S1: top 撇 — moderate slant from (88, 55) down-left to (58, 100)
    bezier(d, (88, 55), (72, 72), (58, 100), w_head=5, w_tail=3, n=40, black=black)
    # S2: 竖 — left vertical of the body
    tapered(d, (58, 98), (58, 215), w_head=5, w_tail=4, n=40, black=black)
    # S3: 横折钩 — top heng from (58, 100) → (128, 100), then zhe down, hook up-left
    polyline(d, [(58, 100), (128, 100)], w=4, black=black)
    tapered(d, (128, 100), (128, 215), w_head=4, w_tail=5, n=35, black=black)
    # hook: short up-left at bottom
    polyline(d, [(128, 215), (108, 205)], w=5, black=black)
    # S4: middle heng #1 (upper of two inner heng)
    polyline(d, [(60, 145), (128, 145)], w=4, black=black)
    # S5: middle heng #2 (lower)
    polyline(d, [(60, 180), (128, 180)], w=4, black=black)
    # S6: small inner 点 between the two heng
    bezier(d, (78, 120), (84, 128), (92, 138), w_head=3, w_tail=5, n=15, black=black)


def draw_shu_weapon_for_LR_right(d, black=(0, 0, 0)):
    """殳 in the LR-right slot (~x 150-275)."""
    # TOP 几-like form — corner at (170, 58) shared by pie and heng.
    # S1: 撇 — from (170, 58) down-left to (150, 110)
    bezier(d, (170, 58), (162, 80), (150, 110), w_head=5, w_tail=2, n=40, black=black)
    # S2: 横折弯钩 — heng from (170, 58) → (250, 58), curve down-right, hook up-left
    polyline(d, [(170, 58), (250, 58)], w=4, black=black)
    bezier(d, (250, 58), (262, 95), (262, 135), w_head=4, w_tail=5, n=35, black=black)
    polyline(d, [(262, 135), (245, 128)], w=5, black=black)

    # BOTTOM 又 form — 横撇 apex on the shaft where 捺 also crosses.
    # S3: 横撇 — short heng (175→215, 150) then long pie sweeping down-left
    polyline(d, [(178, 150), (215, 150)], w=4, black=black)
    bezier(d, (215, 150), (190, 195), (155, 240), w_head=5, w_tail=2, n=45, black=black)
    # S4: 捺 — starts high on the pie shaft, crosses down-right to lower-right
    bezier(d, (190, 168), (220, 200), (275, 245), w_head=3, w_tail=8, n=45, black=black)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_zhou_boat_for_LR_left(d)
    draw_shu_weapon_for_LR_right(d)
    out = os.path.join(os.path.dirname(__file__), "01_般.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
