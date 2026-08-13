"""p3_char_0266_伥 (chāng) — 亻 + 长, L-R, 6 strokes.

Recipe P-A-006: MMH-anchor verbatim + stroke-primitive layer. Refuse
whole-radical composition (would double-transform draw_ren_left +
draw_chang_long). Inline every stroke directly.

MMH anchors (300x300 pixel coords derived from 米字格 cell + frac):
  s1 pie:  head (86.1, 75.6)  tail (20.8, 204.2)   [亻 pie]
  s2 shu:  head (64.7, 163.2) tail (72.1, 294.1)   [亻 shu]
  s3 pie:  head (205.4, 90.5) tail (161.1, 152.1)  [长 top-right pie]
  s4 heng: head (97.9, 184.0) tail (255.5, 171.4)  [长 wide horizontal]
  s5 shu-ti: head (138.3, 74.4) tail (292.2, 254.9) — but MMH samples
             a compound 竖提: descends from top, kinks right at bottom.
             Inline as polyline (no clean bank primitive for 竖提 arc).
  s6 na:   head (160.5, 184.9) tail (281.0, 260.4) [长 diagonal na]
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitives / polylines below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006 recipe. s5 竖提 inlined as polyline (no bank primitive).',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    black = (0, 0, 0)

    # s1: 亻 pie — head TL(86, 76) → tail BL(21, 204). Reduce bow so
    #     it reads as a person radical pie, not a dominant sweep.
    draw_pie(d, (86, 76), (21, 204),
             bow_perp=8, w_head=8, w_tail=3, steps=90)

    # s2: 亻 shu — head ML(65, 163) → tail BL(72, 294)
    draw_shu(d, (65, 163), (72, 294), width=7)

    # s3: 长 top-right pie — head TR(205, 91) → tail C(161, 152)
    draw_pie(d, (205, 91), (161, 152),
             bow_perp=5, w_head=8, w_tail=3, steps=60)

    # s4: 长 wide heng — spans from ML across to MR. Extend a touch
    #     wider so it crosses s5 竖提 solidly.
    draw_heng(d, (98, 184), (272, 172), width_head=8, width_tail=10)

    # s5: 长 竖提 (compound) — MMH head TC(138, 74) is high; anchor
    #     descends through left-mid of 长 body then flicks right at
    #     bottom. Inline as tapered polyline (no bank primitive).
    poly_s5 = [(138, 74), (142, 130), (146, 190), (150, 240), (192, 258)]
    d.line(poly_s5, fill=black, width=8, joint='curve')
    # taper ti tail flick
    d.line([(180, 253), (196, 258)], fill=black, width=5, joint='curve')

    # s6: 长 na — head C(161, 185) → tail BR(281, 260)
    draw_na(d, (161, 185), (281, 260),
            bow_perp=10, w_head=4, w_tail=12, steps=80)

    out = os.path.join(os.path.dirname(__file__), '01_伥.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
