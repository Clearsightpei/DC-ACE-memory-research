# p3_char_0179_付 — G3 attempt.
# 付 = 亻 (left person radical, 2 strokes: pie + shu) + 寸 (right, 3 strokes:
#     heng + shu_gou + dian). 5 strokes total.
# GT shows thin, MMH-style lines — keep widths modest (~4-6 px).
# 亻 sits on the left third; 寸 sits on the right two-thirds.

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
    # Stroke 1: 撇 — pie sweep from upper part of left zone down-left to lower-left.
    # Head near (-50, +95), sweep through (-72, 10), tail near (-95, -85).
    bezier_stroke(d,
                  to_px(-50, 95),
                  to_px(-72, 10),
                  to_px(-95, -85),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu, head touching pie mid-shaft (~ y=30), tail low.
    line_stroke(d,
                to_px(-52, 30),
                to_px(-52, -110),
                w_head=6, w_tail=5, n=40)

    # ---------- 寸 (right side) ----------
    # Stroke 3: 一 (heng) — long horizontal, upper part of right zone.
    line_stroke(d,
                to_px(-5, 45),
                to_px(100, 45),
                w_head=5, w_tail=5, n=40)

    # Stroke 4: 亅 (shu_gou) — vertical crossing heng, then small hook to upper-left.
    line_stroke(d,
                to_px(48, 85),
                to_px(48, -95),
                w_head=6, w_tail=6, n=40)
    # Hook flick (short bezier lifting left-up at the bottom, slightly larger)
    bezier_stroke(d,
                  to_px(48, -95),
                  to_px(40, -88),
                  to_px(25, -75),
                  w_head=6, w_tail=1, n=25)

    # Stroke 5: 丶 (dian) — dot in lower-left pocket, below heng, left of shu_gou.
    # In the GT it's clearly visible around mid-height of the shu_gou below heng.
    bezier_stroke(d,
                  to_px(10, 5),
                  to_px(22, -5),
                  to_px(35, -18),
                  w_head=3, w_tail=8, n=25)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_付.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
