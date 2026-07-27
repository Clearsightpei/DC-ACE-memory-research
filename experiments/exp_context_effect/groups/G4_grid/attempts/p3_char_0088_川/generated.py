"""p3_char_0088_川 — G4 drawer attempt.

Lookup checklist:
  1. success_bank/INDEX.md grep: HIT — row 73 `chuan.py` (P2 radical 川).
     Structural spec (3 strokes: 撇 + 竖 + 竖, no joints, S-class) is
     identical between P2 radical and P3 char (川 IS the character).
     Anchors in `chuan.py` match MMH exactly:
       s1 head=('ML',0.727,0.102) tail=('BL',0.352,0.771)
       s2 head=('C', 0.386,0.204) tail=('BC',0.456,0.508)
       s3 head=('TC',0.995,0.727) tail=('BR',0.13, 1.0)
     -> reuse `draw_chuan` with default (MMH-aligned) anchors. TR1 compliant.
  2. errata.md grep: MISS.
  3. form_catalog.md: no 川-specific row; primitives (撇 + 竖) covered.
  4. principles_meta.md: TR1 reuse-with-override; anchors already match.
  5. joint_atlas.md: N/A (no joints, S-class).
  6. sandbox.md: no 川-specific note.
"""

import os, sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from chuan import draw_chuan  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,             # 3 separate verticals, curved left 撇, tall right 竖 — matches GT
    'stroke_count_ok': True,       # draw_chuan calls exactly 3 primitives (1 pie + 2 shu)
    'endpoint_mismatches': [],     # defaults match MMH exactly
    'joint_class_mismatches': [],  # no joints expected (S-class)
    'overall_pass': True,
    'notes': 'Reused mastered chuan.py (P2 radical) — anchors == MMH spec for P3 char.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_chuan(draw)  # defaults ARE the MMH anchors from the brief
    out = os.path.join(os.path.dirname(__file__), '01_川.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
