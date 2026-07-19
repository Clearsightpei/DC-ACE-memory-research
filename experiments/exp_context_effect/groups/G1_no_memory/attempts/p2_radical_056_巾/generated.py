"""G1 render for 巾 (radical, 3 strokes).

Structure (from GT observation):
  Stroke 1: 丿 - short left slant descending, left side of frame
  Stroke 2: 𠃍 - horizontal top with right vertical (top-right corner box)
  Stroke 3: 丨 - long central vertical descending well below the box
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_巾.png")

img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

INK = "black"
W = 6  # stroke width

def line(pts, width=W):
    d.line(pts, fill=INK, width=width, joint="curve")

# Layout: box top ~ y=95, box bottom ~ y=195
# Central vertical: x=150, extends from ~y=85 (top hook nub) to y=270

# --- Stroke 2 (draw first as backbone): top horizontal + right vertical (𠃍) ---
# Small nub going up-left at start (top of horizontal)
# Then horizontal from x=95 to x=205
# Then vertical down from (205, 95) to (200, 200)  (slight taper inward)
# top nub
line([(112, 78), (110, 88)], width=W)
# horizontal top
line([(110, 88), (200, 92)], width=W)
# right vertical with hook inward at bottom
line([(200, 92), (198, 150), (188, 195), (178, 200)], width=W)

# --- Stroke 1: 丿 left descending curve ---
# Starts at top-left corner of box, curves down-left, long
line([(112, 92), (105, 140), (92, 200), (82, 255)], width=W)

# --- Stroke 3: 丨 central long vertical ---
# From just above top horizontal down past bottom
line([(150, 70), (150, 280)], width=W)

img.save(OUT)
print(f"wrote {OUT}")
