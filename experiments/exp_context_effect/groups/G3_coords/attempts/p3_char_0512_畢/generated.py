# BANK_DEVIATION
# skipped: bi_field_over_ji.py (畀), shen_extend.py (申)
# reason: 畢 is 田-top + compound-lower (two short shu + long heng + central shu-extending + bottom heng), taller than 畀/申
# fresh_component: bi_field — 田 on top compressed to upper-third, plus manual lower compound
#
# 畢 (bì) — 11 strokes:
#   Upper (田-box): 1.left竖, 2.横折, 3.内竖, 4.内横, 5.下横
#   Lower compound: 6-7. two short 竖 hanging below 田, 8. long 横 (mid),
#     9. central 竖 (extending down to bottom), 10. bottom 横

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_畢.png")


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- 田 (upper): compressed into upper third ----
    x_left  = 95
    x_right = 205
    y_top   = 35
    y_bot   = 130
    x_mid   = (x_left + x_right) // 2
    y_mid   = (y_top + y_bot) // 2

    w  = 7   # box edge width
    wm = 6   # inner cross width

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

    # ---- Two short 竖 hanging below 田 (like 卄 remnant) ----
    y_short_top = 130
    y_short_bot = 175
    x_sl = 120
    x_sr = 180
    w_short = 7
    d.line([(x_sl, y_short_top), (x_sl, y_short_bot)], fill=(0, 0, 0), width=w_short)
    d.line([(x_sr, y_short_top), (x_sr, y_short_bot)], fill=(0, 0, 0), width=w_short)

    # ---- Long 横 mid-crossbar ----
    y_cross_mid = 195
    x_cross_l   = 35
    x_cross_r   = 265
    w_cross     = 8
    d.line([(x_cross_l, y_cross_mid), (x_cross_r, y_cross_mid)],
           fill=(0, 0, 0), width=w_cross)

    # ---- Central 竖 extending down (through crossbar to bottom) ----
    x_center = 150
    y_shu_top = 155
    y_shu_bot = 285
    w_shu = 9
    d.line([(x_center, y_shu_top), (x_center, y_shu_bot)],
           fill=(0, 0, 0), width=w_shu)

    # ---- Bottom 横 ----
    y_bot_heng = 260
    x_bh_l = 60
    x_bh_r = 240
    w_bh   = 8
    d.line([(x_bh_l, y_bot_heng), (x_bh_r, y_bot_heng)],
           fill=(0, 0, 0), width=w_bh)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
