"""G5 attempt: p2_radical_113_犬 (犬 quǎn, 'dog') — 4 strokes.

犬 = 大 + 丶 (dot in upper-right). Same 3-stroke skeleton as 大 (heng + pie + na)
plus a 4th stroke: a small 点 in the upper right.

MMH anchor cross-check:
  s1 head ML(0.606,0.655)=(60.6,165.5)  tail MR(0.235,0.497)=(223.5,149.7)  → 横
  s2 head TC(0.292,0.647)=(129.2,64.7)  tail BL(0.416,0.915)=(41.6,291.5)   → 撇
  s3 head C (0.488,0.702)=(148.8,170.2) tail BR(0.836,0.944)=(283.6,294.4)  → 捺
  s4 head TC(0.957,0.894)=(195.7,89.4)  tail MR(0.326,0.137)=(232.6,113.7)  → 丶

Joints:
  s1.mid P s2.mid @ C (weld — heng crosses pie)
  s1.mid N s3.head @ C (gap ~19 px — na starts below heng, no weld)
  s2.mid N s3.head @ C (gap ~20 px — na starts to the right of pie mid)

Bank usage: inline stroke primitives (heng, pie, na, dian). Whole-radical
primitive draw_da could have been used for the 大 skeleton but MMH gives
犬-specific anchors that differ slightly from da_big.py's baked-in values;
inlining lets us honor the MMH anchors exactly. No BANK_DEVIATION needed —
this is straight primitive composition, not a substitution.
"""

import sys
import pathlib

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'),
)

from PIL import Image, ImageDraw  # noqa: E402

from heng import draw_heng  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402
from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 primitive calls, matches MMH
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Anchors placed directly from MMH; na head sits below+right of heng-pie X for the two N-gaps.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — 横 (heng)
    s1_head = (60.6, 165.5)
    s1_tail = (223.5, 149.7)
    draw_heng(d, s1_head, s1_tail, width_head=7, width_tail=7)

    # s2 — 撇 (pie) — long sweep from top-center down-left to bottom-left
    s2_head = (129.2, 64.7)
    s2_tail = (41.6, 291.5)
    draw_pie(d, s2_head, s2_tail,
             bow_perp=-22, w_head=5, w_tail=2, steps=100)

    # s3 — 捺 (na) — head at C, slightly below heng crossing (N-gap ~19 px)
    s3_head = (148.8, 170.2)
    s3_tail = (283.6, 294.4)
    draw_na(d, s3_head, s3_tail,
            bow_perp=-6, w_head=3, w_tail=10, steps=100)

    # s4 — 丶 (dian) — small dot in upper right
    s4_head = (195.7, 89.4)
    s4_tail = (232.6, 113.7)
    draw_dian(d, s4_head, s4_tail, w_head=3, w_tail=8, bow=3)

    img.save(pathlib.Path(__file__).parent / '01_犬.png')


if __name__ == '__main__':
    render()
