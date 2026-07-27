"""p3_char_0037_勹 — direct reuse of mastered success_bank/code/bao.py.

Lookup checklist (per memory_index.md):
  1. INDEX.md grep 勹 → HIT: bao.py (p2_radical_010_勹). Reuse per TR1.
  2. errata.md grep 勹 → no active fix needed.
  3. form_catalog.md → 撇 + 横折钩 pattern already encoded in bao.py.
  4. principles_meta.md TR1 → reuse mastered primitive with OVERRIDING anchors
     when composition differs. Here the character IS the radical, so calling
     with the mastered default anchors is correct.
  5. joint_atlas.md → s1.mid ⇆ s2.head @ ML is N-class (small gap ~16 px).
     Do NOT weld. bao.py already enforces this.
  6. sandbox.md → nothing extra.

Stroke count: 2 (matches MMH expected 2).
Endpoint anchors (using bao.py defaults):
  s1 撇     head ('TC', 0.116, 0.645)  tail ('ML', 0.56, 0.682)
  s2 横折钩 head ('ML', 0.99, 0.34)    tail ('BC', 0.35, 0.78)
Expected (MMH):
  s1 head ('TC', 0.116, 0.645)  tail ('ML', 0.56, 0.682)   → exact match
  s2 head ('ML', 0.987, 0.336)  tail ('BC', 0.453, 0.742)  → within ±0.20 tolerance
Joint: N-class at ML — implemented as N (small natural gap), matches expected.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Direct reuse of mastered bao.py (p2_radical_010_勹). '
             'Same character, defaults land within tolerance of MMH.',
}

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from bao import draw_bao  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_bao(draw)
    out = os.path.join(_HERE, '01_勹.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
