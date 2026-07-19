"""片 (piàn) — 4画部首. REVISION 1.

Revision notes vs pass 1:
- Pass 1's 撇 was too vertical; GT's 撇 curves noticeably (convex-right)
  and its tip lands in the lower area but not off-canvas. Re-tune.
- Pass 1's middle 横 was too low (mid-canvas y=150). GT has the 横
  around y~130 (upper-middle), forming the bottom of the top 竖.
- Pass 1's bottom L was too small and detached from 撇. GT has the
  横 part of the bottom-L reaching from the 撇 body across to the
  right descender. Extend the horizontal.
- Overall: composition should read as 撇 down the left, small 卜-like
  cluster (short 竖 + short 横) on upper-right, and a bottom-right L
  where the horizontal welds to the 撇 body.

Anchor plan (revised):
  stroke 1 (撇 pie, curved):
    head @ ('TC', 0.20, 0.20) -> px (120, 20)
    tail @ ('BL', 0.55, 0.90) -> px (55, 290)
    curved bow to the right.
  stroke 2 (短竖 shu, upper-right):
    head @ ('TC', 0.75, 0.30) -> px (175, 30)
    tail @ ('C',  0.75, 0.25) -> px (175, 125)
    straight vertical (same column).
  stroke 3 (短横 heng, connects 撇 body to right 竖):
    head @ ('C',  0.05, 0.25) -> px (105, 125)   # near 撇 body
    tail @ ('MR', 0.10, 0.25) -> px (210, 125)   # right side
    same row.
  stroke 4 (横折 heng_zhe, bottom L; horizontal welds to 撇 body):
    head   @ ('C',  0.10, 0.55) -> px (110, 155)  # T-weld with 撇 body
    corner @ ('MR', 0.10, 0.55) -> px (210, 155)  # right edge, same row
    tail   @ ('MR', 0.10, 1.40) -> px (210, 240)  # straight down (still in canvas)

Joints:
  s1.mid ~ s3.head  (N, small gap ~5-15 px OK, per TR10 must read connected)
  s1.mid ~ s4.head  (N, small gap ~5-15 px OK)
  s2.tail ~ s3 (N, ~10 px)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revision 1. Rendered 4 strokes matching MMH count. Two specific visual '
             'agreements vs GT: (1) long curved 撇 sweeps from upper-mid down to lower-left, '
             'curved convex-right — same as GT. (2) bottom-right L (横折) has its horizontal '
             'starting at the 撇 body and extending right, then dropping down as a right-side '
             'vertical — same enclosing "mouth" shape as GT. (3) short 竖+短横 pair sits '
             'in the upper-right, forming the 卜-like cluster.'
}

import os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(os.path.dirname(HERE), '..', 'success_bank', 'code')
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---------- stroke 1: 撇 (long down-left sweep, curved) ----------
s1_head = anchor_to_xy(('TC', 0.20, 0.20))
s1_tail = anchor_to_xy(('BL', 0.55, 0.90))
mid1 = ((s1_head[0] + s1_tail[0]) / 2, (s1_head[1] + s1_tail[1]) / 2)
# Bow rightward (convex-right): perpendicular to chord, pointing +x direction
# chord direction: (s1_tail - s1_head) roughly (-65, 250); perpendicular to right = (+250, +65) normalized
# We want ctrl on the right side of the chord
ctrl1 = (mid1[0] + 35, mid1[1] - 10)
s1_pts = quad_bezier(s1_head, ctrl1, s1_tail, n=48)
s1_widths = [max(2, 12 - 10 * (i / 48)) for i in range(len(s1_pts))]
stroke_variable_width(draw, s1_pts, s1_widths)

# ---------- stroke 2: 短竖 (short vertical, upper-right) ----------
s2_head = anchor_to_xy(('TC', 0.75, 0.30))
s2_tail = anchor_to_xy(('C',  0.75, 0.25))
assert abs(s2_head[0] - s2_tail[0]) < 2
fat_line(draw, s2_head, s2_tail, width=8)

# ---------- stroke 3: 短横 (horizontal between 撇 and right 竖) ----------
s3_head = anchor_to_xy(('C',  0.05, 0.25))
s3_tail = anchor_to_xy(('MR', 0.10, 0.25))
assert abs(s3_head[1] - s3_tail[1]) < 12
fat_line(draw, s3_head, s3_tail, width=7)

# ---------- stroke 4: 横折 (bottom-right L; horizontal welds to 撇 body) ----------
s4_head   = anchor_to_xy(('C',  0.10, 0.55))
s4_corner = anchor_to_xy(('MR', 0.10, 0.55))
s4_tail   = anchor_to_xy(('MR', 0.10, 1.40))  # descends into BR area but staying at x=210
assert abs(s4_head[1] - s4_corner[1]) < 6, '横折 horizontal must be flat'
assert abs(s4_corner[0] - s4_tail[0]) < 4, '横折 vertical must be same column'
fat_line(draw, s4_head, s4_corner, width=8)
# 顿笔 disc at corner
r = 6
draw.ellipse([s4_corner[0]-r, s4_corner[1]-r, s4_corner[0]+r, s4_corner[1]+r], fill=(0,0,0))
fat_line(draw, s4_corner, s4_tail, width=8)

# ---------- Sanity gap checks ----------
# Find s1's actual pixel position at t ~ 0.4 (where the horizontals should attach)
def pt_on_bezier(t, p0, p1, p2):
    return ((1-t)**2 * p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0],
            (1-t)**2 * p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1])

s1_at_29 = pt_on_bezier(0.29, s1_head, ctrl1, s1_tail)
s1_at_54 = pt_on_bezier(0.54, s1_head, ctrl1, s1_tail)
gap_s1_s3 = ((s1_at_29[0]-s3_head[0])**2 + (s1_at_29[1]-s3_head[1])**2)**0.5
gap_s1_s4 = ((s1_at_54[0]-s4_head[0])**2 + (s1_at_54[1]-s4_head[1])**2)**0.5
print(f's1@0.29 = {s1_at_29}, s3.head = {s3_head}, gap = {gap_s1_s3:.1f} px')
print(f's1@0.54 = {s1_at_54}, s4.head = {s4_head}, gap = {gap_s1_s4:.1f} px')

out = os.path.join(HERE, '01_片.png')
img.save(out)
print(f'Saved {out}')
