"""
橫折提 (heng-zhe-ti): horizontal + downward turn (折 shoulder) + rising 提.

Three beats:
  1. 横 primary — left→right, slight up-tilt (~3-5°), uniform width, small
     顿 press at the start.
  2. 折 shoulder — sharp ~90° corner at the right end of 横, one slightly
     larger dab; short 竖 dropping down from the corner (this stroke's 竖
     segment is short compared to 横折's; it exists mainly to anchor the
     提).
  3. 提 tail — rising up-and-right from the bottom of the short 竖,
     thick→thin, tapering to a sharp tip. Angle ~25-30° above horizontal.

Uses the brush-dab technique from drawer_memory.md.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab_line(p0, p1, r_start, r_end, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab(p, r):
    x, y = p
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- Beat 1: 横 (horizontal) ---
# Start upper-left area, end near the right side. Slight upward tilt.
# In 横折提, the 横 tends to be a bit shorter than a standalone 横 because
# the 提 needs horizontal room. Place it in the upper-middle band.
heng_start = (55, 105)
heng_end = (215, 92)   # slight upward tilt (~4-5°)
r_heng = 5.5

# 顿笔 opening press
dab(heng_start, r_heng + 2)
# main 横 body; ramp radius up slightly at the end toward the 折 shoulder
dab_line(heng_start, heng_end, r_heng, r_heng + 1.5)

# --- Beat 2: 折 shoulder + short 竖 down ---
# Shoulder dab, slightly bigger — this is the 顿 press at the corner.
shoulder = (218, 92)
dab(shoulder, r_heng + 3.5)

# Short 竖 dropping straight down from the shoulder. In 横折提 the vertical
# is short (much shorter than in a pure 横折), because 提 then springs off
# the bottom.
shu_top = (215, 96)
shu_bot = (207, 168)   # slight lean-in typical of a short 竖 inside 折
dab_line(shu_top, shu_bot, r_heng + 2.0, r_heng + 0.5)

# --- Beat 3: 提 rising ---
# Start at the bottom of the short 竖, rise up-and-right, thick→thin, sharp tip.
# Angle roughly 25-30° above horizontal.
ti_start = (200, 172)
ti_end = (270, 122)    # up and to the right; ~35° above horizontal
# Small joining 顿 at the base of the 提 to hide the seam with the 竖 tail.
dab(ti_start, r_heng + 2.5)
dab_line(ti_start, ti_end, r_heng + 1.5, 1.2)

out_path = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p1_stroke_20_橫折提/01_橫折提.png"
)
img.save(out_path)
print("saved:", out_path)
