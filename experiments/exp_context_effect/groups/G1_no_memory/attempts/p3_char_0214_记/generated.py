"""Render 记 (jì) — 讠 radical (left) + 己 (right)."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 5


def stroke(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")


# ---------- Left: 讠 (simplified speech radical) ----------
# 1) Top dot — short diagonal tick, upper-left
stroke([(75, 75), (95, 95)], width=6)

# 2) Horizontal-fold-tick (橫折提): short horizontal, turn down-left, then tick up-right
#    This is the characteristic "z-like" middle stroke of 讠
stroke([(60, 135), (110, 135), (70, 175), (115, 175)], width=LW)

# 3) Bottom curved descender ending in a small upward hook
stroke([(95, 200), (85, 245), (130, 260)], width=LW)

# ---------- Right: 己 ----------
# Stroke 1 (橫折): horizontal top then turn down (top edge + right side upper)
stroke([(155, 100), (245, 100), (245, 165)], width=LW)

# Stroke 2 (橫): middle horizontal
stroke([(155, 165), (230, 165)], width=LW)

# Stroke 3 (竖弯钩): left vertical down, across bottom, then up-hook on right
stroke([(155, 100), (155, 250), (250, 250), (250, 220)], width=LW)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p3_char_0214_记/01_记.png"
)
