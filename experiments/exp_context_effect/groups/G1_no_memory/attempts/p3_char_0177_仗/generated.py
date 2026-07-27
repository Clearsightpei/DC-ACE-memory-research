"""Render 仗 (character) at 300x300 using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
LW = 5

# 仗 = 亻 (person radical, left) + 丈 (right)
# Left radical 亻: short slanted stroke + long vertical
# Piě (short slant) from top down-left
d.line([(90, 80), (65, 140)], fill=BLACK, width=LW)
# Vertical (shu) - long downward
d.line([(85, 110), (85, 245)], fill=BLACK, width=LW)

# Right side 丈:
# Top horizontal (héng) - spans upper portion
d.line([(140, 110), (245, 110)], fill=BLACK, width=LW)
# Short piě crossing horizontal (from upper-right down-left through horizontal)
d.line([(210, 85), (185, 145)], fill=BLACK, width=LW)
# Long piě - main slant from upper center going far down-left
d.line([(190, 140), (130, 255)], fill=BLACK, width=LW)
# Long nà - right-falling stroke crossing piě, going down-right
d.line([(175, 150), (260, 255)], fill=BLACK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_仗.png")
img.save(out_path)
print(f"Saved {out_path}")
