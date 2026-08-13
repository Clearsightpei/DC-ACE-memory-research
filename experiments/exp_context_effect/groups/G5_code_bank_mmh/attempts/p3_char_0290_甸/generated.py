"""p3_char_0290_甸 — G5 attempt.

Decomposition (from MMH-injected block + GT PNG):
  甸 = 勹 (wrap, 2 strokes) enclosing 田 (field, 5 strokes) → 7 strokes total.

Recipe (P-A-006): use MMH anchors verbatim + stroke-primitive layer.
No whole-radical composition (P-A-007 does not apply here — the wrap
here is scaled/positioned differently than the standalone bao_wrap
primitive, and the inner 田 is not a bank primitive).

Bank primitives used (as-is, no deviation):
  - draw_pie          (stroke 1: 撇 of 勹)
  - draw_heng_zhe_gou (stroke 2: 横折钩 wrap)
  - draw_shu          (strokes 3, 6: verticals of 田)
  - draw_heng_zhe_box (stroke 4: 横折 of 田 top-right)
  - draw_heng         (strokes 5, 7: horizontals of 田)
"""

import os, sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from pie import draw_pie
from heng_zhe_gou import draw_heng_zhe_gou
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box
from heng import draw_heng


def anchor(cell, xf, yf):
    """米字格 3x3 cell + local frac → pixel (300x300 canvas, 100px cells)."""
    cx = {'TL':0,'TC':100,'TR':200,'ML':0,'MC':100,'C':100,'MR':200,'BL':0,'BC':100,'BR':200}[cell]
    cy = {'TL':0,'TC':0,'TR':0,'ML':100,'MC':100,'C':100,'MR':100,'BL':200,'BC':200,'BR':200}[cell]
    return (cx + xf * 100, cy + yf * 100)


# ---------- MMH anchors (verbatim) ----------
s1_head = anchor('TC', 0.213, 0.504)   # (121.3, 50.4)
s1_tail = anchor('ML', 0.668, 0.538)   # ( 66.8, 153.8)

s2_head = anchor('C',  0.037, 0.251)   # (103.7, 125.1)
s2_tail = anchor('BC', 0.644, 0.795)   # (164.4, 279.5)

s3_head = anchor('ML', 0.448, 0.749)   # ( 44.8, 174.9)
s3_tail = anchor('BL', 0.727, 0.566)   # ( 72.7, 256.6)

s4_head = anchor('ML', 0.627, 0.761)   # ( 62.7, 176.1)
s4_tail = anchor('BC', 0.377, 0.458)   # (137.7, 245.8)

s5_head = anchor('BL', 0.817, 0.136)   # ( 81.7, 213.6)
s5_tail = anchor('BC', 0.324, 0.074)   # (132.4, 207.4)

s6_head = anchor('ML', 0.987, 0.802)   # ( 98.7, 180.2)
s6_tail = anchor('BC', 0.002, 0.367)   # (100.2, 236.7)

s7_head = anchor('BL', 0.776, 0.499)   # ( 77.6, 249.9)
s7_tail = anchor('BC', 0.354, 0.388)   # (135.4, 238.8)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# stroke 1 — 撇 of 勹 (short leftward sweep)
draw_pie(d, s1_head, s1_tail, bow_perp=6, w_head=6, w_tail=3)

# stroke 2 — 横折钩 outer wrap of 勹
# MMH gives only head+tail; corner is derived: tail sits at bottom-center-
# ish, so corner is to the right (encloses 田 which spans x≈45..140).
# Choose corner at (198, 118) — slightly above head_y, well right of 田.
# Hook flicks up-left from tail.
s2_corner   = (198.0, 118.0)
s2_hook_tip = (s2_tail[0] - 12, s2_tail[1] - 14)
draw_heng_zhe_gou(d, s2_head, s2_corner, s2_tail, s2_hook_tip)

# stroke 3 — 竖 (left vertical of 田)
draw_shu(d, s3_head, s3_tail, width=5)

# stroke 4 — 横折 top-right corner of 田 (boxy)
draw_heng_zhe_box(d, top_left=s4_head, bottom_right=s4_tail, width=5)

# stroke 5 — middle 横 of 田
draw_heng(d, s5_head, s5_tail, width_head=5, width_tail=6)

# stroke 6 — middle 竖 of 田
draw_shu(d, s6_head, s6_tail, width=5)

# stroke 7 — bottom 横 of 田
draw_heng(d, s7_head, s7_tail, width_head=5, width_tail=6)


SELF_CHECK = {
    'visual_ok': None,          # decide after render
    'stroke_count_ok': True,    # 7 primitive calls, one per MMH stroke
    'endpoint_mismatches': [],  # MMH anchors used verbatim
    'joint_class_mismatches': [],  # inner 田 joints are N (no forced weld)
    'overall_pass': None,
    'notes': 'P-A-006: MMH anchors verbatim + stroke primitives; '
             'corner for s2 (heng_zhe_gou) inferred at (198,118) since '
             'MMH exposes only head+tail.',
}


out_png = os.path.join(os.path.dirname(__file__), '01_甸.png')
img.save(out_png)
print(f"wrote {out_png}")
