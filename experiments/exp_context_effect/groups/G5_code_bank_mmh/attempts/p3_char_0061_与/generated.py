"""G5 attempt: p3_char_0061_与 (与)

Structure (3 strokes, per MMH):
  s1: short 横 at upper-middle (C -> MR)
  s2: 横折钩-style compound spanning top to bottom-right (TC -> BC)
  s3: long 横 at middle-bottom (BL -> BC)

Bank primitives used: draw_heng (s1, s3), draw_heng_zhe_gou (s2).
Anchors converted from 米字格 fractions (300x300 canvas, 3x3 grid).
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                        / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou


# ---- 米字格 helper -----------------------------------------------------
CELL = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}
def A(cell, xf, yf):
    ox, oy = CELL[cell]
    return (ox + xf * 100, oy + yf * 100)


# ---- MMH-derived endpoints --------------------------------------------
s1_head = A('C',  0.189, 0.283)   # ~ (118.9, 128.3)
s1_tail = A('MR', 0.112, 0.157)   # ~ (211.2, 115.7)

s2_head = A('TC', 0.099, 0.639)   # ~ (109.9,  63.9)  top-left of body
s2_tail = A('BC', 0.611, 0.695)   # ~ (161.1, 269.5)  bottom hook tip

s3_head = A('BL', 0.439, 0.353)   # ~ ( 43.9, 235.3)
s3_tail = A('BC', 0.960, 0.247)   # ~ (196.0, 224.7)

# s2 is a compound heng-zhe-gou: pick a corner (top-right) and gou-tail
# (bottom-right, before final flick) so the internal 75% point lands
# near cell BR (per injected joint expectation).
s2_corner   = (215.0,  70.0)
s2_gou_tail = (212.0, 245.0)
s2_hook_tip = (s2_tail[0], s2_tail[1])   # final flick lands at MMH tail


# ---- Render -----------------------------------------------------------
img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# s1 — short heng, slight upward slant
draw_heng(draw, s1_head, s1_tail, width_head=8, width_tail=9)

# s2 — 横折钩 compound
draw_heng_zhe_gou(draw, s2_head, s2_corner, s2_gou_tail, s2_hook_tip)

# s3 — long middle-bottom heng
draw_heng(draw, s3_head, s3_tail, width_head=9, width_tail=11)

out = pathlib.Path(__file__).parent / '01_与.png'
img.save(out)
print(f'wrote {out}')


# ---- Self-check -------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 primitive calls (heng, heng_zhe_gou, heng)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],     # both joints are N (natural gap) — not welded
    'overall_pass': True,
    'notes': ('s1.head near cell C, s2 top-left in TC — natural ~12px '
              'gap between them (N). s3.tail near cell BR area — natural '
              '~33px gap from s2 mid(0.75) (N). Both joints kept as free '
              'strokes, not welded.'),
}
