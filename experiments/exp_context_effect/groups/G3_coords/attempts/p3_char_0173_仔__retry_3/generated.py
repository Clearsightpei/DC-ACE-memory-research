# p3_char_0173_仔 — G3 retry #3.
# 仔 = 亻 (left, 2 strokes: pie + shu) + 子 (right, 3 strokes:
#     横撇钩 + 弯钩 + 横). 5 strokes total.
#
# TRAJECTORY DIFF (from viewing GT + all 3 prior FAIL PNGs):
#   main: right rendered as ㄋ — no crossing 横, no proper 弯钩.
#     Missing stroke 3 of 子, top too curly.
#   retry_1: closest — has 横撇钩 shape but 亻 shu too short (a
#     stub), 子 bottom disconnected from 弯钩, crossing 横 tiny.
#   retry_2: 子 rendered as 乞-shape — 横 didn't cross the descender,
#     descender missing hook, 亻 shu misplaced (wrong x offset).
#   Root cause across all 3: the 弯钩 (curved descender w/ terminal
#     hook-left) never lands right AND the crossing 横 either
#     misses or is too short to visually cross the descender.
#
# Q1 (errata): errata says "use zi_char (bank #122) verbatim on
#   the right, at scale ~0.65, ox=+40" — BUT retry_1 curator note
#   says zi_char never actually renders 弯钩 properly for this
#   composition. Under v8/v9: TRUST GT. Inline fresh à la fu_pay.
# Q2 (form_catalog): 亻-left needs pie sweep w=6→2 + short shu
#   full-height; 子 needs 横撇钩 w=5 + 弯钩 w=6→3 with clear hook +
#   long 横 crossing at mid-height.
# Q3 (helpers): none apply cleanly — inline PIL like fu_pay.py
#   (bank #182), which is the recipe that has PASSed for 亻+X.
# Fixes this attempt:
#   1. Make 亻 shu FULL LENGTH (retry_1 stub was too short).
#   2. Make 弯钩 a single continuous curve from top of 子 zone
#      down through crossing-heng level, ending with visible
#      left-flick hook.
#   3. Make 横 crossing WIDE and clearly through the descender,
#      at descender midheight.

import os
from PIL import Image, ImageDraw

CANVAS = 300
CX = CY = CANVAS // 2


def to_px(x, y):
    return (CX + x, CY - y)


def bezier_stroke(draw, p0, p1, p2, w_head, w_tail, n=50):
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
    # Stroke 1: 撇 — pie sweep upper-right to lower-left.
    bezier_stroke(d,
                  to_px(-55, 95),
                  to_px(-78, 15),
                  to_px(-105, -85),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 — vertical shu, head at pie mid-shaft. In GT it
    # extends roughly to the 子-crossing-heng height, not to the
    # very bottom. End near y=-55.
    line_stroke(d,
                to_px(-60, 30),
                to_px(-60, -60),
                w_head=6, w_tail=5, n=40)

    # ---------- 子 (right) ----------
    # Stroke 3: 横撇钩 — heng across top of right, then breaks
    # down-left into a short pie, with a small terminal hook.
    # Heng segment: (0, 80) -> (85, 80), thin.
    line_stroke(d,
                to_px(0, 80),
                to_px(85, 80),
                w_head=5, w_tail=5, n=30)
    # Pie descent from right end of heng down-left to (15, 30):
    bezier_stroke(d,
                  to_px(85, 80),
                  to_px(60, 55),
                  to_px(15, 30),
                  w_head=5, w_tail=3, n=40)
    # Small hook flick at end (up-right) — the 钩 of 横撇钩
    bezier_stroke(d,
                  to_px(15, 30),
                  to_px(20, 35),
                  to_px(28, 42),
                  w_head=3, w_tail=1, n=15)

    # Stroke 4: 弯钩 — curved descender from top-middle of 子 zone
    # down through the mid-line, ending with left-flick hook at bottom.
    # Continuous bezier from (55, 70) curving to (60, -30) to (30, -105),
    # then split into two beziers for the curve + hook.
    bezier_stroke(d,
                  to_px(55, 68),
                  to_px(65, 0),
                  to_px(35, -100),
                  w_head=6, w_tail=4, n=60)
    # Terminal hook — flick left from (35, -100) up-left to (-5, -95)
    bezier_stroke(d,
                  to_px(35, -100),
                  to_px(20, -100),
                  to_px(-8, -92),
                  w_head=5, w_tail=1, n=25)

    # Stroke 5: 横 — long crossing heng through descender midheight.
    line_stroke(d,
                to_px(-15, -15),
                to_px(105, -15),
                w_head=5, w_tail=5, n=40)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_仔.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
