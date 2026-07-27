# p3_char_0002_丨 — character 丨 (gun), 1 stroke.
#
# GT observation (gt/phase3/丨.png): identical shape to the phase-2
# radical form — a slight rightward-scooping head at the top followed
# by a long straight vertical descent. Slim ink (~10 px).
#
# Strategy: reuse the bank primitive `draw_gun_radical` from
# success_bank/code/gun_radical.py at deliberate (ox, oy, scale)=(0,0,1.0).
# The canonical unit already matches the GT geometry (head arc from
# math (-6,+85) to (+4,+60), shaft to (+4,-100), thickness 10).
# TR1-compliant: (ox, oy, scale) chosen deliberately (not defaults —
# 0,0,1.0 is the correct deliberate value for a full-canvas standalone).

import os
import sys
from PIL import Image, ImageDraw

# Import the bank primitive
HERE = os.path.dirname(os.path.abspath(__file__))
BANK_CODE = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_CODE)
from gun_radical import draw_gun_radical  # noqa: E402

CANVAS = 300
OUT_PNG = os.path.join(HERE, "01_丨.png")


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Standalone character on full canvas — center, unit scale.
    draw_gun_radical(draw, ox=0.0, oy=0.0, scale=1.0)
    img.save(OUT_PNG)


if __name__ == "__main__":
    main()
