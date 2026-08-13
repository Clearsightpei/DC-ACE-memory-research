# p3_char_0346_佞 (nìng) — G3 attempt.
# 佞 = 亻 (left, 2 strokes: pie + shu) + 仁 sub-composition on the right:
#     top: 二 (two 横), bottom: 女 (3 strokes: 撇点 + 撇 + 长横).
# Total 7 strokes. GT shows thin, MMH-style lines (~4-5 px).
# Layout:
#   亻 occupies left ~1/3 (x ~ -110 .. -60)
#   Right side (x ~ -40 .. +110):
#     二 top rows at y~+95 and y~+55
#     女 lower half:  长横 spans across around y~-20; 撇点 and 撇 above/below

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

    W = 4  # base stroke width per P12

    # ---------- 亻 (left radical) ----------
    # Stroke 1: 撇 pie — head near upper-mid-left, sweeps down-left
    bezier_stroke(d,
                  to_px(-75, 105),
                  to_px(-92, 25),
                  to_px(-112, -70),
                  w_head=6, w_tail=2, n=55)
    # Stroke 2: 竖 shu — vertical touching pie mid-shaft; ends around y=-95
    line_stroke(d,
                to_px(-78, 35),
                to_px(-78, -100),
                w_head=W + 1, w_tail=W + 1, n=40)

    # ---------- 二 (top right, above 女) ----------
    # Stroke 3: upper 横 (shorter)
    line_stroke(d,
                to_px(0, 115),
                to_px(75, 115),
                w_head=W, w_tail=W, n=30)
    # Stroke 4: lower 横 (a bit longer, slightly right-tilted)
    line_stroke(d,
                to_px(-15, 75),
                to_px(100, 75),
                w_head=W, w_tail=W, n=30)

    # ---------- 女 (bottom right) ----------
    # Stroke 5: 撇点 (starts as a pie from upper-right sweeping down-left,
    # then flicks down-right at the bottom). Two-segment: pie + na-flick.
    # Pie portion
    bezier_stroke(d,
                  to_px(55, 45),
                  to_px(20, -25),
                  to_px(-18, -80),
                  w_head=5, w_tail=3, n=40)
    # 点 flick (short down-right stroke joining the pie tail)
    bezier_stroke(d,
                  to_px(-18, -80),
                  to_px(-5, -95),
                  to_px(15, -110),
                  w_head=3, w_tail=6, n=25)

    # Stroke 6: 撇 — long pie crossing through the first one, going down-left.
    bezier_stroke(d,
                  to_px(95, 25),
                  to_px(50, -45),
                  to_px(10, -115),
                  w_head=5, w_tail=2, n=50)

    # Stroke 7: 长横 — long horizontal across the middle of 女, crossing both pies.
    line_stroke(d,
                to_px(-25, 0),
                to_px(110, 0),
                w_head=W, w_tail=W, n=40)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佞.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
