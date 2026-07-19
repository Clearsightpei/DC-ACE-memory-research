"""
p2_radical_099_旡 — G2 revision.

Revision from first attempt: (a) reduced visible 顿-dab balls at
standalone endpoints (per memory: use plain r or r+1, not r+2, at
terminal endpoints for standalones); (b) moved the 横折 nub upward
and slightly left so it reads as a compact tucked corner rather
than centered; (c) extended the 竖弯钩 sweep so the horizontal
baseline segment reaches farther right; (d) enlarged the terminal
hook flick and angled it a bit more toward NW so it reads as a
swept flick rather than a nub.

旡 (4 strokes):
  1) short top 横 (heng), upper-center
  2) 撇 (pie) descending from upper-right down-and-left
  3) 横折 (heng-zhe) forming a small tucked corner in middle area
  4) 竖弯钩 (shu-wan-gou) — long sweep with terminal hook up-left

PIL brush-dab technique. Canvas 300x300, white bg, black ink.
Image coords: y grows DOWN.
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
# Stroke 1: short top 横 (heng), upper-center
#   Small horizontal bar; subtle terminal presses (no visible balls).
# ---------------------------------------------------------------
h1_x0, h1_y0 = 110, 82
h1_x1, h1_y1 = 195, 78  # tiny up-tilt
r_h = 4.5
dab(h1_x0, h1_y0, r_h + 0.5)  # subtle 顿
line_dabs(h1_x0, h1_y0, h1_x1, h1_y1, r_h, r_h)
dab(h1_x1, h1_y1, r_h + 0.5)  # subtle end press

# ---------------------------------------------------------------
# Stroke 2: 撇 (pie), throws from upper-right down-and-left.
#   Starts above the top 横 on its right side, sweeps down through
#   the middle-left, ending in the lower-left region. Gentle bow.
# ---------------------------------------------------------------
p_p0 = (188, 62)
p_p2 = (58, 260)
p_p1 = (165, 165)   # ctrl toward interior → gentle rightward bow
dab(p_p0[0], p_p0[1], 9)  # 顿笔 at start (smaller than before)
bezier_dabs(p_p0, p_p1, p_p2, r_start=7.5, r_end=1.4, steps=280, easing=1.15)

# ---------------------------------------------------------------
# Stroke 3: 横折 — small tucked corner, positioned mid-left.
#   Short 横 then shoulder then short 竖. Forms the "hook-nub" the
#   GT shows in the middle. Kept compact.
# ---------------------------------------------------------------
hz_x0, hz_y0 = 100, 135      # start of short 横
hz_x1, hz_y1 = 168, 130      # end of 横 / start of 竖 (slight up-tilt)
hz_x2, hz_y2 = 165, 168      # end of 竖 (short drop)
r_hz = 4.5
dab(hz_x0, hz_y0, r_hz + 0.8)                              # start press
line_dabs(hz_x0, hz_y0, hz_x1, hz_y1, r_hz, r_hz + 0.5)    # ramp up into corner
dab(hz_x1, hz_y1, r_hz + 2.5)                              # shoulder 顿
line_dabs(hz_x1, hz_y1, hz_x2, hz_y2, r_hz + 0.5, r_hz)    # short 竖
dab(hz_x2, hz_y2, r_hz + 1.0)                              # blunt end

# ---------------------------------------------------------------
# Stroke 4: 竖弯钩 — the sweeping tail dominating the right side.
#   Vertical descends from upper-right, arcs smoothly rightward
#   along the baseline, extends farther right, then terminal hook
#   flicks up-and-slightly-left.
# ---------------------------------------------------------------
# Vertical segment (bezier for a gentle bow so it can lean slightly).
v_x0, v_y0 = 208, 92         # top of the sweep, near top-right area
v_x1, v_y1 = 132, 222        # bottom-of-vertical / start-of-arc
bezier_dabs(
    (v_x0, v_y0),
    (172, 162),              # ctrl pulled toward interior
    (v_x1, v_y1),
    r_start=6.5, r_end=5.5, steps=240, easing=1.0,
)

# Smooth arc: descending-vertical → rightward-horizontal.
# Tangent-continuous parametrization from drawer_memory.
R = 34
arc_steps = 100
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = v_x1 + R * (1 - math.cos(t * math.pi / 2))
    y = v_y1 + R * math.sin(t * math.pi / 2)
    dab(x, y, 5.5)

arc_end_x = v_x1 + R
arc_end_y = v_y1 + R

# Longer rightward 横 along baseline from arc end (extends farther right).
h2_x1 = arc_end_x + 78
h2_y1 = arc_end_y
line_dabs(arc_end_x, arc_end_y, h2_x1, h2_y1, 5.5, 5.5)

# Terminal hook flick: up-and-slightly-left. Longer + more swept.
hook_len = 42
hook_angle = math.radians(-118)  # slightly more toward NW
hook_x1 = h2_x1 + hook_len * math.cos(hook_angle)
hook_y1 = h2_y1 + hook_len * math.sin(hook_angle)
# Joining dab at hook base equal to segment radius (per memory).
dab(h2_x1, h2_y1, 5.5)
hook_steps = 110
for i in range(hook_steps + 1):
    t = i / hook_steps
    x = h2_x1 + (hook_x1 - h2_x1) * t
    y = h2_y1 + (hook_y1 - h2_y1) * t
    r = 5.5 + (1.2 - 5.5) * t
    dab(x, y, r)


out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_旡.png")
img.save(out_path)
print(f"Saved: {out_path}")
