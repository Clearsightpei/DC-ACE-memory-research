"""
夕 (xi) — 3-stroke radical.
Strokes: 1) 撇 (top short throw-away, upper-right → lower-left)
         2) 横折钩 (short 横 + shoulder + long 撇 tail curving down-left; note: MMH form
            for 夕 is really 横折钩-like but the "hook" is a long bowed 撇 tail — see GT)
         3) 点/短撇 inside the belly (short throw-away from top-right inside to lower-left)

Renderer: PIL brush-dabs. 300x300 white canvas, black ink.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        steps = max(40, int(math.hypot(x1 - x0, y1 - y0) * 2))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=200, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ---- Stroke 1: top 撇 ----
# short throw-away starting upper-mid, sweeping down-left; lands near stroke-2's start x
# GT shows this 撇's tip landing in the middle of the character horizontally
p0 = (175, 65)
p2 = (105, 175)
ctrl = (155, 115)
dab(p0[0], p0[1], 6)  # small 顿笔 — standalone-scale, no big ball
bezier_dabs(p0, ctrl, p2, 6, 1.2, steps=250, ease=1.2)

# ---- Stroke 2: 横折 with long bowed 撇 tail (夕's outer body) ----
# short 横 starting from where stroke-1 originated area, going right; shoulder;
# then long bowed 撇 down-left tail
h_start = (150, 78)
h_end = (210, 70)   # slight up-tilt
# 横
line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], 5.5, 5.5, steps=140)
# shoulder dab — modest, this IS a real 折 shoulder so r+2 is appropriate
dab(h_end[0], h_end[1], 7.5)
# long bowed 撇 tail: from shoulder curving down and to the LEFT
# Belly on the RIGHT (tail arcs from upper-right sweeping down-left, bulging rightward)
tail_p0 = (210, 70)
tail_p2 = (100, 262)
tail_ctrl = (225, 180)  # pull rightward → belly on right, tail arcs to left
bezier_dabs(tail_p0, tail_ctrl, tail_p2, 6.5, 1.2, steps=350, ease=1.15)

# ---- Stroke 3: inside 点 (short 撇-like dot) ----
# small throw-away inside the belly — upper-right → lower-left
# Positioned inside the belly (between the outer tail and stroke 1)
in_p0 = (180, 150)
in_p2 = (140, 195)
in_ctrl = (168, 172)
dab(in_p0[0], in_p0[1], 4.5)
bezier_dabs(in_p0, in_ctrl, in_p2, 5, 1.3, steps=120, ease=1.2)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_075_夕/01_夕.png")
