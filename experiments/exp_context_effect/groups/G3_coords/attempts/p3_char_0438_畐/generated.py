# p3_char_0438_畐 — 畐 (fú), 9 strokes.
# Structure (top-to-bottom vertical stack):
#   一 (short heng, top)     — 1 stroke
#   口 (small box, middle)   — 3 strokes
#   田 (box with cross, bot) — 5 strokes
#
# BANK_DEVIATION
# skipped: kou.py, bi_field_over_ji.py
# reason: 畐 is a 3-tier vertical stack (heng / kou / tian) needing tight
#         proportional coordination; composing three separate primitives
#         with different scales/origins is fiddlier than one clean inline
#         PIL render where all three tiers share coherent widths + spacing.
# fresh_component: fu_full_stack — heng+kou+tian vertical stack for 畐-family
#                  (potentially reusable for 富, 福, 幅 etc. that share the
#                   一/口/田 stack under other radicals)

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_畐.png")


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- 一 (top heng) ----
    # Short heng near top; slightly narrower than the 口 below.
    y_heng = 50
    x_heng_l = 95
    x_heng_r = 195
    w_heng = 8
    d.line([(x_heng_l, y_heng), (x_heng_r, y_heng)], fill=(0, 0, 0), width=w_heng)

    # ---- 口 (middle box) ----
    # Nearly as wide as 田 below; sits just under 一.
    kx_l = 85
    kx_r = 215
    ky_t = 70
    ky_b = 145
    w_k = 8

    # Left 竖
    d.line([(kx_l, ky_t), (kx_l, ky_b)], fill=(0, 0, 0), width=w_k)
    # Top + right (横折)
    d.line([(kx_l - 2, ky_t), (kx_r + 2, ky_t)], fill=(0, 0, 0), width=w_k)
    d.line([(kx_r, ky_t), (kx_r, ky_b)], fill=(0, 0, 0), width=w_k)
    # Bottom 横
    d.line([(kx_l - 2, ky_b), (kx_r + 2, ky_b)], fill=(0, 0, 0), width=w_k)

    # ---- 田 (bottom box with cross) ----
    tx_l = 75
    tx_r = 225
    ty_t = 155
    ty_b = 270
    tx_m = (tx_l + tx_r) // 2
    ty_m = (ty_t + ty_b) // 2

    w_t = 9   # outer box width
    w_tm = 7  # inner cross width

    # Left 竖
    d.line([(tx_l, ty_t), (tx_l, ty_b)], fill=(0, 0, 0), width=w_t)
    # Top + right (横折)
    d.line([(tx_l - 3, ty_t), (tx_r + 3, ty_t)], fill=(0, 0, 0), width=w_t)
    d.line([(tx_r, ty_t), (tx_r, ty_b)], fill=(0, 0, 0), width=w_t)
    # Middle 竖
    d.line([(tx_m, ty_t + 4), (tx_m, ty_b - 2)], fill=(0, 0, 0), width=w_tm)
    # Middle 横
    d.line([(tx_l + 3, ty_m), (tx_r - 3, ty_m)], fill=(0, 0, 0), width=w_tm)
    # Bottom 横
    d.line([(tx_l - 3, ty_b), (tx_r + 3, ty_b)], fill=(0, 0, 0), width=w_t)

    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
