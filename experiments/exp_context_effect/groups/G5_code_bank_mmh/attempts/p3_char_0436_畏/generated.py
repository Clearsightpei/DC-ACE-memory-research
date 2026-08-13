"""p3_char_0436_畏 — G5 attempt.

Reasoning trace (P-A-008 compliant):

畏 = 田 (top, 5 strokes) + lower-衣-variant (bottom, 4 strokes) = 9 strokes.

Bank check (P-A-007-v2 hard-check):
- No `tian_field` bank entry. Available box relatives: kou_mouth (3-stroke
  口, wrong stroke count), si_four (5-stroke 四, wrong internal marks),
  you_by (5-stroke 由, has central-top shu extension, wrong shape).
- None of them is a whole-radical match for 田 (which is 5 strokes = shu
  + heng_zhe + heng + shu + heng). Decision: inline 田 from MMH anchors
  using stroke primitives (P-A-006 recipe).
- No whole-radical for the bottom (衣-lower-variant) either; inline it
  too.

BANK_DEVIATION:
  skipped: kou_mouth, si_four, you_by (none of them matches 田 top-half)
  reason: 田 needs internal cross (heng + shu inside a box); no bank
    entry has that geometry. si_four has pie+shu_zhe inside; you_by has
    central-top shu extending upward. Neither is 田.
  fresh_component: tian_field_inline (5 primitives: shu + heng_zhe_box +
    heng-mid + shu-mid + heng-bot) for 田 top.

Endpoint anchors are taken verbatim from the MMH-injected block
(P-A-006 recipe: MMH-anchor verbatim + stroke-primitive layer).
"""

import os, sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from pie import draw_pie
from na import draw_na


# ── Anchor conversion (米字格 cell + fractional coords → PIL px) ─────
_COL = {'L': 0, 'C': 1, 'R': 2}
_ROW = {'T': 0, 'M': 1, 'B': 2}
CELL = 100  # 300/3

def A(cell, xf, yf):
    if cell == 'C':
        col, row = 1, 1
    else:
        row = _ROW[cell[0]]
        col = _COL[cell[1]]
    return (col * CELL + xf * CELL, row * CELL + yf * CELL)


# ── Render ────────────────────────────────────────────────────────
img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ── TOP: 田 (strokes 1-5, MMH-anchor verbatim) ────────────────────
# s1: 竖 left vertical of 田
s1_head = A('TL', 0.826, 0.744)   # ≈ (82.6, 74.4)
s1_tail = A('C',  0.09,  0.576)   # ≈ (109, 157.6)
draw_shu(draw, s1_head, s1_tail, width=6)

# s2: 横折 top+right compound of 田 — head at top-left, corner then down
# Endpoints are head (top-left) and tail (bottom-right of box).
# Rendered via heng_zhe_box which handles the L-shape.
s2_head = A('TL', 0.961, 0.744)   # ≈ (96.1, 74.4)
s2_tail = A('C',  0.913, 0.494)   # ≈ (191.3, 149.4)
draw_heng_zhe_box(draw, s2_head, s2_tail, width=6)

# s3: middle 横 of 田
s3_head = A('C', 0.184, 0.14)     # ≈ (118.4, 114)
s3_tail = A('C', 0.802, 0.058)    # ≈ (180.2, 105.8)
draw_heng(draw, s3_head, s3_tail, width_head=6, width_tail=7)

# s4: middle 竖 of 田 (through the center, penetrates top and middle heng)
s4_head = A('TC', 0.421, 0.762)   # ≈ (142.1, 76.2)
s4_tail = A('C',  0.436, 0.362)   # ≈ (143.6, 136.2)
draw_shu(draw, s4_head, s4_tail, width=6)

# s5: bottom 横 of 田 (closes box)
s5_head = A('C', 0.14,  0.503)    # ≈ (114, 150.3)
s5_tail = A('C', 0.808, 0.362)    # ≈ (180.8, 136.2)
draw_heng(draw, s5_head, s5_tail, width_head=6, width_tail=7)

# ── BOTTOM: 衣-lower variant (strokes 6-9) ───────────────────────
# s6: long 横 spanning below 田
s6_head = A('ML', 0.36,  0.884)   # ≈ (36, 188.4)
s6_tail = A('MR', 0.646, 0.711)   # ≈ (264.6, 171.1)
draw_heng(draw, s6_head, s6_tail, width_head=8, width_tail=9)

# s7: short slanted stroke going down-right from lower-left (a shu-like
# drop that curves). Head above the long heng near left, tail below on
# center. Render as a shu (straight-ish body) since primary motion is
# vertical.
s7_head = A('ML', 0.882, 0.922)   # ≈ (88.2, 192.2)
s7_tail = A('BC', 0.482, 0.458)   # ≈ (148.2, 245.8)
draw_shu(draw, s7_head, s7_tail, width=6)

# s8: 撇 — short leftward-down curve on the right side, from (208, 184)
# to (179, 219). Down-LEFT motion, so use draw_pie.
s8_head = A('MR', 0.083, 0.837)   # ≈ (208.3, 183.7)
s8_tail = A('BC', 0.79,  0.194)   # ≈ (179, 219.4)
draw_pie(draw, s8_head, s8_tail, bow_perp=6, w_head=7, w_tail=3)

# s9: 捺 — long thickening rightward-down sweep, the main bottom-right
# stroke. Head ≈ center, tail ≈ bottom-right.
s9_head = A('C',  0.277, 0.846)   # ≈ (127.7, 184.6)
s9_tail = A('BR', 0.81,  0.812)   # ≈ (281, 281.2)
draw_na(draw, s9_head, s9_tail, bow_perp=14, w_head=4, w_tail=11)


# ── Self-check log ────────────────────────────────────────────────
SELF_CHECK = {
    'visual_ok': None,           # populated after first render + visual compare
    'stroke_count_ok': True,     # 9 primitive calls = 9 strokes
    'endpoint_mismatches': [],   # all anchors used verbatim from MMH
    'joint_class_mismatches': [],  # joints not explicitly welded; natural N-class gaps
    'overall_pass': None,
    'notes': 'MMH-anchor verbatim, P-A-006 recipe. BANK_DEVIATION for 田 top (no tian bank entry).'
}

out_path = os.path.join(os.path.dirname(__file__), '01_畏.png')
img.save(out_path)
print(f"saved {out_path}")
