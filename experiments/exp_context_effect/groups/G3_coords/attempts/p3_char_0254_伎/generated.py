# p3_char_0254_伎 — G3 attempt.
# 伎 = 亻 (left, 2 strokes: pie + shu) + 支 (right, 4 strokes: heng + shu +
#     横撇 + 捺). 6 strokes total.
# GT shows thin MMH-style ink — keep widths ~4-6 px.
# 亻 sits on the left third; 支 sits on the right two-thirds.

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
                  to_px(-55, 100),
                  to_px(-78, 15),
                  to_px(-100, -90),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu meeting pie mid-shaft (shorter, ends near pie tail).
    line_stroke(d,
                to_px(-57, 30),
                to_px(-57, -95),
                w_head=6, w_tail=5, n=40)

    # ---------- 支 (right side) ----------
    # Stroke 3: 一 (top heng) — short horizontal near top of right zone.
    line_stroke(d,
                to_px(-5, 95),
                to_px(75, 95),
                w_head=5, w_tail=5, n=30)

    # Stroke 4: 丨 (short shu) — vertical dropping from heng center down.
    line_stroke(d,
                to_px(35, 95),
                to_px(35, 15),
                w_head=6, w_tail=5, n=30)

    # Stroke 5: 横撇 — horizontal segment then hooking down-left as pie.
    # Horizontal part
    line_stroke(d,
                to_px(-10, 15),
                to_px(80, 15),
                w_head=5, w_tail=5, n=30)
    # Descending pie continuation from right end of the heng, sweeping left-down.
    bezier_stroke(d,
                  to_px(80, 15),
                  to_px(40, -50),
                  to_px(-40, -110),
                  w_head=6, w_tail=2, n=55)

    # Stroke 6: 捺 — na sweeping from mid-upper down to lower-right.
    bezier_stroke(d,
                  to_px(10, 5),
                  to_px(55, -50),
                  to_px(105, -105),
                  w_head=3, w_tail=8, n=45)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_伎.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
