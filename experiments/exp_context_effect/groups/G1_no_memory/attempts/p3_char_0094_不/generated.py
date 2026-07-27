"""Render 不 (character) to 01_不.png at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

def stroke(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

# Stroke 1: top horizontal (long, slight upward taper toward right)
# Runs roughly from x=45 to x=255 near y=90
stroke([(45, 100), (110, 88), (190, 85), (255, 95)], width=7)

# Stroke 2: left-falling 撇 - starts near center-top, sweeps to lower-left
stroke([(150, 100), (130, 145), (95, 200), (55, 255)], width=6)

# Stroke 3: central vertical (short) - starts at intersection, goes straight down
stroke([(155, 130), (155, 200), (155, 265)], width=7)

# Stroke 4: right dot / short falling stroke (点) on the right
stroke([(185, 155), (210, 200), (235, 245)], width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_不.png")
img.save(out_path)
print(f"Saved: {out_path}")
