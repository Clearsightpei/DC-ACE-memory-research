"""G1 render of 癸 (gui). PIL-based, 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(pts, w=LW):
    d.line(pts, fill="black", width=w)

# 癸 has 9 strokes. Top: 癶 (two symmetric feet-like radicals).
# Bottom: 天-like (一 + 人 with extra dot? actually 矢-like or 天).
# Reference GT: top is 癶, bottom is 天.

# ---- TOP: 癶 (two mirrored parts) ----
# Left side of 癶: a short right-slanting stroke + a long left-falling curve
# Right side of 癶: a short left-slanting stroke + a long right-falling
# GT shows:
#   - left: small stroke slanting down-right (小撇), long 撇 down-left curving
#   - right: small stroke down-left, long 捺 down-right

# Left side of 癶:
# Small 点/short diagonal at top
line([(75, 45), (95, 70)], w=4)
# Long 撇 curving down-left
line([(105, 55), (95, 95), (70, 140), (50, 170)], w=4)

# Right side of 癶:
# Small 撇 (short diagonal down-left)
line([(185, 50), (170, 75)], w=4)
# Small 点 (short diagonal down-right) making the top of the right radical
line([(180, 55), (200, 80)], w=4)
# Long 捺 curving down-right
line([(155, 75), (180, 115), (215, 150), (245, 170)], w=4)

# ---- BOTTOM: 天 (horizontal + horizontal + 人) ----
# Top horizontal of 天 (shorter, upper)
line([(80, 170), (215, 165)], w=4)
# Second horizontal of 天 (longer, lower)
line([(65, 200), (230, 200)], w=4)
# 撇 of 人 (from just above/at second horizontal center, down-left)
line([(150, 195), (110, 240), (85, 265)], w=4)
# 捺 of 人 (from same center, down-right)
line([(150, 205), (185, 245), (215, 265)], w=4)

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_癸.png")
img.save(out)
print("wrote", out)
