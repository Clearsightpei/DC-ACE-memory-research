# p3_char_0019_儿 — G3 coord-bank attempt (redo vs clean GT).
#
# Strategy: reuse the mastered er_ren radical primitive (from
# success_bank/code/er_ren.py). Character-form 儿 = same shape as
# the radical but larger, filling the canvas.
#
# TR1-TR3 compliance: (ox, oy, scale) chosen deliberately for this
# composition. Radical mastered at (0, 0, 1.0). Clean GT shows the
# character occupying roughly the full central 200x200 area, so bump
# scale to ~1.3 and slightly recenter.

import os
import sys

from PIL import Image, ImageDraw

_ROOT = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_ROOT, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from er_ren import draw_er_ren  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Character-scale composition.
    # scale=1.3 to fill the canvas the way the GT does.
    # ox=0 keeps horizontal center; oy=-5 nudges down a hair since
    # the pie head sits high in the radical primitive.
    draw_er_ren(t, ox=0, oy=-5, scale=1.3)

    out_path = os.path.join(_ROOT, "01_儿.png")
    img.save(out_path, "PNG")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
