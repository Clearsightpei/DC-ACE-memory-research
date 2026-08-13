"""G5 attempt: p2_radical_076_小 (3 strokes).

MMH anchors (300x300 canvas, 米字格 3x3 cells):
 - s1 (center shu-gou): head TC(0.418, 0.735)=(141.8, 73.5) → tail BC(0.049, 0.672)=(104.9, 267.2)
 - s2 (left pie/dian):  head ML(0.82, 0.605)=(82.0, 160.5) → tail BL(0.498, 0.197)=(49.8, 219.7)
 - s3 (right dian):     head MR(0.077, 0.553)=(207.7, 155.3) → tail BR(0.575, 0.089)=(257.5, 208.9)

Uses promoted bank primitives (shu_gou, pie, dian) — no BANK_DEVIATION.
Joint expectations: NONE (strokes do not meet).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes, no joints. Center shu_gou (small hook), left pie sweeps down-left, right dian sweeps down-right.',
}

import sys
import pathlib
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from shu_gou import draw_shu_gou
from pie import draw_pie
from dian import draw_dian


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: center 竖钩 (vertical with small hook to lower-left)
    draw_shu_gou(d, head=(142, 74), tail=(105, 267), width=7, hook_start_offset=35)

    # s2: left 撇 — short leftward slanted stroke
    draw_pie(d, head=(82, 161), tail=(50, 220), bow_perp=6, w_head=8, w_tail=3, steps=60)

    # s3: right 点 — short down-right tapered dot (thicker at tail)
    draw_dian(d, head=(208, 155), tail=(258, 209), w_head=3, w_tail=8, bow=4, steps=48)

    out = pathlib.Path(__file__).parent / '01_小.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
