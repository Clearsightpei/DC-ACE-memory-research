# p3_char_0446_疤 (bā) — 疒 envelope + 巴 (snake) interior.
#
# Composition (from GT):
#   1. 疒: top-right small dot, thin heng roof, long left-descending 撇,
#      two 冫 marks tucked in upper-left belly.
#   2. 巴 (4 strokes): 横折 (top+right, ends at mid) + 竖 (left) + 横 (mid)
#      + 竖弯钩 (bottom of left → base horizontal → right hook up).
#      Sits in the lower-right belly of 疒.
#
# Bank reuse:
#   - Envelope: reuse draw_ne_chuang from ne_sick.py (v9 rerun graduate).
#     Same pattern proven in shan_hernia.py (疝).
#   - Interior 巴: inline (no dedicated 巴 bank entry).
#
# No BANK_DEVIATION: envelope used as-is (proven fit for 疒-composites).

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from ne_sick import draw_ne_chuang, _tapered_line  # noqa: E402

_CANVAS = 300


def draw_ba_interior(draw, x_left=145, x_right=240,
                     y_top=130, y_mid=180, y_body_bot=222,
                     y_base=262, hook_up=232, w=5):
    """巴 rendered inline in the belly of 疒 (lower-right belly).

    Strokes:
      1. 横折  — top horizontal + right vertical (stops at y_mid)
      2. 竖    — left vertical (top to body_bot)
      3. 横    — middle horizontal
      4. 竖弯钩 — from left-body-bot, down to base, right along base,
                  hook up on the right side
    """
    # 1. 横折 (top + right-down to middle)
    draw.line([(x_left, y_top), (x_right, y_top)],
              fill=(0, 0, 0), width=w)
    draw.line([(x_right, y_top), (x_right, y_mid)],
              fill=(0, 0, 0), width=w)

    # 2. 竖 (left vertical, top down to body_bot)
    draw.line([(x_left, y_top), (x_left, y_body_bot)],
              fill=(0, 0, 0), width=w)

    # 3. 横 (middle horizontal)
    draw.line([(x_left, y_mid), (x_right, y_mid)],
              fill=(0, 0, 0), width=w)

    # 4. 竖弯钩 (from left-body-bot, drop a bit, sweep right along base,
    #           then hook up on the right)
    #    Continue left vertical down slightly, then curve right to base,
    #    then hook up.
    draw.line([(x_left, y_body_bot), (x_left, y_base)],
              fill=(0, 0, 0), width=w)
    draw.line([(x_left, y_base), (x_right + 5, y_base)],
              fill=(0, 0, 0), width=w)
    # Hook up (short vertical up-tick on the right end)
    draw.line([(x_right + 5, y_base), (x_right + 5, hook_up)],
              fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Envelope 疒 from bank.
    draw_ne_chuang(draw)
    # Interior 巴 (lower-right belly)
    draw_ba_interior(draw,
                     x_left=142, x_right=235,
                     y_top=128, y_mid=182,
                     y_body_bot=220, y_base=262, hook_up=232, w=5)
    out = os.path.join(_HERE, "01_疤.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
