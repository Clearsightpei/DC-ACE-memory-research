# BANK_DEVIATION
# skipped: bi_field_over_ji.py (畀)
# reason: 畀 stacks 田 over splayed 丌 legs; 畏 stacks 田 over a
#   horizontal + 撇/竖/捺 (衣-bottom-like) foot with different topology.
# fresh_component: wei_bottom_yi_like — heng crossbar + short mid + long
#   pie down-left + long na down-right, tucked under a compressed 田.
#
# p3_char_0436_畏 — 9 strokes: 田 (5) + heng + short vertical/pie + long
# 撇 + long 捺.

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_畏.png")


def _curve(d, p0, p1, p2, width, steps=40):
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

    # ---- 田 (upper): compressed to leave bottom for foot ----
    x_left  = 90
    x_right = 210
    y_top   = 35
    y_bot   = 160
    x_mid   = (x_left + x_right) // 2
    y_mid   = (y_top + y_bot) // 2

    w  = 7   # box edge width
    wm = 6   # inner cross width

    # Stroke 1: left 竖
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top + right)
    d.line([(x_left - 3, y_top), (x_right + 3, y_top)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle 竖 (inside)
    d.line([(x_mid, y_top + 3), (x_mid, y_bot - 2)], fill=(0, 0, 0), width=wm)
    # Stroke 4: middle 横 (inside)
    d.line([(x_left + 3, y_mid), (x_right - 3, y_mid)], fill=(0, 0, 0), width=wm)
    # Stroke 5: bottom 横 (closes box)
    d.line([(x_left - 3, y_bot), (x_right + 3, y_bot)], fill=(0, 0, 0), width=w)

    # ---- 衣-like foot ----
    # Stroke 6: 横 crossbar — spans wider than 田, tilts slightly up-right
    d.line([(50, 188), (250, 180)], fill=(0, 0, 0), width=8)

    # Stroke 7: small central down-tick (short 竖 dropping from crossbar)
    d.line([(148, 190), (152, 210)], fill=(0, 0, 0), width=7)

    # Stroke 8: long 撇 — swept down-left, sweeping wide
    _curve(d, (140, 195), (95, 240), (40, 290), width=9)

    # Stroke 9: long 捺 — sweeping down-right with slight taper swell
    na_pts = [(155, 195), (185, 225), (220, 255), (255, 285), (275, 295)]
    widths = [6, 8, 10, 10, 7]
    for i in range(len(na_pts) - 1):
        d.line([na_pts[i], na_pts[i + 1]], fill=(0, 0, 0), width=widths[i])

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
