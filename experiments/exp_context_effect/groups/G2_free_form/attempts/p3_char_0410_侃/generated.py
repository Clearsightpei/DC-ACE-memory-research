"""
Render 侃 (kan) at 300x300.

Structure: 亻 (left) + 冂-shape with 川-like inside (top-right) + 儿 (bottom-right).
The GT shows a hood/frame on top-right with inner marks, and 儿 below.

Revision notes: fixed 亻 connection point (撇 crosses 竖 near the top),
made 儿 legs actually connect to the top component, softened hook.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(pts, width=6):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=width)
    for p in pts:
        d.ellipse([p[0] - width // 2, p[1] - width // 2,
                   p[0] + width // 2, p[1] + width // 2], fill=INK)


# ----- 亻 (person radical, left side) -----
# 撇: starts high, sweeps down-left. Meeting point around (80, 115)
stroke([(95, 65), (88, 90), (78, 115), (60, 165), (42, 220)], width=6)
# 竖: from where the 撇 curves (about y=115) straight down
stroke([(80, 115), (80, 250)], width=6)

# ----- Right side top: 冂-hood with inner marks -----
# Top horizontal (long) of the hood
stroke([(130, 85), (245, 85)], width=6)
# Right vertical of the hood going down
stroke([(243, 85), (240, 175)], width=6)
# Left short vertical starting from top-horizontal going down a bit
stroke([(135, 85), (138, 110)], width=6)
# Inner horizontal (making it 冋-like)
stroke([(155, 130), (220, 130)], width=6)
# Inner short vertical (left of inner horizontal)
stroke([(158, 105), (158, 130)], width=6)
# Another inner short vertical (right of inner horizontal, forming boxes)
stroke([(200, 105), (200, 130)], width=6)

# ----- Right side bottom: 儿 -----
# 撇 (left leg): sweeps down-left from around center-right
stroke([(160, 175), (145, 215), (128, 258)], width=6)
# 竖弯钩 (right leg): vertical then curves right, then hook up-left
# vertical portion
stroke([(215, 175), (213, 225)], width=6)
# curve right (approximate with polyline)
stroke([(213, 225), (222, 245), (240, 258), (262, 258)], width=6)
# terminal hook: up-and-slightly-LEFT
stroke([(262, 258), (258, 240)], width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0410_侃/01_侃.png")
print("wrote 01_侃.png")
