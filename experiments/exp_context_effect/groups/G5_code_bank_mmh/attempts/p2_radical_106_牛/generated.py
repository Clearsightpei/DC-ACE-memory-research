"""p2_radical_106_牛 — G5 attempt.

4 strokes: (1) top-left short 撇, (2) short upper 横, (3) long middle 横,
(4) long vertical 丨 piercing both 横 through center.

Using bank primitives: draw_pie, draw_heng, draw_shu.
No BANK_DEVIATION — primitives fit cleanly with endpoint anchors from MMH.

米字格 anchors (300×300, 3×3 grid of 100×100 cells):
  cell_origin[TL] = (0,0), TC=(100,0), TR=(200,0)
  cell_origin[ML] = (0,100), C=(100,100), MR=(200,100)
  cell_origin[BL] = (0,200), BC=(100,200), BR=(200,200)
  pixel = cell_origin + (x_frac * 100, y_frac * 100)
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from heng import draw_heng
from pie import draw_pie
from shu import draw_shu


def anchor(cell, xf, yf):
    origins = {
        'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
        'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }
    ox, oy = origins[cell]
    return (ox + xf * 100, oy + yf * 100)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('4 strokes: pie(TL->ML), heng(ML->MR upper), heng(BL->MR long), '
              'shu(TC->BC vertical). Shu pierces both hengs (P joints at C). '
              'Pie ends near s2 head with a small natural gap (N joint).')
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 撇 head @ TL(0.92,0.967)=(92,96.7)  tail @ ML(0.606,0.688)=(60.6,168.8)
    s1_head = anchor('TL', 0.92, 0.967)
    s1_tail = anchor('ML', 0.606, 0.688)
    draw_pie(d, s1_head, s1_tail, bow_perp=6, w_head=6, w_tail=2, steps=60)

    # Stroke 2: 短横 head @ ML(0.999,0.374)=(99.9,137.4) tail @ MR(0.153,0.207)=(215.3,120.7)
    s2_head = anchor('ML', 0.999, 0.374)
    s2_tail = anchor('MR', 0.153, 0.207)
    draw_heng(d, s2_head, s2_tail, width_head=7, width_tail=8)

    # Stroke 3: 长横 head @ BL(0.34,0.077)=(34,207.7) tail @ MR(0.701,0.901)=(270.1,190.1)
    s3_head = anchor('BL', 0.34, 0.077)
    s3_tail = anchor('MR', 0.701, 0.901)
    draw_heng(d, s3_head, s3_tail, width_head=8, width_tail=10)

    # Stroke 4: 丨 head @ TC(0.397,0.574)=(139.7,57.4) tail @ BC(0.532,1.182)=(153.2,318.2)
    # Clip tail to stay within 300 canvas.
    s4_head = anchor('TC', 0.397, 0.574)
    s4_tail_raw = anchor('BC', 0.532, 1.182)
    s4_tail = (s4_tail_raw[0], min(s4_tail_raw[1], 296))
    draw_shu(d, s4_head, s4_tail, width=7)

    out = Path(__file__).parent / '01_牛.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
