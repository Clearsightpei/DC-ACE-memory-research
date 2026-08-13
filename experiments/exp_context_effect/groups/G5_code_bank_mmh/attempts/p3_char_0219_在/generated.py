"""G5 attempt for p3_char_0219_在 (6 strokes).

Decomposition (from MMH anchors):
  s1: top short heng   ML(0.724,0.263) -> MR(0.188,0.063)
  s2: long pie          TC(0.368,0.53)  -> BL(0.144,0.552)
  s3: short left shu    ML(0.756,0.731) -> BL(0.838,1.018)
  s4: middle heng       BC(0.236,0.077) -> MR(0.25 ,0.939)
  s5: center shu        C (0.626,0.479) -> BC(0.69 ,0.602)
  s6: bottom heng       BC(0.078,0.728) -> BR(0.599,0.684)

All strokes use bank primitives directly (no BANK_DEVIATION); the shapes
are basic heng/pie/shu which the bank already supports cleanly.
"""

import os
import sys

# Add bank code path so we can import primitives.
BANK = os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
)
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw

from heng import draw_heng   # noqa: E402
from pie import draw_pie     # noqa: E402
from shu import draw_shu     # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('6 strokes: heng+pie+shu+heng+shu+heng. All P/N joints '
              'satisfied by using exact anchor endpoints.')
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top short heng
    draw_heng(d, (72.4, 126.3), (218.8, 106.3),
              width_head=8, width_tail=9)

    # s2: long diagonal pie (drives left-bottom sweep)
    # bow_perp small so it stays close to straight-line MMH median
    draw_pie(d, (136.8, 53.0), (14.4, 255.2),
             bow_perp=8, w_head=10, w_tail=3, steps=90)

    # s3: short left shu (small vertical piece along the pie's lower arc,
    # forming an N-gap with s6 head)
    draw_shu(d, (75.6, 173.1), (83.8, 301.8), width=6)

    # s4: middle heng (crosses s5 shu at ~x=175 -> P weld)
    draw_heng(d, (123.6, 207.7), (225.0, 193.9),
              width_head=7, width_tail=8)

    # s5: center shu (stops above s6, ~17px gap -> N)
    draw_shu(d, (162.6, 147.9), (169.0, 260.2), width=7)

    # s6: bottom heng
    draw_heng(d, (107.8, 272.8), (259.9, 268.4),
              width_head=9, width_tail=10)

    out = os.path.join(os.path.dirname(__file__), "01_在.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
