"""Render 原 (yuan) - 10 strokes. Revised."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# --- 厂 radical ---
# Top horizontal - slight downward slope
stroke([(75, 55), (250, 60)], width=5)
# Long left-falling diagonal
stroke([(82, 55), (68, 120), (50, 200), (28, 285)], width=5)

# --- 白 (inside upper) ---
# Small pie above 白
stroke([(148, 85), (135, 100)], width=4)
# Left vertical of 白
stroke([(122, 105), (122, 175)], width=4)
# Top horizontal + right vertical of 白 frame
stroke([(122, 105), (208, 105), (208, 175)], width=4)
# Middle short horizontal inside
stroke([(130, 140), (200, 140)], width=4)
# Bottom horizontal closing 白
stroke([(122, 175), (208, 175)], width=4)

# --- 小-like below inside ---
# Left slanting dot (short pie)
stroke([(120, 200), (105, 240)], width=4)
# Center vertical hook (main)
stroke([(163, 190), (163, 255), (155, 265)], width=5)
# Right slanting na
stroke([(195, 200), (240, 275)], width=4)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0515_原/01_原.png")
print("saved")
