"""
p3_char_0099_予  — 4 strokes:
  1) 横撇 (top): horizontal into a down-left diagonal
  2) 横撇 (middle, smaller, tucked inside upper fold)
  3) 撇 (curved diagonal going down-left, starting from lower-right area)
  4) 竖钩 (vertical stroke through center from ~middle fold down, hook at bottom-left)

Revision notes vs pass 1:
- narrowed the top 横 (was too wide)
- middle 横撇 shortened and nested inside stroke 1's diagonal
- 撇 (stroke 3) starts from the upper-right of the middle fold, not from far right
- 竖钩 starts lower (from the middle intersection), extends further down with a clearer hook
"""
from PIL import Image, ImageDraw
from math import comb

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=6):
    d.line(points, fill=BLACK, width=width, joint="curve")
    r = width // 2
    for (x, y) in (points[0], points[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def curve(points, width=6, samples=40):
    n = len(points) - 1
    pts = []
    for i in range(samples + 1):
        t = i / samples
        x = sum(comb(n, k) * (1 - t) ** (n - k) * t ** k * p[0] for k, p in enumerate(points))
        y = sum(comb(n, k) * (1 - t) ** (n - k) * t ** k * p[1] for k, p in enumerate(points))
        pts.append((x, y))
    stroke(pts, width=width)


# Stroke 1: 横撇 top — horizontal, then diagonal down-left
stroke([(115, 78), (195, 76)], width=6)
curve([(195, 76), (185, 100), (155, 118)], width=6)

# Stroke 2: 横撇 middle — smaller inner fold, nested under stroke 1
stroke([(120, 130), (180, 128)], width=6)
curve([(180, 128), (170, 145), (150, 158)], width=6)

# Stroke 3: 撇 — long curved diagonal, starts from the right side of middle fold, sweeps down-left
curve([(200, 135), (160, 200), (85, 250)], width=6)

# Stroke 4: 竖钩 — vertical from the middle-fold intersection, down through body, hook left at bottom
stroke([(155, 128), (152, 245)], width=7)
curve([(152, 245), (140, 252), (120, 248)], width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0099_予/01_予.png")
print("saved")
