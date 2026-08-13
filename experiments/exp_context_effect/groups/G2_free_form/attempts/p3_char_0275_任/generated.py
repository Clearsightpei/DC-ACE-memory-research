"""
任 = 亻 (person radical, left) + 壬 (right)
Stroke count: 6 total
  Left 亻 (2 strokes): 撇 (top-left slanting), 竖 (vertical)
  Right 壬 (4 strokes): 撇 (top, short slant), 横 (short middle), 竖 (through), 横 (long bottom)

SIGNATURE CHECK (per sibling checklist):
  Right component is 壬 not 王/士:
  - top stroke is a 撇 (slanting), not a flat 横
  - two 横 strokes in body (middle short, bottom LONG — bottom is the character's base)
  - 壬's top 撇 slants down-right (like 千's top)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(pts, width=8):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    for p in pts:
        d.ellipse([p[0] - width // 2, p[1] - width // 2,
                   p[0] + width // 2, p[1] + width // 2], fill=BLACK)

# ------------ LEFT: 亻 ------------
# 撇 (long diagonal from upper area down-left)
pie_pts = [(95, 70), (88, 100), (78, 140), (62, 195)]
stroke(pie_pts, width=8)

# 竖 (from mid of 撇 down)
shu_pts = [(88, 115), (90, 175), (92, 235)]
stroke(shu_pts, width=8)

# ------------ RIGHT: 壬 ------------
# top 撇 (short slanting stroke, upper region of 壬)
top_pie = [(155, 78), (175, 90), (215, 100)]
# rendered as short slanted line going right-down slightly then flattening
top_pie = [(160, 75), (185, 85), (220, 100)]
stroke(top_pie, width=8)

# middle 横 (short horizontal, sitting inside 壬)
mid_heng = [(170, 135), (235, 130)]
stroke(mid_heng, width=8)

# 竖 (vertical through middle)
shu2 = [(195, 100), (195, 235)]
stroke(shu2, width=8)

# bottom 横 (LONG horizontal - the base)
bot_heng = [(140, 235), (270, 232)]
stroke(bot_heng, width=9)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0275_任/01_任.png")
print("saved")
