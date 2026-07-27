"""p3_char_0001_一 (yī, "one") — single 横 stroke.

Anchor plan (TR7):
  stroke 1 (横):
    head @ ('ML', 0.354, 0.849)   # MMH-derived, same row as tail
    tail @ ('MR', 0.695, 0.825)   # same M-row → TR8 rule 5 satisfied
    width = 10 (default heng)

Joints: NONE (single stroke).

Bank reuse: uses draw_heng from success_bank primitives with OVERRIDE
anchors (TR1). Verbatim MMH is appropriate for Phase-3 character
context (TR9 says MMH is a FLOOR for STANDALONE radicals only — this
is a character context, so no expansion).
"""
import sys
import os
from PIL import Image, ImageDraw

# Import from G4 success_bank code
BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    '..', '..', 'success_bank', 'code')
sys.path.insert(0, BANK)

from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Single 横 stroke with MMH-verbatim anchors '
              "head=('ML',0.354,0.849), tail=('MR',0.695,0.825). "
              'Same-row check (TR8 r5) satisfied. No joints.')
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    head = ('ML', 0.354, 0.849)
    tail = ('MR', 0.695, 0.825)
    draw_heng(draw, head, tail, width=10)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_一.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
