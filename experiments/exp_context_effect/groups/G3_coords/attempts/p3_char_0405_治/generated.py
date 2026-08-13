# 治 (zhì) — p3_char_0405
# LR composition: 氵 (left) + 台 (right).
# Left uses bank san_dian_shui at deliberate (ox, oy, scale) per TR1-TR3.
# Right (台 = 厶 + 口): 口 uses bank kou; 厶 inlined fresh (no bank entry).
# No BANK_DEVIATION needed — san_dian_shui + kou called directly; 厶 has
# no bank entry so inline is the only option.

import os
import sys

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from san_dian_shui import draw_san_dian_shui  # noqa: E402
from kou import draw_kou  # noqa: E402

CANVAS = 300
INK = (0, 0, 0)


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_line(draw, p0, p1, w0, w1, steps=40):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def _tapered_bezier(draw, p0, p1, p2, w0, w1, steps=60):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u ** 2 * x2
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u ** 2 * y2
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def draw_si_private(d, cx, cy, size=1.0):
    """厶 (private) — 2 strokes: 撇 (down-left) + 折(right + down turn).
    Centered at (cx, cy) pixel coords, `size` scales the whole shape.
    Renders at approximately 60*size wide, 45*size tall.
    """
    s = size
    # Stroke 1: 撇 — top-right down to lower-left. Slightly bowed.
    p0 = (cx + 22 * s, cy - 22 * s)   # head, upper-right
    p1 = (cx + 5 * s,  cy - 5 * s)    # control (bow toward center)
    p2 = (cx - 28 * s, cy + 18 * s)   # tail, lower-left
    _tapered_bezier(d, p0, p1, p2, w0=6, w1=3)
    # Stroke 2: 折 — starts at pie mid-bottom area, goes right then down (dot).
    # Actually a short 横折点 form: heng right, then dot down.
    h0 = (cx - 6 * s,  cy + 8 * s)
    h1 = (cx + 20 * s, cy + 8 * s)
    _tapered_line(d, h0, h1, w0=5, w1=6)
    # Small dot descending from the fold tip
    d0 = (cx + 20 * s, cy + 8 * s)
    d1 = (cx + 26 * s, cy + 22 * s)
    _tapered_line(d, d0, d1, w0=6, w1=7)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # LEFT: 氵 — bank primitive, shifted left, moderate scale.
    draw_san_dian_shui(d, ox=-85, oy=+5, scale=0.85)

    # RIGHT: 台
    # Component split within right half:
    #   厶 top:   pixel (215, 95)
    #   一 line under 厶 (part of the ム-tail spread)
    #   口 bottom: math (ox=+45, oy=-45), small scale
    # 厶
    draw_si_private(d, cx=215, cy=95, size=1.1)
    # A short horizontal 一 tucked under 厶 (the ム-stroke tail extension)
    _tapered_line(d, (172, 158), (258, 158), w0=6, w1=7)
    # 口 at bottom-right — bank kou, scale 0.55
    draw_kou(d, ox=+50, oy=-55, scale=0.55)

    out_path = os.path.join(os.path.dirname(__file__), "01_治.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
