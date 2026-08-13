# p3_char_0299_里 — draw 里 (li), 7 strokes
# Structure: 田-like top rectangle (with internal + cross via long
# vertical + one middle heng) + 土-like extension below (short heng + long base heng).
# GT observation: thin uniform ink, top rectangle a bit narrower than
# the bottom base heng which is the widest stroke. Central vertical
# runs from top of rectangle down to the base heng.

import os
from PIL import Image, ImageDraw

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SIZE = 300


def draw_li(draw):
    # Top rectangle (田 upper part) — a bit narrow-tall
    rect_l, rect_r = 95, 205
    rect_t, rect_b = 55, 175

    # Central long vertical, spans from top of rectangle through middle
    # and down to the base heng near the bottom.
    vx = 150
    v_top = rect_t
    v_bot = 258

    w = 5  # ink width uniform-ish

    # Stroke 1: left vertical of rectangle
    draw.line([(rect_l, rect_t), (rect_l, rect_b)], fill='black', width=w)
    # Stroke 2: 横折 — top heng then right vertical
    draw.line([(rect_l, rect_t), (rect_r, rect_t)], fill='black', width=w)
    draw.line([(rect_r, rect_t), (rect_r, rect_b)], fill='black', width=w)
    # Stroke 3: middle heng inside rectangle
    mid_y = (rect_t + rect_b) // 2
    draw.line([(rect_l, mid_y), (rect_r, mid_y)], fill='black', width=w)
    # Stroke 4: bottom of rectangle (also serves as heng)
    draw.line([(rect_l, rect_b), (rect_r, rect_b)], fill='black', width=w)
    # Stroke 5: long central vertical through the rectangle down
    draw.line([(vx, v_top), (vx, v_bot)], fill='black', width=w)
    # Stroke 6: short middle heng between rectangle bottom and base
    short_y = 215
    draw.line([(115, short_y), (185, short_y)], fill='black', width=w)
    # Stroke 7: long base heng — widest stroke
    base_y = v_bot
    draw.line([(60, base_y), (240, base_y)], fill='black', width=w)


def main():
    img = Image.new('RGB', (SIZE, SIZE), 'white')
    d = ImageDraw.Draw(img)
    draw_li(d)
    img.save(os.path.join(OUT_DIR, '01_里.png'))


if __name__ == '__main__':
    main()
