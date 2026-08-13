# generated.py — 区 (qū), 4 strokes: 一 (top heng) + 乂 (X cross, 撇+捺) + 乚-like bottom of 匚.
# Actually 区 = 匚 outer envelope (2 strokes: top heng + bottom 竖折) + 乂 inside (2 strokes: 撇 + 捺).
# Total 4 strokes.
#
# Retrieval:
#   form_catalog rows 143 (撇 乂 standalone) + 161 (捺 乂 standalone) — use yi_cross.py.
#   INDEX row 40: fang.py (匚) — direct radical primitive for the outer envelope.
# Composition: draw fang.py at (0, 0, 1.0) for the envelope, then draw_yi_cross
#   scaled down and placed inside the envelope. Box interior center ≈ math (-2, -22).
#   yi_cross natural spread x∈(-105..+100), y∈(+65..-110) — at scale 0.55 fits
#   inside box interior comfortably; offset to place crossing near box center.

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "success_bank", "code"))

from PIL import Image, ImageDraw
from fang import draw_fang
from yi_cross import draw_yi_cross

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
draw = ImageDraw.Draw(img)

# 1. Outer envelope 匚 — use fang.py directly at default scale.
draw_fang(draw, ox=0.0, oy=0.0, scale=1.0)

# 2. Inner 乂 — revised: scaled to 0.65 (was 0.55, too small vs GT); shifted
#    right to sit more centered in the box interior (GT shows 乂 filling most
#    of the box interior, with arms reaching near the bottom rail).
draw_yi_cross(draw, ox=+3, oy=-28, scale=0.65)

out_path = os.path.join(os.path.dirname(__file__), "01_区.png")
img.save(out_path)
print(f"wrote {out_path}")
