"""Render 久 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def stroke(pts, width=5):
    draw.line(pts, fill="black", width=width, joint="curve")

# 久 — 3 strokes based on GT:
# 1) small 撇 with tiny hook at top (near upper-center)
# 2) long 横撇/横捺 — small tick right then long sweeping curve down-left
#    (this is the big left-sweeping arc that dominates the character)
# 3) 捺 — long diagonal from middle down to bottom-right

# Stroke 1: small piece at top - tiny hook shape
# GT shows a small "𠂉"-like element near top-center
s1 = [(115, 80), (130, 78), (133, 92), (122, 105)]
stroke(s1, width=4)

# Stroke 2: the long left-sweeping stroke
# starts with a short right-tick, then curves down and sweeps far to lower-left
s2 = [
    (105, 125), (125, 118), (145, 118), (160, 125),
    (150, 145), (135, 170), (115, 200), (90, 225), (65, 245), (50, 253)
]
stroke(s2, width=5)

# Stroke 3: 捺 - starts on stroke 2 around middle, sweeps down-right with widening tail
s3 = [
    (128, 170), (145, 195), (165, 220), (190, 245), (220, 265), (245, 272)
]
stroke(s3, width=5)

out_path = os.path.join(os.path.dirname(__file__), "01_久.png")
img.save(out_path)
print(f"Saved: {out_path}")
