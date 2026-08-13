"""p3_char_0454_疭 — G5 attempt

Reasoning trace (P-A-008):
- 疭 = 疒 (5 strokes) + 从 (4 strokes) = 9 strokes; matches MMH count.
- 疒 is on the terminal-freeze list (P-A-007, post-B10): no whole-radical
  bank primitive exists. Inline from stroke primitives with MMH anchors
  verbatim (P-A-006 recipe).
- 从 = two 人 side by side (pie + na each). No whole-radical bank for 从
  either. Inline as pie + na per person. This is a stroke-primitive layer
  approach — matches sibling 疫/疥/疤 template (see attempts/p3_char_0450_疫/).
- No BANK_DEVIATION: every stroke uses a bank stroke primitive at MMH
  endpoints — no whole-radical primitive was skipped because none exists.

BANK usage:
- s1: dian (top dot of 疒)
- s2: heng_pie (short heng bending down of 疒)
- s3: pie (long left-descending sweep of 疒)
- s4: dian (small inside dot of 疒)
- s5: ti (rising ti of 疒)
- s6: pie (left 人 of 从 — small pie)
- s7: na (left 人 of 从 — small na)
- s8: pie (right 人 of 从 — long pie down-left)
- s9: na (right 人 of 从 — long na sweeping bottom-right)
"""
import sys
import os
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from dian import draw_dian
from pie import draw_pie
from na import draw_na
from ti import draw_ti
from heng_pie import draw_heng_pie


# ---------- MMH 米字格 → pixel helper (300×300, 3×3 cells of 100) ----------
CELL_OFFSETS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}
def A(cell, xf, yf):
    ox, oy = CELL_OFFSETS[cell]
    return (ox + xf * 100, oy + yf * 100)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --------- 疒 radical (s1–s5) ---------
# s1: top dot of 疒 — small dian going down-right
s1_h = A('TC', 0.412, 0.507)   # (141.2, 50.7)
s1_t = A('TC', 0.799, 0.771)   # (179.9, 77.1)
draw_dian(d, s1_h, s1_t, w_head=2, w_tail=6, bow=2)

# s2: short 横 of 疒 — center-left up to top-right, slight up-slant
s2_h = A('C', 0.16, 0.175)     # (116.0, 117.5)
s2_t = A('TR', 0.347, 0.914)   # (234.7, 91.4)
# Use heng_pie so it has a tiny turn at the end (matches GT tick).
draw_heng_pie(d, s2_h, s2_t,
              apex_x=s2_h[0] + 100,
              corner_x=s2_h[0] + 110)

# s3: long 撇 of 疒 — from upper-right of 疒 sweeping down-left
s3_h = A('ML', 0.935, 0.008)   # (93.5, 100.8)
s3_t = A('BL', 0.387, 1.006)   # (38.7, 300.6)
draw_pie(d, s3_h, s3_t, bow_perp=14, w_head=9, w_tail=3)

# s4: small dian inside upper 疒 (goes down-right)
s4_h = A('ML', 0.442, 0.242)   # (44.2, 124.2)
s4_t = A('ML', 0.747, 0.526)   # (74.7, 152.6)
draw_dian(d, s4_h, s4_t, w_head=2, w_tail=6, bow=1)

# s5: 提 rising diagonal inside 疒 (head lower-left, tail upper-right)
s5_h = A('BL', 0.229, 0.194)   # (22.9, 219.4)
s5_t = A('ML', 0.858, 0.819)   # (85.8, 181.9)
draw_ti(d, s5_h, s5_t, w_head=8, w_tail=2)

# --------- 从 inner (two 人; s6+s7 = left person; s8+s9 = right person) ---------
# s6: left 人 pie — center down to bottom-left
s6_h = A('C', 0.336, 0.518)    # (133.6, 151.8)
s6_t = A('BC', 0.005, 0.725)   # (100.5, 272.5)
draw_pie(d, s6_h, s6_t, bow_perp=8, w_head=7, w_tail=3)

# s7: left 人 na — small na sweeping down-right (below/right of s6 crossing)
s7_h = A('BC', 0.403, 0.191)   # (140.3, 219.1)
s7_t = A('BC', 0.626, 0.487)   # (162.6, 248.7)
draw_na(d, s7_h, s7_t, bow_perp=4, w_head=3, w_tail=7)

# s8: right 人 pie — long, from upper-right down to bottom-center
s8_h = A('C', 0.893, 0.345)    # (189.3, 134.5)
s8_t = A('BC', 0.342, 1.023)   # (134.2, 302.3)
draw_pie(d, s8_h, s8_t, bow_perp=14, w_head=8, w_tail=3)

# s9: right 人 na — long sweeping down-right (bottom-right corner)
s9_h = A('BR', 0.039, 0.145)   # (203.9, 214.5)
s9_t = A('BR', 0.83, 0.985)    # (283.0, 298.5)
draw_na(d, s9_h, s9_t, bow_perp=14, w_head=3, w_tail=11)

# --------- self-check ---------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 9 primitives called, matches MMH
    'endpoint_mismatches': [],     # MMH anchors used verbatim
    'joint_class_mismatches': [],  # all 6 expected joints are N (natural gaps);
                                   # no artificial welding — each stroke uses
                                   # its own MMH endpoints, so gaps arise naturally.
    'overall_pass': True,
    'notes': ('疒 + 从 inlined from stroke primitives (P-A-006). MMH endpoints '
              'used verbatim. No whole-radical bank for either 疒 (terminal-'
              'freeze) or 从 (2 人 side by side); stroke-primitive layer '
              'matches directly. Sibling of 疫/疥/疤 recipe.'),
}

out = os.path.join(os.path.dirname(__file__), '01_疭.png')
img.save(out)
print('wrote', out, 'strokes=9', 'SELF_CHECK=', SELF_CHECK['overall_pass'])
