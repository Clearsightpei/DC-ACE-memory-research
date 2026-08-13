# p3_char_0533_值 — G3 attempt.
# 值 = 亻 (left, 2 strokes) + 直 (right, 8 strokes) = 10 strokes total.
# 直 = 一 (top wide heng) + 丨 (long shu through top heng)
#     + 横折 (top-right corner of 目)
#     + 三 (three inner hengs of 目, the bottom one closes the frame)
#     + 一 (bottom wide heng, widest of all).
# Recipe adapted from zhan_char.py (亻 side with bezier pie + shu),
# right side is a fresh inline 直 (no bank entry for 直).
# Bank primitive ren_pang uses turtle-only signature; here we inline
# the 亻 in PIL to keep left+right in one draw context. Not a
# BANK_DEVIATION — this is the standard 亻-inline pattern that
# fu_pay / zhan / yong / ka / hua all use in the bank.

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
    # Stroke 1: 撇 — pie sweep from upper part of left zone down-left.
    bezier_stroke(d,
                  to_px(-70, 105),
                  to_px(-92, 15),
                  to_px(-118, -100),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu, head touching pie mid-shaft, tail low.
    line_stroke(d,
                to_px(-72, 35),
                to_px(-72, -110),
                w_head=5, w_tail=5, n=40)

    # ---------- 直 (right side) ----------
    # Layout: right slot spans x ~ [-40, +115]
    # Top heng at y=115, bottom heng at y=-115, 目 frame in middle.

    # Stroke 3: 一 (top heng) — wide, spans top of right slot.
    line_stroke(d,
                to_px(-40, 110),
                to_px(90, 110),
                w_head=5, w_tail=5, n=30)

    # Stroke 4: 丨 (long shu) — descends from top heng downward through
    # the frame; slightly left of center of right slot.
    line_stroke(d,
                to_px(-5, 110),
                to_px(-5, -85),
                w_head=5, w_tail=5, n=40)

    # Stroke 5: 横折 — top of 目 frame + right vertical.
    #   part A: short top heng (right side of frame top) from shu to right edge.
    line_stroke(d,
                to_px(-5, 55),
                to_px(85, 55),
                w_head=5, w_tail=5, n=25)
    #   part B: right vertical going down.
    line_stroke(d,
                to_px(85, 55),
                to_px(85, -85),
                w_head=5, w_tail=5, n=35)

    # Stroke 6: 一 — first inner heng of 目 (middle bar).
    line_stroke(d,
                to_px(-5, 15),
                to_px(85, 15),
                w_head=4, w_tail=5, n=25)

    # Stroke 7: 一 — second inner heng of 目 (middle bar).
    line_stroke(d,
                to_px(-5, -30),
                to_px(85, -30),
                w_head=4, w_tail=5, n=25)

    # Stroke 8: 一 — bottom heng of 目 frame (closes the box).
    line_stroke(d,
                to_px(-5, -85),
                to_px(85, -85),
                w_head=5, w_tail=5, n=25)

    # Stroke 9: 一 (bottom wide heng) — widest of all, sits below the
    # 目 frame; extends beyond both frame edges.
    line_stroke(d,
                to_px(-40, -115),
                to_px(105, -115),
                w_head=5, w_tail=6, n=30)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(out_dir, "01_值.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
