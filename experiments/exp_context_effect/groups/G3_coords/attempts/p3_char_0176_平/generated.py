# p3_char_0176_平 — 平 (píng), 5 strokes.
# Stroke order (MMH): 1) short top 一, 2) 丶 left dot, 3) 丿 right sweep,
# 4) long 一 across middle, 5) 丨 vertical through the long heng.
#
# Reuses shared bank primitives (heng, shu) with deliberate (ox, oy, scale)
# per TR1-TR3. The two side dots are inlined tapered short strokes
# (small pie-like left, small na-like right) — not the heavy 点 primitive,
# which is too large and heavy for this position (GT dots are thin ~4 px).

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_line(t, x0, y0, x1, y1, w_head, w_tail, n=24):
    """Straight tapered line from (x0,y0) to (x1,y1) in math coords."""
    prev = None
    for i in range(n + 1):
        u = i / n
        mx = x0 + (x1 - x0) * u
        my = y0 + (y1 - y0) * u
        px, py = _to_pixel(mx, my)
        if prev is not None:
            w = w_head * (1 - u) + w_tail * u
            wi = max(1, int(round(w)))
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _thin_line(t, x0, y0, x1, y1, w=5):
    """Uniform-width thin line in math coords (matches MMH GT style)."""
    p0 = _to_pixel(x0, y0)
    p1 = _to_pixel(x1, y1)
    t.line([p0, p1], fill=(0, 0, 0), width=w)


def draw_ping(t, ox=0.0, oy=0.0, scale=1.0):
    """Draw 平 centered around (ox, oy). Thin uniform widths per P12 (MMH GT)."""
    W = 5  # uniform thin width matching GT style

    # 1) Short top 横 — high on canvas, narrow.
    _thin_line(t,
               x0=ox + (-40) * scale, y0=oy + 78 * scale,
               x1=ox + 40 * scale,    y1=oy + 78 * scale,
               w=W)

    # 2) Left small pie — starts near top-heng right-center, sweeps down-left.
    _thin_line(t,
               x0=ox + (-8)  * scale, y0=oy + 65 * scale,
               x1=ox + (-42) * scale, y1=oy + 35 * scale,
               w=W)

    # 3) Right small down-right sweep — mirrors the left.
    _thin_line(t,
               x0=ox + 8  * scale, y0=oy + 65 * scale,
               x1=ox + 42 * scale, y1=oy + 35 * scale,
               w=W)

    # 4) Long middle 横 — wide, centered.
    _thin_line(t,
               x0=ox + (-110) * scale, y0=oy + 5 * scale,
               x1=ox + 110  * scale,   y1=oy + 5 * scale,
               w=W)

    # 5) Long vertical 竖 — from just above middle heng down past bottom.
    _thin_line(t,
               x0=ox + 0, y0=oy + 45  * scale,
               x1=ox + 0, y1=oy + (-125) * scale,
               w=W)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_ping(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_平.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
