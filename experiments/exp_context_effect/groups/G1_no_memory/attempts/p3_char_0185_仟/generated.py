"""Render 仟 (qiān) — 亻 (person radical) + 千 (thousand) — 5 strokes total."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6


def stroke(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")


# --- Left: 亻 (person radical) ---
# Stroke 1: 撇 (piě) — slanted, slight curve, from upper-mid to bottom-left
stroke([(90, 90), (80, 125), (65, 170), (50, 210)], width=7)
# Stroke 2: 竖 (shù) — vertical descending from middle of piě
stroke([(80, 140), (82, 265)], width=7)

# --- Right: 千 (thousand) — 3 strokes ---
# Stroke 3: 撇 (short slanted top of 千, going right-to-left down)
stroke([(215, 75), (170, 115)], width=7)
# Stroke 4: 横 (horizontal) — long horizontal, slight upward tilt right
stroke([(140, 135), (260, 125)], width=7)
# Stroke 5: 竖 (long vertical through center, slight curve)
stroke([(198, 110), (195, 180), (192, 275)], width=7)

out = os.path.join(os.path.dirname(__file__), "01_仟.png")
img.save(out)
print(f"wrote {out}")
