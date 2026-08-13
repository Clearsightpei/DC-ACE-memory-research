# p3_char_0506_畜 (xù) — 10 strokes.
# Structure: 亠 (dot + long heng) over 幺 (two 撇折 swirls + dot) over 田 (box + cross).
# Bank-reference: 畀's inline 田 (bi_field_over_ji.py) fits with slight compression;
# 幺 shape reuses the _bow_bezier idea from yao attempt (inlined here for clarity).
# BANK_DEVIATION
# skipped: xuan_char.py (亘 not 玄), tou_radical.py (bank 亠 is standalone-scaled)
# reason: 畜's 亠 must sit above a 幺, then a 田 — need bespoke vertical layout;
#         inline PIL cleaner than three separate bank calls with (ox, oy, scale).
# fresh_component: xu_char (亠 + inline 幺-swirl + compressed 田)

import os, math
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_畜.png")


def _bow_bezier(draw, p0, p2, bow_perp, w_head, w_tail, n=40):
    x0, y0 = p0
    x1, y1 = p2
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    cx = mx + perp_x * bow_perp
    cy = my + perp_y * bow_perp
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        w = max(1, int(round(w_head + (w_tail - w_head) * u)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def _tapered_line(draw, p0, p1, w_head, w_tail, n=16):
    x0, y0 = p0
    x1, y1 = p1
    prev = None
    for i in range(n + 1):
        u = i / n
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = max(1, int(round(w_head + (w_tail - w_head) * u)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w)
        prev = (x, y)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---------- 亠 (top) ----------
    # Stroke 1: 点 (dot) — small teardrop, upper-right of center
    _tapered_line(d, (150, 32), (162, 52), w_head=2, w_tail=7, n=14)

    # Stroke 2: 一 (long heng) — widest stroke of the whole char
    d.line([(40, 70), (260, 68)], fill=(0, 0, 0), width=6)

    # ---------- 幺 (middle swirl) ----------
    # Compressed rendering: two small 撇折 loops + a small dot.
    # Upper 撇折: pie down-left then a rightward curl
    _bow_bezier(d, (135, 82), (110, 108), bow_perp=-4, w_head=5, w_tail=3, n=32)
    _bow_bezier(d, (110, 108), (150, 118), bow_perp=-5, w_head=3, w_tail=3, n=28)

    # Lower 撇折 (slightly larger, sits just below the upper one)
    _bow_bezier(d, (150, 118), (118, 145), bow_perp=-5, w_head=5, w_tail=3, n=32)
    _bow_bezier(d, (118, 145), (162, 158), bow_perp=-6, w_head=3, w_tail=3, n=28)

    # Small 点 to the right of the lower loop
    _tapered_line(d, (170, 138), (185, 160), w_head=2, w_tail=6, n=14)

    # ---------- 田 (bottom) ----------
    x_left  = 78
    x_right = 222
    y_top   = 170
    y_bot   = 278
    x_mid   = (x_left + x_right) // 2
    y_mid   = (y_top + y_bot) // 2

    w = 7
    wm = 6

    # Stroke: left 竖
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke: 横折 (top heng + right shu)
    d.line([(x_left - 2, y_top), (x_right + 2, y_top)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Middle 竖 (inside)
    d.line([(x_mid, y_top + 3), (x_mid, y_bot - 2)], fill=(0, 0, 0), width=wm)
    # Middle 横 (inside)
    d.line([(x_left + 2, y_mid), (x_right - 2, y_mid)], fill=(0, 0, 0), width=wm)
    # Bottom 横 (closes box)
    d.line([(x_left - 2, y_bot), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
