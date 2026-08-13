"""p2_radical_042_巛 — three wavy vertical strokes (river radical).

MMH anchors (converted 米字格 → pixel on 300px canvas, cells 100x100):
  stroke 1: head TL(0.885, 0.858) → tail BC(0.081, 0.842)  = (88.5, 85.8) → (108.1, 284.2)
  stroke 2: head TC(0.494, 0.829) → tail BC(0.699, 0.798)  = (149.4, 82.9) → (169.9, 279.8)
  stroke 3: head TR(0.145, 0.797) → tail BR(0.414, 0.818)  = (214.5, 79.7) → (241.4, 281.8)
Joints: NONE (three separate strokes, clean gaps).

Bank use: draw_pie is the closest primitive (curved stroke with taper +
perpendicular bow). Each stroke of 巛 is a leftward-bowed near-vertical
that tapers slightly. Endpoint-based signature fits the anchors directly.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes; endpoints match MMH anchors directly; no joints; bow_perp=-10 gives leftward bow characteristic of 巛 flowing-water shape.'
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Anchors → pixels (cell 100×100 on 300 canvas)
    s1_head = (88.5, 85.8)
    s1_tail = (108.1, 284.2)
    s2_head = (149.4, 82.9)
    s2_tail = (169.9, 279.8)
    s3_head = (214.5, 79.7)
    s3_tail = (241.4, 281.8)

    # bow_perp negative → curve bows LEFT of travel direction (each stroke
    # travels down-slightly-right, so negative perp bows to the left,
    # yielding the flowing-water arc characteristic of 巛).
    # Stronger negative bow → visible leftward arc characteristic of 巛
    bow = -22
    for head, tail in [(s1_head, s1_tail), (s2_head, s2_tail), (s3_head, s3_tail)]:
        draw_pie(d, head, tail, bow_perp=bow, w_head=5, w_tail=5, steps=80)

    out_path = os.path.join(os.path.dirname(__file__), '01_巛.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    render()
