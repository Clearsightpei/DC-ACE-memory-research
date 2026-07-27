# p3_char_0106_日 — G3 attempt
# Strategy: Phase-3 char 日 has identical shape to Phase-2 radical 日
# (bank #83, ri.py). Per memory_index priority #1 (radical→char
# identity alias), call draw_ri with (ox=0, oy=0, scale=1.0).

import sys, os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from ri import draw_ri  # type: ignore

img = Image.new("RGB", (300, 300), "white")
t = ImageDraw.Draw(img)

# Identity alias: character 日 == radical 日 shape.
draw_ri(t, ox=0, oy=0, scale=1.0)

out_path = os.path.join(HERE, "01_日.png")
img.save(out_path)
print(f"wrote {out_path}")
