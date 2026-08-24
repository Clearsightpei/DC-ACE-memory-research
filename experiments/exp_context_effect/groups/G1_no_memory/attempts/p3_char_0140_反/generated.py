"""Render 反 as a 300x300 PNG.

Structure from GT:
  - Long 撇 sweeping from upper-mid down to lower-left
  - Top horizontal (short 橫) sitting on top-right, above the fold
  - 橫折 (horizontal then diagonal down-left inside)
  - 捺 diagonal from center down-right
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
T = 5


def line(p1, p2, w=T):
    d.line([p1, p2], fill=BLACK, width=w)


def curve(points, w=T):
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=BLACK, width=w)


# Stroke 1: long 撇 - top starts around (130, 65), sweeps to (55, 265)
curve([(130, 65), (110, 120), (90, 170), (70, 220), (55, 265)], w=T)

# Stroke 2: short 橫 on top - the little cap above, from (155, 85) slight rise to (230, 78)
line((150, 88), (232, 75), w=T)

# Stroke 3: 橫折 - horizontal from left edge of 撇 area rightward, then curls down
# Horizontal from (115, 145) to (225, 145)
line((110, 145), (225, 145), w=T)
# Fold going down-left with slight curve to (140, 240)
curve([(225, 145), (215, 175), (195, 205), (170, 225), (140, 245)], w=T)

# Stroke 4: 捺 - diagonal from around (150, 200) sweeping down-right to (265, 270)
curve([(155, 200), (190, 230), (225, 255), (265, 272)], w=T)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0140_反/01_反.png")
print("saved")
