"""G1 render for 在 (p3_char_0219). PIL, 300x300."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 5  # stroke width

# 在: 6 strokes
# Order: 1) short horizontal top (heng)
#        2) long left-falling pie (from top-right area sweeping down-left)
#        3) horizontal in middle (heng)
#        4) vertical dropping down from middle heng (shu)
#        5) short horizontal inside (top of 土 lower box)
#        6) long horizontal bottom (bottom of 土)

# Stroke 1: short heng at top (upper right area)
d.line([(120, 70), (200, 65)], fill="black", width=W)

# Stroke 2: long pie sweeping from top-right down to bottom-left
d.line([(175, 55), (75, 255)], fill="black", width=W)

# Stroke 3: horizontal heng crossing middle
d.line([(105, 145), (230, 140)], fill="black", width=W)

# Stroke 4: vertical shu from middle heng going down
d.line([(165, 130), (160, 250)], fill="black", width=W)

# Stroke 5: short inner heng (lower-middle, inside)
d.line([(130, 200), (215, 198)], fill="black", width=W)

# Stroke 6: long bottom heng
d.line([(105, 255), (250, 250)], fill="black", width=W)

out = os.path.join(os.path.dirname(__file__), "01_在.png")
img.save(out)
print("wrote", out)
