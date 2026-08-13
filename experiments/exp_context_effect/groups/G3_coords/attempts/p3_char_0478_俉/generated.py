# BANK_DEVIATION
# skipped: kou.py (turtle-based bank primitive)
# reason: kou is a turtle-based primitive; this attempt uses PIL inline rendering
#         consistent with fu_pay.py pattern for L-R composition. 吾 (right side)
#         needs its own 五+口 stacked geometry not covered by any single bank entry.
# fresh_component: wu_kou_stack_for_LR_right (五 stacked over 口 in right slot)
#
# p3_char_0478_俉 — G3 attempt.
# 俉 = 亻 (left person radical, 2 strokes) + 吾 (right, 7 strokes: 五 stacked on 口).
# 吾 = 五 (top: heng + shu + fold + heng) + 口 (bottom box).
# Total ~9 strokes. GT shows thin MMH-style lines; keep widths modest (~4-6 px).
# 亻 sits on the left ~third; 吾 sits on the right ~two-thirds.

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
    # Stroke 1: 撇 (pie) — moderate sweep from upper mid-left down-left.
    bezier_stroke(d,
                  to_px(-50, 90),
                  to_px(-70, 15),
                  to_px(-90, -80),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 (shu) — vertical, touching pie mid-shaft.
    line_stroke(d,
                to_px(-55, 25),
                to_px(-55, -105),
                w_head=6, w_tail=5, n=40)

    # ---------- 吾 (right side, 五 stacked on 口) ----------
    # ----- 五 (top) -----
    # Stroke 3: top 一 (heng) — long horizontal at top.
    line_stroke(d,
                to_px(-10, 95),
                to_px(90, 95),
                w_head=5, w_tail=5, n=40)

    # Stroke 4: 竖 (shu) — short vertical descending from top-heng, left of centre.
    line_stroke(d,
                to_px(15, 90),
                to_px(15, 55),
                w_head=5, w_tail=5, n=25)

    # Stroke 5: 横折 (heng zhe) — small internal fold forming middle box of 五.
    # Short horizontal segment from shu to right side
    line_stroke(d,
                to_px(15, 55),
                to_px(70, 55),
                w_head=5, w_tail=5, n=25)
    # Fold: short right-vertical descending
    line_stroke(d,
                to_px(70, 58),
                to_px(70, 30),
                w_head=5, w_tail=5, n=20)

    # Stroke 6: bottom 一 (heng) of 五 — long horizontal, forms top of 口 too.
    line_stroke(d,
                to_px(-10, 25),
                to_px(90, 25),
                w_head=5, w_tail=5, n=40)

    # ----- 口 (bottom box) -----
    # Left 竖
    line_stroke(d,
                to_px(-5, 20),
                to_px(-5, -85),
                w_head=5, w_tail=5, n=35)
    # Right 竖
    line_stroke(d,
                to_px(85, 20),
                to_px(85, -85),
                w_head=5, w_tail=5, n=35)
    # Bottom 一 of 口
    line_stroke(d,
                to_px(-10, -85),
                to_px(90, -85),
                w_head=5, w_tail=5, n=35)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_俉.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
