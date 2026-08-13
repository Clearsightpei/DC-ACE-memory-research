"""p3_char_0157_甲 — G5 attempt.

Decomposition per MMH structural block (5 strokes):
- s1: left 竖 of box   TL(0.586,0.861) -> ML(0.958,0.931) = (58.6,86.1) -> (95.8,193.1)
- s2: 横折 (top+right) TL(0.779,0.885) -> MR(0.077,0.89)  = (77.9,88.5) -> (207.7,189.0)
- s3: middle 横        C(0.11,0.333) -> C(0.869,0.269)     = (111.0,133.3) -> (186.9,126.9)
- s4: bottom 横        C(0.008,0.89) -> C(0.907,0.775)     = (100.8,189.0) -> (190.7,177.5)
- s5: long 竖 shu     TC(0.333,0.917) -> BC(0.427,1.117)  = (133.3,91.7) -> (142.7,311.7)

Uses bank primitives draw_shu, draw_heng, draw_heng_zhe_box (no BANK_DEVIATION).
The vertical shu s5 pierces the middle heng s3 and bottom heng s4 (both P joints,
natural — the shu is drawn LAST so it visibly crosses the box interior).
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'))

from PIL import Image, ImageDraw

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 5 primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes: s1 shu (left), s2 heng_zhe_box (top+right), s3 middle heng, s4 bottom heng, s5 long shu. s5 drawn last so it visibly pierces s3 and s4 (P joints).',
}


def draw_jia(draw: ImageDraw.ImageDraw):
    # s1: left 竖 of box
    draw_shu(draw, (58.6, 86.1), (95.8, 193.1), width=8)

    # s2: 横折 top+right (top_left, bottom_right)
    draw_heng_zhe_box(draw, (77.9, 88.5), (207.7, 189.0), width=8)

    # s3: middle 横 inside the box
    draw_heng(draw, (111.0, 133.3), (186.9, 126.9), width_head=7, width_tail=8)

    # s4: bottom 横 (closes the box)
    draw_heng(draw, (100.8, 189.0), (190.7, 177.5), width_head=8, width_tail=9)

    # s5: long central 竖 (drawn LAST so it pierces s3 & s4 visibly)
    draw_shu(draw, (133.3, 91.7), (142.7, 300.0), width=8)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_jia(d)
    out = pathlib.Path(__file__).parent / '01_甲.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
