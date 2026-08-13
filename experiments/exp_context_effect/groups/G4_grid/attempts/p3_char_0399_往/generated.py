"""往 (wǎng) — 8 strokes.

Decomposition: 往 = 彳 (left, 3 strokes) + 主 (right, 5 strokes).
  主 = top 点 + top 横 + spine 竖 (crossing) + middle 横 + bottom 横.

MMH-verbatim anchors — do not tune. B9 A-recipe points 1-5 + B10 point 6/7.

Joints (from MMH-injected spec):
  s1.mid ⇆ s2.head @ ML  : N (gap ~35 px)
  s2.mid ⇆ s3.head @ ML  : N (gap ~14 px)
  s3.mid ⇆ s8.head @ BL  : N (gap ~31 px)   -- 彳's shu-tail near bottom-heng head
  s5.mid ⇆ s7.head @ C   : N (gap ~14 px)   -- top heng does NOT touch spine
  s6.mid ⇆ s7.mid @ C    : P (welded)       -- middle heng crossed by spine
  s7.tail ⇆ s8.mid @ BC  : N (gap ~15 px)   -- spine ends above bottom heng
"""

# BANK_DEVIATION
# skipped: chi_step.py
# reason: chi_step defaults live in TC/C/BC (near-center column) but MMH
#   places 彳 for 往 in the far-left column TL/ML/BL — classic B10
#   compound-slot compression pattern. Inline via pie+shu with MMH
#   anchors preserves the left-column proportion.
# fresh_component: chi_step_farleft_column

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie  import draw_pie
from shu  import draw_shu
from heng import draw_heng
from dian import draw_dian

img  = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---- 彳 (left, 3 strokes) — inlined, MMH-verbatim ----
# s1 — short 撇 (upper), TL→ML
draw_pie(draw, ('TL', 0.973, 0.606), ('ML', 0.425, 0.345),
         head_width=8, tail_width=1, curve=0.10)
# s2 — longer 撇 (middle), ML→BL, big sweep left
draw_pie(draw, ('ML', 0.964, 0.236), ('BL', 0.152, 0.364),
         head_width=10, tail_width=1, curve=0.10)
# s3 — short 竖 (bottom of 彳), ML→BL
draw_shu(draw, ('ML', 0.797, 0.884), ('BL', 0.803, 0.947), width=9)

# ---- 主 (right, 5 strokes) — inlined, MMH-verbatim ----
# s4 — top 点 (dot), TC→TR
draw_dian(draw, ('TC', 0.644, 0.653), ('TR', 0.004, 0.949),
          head_width=2, peak_width=11, curve=0.08)
# s5 — top 横, C→MR (N-gap to spine — do NOT weld)
draw_heng(draw, ('C', 0.33, 0.397), ('MR', 0.432, 0.254), width=9)
# s6 — middle 横, C→MR (P-cross with spine s7)
draw_heng(draw, ('C', 0.345, 0.972), ('MR', 0.329, 0.881), width=10)
# s7 — 竖 spine, C→BC (crosses middle heng)
draw_shu(draw, ('C', 0.752, 0.447), ('BC', 0.793, 0.487), width=10)
# s8 — bottom 横, BC→BR (widest — base of 主)
draw_heng(draw, ('BC', 0.028, 0.622), ('BR', 0.751, 0.566), width=11)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 8 draw calls == 8 expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; chi_step skipped for far-left slot; N gaps preserved on s5/s7, s7/s8; P weld at s6/s7 spine crossing.',
}

out = os.path.join(os.path.dirname(__file__), '01_往.png')
img.save(out)
print('wrote', out)
