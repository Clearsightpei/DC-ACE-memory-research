"""G1 render for 仲 (p3_char_0242) — no memory, cold render."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
ink = "black"
lw = 5

# 仲 = 亻 (left) + 中 (right)
# Left radical 亻 (person)
# Stroke 1: 撇 - slanting from upper-right area down-left, gentle curve
d.line([(95, 75), (55, 210)], fill=ink, width=lw)
# Stroke 2: 竖 - vertical starting where 撇 passes through, going down
d.line([(80, 145), (80, 265)], fill=ink, width=lw)

# Right side 中 - compact box with long central vertical
# Box top-left ~ (145, 110), bottom-right ~ (225, 200)
# Stroke 1: 竖 (left side of box)
d.line([(148, 110), (148, 200)], fill=ink, width=lw)
# Stroke 2: 横折 (top + right side of box)
d.line([(148, 110), (228, 110)], fill=ink, width=lw)
d.line([(228, 110), (228, 200)], fill=ink, width=lw)
# Stroke 3: 横 (bottom of box)
d.line([(148, 200), (228, 200)], fill=ink, width=lw)
# Stroke 4: 竖 (long central vertical through the box)
d.line([(188, 65), (188, 260)], fill=ink, width=lw)

out = os.path.join(os.path.dirname(__file__), "01_仲.png")
img.save(out)
print(f"wrote {out}")
