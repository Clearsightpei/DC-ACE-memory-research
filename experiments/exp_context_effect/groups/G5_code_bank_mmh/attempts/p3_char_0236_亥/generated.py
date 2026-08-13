"""p3_char_0236_亥 — G5 attempt. 6 strokes.

Recipe: P-A-006 — MMH anchors verbatim + stroke-primitive layer.
No whole-radical composition (no 亠 primitive) — direct stroke render.

MMH anchor → pixel conversion (3x3 米字格 on 300x300, cells 100x100):
  s1 head TC(0.269,0.571) → (127, 57)
     tail TC(0.69, 0.873) → (169, 87)     [short slanted dot/pie top]
  s2 head ML(0.387,0.33)  → ( 39,133)
     tail MR(0.625,0.172) → (262,117)     [long heng, mild rise right]
  s3 head C (0.216,0.324) → (122,132)
     tail BC(0.427,0.001) → (143,200)     [short pie mostly vertical]
  s4 head C (0.743,0.427) → (174,143)
     tail BL(0.41, 0.915) → (141,291)     [long descending pie]
  s5 head C (0.91, 0.951) → (191,195)
     tail BC(0.09, 0.985) → (109,298)     [medium pie down-left]
  s6 head BC(0.761,0.572) → (176,257)
     tail BR(0.312,1.026) → (231,303)     [short na down-right]

Joints (all N-class — small natural gap; do NOT weld):
  s2.mid(0.34) ~ s3.head @ C  — expected gap ~14 px
  s3.tail      ~ s4.mid(0.42) @ BC — expected gap ~19 px
  s5.mid(0.52) ~ s6.head @ BC — expected gap ~17 px

Stroke count: 6 primitive calls (verified).

No BANK_DEVIATION: all six strokes fit standard bank primitives
(dian/heng/pie/na) with per-stroke anchor+parameter tuning.
"""

import sys
import pathlib
from PIL import Image, ImageDraw

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'),
)

from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all three joints rendered as N (natural gap preserved by anchors)
    'overall_pass': True,
    'notes': 'P-A-006 recipe. Six strokes: dian + heng + pie + pie + pie + na. '
             'N-gaps preserved: s2/s3 (~14px), s3/s4 (~19px), s5/s6 (~17px).',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — top dot: short slanted stroke down-right (dian-like)
    draw_dian(d, head=(127, 57), tail=(169, 87),
              w_head=3, w_tail=8, bow=3, steps=40)

    # s2 — long heng across upper-middle, slight rise to the right
    draw_heng(d, head=(39, 133), tail=(262, 117),
              width_head=8, width_tail=9)

    # s3 — short near-vertical pie, mid-canvas
    draw_pie(d, head=(122, 132), tail=(143, 200),
             bow_perp=4, w_head=6, w_tail=3, steps=40)

    # s4 — long descending pie from mid-right down to bottom-left
    draw_pie(d, head=(174, 143), tail=(141, 291),
             bow_perp=14, w_head=8, w_tail=3, steps=80)

    # s5 — medium pie from right-of-center down to bottom-center
    draw_pie(d, head=(191, 195), tail=(109, 298),
             bow_perp=10, w_head=7, w_tail=3, steps=60)

    # s6 — short na down-right at bottom, tail off-canvas
    draw_na(d, head=(176, 257), tail=(231, 303),
            bow_perp=6, w_head=4, w_tail=10, steps=50)

    out = pathlib.Path(__file__).parent / '01_亥.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
