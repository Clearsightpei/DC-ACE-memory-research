# p3_char_0252_伊 — G3 attempt.
# 伊 = 亻 (left person radical: 2 strokes pie+shu) +
#     尹 (right: 4 strokes — heng-zhe top, middle heng, third heng, long pie descending)
# GT shows thin MMH-style lines (~4-6 px), thin uniform widths.
# Left column: 亻 (pie sweep + vertical shu, tall).
# Right column: 尹 — top "cap" heng that turns down at right, then a middle heng,
#   then a shorter heng, all crossed by a long descending pie that starts upper-right
#   and sweeps down to lower-left below 亻.

import os
from PIL import Image, ImageDraw

CANVAS = 300
CX = CY = CANVAS // 2


def to_px(x, y):
    return (CX + x, CY - y)


def bezier_stroke(draw, p0, p1, p2, w_head, w_tail, n=45):
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


def line_stroke(draw, p0, p1, w_head, w_tail, n=30):
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
    # Stroke 1: pie sweep from upper part of left zone down-left.
    bezier_stroke(d,
                  to_px(-50, 90),
                  to_px(-70, 15),
                  to_px(-90, -70),
                  w_head=6, w_tail=2, n=55)
    # Stroke 2: shu vertical, touching pie mid-shaft.
    line_stroke(d,
                to_px(-53, 25),
                to_px(-53, -95),
                w_head=5, w_tail=4, n=40)

    # ---------- 尹 (right side, 4 strokes) ----------
    # Stroke 3: small 撇 at top of 尹 (short down-left flick).
    bezier_stroke(d,
                  to_px(30, 115),
                  to_px(22, 105),
                  to_px(10, 90),
                  w_head=5, w_tail=2, n=25)

    # Stroke 4: 横折 — top heng from left going right, then folding down
    # into a short vertical on the right side of 尹.
    line_stroke(d,
                to_px(-5, 75),
                to_px(80, 75),
                w_head=5, w_tail=5, n=30)
    line_stroke(d,
                to_px(80, 75),
                to_px(80, 40),
                w_head=5, w_tail=4, n=15)

    # Stroke 5: middle 横 — from left of right zone to right, at mid-height.
    line_stroke(d,
                to_px(-15, 30),
                to_px(75, 30),
                w_head=5, w_tail=5, n=30)

    # Stroke 6: long 撇 — starts from upper-right area, sweeps down-left
    # crossing through the hengs, ending in lower-left.
    bezier_stroke(d,
                  to_px(60, 100),
                  to_px(25, -15),
                  to_px(-30, -110),
                  w_head=6, w_tail=2, n=60)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_伊.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
