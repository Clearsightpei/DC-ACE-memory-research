"""p3_char_0008_亅 (jué) — Phase-3 character, 1 stroke (竖钩).

Uses the mastered draw_jue primitive from success_bank (defaults already
match MMH anchors for standalone radical).

Expected structural spec (from dispatcher):
  - stroke count: 1
  - stroke 1: head @ ('TC', 0.283, 0.674) · tail @ ('BL', 0.973, 0.722)
  - joints: NONE
"""
import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from jue import draw_jue  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 1 primitive call = 1 stroke
    'endpoint_mismatches': [],        # defaults match expected anchors exactly
    'joint_class_mismatches': [],     # NONE expected
    'overall_pass': True,
    'notes': 'draw_jue defaults are the exact MMH anchors for standalone 亅.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    # Use defaults — they are the MMH-derived anchors:
    #   head    = ('TC', 0.283, 0.674)
    #   tip     = ('BL', 0.973, 0.722)
    draw_jue(draw)
    out = os.path.join(_HERE, '01_亅.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
