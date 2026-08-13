# BANK_DEVIATION
# skipped: ren_pang.py (bank primitive pie+shu composition)
# reason: fu_pay pattern shows GT of 亻+X characters wants thin (~4-6px)
#         inline bezier pie with tail sweeping to lower-left, not the
#         compressed bank pie; also 佯 needs 亻 sized to match a 6-stroke
#         right side, requiring finer control than (ox,oy,scale) allows.
# fresh_component: yang_char_inline (亻 + 羊 inline PIL, MMH-thin widths)
#
# 佯 = 亻 (left, 2 strokes: pie + shu) + 羊 (right, 6 strokes:
#   two dots forming 丷 + three heng + one long vertical shu). 8 strokes total.
# Following the fu_pay recipe: PIL inline, thin widths ~4-6, gently tapered pie.

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

    # ---------- 亻 (left radical, occupies left ~1/3) ----------
    # Stroke 1: pie — head upper of the radical zone, sweep to lower-left.
    # Tightened to fit within canvas; GT shows pie contained, not off-edge.
    bezier_stroke(d,
                  to_px(-55, 105),
                  to_px(-78, 30),
                  to_px(-100, -70),
                  w_head=6, w_tail=2, n=55)
    # Stroke 2: shu — vertical, touching pie mid-shaft.
    line_stroke(d,
                to_px(-58, 40),
                to_px(-58, -95),
                w_head=5, w_tail=5, n=40)

    # ---------- 羊 (right side, occupies right ~2/3) ----------
    # Right side center vertical axis around x=+35.
    # Stroke 3: left dot (丶) — top of 丷, short pie-like going down-left.
    bezier_stroke(d,
                  to_px(0, 115),
                  to_px(-8, 100),
                  to_px(-18, 80),
                  w_head=3, w_tail=6, n=25)
    # Stroke 4: right dot (丿-ish) — top of 丷, short flick going down-right.
    bezier_stroke(d,
                  to_px(60, 115),
                  to_px(68, 100),
                  to_px(78, 80),
                  w_head=3, w_tail=6, n=25)

    # Stroke 5: top heng — short-ish, sits below the two dots.
    line_stroke(d,
                to_px(-15, 55),
                to_px(80, 55),
                w_head=5, w_tail=5, n=40)

    # Stroke 6: middle heng — similar length or slightly shorter than top.
    line_stroke(d,
                to_px(-15, 0),
                to_px(80, 0),
                w_head=5, w_tail=5, n=40)

    # Stroke 7: bottom heng — longest, defines the base width.
    line_stroke(d,
                to_px(-35, -55),
                to_px(105, -55),
                w_head=5, w_tail=5, n=40)

    # Stroke 8: vertical shu — from just above top heng down through bottom heng,
    # exits well below (this is the long tail of 羊).
    line_stroke(d,
                to_px(35, 75),
                to_px(35, -125),
                w_head=5, w_tail=5, n=50)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佯.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
