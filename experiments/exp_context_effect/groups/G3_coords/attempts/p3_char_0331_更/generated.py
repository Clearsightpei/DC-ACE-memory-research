# p3_char_0331_更 — 更 (gèng/gēng), 7 strokes.
# Composition: top 横 + 曰-style box (with middle bar) + long 撇 sweeping
# down-left through the box + long 捺 sweeping down-right.
# Inspired by shen_extend.py (box + protruding shu) but here the "legs"
# are 撇 & 捺 instead of a central 竖.
#
# Strokes (roughly MMH order):
#   1. 横 (top horizontal, above box)
#   2. 竖 (left side of box)
#   3. 横折 (top + right of box)
#   4. 横 (middle bar inside box)
#   5. 横 (bottom of box)
#   6. 撇 (long, from top-center down-left to bottom-left area)
#   7. 捺 (long, from middle down-right to bottom-right area)

import os
from PIL import Image, ImageDraw

CANVAS = 300
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(OUT_DIR, "01_更.png")


def draw_geng(draw, ox=0, oy=0, scale=1.0):
    # Top 横 — MMH GT is thin uniform lines; use w~5 (P12).
    y_top_heng = 65 + oy
    x_top_left = 55 + ox
    x_top_right = 250 + ox
    w_top = max(1, int(round(5 * scale)))
    draw.line([(x_top_left, y_top_heng), (x_top_right, y_top_heng)],
              fill=(0, 0, 0), width=w_top)

    # Box (曰-style, squat, in the upper-middle band)
    x_left = 90 + ox
    x_right = 210 + ox
    y_top = 90 + oy
    y_bot = 185 + oy
    y_mid = 138 + oy
    w = max(1, int(round(5 * scale)))
    w_mid = max(1, int(round(5 * scale)))

    # Stroke 2: left 竖
    draw.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: 横折 (top horizontal + right vertical)
    draw.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    draw.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 4: middle 横
    draw.line([(x_left + 2, y_mid), (x_right - 2, y_mid)],
              fill=(0, 0, 0), width=w_mid)
    # Stroke 5: bottom 横
    draw.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)

    # Stroke 6: long 撇 — sweeps from just below top-heng, near the
    # horizontal midline of the box on the LEFT side, curving out and
    # down to the bottom-left corner of the canvas.
    # Use a quadratic-ish curve via multiple line segments.
    pie_head = (150 + ox, 78 + oy)   # starts just below top-heng, near horizontal center
    pie_mid = (115 + ox, 205 + oy)
    pie_tail = (45 + ox, 275 + oy)
    w_pie = max(1, int(round(5 * scale)))
    # simple bezier-ish via 3 segments
    _draw_curve(draw, pie_head, pie_mid, pie_tail, w_pie)

    # Stroke 7: long 捺 — starts inside the box near center, sweeps
    # down-right past the right edge, ending at bottom-right area with
    # a flat tail.
    na_head = (160 + ox, 148 + oy)
    na_mid = (210 + ox, 225 + oy)
    na_tail = (275 + ox, 278 + oy)
    w_na = max(1, int(round(5 * scale)))
    _draw_curve(draw, na_head, na_mid, na_tail, w_na)


def _draw_curve(draw, p0, p1, p2, width, steps=24):
    """Draw a quadratic bezier by line segments."""
    prev = p0
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        draw.line([prev, (x, y)], fill=(0, 0, 0), width=width)
        prev = (x, y)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)
    draw_geng(draw)
    img.save(OUT_PNG)
    print(f"wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
