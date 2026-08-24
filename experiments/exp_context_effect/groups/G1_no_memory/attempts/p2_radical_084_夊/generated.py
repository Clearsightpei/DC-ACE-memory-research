"""G1 first-render for 夊 (3-stroke radical).

Strokes (per GT):
  1. Short 撇 with tiny top hook at upper area
  2. Long 撇 sweeping down-left from top
  3. 捺 sweeping down-right then flattening into a long horizontal tail
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    # smooth polyline
    d.line(pts, fill="black", width=width, joint="curve")

# Stroke 1: short curved 撇 with tiny hook at top (top-center area)
# starts near (160, 55) small hook, curves down-left to about (135, 115)
s1 = [
    (168, 55), (172, 62), (168, 68), (160, 70),  # tiny hook
    (155, 78), (148, 90), (140, 105), (132, 118),
]
stroke(s1, width=5)

# Stroke 2: long 撇 — starts near top center-right, sweeps down-left to lower-left
s2 = [
    (175, 80), (168, 100), (155, 125), (135, 155),
    (110, 190), (85, 225), (65, 255),
]
stroke(s2, width=6)

# Stroke 3: 捺 — starts near top of stroke 2 crossing, sweeps down-right,
# then flattens into a long horizontal tail on the bottom
s3 = [
    (120, 100), (135, 125), (155, 155), (180, 190),
    (205, 220), (225, 240), (245, 250), (265, 253), (280, 253),
]
stroke(s3, width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_084_夊/01_夊.png")
print("saved")
