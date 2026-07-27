"""丷 (bā-tou / eight-top radical) — 2 strokes, no joints (clear separation).

MMH-derived structural expectations:
  stroke 1: head @ ('ML', 0.952, 0.447)  →  tail @ ('C',  0.254, 0.717)
    (goes DOWN-RIGHT: dx=+30 px, dy=+27 px — this is the LEFT dot, 点)
  stroke 2: head @ ('C',  0.904, 0.266)  →  tail @ ('C',  0.567, 0.764)
    (goes DOWN-LEFT: dx=-34 px, dy=+50 px — this is the RIGHT sweep, 撇)

Joints: NONE — both strokes stand apart with clear separation.

Anchor plan (TR7):
  s1 (点 left, sweeps down-right — RIGHT-leaning 点):
     head=('ML', 0.952, 0.447)   px=(95.2, 144.7)
     tail=('C',  0.254, 0.717)   px=(125.4, 171.7)
     draw_dian with default curve=0.08 → thin head, rounded press tail.
  s2 (撇 right, sweeps down-left):
     head=('C', 0.904, 0.266)    px=(190.4, 126.6)
     tail=('C', 0.567, 0.764)    px=(156.7, 176.4)
     draw_pie with head_width smaller (short pie in a radical top).

Sanity (TR8):
  - No horizontals or verticals — no row/column invariant applies.
  - Endpoints all inside 米字格.
  - No joints declared — no anchor sharing needed.
  - Gap between s1.tail (125.4, 171.7) and s2.tail (156.7, 176.4) ≈ 32 px
    → visible separation (radical's signature is TWO separate marks).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('丷: 2 strokes, no joints. s1 = left 点 sweeping down-right, '
              's2 = right 撇 sweeping down-left. Anchors match MMH exactly. '
              'Kept compact within upper-middle band per GT.'),
}

import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import CANVAS
from dian import draw_dian
from pie import draw_pie


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1: left dot (点), sweeping down-right.
    # Head thin (up-left), tail rounded (down-right).
    draw_dian(draw,
              from_anchor=('ML', 0.952, 0.447),
              to_anchor=('C',  0.254, 0.717),
              head_width=2, peak_width=10, curve=0.08)

    # Stroke 2: right sweep (撇), sweeping down-left.
    # Short pie — narrower head than a full standalone 撇.
    draw_pie(draw,
             from_anchor=('C', 0.904, 0.266),
             to_anchor=('C', 0.567, 0.764),
             head_width=10, tail_width=1, curve=0.08)

    out_path = os.path.join(os.path.dirname(__file__), '01_丷.png')
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == '__main__':
    main()
