# p3_char_0166_去 (qù, "to go") — 5 strokes: 土 (heng+shu+heng) + 厶 (撇折+点).
# G3 coord-bank recipe.
# Composition: 土 on top half (reuse tu.py at scale ~0.75, shifted up),
# 厶 inlined on bottom half (no bank entry; 厶 is in errata).
#
# Math-coord convention: (0,0) = canvas center, +y is UP.
# _to_pixel handles the PIL flip.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from tu import draw_tu  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_si_inline(t, ox=0.0, oy=0.0, scale=1.0):
    """厶 inlined — 2 strokes: 撇折 (long) + 点 (short).

    撇折: starts near top-center, sweeps down-left as 撇, then turns
          and runs rightward as a slanted heng along the bottom.
    点  : short slanted stroke on the upper-right, above the folded heng.
    """
    thick = max(4, int(round(8 * scale)))

    # 撇折: two segments joined at the bottom-left corner.
    # Top head A -> bottom-left elbow B -> right end C.
    A = (ox + 5 * scale,   oy + 35 * scale)     # top start of pie
    B = (ox - 45 * scale,  oy - 25 * scale)     # elbow (bottom-left)
    C = (ox + 50 * scale,  oy - 30 * scale)     # right end of the folded heng

    ax, ay = _to_pixel(*A)
    bx, by = _to_pixel(*B)
    cx, cy = _to_pixel(*C)

    t.line([(ax, ay), (bx, by)], fill=(0, 0, 0), width=thick)
    t.line([(bx, by), (cx, cy)], fill=(0, 0, 0), width=thick)

    # 点 (dot): short slanted stroke at upper-right, above the heng leg.
    D1 = (ox + 30 * scale, oy + 5 * scale)
    D2 = (ox + 48 * scale, oy - 15 * scale)
    d1x, d1y = _to_pixel(*D1)
    d2x, d2y = _to_pixel(*D2)
    t.line([(d1x, d1y), (d2x, d2y)],
           fill=(0, 0, 0), width=max(5, int(round(10 * scale))))


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # 土 on top — reuse bank primitive.
    # tu.py at scale=1.0 spans roughly y=+30 (top heng) to y=-80 (bottom
    # heng). We want it in the upper half of the canvas, so lift oy.
    draw_tu(t, ox=0, oy=55, scale=0.75)

    # 厶 on bottom — inlined, larger, centered in the lower ~40% of canvas.
    draw_si_inline(t, ox=0, oy=-70, scale=1.15)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_去.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
