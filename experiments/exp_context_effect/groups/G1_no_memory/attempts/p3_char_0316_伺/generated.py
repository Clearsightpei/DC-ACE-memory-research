"""Render 伺 (character) to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
from pathlib import Path

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)
INK = "black"

def poly(points, w=5):
    d.line(points, fill=INK, width=w, joint="curve")

def line(p1, p2, w=5):
    d.line([p1, p2], fill=INK, width=w)

# 伺 = 亻 (left person radical) + 司 (right)

# ----- 亻 radical (left) -----
# stroke 1: 撇 curving from upper area down-left
poly([(80, 55), (65, 100), (48, 155), (30, 225)], w=6)
# stroke 2: 竖 (vertical) attached near the bend of 撇
line((78, 95), (82, 265), w=6)

# ----- 司 (right) -----
# stroke 1: 横折钩 — top horizontal then right vertical with small hook at bottom
poly([(115, 60), (255, 55), (258, 245), (245, 258)], w=6)

# stroke 2: 一 (short horizontal inside, upper area)
poly([(140, 120), (240, 118)], w=5)

# stroke 3: 口 (small mouth box near bottom-left of interior)
# Left vertical
line((140, 160), (140, 230), w=5)
# Top of box
line((140, 160), (215, 160), w=5)
# Right vertical of box
line((215, 160), (215, 230), w=5)
# Bottom of box
line((140, 230), (215, 230), w=5)

out = Path(__file__).parent / "01_伺.png"
img.save(out)
print(f"Wrote {out}")
