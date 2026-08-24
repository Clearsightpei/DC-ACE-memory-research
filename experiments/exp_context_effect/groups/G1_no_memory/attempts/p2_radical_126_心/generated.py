"""Render 心 (radical) to a 300x300 PNG using PIL.

Strokes (per GT):
  1. 左点 (left dot) — short down-slanted mark, lower-left.
  2. 卧钩 (lying hook) — deep bowl curving from upper-left down and
     back up to upper-right, ending in an up-left hook.
  3. 中点 (middle dot) — short slanted mark inside/above the bowl.
  4. 右点 (right dot) — short slanted mark upper-right.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"


def stroke(pts, width=7):
    draw.line(pts, fill=INK, width=width, joint="curve")
    r = width / 2
    for (x, y) in (pts[0], pts[-1]):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# ---- Stroke 1: 左点 — short slanted mark on the left side ----
stroke([(70, 165), (90, 210)], width=7)

# ---- Stroke 2: 卧钩 (lying hook) — deeper bowl ----
# Starts upper-left area, curves down through the bottom, comes back up
# on the right side to about mid-height, then a small up-left hook.
bowl = [
    (100, 195),
    (110, 225),
    (135, 250),
    (170, 258),
    (200, 250),
    (222, 230),
    (232, 205),
]
stroke(bowl, width=8)
# Hook at the tail of the 卧钩 — points up-left
stroke([(232, 205), (215, 195)], width=7)

# ---- Stroke 3: 中点 — small slanted mark above the middle of the bowl ----
stroke([(160, 175), (172, 205)], width=7)

# ---- Stroke 4: 右点 — small slanted mark to the upper right ----
stroke([(210, 155), (232, 178)], width=7)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p2_radical_126_心/01_心.png"
)
print("saved")
