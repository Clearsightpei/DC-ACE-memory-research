"""G1 render for 声 (shēng)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def line(pts, w=LW):
    d.line(pts, fill=BLACK, width=w, joint="curve")

# 声 = 士 (top) over 尸-like base
# Stroke 1: top short horizontal (士 top)
line([(115, 60), (200, 55)], LW)

# Stroke 2: vertical connecting top horiz to middle horiz
line([(160, 55), (160, 115)], LW)

# Stroke 3: wide horizontal (base of 士 / top of 尸 upper)
line([(85, 115), (240, 108)], LW)

# Stroke 4: long left slash — starts at top of wide horiz on left, sweeps down and curves left at bottom
# This is the 丿 spanning most of the character height
line([(95, 115), (85, 200), (75, 250), (55, 270)], LW)

# Stroke 5: right vertical hook coming down from wide horiz right area — short vertical
line([(215, 115), (218, 175)], LW)

# Stroke 6: middle horizontal inside 尸 (between the two horizontals)
line([(95, 175), (218, 172)], LW)

# Stroke 7: bottom horizontal (base of 尸)
line([(85, 235), (230, 228)], LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_声.png"))
print("saved")
