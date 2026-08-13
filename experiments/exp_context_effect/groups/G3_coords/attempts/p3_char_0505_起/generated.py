# BANK_DEVIATION
# skipped: zou_zhi.py, ji.py, tu.py
# reason: 起 = 走 (left, with long swooping 捺 that runs under the whole
#   character) + 己 (upper right sitting above that 捺). The bank's
#   zou_zhi is 辶 (different radical), tu is standalone 土, and ji is a
#   standalone 己 sized for full canvas — none composes cleanly into this
#   走-wraps-under-己 layout. Inline fresh.
# fresh_component: qi_char_left_zou + qi_char_upper_right_ji
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, width=5):
    d.line([p0, p1], fill="black", width=width)

def polyline(pts, width=5):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], width=width)

def curve(pts, width=5, steps=28):
    p0, p1, p2 = pts
    prev = p0
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        line(prev, (x, y), width=width)
        prev = (x, y)

# ==== 走 (top-left 土 + middle wide heng + lower 龰 with sweeping na) ====
# top heng (土 top)
line((55, 70), (135, 70), width=5)
# short shu of 土
line((92, 50), (92, 95), width=5)
# 土 base heng
line((60, 98), (128, 98), width=5)

# short vertical stem from 土 base down to middle heng
line((92, 98), (92, 148), width=5)

# WIDE middle heng — crosses under the whole character, extends past 己 zone
line((30, 148), (215, 148), width=5)

# lower part: 撇 sweeping down-left from around center
curve([(95, 155), (65, 200), (30, 265)], width=5)

# 捺 — long calligraphic sweep from center-mid to far bottom-right
curve([(105, 175), (180, 235), (285, 255)], width=6)

# ==== 己 (upper right) ====
# 横折: top heng + right-down descent
polyline([(170, 60), (240, 60), (240, 105)], width=5)
# middle heng
line((170, 105), (232, 105), width=5)
# left vertical continuation of the 竖弯钩 from the top-left corner
polyline([(170, 60), (170, 138)], width=5)
# bottom curve of 竖弯钩: from left-bottom sweeping right, ending with small upward hook
curve([(170, 138), (205, 148), (250, 140)], width=5)
# hook tick upward
line((248, 142), (243, 128), width=5)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_起.png")
img.save(out_path)
print("Saved", out_path)
