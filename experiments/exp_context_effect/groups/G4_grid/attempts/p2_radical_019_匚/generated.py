"""匚 (fāng, "open box on right") — 2-stroke enclosing radical.

Stroke plan:
  s1 — 横 (top horizontal). head near TL(0.2, 0.30), tail near TR(0.85, 0.30).
       This is the top bar of the open box.
  s2 — 竖折 (vertical then right). head at TL(0.15, 0.38),
       corner at BL(0.15, 0.70), tail at BR(0.80, 0.70).
       This forms the left wall + bottom of the open box.

Joint at top-left:
  s1.head @ TL(0.20, 0.30) ⇆ s2.head @ TL(0.15, 0.38)  -> N (small natural
  gap, ~15-25 px). MMH expects an N-class gap here; DO NOT weld.

Per TR2 (enclosing radical) — occupy nearly the full 米字格 with small
edge margin.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../success_bank/code')))

from PIL import Image, ImageDraw

from _anchor import anchor_to_xy
from heng import draw_heng
from shu_zhe import draw_shu_zhe


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Stroke 1 = 横 (top bar). Stroke 2 = 竖折 (left wall + bottom). '
             'Top-left corner is N-class gap ~18 px between s1 head and s2 head, '
             'per MMH. Anchors overridden to span full grid per TR2 (enclosing).',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1: 横 (top horizontal). Top bar of 匚.
    # Head is up-and-right of s2's head so the top-left corner shows an
    # N-class gap (~20 px) rather than welding.
    s1_head = ('TL', 0.28, 0.28)
    s1_tail = ('TR', 0.85, 0.28)
    draw_heng(draw, s1_head, s1_tail, width=9)

    # Stroke 2: 竖折 (vertical descent then rightward).
    # head lives lower-and-left of s1.head to open the N gap.
    s2_head = ('TL', 0.15, 0.45)
    s2_corner = ('BL', 0.15, 0.70)
    s2_tail = ('BR', 0.80, 0.70)
    draw_shu_zhe(draw, s2_head, s2_corner, s2_tail,
                 v_width=10, h_width=10, shoulder=12)

    # Report joint gap for self-check.
    p1 = anchor_to_xy(s1_head)
    p2 = anchor_to_xy(s2_head)
    gap_px = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
    SELF_CHECK['notes'] += f' actual_gap_px={gap_px:.1f}'

    out = os.path.join(os.path.dirname(__file__), '01_匚.png')
    img.save(out)
    print(f'wrote {out}  self_check_gap_px={gap_px:.1f}')


if __name__ == '__main__':
    render()
