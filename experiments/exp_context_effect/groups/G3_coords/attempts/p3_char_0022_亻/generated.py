# p3_char_0022_亻 — 亻 (ren-pang), person side-radical, 2 strokes.
#
# 亻 is a character-and-radical coincidence: the Phase-2 radical PASS
# (position 61, entry 45 in success bank) is exactly this shape. Reuse
# ren_pang directly at center, no transformation needed (scale=1.0,
# ox=oy=0). Per TR2, defaults are only appropriate when composition
# origin genuinely IS the canvas center — for a standalone radical this
# is deliberate, not accidental.

import os
import sys
from PIL import Image, ImageDraw

# Add success bank to import path.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402


def main() -> None:
    canvas = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(canvas)
    # Standalone 亻 centered on canvas: origin at canvas center, unit scale.
    draw_ren_pang(t, ox=0.0, oy=0.0, scale=1.0)
    out_path = os.path.join(_HERE, "01_亻.png")
    canvas.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
