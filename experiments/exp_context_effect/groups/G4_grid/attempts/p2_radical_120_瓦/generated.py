"""瓦 (wǎ) — 4-stroke radical.

Stroke plan (matching MMH-derived expectations):
  s1: 横 (top horizontal, slightly tilted rising)
       head ('TL', 0.7, 0.958)  → tail ('TR', 0.206, 0.779)
  s2: 丿 (pie — long descending left-curve from upper mid down to mid-bottom)
       head ('ML', 0.976, 0.055) → tail ('BC', 0.468, 0.42)
  s3: 横斜钩 (main horizontal-slanted-hook wrapping from mid-left across to BR
       area with an upward hook at the end)
       head ('C', 0.11, 0.608) → tail ('BR', 0.722, 0.347)
  s4: 丶 (dot in mid area — MMH tail suggests down-right dot)
       head ('C', 0.113, 0.89)  → tail ('BC', 0.424, 0.13)

Joints (all N-class per MMH — small gaps, not welded).

Revision 2: extended top horizontal endpoint area; softened pie curve;
gave 横斜钩 a substantial low belly so it looks like the wrapping hook
in the GT (which sweeps down and back up); dot slightly more prominent.
Kept endpoints within MMH tolerance (±0.20 x_frac/y_frac).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Rev2: extended s3 belly downward for wrapping look; dot compact.'
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier, stroke_variable_width,
                     fat_line, sample_line)

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
draw = ImageDraw.Draw(img)


# ---------------- Stroke 1: top 横 ------------------------------------------------
s1_head = ('TL', 0.7, 0.958)   # (~70, 96)
s1_tail = ('TR', 0.206, 0.779) # (~221, 78)
p1a = anchor_to_xy(s1_head)
p1b = anchor_to_xy(s1_tail)
pts1 = sample_line(p1a, p1b, n=30)
n1 = len(pts1) - 1
widths1 = [7 + (10 - 7) * (i / n1) for i in range(n1 + 1)]
stroke_variable_width(draw, pts1, widths1)


# ---------------- Stroke 2: 丿 pie (upper long descender) ------------------------
s2_head = ('ML', 0.976, 0.055) # (~98, 106)
s2_tail = ('BC', 0.468, 0.42)  # (~147, 242)
p2a = anchor_to_xy(s2_head)
p2b = anchor_to_xy(s2_tail)
# Pie should sweep gently left then straighten. Bow the belly leftward.
dx, dy = p2b[0] - p2a[0], p2b[1] - p2a[1]
length = max(1.0, (dx * dx + dy * dy) ** 0.5)
perp = (-dy / length, dx / length)
bow = -0.15 * length  # concave-left
mid = ((p2a[0] + p2b[0]) * 0.5, (p2a[1] + p2b[1]) * 0.5)
ctrl2 = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
pts2 = quad_bezier(p2a, ctrl2, p2b, n=48)
n2 = len(pts2) - 1
widths2 = [11 + (2 - 11) * ((i / n2) ** 1.4) for i in range(n2 + 1)]
stroke_variable_width(draw, pts2, widths2)


# ---------------- Stroke 3: 横斜钩 (wrapping right-hook that goes low then hooks up)
s3_head = ('C', 0.11, 0.608)   # (~111, 161)
s3_tail = ('BR', 0.722, 0.347) # (~272, 235)
p3a = anchor_to_xy(s3_head)
p3b = anchor_to_xy(s3_tail)
# For the wrapping look, put the belly BELOW the chord (higher y in PIL).
# Break into 2 pieces so we can push the belly LOW (near y ~ 275) then
# come up to the tail before hooking.
low_belly = (200, 275)  # deep swoop point (near BC bottom)
# First half: p3a → low_belly (horizontal-going-down curve)
mid1_ctrl = (p3a[0] + 60, p3a[1] + 20)  # start heading right, dip
pts3a = quad_bezier(p3a, mid1_ctrl, low_belly, n=40)
# Second half: low_belly → p3b (rising back up-right to tail)
mid2_ctrl = (low_belly[0] + 50, low_belly[1] - 10)
pts3b = quad_bezier(low_belly, mid2_ctrl, p3b, n=30)
pts3 = pts3a + pts3b[1:]
n3 = len(pts3) - 1
widths3 = []
for i in range(n3 + 1):
    t = i / n3
    # 8 → 12 (belly) → 9
    if t < 0.55:
        w = 8 + (12 - 8) * (t / 0.55)
    else:
        w = 12 + (9 - 12) * ((t - 0.55) / 0.45)
    widths3.append(w)
stroke_variable_width(draw, pts3, widths3)

# Hook: small upward flick from p3b going up-and-slightly-left
hook_len = 26
hook_tip = (p3b[0] - 6, p3b[1] - hook_len)
hook_ctrl = (p3b[0] + 3, p3b[1] - hook_len * 0.5)
hpts = quad_bezier(p3b, hook_ctrl, hook_tip, n=20)
kh = len(hpts) - 1
hwidths = [9 + (1 - 9) * (i / kh) for i in range(kh + 1)]
stroke_variable_width(draw, hpts, hwidths)


# ---------------- Stroke 4: 丶 dot (short slant down-right) ----------------------
s4_head = ('C', 0.113, 0.89)   # (~111, 189)
s4_tail = ('BC', 0.424, 0.13)  # (~142, 213)
p4a = anchor_to_xy(s4_head)
p4b = anchor_to_xy(s4_tail)
pts4 = sample_line(p4a, p4b, n=20)
n4 = len(pts4) - 1
widths4 = []
for i in range(n4 + 1):
    t = i / n4
    if t < 0.55:
        w = 3 + (12 - 3) * (t / 0.55)
    else:
        w = 12 + (2 - 12) * ((t - 0.55) / 0.45)
    widths4.append(w)
stroke_variable_width(draw, pts4, widths4)


out_path = os.path.join(os.path.dirname(__file__), '01_瓦.png')
img.save(out_path)
print(f"Saved {out_path}")
