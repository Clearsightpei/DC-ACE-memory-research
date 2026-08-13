"""Render 並 (p3_char_0360) at 300x300 with PIL.

Structure (top-to-bottom):
- 丷: two short dots (left leans right, right leans left)
- 一: short upper horizontal
- 丷 lower dots-and-flicks: two more dots (small 丿 left, 丶 right)
- 丨 丨: two verticals descending to base
- 一: long lower horizontal (widest stroke)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)

def line(p1, p2, width=6):
    d.line([p1, p2], fill=INK, width=width)

def dot(p1, p2, width=7):
    d.line([p1, p2], fill=INK, width=width)

# Top 丷 (two dots)
line((110, 60), (100, 85), width=7)   # left dot, slanting down-left
line((190, 60), (200, 85), width=7)   # right dot, slanting down-right

# Upper horizontal (short, slightly slanting up-right)
line((85, 115), (215, 108), width=6)

# Middle two dots/flicks (flanking outward of verticals)
line((100, 135), (85, 175), width=6)   # left outer flick (丿 style)
line((215, 135), (230, 175), width=6)  # right outer flick (丶 style)

# Two verticals descending to bottom base
line((130, 125), (133, 240), width=7)  # left vertical
line((180, 125), (188, 240), width=7)  # right vertical

# Long lower horizontal (base)
line((45, 245), (270, 250), width=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0360_並/01_並.png")
