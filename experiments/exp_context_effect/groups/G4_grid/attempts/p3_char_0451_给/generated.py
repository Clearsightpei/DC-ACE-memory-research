# BANK_DEVIATION
# skipped: si_silk.py
# reason: si_silk defaults render standalone-width 纟 across cols; 给 needs a
#         compressed left-column 纟 whose 3 endpoints match the MMH anchors
#         (s1..s3) — 3+ anchor overrides violates never-tune-anchors rule.
# fresh_component: si_silk_left_for_给

"""给 (gěi) — Phase 3, 9 strokes.

Decomposition: 纟 (left radical, 3 strokes) + 合 (right, 6 strokes).
纟 strokes s1/s2 are compressed pie-zhe loops in the left column;
s3 is the 提. 合 = 亼 top (撇+捺+短横) + 口 bottom (竖+横折+横).
All 9 joints are N-class (small natural gaps).
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, fat_line,
                     stroke_variable_width, quad_bezier)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 9 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 9 joints implemented as N (natural gaps)
    'overall_pass': True,
    'notes': '给 = 纟(3) + 合(6). Inline fresh 纟 to match compressed left-radical anchors.',
}


# ---------------- local stroke primitives ----------------

def draw_pie(draw, head, tail, head_w=13, tail_w=2, curve=0.12, segments=44):
    p0 = anchor_to_xy(head); p2 = anchor_to_xy(tail)
    mx, my = (p0[0] + p2[0]) / 2.0, (p0[1] + p2[1]) / 2.0
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    nx, ny = -dy / L, dx / L  # bow outward (right)
    p1 = (mx + nx * curve * L, my + ny * curve * L)
    pts = quad_bezier(p0, p1, p2, n=segments)
    widths = [head_w + (tail_w - head_w) * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def draw_na(draw, head, tail, head_w=3, peak_w=14, tail_w=2,
            peak_t=0.82, curve=0.08, segments=44):
    p0 = anchor_to_xy(head); p2 = anchor_to_xy(tail)
    mx, my = (p0[0] + p2[0]) / 2.0, (p0[1] + p2[1]) / 2.0
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    nx, ny = dy / L, -dx / L  # bow opposite way
    p1 = (mx + nx * curve * L, my + ny * curve * L)
    pts = quad_bezier(p0, p1, p2, n=segments)
    widths = []
    n = len(pts) - 1
    for i in range(len(pts)):
        t = i / n
        if t < peak_t:
            w = head_w + (peak_w - head_w) * (t / peak_t)
        else:
            w = peak_w + (tail_w - peak_w) * ((t - peak_t) / (1 - peak_t))
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


def draw_pie_zhe(draw, head, pivot, tail,
                 pie_head_w=9, pie_tip_w=3, heng_w=6, segments=32):
    """撇折: pie curve head→pivot, then heng-like segment pivot→tail."""
    p0 = anchor_to_xy(head); pv = anchor_to_xy(pivot); p2 = anchor_to_xy(tail)
    # pie arc via slight curve
    mx, my = (p0[0] + pv[0]) / 2.0, (p0[1] + pv[1]) / 2.0
    dx, dy = pv[0] - p0[0], pv[1] - p0[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    nx, ny = -dy / L, dx / L
    curve = 0.10
    p1 = (mx + nx * curve * L, my + ny * curve * L)
    pts = quad_bezier(p0, p1, pv, n=segments)
    widths = [pie_head_w + (pie_tip_w - pie_head_w) * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)
    # heng flick pivot→tail (uniform)
    fat_line(draw, pv, p2, width=heng_w)


def draw_ti(draw, head, tail, head_w=12, tail_w=2, curve=0.06, segments=40):
    p0 = anchor_to_xy(head); p2 = anchor_to_xy(tail)
    mx, my = (p0[0] + p2[0]) / 2.0, (p0[1] + p2[1]) / 2.0
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    nx, ny = -dy / L, dx / L
    p1 = (mx + nx * curve * L, my + ny * curve * L)
    pts = quad_bezier(p0, p1, p2, n=segments)
    widths = [head_w + (tail_w - head_w) * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


# ---------------- render ----------------

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# 纟 (left radical, 3 strokes) — compressed left column
# --- s1  first 撇折 loop (top): head TL(0.782,0.706)  → tail ML(0.85,0.582)
# tighter pivot: keep the loop small and contained near the endpoints
draw_pie_zhe(draw,
             head=('TL', 0.782, 0.706),
             pivot=('TL', 0.62, 0.90),
             tail=('ML', 0.85, 0.582),
             pie_head_w=7, pie_tip_w=2, heng_w=4)

# --- s2  second 撇折 loop (middle): head C(0.075,0.146) → tail C(0.087,0.942)
# tighter pivot in ML cell so the loop stays compact
draw_pie_zhe(draw,
             head=('C', 0.075, 0.146),
             pivot=('ML', 0.90, 0.60),
             tail=('C', 0.087, 0.942),
             pie_head_w=8, pie_tip_w=2, heng_w=5)

# --- s3  提 (rising flick): head BL(0.319,0.613) → tail BC(0.189,0.235)
draw_ti(draw,
        head=('BL', 0.319, 0.613),
        tail=('BC', 0.189, 0.235),
        head_w=12, tail_w=2, curve=0.05)

# 合 (right, 6 strokes)
# --- s4  撇 (roof left of 亼): head TC(0.705,0.686) → tail C(0.245,0.995)
draw_pie(draw, ('TC', 0.705, 0.686), ('C', 0.245, 0.995),
         head_w=13, tail_w=2, curve=0.05)

# --- s5  捺 (roof right of 亼): head C(0.875,0.081) → tail MR(0.921,0.863)
draw_na(draw, ('C', 0.875, 0.081), ('MR', 0.921, 0.863),
        head_w=3, peak_w=14, tail_w=2, peak_t=0.82, curve=0.08)

# --- s6  短横 (middle bar of 亼): head C(0.465,0.881) → tail MR(0.112,0.784)
p6h = anchor_to_xy(('C', 0.465, 0.881))
p6t = anchor_to_xy(('MR', 0.112, 0.784))
fat_line(draw, p6h, p6t, width=8)

# --- s7  竖 (口 left wall): head BC(0.318,0.206) → tail BC(0.535,0.933)
p7h = anchor_to_xy(('BC', 0.318, 0.206))
p7t = anchor_to_xy(('BC', 0.535, 0.933))
fat_line(draw, p7h, p7t, width=8)

# --- s8  横折 (口 top bar + right wall): head BC(0.479,0.218) → tail BR(0.071,0.572)
# MMH gives head/tail of compound stroke; synthesize the corner so top is horizontal
# and right wall is vertical.
p8h = anchor_to_xy(('BC', 0.479, 0.218))
p8t = anchor_to_xy(('BR', 0.071, 0.572))
p8c = (p8t[0], p8h[1])  # corner: top-right of 口
fat_line(draw, p8h, p8c, width=8)   # top bar
fat_line(draw, p8c, p8t, width=8)   # right wall
# reinforcing ink dot at the fold
cx, cy = p8c
draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(0, 0, 0))

# --- s9  横 (口 bottom bar): head BC(0.582,0.716) → tail BR(0.268,0.684)
p9h = anchor_to_xy(('BC', 0.582, 0.716))
p9t = anchor_to_xy(('BR', 0.268, 0.684))
fat_line(draw, p9h, p9t, width=8)

out = os.path.join(os.path.dirname(__file__), '01_给.png')
img.save(out)
print('wrote', out)
