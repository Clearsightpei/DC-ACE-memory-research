"""
p3_char_0354 佧 = 亻 (left) + 卡 (right).

Layout (300x300):
- 亻 on the LEFT (~x 55-100):
  - 撇: from top (~x=85, y=70) sweeping down-left to (~x=55, y=180)
  - 竖: from mid of 撇 (~x=78, y=115) straight down to (~x=82, y=250)
- 卡 on the RIGHT (~x 130-260, centered ~x=195):
  - short 竖 (top): from (~x=195, y=70) down to (~x=195, y=105)
  - short 横 (top of 上): from (~x=195, y=95) right to (~x=235, y=90)
  - long 横 (middle main horiz): from (~x=140, y=135) right to (~x=265, y=130)
  - long 竖: from (~x=195, y=100) down through the horiz to (~x=195, y=255)
  - small 点/short 撇 tick on right side of vertical: from (~x=210, y=170) down-right to (~x=245, y=185)

Free-hand feel with slight jitter, PIL.
"""

from PIL import Image, ImageDraw
import math, random

random.seed(42)

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def stroke(points, width_start=6, width_end=6, taper=False):
    """Draw a stroke as a series of small connected discs to simulate ink."""
    if len(points) < 2:
        return
    # sample densely along polyline
    pts = []
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        d = math.hypot(x1 - x0, y1 - y0)
        n = max(2, int(d))
        for k in range(n):
            t = k / n
            pts.append((x0 + t * (x1 - x0), y0 + t * (y1 - y0)))
    pts.append(points[-1])
    total = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, total - 1)
        w = width_start + (width_end - width_start) * t if taper else (width_start + width_end) / 2
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

# ---------- 亻 (left) ----------
# 撇: top to lower-left, slight curve
pie = [(88, 68), (80, 100), (70, 135), (58, 175)]
stroke(pie, width_start=8, width_end=3, taper=True)

# 竖: from mid of 撇 straight down
shu_left = [(78, 118), (80, 175), (82, 250)]
stroke(shu_left, width_start=7, width_end=6)

# ---------- 卡 (right) ----------
# small 竖 (top of 上)
shu_top = [(195, 72), (195, 100)]
stroke(shu_top, width_start=6, width_end=6)

# short 横 (top of 上) — leans slightly up-right
heng_top = [(198, 100), (240, 92)]
stroke(heng_top, width_start=5, width_end=6)

# long 横 (middle) — leans slightly up-right
heng_mid = [(135, 138), (200, 133), (268, 128)]
stroke(heng_mid, width_start=6, width_end=6)

# long 竖 (through the character body), extends well below middle horiz
shu_main = [(195, 100), (195, 175), (195, 258)]
stroke(shu_main, width_start=7, width_end=6)

# small 点/short 撇 tick on right side of vertical (卜 side)
# From near the vertical going down-right
dian = [(207, 168), (225, 178), (245, 188)]
stroke(dian, width_start=5, width_end=3, taper=True)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0354_佧/01_佧.png")
