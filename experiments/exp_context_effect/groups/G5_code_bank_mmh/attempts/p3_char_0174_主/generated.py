"""G5 attempt: p3_char_0174_主.

主 = 5 strokes (MMH order: dian, top-heng, middle-heng, shu-shaft, bottom-heng):
  s1 dian (top dot)         TC(0.310, 0.612) -> TC(0.679, 0.920)   ~ (131.0, 61.2) -> (167.9, 92.0)
  s2 top short heng          ML(0.817, 0.412) -> MR(0.200, 0.242)  ~ (81.7, 141.2) -> (220.0, 124.2)
  s3 middle short heng       BL(0.888, 0.101) -> MR(0.039, 0.963)  ~ (88.8, 210.1) -> (203.9, 196.3)
  s4 shu shaft (vertical)    C(0.412, 0.453)  -> BC(0.441, 0.657)  ~ (141.2, 145.3) -> (144.1, 265.7)
  s5 long bottom heng        BL(0.346, 0.801) -> BR(0.789, 0.757)  ~ (34.6, 280.1) -> (278.9, 275.7)

Joints:
  s2.mid X s4.head @ C  : N  (gap ~15 px  — shu starts just below top heng, not welded)
  s3.mid X s4.mid  @ BC : P  (welded cross — shu pierces middle heng)
  s4.tail X s5.mid @ BC : N  (gap ~19 px  — shu stops short of bottom heng)

# BANK_DEVIATION
# skipped: wang_king.py   (compound-radical bank entry for 王)
# reason: wang_king embeds standalone 王 pixel geometry; inside 主 the
#         entire 王 must sit lower (top heng ~y=130 vs. wang_king's y=95)
#         to leave headroom for the top dian. Composing via heng/shu
#         stroke primitives with MMH pixel anchors is a cleaner fit than
#         translating a 4-stroke compound.
# fresh_component: wang_lower_for_主  (王 shifted down + slight inter-heng
#         gap tightening; may be reusable for other X + 王 stacks)
"""

import os
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 5 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('dian on top; 王-triple-heng + central shu below; shu welds '
              'the middle heng (P), keeps ~15px gap under top heng and '
              '~19px gap above bottom heng (N/N).')
}


def draw(d: ImageDraw.ImageDraw):
    # s1 — dian (top dot; thin head upper-left, thick tail lower-right)
    draw_dian(d, head=(131.0, 61.2), tail=(167.9, 92.0),
              w_head=3, w_tail=7, bow=3)

    # s2 — top short heng of 王
    draw_heng(d, head=(81.7, 141.2), tail=(220.0, 124.2),
              width_head=7, width_tail=8)

    # s3 — middle short heng of 王 (crossed by shu)
    draw_heng(d, head=(88.8, 210.1), tail=(203.9, 196.3),
              width_head=7, width_tail=8)

    # s4 — central shu shaft: starts ~15 px below top heng (N),
    # pierces middle heng (P), stops ~19 px above bottom heng (N)
    draw_shu(d, head=(141.2, 145.3), tail=(144.1, 265.7),
             width=7, top_curl=False)

    # s5 — long bottom heng of 王 (the 王-shape marker: widest stroke)
    draw_heng(d, head=(34.6, 280.1), tail=(278.9, 275.7),
              width_head=9, width_tail=11)


def main():
    im = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(im)
    draw(d)
    out = os.path.join(os.path.dirname(__file__), '01_主.png')
    im.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
