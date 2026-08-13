# p3_char_0460_皅 — 白 (LEFT compressed) + 巴 (RIGHT inline)
# 巴 not in bank → fresh inline render.
# Uses bank primitive bai_char_compressed_for_LR for LEFT slot.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from bai_char_compressed_for_LR import draw_bai_compressed  # noqa: E402


def draw_ba_right(canvas, x_left=160, x_right=250,
                  y_top=75, y_bot=250):
    """Fresh render of 巴 sitting in the RIGHT slot.
    Standard 4-stroke construction: 横折 top, 竖 left, 横 middle,
    竖弯钩 base with rightward horizontal and upward hook.
    """
    w = 9
    w_mid = 7
    y_mid = int(y_top + (y_bot - y_top) * 0.52)

    # Stroke 1: 竖 left (top-left → bottom-left)
    canvas.line([(x_left, y_top), (x_left + 2, y_bot - 30)],
                fill=(0, 0, 0), width=w)

    # Stroke 2: 横折 — top 横 then right 竖 down (full down to near baseline,
    # closes the box on the right).
    canvas.line([(x_left - 2, y_top), (x_right, y_top + 2)],
                fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top + 2), (x_right - 2, y_bot - 12)],
                fill=(0, 0, 0), width=w)

    # Stroke 3: 横 middle (inside the box, small gap on right)
    canvas.line([(x_left + 4, y_mid), (x_right - 10, y_mid + 4)],
                fill=(0, 0, 0), width=w_mid)

    # Stroke 4: 竖弯钩 — sweeping base that runs from bottom-left of body,
    # right along baseline PAST the right wall, then hooks UP.
    base_y = y_bot
    # a. horizontal base sweep (extends past x_right)
    canvas.line([(x_left + 2, base_y - 6),
                 (x_right + 14, base_y)],
                fill=(0, 0, 0), width=w)
    # b. upward hook at the right tail
    canvas.line([(x_right + 14, base_y),
                 (x_right + 8, base_y - 32)],
                fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # LEFT: 白 compressed (bank primitive, default footprint 42..122 / 92..252)
    draw_bai_compressed(d, x_left=32, x_right=112,
                        y_top=100, y_bot=248)

    # RIGHT: 巴 (fresh)
    draw_ba_right(d, x_left=155, x_right=245,
                  y_top=75, y_bot=250)

    out = os.path.join(os.path.dirname(__file__), "01_皅.png")
    img.save(out)


if __name__ == "__main__":
    main()
