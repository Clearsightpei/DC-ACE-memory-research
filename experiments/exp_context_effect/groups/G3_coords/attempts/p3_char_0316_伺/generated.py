# p3_char_0316_伺 — G3 attempt.
# 伺 = 亻 (left, 2 strokes: 撇 + 竖) + 司 (right, 5 strokes:
#       横折钩 envelope + inner 一 + 口 [竖 + 横折 + 横]).
# 7 strokes total. L-R composition per B6/B7 pattern
# (ren_pang-style left compressed, inline thin right).
# GT shows thin MMH-style lines; widths ~4-6 px.

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


def draw_si_char(draw, ox=0, oy=0, scale=1.0):
    """Callable: renders 伺 into draw at math-coord offset (ox,oy)."""
    def T(x, y):
        return to_px(ox + x * scale, oy + y * scale)

    # ---------- 亻 (left radical, compressed) ----------
    # 撇 — pie head high-left of person, sweep down-left.
    bezier_stroke(draw,
                  T(-55, 100),
                  T(-78, 15),
                  T(-100, -80),
                  w_head=6, w_tail=2, n=55)
    # 竖 — vertical, top touches pie mid-shaft.
    line_stroke(draw,
                T(-58, 30),
                T(-58, -110),
                w_head=6, w_tail=5, n=40)

    # ---------- 司 (right, inline) ----------
    # Stroke 1: 横折钩 — top heng, right vertical, hook flick UP-LEFT at bottom.
    # top heng
    line_stroke(draw,
                T(-25, 100),
                T(110, 100),
                w_head=5, w_tail=5, n=40)
    # right vertical (down)
    line_stroke(draw,
                T(110, 100),
                T(110, -95),
                w_head=5, w_tail=5, n=40)
    # hook flick at bottom — UP-LEFT
    bezier_stroke(draw,
                  T(110, -95),
                  T(100, -85),
                  T(80, -75),
                  w_head=5, w_tail=1, n=25)

    # Stroke 2: 一 (inner heng) — mid-height, from left edge (open side) to right vertical.
    line_stroke(draw,
                T(-15, 25),
                T(100, 25),
                w_head=4, w_tail=4, n=40)

    # ---------- 口 (inside, lower half of 司) ----------
    # 口 sits in the lower interior, small.
    # Corners: TL (-5, -10), TR (85, -10), BL (-5, -75), BR (85, -75)
    # Stroke 3: 竖 — left side of mouth (top-down)
    line_stroke(draw,
                T(-5, -5),
                T(-5, -75),
                w_head=4, w_tail=4, n=25)
    # Stroke 4: 横折 — top heng + right shu (one stroke, elbow at TR)
    line_stroke(draw,
                T(-5, -5),
                T(85, -5),
                w_head=4, w_tail=4, n=25)
    line_stroke(draw,
                T(85, -5),
                T(85, -75),
                w_head=4, w_tail=4, n=25)
    # Stroke 5: 横 — bottom heng closing the mouth
    line_stroke(draw,
                T(-5, -75),
                T(85, -75),
                w_head=4, w_tail=4, n=25)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_si_char(d)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_伺.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
