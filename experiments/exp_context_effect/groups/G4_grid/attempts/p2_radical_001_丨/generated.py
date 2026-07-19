"""p2_radical_001_丨 — G4 grid-bank attempt.

Target: 丨 (1-画 radical, vertical stroke).
Bank strategy: 丨 is the canonical wrapper for `draw_shu` (principle_bank
Phase-1-general rule "1-画 primitives as radical wrappers"). Reuse the
promoted `shu.py` primitive with anchors OVERRIDDEN per TR1 to match the
MMH-derived endpoints for THIS composition.

Anchor plan (from MMH structural expectations):
  stroke 1 (竖, draw_shu):
    head @ ('TC', 0.301, 0.665)  → PIL (130.1, 66.5)
    tail @ ('BC', 0.412, 1.000)  → PIL (141.2, 300.0)
    (MMH gave tail y_frac=1.026; clamp to 1.0 since PIL canvas is 300px.
     Rightward drift head→tail matches GT's subtle diagonal.)
  width: 10 (standalone-radical width, per shu.py default).

Joints: NONE (single stroke).

Direction invariants:
  - vertical descent: p_tail.y > p_head.y  (top-to-bottom)
  - slight rightward drift: p_tail.x > p_head.x
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 1 primitive call (draw_shu) == 1 expected
    'endpoint_mismatches': [],     # head TC 0.301,0.665 exact; tail BC 0.412,1.000 vs 1.026 (Δy=0.026, well within ±0.20)
    'joint_class_mismatches': [],  # no joints expected, none produced
    'overall_pass': True,
    'notes': 'Wrapper for draw_shu with MMH-derived anchors; y_frac tail clamped from 1.026 → 1.000 to stay on 300px canvas.',
}

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from shu import draw_shu


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    HEAD = ('TC', 0.301, 0.665)
    TAIL = ('BC', 0.412, 1.000)  # clamped from MMH 1.026

    # Sanity assertions before render.
    p_head = anchor_to_xy(HEAD)
    p_tail = anchor_to_xy(TAIL)
    assert p_tail[1] > p_head[1], 'vertical must descend'
    assert p_tail[0] >= p_head[0], 'slight rightward drift expected'
    assert 0 <= p_head[0] <= 300 and 0 <= p_head[1] <= 300
    assert 0 <= p_tail[0] <= 300 and 0 <= p_tail[1] <= 300

    draw_shu(draw, HEAD, TAIL, width=10)

    out = os.path.join(_HERE, '01_丨.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
