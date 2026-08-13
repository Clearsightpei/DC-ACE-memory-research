"""G1 draw of 乿 - left: 糸 radical, right: 乚 hook."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 4

# ============ LEFT: 糸 radical (occupies left half) ============
# Top curved stroke (丿 head)
d.line([(90, 55), (60, 90)], fill=INK, width=LW)
# Small horizontal-ish stroke at top
d.line([(60, 80), (110, 75)], fill=INK, width=LW)

# 幺 upper loop (triangular)
d.line([(65, 95), (115, 100)], fill=INK, width=LW)
d.line([(115, 100), (90, 130)], fill=INK, width=LW)
d.line([(90, 130), (60, 125)], fill=INK, width=LW)

# 幺 lower loop
d.line([(60, 140), (120, 145)], fill=INK, width=LW)
d.line([(120, 145), (90, 175)], fill=INK, width=LW)
d.line([(90, 175), (55, 170)], fill=INK, width=LW)

# 小 bottom: vertical + two side strokes
# vertical stroke (center)
d.line([(90, 180), (90, 265)], fill=INK, width=LW)
# left diagonal
d.line([(85, 195), (45, 260)], fill=INK, width=LW)
# right diagonal
d.line([(95, 195), (135, 260)], fill=INK, width=LW)

# ============ RIGHT: 乚 hook ============
# A tall vertical descending then curving right into a hook
# starts near top-right, goes down, curves right at bottom
d.line([(200, 55), (200, 240)], fill=INK, width=LW)
# curve bottom - approximate with segments
d.line([(200, 240), (210, 258)], fill=INK, width=LW)
d.line([(210, 258), (230, 268)], fill=INK, width=LW)
d.line([(230, 268), (270, 268)], fill=INK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_乿.png")
img.save(out)
print(f"Saved {out}")
