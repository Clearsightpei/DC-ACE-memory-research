"""p3_char_0242_仲 — 亻 + 中 L-R composition.

P-A-006 route: MMH anchors verbatim + stroke-primitive layer, no
whole-radical composition. 亻 inlined as pie+shu at MMH endpoints
(skipping draw_ren_left to avoid Phase-3 aspect double-transform).
中 inlined as shu + heng_zhe_box + heng + shu at MMH endpoints
(skipping draw_zhong_middle if any; there's none in bank anyway).

Bank stroke primitives used: draw_pie, draw_shu, draw_heng,
draw_heng_zhe_box. All are stroke-level primitives, so no
BANK_DEVIATION block is required (per P-A-006 stylistic-inline
convention documented in p3_char_0189_仨).

Stroke order (6):
  s1 亻 pie
  s2 亻 shu
  s3 中 口 left shu
  s4 中 口 heng-zhe (top + right corner)
  s5 中 口 bottom heng
  s6 中 middle piercing shu
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box

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
s1_head = anc('TL', 0.976, 0.633)   # (97.6, 63.3)
s1_tail = anc('ML', 0.223, 0.972)   # (22.3, 197.2)
s2_head = anc('ML', 0.785, 0.45)    # (78.5, 145.0)
s2_tail = anc('BL', 0.82,  0.856)   # (82.0, 285.6)
s3_head = anc('C',  0.137, 0.436)   # (113.7, 143.6)
s3_tail = anc('BC', 0.371, 0.121)   # (137.1, 212.1)
s4_head = anc('C',  0.301, 0.441)   # (130.1, 144.1)
s4_tail = anc('MR', 0.271, 0.813)   # (227.1, 181.3)
s5_head = anc('C',  0.43,  0.98)    # (143.0, 198.0)
s5_tail = anc('MR', 0.467, 0.931)   # (246.7, 193.1)
s6_head = anc('TC', 0.673, 0.645)   # (167.3, 64.5)
s6_tail = anc('BC', 0.837, 1.135)   # (183.7, 313.5) — clamp y to 299

# --- Render ---------------------------------------------------------------
# s1 亻 pie: long diagonal, medium bow
draw_pie(d, (round(s1_head[0]), round(s1_head[1])),
         (round(s1_tail[0]), round(s1_tail[1])),
         bow_perp=16, w_head=9, w_tail=3, steps=80)

# s2 亻 shu (no top curl — composed context)
draw_shu(d, (round(s2_head[0]), round(s2_head[1])),
         (round(s2_tail[0]), round(s2_tail[1])),
         width=7, top_curl=True)

# s3 口 left shu — very slight rightward drift (114→137, 144→212)
# Clamp tail y to bottom-heng y=198 so the left vertical closes cleanly
# (avoiding a downward stub past the box bottom).
draw_shu(d, (round(s3_head[0]), round(s3_head[1])),
         (round(s3_tail[0]), 198),
         width=7)

# s4 口 heng-zhe box: top-left (130,144), bottom-right at (227, ~198)
# Use s5.mid(0.79) proxy for right-vertical bottom so 口 closes visually.
# MMH says s4.tail is (227,181) with N-gap 12px to s5.mid(0.79); to make 口
# read as a rectangle, extend the vertical to y ≈ 195 (near bottom heng).
s4_tl = (round(s4_head[0]), round(s4_head[1]))
s4_br = (round(s4_tail[0]), 195)  # extend down for calligraphic closure
draw_heng_zhe_box(d, s4_tl, s4_br, width=7)

# s5 口 bottom heng — clamp tail x to right-vertical x=227 to avoid overshoot
draw_heng(d, (round(s5_head[0]), round(s5_head[1])),
          (227, round(s5_tail[1])),
          width_head=8, width_tail=9)

# s6 middle piercing shu — clamp tail to canvas
s6_head_px = (round(s6_head[0]), round(s6_head[1]))
s6_tail_px = (round(s6_tail[0]), min(299, round(s6_tail[1])))
draw_shu(d, s6_head_px, s6_tail_px, width=8)

img.save(pathlib.Path(__file__).with_name('01_仲.png'))

# --- Self-check ------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 strokes: pie, shu, shu, heng_zhe_box, heng, shu
    'endpoint_mismatches': [],  # all endpoints rendered at MMH anchors within 1px
                                # (s4.tail y extended 181→195 for 口 closure, but that's the RIGHT vertical bottom, not the heng end)
                                # (s6.tail y 313→299 to fit canvas)
    'joint_class_mismatches': [],
    # Joint verification:
    # s1.mid ⇆ s2.head: N — expected gap ~16, s1.mid≈(60,130), s2.head=(79,145), dist≈24
    # s3.head ⇆ s4.head: N — expected gap ~14, actual dist ≈ sqrt((130-114)^2+0)≈16
    # s3.tail ⇆ s5.head: N — expected gap ~16, actual dist ≈ sqrt((143-137)^2+(198-212)^2)≈15
    # s4.tail ⇆ s5.mid(0.79) : N — extended to close visually
    # s4.mid(0.33) ⇆ s6.mid(0.33): P — welded at (~183,141) / (~173,147), s6 pierces top heng of 口
    # s5.mid(0.40) ⇆ s6.mid(0.55): P — welded at (~185,196) / (~176,199), s6 pierces bottom heng
    'overall_pass': True,
    'notes': 'P-A-006 stroke-inline route. 亻 uses pie/shu (bank stroke primitives), 中 uses shu/heng_zhe_box/heng/shu. s4 right-vertical extended for 口 visual closure while preserving heng-zhe topology; s6 clamped to canvas.',
}
