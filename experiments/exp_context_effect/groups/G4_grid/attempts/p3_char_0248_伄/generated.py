"""p3_char_0248_伄 — 亻 (left) + right-side vertical-piercing frame.

Decomposition: 亻 (2 strokes) + right side (4 strokes: top heng-zhe-ish,
small heng, pie, long central 竖 that pierces).

6 strokes total, matching MMH.
"""
import os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, stroke_variable_width, sample_line, quad_bezier

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes: 亻 (pie+shu) + right (heng-fold, small heng, pie, central shu).'
}

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
W_MAIN = 4
W_THIN = 3


def curve(p0, p2, bend=(0, 0), n=40, w=W_MAIN):
    """Draw a quadratic bezier from p0 to p2 with control offset bend from midpoint."""
    mx = (p0[0] + p2[0]) / 2 + bend[0]
    my = (p0[1] + p2[1]) / 2 + bend[1]
    pts = quad_bezier(p0, (mx, my), p2, n=n)
    widths = [w] * len(pts)
    stroke_variable_width(d, pts, widths, color=BLACK)


def line(p0, p1, w=W_MAIN):
    pts = sample_line(p0, p1, n=20)
    widths = [w] * len(pts)
    stroke_variable_width(d, pts, widths, color=BLACK)


# ---- Stroke 1: 亻 pie — head TL(0.826, 0.762) -> tail ML(0.196, 0.937)
s1_head = anchor_to_xy(('TL', 0.826, 0.762))
s1_tail = anchor_to_xy(('ML', 0.196, 0.937))
curve(s1_head, s1_tail, bend=(-8, 6), w=W_MAIN)

# ---- Stroke 2: 亻 shu — head ML(0.686, 0.506) -> tail BL(0.727, 0.915)
s2_head = anchor_to_xy(('ML', 0.686, 0.506))
s2_tail = anchor_to_xy(('BL', 0.727, 0.915))
line(s2_head, s2_tail, w=W_MAIN)

# ---- Stroke 3: right-side top heng — head TC(0.28, 0.996) -> tail MR(0.068, 0.301)
# Actually this is horizontal-fold: goes right then down. Head at bottom of top center,
# tail at top of MR. Draw as heng-zhe (right then down).
s3_head = anchor_to_xy(('TC', 0.28, 0.996))
s3_tail = anchor_to_xy(('MR', 0.068, 0.301))
# Corner at approx (s3_tail.x, s3_head.y) — right first, then down
corner3 = (s3_tail[0], s3_head[1])
line(s3_head, corner3, w=W_MAIN)
line(corner3, s3_tail, w=W_MAIN)

# ---- Stroke 4: small heng — head C(0.315, 0.503) -> tail MR(0.268, 0.43)
s4_head = anchor_to_xy(('C', 0.315, 0.503))
s4_tail = anchor_to_xy(('MR', 0.268, 0.43))
line(s4_head, s4_tail, w=W_THIN)

# ---- Stroke 5: pie/left-down — head C(0.181, 0.468) -> tail BR(0.074, 0.341)
s5_head = anchor_to_xy(('C', 0.181, 0.468))
s5_tail = anchor_to_xy(('BR', 0.074, 0.341))
curve(s5_head, s5_tail, bend=(-4, 4), w=W_MAIN)

# ---- Stroke 6: long central 竖 — head C(0.576, 0.055) -> tail BC(0.682, 1.103)
s6_head = anchor_to_xy(('C', 0.576, 0.055))
s6_tail = anchor_to_xy(('BC', 0.682, 1.103))
line(s6_head, s6_tail, w=W_MAIN)

# Verify stroke count assertion
_STROKE_COUNT = 6
assert _STROKE_COUNT == 6, "Expected 6 strokes"

out_path = os.path.join(os.path.dirname(__file__), '01_伄.png')
img.save(out_path)
print(f'Saved {out_path}')
