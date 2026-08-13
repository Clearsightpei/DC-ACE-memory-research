# 每 (měi) — 7 strokes: 𠂉 top (撇 + short heng) + 母 bottom
# (竖折 + 横折钩 + 点 + 长横 + 点).
# No suitable bank primitive for 母 exists; inlined fresh with PIL.
# Math-convention coords (y grows UP), origin at canvas center (150,150).

import math
from PIL import Image, ImageDraw

CANVAS = 300


def to_px(x, y):
    return CANVAS / 2 + x, CANVAS / 2 - y


def line(t, p0, p1, w=6):
    x0, y0 = to_px(*p0)
    x1, y1 = to_px(*p1)
    t.line([(x0, y0), (x1, y1)], fill=(0, 0, 0), width=w)


def curve(t, p0, ctl, p1, w_head=6, w_tail=3, n=40):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * ctl[0] + u ** 2 * p1[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * ctl[1] + u ** 2 * p1[1]
        px, py = to_px(x, y)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def dian(t, x, y, dx=6, dy=-8, w=6):
    # small down-right stroke
    line(t, (x, y), (x + dx, y + dy), w=w)


def draw_mei(img):
    t = ImageDraw.Draw(img)

    # ---------- TOP 𠂉 (撇 sweeps down-left; short heng crosses its top) ----------
    # 撇: from upper-right, sweeps down and to the left of 母's left edge
    curve(t,
          p0=(0, 125), ctl=(-25, 90), p1=(-60, 45),
          w_head=6, w_tail=2)
    # short 横 (slightly tilted), crossing the 撇 near its top
    line(t, (-25, 108), (55, 100), w=6)

    # ---------- BOTTOM 母 (slightly narrower, leans right per GT) ----------
    # envelope: x in [-55, 60], top y ~ 45, bottom y ~ -95
    top_y = 45
    bot_y = -95
    xL = -55
    xR = 60

    # 1) 竖折 — left vertical + bottom horizontal (slight lean: bottom drifts right)
    line(t, (xL, top_y), (xL + 6, bot_y), w=6)
    line(t, (xL + 6, bot_y), (xR + 4, bot_y - 3), w=6)

    # 2) 横折钩 — top horizontal + right vertical + hook at bottom-left
    line(t, (xL + 2, top_y), (xR + 6, top_y - 4), w=6)
    line(t, (xR + 6, top_y - 4), (xR + 4, bot_y + 12), w=6)
    # hook: small stub to lower-left
    line(t, (xR + 4, bot_y + 12), (xR - 8, bot_y + 24), w=6)

    # 3) interior 点 (upper area, left-of-center)
    dian(t, -18, 8, dx=8, dy=-12, w=6)

    # 4) 长横 — long horizontal that extends past both envelope sides
    line(t, (-100, -30), (105, -35), w=6)

    # 5) interior 点 (lower-ish area, right-of-center)
    dian(t, 18, 8, dx=8, dy=-12, w=6)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw_mei(img)
    import os
    out = os.path.join(os.path.dirname(__file__), "01_每.png")
    img.save(out)
    print("wrote", out)
