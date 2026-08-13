# p3_char_0340_佚 — G3 attempt.
# 佚 = 亻 (left, 2 strokes: pie + shu) + 失 (right, 5 strokes: pie + heng + heng + pie + na).
# Total 7 strokes.
# GT shows thin MMH lines (~4-6 px). L-R split: 亻 ~ left third, 失 ~ right two-thirds.
# 亻 recipe adapted from bank fu_pay.py (paid PASS).
# 失 side: known errata pattern — the pie/na apex must sit ON the middle heng, not float above.

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
    # Stroke 1: 撇 — pie from upper-mid down-left.
    bezier_stroke(d,
                  to_px(-55, 95),
                  to_px(-78, 5),
                  to_px(-100, -90),
                  w_head=6, w_tail=2, n=55)
    # Stroke 2: 竖 — vertical shu meeting pie ~ mid-shaft.
    line_stroke(d,
                to_px(-58, 25),
                to_px(-58, -115),
                w_head=6, w_tail=5, n=40)

    # ---------- 失 (right side) ----------
    # 失 layout (right two-thirds, x from ~ -20 to 105).
    # Middle heng at y = 25 (apex line). Top heng at y = 65 (shorter).
    # Small 撇 above at top. Pie+na descending from apex on middle heng.

    # Stroke 3: 短撇 — small pie at top, above the top heng.
    bezier_stroke(d,
                  to_px(45, 115),
                  to_px(38, 105),
                  to_px(25, 90),
                  w_head=5, w_tail=2, n=25)

    # Stroke 4: 上横 — shorter top heng.
    line_stroke(d,
                to_px(5, 70),
                to_px(75, 70),
                w_head=5, w_tail=5, n=30)

    # Stroke 5: 中横 (long) — the long middle heng where pie/na apex lands.
    line_stroke(d,
                to_px(-20, 25),
                to_px(100, 25),
                w_head=5, w_tail=5, n=40)

    # Apex point where pie & na kiss — ON the middle heng, slightly right of center.
    APEX = to_px(50, 25)

    # Stroke 6: 撇 — pie from apex descending down-left, curving out.
    bezier_stroke(d,
                  APEX,
                  to_px(20, -25),
                  to_px(-15, -110),
                  w_head=6, w_tail=2, n=55)

    # Stroke 7: 捺 — na descending down-right from apex, thicker tail flaring out.
    bezier_stroke(d,
                  APEX,
                  to_px(75, -30),
                  to_px(110, -115),
                  w_head=4, w_tail=8, n=55)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佚.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
