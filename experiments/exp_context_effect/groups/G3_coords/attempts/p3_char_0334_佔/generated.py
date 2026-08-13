# p3_char_0334_佔 — G3 attempt.
# 佔 = 亻 (left, 2 strokes) + 占 (right, 5 strokes) = 7 strokes total.
# 占 = 卜 (top: 丨 + short 一) + 口 (bottom: 丨 + 横折 + 一).
# GT shows thin uniform MMH-style lines; 亻 sits left third, 占 sits right two-thirds.
# Recipe adapted from fu_pay.py (亻 side) + inline 占.

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
    # Stroke 1: 撇 — pie sweep from upper part of left zone down-left.
    bezier_stroke(d,
                  to_px(-60, 100),
                  to_px(-82, 15),
                  to_px(-105, -95),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu, head touching pie mid-shaft, tail low.
    line_stroke(d,
                to_px(-62, 35),
                to_px(-62, -100),
                w_head=5, w_tail=5, n=40)

    # ---------- 占 (right side) ----------
    # 卜 top portion:
    # Stroke 3: 丨 (vertical) — top center of right zone, sits just above 口.
    line_stroke(d,
                to_px(15, 115),
                to_px(15, 10),
                w_head=5, w_tail=5, n=40)

    # Stroke 4: 一 (short heng of 卜) — a short horizontal off the vertical,
    # going right around mid-upper height.
    line_stroke(d,
                to_px(20, 65),
                to_px(78, 65),
                w_head=4, w_tail=5, n=25)

    # 口 bottom portion (rectangle, thin uniform strokes):
    # Stroke 5: 丨 (left vertical of 口)
    line_stroke(d,
                to_px(-15, 5),
                to_px(-15, -95),
                w_head=5, w_tail=5, n=40)

    # Stroke 6: 横折 — top heng across then down the right side.
    #   part A: top heng from (-15, 5) to (85, 5)
    line_stroke(d,
                to_px(-15, 5),
                to_px(85, 5),
                w_head=5, w_tail=5, n=30)
    #   part B: right shu from (85, 5) to (85, -95)
    line_stroke(d,
                to_px(85, 5),
                to_px(85, -95),
                w_head=5, w_tail=5, n=30)

    # Stroke 7: 一 (bottom heng of 口)
    line_stroke(d,
                to_px(-15, -95),
                to_px(85, -95),
                w_head=5, w_tail=5, n=30)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佔.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
