# p3_char_0364_畀 — 畀 (bì), 8 strokes.
# Structure: 田 (rice-field, 5 strokes: left竖 + 横折 + 中竖 + 中横 + 下横)
# stacked over 丌-style base (3 strokes: long 横 crossbar + left 撇 leg + right 竖 leg).
# BANK_DEVIATION
# skipped: jia_first.py (甲) — similar box+middle-heng+long-vertical pattern
# reason: 畀's bottom is 丌 (crossbar + two splayed legs), not a single central 竖
# fresh_component: bi_field_over_ji — 田-box stacked over splayed-leg 丌
#
# Inline PIL: cleaner than composing bank primitives for the 田+丌 stack.

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_畀.png")


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- 田 (upper): box with cross ----
    x_left  = 80
    x_right = 220
    y_top   = 40
    y_bot   = 170
    x_mid   = (x_left + x_right) // 2
    y_mid   = (y_top + y_bot) // 2

    w  = 8   # box edge width
    wm = 7   # inner cross width

    # Stroke 1: left 竖
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top + right)
    d.line([(x_left - 3, y_top), (x_right + 3, y_top)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle 竖 (inside)
    d.line([(x_mid, y_top + 4), (x_mid, y_bot - 2)], fill=(0, 0, 0), width=wm)
    # Stroke 4: middle 横 (inside)
    d.line([(x_left + 3, y_mid), (x_right - 3, y_mid)], fill=(0, 0, 0), width=wm)
    # Stroke 5: bottom 横 (closes box)
    d.line([(x_left - 3, y_bot), (x_right + 3, y_bot)], fill=(0, 0, 0), width=w)

    # ---- 丌 (lower): long crossbar + two splayed legs ----
    y_cross    = 210
    x_cross_l  = 35
    x_cross_r  = 265

    w_cross = 9
    w_leg   = 9

    # Stroke 6: long 横 crossbar (wider than 田 above)
    d.line([(x_cross_l, y_cross), (x_cross_r, y_cross)], fill=(0, 0, 0), width=w_cross)

    # Stroke 7: left 撇 leg — from near left-inner of crossbar, splays down-left
    # Curved slightly: use short-line approximation via 3-point bezier.
    def _curve(p0, p1, p2, width, steps=32):
        pts = []
        for i in range(steps + 1):
            u = i / steps
            x = (1 - u) * (1 - u) * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
            y = (1 - u) * (1 - u) * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
            pts.append((x, y))
        d.line(pts, fill=(0, 0, 0), width=width)

    _curve((95, 215), (75, 255), (45, 290), w_leg)

    # Stroke 8: right 竖 leg — near right of crossbar, straight down (slight outward lean)
    d.line([(205, 215), (215, 290)], fill=(0, 0, 0), width=w_leg)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
