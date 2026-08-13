"""Render 兆 to a 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(points, width=7):
    d.line(points, fill="black", width=width, joint="curve")

# 兆 — 6 strokes, roughly symmetric left/right

# --- LEFT half ---
# Stroke 1: short upper-left slanted pie stroke
stroke([(90, 95), (65, 125)], width=6)

# Stroke 2: long left vertical-pie stroke, curves down-left
pts2 = [(110, 80), (105, 130), (90, 180), (65, 230), (48, 262)]
stroke(pts2, width=8)

# Stroke 3: small inner left dot (short slant down-right)
stroke([(128, 165), (150, 182)], width=6)

# --- RIGHT half ---
# Stroke 4: small inner right dot (short slant down-right)
stroke([(178, 150), (200, 168)], width=6)

# Stroke 5: right-side upper small pie stroke (short slant)
stroke([(200, 90), (180, 118)], width=6)

# Stroke 6: rightmost curved vertical with hook (竖弯钩) — main tall stroke on right
pts6 = [(225, 85), (222, 140), (222, 200), (228, 240), (245, 260), (270, 258), (278, 245)]
stroke(pts6, width=8)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_兆.png"))
print("wrote 01_兆.png")
