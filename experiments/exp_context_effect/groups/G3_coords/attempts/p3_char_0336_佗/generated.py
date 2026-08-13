# p3_char_0336_佗 — G3 attempt.
# 佗 (tuō) = 亻 (left person radical, 2 strokes: pie + shu) + 它 (right, 5 strokes:
#     dian + heng_gou (roof) + pie + shu_wan_gou). Total ~5-7 strokes.
# GT is thin uniform MMH-style lines. Follow fu_pay.py recipe:
#   inline PIL, ~4-6 px widths, math coords via to_px.
# Layout: 亻 on left ~35% width, 它 on right ~65% width.

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

    # ---------- 亻 (left radical, ~ x=-120 to -35) ----------
    # Stroke 1: 撇 — pie from upper (-55, 95) sweeping down-left to (-115, -85)
    bezier_stroke(d,
                  to_px(-55, 95),
                  to_px(-80, 10),
                  to_px(-115, -85),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu touching pie mid-shaft
    line_stroke(d,
                to_px(-58, 25),
                to_px(-58, -115),
                w_head=6, w_tail=5, n=40)

    # ---------- 它 (right side, ~ x=-15 to 115) ----------
    # Stroke 3: 点 — small dian on top of 宀 roof, going down-right
    bezier_stroke(d,
                  to_px(45, 118),
                  to_px(50, 108),
                  to_px(58, 98),
                  w_head=3, w_tail=7, n=20)

    # Stroke 4: 横钩 — wide horizontal along top, ending with small down-left hook
    # Horizontal main
    line_stroke(d,
                to_px(-15, 80),
                to_px(105, 80),
                w_head=5, w_tail=5, n=40)
    # Hook: down-left from right endpoint
    line_stroke(d,
                to_px(105, 80),
                to_px(95, 62),
                w_head=5, w_tail=2, n=15)

    # Stroke 5: 撇 — long pie starting near roof-left, sweeping down-left
    bezier_stroke(d,
                  to_px(10, 55),
                  to_px(-8, 0),
                  to_px(-25, -70),
                  w_head=6, w_tail=2, n=55)

    # Stroke 6: 竖弯钩 — vertical shaft on right, curves right along bottom, hooks up
    # Vertical shaft from ~ (35, 55) down to (35, -90)
    line_stroke(d,
                to_px(35, 55),
                to_px(35, -90),
                w_head=6, w_tail=5, n=40)
    # Curve rightward along the bottom
    bezier_stroke(d,
                  to_px(35, -90),
                  to_px(55, -115),
                  to_px(105, -110),
                  w_head=6, w_tail=6, n=40)
    # Hook flick upward at right end
    line_stroke(d,
                to_px(105, -110),
                to_px(108, -80),
                w_head=6, w_tail=2, n=20)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佗.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
