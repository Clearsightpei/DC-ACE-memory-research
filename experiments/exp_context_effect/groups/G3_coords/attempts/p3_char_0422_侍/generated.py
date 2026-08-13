# p3_char_0422_侍 — G3 attempt.
# 侍 = 亻 (left, 2 strokes: pie + shu) + 寺 (right, 6 strokes = 土 top: heng+shu+heng,
#     then 寸 bottom: heng + shu_gou + dian). 8 strokes total.
# Base pattern lifted from fu_pay.py (亻 + 寸) but 寺 stacks 土 above 寸, so the
# right side is TALLER — 土 occupies upper-right, 寸 lower-right, with the
# bottom heng of 土 typically merging into the top heng of 寸 as the LONGEST
# horizontal spanning most of right zone. GT confirms: one very wide heng
# roughly at right-mid-height, thin uniform MMH-style lines.
#
# BANK_DEVIATION
# skipped: ren_pang.py, tu.py, cun.py
# reason: right side stacks two components (土 over 寸); bank turtle primitives
#   don't compose cleanly under vertical stacking + shared L-R budget. Inline
#   PIL with fu_pay.py's proven bezier/line width knobs is simpler.
# fresh_component: shi_char_stacked_right (土 + 寸 vertical stack for right side)

import os
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

    # ---------- 亻 (left radical) ----------
    # Stroke 1: 撇 (pie) — from upper-left down-left
    bezier_stroke(d,
                  to_px(-55, 100),
                  to_px(-78, 15),
                  to_px(-100, -95),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 (shu) — vertical descending; head sits on pie mid-shaft
    line_stroke(d,
                to_px(-72, 20),
                to_px(-72, -115),
                w_head=6, w_tail=5, n=40)

    # ---------- 寺 (right side) ----------
    # 土 upper part: strokes 3-5
    # Stroke 3: 一 (short heng, top of 土)
    line_stroke(d,
                to_px(5, 105),
                to_px(75, 105),
                w_head=4, w_tail=4, n=25)

    # Stroke 4: 丨 (shu, vertical through both 土 hengs)
    line_stroke(d,
                to_px(40, 115),
                to_px(40, 40),
                w_head=5, w_tail=5, n=25)

    # Stroke 5: 一 (LONG bottom heng of 土 = also the transition heng; widest horizontal)
    line_stroke(d,
                to_px(-15, 40),
                to_px(105, 40),
                w_head=5, w_tail=5, n=40)

    # 寸 lower part: strokes 6-8
    # Stroke 6: 一 (heng of 寸) — a bit shorter than the widest heng above
    line_stroke(d,
                to_px(0, -10),
                to_px(95, -10),
                w_head=4, w_tail=4, n=30)

    # Stroke 7: 亅 (shu_gou) — vertical crossing 寸's heng, with hook at bottom
    line_stroke(d,
                to_px(50, 25),
                to_px(50, -110),
                w_head=5, w_tail=5, n=40)
    bezier_stroke(d,
                  to_px(50, -110),
                  to_px(42, -103),
                  to_px(25, -92),
                  w_head=5, w_tail=1, n=25)

    # Stroke 8: 丶 (dian) — dot below heng, left of shu_gou
    bezier_stroke(d,
                  to_px(8, -35),
                  to_px(22, -45),
                  to_px(38, -58),
                  w_head=3, w_tail=7, n=25)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_侍.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
