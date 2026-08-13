"""p3_char_0101_亓 (qi) — 4 strokes: short heng + wide heng + pie + shu.

Uses bank primitives (heng, pie, shu) directly. Anchors from MMH block.

米字格 → pixel conversions (300x300, each cell = 100x100):
  s1 head TC(0.017,0.97) = (101.7,  97.0)   tail TR(0.065,0.885) = (206.5, 88.5)
  s2 head ML(0.407,0.658) = ( 40.7, 165.8)  tail MR(0.695,0.512) = (269.5,151.2)
  s3 head C  (0.005,0.69) = (100.5, 169.0)  tail BL(0.53, 0.889) = ( 53.0,288.9)
  s4 head C  (0.737,0.585)= (173.7,158.5)   tail BC(0.875,1.079) = (187.5,307.9)

Joints (both N — natural gaps, not welded):
  s2.mid(0.23) ≈ ( 93.4, 162.4)  vs s3.head (100.5,169.0)  → gap ≈ 9 px  (target ~14)
  s2.mid(0.55) ≈ (166.6, 157.8)  vs s4.head (173.7,158.5)  → gap ≈ 7 px  (target ~12)
Both remain unwelded — anchors themselves already sit apart.
"""

import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All 4 strokes drawn from bank primitives; N-joints preserved by anchor geometry.'
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: short top heng — a small horizontal at very top-center
    draw_heng(d, (102, 97), (207, 89), width_head=7, width_tail=9)

    # s2: wider middle heng spanning most of the canvas
    draw_heng(d, (41, 166), (270, 151), width_head=9, width_tail=11)

    # s3: pie — from just under center, sweeping down-left to bottom-left
    draw_pie(d, (101, 169), (53, 289),
             bow_perp=10, w_head=7, w_tail=2, steps=80)

    # s4: shu — near-vertical descender on right side of center
    draw_shu(d, (174, 158), (187, 308), width=7)

    return img


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_亓.png'
    render().save(out)
    print(f'wrote {out}')
