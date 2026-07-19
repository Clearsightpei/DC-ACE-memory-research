"""
纟 (silk radical, 3 strokes).

Structure: two 撇折 stacked in the upper 2/3, then a 提 at the bottom.
  Stroke 1: 撇折 — short 撇 from upper-right to lower-left, shoulder-dab,
            short 横 running rightward.
  Stroke 2: 撇折 — same shape, placed below stroke 1, slightly shifted
            so its 撇 starts near where stroke 1's 横 ends (creating the
            characteristic "cursive" zig).
  Stroke 3: 提 (rising) — thick-to-thin, going from lower-left to
            upper-right, forming the base.

Applies:
- shared-joint principle (2): each 撇折's two beats share their shoulder.
- 撇折 recipe from drawer_memory: 撇 primary + shoulder-dab + short 横
  with slight up-tilt + terminal press.
- Standalone scale-up: modestly larger curvature; small 顿-dabs (r+1
  at endpoints, not r+2) to avoid balloon-heads on a standalone radical.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier(P0, P1, P2, r_start, r_end, steps=400):
    """Quadratic Bezier stroke, taper r_start -> r_end via brush dabs."""
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t ** 2 * P2[0]
        y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t ** 2 * P2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def line_stroke(P0, P1, r_start, r_end, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = P0[0] + (P1[0] - P0[0]) * t
        y = P0[1] + (P1[1] - P0[1]) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# --------------------------------------------------------------
# Stroke 1: upper 撇折
#   撇 from (155, 55) throwing down-left to (105, 110)
#   shoulder dab at 撇 tip
#   横 rightward to (175, 100) with slight up-tilt
# --------------------------------------------------------------
p1_start = (155, 55)
p1_ctrl  = (140, 90)
p1_tip   = (105, 110)
bezier(p1_start, p1_ctrl, p1_tip, r_start=6.5, r_end=2.0, steps=350)
# 顿 dab at start of 撇 (small for standalone)
dab(*p1_start, 7)
# shoulder dab at 撇 tip
dab(*p1_tip, 5.5)
# 横 rightward from tip, slight up-tilt
h1_end = (185, 100)
line_stroke(p1_tip, h1_end, r_start=5.0, r_end=4.0, steps=250)
# small terminal press at horizontal end
dab(*h1_end, 5.5)


# --------------------------------------------------------------
# Stroke 2: middle 撇折 (below stroke 1, offset slightly right at top)
#   撇 from (170, 125) to (115, 180)
#   横 rightward to (190, 170)
# --------------------------------------------------------------
p2_start = (170, 125)
p2_ctrl  = (155, 160)
p2_tip   = (115, 180)
bezier(p2_start, p2_ctrl, p2_tip, r_start=6.5, r_end=2.0, steps=350)
dab(*p2_start, 7)
dab(*p2_tip, 5.5)
h2_end = (195, 170)
line_stroke(p2_tip, h2_end, r_start=5.0, r_end=4.0, steps=250)
dab(*h2_end, 5.5)


# --------------------------------------------------------------
# Stroke 3: 提 (rising) — thick to thin, up-and-right
#   from lower-left (75, 245) to upper-right (215, 210)
#   thick start, sharp tip, angle ~15° above horizontal (mild rise)
# --------------------------------------------------------------
ti_start = (75, 245)
ti_end   = (215, 210)
line_stroke(ti_start, ti_end, r_start=8.5, r_end=1.2, steps=350)
# small 顿 dab at rising start
dab(*ti_start, 9.5)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_070_纟/01_纟.png")
print("wrote 01_纟.png")
