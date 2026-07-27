# p3_char_0149_升 — main attempt (G3, no retry)
# 升 has 4 strokes:
#   1. short 撇 at top (short leftward tick)
#   2. long 撇 sweeping from upper-middle down to lower-left (main long pie)
#   3. 横 horizontal across the middle
#   4. long 竖 on the right descending below the horizontal
#
# GT-observed layout (300x300 canvas, math coords, center=origin):
#   - short pie: from ~(-25, 90) down to ~(-55, 55)
#   - long pie: starts near (5, 80), curves down-left to ~(-95, -100)
#   - heng: from ~(-95, 10) to ~(75, 20)  (slight upward tilt right)
#   - shu: from ~(55, 90) down to ~(55, -130), long vertical on right
#
# Widths are thin/uniform to match MMH GT (per P12).

import sys
from pathlib import Path
from PIL import Image, ImageDraw

CANVAS = 300


def to_px(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_line(d, p0, p1, w):
    d.line([to_px(*p0), to_px(*p1)], fill=(0, 0, 0), width=w)
    # end caps
    for (x, y) in (p0, p1):
        px, py = to_px(x, y)
        r = w / 2.0
        d.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def draw_bezier(d, p0, p1, p2, w_head, w_tail, n=60):
    prev = None
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u ** 2 * x2
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u ** 2 * y2
        px, py = to_px(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            d.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Uniform thin widths ~5px (MMH GT style, per P12)
    W = 5

    # Stroke 1: short 撇 at top — short down-left tick near top-center
    # slightly steeper, positioned upper area
    draw_bezier(d, (-10, 105), (-25, 90), (-45, 70), W, 2)

    # Stroke 2: long 撇 — starts near top-center, curves down-left broadly
    # start near (15, 90), sweep to (-100, -110)
    draw_bezier(d, (15, 90), (-25, 10), (-100, -110), W + 1, 2)

    # Stroke 3: 横 — horizontal across the middle
    draw_line(d, (-90, 5), (75, 15), W)

    # Stroke 4: long 竖 on the right — from top down to lower area
    draw_line(d, (55, 100), (55, -125), W)

    out = Path(__file__).parent / "01_升.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
