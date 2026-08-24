"""
p3_char_0262 伛 (yǔ)
Structure: 亻 (left, person radical) + 区 (right, three-sided box with 乂)
Strokes:
  亻: 1) 撇 (down-left flick), 2) 竖 (long vertical)
  区: 3) 一 (top horizontal), 4) 丿 (left of X), 5) 乀 (right of X, angled),
      6) 乚 竖折 (vertical then bottom horizontal, forming left+bottom of frame)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush(pts, width=6):
    # Draw a slightly tapered stroke by dabbing along polyline
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    for x, y in pts:
        d.ellipse((x - width/2, y - width/2, x + width/2, y + width/2), fill="black")

# --- 亻 (left radical) ---
# 1) 撇: from about (100, 70) down-left to (55, 165)
brush([(100, 65), (90, 100), (75, 135), (58, 170)], width=6)

# 2) 竖: from around (95, 100) straight down to (95, 275)
brush([(95, 100), (95, 275)], width=7)

# --- 区 (right side) ---
# The right side occupies roughly x=125..270, y=75..255

# 3) 一: top horizontal — from (140, 100) to (265, 100)
brush([(140, 100), (265, 100)], width=6)

# Inside 乂 (X):
# 4) 丿: from top-right area (215, 120) down-left to (155, 210)
brush([(215, 120), (195, 150), (175, 180), (155, 210)], width=6)

# 5) 乀 / right diagonal of 乂: from (170, 130) down-right to (240, 210), slight arc
brush([(170, 130), (190, 155), (215, 185), (240, 215)], width=6)

# 6) 竖折 乚: vertical from (140, 100) down to (140, 250), then horizontal to (270, 250)
brush([(140, 100), (140, 175), (140, 250), (200, 250), (270, 250)], width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0262_伛/01_伛.png")
print("saved")
