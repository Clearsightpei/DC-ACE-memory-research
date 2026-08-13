# p3_char_0396_佴 — G3 attempt.
# 佴 = 亻 (left person radical, 2 strokes: pie + shu) + 耳 (right, 6 strokes:
#     top heng, left shu, two inner heng, right shu (extends below), long
#     bottom heng).
# GT shows thin MMH-style lines with mildly cursive/loose feel. Widths ~4-6 px.
# 亻 sits on left ~30% of canvas; 耳 fills the right ~60%.
#
# Recipe: inline PIL, following fu_pay.py pattern (a B6 PASS).

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
    # Stroke 1: 撇 — pie sweep from upper-left area down-left.
    bezier_stroke(d,
                  to_px(-70, 95),
                  to_px(-92, 5),
                  to_px(-115, -90),
                  w_head=5, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu, head touching pie mid-shaft (~y=25), tail low.
    line_stroke(d,
                to_px(-72, 25),
                to_px(-72, -115),
                w_head=5, w_tail=4, n=40)

    # ---------- 耳 (right side) ----------
    # 耳 rectangular frame with two inner horizontals, right shu extending below,
    # bottom heng longest.
    # Frame: left shu at x=-20, right shu at x=+70.
    # Top heng at y=90, middle inner heng at y=45, lower inner heng at y=0,
    # bottom heng at y=-55 (longest), right shu extends to y=-115.

    # Stroke 3: top 横
    line_stroke(d,
                to_px(-20, 90),
                to_px(70, 90),
                w_head=5, w_tail=5, n=40)

    # Stroke 4: left 竖 (short — from top down to bottom heng)
    line_stroke(d,
                to_px(-20, 92),
                to_px(-20, -55),
                w_head=5, w_tail=5, n=40)

    # Stroke 5: upper inner 横
    line_stroke(d,
                to_px(-15, 40),
                to_px(65, 40),
                w_head=4, w_tail=4, n=30)

    # Stroke 6: lower inner 横
    line_stroke(d,
                to_px(-15, -10),
                to_px(65, -10),
                w_head=4, w_tail=4, n=30)

    # Stroke 7: right 竖 (extends below the bottom heng — the tail of 耳)
    line_stroke(d,
                to_px(70, 92),
                to_px(70, -115),
                w_head=5, w_tail=5, n=45)

    # Stroke 8: bottom 横 — longest, extends beyond the frame on both sides
    line_stroke(d,
                to_px(-45, -55),
                to_px(105, -55),
                w_head=5, w_tail=5, n=50)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佴.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
