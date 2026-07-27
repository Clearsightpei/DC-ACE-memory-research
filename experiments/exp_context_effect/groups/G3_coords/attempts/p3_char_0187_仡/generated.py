# p3_char_0187_仡 — G3 attempt.
# 仡 = 亻 (left, 2 strokes: pie + shu) + 乞 (right, 3 strokes: short pie,
#     heng, and 乙-shape ending with rightward flick).
# 5 strokes total. GT is thin MMH-style — widths ~4-6 px.
# Composition patterned after fu_pay.py (亻 + right-side component).

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


def cubic_stroke(draw, p0, p1, p2, p3, w_head, w_tail, n=60):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = ((1 - u) ** 3 * p0[0] + 3 * (1 - u) ** 2 * u * p1[0]
              + 3 * (1 - u) * u ** 2 * p2[0] + u ** 3 * p3[0])
        by = ((1 - u) ** 3 * p0[1] + 3 * (1 - u) ** 2 * u * p1[1]
              + 3 * (1 - u) * u ** 2 * p2[1] + u ** 3 * p3[1])
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
    # Stroke 1: 撇 sweep
    bezier_stroke(d,
                  to_px(-55, 100),
                  to_px(-78, 15),
                  to_px(-100, -85),
                  w_head=6, w_tail=2, n=55)
    # Stroke 2: 竖 vertical, head touching mid-shaft of pie
    line_stroke(d,
                to_px(-58, 30),
                to_px(-58, -115),
                w_head=6, w_tail=5, n=40)

    # ---------- 乞 (right side) ----------
    # Stroke 3: short 撇 at top — slanting down-left
    bezier_stroke(d,
                  to_px(65, 100),
                  to_px(35, 85),
                  to_px(5, 65),
                  w_head=6, w_tail=3, n=30)

    # Stroke 4: 一 heng — mid horizontal spanning the right zone
    line_stroke(d,
                to_px(-5, 35),
                to_px(95, 40),
                w_head=5, w_tail=5, n=40)

    # Stroke 5: 乙 — one continuous curve: descends from upper-left,
    # bows leftward, sweeps along the bottom, and lifts with a rightward
    # flick at the end.
    cubic_stroke(d,
                 to_px(10, 15),
                 to_px(-10, -30),
                 to_px(-15, -75),
                 to_px(15, -95),
                 w_head=5, w_tail=5, n=80)
    cubic_stroke(d,
                 to_px(15, -95),
                 to_px(50, -105),
                 to_px(85, -95),
                 to_px(100, -75),
                 w_head=5, w_tail=6, n=60)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_仡.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
