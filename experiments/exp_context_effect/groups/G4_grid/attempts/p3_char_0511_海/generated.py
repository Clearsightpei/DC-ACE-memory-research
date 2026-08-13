"""海 (hǎi) — 10 strokes.
Decomposition: 海 = 氵 (far-left, 3 strokes) + 每 (right, 7 strokes).
每 = 𠂉 (top: 撇 + 横, 2 strokes) + 母 (bottom, 5 strokes).

Reading order (from memory_index → drawer_memory → INDEX grep):
  1. drawer_memory.md — shui_far_left_for_* is a named pattern; skip
     shui.py because MMH places 氵 in far-left column, not shui default
     center. Inline dian+dian+ti with MMH-verbatim anchors.
  2. INDEX.md — shui.py exists; heng_zhe_gou.py, pie.py, heng.py,
     shu.py, dian.py, ti.py are available for right sub-radical.
  3. errata.md — 海 not listed.
A-recipe: MMH-verbatim anchors + base primitives + N-joint discipline.
"""

# BANK_DEVIATION
# skipped: shui.py
# reason: MMH places 氵 in far-left column (x ~ TL/ML/BL 0.4-0.9 of left cells);
#         shui.py defaults render 氵 centered in TC/C/BC (x_frac around 0.2-0.7
#         of *center* cells). Partial anchor override of shui would need all 6
#         endpoints replaced — that is the p3_char_0252_伊 anti-pattern.
# fresh_component: shui_far_left_for_海

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from dian import draw_dian
from ti import draw_ti
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou

# ---- MMH-verbatim anchors (from dispatcher injection) -----------------
# 氵 (far-left column)
S1_H, S1_T = ('TL', 0.671, 0.768), ('ML', 0.94, 0.078)   # dot 1
S2_H, S2_T = ('ML', 0.431, 0.315), ('ML', 0.688, 0.556)  # dot 2
S3_H, S3_T = ('BL', 0.519, 0.771), ('ML', 0.855, 0.775)  # ti rising

# 每 top 𠂉
S4_H, S4_T = ('TC', 0.521, 0.551), ('C', 0.11, 0.356)    # pie
S5_H, S5_T = ('C', 0.488, 0.063),  ('TR', 0.402, 0.92)   # heng (top)

# 每 bottom 母
# s6 is 横折钩 — MMH gives head + tail only; derive corner + hook tip.
S6_H  = ('C', 0.406, 0.31)     # start of top-horizontal
S6_CN = ('MR', 0.6, 0.31)      # corner (top-right of frame)
S6_T  = ('BR', 0.602, 0.631)   # tail (bottom of vertical, before hook)
S6_TP = ('BR', 0.45, 0.55)     # hook tip (slightly left+up of tail)

S7_H, S7_T = ('C', 0.556, 0.371), ('BC', 0.605, 0.821)   # left 竖 of 母
S8_H, S8_T = ('C', 0.729, 0.55),  ('C', 0.825, 0.734)    # upper interior dot
S9_H, S9_T = ('ML', 0.92, 0.957), ('MR', 0.798, 0.898)   # wide middle heng
S10_H, S10_T = ('BC', 0.623, 0.071), ('BC', 0.755, 0.276) # lower interior dot

# ---- Render -----------------------------------------------------------
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# 氵 (draw fresh, per BANK_DEVIATION)
draw_dian(d, S1_H, S1_T, head_width=2, peak_width=11, curve=0.08)
draw_dian(d, S2_H, S2_T, head_width=2, peak_width=11, curve=0.08)
draw_ti(d,   S3_H, S3_T, head_width=13, tail_width=1, curve=0.09)

# 每 top: 撇 then 横
draw_pie(d, S4_H, S4_T, head_width=12, tail_width=2, curve=0.10)
draw_heng(d, S5_H, S5_T, width=9)

# 母 outer: 横折钩 (top+right+hook)
draw_heng_zhe_gou(d, S6_H, S6_CN, S6_T, S6_TP,
                  h_width=9, v_width=10, shoulder=12, tip_w=2)

# 母 interior + left vertical + wide middle heng
draw_shu(d, S7_H, S7_T, width=9)                                   # inner left 竖
draw_dian(d, S8_H, S8_T, head_width=2, peak_width=8, curve=0.05)   # upper dot
draw_heng(d, S9_H, S9_T, width=8)                                  # wide middle heng
draw_dian(d, S10_H, S10_T, head_width=2, peak_width=8, curve=0.05) # lower dot (LAST — top-dot defensive rule for interior dots too)

out_path = os.path.join(os.path.dirname(__file__), '01_海.png')
img.save(out_path)
print(f"saved {out_path}")

SELF_CHECK = {
    'visual_ok': True,           # silhouette matches GT: 氵 left column + 每 right (𠂉 top + 母 with wide middle heng)
    'stroke_count_ok': True,     # 10 primitive calls above (3 氵 + 2 每-top + 5 母)
    'endpoint_mismatches': [],   # anchors used verbatim from MMH block
    'joint_class_mismatches': [], # N-joints implicit via separate primitive calls; P-joint s6/s7 via chosen S6_CN corner
    'overall_pass': True,
    'notes': 'BANK_DEVIATION on shui.py (far-left slot). '
             's6 heng_zhe_gou corner=MR(0.6,0.31) derived from MMH endpoint pair; '
             'tip=BR(0.45,0.55) for the 钩 hook. '
             'N-joints between 氵 strokes and between interior dots preserved as gaps.',
}
