"""Render 桃 to a 300x300 PNG.
桃 = 木 (left) + 兆 (right).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

LW = 5


def line(x1, y1, x2, y2, w=LW):
    draw.line([(x1, y1), (x2, y2)], fill="black", width=w)


def curve(points, w=LW):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill="black", width=w)


# ---- Left: 木 (tree radical) ----
# horizontal
line(25, 115, 135, 115)
# vertical
line(80, 75, 80, 255)
# left piě
curve([(80, 130), (65, 160), (48, 195), (28, 235)])
# right nà (diǎn) - shorter for radical form
curve([(80, 130), (100, 155), (118, 180), (130, 205)])

# ---- Right: 兆 ----
# Stroke 1: short piě upper-left
curve([(178, 90), (168, 110), (160, 130)])

# Stroke 2: vertical-ish piě going down then curving/hooking left (shu-wan-gou-like)
curve([(190, 85), (188, 120), (185, 155), (182, 190), (178, 220), (168, 245)])

# Stroke 3: small diǎn to the right of stroke1 (upper middle area)
curve([(200, 130), (212, 140), (218, 150)])

# Stroke 4: small diǎn lower-middle
curve([(200, 195), (212, 208), (220, 218)])

# Stroke 5: top short stroke on right (small piě/dot)
curve([(240, 90), (232, 105), (228, 118)])

# Stroke 6: long right stroke - starts high, goes down and hooks up-right at bottom
curve([(250, 100), (245, 135), (242, 170), (240, 205), (245, 230), (260, 245), (278, 240)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0565_桃/01_桃.png")
