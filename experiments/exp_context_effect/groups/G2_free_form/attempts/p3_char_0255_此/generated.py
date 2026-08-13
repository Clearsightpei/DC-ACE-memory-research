"""此 = 止 (left) + 匕 (right)

# SIGNATURE CHECK (from sibling_signature_checklist.md — applied to 匕 as component):
# 匕: top stroke is a 撇 (upper-right→lower-left); terminal hook flicks UP-and-LEFT.
# (contrast with 七 which has a 横 on top)

Stroke plan:
 止 (left half, roughly x=50..145):
   1. 竖 — middle-vertical from top to base
   2. 短横 — short horizontal tick to the right at mid-height
   3. 短竖 — small vertical on the left, up from base
   4. 长横 — bottom horizontal (baseline)
 匕 (right half, roughly x=160..270):
   5. 撇 — top-right down to lower-left (crosses upper interior)
   6. 竖弯钩 — starts near top of 撇, goes down, curves right along base,
      terminal flicks UP-and-LEFT
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def line(p1, p2, width=LW):
    d.line([p1, p2], fill=BLACK, width=width)

def polyline(pts, width=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=BLACK, width=width)
    # smoothing dabs at joints
    for p in pts:
        d.ellipse([p[0]-width/2, p[1]-width/2, p[0]+width/2, p[1]+width/2], fill=BLACK)

# ---- 止 (left) ----
# 1. middle vertical (main vertical of 止)
line((100, 90), (100, 235), width=LW)

# 2. short horizontal tick — from middle vertical outward to the right at mid
line((100, 155), (150, 145), width=LW)

# 3. small vertical on the left, up from base (short)
line((60, 175), (60, 235), width=LW)

# 4. long bottom horizontal (baseline of 止), slight upward tilt to the right
line((45, 240), (160, 232), width=LW)

# ---- 匕 (right) ----
# 5. 撇 — from upper right down-left, slight curve
pie_pts = [(245, 85), (230, 110), (210, 135), (185, 160), (170, 175)]
polyline(pie_pts, width=LW)

# 6. 竖弯钩 — starts at top ~ where 撇 meets its top area, goes down,
#    curves right along base, hooks UP-and-LEFT at the end
shu_wan_gou = [
    (215, 110),   # start (upper) - near top of 撇
    (218, 150),
    (222, 195),
    (228, 230),   # begin curve
    (245, 250),
    (265, 255),
    (280, 250),   # rightmost bottom
]
polyline(shu_wan_gou, width=LW)
# Hook flick UP-and-LEFT — make it clearly visible
hook = [(280, 250), (275, 235), (268, 220), (260, 210)]
polyline(hook, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0255_此/01_此.png")
print("saved")
