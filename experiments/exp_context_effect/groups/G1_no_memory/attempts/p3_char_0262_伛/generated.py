"""Render 伛 (yǔ) = 亻 + 区 as 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    # simple thick polyline
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill="black")

# --- 亻 (person radical) on the left ---
# slanted stroke: top going down-left
stroke([(95, 60), (85, 90), (70, 135), (55, 180)], width=6)
# vertical stroke: from elbow area straight down
stroke([(82, 105), (85, 175), (87, 255)], width=6)

# --- 区 on the right ---
# Top horizontal (going right, slight rise)
stroke([(135, 95), (200, 88), (245, 85)], width=6)
# Right vertical (from end of top horizontal going down)
stroke([(243, 85), (240, 160), (237, 225)], width=6)

# 乂 inside (X-shape)
# 撇 from upper-right going to lower-left
stroke([(220, 115), (185, 155), (150, 200)], width=6)
# 捺 from upper-left going to lower-right
stroke([(160, 120), (200, 170), (235, 215)], width=6)

# Bottom horizontal (straight bottom extends right, closes the enclosure)
stroke([(130, 255), (200, 258), (260, 258)], width=6)

os.makedirs(os.path.dirname(__file__) or ".", exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_伛.png")
img.save(out)
print("wrote", out)
