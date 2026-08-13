# BANK_DEVIATION
# skipped: yao_tiny.py (幺) — MMH 仫 right radical is 么 (3 strokes: pie + pie_zhe + na),
#          not 幺; the yao_tiny geometry (幺 = 撇折+撇折+dian) does not match.
# reason: right radical is 么 with anchors requiring pie/pie_zhe/na endpoints outside
#         yao_tiny's canonical positions.
# fresh_component: mo_right_variant_for_仫 (3-stroke inline 么 sized/placed per MMH)

"""仫 (mu) = 亻 (left, 2 strokes) + 么 (right, 3 strokes). Total 5 strokes.

Left: reuse draw_ren_left translated by (ox=-60, oy=-5) so its endpoints
match the MMH anchors for s1 and s2 within the ±0.20 tolerance.

Right (么): inline 3 strokes derived from MMH anchors:
  s3 = pie (top-right down to mid-lower-left)
  s4 = pie_zhe (fold stroke going down then right)
  s5 = na-like tail
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from ren_left import draw_ren_left  # noqa: E402
from pie import draw_pie  # noqa: E402
from pie_zhe import draw_pie_zhe  # noqa: E402
from na import draw_na  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 5 turtle/PIL stroke calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'ren_left translated (ox=-60, oy=-5); 么 inlined (pie + pie_zhe + na).'
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Left radical 亻 (s1 + s2) via bank primitive, translated ----
    draw_ren_left(d, ox=-60, oy=-5, scale=1.0)
    # s1_head≈(98.8,68.8) vs MMH (99, 65.6) OK
    # s1_tail≈(20.6,206.2) vs MMH (19.9, 206.5) OK
    # s2_head≈(78.9,153.2) vs MMH (72.9, 158.5) OK
    # s2_tail≈(84.1,287.7) vs MMH (76.8, 298.8) OK

    # ---- Right radical 么 (s3 + s4 + s5), inline ----
    # s3: top 撇 from TC(170.5, 92.3) → BC(110.2, 200.7)
    draw_pie(d, head=(170.5, 92.3), tail=(110.2, 200.7),
             bow_perp=10, w_head=8, w_tail=3, steps=80)

    # s4: 撇折-like stroke going head (186, 164.6) → tail (229.1, 253.1).
    # MMH treats this as a fold: pie start slanting down-left, corner, then heng-like tail.
    draw_pie_zhe(d,
                 head=(186.0, 164.6),
                 corner=(178.0, 230.0),
                 tail=(229.1, 253.1),
                 pie_bow=6, zhe_bow=2, w_head=7, w_corner=6, w_tail=5)

    # s5: na-like ending stroke from BR(215.3, 214.2) → BR(252.2, 278.0).
    # Slight rightward-bowed sweep, thickening to tail.
    draw_na(d, head=(215.3, 214.2), tail=(252.2, 278.0),
            bow_perp=10, w_head=4, w_tail=10, steps=80)

    out = Path(__file__).parent / '01_仫.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
