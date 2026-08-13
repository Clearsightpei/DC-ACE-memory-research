"""疥 (jiè, "scabies") — 9 strokes.

Decomposition: 疥 = 疒 (sickness-radical, 5 strokes) + 介 (4 strokes).
  疒 = top-dot (s1) + top-heng (s2) + long-left-pie (s3) + upper-dot (s4) + lower-ti/dot (s5)
  介 = long-pie (s6) + long-na (s7) + short-pie (s8) + short-shu (s9)

Approach: inline via base primitives (fat_line / stroke_variable_width /
quad_bezier) with MMH-verbatim anchors from dispatcher block.
Per B9 A-recipe point 4: base primitives + MMH-verbatim beats compound
overrides. No bank primitive for 疒 exists — no BANK_DEVIATION signal
needed.
"""

# Memory-index reading order log:
#   1. drawer_memory.md — read (A-recipe, N-joint discipline).
#   2. success_bank/INDEX.md grep — no entry for 疥, 疒, 介.
#   3. errata.md grep — no entry for 疥.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 draw calls, one per MMH stroke
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 7 joints are N (natural gap) — inlined with small gap preserved
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; all N-joints preserved (no welds).',
}

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line


def A(t):
    return anchor_to_xy(t)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- 疒 radical (strokes 1-5) ---

# s1: top small dot (short diagonal). MMH: TC(0.389,0.489) -> TC(0.74,0.706)
p0 = A(('TC', 0.389, 0.489)); p1 = A(('TC', 0.74, 0.706))
stroke_variable_width(d, sample_line(p0, p1, n=16),
                      widths=[3] + [6]*15 + [3], color=(0, 0, 0))

# s2: top heng (short). MMH: TC(0.049,0.987) -> TR(0.224,0.87)
p0 = A(('TC', 0.049, 0.987)); p1 = A(('TR', 0.224, 0.87))
stroke_variable_width(d, sample_line(p0, p1, n=24),
                      widths=[5] + [7]*23 + [4], color=(0, 0, 0))

# s3: long left 撇 with slight curve. MMH: TL(0.85,0.926) -> BL(0.354,0.9)
p0 = A(('TL', 0.85, 0.926)); p2 = A(('BL', 0.354, 0.9))
# curve control point pulled slightly left of the midline
mx = (p0[0] + p2[0]) / 2 - 8
my = (p0[1] + p2[1]) / 2
pts = quad_bezier(p0, (mx, my), p2, n=48)
n = len(pts)
widths = [max(2, int(round(9 * (1 - i / (n - 1)) + 3 * (i / (n - 1))))) for i in range(n)]
stroke_variable_width(d, pts, widths, color=(0, 0, 0))

# s4: upper left dot. MMH: ML(0.398,0.219) -> ML(0.612,0.512)
p0 = A(('ML', 0.398, 0.219)); p1 = A(('ML', 0.612, 0.512))
stroke_variable_width(d, sample_line(p0, p1, n=14),
                      widths=[3] + [6]*13 + [4], color=(0, 0, 0))

# s5: lower ti (rising) / dot. MMH: BL(0.146,0.083) -> ML(0.797,0.811)
p0 = A(('BL', 0.146, 0.083)); p1 = A(('ML', 0.797, 0.811))
stroke_variable_width(d, sample_line(p0, p1, n=24),
                      widths=[7] + [5]*23 + [2], color=(0, 0, 0))

# --- 介 (strokes 6-9), sits in the right-inner region ---

# s6: 介's long left 撇. MMH: C(0.611,0.11) -> BL(0.946,0.027)
p0 = A(('C', 0.611, 0.11)); p2 = A(('BL', 0.946, 0.027))
mx = (p0[0] + p2[0]) / 2 - 6
my = (p0[1] + p2[1]) / 2
pts = quad_bezier(p0, (mx, my), p2, n=48)
n = len(pts)
widths = [max(2, int(round(8 * (1 - i / (n - 1)) + 3 * (i / (n - 1))))) for i in range(n)]
stroke_variable_width(d, pts, widths, color=(0, 0, 0))

# s7: 介's long right 捺. MMH: C(0.761,0.312) -> MR(0.807,0.89)
p0 = A(('C', 0.761, 0.312)); p2 = A(('MR', 0.807, 0.89))
# subtle na curve — control slightly right/down of midpoint
mx = (p0[0] + p2[0]) / 2 + 4
my = (p0[1] + p2[1]) / 2 + 4
pts = quad_bezier(p0, (mx, my), p2, n=48)
n = len(pts)
widths = [max(3, int(round(4 * (1 - i / (n - 1)) + 10 * (i / (n - 1))))) for i in range(n)]
stroke_variable_width(d, pts, widths, color=(0, 0, 0))

# s8: 介's short inner 撇 (left inner). MMH: C(0.269,0.96) -> BL(0.952,0.88)
p0 = A(('C', 0.269, 0.96)); p1 = A(('BL', 0.952, 0.88))
stroke_variable_width(d, sample_line(p0, p1, n=24),
                      widths=[6] + [5]*23 + [2], color=(0, 0, 0))

# s9: 介's right inner 竖 (short vertical). MMH: C(0.831,0.834) -> BC(0.945,1.059)
p0 = A(('C', 0.831, 0.834)); p1 = A(('BC', 0.945, 1.059))
fat_line(d, p0, p1, width=7, color=(0, 0, 0))

out = os.path.join(_HERE, '01_疥.png')
img.save(out)
print(f'wrote {out}')
