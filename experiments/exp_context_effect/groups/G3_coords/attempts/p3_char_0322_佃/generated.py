# p3_char_0322_佃 — 佃 (diàn), 7 strokes: 亻 (left, 2) + 田 (right, 5).
# Composition: bank ren_pang on left + inline 田 (box + cross) on right.
# Follows the men_plural / zhong_char L-R pattern (see drawer_memory.md).
# The 田 form has no bank entry; jia_first is closest but has the long
# extending 竖 below — for 田 the box closes at bottom.

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang import draw_ren_pang  # noqa: E402


def draw_tian(d, ox=0, oy=0, scale=1.0):
    """田 (field), 5 strokes: 竖 + 横折 + 竖(mid) + 横(mid) + 横(bottom).
    Roughly square box centered on (ox, oy)."""
    x_left = -50 + ox
    x_right = 55 + ox
    y_top = -60 + oy
    y_bot = 55 + oy
    y_mid = int((y_top + y_bot) / 2)
    x_mid = int((x_left + x_right) / 2)
    w = max(1, int(round(9 * scale)))
    w_thin = max(1, int(round(7 * scale)))

    # Stroke 1: left 竖
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top heng + right shu)
    d.line([(x_left - 2, y_top), (x_right + 2, y_top)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle 竖
    d.line([(x_mid, y_top + 4), (x_mid, y_bot - 3)], fill=(0, 0, 0), width=w_thin)
    # Stroke 4: middle 横
    d.line([(x_left + 3, y_mid), (x_right - 3, y_mid)], fill=(0, 0, 0), width=w_thin)
    # Stroke 5: bottom 横
    d.line([(x_left - 2, y_bot), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 on left — proven ren_pang offsets from zhong_char / men_plural
    draw_ren_pang(d, ox=-55.0, oy=0.0, scale=0.85)

    # 田 on right — centered around x=205, roughly y-centered (slightly high)
    draw_tian(d, ox=205, oy=145, scale=0.88)

    out = os.path.join(os.path.dirname(__file__), "01_佃.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
