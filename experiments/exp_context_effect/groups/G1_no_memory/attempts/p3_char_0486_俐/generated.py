"""G1 render of 俐 (亻 + 利). Revision 2."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 5

def poly(pts, w=LW):
    d.line(pts, fill=INK, width=w, joint="curve")

def line(p0, p1, w=LW):
    d.line([p0, p1], fill=INK, width=w)

# =========================================================
# LEFT: 亻 (person radical) — x ~ 40..95
# =========================================================
# 撇: from upper-right sweeping down-left
poly([(88, 70), (75, 105), (60, 155), (45, 215)], w=LW)
# 竖: vertical, starting from about mid of 撇, going down
line((78, 130), (78, 265))

# =========================================================
# RIGHT: 利 = 禾 + 刂
# 禾 center around x=170; 刂 around x=245
# =========================================================

# 禾 top 撇 (small slanted stroke above the horizontal)
poly([(170, 55), (160, 68), (148, 78)], w=LW)

# 禾 horizontal 一 (below the top 撇)
line((125, 100), (215, 95))

# 禾 vertical 竖 (center, down)
line((170, 95), (170, 250))

# 禾 撇 (from center down-left)
poly([(170, 135), (150, 170), (125, 210)], w=LW)

# 禾 捺 (from center down-right)
poly([(170, 135), (192, 170), (218, 210)], w=LW)

# =========================================================
# 刂 (knife) — short left vert + long right vert with hook
# =========================================================
# Short left vertical (short 竖)
line((235, 105), (235, 180))

# Long right vertical with hook (竖钩)
poly([(262, 75), (262, 250), (250, 258)], w=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0486_俐/01_俐.png")
