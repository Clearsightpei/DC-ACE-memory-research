# p3_char_0031_厂 — character 厂 (same shape as radical 厂, bank #67).
# Bank primitive draw_chang is a perfect fit: wide 横 + nearly-vertical 丿.
# For a character (vs. radical), let it fill the canvas naturally at scale 1.0.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from chang import draw_chang  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    # Use bank primitive at natural scale, centered.
    # (ox, oy, scale) deliberately chosen per TR: origin=canvas center,
    # scale 1.0 because 厂 as a standalone character should fill the canvas
    # the same way the radical PASS filled it (bank recipe already tuned for
    # ~200px span).
    draw_chang(t, ox=0.0, oy=0.0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_厂.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
