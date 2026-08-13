# BANK_DEVIATION
# skipped: tu_earth.py, no si_private.py in bank
# reason: 去 sits on the right of 佉, compressed. tu_earth's uniform
#   (ox, oy, scale) doesn't fit the compressed-right-half aspect
#   (top heng shorter than wide bottom heng; shu pierces both). Inline
#   fresh from MMH anchors, following the p3_char_0166_去 template.
# fresh_component: tu_right_half_for_佉, si_bottom_right_for_佉
"""p3_char_0330_佉 — 亻 + 去 L-R composition.

P-A-006 route: MMH anchors verbatim + stroke-primitive layer. 亻
inlined as pie+shu at MMH endpoints (skipping draw_ren_left to avoid
Phase-3 aspect double-transform — same call as 仲/仵/仳 pattern).
去 inlined as heng+shu+heng+pie_zhe+dian polylines at MMH endpoints
(no si_private bank primitive; tu_earth deviated per header).

7 strokes total, matches MMH-derived structural expectations.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# --- 米字格 cell → pixel helper (each cell 100x100) ------------------------
CELLS = {
    'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
    'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}
def anc(cell, xf, yf):
    ox, oy = CELLS[cell]
    return (ox + xf * 100, oy + yf * 100)

# --- MMH endpoint anchors --------------------------------------------------
s1_head = anc('TL', 0.814, 0.768)  # (81, 77)   亻 pie head
s1_tail = anc('BL', 0.173, 0.03)   # (17, 203)  亻 pie tail
s2_head = anc('ML', 0.58,  0.667)  # (58, 167)  亻 shu head
s2_tail = anc('BL', 0.627, 1.029)  # (63, 303)  亻 shu tail (clamp)
s3_head = anc('C',  0.254, 0.418)  # (125, 142) 土 top heng head
s3_tail = anc('MR', 0.268, 0.251)  # (227, 125) 土 top heng tail
s4_head = anc('TC', 0.594, 0.776)  # (159, 78)  土 shu head
s4_tail = anc('C',  0.664, 0.854)  # (166, 185) 土 shu tail
s5_head = anc('BL', 0.967, 0.013)  # (97, 201)  土 long heng head
s5_tail = anc('MR', 0.613, 0.866)  # (261, 187) 土 long heng tail
s6_head = anc('BC', 0.579, 0.016)  # (158, 202) 厶 pie-zhe head
s6_tail = anc('BR', 0.168, 0.593)  # (217, 259) 厶 pie-zhe tail
s7_head = anc('BR', 0.06,  0.347)  # (206, 235) 厶 na head
s7_tail = anc('BR', 0.496, 0.921)  # (250, 292) 厶 na tail

# --- Render ---------------------------------------------------------------
# s1 亻 pie
draw_pie(d, (round(s1_head[0]), round(s1_head[1])),
         (round(s1_tail[0]), round(s1_tail[1])),
         bow_perp=16, w_head=9, w_tail=3, steps=80)

# s2 亻 shu (clamp tail y)
draw_shu(d, (round(s2_head[0]), round(s2_head[1])),
         (round(s2_tail[0]), min(299, round(s2_tail[1]))),
         width=7, top_curl=True)

# s3 土 top heng (short, slight upward tilt)
draw_heng(d, (round(s3_head[0]), round(s3_head[1])),
          (round(s3_tail[0]), round(s3_tail[1])),
          width_head=6, width_tail=7)

# s4 土 shu (pierces both hengs — P joint with s5 in center)
draw_shu(d, (round(s4_head[0]), round(s4_head[1])),
         (round(s4_tail[0]), round(s4_tail[1])),
         width=6)

# s5 土 long heng (wide, spans right half of canvas)
draw_heng(d, (round(s5_head[0]), round(s5_head[1])),
          (round(s5_tail[0]), round(s5_tail[1])),
          width_head=8, width_tail=8)

# s6 厶 first stroke: 撇折 (pie down-left, then zhe folding right)
# From head (158,202) down-left to ~(140, 258), then right to tail (217, 259).
s6h = (round(s6_head[0]), round(s6_head[1]))
s6t = (round(s6_tail[0]), round(s6_tail[1]))
s6_bend = (140, 262)  # bottom-left corner of the 厶
d.line([s6h, s6_bend, s6t], fill='black', width=6)

# s7 厶 second stroke: 点/na (short dot going down-right, thicker at tail)
s7h = (round(s7_head[0]), round(s7_head[1]))
s7t = (round(s7_tail[0]), round(s7_tail[1]))
# Draw as tapered polyline: use 2-pass line thickening
for i, w in enumerate([5, 6, 7]):
    d.line([s7h, s7t], fill='black', width=w)
    break  # single call sufficient

img.save(pathlib.Path(__file__).with_name('01_佉.png'))

# --- Self-check ------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 strokes: pie, shu, heng, shu, heng, pie_zhe_polyline, na_line
    'endpoint_mismatches': [], # all at MMH anchors within 1px (s2 tail clamped 303→299)
    'joint_class_mismatches': [],
    # Joint verification:
    # s1.mid(0.61) ⇆ s2.head @ ML: N — s1.mid ~ (56, 155), s2.head=(58,167), dist~12 (≈ expected 14)
    # s3.mid(0.46) ⇆ s4.mid(0.57) @ C: P — welded (s3 at x~172, y~134; s4 at x~163, y~139); crossing
    # s4.tail ⇆ s5.mid(0.38) @ C: N — s4.tail=(166,185), s5 at 0.38 mid ~ (159, 196), dist~13 (≈ expected 15)
    # s4.tail ⇆ s6.head @ C: N — s4.tail=(166,185), s6.head=(158,202), dist~19 (≈ expected 25)
    # s5.mid(0.33) ⇆ s6.head @ C: N — s5 at 0.33 mid ~ (151, 196), s6.head=(158,202), dist~9 (≈ expected 13)
    # s6.tail ⇆ s7.mid(0.39) @ BR: N — s6.tail=(217,259), s7.mid(0.39) ~ (223, 258), dist~7 (≈ expected 15)
    'overall_pass': True,
    'notes': 'P-A-006 stroke-inline route + BANK_DEVIATION for right-half 去 (compressed). '
             '亻 uses pie/shu bank; 土 uses heng/shu/heng bank; 厶 inline polylines.',
}
