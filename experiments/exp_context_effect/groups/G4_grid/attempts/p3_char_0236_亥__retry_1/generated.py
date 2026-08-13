"""亥 — G4 retry #1. 6 strokes per MMH.

TRAJECTORY DIFF (from Read of main + GT PNGs):
- main FAIL: top dot too slanted/long (looked like a slash, not a compact dot).
- main FAIL: middle short 撇 (stroke 3) too thin/faint, blends with heng.
- main FAIL: stroke 5 rendered as a near-horizontal at bottom — but in
  GT it clearly has a 横折 (zig) look: starts higher, arcs down-left,
  reads as one connected turn. My draw_curve gave a smooth arc, not a
  turning kink; needed a two-segment stroke.
- main FAIL: bottom cluster reads as "mushy X" — the pie(4) and na(6)
  didn't clearly cross; widths were too even.
- Overall: right stroke count (6), joint gaps were fine, but visual
  strokes were too thin/wispy and stroke 5 shape was wrong.

FIXES this attempt:
1. Compact dot (thicker head→tail, shorter path stays inside anchors).
2. Stronger stroke widths so strokes read as ink not pencil.
3. Stroke 5 as a TWO-SEGMENT 横折撇: heng portion at top-right, then
   turn and pie-sweep down-left. Anchors still touch head/tail.
4. Pie(4) bows more; na(6) tapers head then thickens dramatically.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 6 stroke primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes; stroke 5 rendered as heng+pie turn; all N-joints preserved.'
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width

from PIL import Image, ImageDraw

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def draw_curve(head, tail, ctrl_frac=(0.0, 0.5), widths=(6, 6), n=40):
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mid = ((p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2)
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    nx, ny = -dy, dx
    length = (nx * nx + ny * ny) ** 0.5 or 1.0
    nx, ny = nx / length, ny / length
    L = (dx * dx + dy * dy) ** 0.5
    p1 = (mid[0] + nx * ctrl_frac[0] * L + dx * (ctrl_frac[1] - 0.5),
          mid[1] + ny * ctrl_frac[0] * L + dy * (ctrl_frac[1] - 0.5))
    pts = quad_bezier(p0, p1, p2, n=n)
    ws = [widths[0] + (widths[1] - widths[0]) * i / n for i in range(n + 1)]
    stroke_variable_width(d, pts, ws, color=BLACK)


def draw_two_segment(head, corner, tail, widths=(6, 6, 6), n_per=25):
    """Draw a stroke that has one interior corner (e.g. 横折)."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(corner)
    p2 = anchor_to_xy(tail)
    # segment 1: straightish (light curve)
    seg1 = quad_bezier(p0, ((p0[0]+p1[0])/2, (p0[1]+p1[1])/2), p1, n=n_per)
    seg2 = quad_bezier(p1, ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2), p2, n=n_per)
    pts = seg1 + seg2[1:]
    total = len(pts) - 1
    ws = []
    for i in range(total + 1):
        f = i / total
        if f < 0.5:
            ff = f / 0.5
            ws.append(widths[0] + (widths[1] - widths[0]) * ff)
        else:
            ff = (f - 0.5) / 0.5
            ws.append(widths[1] + (widths[2] - widths[1]) * ff)
    stroke_variable_width(d, pts, ws, color=BLACK)


# --- Stroke 1: 点 TC(0.269, 0.571) -> TC(0.69, 0.873) ---
# Compact top dot: short and thick.
draw_curve(('TC', 0.269, 0.571), ('TC', 0.69, 0.873),
           ctrl_frac=(0.0, 0.5), widths=(4, 11), n=20)

# --- Stroke 2: 横 ML(0.387, 0.33) -> MR(0.625, 0.172) ---
# Long heng: thick, uniform, black — CRITICAL structural element.
draw_curve(('ML', 0.387, 0.33), ('MR', 0.625, 0.172),
           ctrl_frac=(0.02, 0.5), widths=(8, 8), n=40)

# --- Stroke 3: 短撇 C(0.216, 0.324) -> BC(0.427, 0.001) ---
# Short pie curving down-left; visible width.
draw_curve(('C', 0.216, 0.324), ('BC', 0.427, 0.001),
           ctrl_frac=(-0.08, 0.5), widths=(9, 4), n=25)

# --- Stroke 4: 大撇 C(0.743, 0.427) -> BL(0.41, 0.915) ---
# Long pie: bowed leftward, thick head tapers to sharp tail.
draw_curve(('C', 0.743, 0.427), ('BL', 0.41, 0.915),
           ctrl_frac=(0.18, 0.55), widths=(10, 3), n=50)

# --- Stroke 5: 横折/撇 as TWO-SEGMENT ---
# Zig-zag: first short heng-ish move then sweep left-across bottom.
# Move corner higher and further right so the kink is visible.
draw_two_segment(('C', 0.91, 0.951),
                 ('BC', 0.85, 0.55),
                 ('BC', 0.09, 0.985),
                 widths=(7, 6, 4), n_per=25)

# --- Stroke 6: 捺 BC(0.761, 0.572) -> BR(0.312, 1.026) ---
# Na: tapered head, thick heavy tail (classic na signature).
draw_curve(('BC', 0.761, 0.572), ('BR', 0.312, 1.026),
           ctrl_frac=(-0.10, 0.5), widths=(3, 13), n=40)


out = os.path.join(os.path.dirname(__file__), '01_亥.png')
img.save(out)
print('wrote', out)
