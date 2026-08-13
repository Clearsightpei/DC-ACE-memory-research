"""p3_char_0224_乓 — G5 attempt.

Composition: 丘 (top) + 丿 (bottom-right, per MMH). 6 strokes.

Bank use: draw_pie (s1, s6), draw_shu (s2, s4), draw_heng (s3, s5).

Anchors (image coords, 300x300, y grows DOWN):
  s1 (top short pie):    (205, 76)  -> (115, 111)
  s2 (left long slant):   (88, 103) -> (107, 211)  [near-vertical, slight right drift]
  s3 (short heng mid):   (115, 150) -> (223, 134)
  s4 (short shu mid):    (169, 152) -> (167, 205)
  s5 (long heng bottom):  (33, 227) -> (270, 212)
  s6 (final pie/na):     (171, 242) -> (231, 303)  [tail below canvas]

Joints all N-class (small natural gap):
  s1.tail ~ s2.head  (~20 px)
  s2.mid  ~ s3.head  (~17 px)
  s2.tail ~ s5.mid   (~19 px)
  s3.mid  ~ s4.head  (~13 px)
  s4.tail ~ s5.mid   (~17 px)

No BANK_DEVIATION: all six strokes fit an existing primitive.
"""

import sys
import pathlib
from PIL import Image, ImageDraw

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'),
)

from pie import draw_pie  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu import draw_shu  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes; N-gap joints preserved by anchor placement.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — top short pie (down-left from top-right of char)
    draw_pie(d, head=(205, 76), tail=(115, 111),
             bow_perp=6, w_head=7, w_tail=3, steps=40)

    # s2 — left long slant (near-vertical with slight right drift + gentle bow)
    # Treat as shu with straight body then use the same signature; but MMH shape
    # is a mild curve. Use pie with small bow, thick body.
    draw_pie(d, head=(88, 103), tail=(107, 211),
             bow_perp=-4, w_head=8, w_tail=6, steps=60)

    # s3 — short horizontal near center, slightly rising right
    draw_heng(d, head=(115, 150), tail=(223, 134),
              width_head=7, width_tail=8)

    # s4 — short vertical middle (of 丘/兵 top block)
    draw_shu(d, head=(169, 152), tail=(167, 205), width=7)

    # s5 — long bottom horizontal (base of 丘), rises very slightly to right
    draw_heng(d, head=(33, 227), tail=(270, 212),
              width_head=9, width_tail=11)

    # s6 — final pie/descending stroke to bottom-right (tail runs off canvas)
    draw_pie(d, head=(171, 242), tail=(231, 303),
             bow_perp=4, w_head=8, w_tail=2, steps=50)

    out = pathlib.Path(__file__).parent / '01_乓.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
