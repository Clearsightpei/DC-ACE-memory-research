# p3_char_0332_佐 — G3 attempt.
# 佐 = 亻 (left, 2 strokes: pie + shu) + 左 (right, 5 strokes: heng + pie + 工).
# Total: 7 strokes.
#   Left 亻: standard ren_pang layout inlined (pie sweeping down-left,
#            short shu touching pie mid-shaft).
#   Right 左 (per GT):
#     s3: 一   short slanting heng, upper-right region.
#     s4: 丿   pie descending down-left through/from left end of s3, sweeping
#              to the lower-left of the right slot.
#     s5: 一   短横 top of 工 (short horizontal, mid of right slot).
#     s6: 丨   short shu.
#     s7: 一   bottom heng, widest, forms base.
# GT shows thin MMH-style lines — keep widths modest (~4-6 px) per drawer_memory.

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
    # Stroke 1: 撇 — pie from upper-mid-left sweeping down-left.
    bezier_stroke(d,
                  to_px(-70, 100),
                  to_px(-90, 15),
                  to_px(-115, -90),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — short vertical, head touching pie mid-shaft.
    line_stroke(d,
                to_px(-72, 35),
                to_px(-72, -105),
                w_head=5, w_tail=5, n=40)

    # ---------- 左 (right side) ----------
    # Stroke 3: 一 — short slanting heng, slightly rising left-to-right.
    line_stroke(d,
                to_px(-20, 78),
                to_px(75, 90),
                w_head=5, w_tail=5, n=40)

    # Stroke 4: 丿 — long pie descending from just left of heng start
    #                 down-left through into the 工 region on the right slot.
    bezier_stroke(d,
                  to_px(20, 105),
                  to_px(-5, 15),
                  to_px(-30, -100),
                  w_head=6, w_tail=2, n=55)

    # ---------- 工 (bottom-right of 左) ----------
    # Stroke 5: short top heng of 工.
    line_stroke(d,
                to_px(0, 0),
                to_px(70, 0),
                w_head=5, w_tail=5, n=30)

    # Stroke 6: short shu of 工.
    line_stroke(d,
                to_px(35, 0),
                to_px(35, -70),
                w_head=5, w_tail=5, n=30)

    # Stroke 7: bottom heng of 工 — widest, forms base.
    line_stroke(d,
                to_px(-20, -70),
                to_px(95, -70),
                w_head=6, w_tail=5, n=40)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佐.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
