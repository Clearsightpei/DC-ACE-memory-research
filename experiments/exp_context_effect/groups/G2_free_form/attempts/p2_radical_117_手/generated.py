"""
p2_radical_117_手 — 4-stroke radical (hand).

Structure (from GT):
  1. 撇 (top): short throw from upper-right → down-and-left (the "flag" on top).
  2. 横 (short, top): horizontal, sits just below where the 撇 tail lands;
     forms the top bar of the "hand fingers".
  3. 横 (long, middle): the longest horizontal; crosses lower.
  4. 竖钩 (vertical hook): straight vertical through both horizontals,
     terminal hook flicks up-and-left from the bottom.

Renderer: PIL brush-dabs (per drawer_memory technique).
Canvas: 300x300 white, black ink.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(p0, p1, r_start, r_end, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r_start, r_end, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# -----------------------------------------------------------------
# Stroke 1: 撇 (top-left flag) — throw from upper-right down to left.
# In GT it starts at upper-mid, curls down-left, ending slightly above
# and to the left of the top 横's start.
p1_start = (195, 70)
p1_ctrl = (160, 85)
p1_end = (75, 115)
# 顿 dab at the start
dab(*p1_start, 8)
bezier_taper(p1_start, p1_ctrl, p1_end, 7.5, 2.0, steps=400)

# -----------------------------------------------------------------
# Stroke 2: short top 横. Starts near where the 撇 tail ends, runs
# rightward with slight upward tilt. Shorter than middle 横.
p2_start = (95, 128)
p2_end = (210, 118)
dab(*p2_start, 7)
line_taper(p2_start, p2_end, 5.5, 5.5, steps=300)
dab(*p2_end, 7)

# -----------------------------------------------------------------
# Stroke 3: long middle 横 (the LONGEST horizontal). Crossbar through
# the vertical, well below the top bar. Slight up-tilt.
p3_start = (40, 180)
p3_end = (260, 170)
dab(*p3_start, 7)
line_taper(p3_start, p3_end, 6.0, 6.0, steps=400)
dab(*p3_end, 7)

# -----------------------------------------------------------------
# Stroke 4: 竖钩 — vertical through both horizontals, ending in a hook
# up-and-slightly-left at the bottom. Starts at/near top-横 level,
# extends down to near bottom of canvas.
v_start = (155, 105)
v_end = (155, 258)
dab(*v_start, 7)
line_taper(v_start, v_end, 6.0, 6.0, steps=400)

# Hook flick from v_end, going up-and-left at ~-115° (image coords).
hook_len = 34
hook_angle_deg = -125  # a bit steeper up
ha = math.radians(hook_angle_deg)
h_end = (v_end[0] + hook_len * math.cos(ha),
         v_end[1] + hook_len * math.sin(ha))
# Joining dab equal to segment radius (per memory: not r+1/r+2 at hook base)
dab(*v_end, 6)
line_taper(v_end, h_end, 6.0, 1.2, steps=200)

# -----------------------------------------------------------------
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "01_手.png")
img.save(out_path)
print(f"Saved: {out_path}")
