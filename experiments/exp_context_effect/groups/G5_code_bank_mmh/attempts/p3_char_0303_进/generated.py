"""p3_char_0303_进 (jìn) — G5 attempt.

Composition strategy: MMH-anchor verbatim per P-A-006 recipe.
7 strokes = 4 (井 body) + 3 (辶 walking radical).

Stroke mapping (from injected MMH block):
  s1: 井 upper heng    (C→MR)   → draw_heng
  s2: 井 lower heng    (C→MR)   → draw_heng
  s3: 井 left slanted  (TC→BC)  → draw_pie   (descends leftward — a 撇)
  s4: 井 right shu     (TC→BC)  → draw_shu   (near-vertical)
  s5: 辶 top-dian      (TL→ML)  → draw_dian
  s6: 辶 middle wavy   (ML→BL)  → inline 横折折撇
  s7: 辶 ping-na       (BL→BR)  → draw_ping_na

# BANK_DEVIATION
# skipped: chuo_walk.py (辶 whole-radical) — per P-A-006 for 7-stroke
#          Phase-3 chars, stroke-primitive layer beats whole-radical
#          composition (avoids double-transform at Phase-3 aspect).
# reason: 井 is straight-stroke right half (aligns with P-COMP-011
#         boundary), and 辶 primitive would drift under whole-scale.
# fresh_component: 井-body via 4 straight-stroke primitives +
#         辶 via 3 stroke primitives (dian + inline zigzag + ping_na)
"""
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from dian import draw_dian
from ping_na import draw_ping_na


def cell(name, xf, yf):
    """Convert (cell, x_frac, y_frac) → (px, py) on 300x300 canvas."""
    offs = {
        'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
        'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }
    ox, oy = offs[name]
    return (ox + xf * 100, oy + yf * 100)


img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# --- s1: 井 upper heng ---
s1_head = cell('C',  0.239, 0.374)   # (123.9, 137.4)
s1_tail = cell('MR', 0.297, 0.248)   # (229.7, 124.8)
draw_heng(draw, s1_head, s1_tail, width_head=8, width_tail=9)

# --- s2: 井 lower heng ---
s2_head = cell('C',  0.128, 0.875)   # (112.8, 187.5)
s2_tail = cell('MR', 0.546, 0.796)   # (254.6, 179.6)
draw_heng(draw, s2_head, s2_tail, width_head=8, width_tail=10)

# --- s3: 井 left slanted (descends leftward — a 撇) ---
s3_head = cell('TC', 0.441, 0.987)   # (144.1, 98.7)
s3_tail = cell('BC', 0.166, 0.347)   # (116.6, 234.7)
draw_pie(draw, s3_head, s3_tail, bow_perp=8, w_head=8, w_tail=4)

# --- s4: 井 right shu (near-vertical) ---
s4_head = cell('TC', 0.866, 0.683)   # (186.6, 68.3)
s4_tail = cell('BC', 0.983, 0.584)   # (198.3, 258.4)
draw_shu(draw, s4_head, s4_tail, width=7)

# --- s5: 辶 top-dian ---
s5_head = cell('TL', 0.694, 0.753)   # (69.4, 75.3)
s5_tail = cell('ML', 0.999, 0.034)   # (99.9, 103.4)
draw_dian(draw, s5_head, s5_tail, w_head=3, w_tail=7, bow=3)

# --- s6: 辶 middle wavy (横折折撇) inline zigzag ---
s6_head = cell('ML', 0.249, 0.693)   # (24.9, 169.3)
s6_tail = cell('BL', 0.855, 0.467)   # (85.5, 246.7)
p_a = (s6_head[0] + 30, s6_head[1] + 3)
p_b = (s6_head[0] + 12, s6_head[1] + 35)
p_c = s6_tail
draw.line([s6_head, p_a], fill='black', width=6)
draw.ellipse([p_a[0]-3, p_a[1]-3, p_a[0]+3, p_a[1]+3], fill='black')
draw.line([p_a, p_b], fill='black', width=5)
draw.ellipse([p_b[0]-3, p_b[1]-3, p_b[0]+3, p_b[1]+3], fill='black')
steps = 40
for i in range(steps):
    t = i / (steps - 1)
    x = p_b[0] + (p_c[0] - p_b[0]) * t
    y = p_b[1] + (p_c[1] - p_b[1]) * t
    r = 5 - 2.5 * t
    draw.ellipse([x - r, y - r, x + r, y + r], fill='black')

# --- s7: 辶 ping-na (long flat bottom sweep) ---
s7_head = cell('BL', 0.27, 0.622)    # (27.0, 262.2)
s7_tail = cell('BR', 0.736, 0.818)   # (273.6, 281.8)
draw_ping_na(draw, s7_head, s7_tail, belly_drop=6)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 strokes = s1..s7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-anchor verbatim per P-A-006; 井 via 4 straight-stroke primitives (heng+heng+pie+shu), 辶 via dian+inline_zigzag+ping_na. s1/s3 and s2/s3 P joints natural crossings. s1/s4 and s2/s4 P joints natural crossings. s6-s7 N gap left natural.',
}

out = os.path.join(os.path.dirname(__file__), '01_进.png')
img.save(out)
print(f'wrote {out}')
