# p3_char_0297_你 — G3 attempt.
# 你 = 亻 (left person radical, 2 strokes: pie + shu) + 尔 (right, 5 strokes:
#       pie + heng_gou hat, then shu_gou vertical + inner pie + right dian).
# Total 7 strokes.
# Template follows fu_pay.py: PIL inline, thin MMH-style widths (~4-6 px),
# 亻 left ~35% width, right component ~65% width.

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
    # Stroke 1: 撇 (pie) — sweep from upper-left down-left.
    bezier_stroke(d,
                  to_px(-55, 100),
                  to_px(-78, 15),
                  to_px(-100, -80),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 (shu) — vertical touching pie mid-shaft.
    line_stroke(d,
                to_px(-58, 35),
                to_px(-58, -105),
                w_head=6, w_tail=5, n=40)

    # ---------- 尔 (right side) ----------
    # Stroke 3: 撇 (pie top) — short slant from apex (~ x=40, y=100) down-left.
    bezier_stroke(d,
                  to_px(40, 100),
                  to_px(20, 75),
                  to_px(0, 45),
                  w_head=5, w_tail=2, n=45)

    # Stroke 4: 横钩 (heng gou) — horizontal from apex sweeping right, ending
    # with a small down-left hook. Forms the "hat" over the body.
    line_stroke(d,
                to_px(40, 100),
                to_px(105, 90),
                w_head=5, w_tail=5, n=30)
    # hook: short flick down-left at the right end
    bezier_stroke(d,
                  to_px(105, 90),
                  to_px(100, 78),
                  to_px(90, 65),
                  w_head=5, w_tail=1, n=20)

    # Stroke 5: 竖钩 (shu gou) — long vertical down the middle of 尔, hooks left.
    line_stroke(d,
                to_px(52, 45),
                to_px(52, -100),
                w_head=6, w_tail=6, n=40)
    # hook flick at bottom, up-left
    bezier_stroke(d,
                  to_px(52, -100),
                  to_px(42, -92),
                  to_px(28, -82),
                  w_head=6, w_tail=1, n=25)

    # Stroke 6: 撇 (inner pie left of shu_gou) — starts near heng underside,
    # sweeps down-left.
    bezier_stroke(d,
                  to_px(30, 25),
                  to_px(15, -10),
                  to_px(0, -45),
                  w_head=5, w_tail=2, n=45)

    # Stroke 7: 丶 (dian on the right) — dot in the right pocket beside shu_gou.
    bezier_stroke(d,
                  to_px(75, 5),
                  to_px(90, -10),
                  to_px(105, -30),
                  w_head=3, w_tail=8, n=25)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_你.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
