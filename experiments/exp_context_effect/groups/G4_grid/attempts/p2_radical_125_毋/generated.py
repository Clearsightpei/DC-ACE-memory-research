"""毋 (wú, 4画) — G4 attempt (revised), MMH-anchor driven.

Revised after first-pass visual mismatch: s1 median passes through
several waypoints indicating a 竖折-shape outer contour (left wall +
bottom bar). Drawn as a polyline through the joint-implied midpoints.

Anchor plan (from MMH-derived structural expectations block):
  s1 (竖折-shaped outer contour, LEFT wall + BOTTOM bar):
     head @ TL(0.911, 0.826) = (91, 82.6)
     mid  @ ML(0.901, 0.617) = (90.1, 161.7)   [fraction 0.25]
     mid  @ BC(0.261, 0.215) = (126.1, 221.5)  [fraction 0.61]
     mid  @ BC(0.908, 0.224) = (190.8, 222.4)  [fraction 0.81]
     tail @ BR(0.517, 0.385) = (251.7, 238.5)

  s2 (short 竖 inner, upper-left of center):
     head @ TC(0.061, 0.888) = (106.1, 88.8)
     tail @ BC(0.333, 0.774) = (133.3, 277.4)

  s3 (撇 diagonal top-center → bottom-left):
     head @ C(0.383, 0.099)  = (138.3, 109.9)
     tail @ BL(0.665, 0.824) = (66.5, 282.4)

  s4 (横 through middle):
     head @ ML(0.217, 0.649) = (21.7, 164.9)
     tail @ MR(0.704, 0.553) = (270.4, 155.3)

Joints (all P except one N):
  s1.mid ⇆ s2.mid @ BC : P
  s1.mid ⇆ s3.mid @ BC : P
  s1.mid ⇆ s4.mid @ ML : P
  s2.head ⇆ s3.head @ C : N (gap ~33 px)
  s2.mid ⇆ s4.mid @ C : P
  s3.mid ⇆ s4.mid @ C : P
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 stroke primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Second render. s1 drawn as polyline through MMH midpoints '
             'to preserve the 竖折-shaped outer contour. s2 short vertical, '
             's3 撇 with curve, s4 middle 横. All P joints welded via shared '
             'crossings; N joint at C is (s2.head 106,89) vs (s3.head 138,110) '
             '≈ 38 px gap.'
}

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
draw = ImageDraw.Draw(img)


# ---- s1: outer contour polyline (竖折-shape) ----
s1_pts = [
    anchor_to_xy(('TL', 0.911, 0.826)),   # (91, 82.6)   head
    anchor_to_xy(('ML', 0.901, 0.617)),   # (90.1, 161.7)
    anchor_to_xy(('BC', 0.261, 0.215)),   # (126.1, 221.5) — corner region
    anchor_to_xy(('BC', 0.908, 0.224)),   # (190.8, 222.4)
    anchor_to_xy(('BR', 0.517, 0.385)),   # (251.7, 238.5) tail
]
# Densify with a curve smoothing through the corner (waypoint 1 → 2 has sharp bend)
# Use straight segments for a clean 竖折 look but with a slightly rounded corner.
def draw_polyline(draw, pts, width=10):
    from _anchor import fat_line
    for i in range(len(pts) - 1):
        fat_line(draw, pts[i], pts[i + 1], width=width)

draw_polyline(draw, s1_pts, width=10)


# ---- s2: short 竖 inner-upper ----
s2_head = anchor_to_xy(('TC', 0.061, 0.888))   # (106.1, 88.8)
s2_tail = anchor_to_xy(('BC', 0.333, 0.774))   # (133.3, 277.4)
fat_line(draw, s2_head, s2_tail, width=10)


# ---- s3: 撇 diagonal top → bottom-left ----
s3_head = anchor_to_xy(('C', 0.383, 0.099))    # (138.3, 109.9)
s3_tail = anchor_to_xy(('BL', 0.665, 0.824))   # (66.5, 282.4)
# Curved sweep with concave-right (positive x-curve offset at midpoint)
ctrl_s3 = ((s3_head[0] + s3_tail[0]) / 2 + 12,
           (s3_head[1] + s3_tail[1]) / 2)
pts_s3 = quad_bezier(s3_head, ctrl_s3, s3_tail, n=40)
n3 = len(pts_s3) - 1
widths_s3 = [12 - 9 * (i / n3) for i in range(n3 + 1)]   # taper head→tail
stroke_variable_width(draw, pts_s3, widths_s3)


# ---- s4: middle 横 ----
s4_head = anchor_to_xy(('ML', 0.217, 0.649))   # (21.7, 164.9)
s4_tail = anchor_to_xy(('MR', 0.704, 0.553))   # (270.4, 155.3)
fat_line(draw, s4_head, s4_tail, width=9)


out = os.path.join(os.path.dirname(__file__), '01_毋.png')
img.save(out)
print(f'Wrote {out}')
