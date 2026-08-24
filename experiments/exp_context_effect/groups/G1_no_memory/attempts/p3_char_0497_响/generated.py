"""Render 响 (xiang) to a 300x300 PNG.
响 = 口 (mouth radical, left) + 向 (right component: 丿 + 冂 + 口 inside).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 4  # stroke thickness

def line(p1, p2, w=T):
    d.line([p1, p2], fill=INK, width=w)

# ---------------- LEFT: 口 (mouth radical, small, mid-left) ----------------
# Position: roughly x in [40, 105], y in [130, 220]
lx1, ly1, lx2, ly2 = 40, 130, 105, 220
# stroke 1: vertical left (丨)
line((lx1, ly1), (lx1, ly2))
# stroke 2: top horizontal + right vertical (横折)
line((lx1, ly1), (lx2, ly1))
line((lx2, ly1), (lx2, ly2))
# stroke 3: bottom horizontal (一)
line((lx1, ly2), (lx2, ly2))

# ---------------- RIGHT: 向 ----------------
# Bounding: roughly x [110, 265], y [40, 260]
# Stroke 1: 丿 (left-falling stroke on top, from around (155, 45) down-left to (120, 105))
line((160, 45), (118, 110))

# Stroke 2: 竖 - left vertical of the 冂 frame, from top of frame to bottom
# Frame top around y=95, left x=125, extends down to y=255
line((125, 95), (125, 255))

# Stroke 3: 横折钩 (top horizontal + right vertical with hook)
# Top horizontal from (125, 95) to (255, 95), then down to (255, 255), then hook left
line((125, 95), (255, 95))
line((255, 95), (255, 250))
# hook (small leftward tick at the bottom)
line((255, 250), (240, 240))

# Stroke 4-6: inner 口 - inside the frame
# Position: x [155, 230], y [155, 220]
ix1, iy1, ix2, iy2 = 155, 155, 230, 220
line((ix1, iy1), (ix1, iy2))          # left vertical
line((ix1, iy1), (ix2, iy1))          # top horizontal
line((ix2, iy1), (ix2, iy2))          # right vertical
line((ix1, iy2), (ix2, iy2))          # bottom horizontal

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0497_响/01_响.png"
img.save(out)
print("Wrote", out)
