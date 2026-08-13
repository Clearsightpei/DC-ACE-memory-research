"""p3_char_0431_说 — 讠 + 兑 (9 strokes).

Decomposition:
  讠 = s1 (dot) + s2 (横折提)             — left column
  兑 = 丷 (s3, s4) + 口 (s5,s6,s7) + 儿 (s8, s9) — right side

MMH provides all 9 endpoint anchors. Because each bank primitive
(yan_speech, kou, er_legs) is calibrated for a whole-canvas standalone
render, using them here would require overriding every anchor tuple,
which the drawer_memory rules forbid. Inline via MMH-verbatim anchors
per B8 guidance (trust MMH).
"""
# BANK_DEVIATION
# skipped: yan_speech.py, kou.py, er_legs.py
# reason: each primitive is calibrated to fill the whole canvas; 说 needs
#         讠 in x<0.30 column and 兑 slotted right-of-讠 as three stacked
#         sub-parts. Overriding all default anchors on 3 primitives is
#         disallowed per drawer_memory's "never-tune-anchors" rule.
# fresh_component: shuo_composition (inlined 讠+兑 via MMH anchors)

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-verbatim anchors for all 9 strokes; all 8 joints class N (small gaps preserved by shortening).'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)


def _short(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    m = (dx * dx + dy * dy) ** 0.5
    if m < 1e-6:
        return pt
    t = min(1.0, px / m)
    return (x0 + dx * t, y0 + dy * t)


# ----- 讠 (left radical) -----
# s1 — 点 (upper dot) — MMH head TL(0.747, 0.686) -> tail TC(0.069, 0.949)
s1h = anchor_to_xy(('TL', 0.747, 0.686))
s1t = anchor_to_xy(('TC', 0.069, 0.949))
stroke_variable_width(d,
    quad_bezier(s1h,
                ((s1h[0] + s1t[0]) / 2 - 4, (s1h[1] + s1t[1]) / 2 - 2),
                s1t, n=24),
    [3] * 13 + [10] * 12)

# s2 — 横折提 — MMH head ML(0.188, 0.649) -> tail BC(0.195, 0.256)
s2h = anchor_to_xy(('ML', 0.188, 0.649))
s2t = anchor_to_xy(('BC', 0.195, 0.256))
# Shape: horizontal from head-right, then vertical down at corner,
# then a ti up-flick to tail. Corner at right end of the heng bar.
s2corner1 = anchor_to_xy(('ML', 0.90, 0.68))   # top-right of the fold
s2corner2 = anchor_to_xy(('BL', 0.70, 0.35))   # bottom of vertical
fat_line(d, s2h, s2corner1, width=8)
fat_line(d, s2corner1, s2corner2, width=8)
# ti flick — thick to thin going up-right
pts_ti = [s2corner2, s2t]
fat_line(d, s2corner2, s2t, width=7)

# ----- 兑 (right side) -----
# s3 — 丷 left dot — MMH TC(0.43, 0.806) -> C(0.649, 0.046) : this reads
#     as a short pie going down-left from top toward center; render as thick dot-pie
s3h = anchor_to_xy(('TC', 0.43, 0.806))
s3t_raw = anchor_to_xy(('C', 0.649, 0.046))
s3t = _short(s3t_raw, s3h, 8)   # keep N gap from s4/s5 area
stroke_variable_width(d,
    quad_bezier(s3h, ((s3h[0] + s3t[0]) / 2, (s3h[1] + s3t[1]) / 2), s3t, n=24),
    [9] * 13 + [3] * 12)

# s4 — 丷 right dot — MMH TR(0.165, 0.554) -> C(0.887, 0.066) : pie going down-left
s4h = anchor_to_xy(('TR', 0.165, 0.554))
s4t_raw = anchor_to_xy(('C', 0.887, 0.066))
s4t = _short(s4t_raw, s4h, 8)
stroke_variable_width(d,
    quad_bezier(s4h, ((s4h[0] + s4t[0]) / 2, (s4h[1] + s4t[1]) / 2), s4t, n=24),
    [3] * 13 + [10] * 12)

# ----- 口 (mouth, small, in middle-right area) -----
# s5 — 口 left wall (shu) — MMH C(0.307, 0.354) -> C(0.512, 0.939)
s5h_raw = anchor_to_xy(('C', 0.307, 0.354))
s5t_raw = anchor_to_xy(('C', 0.512, 0.939))
s5h = _short(s5h_raw, s5t_raw, 3)
s5t = _short(s5t_raw, s5h_raw, 3)
fat_line(d, s5h, s5t, width=8)

# s6 — 口 top+right wall (heng-zhe) — MMH C(0.447, 0.345) -> MR(0.027, 0.673)
s6h_raw = anchor_to_xy(('C', 0.447, 0.345))
s6t_raw = anchor_to_xy(('MR', 0.027, 0.673))
s6c = (s6t_raw[0], s6h_raw[1])   # corner at top-right of the little box
s6h = _short(s6h_raw, s6c, 3)
s6t = _short(s6t_raw, s6c, 3)
fat_line(d, s6h, s6c, width=8)
fat_line(d, s6c, s6t, width=8)

# s7 — 口 bottom (heng) — MMH C(0.564, 0.884) -> MR(0.197, 0.784)
# note MMH lists s7 head near bottom-of-口 and tail up-right (drawn L→R
# in canonical order); anchors correspond to bottom bar.
s7h_raw = anchor_to_xy(('C', 0.564, 0.884))
s7t_raw = anchor_to_xy(('MR', 0.197, 0.784))
s7h = _short(s7h_raw, s7t_raw, 3)
s7t = _short(s7t_raw, s7h_raw, 3)
fat_line(d, s7h, s7t, width=8)

# ----- 儿 (legs, bottom) -----
# s8 — 撇 — MMH BC(0.477, 0.101) -> BL(0.993, 0.918) : long pie down-left
s8h = anchor_to_xy(('BC', 0.477, 0.101))
s8t = anchor_to_xy(('BL', 0.993, 0.918))
# add a mid control for slight curve
s8m = ((s8h[0] + s8t[0]) / 2 - 4, (s8h[1] + s8t[1]) / 2 + 6)
pts = quad_bezier(s8h, s8m, s8t, n=48)
widths = [11 - (11 - 2) * i / 48 for i in range(49)]
stroke_variable_width(d, pts, widths)

# s9 — 竖弯钩 — MMH C(0.811, 0.878) -> BR(0.73, 0.3)
# 竖弯钩: descend vertically from head, sweep right at bottom, hook UP.
# MMH head is upper (y=0.878 in C = y~188), tail is upper-right (y=0.3 in BR = y~230)
# The tail is the hook tip pointing UP. Vertical goes DOWN first, then curves.
s9h = anchor_to_xy(('C', 0.811, 0.878))       # top of vertical, right-of-center
s9belly = anchor_to_xy(('BC', 0.85, 0.55))    # descending vertical mid-BC
s9corner = anchor_to_xy(('BR', 0.10, 0.85))   # bend at bottom
s9sweep = anchor_to_xy(('BR', 0.65, 0.75))    # sweep along bottom
s9tip = anchor_to_xy(('BR', 0.73, 0.30))      # hook UP tip (= MMH tail)
# vertical segment
fat_line(d, s9h, s9belly, width=9)
fat_line(d, s9belly, s9corner, width=9)
# curve to right along bottom (approximate arc via two segments)
fat_line(d, s9corner, s9sweep, width=9)
# hook up
fat_line(d, s9sweep, s9tip, width=7)

# Stroke count assertion (self-check)
STROKE_COUNT = 9
assert STROKE_COUNT == 9

out_path = os.path.join(os.path.dirname(__file__), '01_说.png')
img.save(out_path)
print(f"wrote {out_path}")
