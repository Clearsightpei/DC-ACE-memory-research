"""G1 render of 必. Standard stroke order:
1) 卧钩 (lying hook) — curved stroke from upper-right, arcs down-left then hooks up
2) left dot (left of hook)
3) piě (short left-falling) — center, crossing the hook
4) upper-right dot
5) lower-right dot
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

def poly(pts, width=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=INK, width=width)

# Stroke 1: 卧钩 — starts upper-middle-right, sweeps down and left in a shallow arc, then hooks up-left
hook = [
    (200, 110), (195, 135), (180, 165), (155, 195),
    (125, 220), (100, 235), (80, 240),
    (85, 225),  # hook up-left
]
poly(hook, width=7)

# Stroke 2: left dot — short diagonal down-left, on the left side
poly([(70, 140), (55, 175)], width=7)

# Stroke 3: 撇 piě — from upper middle going down-left, crossing through the hook
poly([(155, 90), (135, 130), (115, 175)], width=6)

# Stroke 4: upper-right dot — short diagonal down-right, upper right area
poly([(215, 85), (235, 115)], width=7)

# Stroke 5: right dot — short diagonal down-right, right-middle area
poly([(215, 175), (240, 205)], width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0155_必/01_必.png")
print("saved")
