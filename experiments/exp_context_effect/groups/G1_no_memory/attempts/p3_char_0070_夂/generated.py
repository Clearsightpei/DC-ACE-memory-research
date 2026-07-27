"""G1 render of 夂 (p3_char_0070_夂)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# Stroke 1: short 撇 at top — small diagonal from upper-mid down-left
d.line([(155, 80), (148, 95), (135, 110)], fill="black", width=4)

# Stroke 2: 横撇 — horizontal from left, then long diagonal down-left
# horizontal segment
d.line([(105, 125), (135, 122), (170, 120), (195, 122)], fill="black", width=4)
# diagonal from the horizontal's right end sweeping down-left
d.line([(195, 122), (170, 150), (135, 185), (100, 215), (75, 230)], fill="black", width=4)

# Stroke 3: 捺 — long diagonal from mid-upper down to lower-right
d.line([(140, 150), (170, 175), (205, 205), (235, 225), (255, 235)], fill="black", width=4)

out = os.path.join(os.path.dirname(__file__), "01_夂.png")
img.save(out)
print("Saved", out)
