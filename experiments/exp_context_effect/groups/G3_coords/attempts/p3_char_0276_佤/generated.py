# p3_char_0276_佤 — G3 attempt.
# 佤 = 亻 (left, 2 strokes) + 瓦 (right, 4 strokes: heng, shu_ti, heng_zhe_wan_gou / xie_gou, dian).
# 6 strokes total. GT shows thin cursive-ish MMH strokes.
# 亻 sits on the left third; 瓦 sits on the right two-thirds.

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
    # Stroke 1: 撇 pie
    bezier_stroke(d,
                  to_px(-70, 100),
                  to_px(-90, 15),
                  to_px(-110, -85),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 shu
    line_stroke(d,
                to_px(-72, 35),
                to_px(-72, -110),
                w_head=6, w_tail=5, n=40)

    # ---------- 瓦 (right) ----------
    # Stroke 1: 横 top horizontal spanning most of right zone (slight up-slant)
    line_stroke(d,
                to_px(-25, 85),
                to_px(95, 92),
                w_head=5, w_tail=5, n=40)

    # Stroke 2: 竖提 short vertical descending then flick right (leftmost of 瓦)
    #   vertical segment
    line_stroke(d,
                to_px(-15, 85),
                to_px(-25, -30),
                w_head=6, w_tail=5, n=30)
    #   ti flick out to lower-right
    bezier_stroke(d,
                  to_px(-25, -30),
                  to_px(-5, -35),
                  to_px(20, -40),
                  w_head=5, w_tail=2, n=25)

    # Stroke 3: 横折斜钩 (the main enveloping curve — open bottom-left, hook bottom-right)
    #   top short heng near mid-height right side
    line_stroke(d,
                to_px(20, 40),
                to_px(80, 45),
                w_head=5, w_tail=5, n=30)
    #   descending sweeping curve down to lower-right ending with hook
    bezier_stroke(d,
                  to_px(80, 45),
                  to_px(105, -50),
                  to_px(95, -115),
                  w_head=5, w_tail=6, n=45)
    #   bottom sweep left along baseline (斜钩 tail curving left)
    bezier_stroke(d,
                  to_px(95, -115),
                  to_px(40, -118),
                  to_px(-10, -95),
                  w_head=6, w_tail=3, n=35)

    # Stroke 4: 点 dian in upper-right pocket, just above/right of stroke-3 heng
    bezier_stroke(d,
                  to_px(70, 75),
                  to_px(78, 68),
                  to_px(88, 58),
                  w_head=3, w_tail=7, n=20)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佤.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
