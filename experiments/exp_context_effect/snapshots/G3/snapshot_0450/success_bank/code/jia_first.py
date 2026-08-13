# p3_char_0157_甲 — 甲 (jiǎ), 5 strokes.
# Structure: rectangular box (like a compressed 日) in the upper portion
# with a horizontal middle bar (like 田's middle heng), and a long
# vertical extending well below the box.
# Strokes: 竖(left) + 横折(top+right) + 横(middle) + 横(bottom) + 长竖(center, extends down)
# Bank-inspired: similar layout to ri.py, but the middle vertical
# continues below the bottom heng (like 中 but with a full box).
# Inline fresh — no exact bank fit for the extending-vertical box form.

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_甲.png")


def draw(canvas, ox=0, oy=0, scale=1.0):
    # Box occupies upper portion; vertical extends down below
    x_left = 80 + ox
    x_right = 220 + ox
    y_top = 55 + oy
    y_bot = 175 + oy   # bottom of box (upper portion only)
    y_mid = 115 + oy   # middle horizontal
    x_center = (x_left + x_right) // 2
    y_extend = 285 + oy  # end of long vertical below the box

    w = max(1, int(round(9 * scale)))
    w_mid = max(1, int(round(8 * scale)))
    w_vert = max(1, int(round(10 * scale)))

    # Stroke 1: left 竖 (left side of box)
    canvas.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top heng + right shu)
    canvas.line([(x_left - 2, y_top), (x_right + 2, y_top)], fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle heng
    canvas.line([(x_left + 3, y_mid), (x_right - 3, y_mid)], fill=(0, 0, 0), width=w_mid)
    # Stroke 4: bottom heng
    canvas.line([(x_left - 2, y_bot), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 5: long central 竖 — starts near top, extends down below box
    canvas.line([(x_center, y_top + 8), (x_center, y_extend)], fill=(0, 0, 0), width=w_vert)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw(d)
    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
