"""p3_char_0030_冫 (bing) — G3 coord-bank attempt.

冫 is a 2-stroke character (identical to the radical form). Bank has a
mastered `draw_bing` primitive from p2_radical_012 that composes:
  - top dian (scaled 0.55)
  - inlined bottom down-left slash with small up-right flick

Per memory_index.md read order: form_catalog doesn't add a new context
row for 冫 (bank primitive fits the standalone form). Use the frozen
primitive with deliberate (ox, oy, scale) per TR1-TR3.

GT inspection: 冫 sits roughly centered horizontally (slight lean right)
and vertically-centered on the 300x300 canvas. Two strokes visible:
small top dot in upper-mid, larger curved slash below-left of it.
The bank's default (ox=0, oy=0, scale=1.0) lands the top dot near the
canvas center — but GT top dot is upper-mid. Shift up by ~+15 (math
convention: +y is up) so the top dot rises above center. scale=1.0
matches GT stroke thickness / extent.
"""

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from bing import draw_bing  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    # Deliberate transform (TR1-TR3): shift up so top dian sits in upper
    # third; standalone character occupies full canvas so scale=1.0.
    draw_bing(t, ox=0.0, oy=15.0, scale=1.0)
    out = os.path.join(_HERE, "01_冫.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    main()
