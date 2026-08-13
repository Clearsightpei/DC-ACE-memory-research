# BANK_DEVIATION
# skipped: xin.py, bi_field_over_ji.py
# reason: 思 = 田-top over 心-bottom stack; xin.py centers 心 at canvas center (won't slot into bottom half without heavy transform); bi_field_over_ji.py bakes a 丌 base underneath 田 (wrong bottom half). Inline both fresh at the vertical positions the GT demands.
# fresh_component: tian_top_for_si + xin_bottom_for_si — 田 compressed to upper ~y=45..140 and 心 laid across y=180..270

# 思 (sī, "think") — 9 strokes = 田 (5) + 心 (4)
# GT reading: 田 sits upper (y ~ 40..145, x ~ 100..215),
# 心 sits lower and slightly wider (y ~ 175..275, x ~ 55..255).

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_思.png")


def _curve(d, p0, p1, p2, w0, w1, steps=40):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = (x, y)
        if prev is not None:
            w = w0 * (1 - u) + w1 * u
            wi = max(1, int(round(w)))
            d.line([prev, pt], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            d.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))
        prev = pt


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---------------- 田 (upper) ----------------
    x_left  = 100
    x_right = 210
    y_top   = 45
    y_bot   = 145
    x_mid   = (x_left + x_right) // 2
    y_mid   = (y_top + y_bot) // 2

    w  = 7   # outer box edge
    wm = 6   # inner cross

    # 1) left 竖
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # 2) 横折 (top + right)
    d.line([(x_left - 2, y_top), (x_right + 2, y_top)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # 3) middle 竖
    d.line([(x_mid, y_top + 3), (x_mid, y_bot - 2)], fill=(0, 0, 0), width=wm)
    # 4) middle 横
    d.line([(x_left + 3, y_mid), (x_right - 3, y_mid)], fill=(0, 0, 0), width=wm)
    # 5) bottom 横 (closes box)
    d.line([(x_left - 2, y_bot), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w)

    # ---------------- 心 (lower) ----------------
    # Bowl: 卧钩 — sweeps from upper-left down-right, curls up at right.
    # Anchor pts (pixel coords).
    bowl_start = (85, 195)
    bowl_ctrl  = (150, 285)
    bowl_end   = (240, 235)
    _curve(d, bowl_start, bowl_ctrl, bowl_end, 5, 9)
    # Hook curl at the right end of bowl (short up-tick)
    d.line([(240, 235), (232, 220)], fill=(0, 0, 0), width=7)

    # 6) left 点 (mirrored, tapered)
    _curve(d, (70, 220), (63, 205), (55, 180), 8, 2)
    # 7) middle 点 (small, near center-inside of bowl, tapered head → tail down-right)
    _curve(d, (140, 205), (148, 215), (158, 228), 3, 7)
    # 8) right 点 (outside upper-right, tapered)
    _curve(d, (215, 175), (230, 190), (255, 210), 3, 8)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
