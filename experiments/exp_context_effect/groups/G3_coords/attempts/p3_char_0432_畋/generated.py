# BANK_DEVIATION
# skipped: bi_field_over_ji.py (田 upper block is baked to canvas-wide box)
# reason: 畋 needs a compressed 田 on the LEFT (~40% width) beside a wide 攵 on the right; bank 田 spans x=80-220 (full-width) and can't shrink cleanly without breaking widths
# fresh_component: tian_compressed_for_LR + poc_knock_for_LR (攵)
#
# 畋 (tián) — 田 (field) + 攵 (knock/poc) L-R composition.
# 田: 5 strokes (left 竖, 横折, middle 竖, middle 横, bottom 横).
# 攵: 4 strokes (small 撇, 短横, big 撇 sweep, long 捺 sweep).

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_畋.png")


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

    # ---- 田 (left, compressed): box with cross ----
    x_left  = 30
    x_right = 135
    y_top   = 80
    y_bot   = 200
    x_mid   = (x_left + x_right) // 2
    y_mid   = (y_top + y_bot) // 2

    w  = 7
    wm = 6

    # Stroke 1: left 竖
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top + right)
    d.line([(x_left - 2, y_top), (x_right + 2, y_top)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle 竖 (inside)
    d.line([(x_mid, y_top + 3), (x_mid, y_bot - 2)], fill=(0, 0, 0), width=wm)
    # Stroke 4: middle 横 (inside)
    d.line([(x_left + 2, y_mid), (x_right - 2, y_mid)], fill=(0, 0, 0), width=wm)
    # Stroke 5: bottom 横 (closes box)
    d.line([(x_left - 2, y_bot), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w)

    # ---- 攵 (right): small 撇 + 短横 + big 撇 + long 捺 ----
    # Stroke 6: short 撇 (top, small diagonal from upper-right down to where 短横 begins)
    _curve(d, (210, 80), (195, 100), (178, 122), 6)

    # Stroke 7: 短横 (short horizontal, slight up-tilt)
    d.line([(172, 128), (255, 122)], fill=(0, 0, 0), width=7)

    # Stroke 8: big 撇 — starts near right end of 短横, sweeps down-left with curve
    _curve(d, (225, 130), (185, 195), (135, 270), 8)

    # Stroke 9: long 捺 — starts on the big-撇 shaft (crossing), sweeps down-right
    _curve(d, (195, 165), (240, 215), (290, 275), 9)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
