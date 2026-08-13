# p3_char_0246_仵 — G3 attempt.
# 仵 (wǔ) = 亻 (left person radical, 2 strokes: pie + shu)
#        + 午 (right, 4 strokes: pie + short heng + long heng + shu).
# 6 strokes total. GT shows thin uniform lines (MMH-style, ~4-6 px).
# 亻 sits on the left third; 午 sits on the right two-thirds, taller.
# The 午 pattern mirrors niu.py structure (pie + heng + heng + shu),
# but without 牛's extra top-left mark.

import os
from PIL import Image, ImageDraw

CANVAS = 300
CX = CY = CANVAS // 2


def to_px(x, y):
    # math coords -> pixel coords (y up)
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
    # Stroke 1: 撇 — sweep from upper part of left zone down-left.
    bezier_stroke(d,
                  to_px(-55, 95),
                  to_px(-77, 10),
                  to_px(-100, -85),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu, head touching pie mid-shaft (~y=30), tail low.
    line_stroke(d,
                to_px(-57, 30),
                to_px(-57, -110),
                w_head=6, w_tail=5, n=40)

    # ---------- 午 (right side) ----------
    # Stroke 3: 撇 — short slant at top, from upper-right going down-left.
    bezier_stroke(d,
                  to_px(30, 100),
                  to_px(10, 75),
                  to_px(-15, 55),
                  w_head=6, w_tail=2, n=40)

    # Stroke 4: 短横 (short heng) — upper horizontal, shorter.
    line_stroke(d,
                to_px(0, 45),
                to_px(70, 45),
                w_head=5, w_tail=5, n=30)

    # Stroke 5: 长横 (long heng) — middle horizontal, spans most of right zone.
    line_stroke(d,
                to_px(-25, -10),
                to_px(95, -10),
                w_head=5, w_tail=5, n=40)

    # Stroke 6: 竖 (shu) — vertical from top through both hengs to bottom.
    line_stroke(d,
                to_px(35, 55),
                to_px(35, -115),
                w_head=6, w_tail=5, n=40)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_仵.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
