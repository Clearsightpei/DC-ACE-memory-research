"""Render 痈 (yong - abscess). 疒 radical enclosing 用."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line(p1, p2, w=4):
    d.line([p1, p2], fill=BLACK, width=w)


def curve(points, w=4):
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=BLACK, width=w)


# ============ 疒 radical ============
# 1) top dot (点) - short diagonal near top
line((118, 40), (135, 58), w=5)

# 2) top horizontal (一) - long
line((70, 72), (215, 68), w=5)

# 3) left long 撇 - starts near top-left of horizontal, sweeps down-left with curl
pts = []
for i in range(50):
    t = i / 49.0
    # gentle curve: mostly vertical then curl left
    x = 88 - 30 * t - 10 * (t ** 2)
    y = 72 + 190 * t
    pts.append((x, y))
curve(pts, w=5)

# 4) left dot 1 (upper) - small down-right stroke
line((78, 115), (92, 130), w=5)

# 5) left dot 2 (lower) - small down-right stroke
line((68, 148), (82, 163), w=5)

# ============ 用 inside ============
# 用 structure: left vertical (撇), top horizontal, right vertical with hook,
# center vertical piercing bottom, two internal horizontals, bottom horizontal

# Left vertical (short 撇 - slight lean)
line((122, 105), (118, 240), w=5)

# Top horizontal (also top of frame)
line((122, 105), (220, 102), w=5)

# Right vertical with hook (竖钩)
line((220, 102), (220, 240), w=5)
line((220, 240), (208, 233), w=5)

# Middle vertical piercing through bottom
line((170, 105), (170, 260), w=5)

# Two internal horizontals
line((120, 155), (220, 153), w=5)
line((120, 200), (220, 198), w=5)

# Bottom horizontal
line((120, 240), (220, 238), w=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_痈.png"))
print("saved")
