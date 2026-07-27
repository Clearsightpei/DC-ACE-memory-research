"""Render 分 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

# Top 八 (eight) — two diverging slanted strokes
# Left stroke of 八 (short 撇: from upper-center going down-left, slight curve)
# Approx with two segments for a mild curve
d.line([(130, 60), (110, 100)], fill=INK, width=LW)
d.line([(110, 100), (85, 145)], fill=INK, width=LW)

# Right stroke of 八 (捺: from upper-center going down-right, long)
d.line([(140, 65), (240, 150)], fill=INK, width=LW)

# Lower part 刀 (knife)
# 横折钩 stroke: horizontal top, turn to vertical/slanted down, then hook at bottom-left
# Top horizontal (short, slightly right of center)
d.line([(115, 170), (200, 170)], fill=INK, width=LW)
# Vertical/slanted drop from right end
d.line([(200, 170), (180, 260)], fill=INK, width=LW)
# Hook at bottom (small tick to the left/up)
d.line([(180, 260), (160, 250)], fill=INK, width=LW)

# 撇 stroke of 刀 — long diagonal from inside upper area down to lower-left
d.line([(150, 180), (75, 275)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_分.png")
img.save(out)
print(f"wrote {out}")
