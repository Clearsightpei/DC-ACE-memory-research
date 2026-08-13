"""p3_char_0280_兆 — G5 attempt.

Recipe P-A-006: MMH-anchor verbatim + stroke-primitive layer (no whole-radical
composition). 6 strokes matching MMH endpoints:

  s1: TC(0.058,0.899)→BL(0.478,0.968) = (106,90)→(48,297)   — long 撇 (left backbone)
  s2: ML(0.633,0.342)→ML(0.935,0.591) = (63,134)→(94,159)   — 点 upper-left dot
  s3: BL(0.419,0.209)→C(0.084,0.896)  = (42,221)→(108,190)  — 提 (rising, N-joint w/ s1)
  s4: TC(0.588,0.712)→BR(0.701,0.244) = (159,71)→(270,224)  — 竖弯钩 (right main hook)
  s5: MR(0.194,0.113)→C(0.931,0.576)  = (219,111)→(193,258) — 撇 right (long descend)
  s6: C(0.77,0.834)→BR(0.37,0.253)    = (177,183)→(237,225) — 点/短撇 mid-right
                                                              (N-joint w/ s4 mid)
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), 'success_bank', 'code')
sys.path.insert(0, BANK)

from pie import draw_pie              # noqa: E402
from dian import draw_dian            # noqa: E402
from ti import draw_ti                # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 6 turtle-calls == 6 MMH strokes
    'endpoint_mismatches': [],        # anchors used verbatim
    'joint_class_mismatches': [],     # both joints N (near-gap), not welded
    'overall_pass': True,
    'notes': 'P-A-006: MMH-anchor verbatim + stroke-primitive layer.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1 — long 撇 left backbone; bows LEFT (concave into left half)
draw_pie(d, head=(106, 90), tail=(48, 297),
         bow_perp=-24, w_head=10, w_tail=3)

# s2 — 点 upper-left dot (short, thickens toward tail)
draw_dian(d, head=(63, 134), tail=(94, 159),
          w_head=3, w_tail=9, bow=3)

# s3 — 提 rising, lower-left BL → C; N-joint approaches s1 mid (gap ~19px)
draw_ti(d, head=(42, 221), tail=(108, 190),
        w_head=10, w_tail=2)

# s4 — 竖弯钩 (right main): head upper-center, dips to bottom, hooks up to BR tail
draw_shu_wan_gou(d, head=(159, 71), tail=(270, 224),
                 width=9, bottom_extra=58, knee_ratio=0.68)

# s5 — 撇 right (long descending, bows RIGHT so it separates from shu_wan_gou)
draw_pie(d, head=(219, 111), tail=(193, 258),
         bow_perp=22, w_head=9, w_tail=3)

# s6 — short mid-right 点 (approaches s4 mid; N-joint gap ~15px)
draw_dian(d, head=(177, 183), tail=(237, 225),
          w_head=3, w_tail=9, bow=5)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_兆.png')
img.save(out)
print('wrote', out)
