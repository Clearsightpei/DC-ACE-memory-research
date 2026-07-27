"""p3_char_0002_丨 — Phase 3 character, 1 stroke.

MMH expectations:
  stroke 1 (竖): head @ ('TC', 0.301, 0.665), tail @ ('BC', 0.412, 1.026)
Joints: NONE.

Bank composition: 丨's canonical shape IS the 竖 primitive. Reuse
draw_gun (which wraps draw_shu) with OVERRIDDEN anchors per TR1
(don't call primitives with their defaults). Chose anchors to match
MMH exactly. Tail y_frac clipped from 1.026 -> 1.000 (max valid
frac within a cell); actual position stays within same BC cell and
well within ±0.20 tolerance.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from gun import draw_gun

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 1 stroke (draw_gun -> draw_shu -> single fat_line)
    'endpoint_mismatches': [], # head/tail match MMH within tolerance
    'joint_class_mismatches': [], # no joints expected
    'overall_pass': True,
    'notes': 'Single 竖 stroke via draw_gun wrapper; MMH anchors used verbatim (tail y_frac clipped from 1.026 to 1.000, within same BC cell).',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # OVERRIDE-anchor call (TR1): pass MMH-derived anchors explicitly.
    head = ('TC', 0.301, 0.665)
    tail = ('BC', 0.412, 1.000)  # clipped from MMH 1.026 to stay in-cell
    draw_gun(draw, head=head, tail=tail, width=10)

    out = os.path.join(_HERE, '01_丨.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
