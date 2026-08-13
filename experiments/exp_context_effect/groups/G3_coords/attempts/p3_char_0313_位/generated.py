# p3_char_0313_位 — G3 attempt.
# 位 = 亻 (left person radical, 2 strokes: pie + shu) + 立 (right, 5 strokes:
#     dian top + short heng + left dian + right dian + long bottom heng)
# 7 strokes total. GT shows thin, MMH-style lines — widths ~4-6 px.
# 亻 on left ~1/3; 立 on right ~2/3, centered right of ren_pang shu.

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
    # Stroke 1: 撇 — pie sweep, more compact.
    bezier_stroke(d,
                  to_px(-55, 90),
                  to_px(-72, 15),
                  to_px(-90, -70),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu, head touching pie mid-shaft.
    line_stroke(d,
                to_px(-57, 25),
                to_px(-57, -95),
                w_head=6, w_tail=5, n=40)

    # ---------- 立 (right side) ----------
    # Stroke 3: 丶 (top dian) — small dot centered above short heng.
    bezier_stroke(d,
                  to_px(25, 95),
                  to_px(28, 85),
                  to_px(32, 72),
                  w_head=3, w_tail=6, n=20)

    # Stroke 4: 一 (short heng, upper) — short horizontal below top dian.
    line_stroke(d,
                to_px(5, 45),
                to_px(60, 45),
                w_head=5, w_tail=5, n=40)

    # Stroke 5: 丶 (left dian) — small dot lower-left of middle area.
    bezier_stroke(d,
                  to_px(5, 20),
                  to_px(0, 5),
                  to_px(-5, -10),
                  w_head=3, w_tail=6, n=20)

    # Stroke 6: 丶 (right dian, slanting into center) — small dot right side.
    bezier_stroke(d,
                  to_px(55, 20),
                  to_px(50, 5),
                  to_px(45, -10),
                  w_head=3, w_tail=6, n=20)

    # Stroke 7: 一 (long bottom heng) — long horizontal, right zone only.
    line_stroke(d,
                to_px(-15, -55),
                to_px(95, -55),
                w_head=5, w_tail=5, n=40)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_位.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
