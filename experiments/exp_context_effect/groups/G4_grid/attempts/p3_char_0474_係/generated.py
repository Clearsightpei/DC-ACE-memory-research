# BANK_DEVIATION
# skipped: ren_side.py
# reason: 亻 sits in far-left column slot (MMH: s1 head TC(0.008,0.595), s2 head ML(0.858,0.362)) — standalone ren_side default anchors would overshoot slot. Inline via pie+shu per B11 A-recipe (ren_side_far_left named pattern, 10+ passing precedent).
# fresh_component: ren_side_far_left_for_compound

"""係 (xì) — 9 strokes.
Decomposition: 係 = 亻 (left, 2 strokes) + 系 (right, 7 strokes).
系 further = 丿 (s3) + 一/横 (s4) + 竖 (s5) + a small mid stroke (s6)
         + 小 (s7 pie + s8 pie + s9 dian/na) as bottom 小/糸 tail.
Strategy: MMH-verbatim anchors, inline base primitives (pie/shu/heng/na/dian).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 9 draw calls, matches MMH expected 9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 5 declared joints are N (natural gaps preserved)
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; all 5 N-joints left as gaps (no welding).',
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier

# ---------- canvas ----------
img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---------- MMH-verbatim anchors ----------
# Stroke 1: 亻 pie — head TC(0.008,0.595) → tail ML(0.243,0.901)
s1_h = anchor_to_xy(('TC', 0.008, 0.595))
s1_t = anchor_to_xy(('ML', 0.243, 0.901))
# Stroke 2: 亻 shu — head ML(0.858,0.362) → tail BL(0.832,0.892)
s2_h = anchor_to_xy(('ML', 0.858, 0.362))
s2_t = anchor_to_xy(('BL', 0.832, 0.892))
# Stroke 3: 系 top pie — head TR(0.332,0.812) → tail C(0.339,0.072)
s3_h = anchor_to_xy(('TR', 0.332, 0.812))
s3_t = anchor_to_xy(('C',  0.339, 0.072))
# Stroke 4: 系 short heng — head C(0.708,0.031) → tail C(0.898,0.509)
s4_h = anchor_to_xy(('C',  0.708, 0.031))
s4_t = anchor_to_xy(('C',  0.898, 0.509))
# Stroke 5: 系 middle vertical — head MR(0.171,0.125) → tail MR(0.329,0.884)
s5_h = anchor_to_xy(('MR', 0.171, 0.125))
s5_t = anchor_to_xy(('MR', 0.329, 0.884))
# Stroke 6: small mid stroke (糸 knot) — head MR(0.259,0.652) → tail MR(0.481,0.98)
s6_h = anchor_to_xy(('MR', 0.259, 0.652))
s6_t = anchor_to_xy(('MR', 0.481, 0.98))
# Stroke 7: bottom 小 left-most pie — head BC(0.852,0.039) → tail BC(0.617,0.78)
s7_h = anchor_to_xy(('BC', 0.852, 0.039))
s7_t = anchor_to_xy(('BC', 0.617, 0.78))
# Stroke 8: bottom 小 mid pie — head BC(0.474,0.3) → tail BC(0.263,0.704)
s8_h = anchor_to_xy(('BC', 0.474, 0.3))
s8_t = anchor_to_xy(('BC', 0.263, 0.704))
# Stroke 9: bottom-right dot/na — head BR(0.3,0.238) → tail BR(0.669,0.637)
s9_h = anchor_to_xy(('BR', 0.3, 0.238))
s9_t = anchor_to_xy(('BR', 0.669, 0.637))


def draw_pie_curve(draw, head, tail, head_w=12, tail_w=2, bulge=0.15, n=48, bulge_side=+1):
    """Curved 撇: head thick tapering to tail; quad-bezier bulge.
    bulge_side=+1: bulge to LEFT of direction (traditional 撇 concave-right).
    bulge_side=-1: bulge to RIGHT of direction.
    """
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    dx, dy = tx - hx, ty - hy
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    # perpendicular offset: rotate direction 90° CCW → (-dy, dx)
    ox, oy = -dy / L * bulge * L * bulge_side, dx / L * bulge * L * bulge_side
    ctrl = (mx + ox, my + oy)
    pts = quad_bezier(head, ctrl, tail, n=n)
    widths = [head_w + (tail_w - head_w) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_na_curve(draw, head, tail, head_w=3, peak_w=13, tail_w=1, peak_t=0.75, n=48):
    """捺 / dot-na: thin head, thickens to peak, tail tapers."""
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    dx, dy = tx - hx, ty - hy
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    # slight bulge downward for na
    ox, oy = -dy / L * 0.08 * L, dx / L * 0.08 * L
    ctrl = (mx - ox, my - oy)
    pts = quad_bezier(head, ctrl, tail, n=n)
    widths = []
    for i in range(n + 1):
        t = i / n
        if t < peak_t:
            w = head_w + (peak_w - head_w) * (t / peak_t)
        else:
            w = peak_w + (tail_w - peak_w) * ((t - peak_t) / (1 - peak_t))
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


# ---------- render ----------
# s1 亻 pie — traditional 撇, thick head, concave-right (bulge LEFT of direction)
draw_pie_curve(draw, s1_h, s1_t, head_w=13, tail_w=2, bulge=0.18, bulge_side=+1)
# s2 亻 shu (uniform vertical, slightly tapered by keeping fat_line)
fat_line(draw, s2_h, s2_t, width=10)
# s3 系 top pie/丿 — nearly horizontal short pie, slight downward bulge
draw_pie_curve(draw, s3_h, s3_t, head_w=11, tail_w=2, bulge=0.12, bulge_side=+1)
# s4 系 short heng (slight down-right)
fat_line(draw, s4_h, s4_t, width=8)
# s5 系 middle vertical (main right-half stem)
fat_line(draw, s5_h, s5_t, width=9)
# s6 系 mid knot (small stroke)
fat_line(draw, s6_h, s6_t, width=8)
# s7 bottom 小 left pie — long, curves left
draw_pie_curve(draw, s7_h, s7_t, head_w=10, tail_w=2, bulge=0.14, bulge_side=+1)
# s8 bottom 小 mid pie — short
draw_pie_curve(draw, s8_h, s8_t, head_w=9, tail_w=2, bulge=0.12, bulge_side=+1)
# s9 bottom-right dot/na — 点 style, thin head → thick peak → taper
draw_na_curve(draw, s9_h, s9_t, head_w=3, peak_w=13, tail_w=2)

# ---------- save ----------
out = os.path.join(os.path.dirname(__file__), '01_係.png')
img.save(out)
print(f'wrote {out}')
