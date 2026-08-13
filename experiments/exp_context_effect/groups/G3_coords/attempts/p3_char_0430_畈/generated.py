# BANK_DEVIATION
# skipped: you.py (又 radical, turtle-based bank primitive) and any tian_* bank
# reason: L-R char with 田 on left + 反 on right — bank you.py has baked (0,10)
#   offsets tuned for standalone/大-family compositions; the 反 here needs the
#   又 tucked inside the 厂 crook with a specific top-短横 + long-撇 envelope,
#   not the bank's isolated 横撇+捺 pair. Inline PIL matches the bi_field_over_ji
#   / bai_char_compressed_for_LR L-R inline recipe cleanly.
# fresh_component: fan_right_for_LR — 厂 (top短横 + long 撇) enveloping a small 又
#   (横撇 + 捺), sized for right slot in L-R composition with 田-left.
#
# p3_char_0430_畈 — 畈 (fàn), 9 strokes (田 5 + 反 4).
# Structure: L-R. 田 compressed on left; 反 (厂 + 又) on right.

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_畈.png")


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

    # ================ 田 (left, compressed) ================
    x_left  = 30
    x_right = 130
    y_top   = 100
    y_bot   = 220
    x_mid   = (x_left + x_right) // 2
    y_mid   = (y_top + y_bot) // 2

    w  = 7
    wm = 6

    # 1: left 竖
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # 2: 横折 (top + right)
    d.line([(x_left - 3, y_top), (x_right + 2, y_top)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # 3: middle 竖
    d.line([(x_mid, y_top + 3), (x_mid, y_bot - 2)], fill=(0, 0, 0), width=wm)
    # 4: middle 横
    d.line([(x_left + 3, y_mid), (x_right - 2, y_mid)], fill=(0, 0, 0), width=wm)
    # 5: bottom 横 (closes)
    d.line([(x_left - 3, y_bot), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w)

    # ================ 反 (right) ================
    # 厂 envelope: short top 横 (slight upward tilt) + long 撇 sweeping down-left.
    # 又 inside crook: 横撇 (short) + 捺 crossing through.

    # Stroke 6: short top 横 (slanting up to the right)
    d.line([(165, 88), (255, 74)], fill=(0, 0, 0), width=7)

    # Stroke 7: long 撇 — from top-right area of 厂 sweeping down to lower-left
    _curve(d, (240, 78), (200, 180), (145, 285), width=8)

    # Stroke 8: 又's 横撇 — short 横 then hooks into a pie down-left, as ONE stroke.
    # Small heng segment
    d.line([(195, 150), (255, 142)], fill=(0, 0, 0), width=7)
    # The pie portion coming off end of heng, curving down-left
    _curve(d, (253, 144), (225, 195), (185, 245), width=7)

    # Stroke 9: 捺 — starts near the top of the 又's crossing point, sweeps down-right
    _curve(d, (215, 165), (250, 220), (290, 280), width=8)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
