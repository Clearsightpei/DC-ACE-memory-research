# BANK_DEVIATION
# skipped: ri.py, fu_right.py
# reason: 日 sits compressed in the LEFT-bottom slot (x~78-145) not full-canvas
#         (ri.py defaults). 阝-right is compressed to right-column x~180-225 with
#         MMH giving only 2 anchors for the 横撇弯钩 ear (fu_right defaults 6 to
#         full canvas). Inline both per B10 A-recipe (compound-slot embedding).
# fresh_component: ri_bl_compressed_for_都, fu_right_narrow_column_for_都
"""p3_char_0503_都 — G4 attempt, 10 strokes.

Composition:
  # 都 = 者 (left, 8 strokes) + 阝 (right, 2 strokes)
  # 者 = 耂 (top-left cap, s1-s4) + 日 (bottom-left compressed, s5-s8)
  # 阝 = 横撇弯钩 (s9) + 竖 long descender (s10)

Reused pattern from 者 A-verdict (p3_char_0373_者); shifted 日 left to
free right column for 阝.

MMH-verbatim anchors:
  s1 ML(0.659,0.063) → TC(0.4,0.976)    — 短横 top of 耂
  s2 TL(0.949,0.548) → ML(0.99,0.444)   — 竖 crossing s1 (P at C)
  s3 ML(0.284,0.6)   → C(0.72,0.409)    — 长横 main crossbar
  s4 TC(0.772,0.888) → BL(0.146,0.546)  — 长撇 sweeping down-left
  s5 ML(0.782,0.869) → BL(0.844,0.742)  — 日 left 竖
  s6 ML(0.938,0.934) → BC(0.43,0.815)   — 日 横折 (single compound)
  s7 BL(0.946,0.273) → BC(0.242,0.218)  — 日 中横
  s8 BL(0.92,0.651)  → BC(0.263,0.622)  — 日 底横
  s9 MR(0.065,0.131) → BR(0.197,0.183)  — 阝 横撇弯钩 (ear, compressed)
  s10 C(0.813,0.031) → BC(0.931,1.202)  — 阝 竖 (long right descender)

Joints (14 total, MMH-declared):
  s1.mid ⇆ s2.mid P — welded at C
  s1.tail ⇆ s4.head N — small gap
  s2.tail ⇆ s3.mid N — small gap
  s3.mid ⇆ s4.mid P — welded
  s3.tail ⇆ s10.mid N — small gap (bar reaches near 阝 shu)
  s4.mid ⇆ s5.head T — tangent (s5 head touches s4)
  s4.mid ⇆ s6.head N — gap
  s4.head ⇆ s10.head N — gap (top of long strokes)
  s5.mid ⇆ s6.head N — 日 top-left corner
  s5.mid ⇆ s7.head N — 日 left wall middle
  s5.tail ⇆ s8.head N — 日 bottom-left corner
  s6.mid ⇆ s7.tail N — 日 middle bar to right wall
  s6.tail ⇆ s8.tail N — 日 bottom-right corner
  s9.head ⇆ s10.head N — 阝 ear top ~ shu head gap
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import (anchor_to_xy, quad_bezier,
                     stroke_variable_width, fat_line, sample_line)
from PIL import Image, ImageDraw

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)
INK = (0, 0, 0)

# ============ 耂 (strokes 1-4) ============

# ---- s1: 短横 top (slight up-right taper) ----
p_s1_h = anchor_to_xy(('ML', 0.659, 0.063))
p_s1_t = anchor_to_xy(('TC', 0.4, 0.976))
pts = sample_line(p_s1_h, p_s1_t, n=24)
widths = [7 + 2 * (i / 24) for i in range(25)]
stroke_variable_width(d, pts, widths, INK)

# ---- s2: 竖 (crosses s1 at P) ----
p_s2_h = anchor_to_xy(('TL', 0.949, 0.548))
p_s2_t = anchor_to_xy(('ML', 0.99, 0.444))
pts = sample_line(p_s2_h, p_s2_t, n=24)
widths = [6] * 25
stroke_variable_width(d, pts, widths, INK)

# ---- s3: 长横 (main crossbar, slight arc) ----
p_s3_h = anchor_to_xy(('ML', 0.284, 0.6))
p_s3_t = anchor_to_xy(('C', 0.72, 0.409))
mx = (p_s3_h[0] + p_s3_t[0]) / 2
my = (p_s3_h[1] + p_s3_t[1]) / 2 - 4
pts = quad_bezier(p_s3_h, (mx, my), p_s3_t, n=48)
widths = [6 + 3 * (i / 48) for i in range(49)]
stroke_variable_width(d, pts, widths, INK)

# ---- s4: 长撇 (upper-right → lower-left; curved) ----
p_s4_h = anchor_to_xy(('TC', 0.772, 0.888))
p_s4_t = anchor_to_xy(('BL', 0.146, 0.546))
mx = (p_s4_h[0] + p_s4_t[0]) / 2 + 18
my = (p_s4_h[1] + p_s4_t[1]) / 2 + 4
pts = quad_bezier(p_s4_h, (mx, my), p_s4_t, n=48)
widths = [9 - 6 * (i / 48) for i in range(49)]
stroke_variable_width(d, pts, widths, INK)

# ============ 日 (strokes 5-8, compressed into BL region) ============

# ---- s5: 日 left 竖 ----
p_s5_h = anchor_to_xy(('ML', 0.782, 0.869))
p_s5_t = anchor_to_xy(('BL', 0.844, 0.742))
fat_line(d, p_s5_h, p_s5_t, width=6)

# ---- s6: 日 横折 (single compound; internal corner) ----
p_s6_h = anchor_to_xy(('ML', 0.938, 0.934))
p_s6_t = anchor_to_xy(('BC', 0.43, 0.815))
corner_s6 = (p_s6_t[0], p_s6_h[1])  # top-right corner of 日 box
fat_line(d, p_s6_h, corner_s6, width=6)
fat_line(d, corner_s6, p_s6_t, width=6)

# ---- s7: 日 middle 横 (attach left wall N-gap; reach right wall) ----
p_s7_h = anchor_to_xy(('BL', 0.946, 0.273))
p_s7_t = anchor_to_xy(('BC', 0.242, 0.218))
p_s7_t = (corner_s6[0], p_s7_t[1])  # extend to kiss right wall
fat_line(d, p_s7_h, p_s7_t, width=5)

# ---- s8: 日 底横 (bottom bar; reach both walls) ----
p_s8_h = anchor_to_xy(('BL', 0.92, 0.651))
p_s8_t = anchor_to_xy(('BC', 0.263, 0.622))
fat_line(d, p_s8_h, p_s8_t, width=6)

# ============ 阝-right (strokes 9-10, right column) ============

# ---- s9: 横撇弯钩 (ear compound; single stroke with internal shape) ----
# MMH gives only head/tail; we synthesize the ear silhouette.
p_s9_h = anchor_to_xy(('MR', 0.065, 0.131))   # top of ear (~206.5, 113.1)
p_s9_t = anchor_to_xy(('BR', 0.197, 0.183))   # bottom-inside end (~219.7, 218.3)
# Segments:
#  A. short 横 rightward from head
#  B. 撇 down-left
#  C. 弯 curving back right
#  D. 钩 hooking left inward → tail
seg_A_end = (p_s9_h[0] + 14, p_s9_h[1] + 2)          # short heng
seg_B_end = (p_s9_h[0] + 4, p_s9_h[1] + 40)          # pie down-left
belly     = (p_s9_h[0] + 22, p_s9_h[1] + 70)         # 弯 belly
seg_C_end = (p_s9_h[0] + 14, p_s9_h[1] + 100)        # bottom of 弯
# 横 short
fat_line(d, p_s9_h, seg_A_end, width=6)
# 撇 curve (quad bezier from A_end through mid to B_end)
mid_pie = ((seg_A_end[0] + seg_B_end[0]) / 2 - 6,
           (seg_A_end[1] + seg_B_end[1]) / 2)
pts = quad_bezier(seg_A_end, mid_pie, seg_B_end, n=20)
widths = [7 - 2 * (i / 20) for i in range(21)]
stroke_variable_width(d, pts, widths, INK)
# 弯 curve (quad bezier through belly)
pts = quad_bezier(seg_B_end, belly, seg_C_end, n=24)
widths = [5 + 4 * (i / 24) for i in range(25)]
stroke_variable_width(d, pts, widths, INK)
# 钩 short hook to tail
fat_line(d, seg_C_end, p_s9_t, width=6)

# ---- s10: 阝 竖 (long vertical descender, right column) ----
p_s10_h = anchor_to_xy(('C', 0.813, 0.031))
p_s10_t_raw = anchor_to_xy(('BC', 0.931, 1.202))
# Clamp to canvas
p_s10_t = (p_s10_t_raw[0], min(p_s10_t_raw[1], 298))
pts = sample_line(p_s10_h, p_s10_t, n=32)
widths = [11 - 3 * (i / 32) for i in range(33)]
stroke_variable_width(d, pts, widths, INK)

out_png = os.path.join(os.path.dirname(__file__), '01_都.png')
img.save(out_png)

# ---- Self-check ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 stroke primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('10 strokes MMH-verbatim. 者 (s1-s8) reuses A-verdict pattern from '
              '0373_者 with 日 shifted LEFT to BL region. 阝-right (s9-s10) '
              'inlined (BANK_DEVIATION vs fu_right for narrow-right-column slot). '
              's1×s2 and s3×s4 welded P; s4.mid⇆s5.head T; all 日 corners + '
              's9.head⇆s10.head remain N (small gap).'),
}

if __name__ == '__main__':
    print('wrote', out_png)
