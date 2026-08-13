"""
p3_char_0340_佚 — 亻 (person radical) + 失 (lose)

Composition:
- 亻 on left: short 撇 top-right→lower-left, then 竖 from mid-stroke going straight down
- 失 on right:
  1. short 撇 top
  2. short 横 (upper)
  3. long 横 (middle, longer than upper) crossing the 撇
  4. long 撇 from top-center going down-left
  5. long 捺 from crossing going down-right, terminates lower-right with a slight flare

No hook. Not a sibling-checklist target. Compound layout: narrow-left / wider-right.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(pts, width=6):
    """Draw a smooth polyline with rounded joins."""
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=BLACK, width=width)
    for p in pts:
        draw.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill=BLACK)

# ---- 亻 (left) — occupies roughly x=45..105
# 撇: from ~(90, 55) sweeping to (55, 145)
pia_pts = [(92, 52), (85, 75), (75, 105), (62, 140), (52, 160)]
stroke(pia_pts, width=6)

# 竖: from ~(80, 100) straight down to (80, 265)
stroke([(80, 105), (80, 265)], width=7)

# ---- 失 (right) — occupies roughly x=115..280
# 1) short 撇 at top-left of 失: (170, 65) → (150, 100)
stroke([(172, 60), (160, 85), (148, 105)], width=6)

# 2) short 横 (upper): (150, 105) → (230, 108)
stroke([(148, 106), (230, 110)], width=6)

# 3) long 横 (middle, longer): (130, 145) → (260, 148)
stroke([(128, 145), (260, 150)], width=6)

# 4) long 撇 from ~(195, 90) down-left curving to (125, 275)
pie_pts = [(195, 90), (188, 130), (175, 175), (160, 220), (140, 255), (122, 278)]
stroke(pie_pts, width=6)

# 5) long 捺 from crossing (~195, 145) sweeping down-right to (275, 275)
na_pts = [(198, 148), (210, 175), (225, 205), (245, 240), (265, 265), (280, 278)]
stroke(na_pts, width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0340_佚/01_佚.png")
print("saved 01_佚.png")
