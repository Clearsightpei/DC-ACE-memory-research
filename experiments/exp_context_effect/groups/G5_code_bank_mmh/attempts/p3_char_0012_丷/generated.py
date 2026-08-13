"""p3_char_0012_丷 — two dian dots (ba-bottom form), G5 attempt.

MMH-derived stroke count: 2. No joints (clear separation).

Stroke 1 (left dot, "\"):  head ML(0.952, 0.447) -> (95, 145)
                           tail C (0.254, 0.717) -> (125, 172)
Stroke 2 (right dot, "/"): head C (0.904, 0.266) -> (190, 127)
                           tail C (0.567, 0.764) -> (157, 176)

Uses bank primitive `dian.py` for both strokes (endpoint-signature).
Direction is fully parametric via endpoints; stroke 2 is the mirror
direction (down-left) so we invert the bow sign to keep the belly
outward.
"""

import sys
import pathlib

from PIL import Image, ImageDraw

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 2 draw_dian calls == expected 2
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # no joints expected
    'overall_pass': True,
    'notes': 'Two dians rendered at MMH-derived anchor pixels; bow signs chosen so belly points outward from center gap.',
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1 — left dot, thin head at upper-left, thick tail at lower-right.
    # Small bow, mild taper — GT strokes are nearly straight tapered dots.
    draw_dian(d, head=(95, 145), tail=(125, 172),
              w_head=2, w_tail=6, bow=2)

    # Stroke 2 — right dot, thin head at upper-right, thick tail at lower-left.
    # Direction is down-left; flip bow sign so the belly bows outward (right).
    draw_dian(d, head=(190, 127), tail=(157, 176),
              w_head=2, w_tail=6, bow=-2)

    img.save(path)


if __name__ == '__main__':
    out = _HERE.parent / '01_丷.png'
    render(out)
    print(f'wrote {out}')
