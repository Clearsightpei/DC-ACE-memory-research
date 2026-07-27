"""Render 升 (rise) as a 300x300 PNG, white background, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

# 升 4 strokes:
# 1) 丿 (pie) — long curved slash starting upper-middle, sweeping down to lower-left
# 2) short rising heng (short tick) — small stroke going up-right from the pie
# 3) long heng — horizontal crossing through the middle-right
# 4) long shu — tall vertical on the right that extends above and below

# Stroke 1: pie (丿) — starts around (145, 55), curves down-left to (75, 245)
# smooth curve via multi-segment
pie_pts = [
    (150, 55), (140, 90), (128, 125), (115, 160),
    (100, 195), (85, 225), (72, 250)
]
d.line(pie_pts, fill=INK, width=LW, joint="curve")

# Stroke 2: short rising tick — small stroke crossing the pie around upper-middle
# from lower-left up to upper-right, meeting stroke 1 area
d.line([(70, 155), (140, 130)], fill=INK, width=LW)

# Stroke 3: long horizontal (heng) — crosses middle, slight rise to the right
d.line([(55, 180), (250, 170)], fill=INK, width=LW)

# Stroke 4: long vertical (shu) — right side, extends from top to bottom
d.line([(200, 55), (200, 275)], fill=INK, width=LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_升.png")
img.save(out_path)
print(f"wrote {out_path}")
