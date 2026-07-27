"""p3_char_0003_乙 — Phase-3 character render.

乙 is a single continuous compound stroke (横折弯钩-family). MMH gives
one stroke with head @ ('TL', 0.715, 0.955), tail @ ('BR', 0.49, 0.083).

The Success Bank contains `yi_second.py` (bootstrap PASS as Phase-2
radical 乙, position 38) with the EXACT same MMH anchors we need.
Per TR1 (supply explicit override anchors for THIS composition), I
pass all 5 anchors explicitly rather than relying on defaults. The
three interior anchors (corner, bottom, hook_s) are the mastered
recipe from the bank, verified passing.

Anchor plan (per TR7):
  s1 (only stroke) — 乙 as one variable-width path
    head    @ ('TL', 0.715, 0.955)   — MMH head (top-left start)
    corner  @ ('TC', 0.95,  0.85)    — top wraps here (recipe)
    bottom  @ ('BC', 0.15,  0.55)    — bottom-left of the wan sweep
    hook_s  @ ('BR', 0.55,  0.55)    — sweep meets rising tail base
    tail    @ ('BR', 0.49,  0.083)   — MMH tail (top of hook tip)
  Joint spec: NONE (single continuous stroke).

Sanity check (TR8):
  - Only 1 stroke primitive call — matches expected count of 1.
  - Head anchor in TL (matches MMH TL 0.715/0.955 exactly).
  - Tail anchor in BR (matches MMH BR 0.49/0.083 exactly).
  - No joints to check.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Reused mastered yi_second.py primitive; MMH endpoints match '
             'the bootstrap-PASS anchors exactly (Phase-2 乙 == Phase-3 乙 shape).',
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from yi_second import draw_yi_second  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Explicit anchors per TR1 (override even though defaults match).
    draw_yi_second(
        draw,
        head=('TL', 0.715, 0.955),
        corner=('TC', 0.95, 0.85),
        bottom=('BC', 0.15, 0.55),
        hook_s=('BR', 0.55, 0.55),
        tail=('BR', 0.49, 0.083),
    )

    out = os.path.join(_HERE, '01_乙.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
