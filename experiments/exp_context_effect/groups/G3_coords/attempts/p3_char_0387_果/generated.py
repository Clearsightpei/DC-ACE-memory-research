# BANK_DEVIATION
# skipped: mu.py (draw_mu — 木 crossing at fixed offset)
# reason: in 果, the middle 竖 of 田 continues straight down as the shu of 木 (one unified vertical),
#         and pie/na cross at the 木-heng level well below 田 — cannot reuse mu.py without rewriting.
# fresh_component: guo_mu_under_tian (inline 木 sharing its vertical with 田's middle-竖)

# p3_char_0387_果 (guǒ), 8 strokes.
# Structure: 田 upper + 木 lower with SHARED central vertical.
# Strokes: 1 左竖 | 2 横折 (top+right) | 3 中竖 (continues DOWN through 木 as 木-shu) |
#          4 中横 (inside 田) | 5 下横 (closes 田, also acts as 木-crossbar-ish? see note) |
#          then 木 crossbar heng | 木 pie | 木 na.
# Simplification: draw 田 as bi_field_over_ji does (5-stroke box), then extend a long central shu
# from y_top of 田 down to y_bot of 木, and add wide 木 heng + pie + na crossing at the 木-heng.

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_果.png")


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- 田 (upper box) ----
    x_left  = 90
    x_right = 210
    y_top   = 45
    y_bot   = 150
    x_mid   = (x_left + x_right) // 2
    y_mid   = (y_top + y_bot) // 2

    w  = 7   # box edge width
    wm = 6   # inner cross width

    # Stroke 1: left 竖
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top + right)
    d.line([(x_left - 3, y_top), (x_right + 3, y_top)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle 竖 — EXTENDS from top of 田 all the way DOWN to bottom of canvas (shared 木-shu)
    y_bottom_shu = 275
    d.line([(x_mid, y_top + 2), (x_mid, y_bottom_shu)], fill=(0, 0, 0), width=wm + 1)
    # Stroke 4: middle 横 (inside 田)
    d.line([(x_left + 3, y_mid), (x_right - 3, y_mid)], fill=(0, 0, 0), width=wm)
    # Stroke 5: bottom 横 (closes 田)
    d.line([(x_left - 3, y_bot), (x_right + 3, y_bot)], fill=(0, 0, 0), width=w)

    # ---- 木 (lower, sharing the central 竖) ----
    # 木 heng: wide crossbar just below 田
    y_heng = 190
    x_heng_l = 40
    x_heng_r = 260
    d.line([(x_heng_l, y_heng), (x_heng_r, y_heng)], fill=(0, 0, 0), width=8)

    # 木 pie: from just left of center on the heng, splaying down-left with curve
    def _curve(p0, p1, p2, width, steps=40):
        pts = []
        for i in range(steps + 1):
            u = i / steps
            x = (1 - u) * (1 - u) * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
            y = (1 - u) * (1 - u) * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
            pts.append((x, y))
        d.line(pts, fill=(0, 0, 0), width=width)

    # pie
    _curve((x_mid - 8, y_heng - 2), (x_mid - 55, y_heng + 40), (30, 285), width=7)
    # na
    _curve((x_mid + 8, y_heng - 2), (x_mid + 55, y_heng + 40), (275, 285), width=7)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
