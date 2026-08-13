# BANK_DEVIATION
# skipped: zou_zhi.py (辶 radical bank) and hua_speak.py (舌 pointer only — its
#   drawing code lives in attempts/p3_char_0389_话/generated.py).
# reason: 适 = 辶 envelope + 舌 in upper-right slot. The frozen zou_zhi.py has
#   (ox, oy, scale) but the envelope needs to be tuned to fit 舌 in the
#   upper-right; easier to inline the 辶 envelope from guo_char.py's proven
#   recipe (same envelope structure worked for 过/边). Similarly the 舌
#   recipe from 话 needs re-slotting into the 辶 envelope's right chamber,
#   so inline both consistently in thin MMH style (W=4-5).
# fresh_component: shi_go_char_inline (辶 envelope + 舌 in right-upper slot)

import os
from PIL import Image, ImageDraw

CANVAS = 300
W = 4
BLACK = (0, 0, 0)


def _tapered_line(D, p0, p1, w0, w1, steps=28):
    x0, y0 = p0
    x1, y1 = p1
    prev = None
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            D.line([prev, (x, y)], fill=BLACK, width=w)
            r = w / 2.0
            D.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)
        prev = (x, y)


def _tapered_bezier(D, p0, p1, p2, w0, w1, steps=48, belly=None, w_belly=None):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        if belly is not None and w_belly is not None:
            if u <= belly:
                w = w0 + (w_belly - w0) * (u / belly)
            else:
                w = w_belly + (w1 - w_belly) * ((u - belly) / (1 - belly))
        else:
            w = w0 + (w1 - w0) * u
        w = max(1, int(round(w)))
        if prev is not None:
            D.line([prev, (bx, by)], fill=BLACK, width=w)
            r = w / 2.0
            D.ellipse([bx - r, by - r, bx + r, by + r], fill=BLACK)
        prev = (bx, by)


def stroke(D, p0, p1, w=W):
    D.line([p0, p1], fill=BLACK, width=w)
    r = w / 2
    for (x, y) in (p0, p1):
        D.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def polyline(D, pts, w=W):
    for i in range(len(pts) - 1):
        stroke(D, pts[i], pts[i + 1], w=w)


def draw_shi(D):
    # ---------- 舌 (right-upper component, above the 平捺) ----------
    # 撇 — short flick at top-right, upper-right to lower-left
    _tapered_line(D, (215, 55), (170, 105), W + 2, W, steps=18)

    # 一 (long heng) — wide horizontal across the top of 舌
    _tapered_line(D, (120, 125), (280, 122), W, W + 1, steps=30)

    # 丨 (shu) — vertical from just above heng down to top of 口
    _tapered_line(D, (198, 95), (198, 175), W, W, steps=20)

    # 口 — mouth box, sits under the shu, wider than tall
    # left 竖
    _tapered_line(D, (155, 175), (155, 235), W, W, steps=18)
    # 横折 top + right vertical (single polyline)
    polyline(D, [(155, 175), (255, 175), (255, 235)], w=W)
    # bottom 横
    _tapered_line(D, (155, 233), (257, 233), W, W, steps=18)

    # ---------- 辶 envelope (left + bottom) ----------
    # Stroke 1: 点 (small dot at top-left of envelope)
    _tapered_bezier(D, (70, 75), (79, 88), (88, 102),
                    w0=2, w1=W + 2, steps=18)

    # Stroke 2: 横折折撇 — small zigzag beneath the dot, on the left
    A = (45, 140)
    B = (95, 135)
    C = (55, 180)
    D_pt = (90, 215)
    _tapered_line(D, A, B, W, W + 1, steps=18)
    _tapered_bezier(D,
                    B,
                    (B[0] + 4, (B[1] + C[1]) / 2 + 2),
                    C,
                    W + 1, W + 1, steps=26)
    _tapered_bezier(D,
                    C,
                    ((C[0] + D_pt[0]) / 2 - 4, (C[1] + D_pt[1]) / 2 - 3),
                    D_pt,
                    W + 1, 2, steps=26)

    # Stroke 3: 平捺 — long flat sweep across the bottom, dips then rises
    _tapered_bezier(D, (35, 245), (160, 278), (290, 240),
                    w0=3, w1=2, steps=80,
                    belly=0.6, w_belly=10)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_shi(D)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_适.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
