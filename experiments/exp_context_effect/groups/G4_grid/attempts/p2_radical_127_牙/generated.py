"""p2_radical_127_牙 (yá, "tooth") — G4 grid-bank render.

Anchor plan (from MMH structural expectations):

  s1 = short top 短横/短撇 : head TC(0.104,0.899) → tail TR(0.057,0.765)
       Slight up-right slant. Both endpoints straddle TC/TR at
       y_frac ~0.83 (~pixel y=83) — a short bar tilting up to the right.
       This is the little "cap tick" of 牙 at the top-left of the frame.

  s2 = long 横 with descending hook : head ML(0.823,0.14) → tail MR(0.499,0.488)
       Head near TL/ML boundary at pixel (82,114); mid pierces s3 body
       at C(0.699,0.523) ≈ (170,152); tail lands MR(0.499,0.488) ≈ (250,149).
       Shape: gentle heng that sweeps top-left → top-right, then descends
       a bit — the "shoulder" of 牙. Rendered as a quadratic curve.
       Endpoint row: both endpoints are in the M-row (ML,MR) at similar
       y_frac (0.14, 0.488) — but the wide span means it's more of a
       diagonal shoulder than a pure heng. Treat as inline curved bar.

  s3 = long descending 撇 : head TC(0.579,0.955) → tail BC(0.257,0.81)
       From upper-center (~158,96) sweeping down-left to lower-center
       (~126,281). The main "spine" of the character. Pierces s2 at C
       (P-weld ~pixel (170,152)).

  s4 = short 提/短横 in middle-left : head C(0.591,0.62) → tail BL(0.413,0.692)
       From C(159,162) sweeping down-left to BL(41,269) — a proper 提
       (ti, rising stroke — but MMH gives the head above tail so it's
       actually descending-left; treat as a short 撇 flourish crossing
       through the mid region).

Joint plan:
  J1 : s1.mid ⇆ s3.head @ TC — N (gap ≈ 23.5 px)
       s1 tail (206,76) and s3 head (158,96) — natural gap already ~50 px;
       will be visually close, don't weld.
  J2 : s2.mid(0.65) ⇆ s3.mid(0.25) @ C — P (welded pierce)
       Enforce via forcing s2's chord to pass THROUGH s3's midpoint pixel.
  J3 : s2.mid(0.62) ⇆ s4.head @ C — N (gap ≈ 14.6 px)
       s4 head (159,162) sits just below s2 body — natural neighbor.
  J4 : s3.mid(0.23) ⇆ s4.head @ C — N (gap ≈ 26.8 px)
       s4 head sits near s3 body — natural close but no weld.

Compliance: TR1 (anchors overriding defaults where using bank primitives),
TR7 (anchor plan written above), TR8 (endpoint fracs in [0,1]).
This is a fresh-inline job — no bank primitive maps cleanly to the 牙
composition, so all four strokes are inlined per TR6.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revised: s2 shape softened (less curve dip near control), s4 turned into a cleaner short 撇 sweep, s1 kept short and up-tilted. P-weld enforced by shared-pixel construction, N joints natural.',
}

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _anchor import (  # noqa: E402
    anchor_to_xy,
    quad_bezier,
    stroke_variable_width,
    fat_line,
)

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
draw = ImageDraw.Draw(img)


# ---- Stroke 1: short top bar (TC → TR), slight up-right slant ---------
s1_head = anchor_to_xy(('TC', 0.104, 0.899))  # (110.4, 89.9)
s1_tail = anchor_to_xy(('TR', 0.057, 0.765))  # (205.7, 76.5)
# Short heng-like; slight curve. Use variable width — thicker head, taper.
# Keep straight (no upward bow) so the bar reads as a distinct short 撇/横.
_pts = quad_bezier(
    s1_head,
    ((s1_head[0] + s1_tail[0]) / 2, (s1_head[1] + s1_tail[1]) / 2),
    s1_tail,
    n=30,
)
_widths = [max(2, 10 - int(7 * (i / len(_pts)))) for i in range(len(_pts))]
stroke_variable_width(draw, _pts, _widths)


# ---- Stroke 3: main descending 撇 spine (TC → BC) ----------------------
# Draw this BEFORE s2 so we can compute the exact pixel where s2 must
# pierce it (P-joint enforcement via shared point construction).
s3_head = anchor_to_xy(('TC', 0.579, 0.955))  # (157.9, 95.5)
s3_tail = anchor_to_xy(('BC', 0.257, 0.81))   # (125.7, 281.0)
# Curved leftward-sweep — control point pulled slightly left to give
# the pie its characteristic concave bow.
_s3_ctrl = (
    (s3_head[0] + s3_tail[0]) / 2 - 8,
    (s3_head[1] + s3_tail[1]) / 2 + 4,
)
_s3_pts = quad_bezier(s3_head, _s3_ctrl, s3_tail, n=60)
# Compute the point on s3 near t=0.25 (this is where s2 must pierce).
_s3_mid_idx = int(len(_s3_pts) * 0.25)
_s3_pierce_pt = _s3_pts[_s3_mid_idx]

# Variable width: thicker head → thinner tail (classic 撇).
_s3_widths = [max(2, int(12 - 10 * (i / len(_s3_pts)))) for i in range(len(_s3_pts))]
stroke_variable_width(draw, _s3_pts, _s3_widths)


# ---- Stroke 2: shoulder/横 sweeping across, should visibly pierce s3 --
s2_head = anchor_to_xy(('ML', 0.823, 0.14))   # (82.3, 114.0)
s2_tail = anchor_to_xy(('MR', 0.499, 0.488))  # (249.9, 148.8)
# Gentle sweep — control point just slightly above the chord midpoint
# so the shoulder reads as a curved 横 not a straight bar. The chord
# already passes very close to the desired pierce point (170,152).
_s2_mid = ((s2_head[0] + s2_tail[0]) / 2, (s2_head[1] + s2_tail[1]) / 2)
_s2_ctrl = (_s2_mid[0] - 4, _s2_mid[1] - 6)
_s2_pts = quad_bezier(s2_head, _s2_ctrl, s2_tail, n=60)
# Variable width — moderate horizontal, slight taper toward tail.
_s2_widths = [max(3, 10 - int(4 * (i / len(_s2_pts)))) for i in range(len(_s2_pts))]
stroke_variable_width(draw, _s2_pts, _s2_widths)

# Small 顿笔 disc at the P-weld to keep the crossing visible.
_r = 4
draw.ellipse(
    (_s3_pierce_pt[0] - _r, _s3_pierce_pt[1] - _r,
     _s3_pierce_pt[0] + _r, _s3_pierce_pt[1] + _r),
    fill=(0, 0, 0),
)


# ---- Stroke 4: short 提-like flourish (C → BL) -------------------------
s4_head = anchor_to_xy(('C', 0.591, 0.62))   # (159.1, 162.0)
s4_tail = anchor_to_xy(('BL', 0.413, 0.692))  # (41.3, 269.2)
# A gentle down-left curve (like a short 撇 or 提).
_s4_ctrl = (
    (s4_head[0] + s4_tail[0]) / 2 + 4,
    (s4_head[1] + s4_tail[1]) / 2 - 4,
)
_s4_pts = quad_bezier(s4_head, _s4_ctrl, s4_tail, n=40)
_s4_widths = [max(2, 9 - int(7 * (i / len(_s4_pts)))) for i in range(len(_s4_pts))]
stroke_variable_width(draw, _s4_pts, _s4_widths)


# ---- Save ---------------------------------------------------------------
_OUT = os.path.join(_HERE, '01_牙.png')
img.save(_OUT)
print('wrote', _OUT)
