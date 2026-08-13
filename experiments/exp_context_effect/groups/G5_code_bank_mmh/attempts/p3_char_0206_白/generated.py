"""p3_char_0206_白 — 5 strokes: pie + shu + heng_zhe_box + middle heng + bottom heng.

Uses G5 bank primitives (pie, shu, heng_zhe_box, heng) with MMH-derived anchors.
Very close cousin of 日 (ri_sun.py) but with an added top 撇 and slightly
different box proportions.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from pie import draw_pie
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 5 primitive calls, matches MMH
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all 5 joints are class N (natural gap), inherent
    'overall_pass': True,
    'notes': 'pie on top; box = shu (s2) + heng_zhe_box (s3); 2 hengs inside.'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # MMH-derived anchors (3x3 米字格 cells, 100 px each on 300x300 canvas)
    # s1 pie: TC(0.315, 0.63) -> ML(0.914, 0.43)
    s1_head = (131.5, 63.0)
    s1_tail = (91.4, 143.0)
    # s2 shu (left of box): ML(0.539, 0.436) -> BL(0.855, 0.742)
    s2_head = (53.9, 143.6)
    s2_tail = (85.5, 274.2)
    # s3 heng_zhe (top+right of box): ML(0.688, 0.453) -> BR(0.036, 0.862)
    s3_head = (68.8, 145.3)
    s3_tail = (203.6, 286.2)
    # s4 middle heng: BL(0.841, 0.019) -> C(0.816, 0.96)
    s4_head = (84.1, 201.9)
    s4_tail = (181.6, 196.0)
    # s5 bottom heng: BL(0.911, 0.561) -> BC(0.919, 0.528)
    s5_head = (91.1, 256.1)
    s5_tail = (191.9, 252.8)

    # s1 pie — top diagonal sweeping down-left. Head upper-right, tail lower-left.
    draw_pie(d, s1_head, s1_tail, bow_perp=10, w_head=9, w_tail=3, steps=80)

    # s2 left 竖 of the box
    draw_shu(d, s2_head, s2_tail, width=8)

    # s3 横折 box: top-left = s3_head, bottom-right = s3_tail
    draw_heng_zhe_box(d, s3_head, s3_tail, width=8)

    # s4 middle 横 inside box (thinner)
    draw_heng(d, s4_head, s4_tail, width_head=6, width_tail=7)

    # s5 bottom 横 inside box (closes the box; heavier)
    draw_heng(d, s5_head, s5_tail, width_head=7, width_tail=8)

    out = pathlib.Path(__file__).parent / '01_白.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
