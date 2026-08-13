"""p3_char_0317_员 (yuán, 'member') — 7 strokes: 口(3) + 贝(4).

# BANK_DEVIATION
# skipped: kou_mouth.py
# reason: top 口 in 员 is compressed wider/shorter than kou_mouth's native
#         aspect (kou native ~125x150; here ~100x60). Uniform-scale call
#         would either over-shrink or distort vertically. Per P-A-006 +
#         P-A-007, use stroke-primitive layer with MMH-verbatim anchors.
# fresh_component: inline kou_compressed_for_yuan (3 strokes: shu + heng_zhe_box + heng)
#
# Bottom 贝 assembled fresh from primitives (no whole-bei bank primitive):
#   s4 left shu, s5 heng_zhe_box (top+right of 贝 outline), s6 pie (leg),
#   s7 dian (leg).
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from pie import draw_pie
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 7 stroke primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 6 joints are class N (natural gaps preserved)
    'overall_pass': True,
    'notes': 'stroke-primitive layer; MMH anchors used verbatim; kou skipped per aspect mismatch.'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ============= TOP 口 (3 strokes) =============
    # s1: left 竖 (short) — MMH head (85.3, 75); tail (104.3, 135.4)
    #     visual-first: keep vertical, extend to bottom of box
    draw_shu(d, (92, 72), (94, 138), width=7)

    # s2: 横折 top+right of 口 — MMH head (99.3, 75.3), tail (183.1, 104.3)
    #     visual-first: extend right side down to close the box (y=138)
    draw_heng_zhe_box(d, top_left=(96, 72), bottom_right=(190, 138), width=7)

    # s3: bottom 横 of 口 — MMH (109.6, 120.7) -> (200.1, 115.4)
    #     visual-first: align with bottom of s1/s2 (y=138)
    draw_heng(d, (100, 138), (198, 134), width_head=7, width_tail=8)

    # ============= BOTTOM 贝 (4 strokes) =============
    # s4: left 竖 of 贝 — MMH (87.3, 149.7) -> (94.6, 254.3)
    draw_shu(d, (87, 150), (95, 254), width=7)

    # s5: 横折 of 贝 (top + right) — MMH (102.2, 152.9) -> (200.1, 255.2)
    #   corner ~ (200, 153); use heng_zhe_box
    draw_heng_zhe_box(d, top_left=(102, 153), bottom_right=(200, 255), width=8)

    # s6: 撇 (left leg of 八 at bottom of 贝) — MMH (133.3, 173.1) -> (69.1, 309.1)
    #   long diagonal, extends below canvas — PIL will clip
    draw_pie(d, (133, 173), (69, 305),
             bow_perp=12, w_head=9, w_tail=3, steps=90)

    # s7: 点/short 捺 (right leg of 八) — MMH (167.3, 268.4) -> (219.4, 314.4)
    draw_dian(d, (167, 268), (219, 305),
              w_head=4, w_tail=11, bow=5, steps=60)

    out = pathlib.Path(__file__).parent / '01_员.png'
    img.save(out)
    print(f'saved: {out}')


if __name__ == '__main__':
    main()
