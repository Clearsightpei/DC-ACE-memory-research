"""
Render 佈 (亻 + 布) to 300x300 PNG.

Composition:
  Left: 亻 (person radical, compressed to left ~35% column).
    - 撇 slanting down-left
    - 竖 straight drop from mid-撇 down
  Right: 布 (cloth, 5 strokes) in right ~65% column.
    - Short 撇 at top-left (heads down-left)
    - Long 横 (horizontal cross)
    - Left 丨 of 巾 (short vertical)
    - 横折钩 forming top+right of 巾, terminal hook UP-LEFT
    - Middle 丨 of 巾 -- extends DOWN LONG past the 亻 baseline
      (this is 布's identifying feature vs 右 etc.)

Hook rule reminder (Tier-0 B): 横折钩 flick UP-and-LEFT.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def brush(points, widths):
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        dx, dy = x1 - x0, y1 - y0
        seg = max(abs(dx), abs(dy))
        steps = max(int(seg) * 2, 8)
        for s in range(steps + 1):
            t = s / steps
            x = x0 + dx * t
            y = y0 + dy * t
            r = w0 * (1 - t) + w1 * t
            d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# =========================================================
# LEFT: 亻  (compressed left-position person radical)
# =========================================================
# 撇
pie_pts = [(85, 55), (78, 85), (65, 115), (48, 145), (28, 175)]
pie_ws = [5.0, 5.0, 4.5, 3.5, 1.8]
brush(pie_pts, pie_ws)
# tiny curl at head
brush([(85, 55), (90, 62), (86, 72)], [5.0, 3.8, 2.3])

# 竖  (starts near where 撇 body passes, ~x=70 y=95, drops to y=245)
shu_pts = [(70, 100), (70, 150), (70, 200), (70, 250)]
shu_ws = [5.0, 5.0, 5.0, 4.5]
brush(shu_pts, shu_ws)
# tiny top 顿
d.ellipse((66, 97, 75, 106), fill="black")


# =========================================================
# RIGHT: 布  (right column x=105..280)
# =========================================================

# Stroke 1: short 撇 at top-left of 布 (starts upper, throws down-left)
p1 = [(160, 45), (150, 65), (135, 85), (118, 105)]
w1 = [4.5, 4.0, 3.2, 1.8]
brush(p1, w1)

# Stroke 2: long 横 (horizontal), sweeps across right column
p2 = [(108, 108), (170, 105), (240, 105), (280, 110)]
w2 = [4.0, 4.5, 4.5, 3.5]
brush(p2, w2)
# small 顿 at right end of 横
d.ellipse((276, 105, 288, 117), fill="black")

# Stroke 3: left 丨 of 巾 (short vertical, hangs from 横)
p3 = [(148, 135), (148, 175), (148, 215), (148, 250)]
w3 = [4.5, 4.5, 4.5, 4.0]
brush(p3, w3)

# Stroke 4: 横折钩 -- top+right of 巾, hook flicks UP-LEFT
# Horizontal top piece (inside the 一)
p4a = [(150, 138), (200, 135), (250, 138)]
w4a = [4.0, 4.5, 5.0]
brush(p4a, w4a)
# Right vertical drop
p4b = [(250, 138), (250, 180), (250, 225)]
w4b = [5.0, 5.0, 4.8]
brush(p4b, w4b)
# Hook flick UP-and-LEFT from the bottom of the vertical
p4c = [(250, 225), (240, 218), (230, 213)]
w4c = [4.8, 3.5, 1.8]
brush(p4c, w4c)
# shoulder 顿 at the top-right corner
d.ellipse((245, 133, 258, 146), fill="black")

# Stroke 5: middle 丨 of 巾 -- extends DOWN LONG (past 亻 baseline)
# starts from just under the 横, drops to y=285 (well below)
p5 = [(198, 140), (198, 190), (198, 240), (198, 285)]
w5 = [4.5, 4.5, 4.5, 4.0]
brush(p5, w5)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0328_佈/01_佈.png"
)
