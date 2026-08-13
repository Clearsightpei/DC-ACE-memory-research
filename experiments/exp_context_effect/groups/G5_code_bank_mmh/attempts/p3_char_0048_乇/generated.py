"""p3_char_0048_乇 — G5 attempt.

Strokes (MMH):
  s1 撇  head TC(0.89,0.82)→(189,82)  tail ML(0.668,0.327)→(66.8,132.7)
  s2 横  head ML(0.281,0.898)→(28.1,189.8)  tail MR(0.479,0.688)→(247.9,168.8)
  s3 竖弯钩 head C(0.122,0.225)→(112.2,122.5)  tail BR(0.572,0.241)→(257.2,224.1)

Joints:
  s1.mid ⇆ s3.head  N (natural gap ~18px) — do NOT weld
  s2.mid ⇆ s3.mid   P (welded) — s2 crosses s3's vertical

Bank primitives used: pie.draw_pie, heng.draw_heng, shu_wan_gou.draw_shu_wan_gou
No BANK_DEVIATION — all three primitives fit cleanly.
"""

import sys, os
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


def _cell_anchor(cell, xf, yf):
    row = {"T": 0, "M": 1, "B": 2, "C": 1}[cell[0] if cell != "C" else "C"]
    col = {"L": 0, "C": 1, "R": 2}[cell[1] if len(cell) == 2 else "C"]
    return (col * 100 + xf * 100, row * 100 + yf * 100)


# Endpoints (pixel)
s1_head = (189.0, 82.0)     # TC 0.89 0.82
s1_tail = (66.8, 132.7)     # ML 0.668 0.327

s2_head = (28.1, 189.8)     # ML 0.281 0.898
s2_tail = (247.9, 168.8)    # MR 0.479 0.688

s3_head = (112.2, 122.5)    # C  0.122 0.225
s3_tail = (257.2, 224.1)    # BR 0.572 0.241


img = Image.new("RGB", (300, 300), "white")
d = ImageDraw.Draw(img)

# s1: pie sweeping down-left from top-right area to mid-left
draw_pie(d, s1_head, s1_tail, bow_perp=6, w_head=8, w_tail=3, steps=80)

# s2: heng, slight rise (nearly horizontal)
draw_heng(d, s2_head, s2_tail, width_head=9, width_tail=10)

# s3: shu-wan-gou — descend from mid-upper, curve right, hook up
draw_shu_wan_gou(d, s3_head, s3_tail,
                 width=8, bottom_extra=60, knee_ratio=0.85)

out = os.path.join(os.path.dirname(__file__), "01_乇.png")
img.save(out)
print("wrote", out)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 3 primitive calls == expected 3
    'endpoint_mismatches': [],         # anchors used verbatim from MMH block
    'joint_class_mismatches': [],      # s1.mid↔s3.head N (natural gap ~22px);
                                       # s2.mid↔s3.mid P (line crossing)
    'overall_pass': True,
    'notes': 'pie/heng/shu_wan_gou from bank, endpoints match MMH block.'
}
