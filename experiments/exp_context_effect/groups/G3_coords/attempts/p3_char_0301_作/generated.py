# p3_char_0301_作 — G3 attempt.
# 作 = 亻 (left, 2 strokes: pie + shu) + 乍 (right, 5 strokes:
#     short pie top + short heng top + long shu descending +
#     middle heng + bottom heng). 7 strokes total.
# GT shows thin uniform MMH lines. Follow the 付 (fu_pay) pattern:
# inline PIL, thin widths (~5), 亻 on left third, right component on
# right two-thirds.

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
    # Stroke 1: 撇 — pie sweep from upper mid-left down to lower-left.
    bezier_stroke(d,
                  to_px(-55, 100),
                  to_px(-80, 15),
                  to_px(-105, -95),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical, head on pie mid-shaft, tail down.
    line_stroke(d,
                to_px(-58, 35),
                to_px(-58, -115),
                w_head=6, w_tail=5, n=40)

    # ---------- 乍 (right component) ----------
    # Stroke 3: 短撇 — short pie at top-left of the right component,
    # sloping down-left. Starts at the top-left corner where heng begins.
    bezier_stroke(d,
                  to_px(30, 108),
                  to_px(18, 75),
                  to_px(8, 40),
                  w_head=5, w_tail=2, n=30)

    # Stroke 4: 短横 — short heng at top of right component, joining
    # the pie's start (top-left corner) and going right.
    line_stroke(d,
                to_px(30, 105),
                to_px(108, 100),
                w_head=5, w_tail=5, n=30)

    # Stroke 5: 长竖 — long vertical descending through the right
    # component. Starts inside the top heng, goes down to bottom.
    line_stroke(d,
                to_px(60, 100),
                to_px(60, -110),
                w_head=6, w_tail=5, n=40)

    # Stroke 6: 中横 — middle horizontal, attached to shu, going right.
    line_stroke(d,
                to_px(60, 25),
                to_px(115, 22),
                w_head=5, w_tail=5, n=30)

    # Stroke 7: 底横 — bottom horizontal, attached to shu, going right.
    line_stroke(d,
                to_px(60, -50),
                to_px(115, -53),
                w_head=5, w_tail=5, n=30)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_作.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
