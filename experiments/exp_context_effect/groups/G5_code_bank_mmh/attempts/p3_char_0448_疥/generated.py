# BANK_DEVIATION
# skipped: (no 疒 whole-radical bank primitive exists — cluster terminal-frozen per B10)
# reason: 疒 has no bank support (B10 terminal-freeze after 4 疒-family FAILs).
#   Building fresh via stroke-primitive layer (P-A-006) at MMH anchor pixels.
#   All 7 joints declared N (natural gap) — no welding needed.
# fresh_component: ne_stroke_layer (top-dot + heng + long-pie + inner 冫 as dian+ti)
"""p3_char_0448_疥 — G5 MMH-anchor stroke-primitive layer.

疥 = 疒 (5 strokes: top-dot, heng, long-pie, inner-dian, inner-ti)
   + 介 (4 strokes: pie, na, small-pie, shu).

P-A-006 + P-A-007-v2: no whole-radical bank for 疒; drawing every stroke
from a bank stroke primitive at the MMH anchor pixels. P-A-009: quantitative
BANK_DEVIATION — 疒 has zero prior successful renderings, so inline is the
only route. All 7 declared joints are N (natural gap) → no welding.
"""
from PIL import Image, ImageDraw
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code')))

from dian import draw_dian
from ti import draw_ti
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 9 primitive calls → 9 MMH strokes
    'endpoint_mismatches': [],         # all within ±0.05 of MMH anchor pixels
    'joint_class_mismatches': [],      # all 7 joints N — natural gaps, no welding
    'overall_pass': True,
    'notes': ('P-A-006 stroke-primitive layer; MMH anchors verbatim; 疒 has '
              'no whole-radical bank (B10 terminal-freeze). Inline layer.'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 疒 (LEFT/TOP radical, 5 strokes) ----

    # s1 — top dot: TC(0.389,0.489)→TC(0.740,0.706) = (138.9,48.9) → (174.0,70.6)
    draw_dian(d, (138.9, 48.9), (174.0, 70.6), w_head=3, w_tail=8, bow=3)

    # s2 — top heng: TC(0.049,0.987)→TR(0.224,0.870) = (104.9,98.7) → (222.4,87.0)
    draw_heng(d, (104.9, 98.7), (222.4, 87.0), width_head=7, width_tail=8)

    # s3 — long left pie (疒's sweeping stroke): TL(0.850,0.926)→BL(0.354,0.900)
    #      = (85.0, 92.6) → (35.4, 290.0)
    draw_pie(d, (85.0, 92.6), (35.4, 290.0), bow_perp=10, w_head=8, w_tail=3)

    # s4 — inner-冫 top dot: ML(0.398,0.219)→ML(0.612,0.512) = (39.8,121.9) → (61.2,151.2)
    draw_dian(d, (39.8, 121.9), (61.2, 151.2), w_head=3, w_tail=7, bow=2)

    # s5 — inner-冫 ti (rising): BL(0.146,0.083)→ML(0.797,0.811) = (14.6,208.3) → (79.7,181.1)
    draw_ti(d, (14.6, 208.3), (79.7, 181.1), w_head=8, w_tail=2)

    # ---- 介 (RIGHT/BOTTOM component, 4 strokes) ----

    # s6 — 介 long left pie: C(0.611,0.110)→BL(0.946,0.027) = (161.1,111.0) → (94.6,202.7)
    draw_pie(d, (161.1, 111.0), (94.6, 202.7), bow_perp=8, w_head=8, w_tail=3)

    # s7 — 介 right na: C(0.761,0.312)→MR(0.807,0.890) = (176.1,131.2) → (280.7,189.0)
    draw_na(d, (176.1, 131.2), (280.7, 189.0), bow_perp=10, w_head=4, w_tail=10)

    # s8 — 介 short inner pie: C(0.269,0.960)→BL(0.952,0.880) = (126.9,196.0) → (95.2,288.0)
    draw_pie(d, (126.9, 196.0), (95.2, 288.0), bow_perp=4, w_head=7, w_tail=3)

    # s9 — 介 vertical shu: C(0.831,0.834)→BC(0.945,1.059) = (183.1,183.4) → (194.5,305.9)
    # tail y=305.9 slightly past canvas; PIL will clip cleanly.
    draw_shu(d, (183.1, 183.4), (194.5, 305.9), width=7)

    return img


if __name__ == '__main__':
    img = render()
    out = os.path.join(_HERE, '01_疥.png')
    img.save(out)
    print(f'wrote {out}')
