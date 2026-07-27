"""p3_char_0030_冫 (bīng) — Phase-3 character, 2画 ("ice" radical / two-drops water).

Strategy: reuse mastered `draw_bing` from success bank verbatim — the
brief's MMH-derived anchors match bing.py's stored anchors exactly:
  s1: head ('TC', 0.245, 0.976), tail ('C', 0.638, 0.395)  [点]
  s2: head ('BC', 0.315, 0.780), tail ('C', 0.734, 0.781)  [提]
Expected joints: NONE (S-class — clear gap).

Anchor plan (TR7):
  stroke 1 点 — head ('TC', 0.245, 0.976), tail ('C', 0.638, 0.395)
    exactly matches expected; single stroke, no joint.
  stroke 2 提 — head ('BC', 0.315, 0.780), tail ('C', 0.734, 0.781)
    exactly matches expected; single stroke, no joint.

TR8 sanity:
  - Both strokes have distinct anchors; no shared points → no joint welds needed.
  - Fracs all in [0,1]. Cells valid.
  - No 横/竖 primitives so rules 5/6 don't apply.
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 2 primitive calls == expected 2
    'endpoint_mismatches': [],         # anchors reused verbatim from brief
    'joint_class_mismatches': [],      # no joints expected, none implemented
    'overall_pass': True,
    'notes': 'Reused mastered draw_bing (bootstrap PASS). Anchors match MMH brief exactly.',
}

import os, sys
from PIL import Image, ImageDraw

# Add success_bank/code to path so bing.py's internal imports work
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from bing import draw_bing  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_bing(draw)
    out = os.path.join(_HERE, '01_冫.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
