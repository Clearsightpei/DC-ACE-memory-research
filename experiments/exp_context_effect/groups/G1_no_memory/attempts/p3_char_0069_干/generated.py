"""Render 干 as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
ink = "black"
w = 7  # stroke width

# Top horizontal (shorter), slight upward tilt right to left like the GT
d.line([(85, 95), (215, 85)], fill=ink, width=w)

# Middle horizontal (longer), slight tilt
d.line([(55, 170), (250, 160)], fill=ink, width=w)

# Vertical stroke through both horizontals, extending to bottom
d.line([(150, 90), (150, 275)], fill=ink, width=w)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0069_干/01_干.png")
