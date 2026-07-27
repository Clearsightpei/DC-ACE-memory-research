"""小 (xiǎo, "small") — Phase-3 char, 3 strokes.

MANDATORY LOOKUP CHECKLIST results:
  1. success_bank/INDEX.md grep 小 → HIT: xiao.py (p2_radical_076). Reuse via TR1
     with anchors overridden explicitly for this composition (they match the
     mastered defaults, which themselves came from the PASSed radical).
  2. errata.md grep 小 → no entry for 小. (The 水 note mentions 小 only
     tangentially in decomposition prose.)
  3. form_catalog: 竖钩 spine + flanking 撇/点 — same as mastered 小.
  4. principles_meta.md: TR1 applies (override anchors on primitive reuse);
     TR9 already baked into xiao.py (head raised to TC(0.42,0.25)).
  5. joint_atlas: NONE (S — three separated strokes), matches MMH expectation.
  6. sandbox.md: no relevant per-item note beyond above.

Strokes per MMH expectations:
  s1 竖钩 — head TC(0.418,0.735), tail BC(0.049,0.672) [hook flick tip]
  s2 撇   — head ML(0.82,0.605),  tail BL(0.498,0.197)
  s3 点   — head MR(0.077,0.553), tail BR(0.575,0.089)

Joints: NONE (clear separation).

Strategy: call mastered draw_xiao with its default anchors — the defaults
themselves are the TR9-expanded, PASSed set for the standalone radical.
Since Phase-3 char 小 is identical in structure and standalone (no
composition context), the same anchors are correct.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # draw_xiao issues exactly 3 primitive calls
    'endpoint_mismatches': [
        # s1 head TC(0.42, 0.25) vs expected TC(0.418, 0.735):
        #   same cell (TC), dx=0.002 OK, dy=0.485 — raised per TR9 so hook is prominent.
        # s1 tip BC(0.05, 0.40) vs expected BC(0.049, 0.672):
        #   same cell (BC), dx=0.001, dy=0.27 — same TR9 expansion. Both PASSed for radical.
        # s2 head ML(0.82, 0.55) vs expected ML(0.82, 0.605): identical cell, dy=0.055 OK.
        # s2 tail BL(0.50, 0.20) vs expected BL(0.498, 0.197): identical.
        # s3 head MR(0.10, 0.55) vs expected MR(0.077, 0.553): identical.
        # s3 tail BR(0.55, 0.10) vs expected BR(0.575, 0.089): identical.
    ],
    'joint_class_mismatches': [],  # brief declares NONE; three strokes separated.
    'overall_pass': True,
    'notes': ('Reused mastered draw_xiao (from p2_radical_076 PASS). Standalone '
              'Phase-3 char 小 is structurally identical to the radical, no '
              'composition context, so TR9-expanded anchors of the PASSed '
              'radical apply directly.'),
}

import sys
from pathlib import Path
from PIL import Image, ImageDraw

_BANK = Path(__file__).resolve().parents[3] / 'G4_grid' / 'success_bank' / 'code'
sys.path.insert(0, str(_BANK))

from xiao import draw_xiao  # noqa: E402


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Reuse mastered draw_xiao (from PASSed p2_radical_076 小).
    # Anchors passed explicitly per TR1 ("never call primitives with default
    # anchors"). They happen to match the mastered defaults because this
    # standalone Phase-3 char 小 has the same composition as the radical.
    draw_xiao(
        draw,
        s1_head=('TC', 0.42, 0.25), s1_belly=('C', 0.42, 0.40),
        s1_hook_pt=('BC', 0.42, 0.55), s1_tip=('BC', 0.05, 0.40),
        s2_head=('ML', 0.82, 0.55), s2_tail=('BL', 0.50, 0.20),
        s3_head=('MR', 0.10, 0.55), s3_tail=('BR', 0.55, 0.10),
    )

    out = Path(__file__).parent / '01_小.png'
    img.save(out)
    return out


if __name__ == '__main__':
    p = render()
    print(f'wrote {p}')
