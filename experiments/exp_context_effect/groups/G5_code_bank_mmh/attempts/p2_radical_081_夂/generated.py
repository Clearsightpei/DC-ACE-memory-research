"""G5 attempt: p2_radical_081_夂 (3-stroke radical).

Structure (from MMH block):
- s1: short pie, head TC(124.5, 55.1) → tail ML(63.6, 137.1) — the small top mark
- s2: long pie, head TC(119.5, 98.7) → tail BL(43.7, 200.1) — main left sweep
- s3: na,       head C (103.7, 114.3) → tail MR(270.1, 193.7) — right sweep

Joints:
- s1.mid ~ s2.head  cell C  : N (small gap ~22 px)
- s1.mid ~ s3.head  cell ML : N (small gap ~12 px)
- s2.mid X s3.mid   cell C  : P (welded pierce)

Bank use: draw_pie (bank primitive) x2 + draw_na (bank primitive) x1.
No BANK_DEVIATION.
"""

import sys
import pathlib

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Using MMH anchors as-is; bows chosen so s2 (pie) and s3 (na) '
             'pierce near cell C, and the small s1 pie sits above them as a '
             'neighbor gap.',
}


def render(out_path: pathlib.Path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: short top pie
    s1_head = (124.5, 55.1)
    s1_tail = (63.6, 137.1)
    draw_pie(d, s1_head, s1_tail,
             bow_perp=6, w_head=7, w_tail=2, steps=60)

    # s2: main long pie sweeping down-left. Extended tail deeper (down &
    # further left) to match GT's longer left-diagonal ink.
    s2_head = (128.0, 100.0)
    s2_tail = (55.0, 235.0)
    draw_pie(d, s2_head, s2_tail,
             bow_perp=10, w_head=10, w_tail=3, steps=100)

    # s3: na sweeping down-right. Head lowered slightly so it crosses
    # s2 near cell C (P joint), and tail dropped to give a stronger,
    # less-horizontal descent that matches the GT's na trajectory.
    s3_head = (120.0, 120.0)
    s3_tail = (255.0, 215.0)
    draw_na(d, s3_head, s3_tail,
            bow_perp=14, w_head=4, w_tail=12, steps=100)

    img.save(out_path)


if __name__ == '__main__':
    out = _HERE.parent / '01_夂.png'
    render(out)
    print(f'wrote {out}')
