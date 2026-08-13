# BANK_DEVIATION
# skipped: quan_tian_for_LR_left.py (compressed 田 for LR-left slot)
# reason: 畧 is a TOP-BOTTOM stack (田 above 各), not LR — need a top-slot 田 instead of a left-slot compressed 田
# fresh_component: tian_top_for_stack — 田 sized for upper half of a top-bottom character
#
# 畧 (lüè) — 11 strokes. Top: 田 (5). Bottom: 各 = 夂 (3) + 口 (3).
# Fresh inline PIL render.
import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_畧.png")


def _curve(d, p0, p1, p2, width, steps=32):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) * (1 - u) * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) * (1 - u) * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    d.line(pts, fill=(0, 0, 0), width=width)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ==============================
    # 田 (top): rectangle with cross
    # ==============================
    x_left  = 90
    x_right = 210
    y_top   = 20
    y_bot   = 130
    x_mid   = (x_left + x_right) // 2
    y_mid   = (y_top + y_bot) // 2

    w  = 7
    wm = 6

    # left 竖
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # top 横 + right 竖 (横折)
    d.line([(x_left - 3, y_top), (x_right + 3, y_top)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # inner 竖
    d.line([(x_mid, y_top + 3), (x_mid, y_bot - 2)], fill=(0, 0, 0), width=wm)
    # inner 横
    d.line([(x_left + 3, y_mid), (x_right - 3, y_mid)], fill=(0, 0, 0), width=wm)
    # bottom 横 (close)
    d.line([(x_left - 3, y_bot), (x_right + 3, y_bot)], fill=(0, 0, 0), width=w)

    # ==============================
    # 夂 (middle): 撇 + 横撇 + 捺
    # ==============================
    # Stroke 1: short 撇 top-left → down-left
    _curve(d, (155, 140), (135, 165), (110, 195), 7)

    # Stroke 2: 横撇 (short horizontal turning into a pie)
    # horizontal segment then down-left
    d.line([(135, 155), (200, 155)], fill=(0, 0, 0), width=7)
    _curve(d, (200, 155), (180, 195), (135, 240), 7)

    # Stroke 3: long 捺 — start near where the pie of 横撇 crosses, sweep down-right
    _curve(d, (160, 190), (185, 225), (225, 250), 8)

    # ==============================
    # 口 (bottom): small rectangle centered
    # ==============================
    kx_l = 115
    kx_r = 195
    ky_t = 240
    ky_b = 285

    wk  = 6
    wkm = 5

    # left 竖
    d.line([(kx_l, ky_t), (kx_l, ky_b)], fill=(0, 0, 0), width=wk)
    # top 横 + right 竖 (横折)
    d.line([(kx_l - 2, ky_t), (kx_r + 2, ky_t)], fill=(0, 0, 0), width=wk)
    d.line([(kx_r, ky_t), (kx_r, ky_b)], fill=(0, 0, 0), width=wk)
    # bottom 横
    d.line([(kx_l - 2, ky_b), (kx_r + 2, ky_b)], fill=(0, 0, 0), width=wk)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
