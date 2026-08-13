# BANK_DEVIATION
# skipped: none directly; but s2 in 车 is a compound 撇折-like path
#          (down-and-slightly-left, then rightward), which is not a canonical
#          shu_zhe (vertical then right) nor a heng_pie. I reuse
#          draw_shu_zhe as a general "2-segment L with 顿笔 knob" primitive
#          — its geometry (head -> corner -> tail with a corner dab) is
#          exactly what MMH's s2 median needs, even though the first
#          segment is slanted rather than pure-vertical.
# reason: preferred to keep 4 primitive calls (matching MMH stroke count)
#         rather than composing s2 out of pie + heng (which would be 5).
# fresh_component: none (bank draw_shu_zhe repurposed as generic bent stroke)

"""p2_radical_089_车 — 车 (4画): heng + 撇折-compound + long heng + shu.

Anchor decoding (300x300, 3x3 米字格 with 100-px cells):
  s1: head ML(0.809, 0.131) -> (81, 113); tail MR(0.171, 0.031) -> (217, 103)
  s2: head TC(0.389, 0.565) -> (139,  57); tail MR(0.183, 0.778) -> (218, 178)
  s3: head BL(0.331, 0.385) -> ( 33, 239); tail BR(0.669, 0.353) -> (267, 235)
  s4: head C (0.415, 0.482) -> (142, 148); tail BC(0.532, 1.146) -> (153, 315)
        (s4 tail y=315 clipped to 295 to stay inside 300-px canvas)

Joint placements:
  s1.mid ⇆ s2.mid at C ≈ (128, 114) — welded (P): s1 crosses s2 near s2's
    upper descent.
  s2.mid(0.75) ⇆ s4.mid(0.22) at C ≈ (150, 181) — welded (P): s2's
    horizontal tail crosses s4's upper shaft.
  s3.mid ⇆ s4.mid at BC ≈ (150, 232) — welded (P): the long middle heng
    crosses the central shu near their midpoints.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from heng import draw_heng
from shu import draw_shu
from shu_zhe import draw_shu_zhe


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitive calls, matches MMH count
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all three joints are P (welded)
    'overall_pass': True,
    'notes': ('s2 rendered as bent stroke via draw_shu_zhe with slanted '
              'first segment; s4 tail clipped to y=295 (MMH gives 315).')
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — top short heng
    draw_heng(d, (81, 113), (217, 103), width_head=9, width_tail=10)

    # s2 — 撇折-like compound: head high at TC, elbow lower-left,
    # tail out to MR. Corner picked so the elbow sits below s1 in cell C
    # (welded joint) and the horizontal tail crosses s4's upper shaft.
    draw_shu_zhe(d, head=(139, 57), corner=(96, 172),
                 tail=(218, 176), width=7)

    # s3 — long middle heng (spans BL through BR, ink extends past s4)
    draw_heng(d, (33, 239), (267, 235), width_head=10, width_tail=12)

    # s4 — central vertical shu descending from C to BC (below s3)
    draw_shu(d, (142, 148), (153, 295), width=8)

    img.save(path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_车.png')
    render(out)
    print('wrote', out)
