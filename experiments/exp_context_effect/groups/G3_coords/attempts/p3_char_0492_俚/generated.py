# BANK_DEVIATION
# skipped: ren_pang.py (bank 亻 is turtle math-coord based)
# reason: composition uses PIL inline pixel coords (fu_pay recipe) so
#         亻 slots cleanly next to inline 里; ren_pang's turtle
#         math-coord signature doesn't compose with PIL right slot.
# fresh_component: ren_pang_pil_for_LR_left (same shape as fu_pay's 亻)
#
# p3_char_0492_俚 — 亻 (left) + 里 (right).
# 里 = 曰 top-rect + 土 bottom, sharing a central 竖 through the whole thing.
# 7 strokes for 里, 2 for 亻 = 9 strokes total. Thin MMH-style widths.

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
    # S1: 撇 — sweep from upper-right of left slot down-left.
    bezier_stroke(d,
                  to_px(-70, 100),
                  to_px(-90, 20),
                  to_px(-110, -85),
                  w_head=6, w_tail=2, n=55)

    # S2: 竖 — vertical, head touching pie mid-shaft. Ends above the base
    # so 亻 doesn't overshoot 里's bottom (GT has 亻's shu ending ~mid-low).
    line_stroke(d,
                to_px(-72, 35),
                to_px(-72, -75),
                w_head=6, w_tail=5, n=40)

    # ---------- 里 (right side) ----------
    # Box for 曰 (upper rectangle): x [-10, +85], y [+95, +25]
    # 土 lives below: middle heng around y=-40, bottom heng at y=-110.
    # Central 竖 runs from the top heng (y=+95) down to the bottom heng (y=-110).

    x_L = -10   # left of upper rect
    x_R = 85    # right of upper rect
    y_top = 95  # top of upper rect
    y_bot = 25  # bottom of upper rect / top of 土
    y_mid = 60  # middle heng inside 曰
    x_mid = (x_L + x_R) // 2  # center where 竖 lives

    # S3: left 竖 of 曰
    line_stroke(d, to_px(x_L, y_top), to_px(x_L, y_bot), 5, 5, n=30)

    # S4: 横折 (top heng + right shu)
    line_stroke(d, to_px(x_L - 2, y_top), to_px(x_R + 2, y_top), 5, 5, n=30)
    line_stroke(d, to_px(x_R, y_top), to_px(x_R, y_bot), 5, 5, n=30)

    # S5: middle 横 inside 曰 (slightly shorter, thinner)
    line_stroke(d, to_px(x_L + 4, y_mid), to_px(x_R - 4, y_mid), 4, 4, n=25)

    # S6: bottom 横 of 曰 (top of 土)
    line_stroke(d, to_px(x_L - 2, y_bot), to_px(x_R + 2, y_bot), 5, 5, n=30)

    # S7: middle 横 of 土 (below 曰)
    y_tu_mid = -40
    line_stroke(d, to_px(x_L + 5, y_tu_mid), to_px(x_R - 5, y_tu_mid), 5, 5, n=30)

    # S8: long central 竖 — from top of 曰 down through 土 to bottom heng
    y_bot_bot = -110
    line_stroke(d, to_px(x_mid, y_top - 2), to_px(x_mid, y_bot_bot + 2), 5, 5, n=45)

    # S9: bottom 横 (widest, base of 土)
    line_stroke(d, to_px(x_L - 25, y_bot_bot), to_px(x_R + 25, y_bot_bot), 6, 6, n=40)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_俚.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
