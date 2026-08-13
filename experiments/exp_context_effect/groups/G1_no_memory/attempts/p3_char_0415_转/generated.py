"""G1 render: 转 (left 车 radical + right 专)."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

def poly(points, w=LW):
    d.line(points, fill="black", width=w, joint="curve")

# ---------- LEFT: 车 radical (simplified 4-stroke form 车) ----------
# Roughly occupies columns 40-135
# stroke 1: top horizontal (short)
line((55, 95), (125, 95))
# stroke 2: middle "口" -- a small box for 日-like center
# horizontal top and bottom + verticals of the middle rect
line((60, 125), (125, 125))
line((60, 165), (125, 165))
line((92, 125), (92, 165))
# stroke 3: long vertical spine of 车 (through the middle)
line((92, 60), (92, 235))
# stroke 4: 提 (rising stroke at the bottom, slanting up-right)
poly([(55, 220), (135, 195)])

# ---------- RIGHT: 专 (right side) ----------
# occupies columns 150-275
# 专 has strokes: horizontal top, small vertical + hook forming top square,
# long horizontal, dot at top-right, then curved hook at bottom
# Top horizontal
line((165, 90), (255, 90))
# Small dip/vertical from top horizontal down and rightward
poly([(190, 90), (190, 125), (240, 125)])
# Long horizontal (middle main stroke)
line((150, 150), (275, 150))
# Vertical going down from middle-right through
poly([(220, 90), (220, 200), (200, 215)])
# Bottom curved hook (the signature 专 curl)
poly([(160, 200), (230, 200), (250, 215), (250, 240), (235, 255), (215, 255)])
# Dot at upper right
poly([(260, 70), (270, 85)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0415_转/01_转.png")
