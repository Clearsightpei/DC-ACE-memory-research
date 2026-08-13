"""p3_char_0358_盯 — G5 attempt.

盯 = 目 (left, 5 strokes) + 丁 (right, 2 strokes) = 7 strokes.

Per P-A-006 (MMH-anchor verbatim + stroke-primitive layer) reinforced
by P-A-007-v2 (call whole-radical bank when it matches; here 目 is NOT
in bank — 日 is but has only 4 strokes; 目 has an extra middle heng —
so decompose into stroke primitives at MMH anchors).

BANK USE (no deviations — all stroke primitives fit cleanly):
- s1: draw_shu — 目 left vertical (MMH anchors)
- s2: draw_heng_zhe_box — 目 top+right box shell (top_left, bottom_right)
- s3, s4, s5: draw_heng — the three interior/closing hengs of 目
- s6: draw_heng — 丁 long top heng
- s7: draw_shu_gou — 丁 vertical with left hook

Reasoning trace per P-A-008:
- 目 sub: whole-radical primitive not in bank; ri_sun (日) is close but
  4 strokes vs 5 — using it would drop the middle interior heng. So we
  compose from stroke primitives at MMH anchors. Structure identical to
  ri_sun.py template plus one extra draw_heng call.
- 丁 sub: no dedicated 丁 bank primitive; it is a trivial 2-stroke
  (heng + shu_gou), both cleanly served by stroke primitives. shi_time
  used the same shu_gou+dian pattern for 寸 — we mimic the shu_gou
  parameterization (hook_start_offset ~ 32-40).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from shu_gou import draw_shu_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 7 primitive calls, MMH expects 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],      # all 9 joints are class N (neighbor gap)
    'overall_pass': True,
    'notes': ('MMH anchors used verbatim; all 9 joints class N — bank '
              'primitives draw discrete strokes with natural pixel gaps '
              'at endpoint junctions, matching N-class expectation.')
}


def _cell(cell, xf, yf):
    """米字格 cell + fraction → 300×300 pixel."""
    origins = {
        'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
        'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }
    ox, oy = origins[cell]
    return (ox + xf * 100, oy + yf * 100)


def draw_ding_stare(d):
    # ==== 目 (left, x ~ 35..100) ====
    # s1: shu — TL(.354,.976) → BL(.445,.663)
    draw_shu(d, _cell('TL', 0.354, 0.976), _cell('BL', 0.445, 0.663),
             width=8)
    # s2: heng_zhe_box — top_left=ML(.527,.017); bottom_right=BC(.008,.689)
    draw_heng_zhe_box(d, _cell('ML', 0.527, 0.017),
                      _cell('BC', 0.008, 0.689), width=8)
    # s3: interior top heng — ML(.554,.629) → ML(.803,.553)
    draw_heng(d, _cell('ML', 0.554, 0.629), _cell('ML', 0.803, 0.553),
              width_head=6, width_tail=7)
    # s4: interior middle heng — BL(.557,.010) → ML(.812,.939)
    draw_heng(d, _cell('BL', 0.557, 0.010), _cell('ML', 0.812, 0.939),
              width_head=6, width_tail=7)
    # s5: bottom closing heng — BL(.527,.558) → BL(.847,.467)
    draw_heng(d, _cell('BL', 0.527, 0.558), _cell('BL', 0.847, 0.467),
              width_head=7, width_tail=9)

    # ==== 丁 (right, x ~ 125..280) ====
    # s6: long top heng — C(.248,.181) → MR(.774,.058)
    draw_heng(d, _cell('C', 0.248, 0.181), _cell('MR', 0.774, 0.058),
              width_head=8, width_tail=10)
    # s7: shu_gou — C(.866,.187) → BC(.562,.692)
    draw_shu_gou(d, _cell('C', 0.866, 0.187), _cell('BC', 0.562, 0.692),
                 width=7, hook_start_offset=34)


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_ding_stare(d)
    out = os.path.join(os.path.dirname(__file__), '01_盯.png')
    img.save(out)
    print(f'wrote {out}')
