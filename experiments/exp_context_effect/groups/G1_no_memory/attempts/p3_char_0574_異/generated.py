"""G1 render of 異 (different) — PIL-based."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=4):
    d.line(pts, fill="black", width=w, joint="curve")

# --- Top: 田 (rectangle with cross) ---
# Rectangle: roughly x 90-210, y 45-135
left, right, top, bot = 90, 210, 45, 135
# Top horizontal
line([(left, top), (right, top)], 5)
# Left vertical (slight bow)
line([(left, top), (left-2, bot)], 5)
# Right vertical (comes down from top-right corner)
line([(right, top), (right+2, bot+3)], 5)
# Bottom horizontal
line([(left-2, bot), (right+2, bot)], 5)
# Middle horizontal
midy = (top + bot) // 2 + 2
line([(left, midy), (right, midy)], 4)
# Middle vertical
midx = (left + right) // 2
line([(midx, top), (midx, bot)], 4)

# --- Middle: connecting horizontal(s) / short strokes forming 共-like middle ---
# Two small vertical strokes below 田 (like legs of 共 upper)
line([(120, bot+2), (118, 165)], 4)
line([(180, bot+2), (182, 165)], 4)

# --- Long horizontal across (bottom cross-bar of 共) ---
line([(55, 195), (250, 190)], 5)

# --- Bottom: two splayed legs (八-like) ---
# Left leg
line([(115, 200), (75, 265)], 5)
# Right leg
line([(180, 200), (230, 265)], 5)

out = os.path.join(os.path.dirname(__file__), "01_異.png")
img.save(out)
print("wrote", out)
