# BANK_DEVIATION
# skipped: jia_first.py (would be a reasonable 日-box source for the 龺 middle)
# reason: 乾's left 龺 stacks 十 + 日 + 一 with a shared central 竖 that
#   pierces all three; jia_first is a monolithic single-竖-through-box
#   that doesn't compose with the stacked 十 and base 一 the way 龺 needs.
# fresh_component: zhao_left_for_qian (龺 as three horizontals + one long central shu)
#
# p3_char_0576_乾 — 乾 (qián). Left = 龺 (十 stacked with 日/曰 and base 一,
# pierced by long central shu). Right = 乞 (short 丿 + 一 + 乙-form 竖弯钩).
# Render fresh with PIL primitives. GT shows relatively thin uniform ink.

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_乾.png")


def draw_qian(canvas):
    W_THIN = 6
    W = 7

    # ---------- LEFT: 龺 (roughly x = 30..135) ----------
    x_l = 40
    x_r = 128
    x_c = (x_l + x_r) // 2  # 84

    # Top tiny 丶/一 (十's 一 above)
    canvas.line([(x_c - 15, 45), (x_c + 15, 45)], fill=(0, 0, 0), width=W)

    # 十's longer heng
    canvas.line([(x_l - 8, 82), (x_r + 8, 82)], fill=(0, 0, 0), width=W)

    # 日/曰 box (more compact vertically)
    y_box_top = 110
    y_box_bot = 175
    y_box_mid = 143
    canvas.line([(x_l, y_box_top), (x_r, y_box_top)], fill=(0, 0, 0), width=W)
    canvas.line([(x_l, y_box_top), (x_l, y_box_bot)], fill=(0, 0, 0), width=W_THIN)
    canvas.line([(x_r, y_box_top), (x_r, y_box_bot)], fill=(0, 0, 0), width=W_THIN)
    canvas.line([(x_l + 3, y_box_mid), (x_r - 3, y_box_mid)], fill=(0, 0, 0), width=W_THIN)
    canvas.line([(x_l, y_box_bot), (x_r, y_box_bot)], fill=(0, 0, 0), width=W)

    # Base horizontal (bottom 一 of 龺) — long, wider than box
    canvas.line([(x_l - 15, 240), (x_r + 15, 240)], fill=(0, 0, 0), width=W)

    # Long central 竖 — pierces from top heng down through box to base
    canvas.line([(x_c, 55), (x_c, 240)], fill=(0, 0, 0), width=W)

    # ---------- RIGHT: 乞 (roughly x = 155..280) ----------
    # Short 丿 (top slanting stroke): from upper-right going down-left
    canvas.line([(230, 55), (185, 105)], fill=(0, 0, 0), width=W)

    # 一 (horizontal below the pie), slight rise to the right
    canvas.line([(160, 135), (280, 128)], fill=(0, 0, 0), width=W)

    # 乙-form 竖弯钩 (bottom sweep): starts near right end of the 一,
    # short down segment, curves down-left then sweeps right along bottom, hook up
    pts = [
        (240, 150),
        (215, 180),
        (195, 215),
        (200, 245),
        (225, 265),
        (260, 268),
        (285, 260),  # hook up
        (283, 240),
    ]
    for i in range(len(pts) - 1):
        canvas.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=W)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_qian(d)
    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
