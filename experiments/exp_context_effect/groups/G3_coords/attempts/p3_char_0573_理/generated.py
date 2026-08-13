# BANK_DEVIATION
# skipped: quan_tian_for_LR_left.py (compressed 田 for LR-left slot)
# reason: In 理, the 田 sits in the TOP-RIGHT (as part of 里), not the
#   left slot; also its middle 竖 continues down through 土, so 田 is
#   not a standalone envelope here.
# fresh_component: li_field_over_tu (田 stacked over 土 with a shared
#   continuous middle 竖 — canonical 里 recipe for L-R right slot)
#
# skipped: (no wang_pang bank entry exists) — inlining 王 radical fresh
# fresh_component: wang_pang_for_LR_left (三横一竖, bottom heng becomes
#   a slight 提 tilt; canonical 王字旁 for L-R left slot)
#
# 理 = 王 (left radical, 王字旁) + 里 (right, 田 over 土 sharing 竖)
# 11 strokes total: 4 (王) + 5 (田) + 2 (土 extras: middle heng + bottom heng)
# = 11 strokes; last stroke of 王 is a slight 提 rather than a pure heng.

import os
from PIL import Image, ImageDraw


def _line(D, p0, p1, w):
    D.line([p0, p1], fill=(0, 0, 0), width=w)
    r = w / 2.0
    for (x, y) in (p0, p1):
        D.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def draw_wang_pang_for_LR_left(D, x_l=30, x_r=115, y_top=55, y_bot=255, w=4):
    """王字旁 (王 as left radical) — 4 strokes, bottom heng slightly tilted up as 提."""
    x_mid = (x_l + x_r) // 2  # vertical shu x
    y_h1 = y_top + 5                       # top heng
    y_h2 = y_top + int(0.48 * (y_bot - y_top))  # middle heng near true middle
    # S1: top heng
    _line(D, (x_l, y_h1), (x_r, y_h1), w)
    # S2: middle heng (slightly shorter)
    _line(D, (x_l + 6, y_h2), (x_r - 4, y_h2), w)
    # S3: vertical shu — extends to meet the 提 (avoids visual gap)
    _line(D, (x_mid, y_h1), (x_mid, y_bot - 4), w)
    # S4: bottom stroke as 提 (upward tick) — starts left-low, ends right-high;
    # anchored so it passes through the shu's endpoint region.
    _line(D, (x_l - 4, y_bot + 8), (x_r + 6, y_bot - 20), w)


def draw_li_field_over_tu(D, x_l=155, x_r=270, y_top=50, y_bot=275, w=4, wm=3):
    """里 (li) — 田 (top) over 土 (bottom), sharing the middle 竖.
    7 strokes: 3 (top 田 frame) + middle shu + middle heng of 田 +
    middle heng of 土 + bottom long heng.
    """
    x_mid = (x_l + x_r) // 2
    y_field_bot = y_top + int(0.42 * (y_bot - y_top))  # 田's bottom edge
    y_field_mid = (y_top + y_field_bot) // 2

    # ---------- 田 (top) ----------
    # S1: left 竖 of 田
    _line(D, (x_l, y_top), (x_l, y_field_bot), w)
    # S2: 横折 (top heng + right 竖)
    _line(D, (x_l - 2, y_top), (x_r + 2, y_top), w)
    _line(D, (x_r, y_top), (x_r, y_field_bot), w)
    # S3: bottom heng of 田
    _line(D, (x_l - 2, y_field_bot), (x_r + 2, y_field_bot), w)
    # S4: middle 竖 — continues DOWN through the 土 to the bottom heng
    _line(D, (x_mid, y_top + 3), (x_mid, y_bot - 5), w)
    # S5: middle heng inside 田
    _line(D, (x_l + 3, y_field_mid), (x_r - 3, y_field_mid), wm)

    # ---------- 土 (bottom) ----------
    y_tu_mid = y_field_bot + int(0.55 * (y_bot - y_field_bot))
    # S6: middle heng of 土 (shorter)
    _line(D, (x_l + 12, y_tu_mid), (x_r - 12, y_tu_mid), w)
    # S7: bottom long heng (widest — spans slightly outside frame)
    _line(D, (x_l - 8, y_bot), (x_r + 10, y_bot), w)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)

    # Left: 王 radical
    draw_wang_pang_for_LR_left(D)

    # Right: 里
    draw_li_field_over_tu(D)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_理.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
