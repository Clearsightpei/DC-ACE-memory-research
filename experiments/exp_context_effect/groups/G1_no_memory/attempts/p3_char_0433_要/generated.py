"""Render 要 (yao) - 9 strokes.
Top: 西-like radical  |  Bottom: 女 (woman)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=3):
    d.line(pts, fill="black", width=width)

# ===== TOP: 西 component =====
# Top horizontal
line([(95, 55), (210, 55)], 3)
# Left vertical (slight lean out)
line([(95, 55), (88, 145)], 3)
# Right vertical (slight lean out)
line([(210, 55), (220, 148)], 3)
# Inner-left vertical (reaches from top down to bottom of box)
line([(130, 60), (128, 145)], 3)
# Inner-right vertical
line([(180, 60), (183, 145)], 3)
# Bottom horizontal (closing the box, slight downward curve)
line([(85, 148), (222, 150)], 3)

# ===== Long horizontal separator (top of 女) =====
line([(45, 185), (258, 182)], 3)

# ===== BOTTOM: 女 (woman) =====
# Left-falling diagonal (撇)
line([(155, 178), (70, 285)], 3)
# Right-falling diagonal (捺)
line([(148, 195), (250, 285)], 3)
# Small horizontal cross through middle of 女
line([(105, 235), (225, 232)], 3)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0433_要/01_要.png")
print("saved")
