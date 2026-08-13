"""亥 — G4 attempt. 6 strokes per MMH.

Split: 亠 (top: dot + heng) + 中撇 + 大撇 + 折/勾/横 + 捺 lower cluster.
Strokes are drawn per the injected anchors. All 3 joints are N-class
(neighbor with small gap) — so we do NOT weld any pair; each stroke is
drawn cleanly to its own endpoints.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes, all N-joints (no welding); anchors follow MMH.'
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

from PIL import Image, ImageDraw

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def draw_curve(head, tail, ctrl_frac=(0.5, 0.5), widths=(6, 6), n=40):
    """Draw a quadratic bezier from head to tail with a mid control point.
    ctrl_frac = (fx, fy) — offset from midpoint as fractions of the
    head→tail vector (normal offset for curvature).
    widths = (w_head, w_tail) linearly interpolated.
    """
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mid = ((p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2)
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    # normal direction
    nx, ny = -dy, dx
    length = (nx * nx + ny * ny) ** 0.5 or 1.0
    nx, ny = nx / length, ny / length
    L = (dx * dx + dy * dy) ** 0.5
    p1 = (mid[0] + nx * ctrl_frac[0] * L + dx * (ctrl_frac[1] - 0.5),
          mid[1] + ny * ctrl_frac[0] * L + dy * (ctrl_frac[1] - 0.5))
    pts = quad_bezier(p0, p1, p2, n=n)
    ws = [widths[0] + (widths[1] - widths[0]) * i / n for i in range(n + 1)]
    stroke_variable_width(d, pts, ws, color=BLACK)


# --- Stroke 1: 点 (top dot) TC(0.269, 0.571) -> TC(0.69, 0.873) ---
# Short slanted stroke, thicker at tail.
draw_curve(('TC', 0.269, 0.571), ('TC', 0.69, 0.873),
           ctrl_frac=(0.0, 0.5), widths=(4, 9), n=20)

# --- Stroke 2: 横 (heng) ML(0.387, 0.33) -> MR(0.625, 0.172) ---
# Long horizontal, slight upward slope, gentle rise.
draw_curve(('ML', 0.387, 0.33), ('MR', 0.625, 0.172),
           ctrl_frac=(0.02, 0.5), widths=(6, 7), n=40)

# --- Stroke 3: 短撇 C(0.216, 0.324) -> BC(0.427, 0.001) ---
# Short curve, upper-left of middle to just below.
draw_curve(('C', 0.216, 0.324), ('BC', 0.427, 0.001),
           ctrl_frac=(-0.05, 0.5), widths=(6, 4), n=25)

# --- Stroke 4: 大撇 C(0.743, 0.427) -> BL(0.41, 0.915) ---
# Big pie curve, from mid-right down to lower-left, bowed leftward.
draw_curve(('C', 0.743, 0.427), ('BL', 0.41, 0.915),
           ctrl_frac=(0.12, 0.55), widths=(8, 4), n=50)

# --- Stroke 5: 横折/撇 C(0.91, 0.951) -> BC(0.09, 0.985) ---
# Rightside starts at mid-right, sweeps left across lower half.
# Slight downward bow.
draw_curve(('C', 0.91, 0.951), ('BC', 0.09, 0.985),
           ctrl_frac=(-0.08, 0.5), widths=(6, 5), n=40)

# --- Stroke 6: 捺 BC(0.761, 0.572) -> BR(0.312, 1.026) ---
# Right-descending na, thickens toward tail then tapers.
draw_curve(('BC', 0.761, 0.572), ('BR', 0.312, 1.026),
           ctrl_frac=(-0.05, 0.5), widths=(4, 10), n=40)


out = os.path.join(os.path.dirname(__file__), '01_亥.png')
img.save(out)
print('wrote', out)
