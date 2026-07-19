"""G1 first render: 卜 (2 strokes)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Stroke 1: vertical (竖) — starts with a small top curve to the left, then goes straight down.
# Top of vertical at (~130, 70), bottom at (~130, 260).
# The GT shows a small leftward curl at the top.
# Draw the curl as a short arc, then the straight vertical.
# Top curl: small arc from (~135, 80) curving up-left to (~120, 65)
curl_pts = [(140, 90), (137, 80), (132, 72), (125, 68), (118, 68)]
draw.line(curl_pts, fill="black", width=6, joint="curve")

# Vertical shaft from (~140, 85) to (~140, 265)
draw.line([(140, 85), (140, 265)], fill="black", width=6)

# Stroke 2: 点 / short curved stroke — starts near vertical shaft around y=150, arcs down-right.
# In GT the dot begins closer to the shaft and ends around (215, 190). Slight downward curve.
dot_pts = [(148, 150), (165, 155), (182, 163), (200, 175), (218, 190)]
draw.line(dot_pts, fill="black", width=6, joint="curve")

out_path = os.path.join(os.path.dirname(__file__), "01_卜.png")
img.save(out_path)
print(out_path)
