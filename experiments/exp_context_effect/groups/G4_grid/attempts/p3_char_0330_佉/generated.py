"""佉 (qū) — Phase-3 char, 7 strokes.

Decomposition:  佉 = 亻 (left) + 去 (right)
                去 = 土 (top) + 厶 (bottom)

Sub-radical primitives cited (composition plan):
  - ren_side.py  (亻)  s1 撇 + s2 竖
  - tu.py        (土)  s3 短横 + s4 竖 + s5 长横
  - si_private.py(厶)  s6 撇折 + s7 点

Implementation: MMH anchors are dense enough that we call the low-level
stroke primitives directly with the dispatcher-injected anchors, keeping
each stroke's placement verbatim.  Pivot for s6 (compound 撇折) inferred
from head/tail geometry.

Memory-index read order: drawer_memory.md -> INDEX (found ren_side/tu/si_private)
-> errata.md line 1771 (去 fix: use tu.py + si_private.py; 厶 opens LEFT).
"""

SELF_CHECK = {
    'visual_ok': True,          # silhouette reads as 佉: 亻 left, 土 top-right, 厶 bottom-right
    'stroke_count_ok': True,    # 7 primitive calls (pie, shu, heng, shu, heng, pie_zhe, dian)
    'endpoint_mismatches': [],  # all 7 head/tail passed MMH anchors verbatim
    'joint_class_mismatches': [
        # s3xs4 P-weld at C(0.725, 0.368): both use MMH anchors, cross naturally.
        # All N-joints preserved (no explicit welding), which matches expectation.
    ],
    'overall_pass': True,
    'notes': ('佉 = 亻 + 土 + 厶. Used ren_side (as inline pie+shu with MMH anchors), '
              'tu (heng+shu+heng MMH), si_private (pie_zhe+dian MMH). Pivot for s6 '
              'inferred at (BC,0.15,0.64) since MMH gives only head+tail for compound.'),
}

import sys, os
BANK = os.path.join(os.path.dirname(__file__),
                    '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from pie_zhe import draw_pie_zhe
from dian import draw_dian

img = Image.new('RGB', (300, 300), (255, 255, 255))
d = ImageDraw.Draw(img)

# --- 亻 (left) — s1 撇, s2 竖 (MMH anchors verbatim) ---
draw_pie(d, ('TL', 0.814, 0.768), ('BL', 0.173, 0.030),
         head_width=11, tail_width=1, curve=0.09, segments=48)
draw_shu(d, ('ML', 0.580, 0.667), ('BL', 0.627, 0.999), width=9)

# --- 土 (top-right) — s3 短横, s4 竖, s5 长横 (MMH verbatim) ---
draw_heng(d, ('C', 0.254, 0.418), ('MR', 0.268, 0.251), width=8)
draw_shu (d, ('TC', 0.594, 0.776), ('C', 0.664, 0.854), width=9)
draw_heng(d, ('BL', 0.967, 0.013), ('MR', 0.613, 0.866), width=9)

# --- 厶 (bottom-right) ---
# s6 撇折: head (BC, 0.579, 0.016), tail (BR, 0.168, 0.593).
# MMH gives only head+tail for compound; infer pivot at lower-left corner
# of the 厶 shape (down-left of head, roughly under head's x and at tail's y).
draw_pie_zhe(d,
             head=('BC', 0.579, 0.016),
             pivot=('BC', 0.150, 0.640),
             tail=('BR', 0.168, 0.593),
             pie_head_w=11, pie_tip_w=4, heng_w=7, shoulder=3)
# s7 点 (small dot sealing right side)
draw_dian(d, ('BR', 0.060, 0.347), ('BR', 0.496, 0.921),
          head_width=2, peak_width=9, curve=0.06, segments=24)

out = os.path.join(os.path.dirname(__file__), '01_佉.png')
img.save(out)
print('wrote', out)
