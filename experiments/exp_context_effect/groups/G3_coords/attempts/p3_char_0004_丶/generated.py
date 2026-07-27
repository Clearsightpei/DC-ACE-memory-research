# p3_char_0004_丶 — the character 丶 (identical form to 丶 radical).
#
# Approach: 丶 as a full character occupies the whole canvas — the same
# curved slim diagonal as the 丶 radical, but scaled up so it fills
# more of the 300x300 box (radicals are usually rendered smaller since
# they're components; standalone chars fill the frame).
#
# Reuse draw_dian_radical (frozen bank primitive) with:
#  - ox=0, oy=0 (centered)
#  - scale=1.15: revision after first-pass compared to GT. First pass
#    at scale=1.55 was too long/skinny and spanned too much vertical
#    range. GT shows a compact bold curved dot occupying the middle
#    of the canvas, only ~70 px tall. A modest scale-up from the
#    radical size (radical spans ~60 px raw at scale=1.0) matches
#    the GT proportions better.
#
# TR1-TR3 compliance: (ox, oy, scale) chosen deliberately for this
# composition, not defaults. Radical form is slim/curved; character
# form is the same shape at similar size but slightly larger.

import sys, os
from PIL import Image, ImageDraw

# Add success_bank/code to import path
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from dian_radical import draw_dian_radical  # noqa: E402

CANVAS = 300
OUT_PNG = os.path.join(HERE, "01_丶.png")


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Standalone character: fill more of the canvas.
    # Radical version spans ~50px; scale up so the stroke has visual
    # weight appropriate for a full character glyph.
    draw_dian_radical(draw, ox=0.0, oy=0.0, scale=1.15)

    img.save(OUT_PNG)
    print("wrote", OUT_PNG)


if __name__ == "__main__":
    main()
