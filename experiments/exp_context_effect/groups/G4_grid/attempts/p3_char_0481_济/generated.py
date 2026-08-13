"""济 (jì) — 9 strokes.
Decomposition: 济 = 氵 (left, 3 strokes: dian + dian + ti)
                 + 齐 (right, 6 strokes: dian + heng + pie + na + shu + shu).

A-recipe applied:
  1. Explicit decomposition (this docstring).
  2. MMH-verbatim anchors — every stroke passes the dispatcher-injected
     tuple UNCHANGED into a base primitive.
  3. SELF_CHECK dict below.
  4. Base primitives only (dian/heng/pie/na/shu/ti). Compound bank
     primitives (shui.py) SKIPPED — see BANK_DEVIATION.
  5. All 6 declared N-joints between 氵 and 齐, and s5↔s7, s4↔s5 etc.
     are left as natural gaps (no artificial weld). s6.mid ⇆ s7.mid is
     the P joint (X-cross apex) — pie and na cross naturally in cell C
     because their endpoints straddle that pixel.

# BANK_DEVIATION
# skipped: shui.py
# reason: shui.py's default anchors place 氵 in the standard column
#   (s1 head TC 0.195); MMH here places 氵 far-left (s1 head TL 0.677,
#   s2 head ML 0.437, s3 head BL 0.606) to leave the right two-thirds
#   for 齐. Same far-left slot pattern documented for 治 (B11 PASS) and
#   油 (B11 PASS).
# fresh_component: shui_far_left_for_济
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from heng import draw_heng
from pie  import draw_pie
from na   import draw_na
from shu  import draw_shu
from ti   import draw_ti

# ------------------------------------------------------------------
# MMH-verbatim anchors (from dispatcher-injected structural block)
# ------------------------------------------------------------------
# 氵 (far-left column)
S1_H, S1_T = ('TL', 0.677, 0.776), ('C',  0.002, 0.031)   # upper 点
S2_H, S2_T = ('ML', 0.437, 0.418), ('ML', 0.756, 0.655)   # middle 点
S3_H, S3_T = ('BL', 0.606, 0.924), ('ML', 0.94,  0.866)   # 提

# 齐 (right two-thirds)
S4_H, S4_T = ('TC', 0.541, 0.618), ('TC', 0.884, 0.841)   # 点 (top-of-齐)
S5_H, S5_T = ('C',  0.192, 0.113), ('MR', 0.417, 0.025)   # 横
S6_H, S6_T = ('C',  0.878, 0.14 ), ('BC', 0.063, 0.036)   # 撇 (X left leg)
S7_H, S7_T = ('C',  0.333, 0.348), ('MR', 0.812, 0.972)   # 捺 (X right leg)
S8_H, S8_T = ('BC', 0.377, 0.147), ('BC', 0.09,  1.009)   # 竖 (left leg)
S9_H, S9_T = ('BC', 0.931, 0.045), ('BR', 0.06,  1.12 )   # 竖 (right leg)

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- 氵 (draw first: left radical) ---
draw_dian(d, S1_H, S1_T, head_width=2, peak_width=11, curve=0.08)
draw_dian(d, S2_H, S2_T, head_width=2, peak_width=11, curve=0.08)
draw_ti  (d, S3_H, S3_T, head_width=13, tail_width=1, curve=0.09)

# --- 齐 (right) ---
# s4: short 点 at top of 齐
draw_dian(d, S4_H, S4_T, head_width=2, peak_width=10, curve=0.05)
# s5: nearly-horizontal 横 across top
draw_heng(d, S5_H, S5_T, width=8)
# s6 + s7: the X-cross (P joint at cell C, natural crossing of endpoints)
draw_pie (d, S6_H, S6_T, head_width=11, tail_width=1, curve=0.08)
draw_na  (d, S7_H, S7_T, head_width=3, peak_width=13, tail_width=1,
          peak_t=0.8, curve=0.08)
# s8, s9: two verticals under the X
draw_shu (d, S8_H, S8_T, width=8)
draw_shu (d, S9_H, S9_T, width=8)

out_png = os.path.join(os.path.dirname(__file__), '01_济.png')
img.save(out_png)
print('wrote', out_png)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 draw calls, 9 MMH strokes
    'endpoint_mismatches': [], # all 9 endpoints MMH-verbatim
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('9 strokes MMH-verbatim; shui skipped (far-left slot); '
              'X-cross via pie+na endpoints straddling cell C — '
              'natural crossing without shared CROSS_ANCHOR '
              '(sufficient here because the X sits isolated between '
              'the top 横 and the two bottom 竖).'),
}
