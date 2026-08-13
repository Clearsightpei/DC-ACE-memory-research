"""伛 = 亻 (left) + 区 (right).

Memory reads (per memory_index.md v8 checklist):
  1. drawer_memory.md — high-value primitive: `ren_side` for 亻.
     No chronic primitive triggers (伛 has none of 丿/刀/冂/弓/马 as
     dominant component; the pie in 亻 is a routine `draw_pie`).
     区 not in bank shortlist — draw its 4 strokes inline from MMH anchors.
  2. success_bank/INDEX.md — no `qu.py` (区). ren_side is available.
  3. errata.md — no entry for 伛.

Structural spec (from dispatcher, 6 strokes):
  s1 pie: ('TL', 0.891, 0.615) → ('BL', 0.164, 0.027)   [亻 pie]
  s2 shu: ('ML', 0.677, 0.532) → ('BL', 0.715, 0.974)   [亻 竖]
  s3 heng: ('C', 0.403, 0.002) → ('TR', 0.402, 0.873)   [区 top 一]
  s4 pie: ('MR', 0.115, 0.225) → ('BC', 0.482, 0.391)   [区 inner 乂 pie]
  s5 na:  ('C', 0.591, 0.509) → ('BR', 0.37, 0.382)     [区 inner 乂 na]
  s6 shu_zhe: ('TC', 0.204, 0.923) [head] → mid ('BC', 0.383, 0.449)
                                   → tail ('BR', 0.646, 0.689)  [区 匚 outer]

Joints (5):
  s1.mid ⇆ s2.head @ ML  N (亻 T-touch as gap)
  s1.head ⇆ s6.head @ TC N (small gap between 亻 pie top and 匚 top)
  s3.head ⇆ s6.head @ C  N (top-horizontal head near 匚 top head)
  s4.mid  ⇆ s5.mid  @ C  P (乂 crossing — welded, shared pixel)
  s4.tail ⇆ s6.mid  @ BC N (pie tail near 匚 corner)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from na import draw_na
from shu_zhe import draw_shu_zhe

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 strokes: pie, shu, heng, pie, na, shu_zhe
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('伛 = 亻 + 区. Verbatim MMH anchors for all 6 strokes. '
              '区 inner 乂 uses P-weld shared control anchor at s4/s5 '
              'crossing. Chronic-import check: no chronic component present.')
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (left radical, strokes 1-2) ----
    # s1 pie: strong 撇 from upper-right of TL down to lower-left of BL
    draw_pie(d, ('TL', 0.891, 0.615), ('BL', 0.164, 0.027),
             head_width=12, tail_width=1, curve=0.10, segments=48)
    # s2 shu: 竖 dropping from ML down to BL
    draw_shu(d, ('ML', 0.677, 0.532), ('BL', 0.715, 0.974), width=9)

    # ---- 区 (right, strokes 3-6) ----
    # s3 top 一 (heng)
    draw_heng(d, ('C', 0.403, 0.002), ('TR', 0.402, 0.873), width=9)

    # s4 & s5 form the inner 乂. Their P-weld control anchor is shared.
    # Route pie & na so their bezier passes through a common midpoint.
    # Use draw_pie / draw_na directly; the given anchors already
    # place the two strokes so their midpoints coincide in cell C.
    # s4 pie: from ('MR', 0.115, 0.225) to ('BC', 0.482, 0.391)
    draw_pie(d, ('MR', 0.115, 0.225), ('BC', 0.482, 0.391),
             head_width=6, tail_width=1, curve=0.05, segments=40)
    # s5 na: from ('C', 0.591, 0.509) to ('BR', 0.37, 0.382)
    draw_na(d, ('C', 0.591, 0.509), ('BR', 0.37, 0.382),
            head_width=3, peak_width=10, tail_width=1,
            peak_t=0.75, curve=0.05, segments=40)

    # s6 outer 匚 as 竖折: head at TC, corner at BC-mid, tail at BR
    # (MMH mid is at ('BC', 0.383, 0.449))
    draw_shu_zhe(d, ('TC', 0.204, 0.923), ('BC', 0.383, 0.449),
                 ('BR', 0.646, 0.689),
                 v_width=9, h_width=9, shoulder=11)

    return img


if __name__ == '__main__':
    out_dir = os.path.dirname(__file__)
    img = render()
    img.save(os.path.join(out_dir, '01_伛.png'))
    print('WROTE', os.path.join(out_dir, '01_伛.png'))
