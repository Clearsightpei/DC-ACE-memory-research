"""
艹 (grass radical, 3 strokes).
Structure (per MMH / GT):
  Beat 1: LEFT vertical (short 竖, slight lean — top slightly right of bottom,
          i.e. leans left-going-down, /).
  Beat 2: RIGHT vertical (short 竖, slight lean — top slightly left of bottom,
          i.e. leans right-going-down, \).
  Beat 3: LONG horizontal 横 crossing through both verticals, slight up-tilt
          (left end lower than right end).

Canvas 300x300, PIL brush-dabs, black on white.
The horizontal crosses both verticals — crossings must be visible on both
sides (principle 3 from memory).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def segment(x0, y0, x1, y1, r_start, r_end, steps=None):
    """Linear brush-dab segment with linearly-varying radius."""
    L = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(80, int(L * 2.5))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---- Layout ----
# 艹 is wide and short — sits in the upper/middle band. GT shows it
# roughly centered vertically with the horizontal around y~155 and
# verticals spanning roughly y=100..y=225.
#
# Horizontal spans ~x=40..x=270 with a slight up-tilt (left lower, right higher).
# Left vertical sits at ~x=110, right vertical at ~x=200.
# Left vertical leans slightly LEFT going down (top at x=115, bottom at x=105).
# Wait — inspecting GT: left top slants outward-left as it rises,
# and right top slants outward-right as it rises. So bottoms are closer
# together than tops:
#   Left vert: top (105, 100) → bottom (118, 225)   (leans right going down)
#   Right vert: top (215, 100) → bottom (200, 225)  (leans left going down)
# Actually re-checking: in the GT the two verticals splay outward at their
# tops — like a shallow /\. Give them a slight outward lean at the top.

# ---- Beat 3 first (bottom layer): long horizontal ----
# Slight up-tilt: left y=170, right y=152.
r_h = 4.5
horiz_x0, horiz_y0 = 38, 170
horiz_x1, horiz_y1 = 272, 152
# subtle press only (standalone-scale — no big balls)
dab(horiz_x0, horiz_y0, r_h + 1)
segment(horiz_x0, horiz_y0, horiz_x1, horiz_y1, r_h, r_h)
dab(horiz_x1, horiz_y1, r_h + 1)

# ---- Beat 1: LEFT vertical ----
# Per GT: tops splay outward, bottoms come inward.
# Left vert leans like `\` — top at ~(100, 105), bottom at ~(122, 235).
r_v = 4.5
lv_top = (100, 105)
lv_bot = (122, 235)
dab(*lv_top, r_v + 1)  # slight 顿 at start
segment(lv_top[0], lv_top[1], lv_bot[0], lv_bot[1], r_v, r_v - 1)  # slight taper toward tip
dab(*lv_bot, r_v - 0.5)  # small terminal

# ---- Beat 2: RIGHT vertical ----
# Right vert leans like `/` — top at ~(222, 105), bottom at ~(198, 235).
rv_top = (222, 105)
rv_bot = (198, 235)
dab(*rv_top, r_v + 1)
segment(rv_top[0], rv_top[1], rv_bot[0], rv_bot[1], r_v, r_v - 1)
dab(*rv_bot, r_v - 0.5)

# Save
out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_039_艹/01_艹.png"
img.save(out)
print("Saved:", out)
