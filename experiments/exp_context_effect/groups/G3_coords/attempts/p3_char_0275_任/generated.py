# p3_char_0275_任 — G3 attempt.
# 任 = 亻 (left person radical, 2 strokes: pie + shu)
#   + 壬 (right, 4 strokes: top short pie, top short heng, vertical shu, bottom long heng).
# Total 6 strokes. Thin MMH-style widths (~4-6 px). Bottom heng of 壬 is the
# widest element; the two hengs stack with vertical piercing both.
# Recipe adapted from fu_pay.py (亻 + 寸) by swapping the right side for 壬.

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
    # Stroke 1: 撇 (pie) — moderate length, from upper-left zone sweeping down-left.
    bezier_stroke(d,
                  to_px(-55, 90),
                  to_px(-72, 15),
                  to_px(-95, -70),
                  w_head=6, w_tail=2, n=55)
    # Stroke 2: 竖 (shu) — vertical from pie mid-shaft down.
    line_stroke(d,
                to_px(-58, 30),
                to_px(-58, -95),
                w_head=6, w_tail=5, n=40)

    # ---------- 壬 (right side) ----------
    # Stroke 3: 丿 (short pie at top of 壬), sweeping from upper-right down-left.
    bezier_stroke(d,
                  to_px(55, 105),
                  to_px(25, 90),
                  to_px(-5, 75),
                  w_head=5, w_tail=2, n=30)

    # Stroke 4: 一 (top short heng) — right of pie tail, short.
    line_stroke(d,
                to_px(0, 55),
                to_px(70, 55),
                w_head=4, w_tail=5, n=30)

    # Stroke 5: 丨 (shu vertical) — pierces top heng, ends near bottom heng.
    line_stroke(d,
                to_px(35, 60),
                to_px(35, -90),
                w_head=5, w_tail=5, n=40)

    # Stroke 6: 一 (bottom heng, longest) — wide horizontal at bottom of right zone.
    line_stroke(d,
                to_px(-20, -90),
                to_px(105, -90),
                w_head=5, w_tail=6, n=40)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(out_dir, "01_任.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
