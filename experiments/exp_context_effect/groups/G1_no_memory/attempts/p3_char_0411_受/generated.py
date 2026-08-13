"""Render 受 to 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 5

def line(pts, w=LW):
    d.line(pts, fill="black", width=w, joint="curve")

# 受: top 爫 (claw) + middle 冖 (cover) + bottom 又
# --- Top 爫: three short strokes + horizontal
line([(100, 55), (92, 78)])       # left short slant
line([(130, 52), (125, 76)])      # middle short slant
line([(160, 55), (155, 78)])      # right short slant
line([(85, 85), (200, 82)])       # horizontal bar of claw

# --- Middle 冖 (cover) — horizontal with small left-drop and right end drop
line([(75, 110), (85, 128)])      # left short drop (dot into vertical)
line([(80, 122), (220, 118)])     # main cover horizontal
line([(220, 118), (212, 140)])    # right end short drop

# small interior marks (inside cover, above 又)
line([(120, 140), (135, 165)])
line([(175, 140), (165, 165)])

# --- Bottom 又
# 撇 (long left-falling curve from upper middle down to lower-left)
line([(115, 165), (105, 195), (95, 220), (80, 250)])
# 捺 (right-falling from crossing point going down-right)
line([(115, 180), (155, 225), (200, 255), (230, 265)])

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_受.png"))
print("saved")
