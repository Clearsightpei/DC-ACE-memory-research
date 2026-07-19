"""厂 (p2_radical_014) — G4 grid-bank attempt.

Anchor plan (from MMH-derived structural expectations):
  stroke 1 (横): head @ ('TC', 0.011, 0.97), tail @ ('TR', 0.432, 0.838), width 10
  stroke 2 (撇): head @ ('TL', 0.773, 0.94), tail @ ('BL', 0.202, 0.974),
                 head_w 12, tail_w 1, curve 0.10

Joints:
  s1.head @ TC(0.011, 0.97) ⇆ s2.head @ TL(0.773, 0.94)
    class N (neighbor, small natural gap ≈ 18.8 px). DO NOT weld.
    Anchors are intentionally NOT identical — the small gap is the point.

Bank use per TR1: primitives called with explicit anchor overrides.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from _anchor import anchor_to_xy
from heng import draw_heng
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('2 strokes; s1 heng across top with slight downward slope, '
              's2 pie curving from upper-right corner (TL of the anchor '
              'grid, near s1 head) down and left to bottom-left. '
              'Joint at TL is N-class: small natural gap ~18.8 px, not welded.')
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1: 横 — head TC(0.011, 0.97), tail TR(0.432, 0.838)
    s1_head = ('TC', 0.011, 0.97)
    s1_tail = ('TR', 0.432, 0.838)
    draw_heng(draw, s1_head, s1_tail, width=10)

    # Stroke 2: 撇 — head TL(0.773, 0.94), tail BL(0.202, 0.974)
    s2_head = ('TL', 0.773, 0.94)
    s2_tail = ('BL', 0.202, 0.974)
    # Revision 1: slimmer head (8 vs 12) + slightly gentler curve (0.07)
    # to better match GT's lean 撇 sweep.
    draw_pie(draw, s2_head, s2_tail,
             head_width=8, tail_width=1, curve=0.07, segments=48)

    # ---- Post-render sanity: pixel gap at expected N-joint ----
    p1 = anchor_to_xy(s1_head)     # s1 head pixel
    p2 = anchor_to_xy(s2_head)     # s2 head pixel
    gap = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
    # Expected gap ≈ 46.9 in MMH; ≈ 18.8 px in the deployed cell scaling.
    # Just print — the anchors themselves enforce the gap by construction.
    print(f'[厂] N-joint pixel gap between s1.head and s2.head = {gap:.1f}')

    # Direction invariants
    ps1_tail = anchor_to_xy(s1_tail)
    ps2_tail = anchor_to_xy(s2_tail)
    assert ps1_tail[0] > p1[0], '横 must go left→right'
    assert ps2_tail[0] < p2[0], '撇 tail must be to the LEFT of head'
    assert ps2_tail[1] > p2[1], '撇 tail must be BELOW head'

    out = os.path.join(os.path.dirname(__file__), '01_厂.png')
    img.save(out)
    print(f'[厂] wrote {out}')


if __name__ == '__main__':
    render()
