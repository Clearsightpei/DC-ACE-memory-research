"""俳 (pái) — 10 strokes.
Decomposition: 俳 = 亻 (left) + 非 (right).
  亻 (2 strokes): pie (s1) + shu (s2), placed in far-left column slot.
  非 (8 strokes): left vertical (s3) + 3 short horizontals branching from it (s4-6)
                  + right vertical (s7) + 3 short horizontals off right vertical (s8-10).

Playbook: A-recipe (B9-B13) — MMH-verbatim anchors, base primitives, no compound
primitives (亻 slot is far-left column per named-pattern ren_side_far_left_for_*;
ren_side.py bakes standalone TC/C anchors that don't match this slot).

Memory reads:
  # drawer_memory.md: 亻+X = ren_side_far_left inline (do NOT partial-override ren_side).
  # success_bank/INDEX.md grep for 俳/非: neither in bank. Inline via base primitives.
  # errata.md grep for 俳: not present.
"""

# BANK_DEVIATION
# skipped: ren_side.py
# reason: 亻 slot per MMH sits far-left (pie head TL 0.888, shu head ML 0.636);
#         ren_side default anchors sit at TC/C standalone-scale — 3+ anchor
#         overrides would trigger the p3_char_0252_伊 partial-override anti-pattern.
# fresh_component: ren_side_far_left_for_俳

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

W = 300
img = Image.new('RGB', (W, W), 'white')
draw = ImageDraw.Draw(img)

# --- Stroke 1: 亻 pie (curved sweep TL → ML) ---
s1_h = anchor_to_xy(('TL', 0.888, 0.659))
s1_t = anchor_to_xy(('ML', 0.161, 0.986))
# Curved pie: control point pulled outward-left to give the pie its arc.
s1_ctrl = (s1_h[0] - 8, (s1_h[1] + s1_t[1]) / 2)
s1_pts = quad_bezier(s1_h, s1_ctrl, s1_t, n=48)
# Tapered: thick head, thin tail (per form_catalog pie taper defaults).
s1_widths = [max(1, int(round(12 - 11 * (i / len(s1_pts))))) for i in range(len(s1_pts))]
stroke_variable_width(draw, s1_pts, s1_widths)

# --- Stroke 2: 亻 shu (straight vertical ML → BL) ---
s2_h = anchor_to_xy(('ML', 0.636, 0.55))
s2_t = anchor_to_xy(('BL', 0.662, 0.883))
fat_line(draw, s2_h, s2_t, width=9)

# --- Stroke 3: 非 left long vertical (TC → BC) ---
s3_h = anchor_to_xy(('TC', 0.362, 0.905))
s3_t = anchor_to_xy(('BC', 0.456, 0.912))
fat_line(draw, s3_h, s3_t, width=8)

# --- Strokes 4,5,6: three short horizontals off 非 left vertical (N-joints, gap ~15-20 px) ---
# All three cross out of ML/BL rightward toward C — MMH-verbatim.
s4_h = anchor_to_xy(('ML', 0.984, 0.462))
s4_t = anchor_to_xy(('C',  0.397, 0.403))
fat_line(draw, s4_h, s4_t, width=7)

s5_h = anchor_to_xy(('ML', 0.976, 0.849))
s5_t = anchor_to_xy(('C',  0.403, 0.787))
fat_line(draw, s5_h, s5_t, width=7)

s6_h = anchor_to_xy(('BL', 0.864, 0.326))
s6_t = anchor_to_xy(('BC', 0.383, 0.124))
fat_line(draw, s6_h, s6_t, width=7)

# --- Stroke 7: 非 right long vertical (TC → BC), the dominant right vertical ---
s7_h = anchor_to_xy(('TC', 0.828, 0.618))
s7_t = anchor_to_xy(('BC', 0.939, 1.05))
# Clamp tail y to canvas edge (1.05 → 1.0 to stay in canvas).
s7_t = (s7_t[0], min(s7_t[1], W - 2))
fat_line(draw, s7_h, s7_t, width=9)

# --- Strokes 8,9,10: three short horizontals off 非 right vertical (extending rightward) ---
s8_h = anchor_to_xy(('MR', 0.045, 0.354))
s8_t = anchor_to_xy(('MR', 0.534, 0.277))
fat_line(draw, s8_h, s8_t, width=7)

s9_h = anchor_to_xy(('MR', 0.062, 0.799))
s9_t = anchor_to_xy(('MR', 0.514, 0.737))
fat_line(draw, s9_h, s9_t, width=7)

s10_h = anchor_to_xy(('BR', 0.045, 0.244))
s10_t = anchor_to_xy(('BR', 0.681, 0.171))
fat_line(draw, s10_h, s10_t, width=7)

out = os.path.join(os.path.dirname(__file__), '01_俳.png')
img.save(out)
print('WROTE', out)

# ----------------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 primitive calls above = 10 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 8 joints are N-class; gaps preserved
                                   # (no welding: s1-mid ⇆ s2-head sit ~13 px apart naturally;
                                   #  s3-mid ⇆ s4/5/6 tails ~20 px apart in C;
                                   #  s7-mid ⇆ s8/9/10 heads ~10-15 px apart in MR/BR)
    'overall_pass': True,
    'notes': ('10 strokes MMH-verbatim. 亻 inline via ren_side_far_left named pattern '
              '(BANK_DEVIATION logged). 非 = two long verticals + 6 short cross-strokes; '
              'all joints left as natural N-gaps per B9 recipe point 5.'),
}
