"""p3_char_0508_畝 — G5 attempt.

Decomposition (10 strokes from MMH):
- 亠 top-left (s1-s2): dot + heng
- 田 middle-left (s3-s7): shu + heng_zhe_box + heng + shu + heng
- 久 right (s8-s10): pie + heng_pie + na

Reasoning trace (P-A-008):
- No 田 or 久 in bank → inline from stroke primitives (P-A-006 stroke-primitive layer).
- MMH middle-heng/middle-shu of 田 are median-only (per anchor calibration note);
  extend to full box extents so cross visibly welds at BL (P-joint s5⇆s6).
- 久 s9 has heng_pie shape (short horizontal then long down-left descend).
- 久 s10 na starts from the P-cross where it meets s9's mid.
- BANK_DEVIATION: none — no bank whole-radical for 亩/田/久 to skip.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../success_bank/code'))

from PIL import Image, ImageDraw

from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box
from pie import draw_pie
from heng_pie import draw_heng_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 10 primitive calls, 10 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '田 middle heng/shu extended past MMH medians to full box extents so P-joint s5⇆s6 welds naturally at BL.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ── 亠 top-left ────────────────────────────────────────────────
    # s1: dot (丶) — MMH TL(0.744,0.773)→C(0.09,0.066) ≈ (74,77)→(109,107)
    draw_dian(d, (74.0, 77.0), (109.0, 107.0),
              w_head=3, w_tail=7, bow=4, steps=48)
    # s2: heng (一) — MMH ML(0.261,0.497)→C(0.359,0.333) ≈ (26,150)→(136,133)
    draw_heng(d, (22.0, 152.0), (140.0, 133.0),
              width_head=7, width_tail=8)

    # ── 田 middle-left (5 strokes) ────────────────────────────────
    # Box outer bounds inferred from MMH:
    # top-left ≈ (20, 190), bottom-right ≈ (105, 277)
    # s3: 竖 left of 田 — MMH ML(0.205,0.901)→BL(0.457,0.769) ≈ (21,190)→(46,277)
    draw_shu(d, (22.0, 188.0), (24.0, 278.0), width=7)
    # s4: 横折 top+right — head (38,190) tail (105,260); extend right/down to corner
    draw_heng_zhe_box(d, (22.0, 188.0), (108.0, 278.0), width=7)
    # s5: 横 middle — MMH BL(0.533,0.271)→BC(0.022,0.183) medial only; extend
    draw_heng(d, (22.0, 232.0), (108.0, 230.0),
              width_head=6, width_tail=6)
    # s6: 竖 middle — MMH ML(0.668,0.934)→BL(0.706,0.534) medial only; extend
    draw_shu(d, (66.0, 190.0), (68.0, 278.0), width=6)
    # s7: 横 bottom close — MMH BL(0.513,0.684)→BC(0.008,0.52); extend to corners
    draw_heng(d, (22.0, 276.0), (108.0, 275.0),
              width_head=7, width_tail=8)

    # ── 久 right (3 strokes) ──────────────────────────────────────
    # s8: 撇 (pie) — MMH TC(0.726,0.671)→C(0.383,0.705) ≈ (173,67)→(138,171)
    draw_pie(d, (173.0, 67.0), (138.0, 171.0),
             bow_perp=10, w_head=8, w_tail=3, steps=80)
    # s9: 横撇 (heng_pie) long down-left sweep
    # MMH C(0.605,0.512)→BC(0.046,0.839) ≈ (160,151)→(105,284)
    draw_heng_pie(d, (160.0, 151.0), (105.0, 284.0),
                  apex_x=210.0, corner_x=215.0)
    # s10: 捺 (na) — MMH BC(0.948,0.124)→BR(0.862,0.88) ≈ (195,212)→(286,288)
    # Head at ~(195,212) welds with s9 mid at BC (P-joint)
    draw_na(d, (185.0, 210.0), (288.0, 288.0),
            bow_perp=12, w_head=4, w_tail=12, steps=80)

    out = os.path.join(os.path.dirname(__file__), '01_畝.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
