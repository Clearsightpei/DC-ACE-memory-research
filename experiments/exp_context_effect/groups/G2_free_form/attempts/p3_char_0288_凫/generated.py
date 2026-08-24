"""
凫 (fu, wild duck) — top: 鸟-simplified head + horizontal;
bottom: 几 (short 撇 + 横折弯钩 with UP-LEFT hook flick).

Structure (top→bottom):
1. Small 撇 above head (short flick down-left).
2. 头 (head): 横折 forming closed rounded rectangle head.
3. 点 inside head (small dot).
4. 横 (long horizontal) crossing through middle, longer than head.
5. 几 底: 短撇 on left + 横折弯钩 on right with UP-LEFT hook.

Applying hook rule: 横折弯钩 terminal flicks UP-and-LEFT (~-115°).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = (0, 0, 0)


def stroke(pts, width=6):
    d.line(pts, fill=INK, width=width, joint="curve")
    for x, y in pts:
        d.ellipse((x - width / 2, y - width / 2, x + width / 2, y + width / 2), fill=INK)


def bezier(p0, p1, p2, p3, n=40):
    out = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u ** 3 * p0[0] + 3 * u ** 2 * t * p1[0] + 3 * u * t ** 2 * p2[0] + t ** 3 * p3[0]
        y = u ** 3 * p0[1] + 3 * u ** 2 * t * p1[1] + 3 * u * t ** 2 * p2[1] + t ** 3 * p3[1]
        out.append((x, y))
    return out


# 1. Top 撇 (extends up-left above head, longer to match GT prominence)
stroke(bezier((165, 30), (155, 45), (148, 58), (132, 75)), width=5)

# 2. Head — 横折钩 as single folded stroke, slightly rounded corners.
# Starts top-left (below where 撇 lands), across, folds down-right, curves back left.
top = bezier((146, 68), (165, 65), (185, 66), (192, 72))       # top slight arch
right = bezier((192, 72), (196, 88), (194, 102), (188, 112))    # right side curve
bot = bezier((188, 112), (170, 115), (152, 114), (140, 110))    # bottom back-left
left = bezier((140, 110), (138, 95), (140, 80), (146, 68))      # closing left
for seg in (top, right, bot, left):
    stroke(seg, width=6)

# 3. 点 inside head (slightly lower-center)
d.ellipse((160, 84, 174, 98), fill=INK)

# 4. Long horizontal crossing (the base of top section, extends beyond head)
stroke([(75, 140), (225, 138)], width=6)

# 5a. 几-底 short 撇 (left leg)
stroke(bezier((115, 155), (108, 200), (100, 235), (78, 268)), width=6)

# 5b. 几-底 横折弯钩 — 横 across top of 几, 折 down-right, 弯 sweeps
# 横 (short flat top)
stroke([(115, 155), (210, 155)], width=6)
# 折 down and gentle curve to right, sweeping down then up-left hook
sweep = bezier((210, 155), (218, 210), (215, 250), (185, 265))
stroke(sweep, width=6)
# 弯 continues right-bottom then hook UP-LEFT
hook_body = bezier((185, 265), (215, 268), (238, 258), (245, 235))
stroke(hook_body, width=6)
# 钩 flick UP-and-LEFT (~-115° per TIER-0 hook rule)
stroke([(245, 235), (232, 220)], width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0288_凫/01_凫.png")
