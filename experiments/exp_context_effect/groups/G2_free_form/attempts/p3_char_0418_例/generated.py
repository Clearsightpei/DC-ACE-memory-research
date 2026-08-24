"""
例 = 亻 (left) + 歹 (middle) + 刂 (right)  — 8 strokes total
Layout: three columns.
  亻: 撇 (top-left down-left) + 竖 (down)
  歹: 一 (short horizontal top) + 撇 (short down-left from top) + 横折 (small
      shoulder with descending fold) + 撇 (long down-left through body)
  刂: 短竖 (short down) + 竖钩 (down + tiny hook UP-LEFT)  — per TIER-0 hook rule
Rendered with PIL, 300x300, black ink on white.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(points, width=7):
    d.line(points, fill=INK, width=width, joint="curve")
    for p in points:
        d.ellipse((p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2), fill=INK)


def bezier(p0, p1, p2, n=30):
    return [(
        (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t**2*p2[0],
        (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t**2*p2[1],
    ) for t in [i/n for i in range(n+1)]]


# ---- 亻 (left, x ~ 40-80) ----
# 撇: from upper area down-left
stroke(bezier((78, 80), (65, 130), (40, 200)), width=7)
# 竖: from top of 撇 straight down
stroke([(78, 100), (80, 250)], width=7)

# ---- 歹 (middle, x ~ 100-180) ----
# 一 top: horizontal
stroke([(112, 82), (178, 80)], width=7)
# 撇 (short) descending from top-right of 一 down-left through center
stroke(bezier((158, 68), (130, 105), (108, 130)), width=7)
# 横折 shoulder box: small horizontal then down-turn (starts under 一)
stroke([(122, 125), (172, 122)], width=7)
stroke([(172, 122), (168, 168)], width=7)
# long 撇 sweeping through body down-left
stroke(bezier((160, 135), (135, 195), (100, 260)), width=7)
# 点 at right bottom of the 歹
stroke(bezier((155, 180), (162, 195), (175, 208)), width=7)

# ---- 刂 (right, x ~ 200-260) ----
# 短竖 (left short vertical)
stroke([(205, 100), (207, 175)], width=7)
# 竖钩 (right long vertical with hook up-left)
stroke([(250, 85), (250, 250)], width=7)
# hook flick UP-LEFT
stroke([(250, 250), (232, 240)], width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0418_例/01_例.png")
print("wrote 01_例.png")
