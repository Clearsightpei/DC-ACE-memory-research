"""Render 水 (radical) to 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 5

def stroke(pts, width=LW):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=INK, width=width)
    for p in pts:
        draw.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill=INK)

# Layout: character occupies roughly y=80..250, x=60..245, centered on x=155
CX = 155

# Stroke 1: 竖钩 - central vertical, slight curve, small hook at bottom
vert = [(CX, 80), (CX, 130), (CX+2, 180), (CX+2, 225), (CX-4, 238), (CX-14, 240)]
stroke(vert)

# Stroke 2: 横撇 (upper-left component) - short horizontal top, then long diagonal down-left
# From GT: starts at roughly (110, 130), goes right briefly to about (135, 128), then sweeps down-left to (65, 205)
hp = [(112, 128), (125, 126), (135, 130), (128, 148), (110, 172), (88, 195), (68, 215)]
stroke(hp)

# Stroke 3: 撇 - short diagonal from mid-center going down-left (below the 横撇)
pie = [(148, 175), (132, 200), (115, 225)]
stroke(pie)

# Stroke 4: 捺 - long sweeping diagonal from upper center going down-right
na = [(162, 140), (180, 165), (205, 200), (232, 235)]
stroke(na)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_水.png")
img.save(out_path)
print(f"Saved {out_path}")
