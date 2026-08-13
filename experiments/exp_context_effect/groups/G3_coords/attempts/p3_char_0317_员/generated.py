# 员 (yuán, "member") — 7 strokes.
# Composition: 口 (top, small) + 贝 (bottom, spans most of canvas).
# GT observation: kou is a small compact box in the upper third. 贝 below
# is a taller box (with one interior horizontal + bottom-closing horizontal)
# and two splayed legs 撇 + 点 at the base.
# Uniform thin stroke width per P12 (MMH GT thin lines).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from kou import draw_kou  # noqa: E402

CANVAS = 300
CX = CANVAS / 2
CY = CANVAS / 2

INK = (0, 0, 0)
WIDTH = 5  # thin uniform per P12


def M(x, y):
    """Math-coord (center, +y up) -> PIL pixel."""
    return (CX + x, CY - y)


def draw_yuan(t, ox=0, oy=0, scale=1.0):
    # --- Top: 口 (small, upper region) ---
    # kou primitive has box roughly ±65 wide, ±50 tall at scale 1.
    # Place at oy=+100 with slightly larger scale to match GT proportions.
    draw_kou(t, ox=ox + 0, oy=oy + 100 * scale, scale=0.38 * scale)

    # --- Bottom: 贝 ---
    # Outer box top ~y=+55, sides at x=±42. Descend to y=-30 (taller box).
    # Interior horizontal ~y=+15. Bottom-closing horizontal at y=-30.
    # Then 撇 leg from (-32,-30) to (-95,-110) and 点 leg from (+32,-30)
    # to (+95,-110).

    # Stroke: 竖 (left side of 贝 box)
    t.line([M(-42 * scale, 55 * scale), M(-42 * scale, -30 * scale)],
           fill=INK, width=WIDTH)

    # Stroke: 横折 (top + right side)
    t.line([M(-42 * scale, 55 * scale), M(42 * scale, 55 * scale)],
           fill=INK, width=WIDTH)
    t.line([M(42 * scale, 55 * scale), M(42 * scale, -30 * scale)],
           fill=INK, width=WIDTH)

    # Stroke: interior 横
    t.line([M(-42 * scale, 15 * scale), M(42 * scale, 15 * scale)],
           fill=INK, width=WIDTH)

    # Stroke: bottom-closing 横 (base of 贝 box)
    t.line([M(-42 * scale, -30 * scale), M(42 * scale, -30 * scale)],
           fill=INK, width=WIDTH)

    # Stroke: 撇 leg (down-left from bottom-left of box)
    t.line([M(-32 * scale, -30 * scale), M(-95 * scale, -110 * scale)],
           fill=INK, width=WIDTH)

    # Stroke: 点 leg (down-right from bottom-right of box)
    t.line([M(32 * scale, -30 * scale), M(95 * scale, -110 * scale)],
           fill=INK, width=WIDTH)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_yuan(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_员.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
