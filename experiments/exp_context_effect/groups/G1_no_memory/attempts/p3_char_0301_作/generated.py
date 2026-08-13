"""Render 作 to 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 6

# 作 = 亻 (left radical: person) + 乍 (right)

# --- 亻 (left radical) ---
# Short diagonal stroke (丿) top-left
d.line([(85, 65), (60, 115)], fill="black", width=LW)
# Long vertical
d.line([(85, 65), (85, 255)], fill="black", width=LW)

# --- 乍 (right side) ---
# 1) short 丿 (slant) at top
d.line([(175, 55), (140, 110)], fill="black", width=LW)
# 2) top horizontal
d.line([(140, 105), (245, 100)], fill="black", width=LW)
# 3) main vertical going down (from under top horizontal)
d.line([(178, 100), (178, 260)], fill="black", width=LW)
# 4) middle short horizontal (right side)
d.line([(178, 165), (235, 163)], fill="black", width=LW)
# 5) bottom horizontal (right side)
d.line([(178, 225), (250, 223)], fill="black", width=LW)

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_作.png")
img.save(out)
print("wrote", out)
