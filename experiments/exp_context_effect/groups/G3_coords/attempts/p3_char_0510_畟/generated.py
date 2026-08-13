# BANK_DEVIATION
# skipped: bi_field_over_ji.py
# reason: 畟 is 田-over-夊 (splayed 撇+横撇+捺 with a small top-pie), not 田-over-丌; the bottom needs a splayed 捺-arm, not two straight legs
# fresh_component: sui_bottom_for_ji — 夊-style bottom (小撇 + 横撇 + long 捺)
#
# p3_char_0510_畟 — jì. Top-bottom stack: 田 (rice-field, 5 strokes) over 夊-like base.
# Bottom (from GT): a short 撇 upper-left, a 横 that turns down as 折/短撇, a long splayed 捺 crossing right-down.

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_畟.png")


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

    # ---- 田 (upper): box with cross ----
    x_left  = 90
    x_right = 210
    y_top   = 35
    y_bot   = 145
    x_mid   = (x_left + x_right) // 2
    y_mid   = (y_top + y_bot) // 2

    w  = 7   # box edge width
    wm = 6   # inner cross width

    # left 竖
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # top + right (横折)
    d.line([(x_left - 3, y_top), (x_right + 3, y_top)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # middle 竖
    d.line([(x_mid, y_top + 3), (x_mid, y_bot - 2)], fill=(0, 0, 0), width=wm)
    # middle 横
    d.line([(x_left + 3, y_mid), (x_right - 3, y_mid)], fill=(0, 0, 0), width=wm)
    # bottom 横 (closes)
    d.line([(x_left - 3, y_bot), (x_right + 3, y_bot)], fill=(0, 0, 0), width=w)

    # ---- 夊 bottom (enlarged; long 捺 dominates) ----
    # Small 撇 upper-left of bottom zone (short diagonal)
    _curve(d, (105, 158), (92, 178), (78, 200), 6)

    # 横撇 / 折 — heng then curls down-left (upper portion of bottom)
    d.line([(115, 175), (215, 175)], fill=(0, 0, 0), width=7)
    # 撇 turn: from right end of heng, curls down-left across
    _curve(d, (215, 175), (190, 220), (130, 265), 7)

    # long splayed 捺 — from around upper-mid crossing point, extends to far lower-right
    _curve(d, (140, 200), (200, 245), (285, 285), 9)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
