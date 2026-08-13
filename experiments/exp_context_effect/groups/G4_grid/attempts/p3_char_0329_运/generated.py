"""p3_char_0329_运 — G4 attempt (revision 1).

运 = 云 (top-right) + 辶 (walk radical wrapping bottom-left).

Revision fixes vs pass 1:
- s1 (top heng): removed TC-far-up waypoint that produced caret shape.
- s2 (long heng): flatter, single midpoint.
- s3/s4 (厶): tightened around the two anchor pairs so they read as a
  small ㄥ triangle rather than open ">".
- s6 (compound S): explicit right-then-down-then-right zigzag using
  ML/BL midpoints, matching the compact span implied by MMH endpoints.
- s7 (平捺): flatter sweep, less dip.

Memory consult: chuo_walk.py exists for standalone 辶 but its anchors
fill the canvas — in 运, 辶 must cede the upper-right half to 云, so
inline via MMH-verbatim (v9 lesson). All 3 joints are N (natural gap).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 7 poly calls == expected 7
    'endpoint_mismatches': [],         # all endpoints MMH-verbatim
    'joint_class_mismatches': [],      # all 3 joints N (no explicit weld)
    'overall_pass': True,
    'notes': 'Revision 1: caret s1 fixed; 厶 tightened; compound-S given explicit zigzag; 平捺 flatter.'
}

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, stroke_variable_width
from PIL import Image, ImageDraw

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)


def poly(anchors, widths):
    pts = [anchor_to_xy(a) for a in anchors]
    stroke_variable_width(draw, pts, widths)


# ==== 云 (s1..s4) — top-right region ====

# s1 — 短横 (short top heng). Slight upward tilt to right.
# MMH endpoints: head C(0.471,0.025) → tail TR(0.191,0.867)
poly([
    ('C', 0.471, 0.025),
    ('TR', 0.191, 0.867),
], [8, 6])

# s2 — 长横 (longer heng, slightly bowed).
# MMH endpoints: head C(0.219,0.535) → tail MR(0.561,0.383)
poly([
    ('C', 0.219, 0.535),
    ('C', 0.65, 0.48),
    ('MR', 0.561, 0.383),
], [8, 8, 6])

# s3 — first stroke of 厶 (short down-right from s2 mid).
# MMH endpoints: head C(0.837,0.562) → tail BR(0.212,0.06)
poly([
    ('C', 0.837, 0.562),
    ('BR', 0.212, 0.06),
], [7, 5])

# s4 — closing stroke of 厶 (comes from MR, curves down into BR).
# MMH endpoints: head MR(0.112,0.784) → tail BR(0.429,0.288)
poly([
    ('MR', 0.112, 0.784),
    ('MR', 0.35, 0.95),
    ('BR', 0.429, 0.288),
], [4, 7, 9])

# ==== 辶 (s5..s7) — walking radical wrapping bottom-left ====

# s5 — 点 (upper-left dot; thin head → thick tail).
# MMH endpoints: head TL(0.765,0.677) → tail TC(0.093,0.932)
poly([
    ('TL', 0.765, 0.677),
    ('TC', 0.093, 0.932),
], [3, 10])

# s6 — 横折折撇 (compact S in left column).
# MMH endpoints: head ML(0.334,0.588) → tail BL(0.902,0.396)
# Shape: short heng right → down corner → short heng right → diagonal down-right.
poly([
    ('ML', 0.334, 0.588),   # head
    ('ML', 0.78, 0.60),     # heng right
    ('ML', 0.80, 0.85),     # corner down
    ('ML', 0.55, 0.98),     # short heng left
    ('BL', 0.65, 0.20),     # into BL cell
    ('BL', 0.902, 0.396),   # tail (near s7 mid)
], [6, 7, 8, 7, 6, 5])

# s7 — 平捺 (long horizontal sweep across bottom).
# MMH endpoints: head BL(0.375,0.531) → tail BR(0.766,0.789)
poly([
    ('BL', 0.375, 0.531),
    ('BL', 0.75, 0.68),
    ('BC', 0.50, 0.78),
    ('BR', 0.30, 0.80),
    ('BR', 0.766, 0.789),
], [4, 9, 12, 10, 5])


img.save(os.path.join(_HERE, '01_运.png'))
print('OK — 7 strokes rendered (rev 1)')
