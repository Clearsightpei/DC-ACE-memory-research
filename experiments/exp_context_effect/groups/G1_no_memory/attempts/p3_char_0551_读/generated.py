"""G1 render of 读 (dú) - to read."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, w=6):
    d.line(pts, fill="black", width=w, joint="curve")

# --- Left side: 讠 (speech radical, simplified) ---
# Dot at top
stroke([(55, 80), (72, 100)], w=7)
# Curved hook down (like reversed L / ㄥ)
stroke([(48, 130), (72, 150), (55, 195), (85, 225)], w=6)

# --- Right side: 卖 ---
# Top: 十 (short horizontal + short vertical)
# short horizontal
stroke([(160, 65), (240, 70)], w=6)
# short vertical through it
stroke([(200, 50), (198, 100)], w=6)

# Second horizontal (longer, under 十)
stroke([(130, 120), (270, 122)], w=6)

# Middle: 冖 (cover) - flat top with two very small hangs
stroke([(145, 150), (255, 150)], w=6)

# Bottom: 头-like element under cover
# small horizontal inside
stroke([(170, 190), (235, 190)], w=6)
# left slanting stroke (撇) from top center
stroke([(200, 165), (140, 265)], w=6)
# right slanting stroke (捺) from upper right
stroke([(215, 200), (275, 265)], w=6)
# small dot bottom-center
stroke([(195, 225), (210, 250)], w=6)

out = os.path.join(os.path.dirname(__file__), "01_读.png")
img.save(out)
print(f"wrote {out}")
