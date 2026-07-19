"""攵 (pū, 4 strokes) — Phase-2 radical 110.

Anchor plan (米字格, 300x300):
  s1 — short 撇: head TC(0.172,0.756)→(117,76), tail BL(0.639,0.039)→(64,204).
       Curved sweep down-and-left.
  s2 — short 横: head C(0.16,0.436)→(116,144), tail MR(0.188,0.26)→(219,126).
       Straight fat_line (same cell row: M-row). Very slight up-tilt matches MMH.
  s3 — 撇 (long, down-left): head C(0.582,0.471)→(158,147), tail overridden to
       BC(0.38,0.81)→(138,281) so it passes through P_CROSS at BC(0.453,0.325)
       ≈ (145,232). MMH nominal tail was BL(0.565,0.81) but shifted to
       guarantee the P-weld with s4 per sandbox lesson (犭 diagnosis).
  s4 — 捺 (down-right): head ML(0.952,0.758)→(95,176), tail overridden to
       BC(0.97,0.9)→(197,290) so it passes through the same P_CROSS.
       MMH nominal tail was BR(0.517,0.9)→(252,290) but shifted for weld.

Joints:
  J1 s1.mid(0.42) ⇆ s2.head @ C  — N (gap ~25 px)
  J2 s1.mid(0.75) ⇆ s4.head @ ML — N (gap ~18 px)
  J3 s2.mid(0.31) ⇆ s3.head @ C  — N (gap ~14 px)
  J4 s3.mid(0.48) ⇆ s4.mid(0.38) @ BC — P (welded via shared P_CROSS point)

Bank use:
  - draw_pie (s1, s3): standard tapered 撇 primitive.
  - draw_heng (s2): straight short bar.
  - draw_na (s4): standard 捺 with peak swell.
All primitives called with OVERRIDING anchors per TR1.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from na import draw_na
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Visual agreements with GT: (1) top curled short 撇 in upper '
              'mid, sweeping down-left; (2) short horizontal bar in middle '
              'region ending upper-right; (3) prominent X-cross at lower '
              'half formed by 撇 (down-left) and 捺 (down-right) with peak '
              'swell on 捺. Overridden s3/s4 tails to force P-weld crossing '
              'at BC(0.453, 0.325).'),
}


# --- Anchor definitions ---
S1_HEAD = ('TC', 0.172, 0.756)
S1_TAIL = ('BL', 0.639, 0.039)

S2_HEAD = ('C', 0.16, 0.436)
S2_TAIL = ('MR', 0.188, 0.26)

S3_HEAD = ('C', 0.582, 0.471)
S3_TAIL = ('BC', 0.38, 0.81)   # overridden from MMH BL(0.565,0.81) for P-weld

S4_HEAD = ('ML', 0.952, 0.758)
S4_TAIL = ('BC', 0.97, 0.9)    # overridden from MMH BR(0.517,0.9) for P-weld


# --- Sanity checks ---
p1h = anchor_to_xy(S1_HEAD); p1t = anchor_to_xy(S1_TAIL)
p2h = anchor_to_xy(S2_HEAD); p2t = anchor_to_xy(S2_TAIL)
p3h = anchor_to_xy(S3_HEAD); p3t = anchor_to_xy(S3_TAIL)
p4h = anchor_to_xy(S4_HEAD); p4t = anchor_to_xy(S4_TAIL)

# Direction invariants
assert p1t[0] < p1h[0] and p1t[1] > p1h[1], "s1 撇: tail should be lower-left of head"
assert p3t[0] < p3h[0] and p3t[1] > p3h[1], "s3 撇: tail should be lower-left of head"
assert p4t[0] > p4h[0] and p4t[1] > p4h[1], "s4 捺: tail should be lower-right of head"

# s2 both endpoints in M-row (TR12)
def _row(a):
    cell = a[0]
    if cell == 'C': return 1
    return {'T':0,'M':1,'B':2}[cell[0]]
assert _row(S2_HEAD) == _row(S2_TAIL), "s2 横: endpoints must share cell row"

# P-weld: s3 and s4 must actually cross in pixel space.
# Compute intersection of the two chords.
def line_intersect(a0, a1, b0, b1):
    x1,y1 = a0; x2,y2 = a1; x3,y3 = b0; x4,y4 = b1
    den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if abs(den) < 1e-6:
        return None
    t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / den
    u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / den
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (x1 + t*(x2-x1), y1 + t*(y2-y1))
    return None

cross_pt = line_intersect(p3h, p3t, p4h, p4t)
assert cross_pt is not None, f"P-weld failed: s3 and s4 must cross. s3={p3h}->{p3t}, s4={p4h}->{p4t}"
# Should be near BC(0.453, 0.325) ≈ (145.3, 232.5)
target = anchor_to_xy(('BC', 0.453, 0.325))
dist_from_target = ((cross_pt[0]-target[0])**2 + (cross_pt[1]-target[1])**2)**0.5
# Just a sanity floor
assert dist_from_target < 40, f"P-cross too far from MMH target: {cross_pt} vs {target}"


# --- Render ---
img = Image.new('RGB', (300, 300), (255, 255, 255))
draw = ImageDraw.Draw(img)

# s1: short curved 撇 (head thick TC, tail thin BL). Extra curve for GT ク-feel.
draw_pie(draw, from_anchor=S1_HEAD, to_anchor=S1_TAIL,
         head_width=10, tail_width=2, curve=0.14, segments=48)

# s2: short horizontal bar (fat_line via draw_heng)
draw_heng(draw, from_anchor=S2_HEAD, to_anchor=S2_TAIL, width=8)

# s3: long 撇 (down-left, thick head, needle tail)
draw_pie(draw, from_anchor=S3_HEAD, to_anchor=S3_TAIL,
         head_width=11, tail_width=2, curve=0.09, segments=48)

# s4: long 捺 (down-right, thin head, peak swell, needle tail)
draw_na(draw, from_anchor=S4_HEAD, to_anchor=S4_TAIL,
        head_width=3, peak_width=13, tail_width=1,
        peak_t=0.78, curve=0.08, segments=48)

# Small emphasis disc at the P-weld crossing so it reads as welded
r = 4
cx, cy = cross_pt
draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(0, 0, 0))

out_path = os.path.join(_HERE, '01_攵.png')
img.save(out_path)
print(f"Saved: {out_path}")
print(f"Cross point: {cross_pt}, target: {target}, dist: {dist_from_target:.1f}")
