"""G5 attempt: p2_radical_098_火 (4 strokes).

Decomposition per MMH-injected anchors (300x300 canvas, 3x3 米字格,
each cell 100x100):
  s1 left dot (点向右下): (63,144) -> (93,185)    [ML cell]
  s2 right dot (点向左下): (209,119) -> (172,173) [MR -> C cell]
  s3 big pie (撇):        (128, 74) -> (51, 290)  [TC -> BL cell]
  s4 big na  (捺):        (150,190) -> (274, 293) [C  -> BR cell]

Joint: s3.mid(0.53) ~ (87,188) and s4.head (150,190) are class N
(natural gap ~22px). No welding.

Bank primitives used: dian (s1, s2), pie (s3), na (s4). All bank
primitives from success_bank/code/ — no BANK_DEVIATION needed.
"""

import sys, pathlib
from PIL import Image, ImageDraw

_HERE = pathlib.Path(__file__).resolve()
_BANK = _HERE.parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(_BANK))

from dian import draw_dian
from pie import draw_pie
from na import draw_na


def cell_anchor(cell, xf, yf):
    """米字格 3x3 -> pixel on 300x300 canvas."""
    origins = {
        'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
        'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }
    ox, oy = origins[cell]
    return (ox + xf * 100, oy + yf * 100)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: left dot — head thin (up-left), tail thicker (down-right)
    h1 = cell_anchor('ML', 0.633, 0.436)   # (63, 143.6)
    t1 = cell_anchor('ML', 0.926, 0.854)   # (92.6, 185.4)
    draw_dian(d, h1, t1, w_head=3, w_tail=7, bow=3, steps=48)

    # s2: right dot — head upper-right, tail lower-left (points inward/down)
    h2 = cell_anchor('MR', 0.092, 0.189)   # (209.2, 118.9)
    t2 = cell_anchor('C',  0.72,  0.731)   # (172.0, 173.1)
    draw_dian(d, h2, t2, w_head=2, w_tail=6, bow=3, steps=48)

    # s3: main 撇 — from upper-center down to lower-left, gentle bow.
    # Negative bow so belly curves to the RIGHT of travel direction
    # (image left) matching the GT's slight leftward arch.
    h3 = cell_anchor('TC', 0.277, 0.735)   # (127.7, 73.5)
    t3 = cell_anchor('BL', 0.51,  0.895)   # (51.0, 289.5)
    draw_pie(d, h3, t3, bow_perp=4, w_head=7, w_tail=3, steps=80)

    # s4: 捺 — from center down to bottom-right, thickening.
    h4 = cell_anchor('C',  0.503, 0.901)   # (150.3, 190.1)
    t4 = cell_anchor('BR', 0.736, 0.927)   # (273.6, 292.7)
    draw_na(d, h4, t4, bow_perp=6, w_head=3, w_tail=9, steps=80)

    out = _HERE.parent / '01_火.png'
    img.save(out)
    print(f'wrote {out}')


SELF_CHECK = {
    'visual_ok': None,  # set after first render + revision decision
    'stroke_count_ok': True,      # 4 strokes drawn (dian, dian, pie, na)
    'endpoint_mismatches': [],    # anchors used exactly as MMH-derived
    'joint_class_mismatches': [], # s3.mid vs s4.head gap ~63px chord,
                                  # after ink radii ~10+4, effective gap
                                  # ~50px — larger than expected 22px but
                                  # still class N (non-welded).
    'overall_pass': None,
    'notes': ('Left dot + right dot + main 撇 + 捺. All bank primitives; '
              'no BANK_DEVIATION. Bow tuned down on 撇 since GT curve '
              'is nearly straight.')
}


if __name__ == '__main__':
    main()
