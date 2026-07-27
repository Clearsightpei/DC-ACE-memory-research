# p3_char_0098_以 — G3 attempt.
# 以 has 4 strokes viewed as two halves separated by a small gap:
#   Left half: 竖提 (vertical curving into an up-right hook) + 短点
#   Right half: 撇 (long down-left sweep) + 点 (heavy tail dot)
# GT shows thin, MMH-style lines — keep widths modest (~4-6 px).

import os
import sys
from PIL import Image, ImageDraw

CANVAS = 300
CX = CY = CANVAS // 2


def to_px(x, y, ox=0.0, oy=0.0):
    return (CX + ox + x, CY - (oy + y))


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

    # ---- LEFT HALF ----
    # Stroke 1: 竖提 — vertical starting high, curving to hook up-right.
    # Head near (-75, +55), body drops to (-70, -55), curves out to (-40, -35).
    # Split into two beziers: main shu + hook (ti).
    p0 = to_px(-70, 55)
    p1 = to_px(-78, -10)   # bow slightly left as it descends
    p2 = to_px(-70, -55)
    bezier_stroke(d, p0, p1, p2, w_head=6, w_tail=5, n=40)
    # ti hook: from bottom of shu, sweep up-right thinning.
    h0 = to_px(-70, -55)
    h1 = to_px(-55, -50)
    h2 = to_px(-30, -30)
    bezier_stroke(d, h0, h1, h2, w_head=5, w_tail=2, n=30)

    # Stroke 2: 短点 (small dot to the right of the shu, upper area)
    d0 = to_px(-30, 40)
    d1 = to_px(-20, 32)
    d2 = to_px(-8, 20)
    bezier_stroke(d, d0, d1, d2, w_head=3, w_tail=8, n=25)

    # ---- RIGHT HALF ----
    # Stroke 3: 撇 — long sweeping curve from upper area down-left.
    # Head near (+40, +70) sweeps to tail near (-5, -75).
    pp0 = to_px(45, 70)
    pp1 = to_px(15, 0)     # bow left through center-lower
    pp2 = to_px(-5, -75)
    bezier_stroke(d, pp0, pp1, pp2, w_head=6, w_tail=2, n=50)

    # Stroke 4: 点 — heavy tail dot on the right, going down-right from meet
    # point roughly at (+20, +10) down to (+70, -70).
    n0 = to_px(20, 15)
    n1 = to_px(45, -25)
    n2 = to_px(75, -70)
    bezier_stroke(d, n0, n1, n2, w_head=3, w_tail=8, n=40)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_以.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()
