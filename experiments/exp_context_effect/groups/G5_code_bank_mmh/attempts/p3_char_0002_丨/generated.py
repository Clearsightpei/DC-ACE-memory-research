"""
G5 render of 丨 (character, 1 stroke).

MMH-derived expectations:
  - stroke count: 1
  - head @ ('TC', 0.301, 0.665) -> pixel (130, 66)
  - tail @ ('BC', 0.412, 1.026) -> pixel (141, 299) [clamped from 302 to canvas]
  - no joints

Visual inspection of GT (gt/phase3/丨.png): identical silhouette to the
Phase-2 radical GT — a soft leftward top-hook curl, then a nearly vertical
descent with a slight rightward drift.

Bank use: calls draw_shu(top_curl=True) from success_bank/code/shu.py.
No BANK_DEVIATION — the bank primitive fits this composition exactly.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Add success_bank/code to import path
BANK = Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from shu import draw_shu  # type: ignore

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # one draw_shu call
    'endpoint_mismatches': [], # head (130,66) ~ TC(.301,.665); tail (141,299) ~ BC(.412,1.026)
    'joint_class_mismatches': [],  # no joints expected
    'overall_pass': True,
    'notes': 'reused draw_shu(top_curl=True) primitive; anchors match MMH.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    head = (130, 66)
    tail = (141, 299)  # clamped from y_frac 1.026 to canvas edge

    draw_shu(draw, head, tail, width=7, top_curl=True)

    out = Path(__file__).parent / '01_丨.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
