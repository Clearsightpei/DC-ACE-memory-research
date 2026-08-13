# BANK_DEVIATION
# skipped: ren_left.py (whole 亻 radical), yuan_first.py (whole 元 whole-radical)
# reason: P-A-006 — 5-6 stroke L-R chars gain A/PASS via MMH-anchor-verbatim
#         stroke-primitive layer, avoiding double-transform of whole-radical
#         composition (P-COMP-009). 伉 = 亻+亢 sits squarely in this class.
# fresh_component: 亻+亢 stroke-primitive layout using MMH-derived pixel anchors.

"""伉 (kang) — 6 strokes, L-R (亻 + 亢).

Recipe: P-A-006 stroke-primitive layer, MMH anchors verbatim.
- s1: 亻 pie      (TL 90.8,66.8  → ML 16.4,199.5)
- s2: 亻 shu      (ML 68.3,155.0 → BL 70.3,291.5)
- s3: 亠 dian     (TC 148.5,65.9 → TC 187.8,94.3)
- s4: 亠 heng     (C 105.8,141.5 → MR 250.2,126.3)
- s5: 几 pie      (C 124.8,170.8 → BL 85.5,291.5)
- s6: 几 shu_wan_gou (C 145.0,173.7 → BR 269.2,229.7)
  MMH class is 横折弯钩 but the horizontal chomp of 几 is very short
  so shu_wan_gou primitive fits.

Joints (all N, small natural gaps):
- s1.mid(0.54) ⇆ s2.head at ML (~18 px gap): natural gap between the
  pie belly and the shu head (亻 canonical relation).
- s2.tail ⇆ s5.tail at BL (~21 px gap): 亻 shu bottom vs 几 pie tail.
- s5.head ⇆ s6.head at C (~16 px gap): the two 几 strokes are close
  but not welded at the top.
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                    "success_bank", "code"))
sys.path.insert(0, BANK)

from pie import draw_pie
from shu import draw_shu
from dian import draw_dian
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitives → 6 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all three joints implemented as N (no weld)
    'overall_pass': True,
    'notes': 'P-A-006 recipe. MMH anchors used as pixel coords verbatim.'
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 亻 pie — long TL→ML sweep with gentle bow
    draw_pie(d, (90.8, 66.8), (16.4, 199.5),
             bow_perp=13, w_head=9, w_tail=3, steps=90)

    # s2: 亻 shu — vertical descender, slight lean
    draw_shu(d, (68.3, 155.0), (70.3, 291.5), width=7)

    # s3: 亠 dian — small dot descending right at top of 亢
    draw_dian(d, (148.5, 65.9), (187.8, 94.3),
              w_head=3, w_tail=8, bow=4, steps=48)

    # s4: 亠 heng — long horizontal, spans C to MR
    draw_heng(d, (105.8, 141.5), (250.2, 126.3),
              width_head=8, width_tail=10)

    # s5: 几 pie — left leg, curves down-left
    draw_pie(d, (124.8, 170.8), (85.5, 291.5),
             bow_perp=10, w_head=8, w_tail=3, steps=80)

    # s6: 几 right leg — shu_wan_gou (descend, curve right, hook up)
    draw_shu_wan_gou(d, (145.0, 173.7), (269.2, 229.7),
                     width=7, bottom_extra=48, knee_ratio=0.72)

    out = os.path.join(os.path.dirname(__file__), '01_伉.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
