"""p3_char_0227_年 — G3 attempt.

年 (nián, year). Reading the GT: descending 撇 from upper-center down-left,
short top 横 to its right, long middle 横, shorter mid-lower 横, long bottom
横, and a long central 竖 running through all horizontals to the bottom.

v8: bank primitives REFERENCE ONLY; hand-derived fresh from GT (trust GT).
"""
from PIL import Image, ImageDraw
from pathlib import Path

W = H = 300
im = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(im)

INK = "black"
LW = 6  # ink width (calligraphic-ish, MMH is a bit thinner but consistent)

# 1. 撇 — top-left descending slash from just right-of-center-top down-left
d.line([(155, 55), (95, 130)], fill=INK, width=LW)

# 2. 横 — short upper horizontal, starting at 撇/竖 join, extending right
d.line([(135, 82), (208, 82)], fill=INK, width=LW)

# 3. 横 — long middle horizontal
d.line([(55, 135), (255, 132)], fill=INK, width=LW)

# 4. 横 — shorter mid-lower horizontal
d.line([(112, 182), (208, 180)], fill=INK, width=LW)

# 5. 横 — long bottom horizontal (base)
d.line([(45, 232), (258, 230)], fill=INK, width=LW)

# 6. 竖 — long central vertical running from just under the top heng
#         through all horizontals down to the base
d.line([(158, 82), (158, 290)], fill=INK, width=LW)

out_dir = Path(__file__).parent
im.save(out_dir / "01_年.png")
print("wrote", out_dir / "01_年.png")
