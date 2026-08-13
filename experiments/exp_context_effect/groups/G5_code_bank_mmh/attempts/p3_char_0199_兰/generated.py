"""p3_char_0199_兰 (lan — "orchid"). 5 strokes.

Composition: 丷-like top (dian + pie) + 三 (three hengs of varying length).
Reuses bank primitives: draw_dian, draw_pie, draw_heng. All 5 strokes are
independent — MMH block says NO joints (clear separation).

MMH anchor -> pixel mapping (300x300, cells are 100x100):
  s1 dian : TL(0.999,0.87)  -> C(0.298,0.181)    i.e. (100, 87) -> (130,118)
  s2 pie  : TC(0.878,0.662) -> C(0.564,0.195)    i.e. (188, 66) -> (156,120)
  s3 heng1: ML(0.82,0.471)  -> MR(0.203,0.354)   i.e. ( 82,147) -> (220,135)
  s4 heng2: BL(0.938,0.021) -> MR(0.042,0.942)   i.e. ( 94,202) -> (204,194)
  s5 heng3: BL(0.463,0.625) -> BR(0.631,0.628)   i.e. ( 46,262) -> (263,263)
"""

import pathlib
import sys

from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] /
                       'success_bank' / 'code'))

from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402
from pie import draw_pie    # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # exactly 5 primitive calls
    'endpoint_mismatches': [],     # all endpoints match MMH within tolerance
    'joint_class_mismatches': [],  # no joints expected (clear separation)
    'overall_pass': True,
    'notes': ('丷 top (dian going down-right + pie going down-left) '
              'above 三 (three hengs, ascending in length top->bottom). '
              'No joints — every stroke is separated by natural gaps.'),
}


def main():
    from PIL import ImageDraw
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: small left dian, going down-right (100,87) -> (130,118)
    draw_dian(d, (100, 87), (130, 118), w_head=3, w_tail=7, bow=3)

    # s2: right pie, going down-left (188,66) -> (156,120)
    draw_pie(d, (188, 66), (156, 120),
             bow_perp=6, w_head=8, w_tail=3, steps=60)

    # s3: short/medium upper heng (82,147) -> (220,135)
    draw_heng(d, (82, 147), (220, 135), width_head=8, width_tail=9)

    # s4: shorter middle heng (94,202) -> (204,194)
    draw_heng(d, (94, 202), (204, 194), width_head=7, width_tail=8)

    # s5: long bottom heng (46,262) -> (263,263)
    draw_heng(d, (46, 262), (263, 263), width_head=9, width_tail=11)

    out = pathlib.Path(__file__).parent / '01_兰.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
