# p3_char_0192_代 — G3 attempt.
# 代 = 亻 (left, 2 strokes: 撇 + 竖) + 弋 (right, 3 strokes: 横 + 斜钩 + 点)
# 5 strokes total. GT shows thin MMH-style lines (~4-6 px widths).
# 亻 sits on the left third; 弋 sits on the right two-thirds.
# 弋's 斜钩 is the dominant stroke — long slanted curve from upper-left
# of right zone sweeping down-right, ending with a small upward hook.

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
    # Stroke 1: 撇 — sweep from upper-mid down-left
    bezier_stroke(d,
                  to_px(-55, 95),
                  to_px(-78, 10),
                  to_px(-100, -90),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical, head touches pie mid-shaft
    line_stroke(d,
                to_px(-58, 30),
                to_px(-58, -115),
                w_head=6, w_tail=5, n=40)

    # ---------- 弋 (right side) ----------
    # Stroke 3: 短横 — short horizontal near upper part of right zone, slightly tilted up-right
    line_stroke(d,
                to_px(-5, 60),
                to_px(55, 68),
                w_head=5, w_tail=5, n=30)

    # Stroke 4: 斜钩 (xie_gou) — long slanted stroke from upper-left of right zone
    # curving down and to the right, ending with a small upward hook.
    # Head near the intersection with the heng, tail near bottom-right.
    bezier_stroke(d,
                  to_px(-25, 95),
                  to_px(30, -20),
                  to_px(95, -100),
                  w_head=5, w_tail=6, n=60)
    # Hook flick at the bottom — short curve going up-right
    bezier_stroke(d,
                  to_px(95, -100),
                  to_px(100, -85),
                  to_px(105, -65),
                  w_head=6, w_tail=1, n=25)

    # Stroke 5: 点 (dian) — small tick at top-right of 弋, going up-right
    bezier_stroke(d,
                  to_px(70, 95),
                  to_px(78, 105),
                  to_px(88, 118),
                  w_head=6, w_tail=2, n=20)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_代.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
