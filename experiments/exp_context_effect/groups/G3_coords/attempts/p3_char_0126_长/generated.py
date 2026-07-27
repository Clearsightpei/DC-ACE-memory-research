# p3_char_0126_长 — 长 (zhǎng), 4 strokes, simplified form.
# REVISION 1: enlarged the character to fill more of the 300x300 canvas
# (was ~140px tall, GT is ~200px), reduced line widths toward MMH-thin
# (P12), extended the vertical shaft ABOVE the heng crossbar (in the GT
# the 竖 crosses through the heng, not hangs from it), and enlarged the
# 捺 sweep so its tail reaches near the bottom-right corner.
#
# Strokes (in order): 撇 (short top pie), 一 (heng crossbar), 竖提, 捺.
#
# GT observations that drove revision:
#   - Top short 撇 sits at ~x=[-45,-15], y=[+80,+40] — small, upper-left.
#   - Heng spans ~[-70, +65] at y~+15, thin (~4-5 px).
#   - 竖 crosses the heng: top ~y=+35, bottom ~y=-95, ti flick to (+5,-80).
#     Shaft slightly left of center (~x=-30).
#   - 捺 head near the top of the vertical shaft (~x=-15, y=+40), tail
#     at bottom-right (~x=+110, y=-105). Big sweep, moderate belly.

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(
    os.path.join(_HERE, "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

CANVAS = 300


def _to_pixel(ox, oy):
    """Math (+y up, center origin) -> PIL pixel (+y down, top-left origin)."""
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_bezier(draw, x0, y0, cx, cy, x1, y1,
                    w_head, w_tail, n=60):
    """Quadratic bezier with linearly-tapered stamped width."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _tapered_line(draw, x0, y0, x1, y1, w_head, w_tail, n=40):
    """Straight tapered stamped stroke."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = x0 + (x1 - x0) * u
        by = y0 + (y1 - y0) * u
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _na_style(draw, x0, y0, cx, cy, x1, y1,
              w_head=3.0, w_belly=13.0, w_tail=3.0, n=70, t_belly=0.72):
    """Bezier with head->belly->tail piecewise-linear width — mimics 捺."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        if u <= t_belly:
            w = w_head + (w_belly - w_head) * (u / t_belly)
        else:
            w = w_belly + (w_tail - w_belly) * ((u - t_belly) / (1 - t_belly))
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_zhang(draw, ox=0.0, oy=0.0, scale=1.0):
    """Draw 长 (zhǎng) at (ox, oy) with scale."""

    # 1. Top short 撇 — upper-left small diagonal.
    _tapered_bezier(
        draw,
        x0=ox + -15 * scale, y0=oy + 80 * scale,   # upper-right head
        cx=ox + -30 * scale, cy=oy + 65 * scale,
        x1=ox + -50 * scale, y1=oy + 40 * scale,   # lower-left tail
        w_head=6.5 * scale, w_tail=2.0 * scale,
    )

    # 2. Wide 横 crossbar — thin, uniform (P12 MMH-thin).
    _tapered_line(
        draw,
        x0=ox + -75 * scale, y0=oy + 15 * scale,
        x1=ox + 70 * scale, y1=oy + 15 * scale,
        w_head=5.0, w_tail=5.0, n=50,
    )

    # 3. 竖提 — vertical shaft crossing the heng.
    #    Top well above the heng (~y=+40), bottom near y=-95, then ti flick.
    _tapered_line(
        draw,
        x0=ox + -30 * scale, y0=oy + 40 * scale,
        x1=ox + -30 * scale, y1=oy + -95 * scale,
        w_head=5.5, w_tail=5.5,
    )
    # Ti flick at base of the vertical, going up-right.
    _tapered_line(
        draw,
        x0=ox + -30 * scale, y0=oy + -95 * scale,
        x1=ox + 5 * scale, y1=oy + -78 * scale,
        w_head=6.0, w_tail=1.5,
    )

    # 4. Big 捺 sweep — head near top of vertical, tail bottom-right.
    _na_style(
        draw,
        x0=ox + -18 * scale, y0=oy + 35 * scale,
        cx=ox + 30 * scale, cy=oy + -5 * scale,
        x1=ox + 110 * scale, y1=oy + -105 * scale,
        w_head=2.5, w_belly=11.0, w_tail=2.5,
        n=80, t_belly=0.72,
    )


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_zhang(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_长.png")
    img.save(out)
    print(f"saved {out}")


if __name__ == "__main__":
    main()
