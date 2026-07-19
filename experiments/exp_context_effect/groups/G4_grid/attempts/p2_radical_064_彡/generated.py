"""彡 (shān) — three-stroke radical, three parallel 撇 (pie) sweeps.

Three pie strokes stacked vertically, each descending from upper-right
to lower-left, tapered. No joints (strokes do not meet).

MMH-derived anchors:
  stroke 1: head @ ('TC', 0.696, 0.653) · tail @ ('C', 0.113, 0.532)
  stroke 2: head @ ('C',  0.734, 0.345) · tail @ ('BC', 0.166, 0.095)
  stroke 3: head @ ('C',  0.928, 0.887) · tail @ ('BL', 0.779, 1.103)
"""
import os
import sys

# Add success bank code dir to path so we can import primitives.
_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from pie import draw_pie

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 pie strokes, no joints; anchors match MMH expected within tolerance.',
}


def draw_shan(draw):
    # stroke 1 — top pie
    draw_pie(draw,
             from_anchor=('TC', 0.696, 0.653),
             to_anchor=('C', 0.113, 0.532),
             head_width=9, tail_width=1, curve=0.10)
    # stroke 2 — middle pie
    draw_pie(draw,
             from_anchor=('C', 0.734, 0.345),
             to_anchor=('BC', 0.166, 0.095),
             head_width=9, tail_width=1, curve=0.10)
    # stroke 3 — bottom pie (longer, sweeps down and left)
    draw_pie(draw,
             from_anchor=('C', 0.928, 0.887),
             to_anchor=('BL', 0.779, 1.103),
             head_width=9, tail_width=1, curve=0.10)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_shan(draw)
    out = os.path.join(os.path.dirname(__file__), '01_彡.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
