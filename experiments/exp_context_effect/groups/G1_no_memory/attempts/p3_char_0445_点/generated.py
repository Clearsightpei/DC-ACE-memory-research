"""Render 点 (dian) to a 300x300 PNG, white bg, black ink.

Structure:
- Top: 占 component (upper: 卜 = short vertical + dot; lower: 口 = small mouth)
- Bottom: 灬 (four dots / fire radical) as four small strokes at base
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5  # main stroke width


def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)


def dot_stroke(p1, p2, w=6):
    # short diagonal "dot" stroke
    d.line([p1, p2], fill=BLACK, width=w)


# ---------- 占 upper: 卜 ----------
# Vertical descender (short, slightly leaning)
line((140, 60), (138, 130), w=LW)
# Small tick at top of vertical (short diagonal going down-right)
line((140, 60), (150, 72), w=LW)
# Horizontal dot / stroke to the right of vertical
line((150, 100), (185, 95), w=LW)

# ---------- 占 lower: 口 (mouth box) ----------
# left vertical
line((110, 130), (110, 175), w=LW)
# top horizontal
line((110, 130), (180, 130), w=LW)
# right vertical
line((180, 130), (180, 175), w=LW)
# bottom horizontal
line((110, 175), (180, 175), w=LW)

# ---------- 灬 four dots at the bottom ----------
# leftmost dot: leans left
dot_stroke((80, 215), (68, 250), w=6)
# second dot: nearly vertical / slight lean
dot_stroke((115, 220), (110, 255), w=6)
# third dot: slight lean right
dot_stroke((155, 220), (160, 255), w=6)
# rightmost dot: leans right
dot_stroke((195, 215), (215, 250), w=6)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p3_char_0445_点/01_点.png"
)
print("saved 01_点.png")
