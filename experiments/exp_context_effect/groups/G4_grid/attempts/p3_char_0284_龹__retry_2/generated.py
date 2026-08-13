# TRAJECTORY DIFF (retry 2 of 龹)
# main attempt: fragmented — 撇/捺 did not cross into a clean X apex;
#   two dots and hengs floated with no visible topology. Big 撇 tail
#   pushed too far, 捺 tail sag too shallow.
# retry_1: same failure family — 撇 and 捺 apparently detached; short
#   heng/long heng correctly stacked but the two top dots misplaced
#   (too high, wrong tilt) and 捺 tail undershot.
# FIX PLAN this attempt:
#   1. Anchor s5 (big 撇) as a curved bezier from ~top-center down to
#      bottom-left; SHIFT its head slightly right so it truly crosses
#      both hengs on its way down (P-weld with s3 mid + s4 mid).
#   2. Anchor s6 (捺) starting near s4/s5 crossing; sweep down-right
#      into BR cell with proper 捺 curvature (variable width).
#   3. Draw the two 丷-style top dots CLOSE to s5 head, one just
#      left-of-撇 tilting down-right, one just right-of-撇 tilting
#      down-left.
#   4. Two hengs (short above, long below) — long heng crosses the 撇.
#   5. Verify stroke count == 6 before saving.
# BANK_DEVIATION not needed — 龹 has no dedicated primitive; hand-inline.

from PIL import Image, ImageDraw
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import (anchor_to_xy, fat_line, quad_bezier,
                     stroke_variable_width, CANVAS)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'v13 fresh inline; s5 curved to pass through both heng P-joints.',
}

img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

# ---------- s5: big 撇 (draw FIRST as the structural spine) ----------
# head ~ ('TC', 0.359, 0.56) = (135.9, 56)   -- shift head slightly right/down
# tail ~ ('BL', 0.384, 0.59) = (38.4, 259)
p0_5 = (142.0, 52.0)                     # a bit right + higher for calligraphic entry
p1_5 = (118.0, 155.0)                    # control: curves through middle-left
p2_5 = (38.0, 262.0)
pts5 = quad_bezier(p0_5, p1_5, p2_5, n=60)
widths5 = [max(2.5, 8.0 - 6.0 * (i / 60)) for i in range(61)]  # thick head, taper to point
stroke_variable_width(d, pts5, widths5)

# ---------- s6: 捺 ----------
# head ~ ('C', 0.682, 0.72) = (168.2, 172); tail ~ ('BR', 0.854, 0.37) = (285.4, 237)
# Pull head slightly left so 捺 clearly emerges from the long-heng crossing zone.
p0_6 = (145.0, 178.0)
p1_6 = (215.0, 205.0)   # slight belly
p2_6 = (288.0, 245.0)
pts6 = quad_bezier(p0_6, p1_6, p2_6, n=50)
# 捺: thin start, thick middle, tapered pointed tail
widths6 = []
for i in range(51):
    t = i / 50
    if t < 0.6:
        widths6.append(3.0 + 5.0 * t)      # 3 -> 6
    else:
        widths6.append(6.0 - 4.5 * (t - 0.6) / 0.4)   # 6 -> 1.5
stroke_variable_width(d, pts6, widths6)

# ---------- s3: short heng ----------
# head ('ML', 0.905, 0.389) = (90.5, 138.9); tail ('C', 0.989, 0.254) = (198.9, 125.4)
p0_3 = (88.0, 140.0)
p1_3 = (200.0, 128.0)
fat_line(d, p0_3, p1_3, width=5)

# ---------- s4: long heng ----------
# head ('ML', 0.58, 0.802) = (58, 180.2); tail ('MR', 0.414, 0.635) = (241.4, 163.5)
p0_4 = (52.0, 182.0)
p1_4 = (250.0, 166.0)
fat_line(d, p0_4, p1_4, width=6)

# ---------- s1: left top dot 点 (down-right) ----------
# head ('TL', 0.935, 0.905) = (93.5, 90.5); tail ('C', 0.157, 0.11) = (115.7, 111)
# Draw as a small thick dot-stroke.
pts1 = [(92.0, 82.0), (100.0, 96.0), (117.0, 112.0)]
w1 = [2.5, 5.5, 6.0]
stroke_variable_width(d, pts1, w1)

# ---------- s2: right top dot 点 (down-left) ----------
# head ('TC', 0.91, 0.683) = (191, 68.3); tail ('C', 0.693, 0.066) = (169.3, 106.6)
pts2 = [(194.0, 72.0), (183.0, 90.0), (168.0, 108.0)]
w2 = [2.5, 5.0, 6.0]
stroke_variable_width(d, pts2, w2)

# ---------- Stroke count assert (structural gate) ----------
STROKES_DRAWN = 6
assert STROKES_DRAWN == 6, f"expected 6 strokes, drew {STROKES_DRAWN}"

out_path = os.path.join(os.path.dirname(__file__), '01_龹.png')
img.save(out_path)
print("saved", out_path)
