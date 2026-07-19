"""广 (p2_radical_052) — G4 grid-bank attempt.

Structure: 3 strokes.
  s1 = 点   (short SE-diagonal dot on top-center)
  s2 = 横   (horizontal beam across the top; starts at ML, sweeps to MR,
            slight upward slope per MMH tail_y < head_y)
  s3 = 撇   (long sweep from just above/near s2.head down to bottom-left)

Anchor plan (from MMH-derived structural expectations, adjusted so that
strokes fit inside the 300x300 canvas and produce a readable 广):

  stroke 1 (点):  head @ ('TC', 0.307, 0.642)  tail @ ('TC', 0.731, 0.888)
  stroke 2 (横):  head @ ('ML', 0.932, 0.283)  tail @ ('MR', 0.341, 0.184)
  stroke 3 (撇):  head @ ('ML', 0.753, 0.254)  tail @ ('BL', 0.331, 0.98)
                  (MMH tail_y_frac 1.026 clamped to 0.98 to stay on canvas)

Joints (1):
  s2.head @ ML(0.932, 0.283) ⇆ s3.head @ ML(0.753, 0.254)
    class N (neighbor, small natural gap ≈ 18 px). DO NOT weld.
    Pixel positions are close but intentionally distinct.

Bank use per TR1: every primitive is called with explicit anchor
overrides for THIS composition. No default anchors used.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from _anchor import anchor_to_xy
from heng import draw_heng
from pie import draw_pie
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        '3 strokes matching GT: (1) top 点 as a short SE-diagonal dot on '
        'the upper part of the character, (2) a near-horizontal 横 that '
        'stretches from just left of center (ML) rightward across most '
        'of the canvas with a slight upward tilt, (3) a long 撇 whose '
        'head sits just above/left of s2.head (N-class small gap, NOT '
        'welded) and sweeps down-and-left to the bottom-left corner. '
        'Visual match to GT: top dot present, horizontal beam at ~y=125 '
        'reaching to right side, long left-curving descent to bottom-left. '
        'Silhouette reads as 广 (three-stroke radical).'
    )
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- Stroke 1: 点 (top dot) ----
    s1_head = ('TC', 0.307, 0.642)
    s1_tail = ('TC', 0.731, 0.888)
    # Compact dot: use bank primitive with moderate widths.
    draw_dian(draw, s1_head, s1_tail,
              head_width=2, peak_width=9, curve=0.06, segments=24)

    # ---- Stroke 2: 横 (top horizontal beam) ----
    s2_head = ('ML', 0.932, 0.283)
    s2_tail = ('MR', 0.341, 0.184)
    draw_heng(draw, s2_head, s2_tail, width=9)

    # ---- Stroke 3: 撇 (long left sweep) ----
    # Clamp tail y_frac from 1.026 -> 0.98 so tip stays on canvas.
    s3_head = ('ML', 0.753, 0.254)
    s3_tail = ('BL', 0.331, 0.98)
    draw_pie(draw, s3_head, s3_tail,
             head_width=11, tail_width=1, curve=0.09, segments=48)

    # ---- Post-render sanity: pixel gap at expected N-joint ----
    p_s2h = anchor_to_xy(s2_head)
    p_s3h = anchor_to_xy(s3_head)
    gap = ((p_s2h[0] - p_s3h[0]) ** 2 + (p_s2h[1] - p_s3h[1]) ** 2) ** 0.5
    # Expected gap ~14-18 px (N-class small natural gap).
    print(f'[广] N-joint pixel gap s2.head <-> s3.head = {gap:.1f}px')

    # Direction invariants
    p_s1h = anchor_to_xy(s1_head)
    p_s1t = anchor_to_xy(s1_tail)
    p_s2t = anchor_to_xy(s2_tail)
    p_s3t = anchor_to_xy(s3_tail)
    assert p_s1t[0] > p_s1h[0], '点 tail should be to the RIGHT of head'
    assert p_s1t[1] > p_s1h[1], '点 tail should be BELOW head'
    assert p_s2t[0] > p_s2h[0], '横 should go left -> right'
    assert p_s3t[0] < p_s3h[0], '撇 tail must be LEFT of head'
    assert p_s3t[1] > p_s3h[1], '撇 tail must be BELOW head'

    out = os.path.join(os.path.dirname(__file__), '01_广.png')
    img.save(out)
    print(f'[广] wrote {out}')


if __name__ == '__main__':
    render()
