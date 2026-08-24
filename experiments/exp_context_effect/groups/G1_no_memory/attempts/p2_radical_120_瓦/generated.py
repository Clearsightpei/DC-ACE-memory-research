"""Render 瓦 (4画 radical) to 300x300 PNG using PIL.

Structure (per GT):
  1) top 横 (horizontal), slight arc
  2) short 丿 diagonal coming down-left from the top-left of stroke 1
  3) short middle horizontal-ish stroke (interior)
  4) large 横折弯钩 (open sweep) — comes from top-right, angles down
     and curves around the bottom, ending in a small hook
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

def curve(points, w=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=BLACK, width=w)

# Stroke 1: top horizontal — slight downward arc from left to right
s1 = [(75, 100), (115, 96), (155, 94), (195, 95), (220, 98)]
curve(s1)

# Stroke 2: short 丿 diagonal starting a bit right of stroke 1's left end,
# going down-left. Ends around (75, 165).
s2 = [(110, 95), (100, 115), (90, 135), (80, 155), (72, 175)]
curve(s2)

# Stroke 3: short interior stroke — small horizontal near middle
s3 = [(110, 170), (140, 168), (165, 170)]
curve(s3)

# Stroke 4: big 横折弯钩 open sweep
# starts at top-right area (roughly continuing from stroke 1's right end),
# goes down as vertical/slight-right, then curves left across the bottom,
# ends in a small upward hook on the left side.
s4 = [
    (215, 105),   # top (near right end of stroke 1)
    (222, 135),
    (225, 165),
    (222, 195),
    (212, 220),
    (195, 240),
    (170, 252),
    (140, 258),
    (115, 258),
    (95, 252),
    (85, 242),
]
curve(s4)
# hook upward at end
d.line([(85, 242), (100, 225)], fill=BLACK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_120_瓦/01_瓦.png")
print("saved")
