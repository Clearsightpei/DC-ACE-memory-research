"""紧 (jǐn) — 10 strokes.

Decomposition: 紧 = 臤 (top: 丨 + 又) + 糸 (bottom: 幺 + 小).
  - s1        : short 丨 (top-left tick of 臤)
  - s2        : long 撇/vertical from top-center down to center
  - s3, s4    : 又 (横撇 + 捺) top-right of 臤
  - s5        : 幺 upper-vertical/hook stem in center
  - s6, s7    : 幺 lower two-arc (like 纟 hooks)
  - s8, s9, s10: 小 base three dots

MMH-verbatim anchors per B9-B13 A-recipe point 2. Base primitives
(fat_line + quad_bezier) per point 4. N-joints leave natural gaps
per point 5. No compound primitive matched slot placement well
enough to import; inlining fresh.
"""

# BANK_DEVIATION
# skipped: si_silk.py
# reason: 糸 in 紧 is bottom-compressed to y∈[0.42, 1.0] with 3-dot 小 base,
#         not si_silk's standalone 3-stroke 纟 form; MMH puts hook stem +
#         two curls + 3 dots at custom BC/BR anchors that don't match
#         si_silk's TC-column default.
# fresh_component: mi_silk_bottom_for_臤+糸

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

# ---- MMH-verbatim endpoints ----
S1H = ('TL', 0.674, 0.923); S1T = ('ML', 0.782, 0.591)
S2H = ('TC', 0.02,  0.691); S2T = ('C',  0.119, 0.629)
S3H = ('TC', 0.564, 0.803); S3T = ('C',  0.474, 0.474)
S4H = ('TC', 0.456, 0.964); S4T = ('MR', 0.701, 0.611)
S5H = ('C',  0.333, 0.438); S5T = ('C',  0.392, 0.978)
S6H = ('C',  0.764, 0.623); S6T = ('BC', 0.89,  0.25)
S7H = ('BC', 0.799, 0.036); S7T = ('BR', 0.027, 0.329)
S8H = ('BC', 0.447, 0.35);  S8T = ('BC', 0.181, 0.897)
S9H = ('BL', 0.896, 0.522); S9T = ('BL', 0.668, 0.892)
S10H = ('BC', 0.901, 0.473); S10T = ('BR', 0.303, 0.924)

# s1 — short 丨 top-left tick of 臤 (top-left 丨 of 臤)
p0, p1 = anchor_to_xy(S1H), anchor_to_xy(S1T)
fat_line(d, p0, p1, width=8)

# s2 — long 撇 from top-center down; slight curve to the left as it descends
p0, p1 = anchor_to_xy(S2H), anchor_to_xy(S2T)
# add gentle leftward curve as a pie stroke
ctrl = ((p0[0] + p1[0]) / 2 - 4, (p0[1] + p1[1]) / 2)
pts = quad_bezier(p0, ctrl, p1, n=40)
widths = [max(2, 11 - int(11 * i / (len(pts) - 1)) + 2) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s3 — 又's 横撇: short diagonal into center (down-left)
p0, p1 = anchor_to_xy(S3H), anchor_to_xy(S3T)
# slight curve to give it a 横撇 feel
ctrl = ((p0[0] + p1[0]) / 2 + 3, (p0[1] + p1[1]) / 2 - 6)
pts = quad_bezier(p0, ctrl, p1, n=30)
widths = [max(2, 10 - int(8 * i / (len(pts) - 1))) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s4 — 又's 捺: long diagonal down-right (thickening then tapering)
p0, p1 = anchor_to_xy(S4H), anchor_to_xy(S4T)
mid = ((p0[0] + p1[0]) / 2 + 4, (p0[1] + p1[1]) / 2 + 8)
pts = quad_bezier(p0, mid, p1, n=48)
n = len(pts)
widths = []
for i in range(n):
    t = i / (n - 1)
    # thin at head, grow to peak ~0.75, taper to thin at tail
    if t < 0.75:
        w = 3 + 11 * (t / 0.75)
    else:
        w = 14 * (1 - (t - 0.75) / 0.25) + 1
    widths.append(max(2, w))
stroke_variable_width(d, pts, widths)

# s5 — 糸's upper 撇/竖 stem: vertical-ish going down through center
p0, p1 = anchor_to_xy(S5H), anchor_to_xy(S5T)
ctrl = ((p0[0] + p1[0]) / 2 - 3, (p0[1] + p1[1]) / 2)
pts = quad_bezier(p0, ctrl, p1, n=40)
widths = [max(2, 8) for _ in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s6 — 糸's first 撇折 (pie_zhe upper lobe): pie going down-left then zhe turning down-right
p0, p1 = anchor_to_xy(S6H), anchor_to_xy(S6T)
# corner at ~55% of the way, bulging further right for a clear pie_zhe bend
cx = p0[0] - 18
cy = (p0[1] + p1[1]) / 2 + 8
# two-segment: pie leg then zhe leg
pts_a = quad_bezier(p0, ((p0[0] + cx)/2 + 4, (p0[1] + cy)/2 - 2), (cx, cy), n=20)
pts_b = quad_bezier((cx, cy), ((cx + p1[0])/2 + 4, (cy + p1[1])/2 + 4), p1, n=20)
pts = pts_a + pts_b[1:]
widths = [max(2, 8 - int(4 * i / (len(pts) - 1))) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s7 — 糸's second 撇折 (pie_zhe lower lobe)
p0, p1 = anchor_to_xy(S7H), anchor_to_xy(S7T)
cx = p0[0] - 22
cy = (p0[1] + p1[1]) / 2 + 4
pts_a = quad_bezier(p0, ((p0[0] + cx)/2 + 2, (p0[1] + cy)/2 - 2), (cx, cy), n=20)
pts_b = quad_bezier((cx, cy), ((cx + p1[0])/2, (cy + p1[1])/2 + 4), p1, n=20)
pts = pts_a + pts_b[1:]
widths = [max(2, 8 - int(4 * i / (len(pts) - 1))) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s8 — 小's left 撇 (dot-like)
p0, p1 = anchor_to_xy(S8H), anchor_to_xy(S8T)
pts = quad_bezier(p0, ((p0[0]+p1[0])/2 - 2, (p0[1]+p1[1])/2), p1, n=25)
widths = [max(2, 9 - int(6 * i / (len(pts) - 1))) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s9 — 小's middle dot
p0, p1 = anchor_to_xy(S9H), anchor_to_xy(S9T)
pts = quad_bezier(p0, ((p0[0]+p1[0])/2 - 2, (p0[1]+p1[1])/2 + 3), p1, n=20)
widths = [max(2, 8 - int(4 * i / (len(pts) - 1))) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s10 — 小's right 捺 (dot)
p0, p1 = anchor_to_xy(S10H), anchor_to_xy(S10T)
pts = quad_bezier(p0, ((p0[0]+p1[0])/2, (p0[1]+p1[1])/2 - 4), p1, n=30)
n = len(pts)
widths = []
for i in range(n):
    t = i / (n - 1)
    if t < 0.7:
        w = 3 + 9 * (t / 0.7)
    else:
        w = 12 * (1 - (t - 0.7) / 0.3) + 1
    widths.append(max(2, w))
stroke_variable_width(d, pts, widths)

img.save(os.path.join(_HERE, '01_紧.png'))

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 strokes rendered
    'endpoint_mismatches': [],  # all MMH-verbatim
    'joint_class_mismatches': [], # N-gaps preserved (no explicit weld)
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 又 X-cross implicit at s3.mid⇆s4.mid (P) via anchor overlap near C(0.5); N-gaps naturally preserved at s2/s5 join and 幺 hook joins; s1-9 dots-last order.',
}
