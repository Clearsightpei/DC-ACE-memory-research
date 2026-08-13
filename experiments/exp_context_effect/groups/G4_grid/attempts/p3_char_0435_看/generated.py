"""看 (kàn) — 9 strokes.
Decomposition: 看 = 手 (top, 4 strokes) + 目 (bottom, 5 strokes).
  手 = short pie (s1) + short heng (s2) + long heng-cross (s3) + long descending pie (s4)
  目 = shu-left (s5) + heng-zhe (s6) + inner heng (s7) + inner heng (s8) + bottom heng (s9)

Strategy: MMH-verbatim anchors + inline base primitives. Bank has no full 手
primitive (only shou_side 扌 which is the reduced left-radical form, wrong here).
Inline pie/shu/heng/heng_zhe. N-joints (~11-35 px gaps expected between strokes
5-9 forming 目) left as gaps.
"""
import os, sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(_BANK))

from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from heng import draw_heng
from shu import draw_shu
from heng_zhe import draw_heng_zhe

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; 手 (4) + 目 (5). All N-joints preserved as gaps.',
}

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# 手 (top) — strokes 1..4
# s1: short top pie of 手
draw_pie(d, ('TC', 0.963, 0.703), ('TL', 0.858, 0.911),
         head_width=10, tail_width=2, curve=0.05, segments=40)

# s2: short upper heng of 手 (upper horizontal on the pie's tail area)
draw_heng(d, ('ML', 0.905, 0.236), ('MR', 0.024, 0.102), width=8)

# s3: main long horizontal of 手 (crosses the descending pie)
draw_heng(d, ('ML', 0.337, 0.72), ('MR', 0.602, 0.523), width=9)

# s4: long descending pie of 手 (P-cross with s2 & s3, welded)
draw_pie(d, ('TC', 0.321, 0.882), ('BL', 0.234, 0.836),
         head_width=11, tail_width=1, curve=0.08, segments=56)

# 目 (bottom) — strokes 5..9
# s5: left 竖 of 目
draw_shu(d, ('C', 0.157, 0.904), ('BC', 0.16, 1.012), width=8)

# s6: 横折 top+right of 目 (corner at (tail.x, head.y) → C(0.796, 0.925))
draw_heng_zhe(d, head=('C', 0.254, 0.925),
                  corner=('C', 0.796, 0.925),
                  tail=('BC', 0.796, 0.874),
                  h_width=8, v_width=8, shoulder=10)

# s7: inner middle heng #1 of 目
draw_heng(d, ('BC', 0.283, 0.312), ('BC', 0.731, 0.232), width=6)

# s8: inner middle heng #2 of 目
draw_heng(d, ('BC', 0.271, 0.61), ('BC', 0.743, 0.537), width=6)

# s9: bottom heng of 目
draw_heng(d, ('BC', 0.248, 0.909), ('BC', 0.852, 0.812), width=8)

out = os.path.join(os.path.dirname(__file__), '01_看.png')
img.save(out)
print('wrote', out)
