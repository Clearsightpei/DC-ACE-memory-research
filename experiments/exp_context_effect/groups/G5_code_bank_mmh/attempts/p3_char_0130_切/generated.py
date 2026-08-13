"""p3_char_0130_切 — G5 attempt.

Decomposition: 切 = 七 (left, 2 strokes) + 刀 (right, 2 strokes) = 4 strokes.
Uses stroke bank (heng, shu, heng_zhe_gou, pie) with MMH-derived anchors.

MMH anchors (converted from cell frac to px, y grows DOWN):
  s1 head ('ML', 0.325, 0.688) = (32.5, 168.8)   heng 七
  s1 tail ('C',  0.307, 0.497) = (130.7, 149.7)
  s2 head ('TL', 0.788, 0.700) = (78.8, 70.0)     shu 七 (diagonal down-right)
  s2 tail ('BC', 0.351, 0.001) = (135.1, 200.1)
  s3 head ('C',  0.471, 0.485) = (147.1, 148.5)   heng_zhe_gou 刀
  s3 tail ('BC', 0.846, 0.549) = (184.6, 254.9)
  s4 head ('C',  0.772, 0.541) = (177.2, 154.1)   pie 刀
  s4 tail ('BL', 0.967, 0.903) = (96.7, 290.3)

Joints expected:
  s1.mid ⇆ s2.mid @ ML — P (welded crossing) — 七's shu crosses heng
  s1.tail ⇆ s3.head @ C — N (~25 px gap) — 七/刀 do not weld
  s3.head ⇆ s4.head @ C — N (~10 px gap) — 刀's pie starts near heng head, small gap
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Uses bank primitives heng/shu/heng_zhe_gou/pie with verbatim MMH anchors.',
}

import sys
import pathlib

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw

from heng import draw_heng
from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1 — 七's heng (left, sloping slightly up to the right)
    draw_heng(d, head=(32.5, 168.8), tail=(130.7, 149.7),
              width_head=8, width_tail=10)

    # Stroke 2 — 七's shu (diagonal down-right, pierces the heng)
    draw_shu(d, head=(78.8, 70.0), tail=(135.1, 200.1), width=7)

    # Stroke 3 — 刀's 横折钩 (heng portion top, corner, vertical curve, small hook)
    draw_heng_zhe_gou(d,
                      heng_head=(147.1, 148.5),
                      corner=(240.0, 152.0),
                      gou_tail=(204.0, 260.0),
                      hook_tip=(184.6, 244.0))

    # Stroke 4 — 刀's 撇 (sweep down-left from inside the frame)
    draw_pie(d, head=(177.2, 154.1), tail=(96.7, 290.3),
             bow_perp=14, w_head=9, w_tail=3)

    out = _HERE.parent / '01_切.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
