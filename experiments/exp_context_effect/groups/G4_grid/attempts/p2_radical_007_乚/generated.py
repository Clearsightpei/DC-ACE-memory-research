"""p2_radical_007_乚 — G4 grid-bank render.

Target: 乚 (1画部首) — a single compound stroke: 竖弯 (shù wān)
  vertical descent, rounded turn, horizontal sweep to the right,
  ends with a small upturn/tick.

MMH-expected stroke count: 1
  stroke 1: head @ ('TL', 0.636, 0.867)  tail @ ('BR', 0.552, 0.124)
  joints: NONE (single compound stroke, no meeting).

Bank use: draw_shu_wan fits perfectly — this radical IS 竖弯. Anchors
are overridden for THIS composition (not the primitive defaults).

Pixel translations:
  head  ('TL', 0.636, 0.867) -> (63.6,  86.7)
  tail  ('BR', 0.552, 0.124) -> (255.2, 212.4)

I add:
  belly at ('ML', 0.55, 0.90)  -> (55, 190)   (control on vertical column,
                                               keeps upper body straight)
  corner at ('BL', 0.70, 0.30) -> (70, 230)   (bend point at bottom-left)
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'shu_wan primitive: head TL, curve at BL corner, tail BR. '
             'No joints expected (single compound stroke). '
             'Stroke count = 1 primitive call.',
}

import os
import sys
from PIL import Image, ImageDraw

# Import the shared primitives (success_bank/code/).
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from shu_wan import draw_shu_wan  # noqa: E402


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # 乚 = single 竖弯 stroke.
    # head TL(0.636, 0.867) -> starts high-left, in TL cell near its bottom.
    # tail BR(0.552, 0.124) -> ends mid-right, high in BR cell (the tail tick).
    draw_shu_wan(
        draw,
        head=('TL', 0.636, 0.867),
        belly=('ML', 0.55, 0.90),
        corner=('BL', 0.70, 0.30),
        tail=('BR', 0.552, 0.124),
        head_w=8, belly_w=11, corner_w=11, tail_w=6,
    )

    out = os.path.join(os.path.dirname(__file__), '01_乚.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
