"""
侌 = 今 (top) + 云 (bottom), stacked vertically.

Top 今:
  - 撇 (left diagonal from apex down-left)
  - 捺 (right diagonal from apex down-right), forming a roof/伞
  - 短横 with tiny left-flick point under the roof
  - 小勾/point strokes inside

Bottom 云:
  - 短横 (short top horizontal)
  - 长横 (longer horizontal, forms the base of the "roof under")
  - 厶 (a small triangle-ish curl under the second horizontal)

Layout: top ~y in [30, 145], bottom ~y in [155, 275].
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=6):
    """Draw a stroke as connected line segments with rounded caps."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    # round caps: draw small filled circles at each vertex
    r = width // 2
    for x, y in pts:
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# ================= TOP: 今 =================
# apex at (150, 32)
# 撇: from apex sweeping down-left, slight curve
pie_pts = [(150, 32), (128, 55), (108, 80), (92, 108), (78, 138)]
stroke(pie_pts, width=6)

# 捺: from apex sweeping down-right, slight curve, longer
na_pts = [(150, 32), (172, 55), (192, 80), (212, 105), (232, 130), (240, 138)]
stroke(na_pts, width=6)

# short 横 under the roof (a small horizontal bar with slight up angle)
# forms the "one" line of 今
heng_pts = [(110, 118), (192, 112)]
stroke(heng_pts, width=6)

# tiny dot/hook inside (the 丶 / small hook of 今)
# a short diagonal flick going down-right then a tiny hook
inner_pts = [(140, 130), (162, 148)]
stroke(inner_pts, width=6)
# terminal small hook
hook_pts = [(162, 148), (152, 148)]
stroke(hook_pts, width=6)

# ================= BOTTOM: 云 =================
# short top 横
top_heng = [(115, 168), (188, 165)]
stroke(top_heng, width=6)

# long lower 横 (base of 二)
long_heng = [(78, 210), (232, 208)]
stroke(long_heng, width=6)

# 厶 under the long heng: a small curved shape
# left flick (撇折): starts mid-left, goes down-right, turns right
sm_pie = [(135, 225), (120, 250)]
stroke(sm_pie, width=6)
# horizontal-ish turn
sm_turn = [(120, 250), (150, 258)]
stroke(sm_turn, width=6)
# small 点 on the right side
sm_dot = [(170, 240), (185, 258)]
stroke(sm_dot, width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0420_侌/01_侌.png")
