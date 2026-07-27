"""Render 文 as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
STROKE = 6

# Stroke 1: dot (点) at top-center — small diagonal tick
draw.line([(135, 40), (160, 65)], fill=INK, width=STROKE)

# Stroke 2: horizontal (横) — slightly tilted, spanning wide
draw.line([(55, 115), (245, 100)], fill=INK, width=STROKE)

# Stroke 3: left-falling (丿) — from center-right of horizontal, sweeping down-left with slight curve
# Approximate curve with a polyline
pts_pie = [(170, 130), (150, 165), (125, 200), (95, 240), (75, 265)]
draw.line(pts_pie, fill=INK, width=STROKE, joint="curve")

# Stroke 4: right-falling (捺) — from center-left of horizontal, crossing 丿 near middle
# Approximate with slight curve
pts_na = [(130, 145), (155, 180), (190, 220), (230, 250), (255, 265)]
draw.line(pts_na, fill=INK, width=STROKE, joint="curve")

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_文.png")
img.save(out_path)
print(f"Saved: {out_path}")
