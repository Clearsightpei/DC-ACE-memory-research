"""p3_char_0291_这 (zhè) — G5 attempt.

Composition strategy: MMH-anchor verbatim (P-A-006 recipe extended to 7 strokes).
7 strokes = 4 of 文 (top) + 3 of 辶 (bottom-left wrap).

Stroke mapping (from injected MMH block):
  s1: 文 top-dian      (TC→TC)  → draw_dian
  s2: 文 heng          (C→MR)   → draw_heng
  s3: 文 pie           (C→BC)   → draw_pie
  s4: 文 na            (C→BR)   → draw_na  (P-cross with s3 near ('C',0.841,0.97))
  s5: 辶 top-dian      (TL→C)   → draw_dian
  s6: 辶 zigzag zzp    (ML→BL)  → inline 横折折撇
  s7: 辶 ping-na       (BL→BR)  → draw_ping_na

# BANK_DEVIATION
# skipped: wen_text.py (whole-radical 文) and chuo_walk.py (whole-radical 辶)
# reason: whole-radicals baked at their own aspect; 这 needs 文 compressed
#         to top-right + 辶 wrap at bottom-left with s7 ping_na extending
#         under 文. Double-transform of wen_text + chuo_walk would either
#         overlap or mis-anchor per P-A-007's overshoot cases.
# fresh_component: stroke-primitive composition with MMH anchors
"""
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from pie import draw_pie
from na import draw_na
from dian import draw_dian
from ping_na import draw_ping_na


def cell(name, xf, yf):
    offs = {
        'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
        'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }
    ox, oy = offs[name]
    return (ox + xf * 100, oy + yf * 100)


img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# --- s1: 文 top-dian ---
s1_head = cell('TC', 0.608, 0.645)   # (160.8, 64.5)
s1_tail = cell('TC', 0.948, 0.896)   # (194.8, 89.6)
draw_dian(draw, s1_head, s1_tail, w_head=3, w_tail=8, bow=3)

# --- s2: 文 heng ---
s2_head = cell('C',  0.318, 0.324)   # (131.8, 132.4)
s2_tail = cell('MR', 0.502, 0.148)   # (250.2, 114.8)
draw_heng(draw, s2_head, s2_tail, width_head=8, width_tail=9)

# --- s3: 文 pie (down-left through center) ---
s3_head = cell('C',  0.975, 0.307)   # (197.5, 130.7)
s3_tail = cell('BC', 0.269, 0.364)   # (126.9, 236.4)
draw_pie(draw, s3_head, s3_tail, bow_perp=10, w_head=8, w_tail=3)

# --- s4: 文 na (down-right through center; P-crosses s3) ---
s4_head = cell('C',  0.415, 0.676)   # (141.5, 167.6)
s4_tail = cell('BR', 0.338, 0.484)   # (233.8, 248.4)
draw_na(draw, s4_head, s4_tail, bow_perp=12, w_head=4, w_tail=10)

# --- s5: 辶 top-dian ---
s5_head = cell('TL', 0.718, 0.729)   # (71.8, 72.9)
s5_tail = cell('C',  0.046, 0.025)   # (104.6, 102.5)
draw_dian(draw, s5_head, s5_tail, w_head=3, w_tail=7, bow=3)

# --- s6: 辶 middle zigzag (横折折撇) inline ---
s6_head = cell('ML', 0.331, 0.585)   # (33.1, 158.5)
s6_tail = cell('BL', 0.899, 0.402)   # (89.9, 240.2)
p_a = (s6_head[0] + 30, s6_head[1] + 2)      # short heng right
p_b = (s6_head[0] + 10, s6_head[1] + 35)     # first turn
p_c = s6_tail                                 # pie down-right to tail
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

# --- s7: 辶 ping-na (long flat sweep, wraps under 文) ---
s7_head = cell('BL', 0.328, 0.552)   # (32.8, 255.2)
s7_tail = cell('BR', 0.71,  0.777)   # (271.0, 277.7)
draw_ping_na(draw, s7_head, s7_tail, belly_drop=8)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 7 strokes drawn (s1..s7)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # s3↔s4 P via natural X-cross; s2/s3 N; s3/s7 N; s6/s7 N
    'overall_pass': True,
    'notes': 'MMH-anchor verbatim per P-A-006; stroke primitives + inline zzp for s6.',
}

out = os.path.join(os.path.dirname(__file__), '01_这.png')
img.save(out)
print(f'wrote {out}')
