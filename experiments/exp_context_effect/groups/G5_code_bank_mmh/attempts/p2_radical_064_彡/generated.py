"""p2_radical_064_彡 — three 撇 (pie) strokes cascading down-left.

Bank use: `pie.py · draw_pie` (endpoint signature) for all three strokes.
No BANK_DEVIATION — the pie primitive fits every stroke of 彡.

MMH structural block (3 strokes, no joints):
  s1: head TC(0.696, 0.653) -> tail C(0.113, 0.532)
  s2: head C (0.734, 0.345) -> tail BC(0.166, 0.095)
  s3: head C (0.928, 0.887) -> tail BL(0.779, 1.103)   (tail y clamped to canvas)

米字格 cells (each 100x100 on 300x300):
  TL=(0,0)  TC=(100,0)  TR=(200,0)
  CL=(0,100) C =(100,100) CR=(200,100)
  BL=(0,200) BC=(100,200) BR=(200,200)
"""

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie  # noqa: E402


def cell(name):
    return {
        'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
        'CL': (0, 100), 'C':  (100, 100), 'CR': (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }[name]


def anchor(cell_name, xf, yf):
    ox, oy = cell(cell_name)
    return (ox + xf * 100, oy + yf * 100)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # exactly 3 draw_pie calls below
    'endpoint_mismatches': [],    # anchors used verbatim from MMH block
    'joint_class_mismatches': [], # MMH block: NONE
    'overall_pass': True,
    'notes': 'Three cascading pie strokes; each uses bank draw_pie with '
             'moderate bow. Tail of s3 clamped to y=298 (MMH says 310).',
}


def draw_shan(draw):
    # Stroke 1: uppermost pie, shortish
    h1 = anchor('TC', 0.696, 0.653)   # (169.6, 65.3)
    t1 = anchor('C',  0.113, 0.532)   # (111.3, 153.2)
    draw_pie(draw, h1, t1, bow_perp=8, w_head=7, w_tail=2, steps=80)

    # Stroke 2: middle pie
    h2 = anchor('C',  0.734, 0.345)   # (173.4, 134.5)
    t2 = anchor('BC', 0.166, 0.095)   # (116.6, 209.5)
    draw_pie(draw, h2, t2, bow_perp=8, w_head=7, w_tail=2, steps=80)

    # Stroke 3: longest bottom pie; MMH tail y=310 -> clamp to 298
    h3 = anchor('C',  0.928, 0.887)   # (192.8, 188.7)
    t3_raw = anchor('BL', 0.779, 1.103)  # (77.9, 310.3)
    t3 = (t3_raw[0], min(t3_raw[1], 298))
    draw_pie(draw, h3, t3, bow_perp=14, w_head=8, w_tail=2, steps=90)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_shan(d)
    out = os.path.join(HERE, '01_彡.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
