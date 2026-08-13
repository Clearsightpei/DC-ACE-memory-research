# BANK_DEVIATION
# skipped: (none for 田; used quan_tian_for_LR_left as-is with tuned coords)
# reason: no bank entry exists for 圭 (土-over-土); tu.py is turtle-based and
#   cannot compose cleanly into a right-column stacked 圭 without heavy transform.
# fresh_component: gui_stacked_for_LR_right (圭 = 6-stroke inline PIL, two 土 stacked,
#   short-top-heng / middle-heng / long-bottom-heng with a shared central shu)
#
# 畦 = 田 (left ~40%) + 圭 (right ~45%). GT shows 田 sitting slightly upper
# in the left column, and 圭 spanning nearly full height on the right with
# three roughly evenly-spaced hengs; bottom heng widest.

import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from quan_tian_for_LR_left import draw_quan_tian_for_LR_left


def draw_gui_stacked_for_LR_right(d, x_left=170, x_right=260,
                                    y_top=70, y_mid_upper=115,
                                    y_mid_lower=165, y_bot=235,
                                    w=5, wm=4, black=(0, 0, 0)):
    """6-stroke 圭 = 土 upper + 土 lower, sharing a central shu that runs
    top-to-bottom. Bottom heng widest (calligraphic base)."""
    x_mid = (x_left + x_right) // 2
    # Upper 土: top-heng (short), shu, middle-heng
    # short top heng (a bit narrower than the middle heng)
    d.line([(x_left + 12, y_top), (x_right - 8, y_top)], fill=black, width=w)
    # middle heng of upper 土 (also serves as separator)
    d.line([(x_left, y_mid_upper), (x_right, y_mid_upper)], fill=black, width=w)
    # Lower 土: top-heng (short), shu (continuous), bottom-heng (widest)
    # short heng of lower 土
    d.line([(x_left + 8, y_mid_lower), (x_right - 12, y_mid_lower)],
           fill=black, width=w)
    # bottom heng (widest, with small overshoots)
    d.line([(x_left - 8, y_bot), (x_right + 8, y_bot)], fill=black, width=w)
    # Central shu — continuous from top-heng down to bottom-heng
    d.line([(x_mid, y_top), (x_mid, y_bot)], fill=black, width=wm)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 田 on left, upper-shifted per GT
    draw_quan_tian_for_LR_left(d,
                               x_left=25, x_right=115,
                               y_top=95, y_bot=200,
                               w=5, wm=4)

    # 圭 on right, full-height
    draw_gui_stacked_for_LR_right(d,
                                   x_left=170, x_right=260,
                                   y_top=65, y_mid_upper=115,
                                   y_mid_lower=170, y_bot=240,
                                   w=5, wm=4)

    out = os.path.join(HERE, "01_畦.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
