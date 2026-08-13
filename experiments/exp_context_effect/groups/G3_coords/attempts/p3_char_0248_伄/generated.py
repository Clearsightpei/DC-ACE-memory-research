# p3_char_0248_伄 — G3 attempt.
# 伄 = 亻 (left person radical, 2 strokes: pie + shu) + 吊 (right, 口 top + 巾 bottom).
# GT shows thin, MMH-style lines — keep widths modest (~4-6 px).
# 亻 sits on the left third; 吊 sits on the right two-thirds.
# Recipe modeled after fu_pay.py (亻 left half is nearly identical).

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
    # Stroke 1: 撇 — pie sweep from upper part of left zone down-left.
    bezier_stroke(d,
                  to_px(-60, 100),
                  to_px(-85, 15),
                  to_px(-110, -85),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu, head touching pie mid-shaft. Shorter than 亻's pie.
    line_stroke(d,
                to_px(-62, 35),
                to_px(-62, -95),
                w_head=6, w_tail=5, n=40)

    # ---------- 吊 (right side) — 口 top + 巾 bottom ----------
    # 口 (top box): 3 strokes — left shu, top heng+heng-fold-shu, bottom heng.
    # Box roughly x=[15,75], y=[60,105]. Small compact box.
    # Stroke 3: left shu of 口
    line_stroke(d, to_px(15, 105), to_px(15, 60), w_head=5, w_tail=5, n=25)
    # Stroke 4: 横折 (heng across top, fold down to right shu)
    line_stroke(d, to_px(15, 105), to_px(75, 105), w_head=5, w_tail=5, n=25)
    line_stroke(d, to_px(75, 105), to_px(75, 60), w_head=5, w_tail=5, n=25)
    # Stroke 5: bottom heng of 口
    line_stroke(d, to_px(15, 60), to_px(75, 60), w_head=5, w_tail=5, n=25)

    # 巾 (bottom): 3 strokes — top heng (wider), left short pie/shu, center shu long.
    # 巾 top heng is wider than 口, and sits just below 口.
    # Stroke 6: heng across top of 巾 (wider than 口)
    line_stroke(d, to_px(-15, 30), to_px(105, 30), w_head=5, w_tail=5, n=30)

    # Stroke 7: left short shu of 巾 — going down from left end of heng, small flick.
    bezier_stroke(d,
                  to_px(0, 30),
                  to_px(-5, -20),
                  to_px(-20, -60),
                  w_head=5, w_tail=2, n=35)

    # Stroke 8: center shu (long, straight, extends far down)
    line_stroke(d, to_px(45, 45), to_px(45, -115), w_head=6, w_tail=5, n=40)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_伄.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
