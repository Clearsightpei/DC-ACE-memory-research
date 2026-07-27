"""Render 仄 to 01_仄.png at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 5

def curve(pts, width=LW):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=INK, width=width)
    for p in pts:
        r = width / 2
        draw.ellipse((p[0]-r, p[1]-r, p[0]+r, p[1]+r), fill=INK)

# 仄 = 厂 (top horizontal + long left-falling 撇) + 人 (short 撇 + 捺) inside

# Stroke 1: top 横 — spans most of upper area
curve([(85, 90), (230, 85)], width=6)

# Stroke 2: long 撇 — from top-left corner curving down-left to bottom-left
curve([(90, 90), (78, 130), (65, 175), (48, 220), (30, 260)], width=6)

# Inner 人 — centered horizontally, sits below the horizontal

# Stroke 3: short 撇 of 人 (from apex going down-left)
curve([(140, 140), (125, 175), (110, 215), (95, 250)], width=6)

# Stroke 4: 捺 of 人 (from apex going down-right, sweeping)
curve([(140, 145), (165, 185), (200, 225), (240, 260)], width=6)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_仄.png")
img.save(out_path)
print(f"Saved {out_path}")
