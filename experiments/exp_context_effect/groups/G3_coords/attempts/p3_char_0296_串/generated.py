# p3_char_0296_串 — 串 (chuàn, "string/skewer"), 7 strokes.
# Composition: two 口 boxes stacked vertically, both pierced by a single
# long 竖 down the center that protrudes above the top box and well below
# the bottom box.
# Recipe: bank kou twice at scale ~0.42, one high one low; then draw one
# long vertical line through the center. Trust GT: the boxes are compact
# and the piercing shu is prominent.
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from kou import draw_kou  # noqa: E402


CANVAS = 300


def _to_pixel(mx, my):
    return CANVAS / 2 + mx, CANVAS / 2 - my


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    kou_scale = 0.45
    # Top 口 — centered high on canvas.
    draw_kou(d, ox=0.0, oy=45.0, scale=kou_scale)
    # Bottom 口 — centered low on canvas.
    draw_kou(d, ox=0.0, oy=-40.0, scale=kou_scale)

    # Central piercing 竖 — passes through both boxes; protrudes a
    # little above the top box and further below the bottom box (matches
    # GT: the tail is longer than the head).
    top_y = 95
    bot_y = -120
    x_top, y_top = _to_pixel(0, top_y)
    x_bot, y_bot = _to_pixel(0, bot_y)
    d.line([(x_top, y_top), (x_bot, y_bot)], fill=(0, 0, 0), width=8)

    out = os.path.join(os.path.dirname(__file__), "01_串.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
