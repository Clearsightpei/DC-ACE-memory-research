"""
夕 retry #1 — apply errata fix:
  - Silhouette family: "square" (x ~70%, y ~70%) per radical_position_rules.
  - Prior attempt was tall/narrow (~40%×85% tall-narrow). Widen the outer
    tail so the body opens to the right and fills a compact square.
  - Two-stroke count per MMH: (1) 撇 top, (2) 横折钩 outer body — but
    canonically visible as 3 marks with an inside 点.
  - Place the inside 点 so it clearly sits in the "belly" of the 横折钩
    (mid-height, right of the 撇), not floating high near the shoulder.
  - Cross-ref form_catalog "撇 as top-of-radical single flick" for
    stroke 1 and "折 shoulder placement" for the top-right corner.

Render at 300x300 white BG, black ink, PIL brush-dabs.
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


def bezier_dabs(p0, p1, p2, r0, r1, steps=250, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# Silhouette target: bounding box ~ x=[55, 235] (180 px wide ~60%),
# y=[50, 260] (210 px tall ~70%). Center of mass slightly upper-left
# because the top 撇 anchors upper-left and the outer 横折钩's tail
# sweeps down and outward.

# ---- Stroke 1: top 撇 (short flick, upper-right → lower-left) ----
# form_catalog: "撇 as top-of-radical single flick" — short-medium,
# steep, thick→thin, gentle rightward bow. Now anchored so its START
# is at ~the same y as the top 横 (aligns visually with the top-left
# corner of the 横折钩), and it sweeps well down-left into the body.
s1_p0 = (155, 70)
s1_ctrl = (130, 130)
s1_p2 = (70, 235)           # long sweep — dominant left body
dab(s1_p0[0], s1_p0[1], 6)   # small 顿 dab at start
bezier_dabs(s1_p0, s1_ctrl, s1_p2, 6.5, 1.3, steps=300, ease=1.15)

# ---- Stroke 2: 横折钩 outer body ----
# Short 横 running rightward from ~stroke-1's start; shoulder;
# long curving tail arcing outward (belly on RIGHT) then down-left.
h_start = (155, 70)
h_end = (220, 65)            # slight up-tilt
line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], 5.5, 5.5, steps=140)
# 折 shoulder dab (r+2 for a real corner)
dab(h_end[0], h_end[1], 7.5)

# Long bowed tail — belly on the OUTSIDE (right side), curving down and
# in to lower-left. Endpoint lands roughly under the character center.
tail_p0 = (220, 65)
tail_ctrl = (240, 170)       # rightward pull → belly on right
tail_p2 = (130, 260)         # tail lands under character center
bezier_dabs(tail_p0, tail_ctrl, tail_p2, 6.5, 1.4, steps=380, ease=1.15)

# ---- Stroke 3: inside 点 (short teardrop dot inside the belly) ----
# Positioned inside the belly at mid-height, between stroke-1's body
# and stroke-2's outer arc. Short teardrop, angled down-right.
in_p0 = (140, 145)
in_ctrl = (162, 158)
in_p2 = (180, 170)
dab(in_p0[0], in_p0[1], 4)
bezier_dabs(in_p0, in_ctrl, in_p2, 4, 6, steps=100, ease=1.2)   # thin→thick teardrop
dab(in_p2[0], in_p2[1], 6)   # terminal press

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_075_夕__retry_1/01_夕.png"
img.save(out_path)
print(f"saved {out_path}")
