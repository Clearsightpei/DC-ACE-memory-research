"""G1 render of 斗 (radical 091, 4画)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

# Stroke 1: upper short 点 — slants from upper-right to lower-left (ノ direction)
d.line([(130, 95), (100, 120)], fill=INK, width=LW)

# Stroke 2: lower short 点 — slants same direction, below stroke 1
d.line([(135, 130), (100, 158)], fill=INK, width=LW)

# Stroke 3: long horizontal (横) across the middle, slight upward curve at ends
# approximate with a shallow polyline
d.line([(55, 190), (150, 183), (245, 188)], fill=INK, width=LW, joint="curve")

# Stroke 4: vertical (竖) — starts near top-right with a small corner (like 丁 top)
# small horizontal cap on top-left of vertical
d.line([(175, 70), (190, 70)], fill=INK, width=LW)
# vertical descending through the horizontal to bottom
d.line([(190, 70), (190, 275)], fill=INK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_斗.png")
img.save(out_path)
print(f"Saved {out_path}")
