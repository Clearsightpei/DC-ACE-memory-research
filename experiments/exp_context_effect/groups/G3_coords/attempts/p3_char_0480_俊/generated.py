# BANK_DEVIATION
# skipped: ren_pang.py
# reason: bank ren_pang uses turtle+bank strokes; this attempt is
#   pure-PIL inline (fu_pay.py pattern) for consistent thin MMH-like
#   widths across both radicals — mixing turtle + PIL adds friction
#   for no visual gain here.
# fresh_component: ren_pang_inline_for_俊
#
# p3_char_0480_俊 — G3 attempt.
# 俊 = 亻 (left, 2 strokes: pie + shu) + 夋 (right, 7 strokes).
# 夋 top: 厶-like corner (2 strokes: short pie + heng_pie)
#      mid: small 八 (pie + short dian)
#      bot: 夂 (short heng_pie + long pie + long na)
# Thin MMH-like widths ~3-5 px.

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
    # Stroke 1: 撇
    bezier_stroke(d,
                  to_px(-70, 95),
                  to_px(-92, 10),
                  to_px(-115, -85),
                  w_head=6, w_tail=2, n=55)
    # Stroke 2: 竖
    line_stroke(d,
                to_px(-72, 30),
                to_px(-72, -115),
                w_head=5, w_tail=4, n=40)

    # ---------- 夋 (right) ----------
    # Top 厶 (small angular): short pie + small heng-into-pie curve
    # Stroke 3: short pie (top-left of 厶)
    bezier_stroke(d,
                  to_px(20, 110),
                  to_px(5, 95),
                  to_px(-5, 78),
                  w_head=4, w_tail=2, n=25)
    # Stroke 4: 横撇 — small heng then downward hook forming right side of 厶
    line_stroke(d,
                to_px(-5, 100),
                to_px(45, 100),
                w_head=3, w_tail=4, n=15)
    bezier_stroke(d,
                  to_px(45, 100),
                  to_px(40, 88),
                  to_px(25, 70),
                  w_head=5, w_tail=2, n=25)

    # Middle 八 (small): left pie + right dian
    # Stroke 5: small pie (left of 八)
    bezier_stroke(d,
                  to_px(15, 55),
                  to_px(-5, 40),
                  to_px(-25, 25),
                  w_head=4, w_tail=2, n=25)
    # Stroke 6: small dian (right of 八)
    bezier_stroke(d,
                  to_px(35, 55),
                  to_px(50, 42),
                  to_px(65, 28),
                  w_head=2, w_tail=5, n=20)

    # Bottom 夂
    # Stroke 7: short heng-pie at top of 夂 — small 横 then pie down
    line_stroke(d,
                to_px(-15, 15),
                to_px(30, 15),
                w_head=3, w_tail=3, n=15)
    bezier_stroke(d,
                  to_px(30, 15),
                  to_px(15, -5),
                  to_px(-5, -25),
                  w_head=5, w_tail=2, n=25)

    # Stroke 8: long pie (main sweep from upper-right down to lower-left)
    bezier_stroke(d,
                  to_px(45, 30),
                  to_px(15, -35),
                  to_px(-40, -105),
                  w_head=6, w_tail=2, n=55)

    # Stroke 9: long na (sweep from mid-upper-left down to lower-right)
    bezier_stroke(d,
                  to_px(-25, -25),
                  to_px(25, -70),
                  to_px(90, -115),
                  w_head=3, w_tail=8, n=55)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_俊.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
