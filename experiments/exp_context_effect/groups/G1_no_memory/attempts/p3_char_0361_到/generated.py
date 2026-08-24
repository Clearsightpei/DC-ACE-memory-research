"""Render 到 (dao) to 300x300 PNG using PIL.
到 = 至 (left) + 刂 (right)
至 structure: top horizontal, slanted stroke down-left, small horizontal,
              then 土 at bottom (short horizontal, vertical, long horizontal)
刂 structure: short left vertical, long right vertical with hook at bottom
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 5

def line(pts):
    d.line(pts, fill="black", width=LW)

# --- 至 (left component, x roughly 30..175) ---
# 1. Top horizontal
line([(45, 75), (170, 75)])
# 2. Slanted stroke from top-right area going down-left (like 厶 opening)
line([(155, 75), (60, 145)])
# 3. Short horizontal below (middle)
line([(70, 130), (150, 130)])
# 4. 土 top short horizontal
line([(80, 175), (140, 175)])
# 5. 土 vertical (center)
line([(110, 155), (110, 220)])
# 6. 土 bottom long horizontal
line([(40, 235), (180, 235)])

# --- 刂 (right knife radical, x roughly 200..270) ---
# Left short vertical (starts a bit lower than right)
line([(210, 110), (210, 220)])
# Right long vertical, taller, ends with hook
line([(260, 60), (260, 245)])
# Hook at bottom of right vertical curves toward left
line([(260, 245), (240, 260)])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0361_到/01_到.png")
print("saved")
