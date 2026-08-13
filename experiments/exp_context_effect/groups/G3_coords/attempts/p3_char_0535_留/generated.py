# BANK_DEVIATION
# skipped: quan_tian_for_LR_left.py (used the reusable 田 primitive AS-IS
#          for the bottom slot — this is not a deviation, just noting reuse)
# reason: n/a — bank primitive fits bottom 田 as a top-bottom stack (wider box)
# fresh_component: liu_top_mao (卯-like top with two angular hooked components)
#
# 留 (liu) — top-bottom stack.
# Top: 卯-like — a small ㄥ-hook on the left + an angular 刀-like hook on the right
# Bottom: 田 (uses quan_tian_for_LR_left with widened box for centered layout)
import os
import sys
from PIL import Image, ImageDraw

# Import bank primitive
BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))
from quan_tian_for_LR_left import draw_quan_tian_for_LR_left


def draw_liu_top_left(d, w=5, black=(0, 0, 0)):
    """Top-left of 卯: a small ㄥ / short 撇 + small enclosure.
    Approx: short pie down-left, short heng, then a small hook curve."""
    # short 撇 (pie): from ~(80, 55) down-left to (60, 100)
    d.line([(85, 55), (62, 100)], fill=black, width=w)
    # short heng crossing: (65, 78) to (110, 75)
    d.line([(65, 78), (110, 75)], fill=black, width=w)
    # small enclosure: right side coming down from (110, 75) to (105, 115) with slight curve
    d.line([(110, 75), (108, 105)], fill=black, width=w)
    # bottom of enclosure short heng-hook to left
    d.line([(108, 105), (78, 115)], fill=black, width=w)


def draw_liu_top_right(d, w=5, black=(0, 0, 0)):
    """Top-right of 卯: angular 刀-like — a heng-zhe (top+right down) + a pie.
    Approx: top heng slightly slanted, then long right vertical with hook,
    and a diagonal 撇 crossing."""
    # top heng: (140, 55) to (225, 60)
    d.line([(140, 55), (225, 60)], fill=black, width=w)
    # right shu-gou coming down from (225,60) to (215, 120), then small hook
    d.line([(225, 60), (218, 120)], fill=black, width=w)
    # hook: small notch to left
    d.line([(218, 120), (205, 118)], fill=black, width=w)
    # 撇 (pie) diagonal cutting from top-right area down-left, crossing the shape
    d.line([(180, 55), (145, 125)], fill=black, width=w)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Top: 卯-like
    draw_liu_top_left(d)
    draw_liu_top_right(d)

    # Bottom: 田 — wider, centered, occupying bottom half
    draw_quan_tian_for_LR_left(d,
                                x_left=75, x_right=225,
                                y_top=150, y_bot=255,
                                w=5, wm=4)

    out = os.path.join(os.path.dirname(__file__), "01_留.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
