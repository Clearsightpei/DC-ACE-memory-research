# p3_char_0294_町 — 町 (chō), 7 strokes.
# Structure: 田 on the left (5 strokes: box + inner cross) + 丁 on the right (2 strokes).
# Bank reference: da_hit.py showed the L-R composition style; jia_first.py
# and shen_extend.py showed the box+inner-heng pattern for 田-family frames;
# ding_char.py is the right-side 丁 primitive.
# Under v8, 田 has no exact bank fit — inline fresh with PIL.
# Right-side 丁: use bank draw_ding_char via math-coord composition (as da_hit).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ding_char import draw_ding_char  # noqa: E402

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
t = ImageDraw.Draw(img)


def draw_tian_frame(canvas, x_left, x_right, y_top, y_bot, w=8, w_mid=7):
    """Inline 田 — box + inner cross (middle heng + middle shu)."""
    x_center = (x_left + x_right) // 2
    y_middle = (y_top + y_bot) // 2
    # Stroke 1: left 竖
    canvas.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top heng + right shu)
    canvas.line([(x_left - 2, y_top), (x_right + 2, y_top)], fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: inner middle 竖 (vertical crossing)
    canvas.line([(x_center, y_top + 3), (x_center, y_bot - 3)], fill=(0, 0, 0), width=w_mid)
    # Stroke 4: inner middle heng
    canvas.line([(x_left + 3, y_middle), (x_right - 3, y_middle)], fill=(0, 0, 0), width=w_mid)
    # Stroke 5: bottom heng
    canvas.line([(x_left - 2, y_bot), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w)


# Left: 田 — sits left, moderate size (GT shows 田 at roughly middle-left).
# PIL coords (top-left origin, y grows down)
draw_tian_frame(t, x_left=40, x_right=140, y_top=90, y_bot=220, w=8, w_mid=7)

# Right: 丁 — bank primitive uses math coords (center origin, +y up).
# GT shows 丁's heng starting from near the top of 田 and extending wide right;
# shu descends past bottom of 田 with a small hook. Bring 丁 closer to 田 (smaller gap).
draw_ding_char(t, ox=35, oy=25, scale=0.90)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_町.png")
img.save(out_path)
print("saved", out_path)
