# p3_char_0159_申 — 申 (shēn), 5 strokes.
# Composition: 日-like box in middle band + central 竖 that protrudes
# above the box and below the box. Similar strategy to 中 (kou + shu),
# but the box has a middle 横 like 日.
#
# Strokes (MMH order for 申):
#   1. 竖 (left side of box)
#   2. 横折 (top + right of box)
#   3. 横 (middle bar inside the box)
#   4. 横 (bottom of box)
#   5. 竖 (central vertical, protruding top & bottom)
#
# Approach: shrink ri-style box to middle band, then draw central shu
# extending above (top ~y=30) and below (bot ~y=280).

import os
import sys
from PIL import Image, ImageDraw

CANVAS = 300
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(OUT_DIR, "01_申.png")


def draw_shen(draw, ox=0, oy=0, scale=1.0):
    # Box (日-shaped) occupies the middle band, narrower than tall.
    x_left = 85 + ox
    x_right = 215 + ox
    y_top = 100 + oy   # top of box
    y_bot = 210 + oy  # bottom of box
    y_mid = 155 + oy  # middle bar

    w = max(1, int(round(9 * scale)))   # box strokes
    w_mid = max(1, int(round(8 * scale)))
    w_shu = max(1, int(round(10 * scale)))  # central 竖

    # Stroke 1: left 竖 (box)
    draw.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top horizontal + right vertical)
    draw.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    draw.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle 横 (inside box)
    draw.line([(x_left + 2, y_mid), (x_right - 2, y_mid)],
              fill=(0, 0, 0), width=w_mid)
    # Stroke 4: bottom 横 (box)
    draw.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 5: central 竖 — protrudes above top of box and below bottom
    x_center = (x_left + x_right) // 2
    y_shu_top = 35 + oy
    y_shu_bot = 275 + oy
    draw.line([(x_center, y_shu_top), (x_center, y_shu_bot)],
              fill=(0, 0, 0), width=w_shu)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)
    draw_shen(draw)
    img.save(OUT_PNG)
    print(f"wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
