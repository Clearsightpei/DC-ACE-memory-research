"""G1 render for 疝 = 疒 (illness radical) + 山 (mountain) inside."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- 疒 radical (outer) ----
# 1. Top dot (short slanted stroke, top-center-ish)
stroke([(110, 40), (135, 60)], width=6)

# 2. Top horizontal stroke of 疒 (long, slight upward slope)
stroke([(85, 85), (240, 75)], width=6)
# small tick down at right end of horizontal
stroke([(240, 75), (250, 100)], width=6)

# 3. Second small slanted stroke (left dot below horizontal)
stroke([(70, 115), (95, 135)], width=6)

# 4. Long curved stroke going down-left (main 撇 of 疒)
stroke([(115, 90), (100, 170), (55, 265)], width=6)

# ---- 山 (mountain) inside, bottom-right area ----
# Middle tall vertical (center peak) - drawn first, tallest
stroke([(170, 155), (170, 260)], width=6)
# Left vertical of 山 (shorter)
stroke([(115, 185), (115, 260)], width=6)
# Bottom horizontal
stroke([(115, 260), (230, 258)], width=6)
# Right vertical (shorter)
stroke([(230, 185), (230, 258)], width=6)

out = os.path.join(os.path.dirname(__file__), "01_疝.png")
img.save(out)
print(f"saved {out}")
