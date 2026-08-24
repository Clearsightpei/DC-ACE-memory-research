"""
伄 = 亻 (left) + 吊 (right).
Right 吊 = 口 (small mouth top) + 巾 (bottom):
  - 巾 has a top 横, two side 竖 (left short, right 横折竖), and
    a long central 竖钩 extending down.
  - The central 竖 of 巾 continues UP through 口 (identity of 吊).

Layout choices:
- 亻: 撇 from top curving down-left; 竖 shorter than in standalone 人.
- 口: small square, top-center of right column.
- 巾-body sits under 口; central 竖 goes from just under 口's top all the way down with UP-LEFT hook flick.
"""
from PIL import Image, ImageDraw
from math import comb

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, w=6):
    d.line([p1, p2], fill="black", width=w)

def bezier(pts, steps=80, w=6):
    n = len(pts) - 1
    prev = None
    for i in range(steps + 1):
        t = i / steps
        x = sum(comb(n, k) * (1 - t) ** (n - k) * t ** k * pts[k][0] for k in range(n + 1))
        y = sum(comb(n, k) * (1 - t) ** (n - k) * t ** k * pts[k][1] for k in range(n + 1))
        if prev is not None:
            d.line([prev, (x, y)], fill="black", width=w)
        prev = (x, y)

# ---------- LEFT: 亻 (person radical, compressed) ----------
# 撇: 起笔 top around (95, 65), sweep down-left curving out to (50, 200)
bezier([(95, 65), (88, 120), (75, 170), (50, 205)], w=7)
# 竖: from junction near top of 撇 straight down (shorter than 撇)
line((97, 90), (97, 235), w=7)

# ---------- RIGHT: 吊 ----------
# 口 at top: ~x 155..220, y 60..110
# top 横
line((155, 62), (220, 62), w=6)
# left 竖
line((156, 62), (156, 110), w=6)
# right 横折 (single stroke joining top-right to bottom-right via corner already at 220,62)
line((220, 62), (220, 110), w=6)
# bottom 横 (closes the mouth)
line((155, 110), (220, 110), w=6)

# 巾 body under 口
# top 横 of 巾 — wider than 口 (like shoulders): x 138..238, y 135
line((138, 135), (238, 135), w=6)
# left short 竖 of 巾
line((150, 135), (150, 200), w=6)
# right 横折竖 of 巾: right vertical drops from top-横's right end
line((230, 135), (230, 200), w=6)
# a small tiny bottom hook on right side (like 冂 wraps in slightly)
# central long 竖钩: from bottom of 口 (y=110) straight down through the 巾 body,
# ends around y=265 with hook flick UP-and-LEFT
line((188, 110), (188, 265), w=7)
bezier([(188, 265), (180, 262), (172, 256), (163, 248)], w=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0248_伄/01_伄.png")
