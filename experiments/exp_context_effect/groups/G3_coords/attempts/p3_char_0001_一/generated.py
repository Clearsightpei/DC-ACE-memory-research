# p3_char_0001_一 — G3 attempt
# 一 is a single 横 stroke. Bank primitive draw_yi (yi.py) is a
# direct fit: it renders a subtly tapered 横 with soft head-顿,
# thin mid, and small tail-顿. Passed at position 37 as radical.
#
# For the standalone character version, GT shows the stroke slightly
# below vertical center (PIL y ~195) and spanning ~60% of canvas.
# yi.py defaults (oy=-45, length_px=176) match this. Called with
# deliberate (ox=0, oy=-45, scale=1.0) per TR1-TR3.

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from yi import draw_yi  # noqa: E402

OUT = Path(__file__).parent / "01_一.png"

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
t = ImageDraw.Draw(img)

# Deliberate placement (TR-compliant): center horizontally (ox=0),
# stroke sits at math y=-45 (PIL y=195), scale 1.0 for standalone char.
draw_yi(t, ox=0.0, oy=-45.0, scale=1.0)

img.save(OUT)
print(f"wrote {OUT}")
