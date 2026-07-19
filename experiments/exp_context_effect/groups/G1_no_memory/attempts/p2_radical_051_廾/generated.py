"""Render 廾 (3-stroke radical) as 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
TH = 5

# 廾 has 3 strokes (stroke order: left slant, horizontal, right vertical):
# GT observation:
# - horizontal is fairly low (~y=200), extending across most of width
# - left stroke is a downward curve, starting upper-left area (~x=95, y=140),
#   curving down and to the left, ending around (60, 240) — like 丿
# - right stroke starts upper-right (~x=205, y=140) and goes straight down
#   ending around (215, 260), slight lean

# --- Stroke 1: left slanting curved stroke (丿-like) ---
pts1 = [(105, 130), (100, 165), (90, 200), (75, 230), (60, 250)]
draw.line(pts1, fill=INK, width=TH, joint="curve")

# --- Stroke 2: horizontal stroke, slight upward tilt to the right ---
pts2 = [(50, 205), (150, 198), (250, 190)]
draw.line(pts2, fill=INK, width=TH, joint="curve")

# --- Stroke 3: right vertical stroke, slight lean ---
pts3 = [(200, 135), (207, 190), (213, 255)]
draw.line(pts3, fill=INK, width=TH, joint="curve")

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_廾.png")
img.save(out_path)
print(f"Saved: {out_path}")
