# p3_char_0264_伢 — G3 attempt (revision 1).
# 伢 = 亻 (left, 2 strokes) + 牙 (right, 4 strokes: heng_pie top, heng_zhe,
#     long pie, shu_gou). 6 strokes total.
# Revision notes: initial render was missing the long 撇 sweep on 牙 —
# strengthened it and shifted the whole layout to give 牙 more room.

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
    # Stroke 1: 撇 — pie sweep upper-mid down to lower-left.
    bezier_stroke(d,
                  to_px(-75, 95),
                  to_px(-95, 5),
                  to_px(-115, -90),
                  w_head=5, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu, head touching pie mid-shaft.
    line_stroke(d,
                to_px(-78, 25),
                to_px(-78, -110),
                w_head=5, w_tail=5, n=40)

    # ---------- 牙 (right side) ----------
    # Stroke 1: small 撇/横 at top-left corner of 牙 — slants down-right
    line_stroke(d,
                to_px(-15, 85),
                to_px(25, 65),
                w_head=5, w_tail=4, n=25)

    # Stroke 2: 横折 — horizontal top, then turns down (forming the shu_gou top).
    line_stroke(d,
                to_px(-10, 45),
                to_px(80, 45),
                w_head=5, w_tail=5, n=30)
    # The 折 down segment
    line_stroke(d,
                to_px(80, 45),
                to_px(75, 20),
                w_head=5, w_tail=5, n=15)

    # Stroke 3: 长撇 — long pie sweeping from just right of top-horizontal
    # down through the middle to lower-left. This is the diagnostic 牙 stroke.
    bezier_stroke(d,
                  to_px(25, 65),
                  to_px(-5, -20),
                  to_px(-40, -115),
                  w_head=6, w_tail=2, n=55)

    # Stroke 4: 竖钩 — vertical from the fold down with hook at bottom-left.
    line_stroke(d,
                to_px(75, 20),
                to_px(60, -115),
                w_head=5, w_tail=5, n=40)
    # small hook lifting up-left at bottom
    bezier_stroke(d,
                  to_px(60, -115),
                  to_px(48, -108),
                  to_px(35, -100),
                  w_head=5, w_tail=1, n=20)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_伢.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
