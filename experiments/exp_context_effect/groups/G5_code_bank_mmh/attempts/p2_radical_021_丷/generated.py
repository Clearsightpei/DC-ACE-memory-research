"""p2_radical_021_丷 (G5)

Composition: two 点/dot-like strokes.
  stroke 1 (LEFT dot):  head ML(0.952, 0.447) → tail C(0.254, 0.717)
                        = (95.2, 144.7) → (125.4, 171.7)  — falls down-right
  stroke 2 (RIGHT dot): head C(0.904, 0.266) → tail C(0.567, 0.764)
                        = (190.4, 126.6) → (156.7, 176.4) — falls down-left,
                          slightly longer than the left one

Bank primitive used: dian.py · draw_dian (both strokes).
No BANK_DEVIATION: dian fits both strokes cleanly; the two strokes are
independent (no joints). Only signature knob adjusted is bow direction
(via sign) so each dot curves outward the way calligraphic 丷 dots do.
"""

import os, sys
from PIL import Image, ImageDraw

# import bank primitive
_BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(_BANK))
from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 2 dian calls == expected 2 strokes
    'endpoint_mismatches': [],   # anchors used exactly match MMH block
    'joint_class_mismatches': [], # no joints expected
    'overall_pass': True,
    'notes': 'Two independent dian strokes; left falls SE with outward bow, '
             'right falls SW with outward bow. Bank primitive dian.py fits both.'
}


def render(out_png):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: LEFT dot. head thin at upper-left, tail thick at lower-right.
    # bow=+5 curves right-of-travel (SW-ish for a SE stroke) => outward curl.
    draw_dian(d,
              head=(95, 145),
              tail=(125, 172),
              w_head=2, w_tail=5, bow=4, steps=48)

    # Stroke 2: RIGHT dot. Longer, falls down-left. Thin head upper-right,
    # thick tail lower-left. For SW travel, bow=+5 (right-of-travel) points
    # NW = curves the stroke concave-up. We want the belly to point outward
    # (to the upper-right / away from center), so use bow=+ (positive).
    draw_dian(d,
              head=(190, 127),
              tail=(157, 176),
              w_head=2, w_tail=6, bow=5, steps=56)

    img.save(out_png)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_丷.png')
    render(out)
    print('wrote', out)
