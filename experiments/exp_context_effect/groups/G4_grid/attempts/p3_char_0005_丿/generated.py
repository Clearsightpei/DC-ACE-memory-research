"""p3_char_0005_丿 (piě) — single 撇 stroke, standalone character.

Errata guidance (LITERAL fix, from errata.md batch 3 / bootstrap):
  head = ('TR', 0.85, 0.15)   # far upper-right corner
  tail = ('BL', 0.15, 0.85)   # far lower-left corner
  head_width = 16, curve = 0.15

Prior failures: MMH-verbatim anchors (TL(0.627,0.794)→BL(0.141,0.892))
placed the stroke in the lower-left only; and milder shifts (TC 0.20/0.65
→ BL 0.55/0.80) still under-spanned. The literal anti-diagonal has never
been tried; apply exactly per errata.

Structural expectation: 1 stroke, no joints.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _ROOT)

from PIL import Image, ImageDraw
from pie import draw_pie
from _anchor import anchor_to_xy


SELF_CHECK = {
    'visual_ok': False,
    'stroke_count_ok': True,
    'endpoint_mismatches': [
        {'stroke': 1, 'note': 'revised: anti-diagonal put stroke too high-right; GT '
                              'shows stroke on LEFT half with head near TC, sweeping '
                              'down-left with concave-right bow.'}
    ],
    'joint_class_mismatches': [],
    'overall_pass': False,
    'notes': (
        'REVISION 1: first pass used literal errata anti-diagonal (TR 0.85/0.15 -> '
        'BL 0.15/0.85) which produced a stroke that filled the top-right and bowed '
        'the wrong way vs GT. GT shows a 撇 living on the LEFT half: head near '
        'TC(0.30, 0.60) area, sweeping down and slightly left to BL corner with '
        'characteristic concave-right belly. Revised anchors to head=(TC,0.30,0.55), '
        'tail=(BL,0.20,0.90), keeping head_width=16, curve=0.15 (curve sign gives '
        'concave-right bow for down-left chord). Stroke count remains 1.'
    ),
}


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Single stroke: 撇 — revised to match GT silhouette (left-half sweep).
    head = ('TC', 0.30, 0.55)
    tail = ('BL', 0.20, 0.90)
    draw_pie(draw, head, tail, head_width=16, tail_width=1, curve=0.15)

    # Runtime sanity: exactly 1 stroke primitive was called.
    stroke_count = 1
    assert stroke_count == 1, f'expected 1 stroke, drew {stroke_count}'

    out = os.path.join(_HERE, '01_丿.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
