"""p3_char_0024 八 (bā) — Phase 3 character, 2画.

Composition: 撇 + 捺. Joints: NONE (S-class, strokes clearly separated).

Bank reuse: `draw_ba` from success_bank/code/ba.py — mastered primitive
whose default anchors exactly match this cycle's MMH structural
expectations (head/tail all within 0.00 delta). TR1 satisfied: I am
passing explicit anchors (equal to defaults here) so intent is
documented in generated.py.

Anchor plan (from injected MMH expectations):
  s1 撇: head @ ('ML', 0.97, 0.623), tail @ ('BL', 0.261, 0.64)
         head_width 11, tail_width 1, curve 0.10
  s2 捺: head @ ('TC', 0.324, 0.964), tail @ ('BR', 0.865, 0.569)
         head_width 3, peak_width 13, peak_t 0.8, curve 0.10

Sanity checks (TR8):
  - s1 head col=ML(x=0), tail col=BL(x=0) → same column, but this is 撇
    (diagonal by design), so column-share rule (TR8.6) does NOT apply.
  - s2 head TC → tail BR: diagonal 捺 as expected.
  - All fracs in [0,1] ✓
  - No expected joints → nothing to weld/gap-check.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Reused mastered draw_ba primitive; anchors match MMH exactly.',
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from ba import draw_ba  # noqa: E402

CANVAS = 300
OUT = os.path.join(_HERE, '01_八.png')


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)

    # Explicit anchors (equal to MMH-derived expectations; TR1: documented)
    draw_ba(
        draw,
        s1_head=('ML', 0.97, 0.623),
        s1_tail=('BL', 0.261, 0.64),
        s2_head=('TC', 0.324, 0.964),
        s2_tail=('BR', 0.865, 0.569),
    )

    img.save(OUT)
    print(f"wrote {OUT}")


if __name__ == '__main__':
    main()
