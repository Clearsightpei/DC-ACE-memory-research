"""
p2_radical_099_旡 — G2 retry #2.

Prior retry_1 diagnosis vs GT:
  - retry_1 rendered as basically 无 (二 top + 撇/竖弯钩 splay).
    The middle 横折 was too shy and blended into a second top-横,
    so the whole glyph read as "二 + splay-legs" (无) rather than
    "一 + 横折-with-竖-drop + splay-legs" (旡).
  - The differentiating bit between 旡 and 无 (from GT) is that
    旡 has a distinctive middle 横折 whose 竖-drop is visible and
    short, NOT a full second 横. And the 竖-drop's endpoint is
    ABOVE the baseline (it does not merge with the right leg).

Fix (retry_2):
  - Give middle 横折 a clearly HORIZONTAL top-bar shorter than the
    top 一, then a definite 竖-drop of ~30 px hanging DOWN from the
    right end (so eye reads it as "hook to the right").
  - Insert a visible whitespace gap between top 一 and the middle
    折 shoulder (~30 px), so top 一 doesn't merge with the 折.
  - Left leg 撇 originates from the LEFT end of the middle-折 bar
    (not from inside), sweeping down-and-left.
  - Right leg 竖弯钩 originates from the tip of the 折's 竖-drop,
    continuing DOWN, then arcing right, hook up-left.

Total: 4 stroke visual units. Compact-square silhouette.
Canvas 300×300, white bg, black ink. PIL brush-dab. y grows DOWN.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    if steps is None:
        steps = max(60, int(L * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=200, easing=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = t ** easing
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---------------------------------------------------------------
# Stroke 1: TOP 一 — short, flat-ish, upper-center.
# ---------------------------------------------------------------
h1_x0, h1_y0 = 100, 80
h1_x1, h1_y1 = 205, 76
r_h = 4.5
dab(h1_x0, h1_y0, r_h + 0.8)
line_dabs(h1_x0, h1_y0, h1_x1, h1_y1, r_h, r_h)
dab(h1_x1, h1_y1, r_h + 1.2)  # small terminal press

# ---------------------------------------------------------------
# Stroke 2: MIDDLE 横折 — short 横 (shorter than top 一) + shoulder
#   + short 竖-drop. This is the SIGNATURE of 旡 (vs 无's 二 top).
#   Positioned with a clear gap below the top 一.
# ---------------------------------------------------------------
hz_x0, hz_y0 = 118, 138       # start of short 横 (a bit inset from left edge)
hz_x1, hz_y1 = 198, 134       # end of 横 / start of 竖-drop
hz_x2, hz_y2 = 194, 172       # end of 竖-drop (short, above baseline)
r_hz = 4.5
dab(hz_x0, hz_y0, r_hz + 0.6)
line_dabs(hz_x0, hz_y0, hz_x1, hz_y1, r_hz, r_hz + 0.3)
dab(hz_x1, hz_y1, r_hz + 2.2)  # shoulder 顿 (bold)
line_dabs(hz_x1, hz_y1, hz_x2, hz_y2, r_hz + 0.3, r_hz - 0.2)
dab(hz_x2, hz_y2, r_hz + 0.3)

# ---------------------------------------------------------------
# Stroke 3: LEFT LEG 撇 — originates near the LEFT end of the
#   middle-折 bar and sweeps down-and-LEFT to lower-left.
# ---------------------------------------------------------------
p_p0 = (118, 138)   # attaches to the left end of 折's 横
p_p2 = (55, 258)    # bottom-left
p_p1 = (92, 210)    # ctrl for gentle bow
dab(p_p0[0], p_p0[1], 7.2)     # small 顿笔 at start
bezier_dabs(p_p0, p_p1, p_p2, r_start=6.3, r_end=1.3, steps=260, easing=1.15)

# ---------------------------------------------------------------
# Stroke 4: RIGHT LEG 竖弯钩 — continues from the tip of the 折's
#   竖-drop, descending farther, arcing rightward at the baseline,
#   terminal hook flicks up-and-slightly-left.
# ---------------------------------------------------------------
v_x0, v_y0 = 194, 172         # continues from end of 折's 竖-drop
v_x1, v_y1 = 175, 240         # bottom-of-vertical / start-of-arc (slight lean-left)
bezier_dabs(
    (v_x0, v_y0),
    (188, 210),               # ctrl slightly inward
    (v_x1, v_y1),
    r_start=5.8, r_end=5.4, steps=220, easing=1.0,
)

# Tangent-continuous arc: descending-vertical → rightward-horizontal.
R = 32
arc_steps = 100
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = v_x1 + R * (1 - math.cos(t * math.pi / 2))
    y = v_y1 + R * math.sin(t * math.pi / 2)
    dab(x, y, 5.4)

arc_end_x = v_x1 + R
arc_end_y = v_y1 + R

# Rightward 横 baseline segment — extend farther right.
h2_x1 = arc_end_x + 30
h2_y1 = arc_end_y
line_dabs(arc_end_x, arc_end_y, h2_x1, h2_y1, 5.4, 5.4)

# Terminal hook flick: up-and-slightly-left.
hook_len = 38
hook_angle = math.radians(-115)
hook_x1 = h2_x1 + hook_len * math.cos(hook_angle)
hook_y1 = h2_y1 + hook_len * math.sin(hook_angle)
dab(h2_x1, h2_y1, 5.4)
hook_steps = 110
for i in range(hook_steps + 1):
    t = i / hook_steps
    x = h2_x1 + (hook_x1 - h2_x1) * t
    y = h2_y1 + (hook_y1 - h2_y1) * t
    r = 5.4 + (1.1 - 5.4) * t
    dab(x, y, r)


out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_旡.png")
img.save(out_path)
print(f"Saved: {out_path}")
