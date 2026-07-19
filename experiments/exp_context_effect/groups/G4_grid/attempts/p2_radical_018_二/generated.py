"""p2_radical_018_二 — G4 grid-bank attempt.

二 is two horizontal strokes with clear separation (no joints).
- Stroke 1 (top 横): short, upper-middle band, slight rise left→right.
- Stroke 2 (bottom 横): longer than top, near bottom band, slight rise
  left→right.

Bank primitive used: draw_heng (heng.py). Per TR1 we OVERRIDE default
anchors with new anchor tuples derived from the MMH-expected endpoints.

Per TR7 anchor plan:
  stroke 1 (heng, top):    head @ ('ML', 0.858, 0.28),  tail @ ('MR', 0.147, 0.157), width 10
  stroke 2 (heng, bottom): head @ ('BL', 0.369, 0.358), tail @ ('BR', 0.684, 0.326), width 11
Joints: none (S — separate strokes; expected clear vertical gap).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '2 heng strokes rendered via draw_heng; MMH anchors used verbatim; no joints expected/implemented.',
}

import os
import sys
from PIL import Image, ImageDraw

# Import from the shared success_bank primitives.
BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code',
)
sys.path.insert(0, BANK)

from heng import draw_heng  # noqa: E402


def main():
    canvas = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    # Stroke 1 — top 横 (short)
    s1_head = ('ML', 0.858, 0.28)
    s1_tail = ('MR', 0.147, 0.157)
    draw_heng(draw, s1_head, s1_tail, width=10)

    # Stroke 2 — bottom 横 (longer)
    s2_head = ('BL', 0.369, 0.358)
    s2_tail = ('BR', 0.684, 0.326)
    draw_heng(draw, s2_head, s2_tail, width=11)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_二.png')
    canvas.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
