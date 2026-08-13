"""Render 经 (simplified) = 纟 + 圣, at 300x300."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5


def line(p0, p1, w=LW):
    draw.line([p0, p1], fill=BLACK, width=w)


def curve(points, w=LW):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=BLACK, width=w)


# ============ Left radical: 纟 (silk radical, simplified) ============
# First fold (撇折) - top
curve([(75, 90), (60, 108), (58, 115), (82, 125)])
# Second fold (撇折) - middle
curve([(85, 138), (68, 155), (66, 162), (92, 172)])
# Bottom rising stroke (提)
line((55, 220), (105, 205))

# ============ Right side: 圣 (又 on top of 工/土) ============
# --- Top: 又-like shape (in simplified 圣) ---
# The top of 圣 is a 又 shape: one horizontal-curved stroke and a diagonal
# Horizontal-ish stroke on top (like 横撇)
curve([(140, 100), (215, 95), (225, 100), (210, 120)])
# Diagonal stroke (捺) crossing down-right
curve([(175, 115), (200, 145), (240, 170), (260, 175)])
# The left descending curve of 又
curve([(175, 115), (155, 155), (140, 195)])

# --- Bottom: 工 (or 土) ---
# Top short horizontal of 工
line((160, 205), (235, 208))
# Vertical
line((197, 208), (197, 260))
# Bottom long horizontal (extends across whole character width)
line((115, 262), (270, 262))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0375_经/01_经.png")
print("saved")
