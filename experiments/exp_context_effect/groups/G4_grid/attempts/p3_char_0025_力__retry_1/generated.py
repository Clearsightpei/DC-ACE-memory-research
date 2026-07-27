"""p3_char_0025_力__retry_1 — G4 grid-bank attempt.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
  1. success_bank/INDEX.md grep '力' -> `li.py` exists (B3 retry PASS).
  2. errata.md grep 'p3_char_0025_力' -> Fix idea: "reuse `li.py` (just
     promoted). Drawer skipped bank retrieval." — apply LITERALLY.
  3. form_catalog.md — n/a, bank primitive covers this.
  4. principles_meta.md — TR1 (override anchors, don't call defaults):
     draw_li exposes overrides, but the MMH-anchor defaults ARE the
     match for this exact character (力). Use defaults.
  5. joint_atlas.md — P weld at C; li.py already implements it
     correctly (撇 pierces 横 descent).
  6. sandbox.md — n/a.

Character: 力 (lì, 2 strokes)
  s1: 横折钩 — head at ML(0.668, 0.474), 折 corner at TR(0.20, 0.85),
      hook base at BC(0.459, 0.596), tip flicks up-left to BC(0.05, 0.35).
  s2: 撇 — head TC(0.40, 0.671) sits ABOVE the top-bar, tail BL(0.372, 0.845).
       Crosses s1's descent (P weld at cell C).

MMH-expected endpoints (from prompt):
  s1 head ML(0.668, 0.474)  = li.py DEFAULTS ✓
  s1 tail BC(0.459, 0.596)  = li.py DEFAULTS ✓
  s2 head TC(0.40, 0.671)   = li.py DEFAULTS ✓
  s2 tail BL(0.372, 0.845)  = li.py DEFAULTS ✓
Joint C P-weld: 撇 crosses 横折钩 descent -> ink overlap (P satisfied
by li.py's construction).

Retry-1 fix (per errata literal): reuse li.py from Success Bank.
Prior attempt inlined heng_zhe_gou with the corner at TR(0.05,0.48),
producing a right-edge vertical drop, not the inward-curving descent
li.py's canonical corner TR(0.20, 0.85) produces.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'stroke_count_actual': 2,
    'stroke_count_expected': 2,
    'endpoint_mismatches': [],  # all four endpoints match MMH exactly
    'joint_class_mismatches': [],  # P weld at C — 撇 pierces 横 descent
    'joints_check': [
        {'joint': 'C', 'expected_class': 'P', 'actual_class': 'P',
         'note': 'li.py 撇 (TC 0.4,0.671 → BL 0.372,0.845) crosses '
                 's1 descent — ink overlap, welded.'},
    ],
    'overall_pass': True,
    'notes': 'Errata fix applied LITERALLY: reused li.py from Success '
             'Bank. All MMH endpoint anchors match li.py DEFAULTS.',
}

import os, sys
from PIL import Image, ImageDraw

# Import bank primitives.
BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from li import draw_li


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    # Use li.py defaults — they ARE the MMH anchors for 力 as a standalone
    # character (TR1 override rule doesn't apply: this IS the target item).
    draw_li(draw)
    out = os.path.join(os.path.dirname(__file__), '01_力.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
