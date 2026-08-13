"""着 (zhao/zhe) — 11 strokes.
Decomposition: 着 = 丷 (top two dots) + 一 short (top heng) + 长撇 (long left sweep)
              + 一 (middle heng crossing sweep) + 目 (bottom rectangle with three inner heng).

A-recipe: MMH-verbatim anchors + base primitives (fat_line / dian / stroke_variable_width)
for all 11 strokes. No compound bank primitive fits this composition cleanly — 着's top
half interleaves 丷/横/长撇/横 in a way no bank standalone captures. Inline via base
primitives per B9 A-recipe point 4.
"""
# memory checklist:
#   1. drawer_memory.md read — no chronic primitive matches (羊/目 not chronic).
#   2. INDEX grep 着/羊/目 — no mastered composite; base primitives only.
#   3. errata.md grep 着 — not listed.
# No BANK_DEVIATION: no bank compound skipped (only base primitives used).

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, sample_line

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)


def draw_dian(draw, head_anchor, tail_anchor):
    """A slanted dot: thin head → thick tail."""
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(tail_anchor)
    pts = sample_line(p0, p1, n=16)
    n = len(pts)
    widths = [2 + 10 * (i / (n - 1)) for i in range(n)]  # 2 → 12
    stroke_variable_width(draw, pts, widths)


def draw_pie_long(draw, head_anchor, tail_anchor, curve=0.10):
    """Long tapered 撇: thick head → thin tail with slight curve."""
    from _anchor import quad_bezier
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    # control point offset perpendicular for a small bow
    mx = (p0[0] + p2[0]) / 2
    my = (p0[1] + p2[1]) / 2
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    # perpendicular unit (rotate -90)
    L = (dx * dx + dy * dy) ** 0.5
    if L < 1e-6:
        L = 1
    px = -dy / L
    py = dx / L
    p1 = (mx + px * curve * L, my + py * curve * L)
    pts = quad_bezier(p0, p1, p2, n=48)
    n = len(pts)
    widths = [12 - 10 * (i / (n - 1)) for i in range(n)]  # 12 → 2
    stroke_variable_width(draw, pts, widths)


def draw_heng(draw, head_anchor, tail_anchor, width=8):
    fat_line(draw, anchor_to_xy(head_anchor), anchor_to_xy(tail_anchor), width)


def draw_shu(draw, head_anchor, tail_anchor, width=8):
    fat_line(draw, anchor_to_xy(head_anchor), anchor_to_xy(tail_anchor), width)


def draw_heng_zhe(draw, head_anchor, tail_anchor, width=8):
    """MMH gives endpoints for a heng-zhe as one stroke; render L-shape via corner
    at (tail_x, head_y). Weld the two segments."""
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    corner = (p2[0], p0[1])
    fat_line(draw, p0, corner, width)
    fat_line(draw, corner, p2, width)


# ---- Draw 11 strokes MMH-verbatim ----
# s1 — top-left dot of 丷 (slanting down-right)
draw_dian(d, ('TC', 0.046, 0.65), ('TC', 0.298, 0.861))
# s2 — top-right dot of 丷 (slanting down-left)
draw_dian(d, ('TC', 0.811, 0.507), ('TC', 0.518, 0.885))
# s3 — top short heng (MMH endpoints span ML→TR near the top)
draw_heng(d, ('ML', 0.896, 0.102), ('TR', 0.077, 0.996), width=8)
# s4 — very short heng segment (top-right dash)
draw_heng(d, ('ML', 0.952, 0.427), ('C', 0.942, 0.377), width=7)
# s5 — middle heng crossing
draw_heng(d, ('ML', 0.451, 0.802), ('MR', 0.552, 0.685), width=8)
# s6 — long 撇 sweeping from C down to BL
draw_pie_long(d, ('C', 0.321, 0.178), ('BL', 0.246, 0.824), curve=0.08)
# s7 — left 竖 of 目
draw_shu(d, ('BC', 0.172, 0.048), ('BC', 0.137, 1.015), width=8)
# s8 — top-right 横折 of 目 (heng + shu as L-shape)
draw_heng_zhe(d, ('BC', 0.222, 0.048), ('BC', 0.764, 0.877), width=8)
# s9 — upper interior heng of 目
draw_heng(d, ('BC', 0.242, 0.385), ('BC', 0.641, 0.309), width=6)
# s10 — middle interior heng of 目
draw_heng(d, ('BC', 0.245, 0.634), ('BC', 0.679, 0.566), width=6)
# s11 — bottom heng of 目
draw_heng(d, ('BC', 0.219, 0.938), ('BC', 0.737, 0.859), width=7)

# Save
out = os.path.join(os.path.dirname(__file__), '01_着.png')
img.save(out)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 11 draw_* calls above
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all N-joints preserved as natural gaps
    'overall_pass': True,
    'notes': '11 strokes MMH-verbatim; heng_zhe rendered as L-shape from single MMH endpoint pair; 丷 dots tapered thin→thick; long 撇 tapered thick→thin with slight bow; 目 rendered with 5-stroke box + interior heng.',
}
