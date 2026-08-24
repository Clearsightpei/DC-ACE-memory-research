"""G1 render of 除 (chu) - left: 阝 (left ear radical), right: 余."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ============ LEFT: 阝 (left ear ~ 3-shape) ============
# horizontal + fold-down + curve back to make a "3"-like ear
ear = [
    (55, 90), (95, 88),
    (108, 105), (100, 130), (75, 138),
    (100, 145), (112, 165), (100, 190), (60, 195),
]
stroke(ear, width=5)

# Vertical descender (竖) - long stroke going down
stroke([(75, 88), (78, 265)], width=6)

# ============ RIGHT: 余 ============
# Top: 人 (person/roof)
# left-falling (撇)
stroke([(200, 55), (150, 115)], width=6)
# right-falling (捺)
stroke([(200, 55), (260, 118)], width=6)

# First horizontal
stroke([(163, 135), (255, 132)], width=5)

# Second, shorter horizontal
stroke([(180, 165), (240, 163)], width=5)

# Central vertical (with slight hook)
stroke([(208, 135), (208, 240), (200, 250)], width=6)

# Bottom left diagonal (撇)
stroke([(208, 195), (160, 250)], width=5)

# Bottom right diagonal (捺)
stroke([(208, 195), (255, 245)], width=5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0491_除/01_除.png")
print("saved")
