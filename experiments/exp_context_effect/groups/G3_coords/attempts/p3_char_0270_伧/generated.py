# p3_char_0270_伧 — G3 attempt (revision 2).
# 伧 = 亻 (left, 2 strokes) + 仓 (right, 4 strokes: 撇+捺 roof, then 横折,
#      then 巴-like pocket with hook).
# Revision notes: v1 had roof too tall/pointy and pocket too detached/boxy.
# Flattening roof, tightening the whole 仓 block, and using a single
# 横折钩 curve for the pocket instead of separate pieces.

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
    # 撇 — long sweep down-left
    bezier_stroke(d,
                  to_px(-60, 100),
                  to_px(-82, 15),
                  to_px(-108, -100),
                  w_head=6, w_tail=2, n=55)
    # 竖 — vertical, head touching pie mid-shaft
    line_stroke(d,
                to_px(-63, 35),
                to_px(-63, -115),
                w_head=6, w_tail=5, n=40)

    # ---------- 仓 (right side) ----------
    # 人 roof (flatter, wider): apex around (30, 100)
    APX = (30, 100)
    # 撇 of roof — from apex sweeping down-left
    bezier_stroke(d,
                  to_px(*APX),
                  to_px(-5, 55),
                  to_px(-35, 15),
                  w_head=5, w_tail=2, n=45)
    # 捺 of roof — from apex sweeping down-right with tail
    bezier_stroke(d,
                  to_px(*APX),
                  to_px(60, 55),
                  to_px(100, 10),
                  w_head=4, w_tail=8, n=45)

    # 横折 — small horizontal segment turning down (middle stroke of 仓)
    # Sits just under the roof, on the left-inside of the pocket.
    # Horizontal
    line_stroke(d,
                to_px(-15, 20),
                to_px(35, 20),
                w_head=4, w_tail=4, n=25)
    # Turn/short drop
    line_stroke(d,
                to_px(35, 20),
                to_px(35, -5),
                w_head=4, w_tail=4, n=15)

    # 巴-pocket: 横折钩 as one composite stroke -----------
    # Top horizontal of pocket
    line_stroke(d,
                to_px(-15, -10),
                to_px(75, -10),
                w_head=5, w_tail=5, n=30)
    # Right side descending
    line_stroke(d,
                to_px(75, -10),
                to_px(72, -95),
                w_head=5, w_tail=5, n=30)
    # Bottom + hook curling up-left
    bezier_stroke(d,
                  to_px(72, -95),
                  to_px(30, -110),
                  to_px(-18, -100),
                  w_head=5, w_tail=4, n=35)
    # small hook flick up-left at the pocket's bottom-left
    bezier_stroke(d,
                  to_px(-18, -100),
                  to_px(-15, -85),
                  to_px(-5, -70),
                  w_head=4, w_tail=1, n=20)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_伧.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
