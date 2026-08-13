"""Render 这 (zhè) to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# --- 文 (upper right component) ---
# Top dot (点)
line([(175, 45), (185, 60)], width=7)

# Horizontal stroke of 文 (横)
line([(140, 85), (235, 82)], width=7)

# 撇 (left-falling) from upper-middle down-left
line([(190, 95), (150, 165)], width=7)

# 捺 (right-falling) from upper-middle down-right
line([(190, 105), (245, 175)], width=7)

# --- 辶 (walking radical, wraps under from left) ---
# Top dot of 辶 (small dot upper-left)
line([(60, 55), (75, 70)], width=7)

# Small stroke (second dot / short curve)
line([(70, 90), (95, 110)], width=7)

# Vertical-ish stroke going down (the 乛 / hook body)
line([(95, 110), (85, 145)], width=7)
line([(85, 145), (105, 170)], width=7)
line([(105, 170), (90, 200)], width=7)

# The long horizontal 平捺 sweep at bottom (curves up at end)
# Start under-left, curves under-middle then upward-right
line([(55, 230), (110, 250), (180, 258), (240, 245), (265, 225)], width=8)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_这.png"))
print("saved")
