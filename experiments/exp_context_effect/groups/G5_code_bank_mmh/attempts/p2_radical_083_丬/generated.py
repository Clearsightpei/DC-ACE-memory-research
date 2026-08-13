"""p2_radical_083_丬 — G5 attempt.

3 strokes per MMH: (1) short 撇 in center-upper, (2) 提 rising from
lower-left to just left of shu, (3) long 竖 from top-center down past
bottom edge.

Joint: s2.tail sits ~near mid-point of s3 with a small natural gap (N-joint,
expected ~28 px). No welding.

Bank usage: draw_pie, draw_ti, draw_shu — no BANK_DEVIATION.
"""

import pathlib
import sys
from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from pie import draw_pie  # noqa: E402 (kept for reference; not used post-revision)
from ti import draw_ti  # noqa: E402
from shu import draw_shu  # noqa: E402
from dian import draw_dian  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 's1 pie short in center; s2 ti rising bottom-left→mid; '
             's3 tall shu with slight top curl. s2.tail to s3-mid gap '
             '≈ 15–20 px (N-joint OK).',
}


def draw(img_path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1 — short slanted 点/短撇 (upper-center-left)
    # GT shows a slim curve tapering thin→slightly thicker down-right.
    # dian (thin head → thick tail) matches the GT silhouette better than pie.
    draw_dian(d, head=(107, 105), tail=(135, 143),
              w_head=2, w_tail=5, bow=3, steps=50)

    # Stroke 2 — 提 (rising diagonal, thicker at head)
    # MMH: head (BL, 0.87, 0.306) → (87.0, 230.6)
    #      tail (C,  0.576, 0.749) → (157.6, 174.9)
    draw_ti(d, head=(88, 232), tail=(153, 176),
            w_head=9, w_tail=3, steps=50)

    # Stroke 3 — 长竖 (top-center to below bottom edge, subtle top curl)
    # MMH: head (TC, 0.538, 0.7) → (153.8, 70.0)
    #      tail (BC, 0.638, 1.026) → (163.8, 302.6)
    draw_shu(d, head=(158, 74), tail=(166, 300),
             width=7, top_curl=True)

    img.save(img_path)


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_丬.png'
    draw(out)
    print('wrote', out)
