"""p3_char_0022_亻 — 亻 (rén-side, "person radical", 2 strokes).

Anchor plan (TR7):
  s1 — 撇 (pie): head ('TC', 0.588, 0.738) → tail ('BL', 0.806, 0.112),
       head_width=12, tail_width=1, curve=0.10.
  s2 — 竖 (shu): head ('C', 0.389, 0.582) → tail ('BC', 0.441, 0.927),
       width=9.

Joint spec:
  s2.head @ C(0.389, 0.582) ⇆ s1.mid ~ C(0.383, 0.511)
  Class: N (neighbor, expected pixel gap ≈ 19 px).
  Do NOT weld — the T-touch anchor sits slightly below-left of chord
  midpoint on the bowed 撇 body (per ren_side.py sandbox note).

Anchors match MMH expected values verbatim. Bank primitive
`draw_ren_side` provides identical structure but with slightly
different shu anchors (defaults) — per TR1 we OVERRIDE with the
MMH anchors from the brief.

TR8 sanity (竖 rule 6): s2 head/tail both have C-column x_frac near
mid (0.389 in C-cell, 0.441 in BC-cell) — same column (C then BC,
both center column). ✓
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Uses MMH-expected anchors verbatim; bank ren_side primitive inlined via direct pie+shu with overrides.',
}

import sys
import os
_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from shu import draw_shu


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1: 撇 (pie)
    s1_head = ('TC', 0.588, 0.738)
    s1_tail = ('BL', 0.806, 0.112)
    draw_pie(draw, s1_head, s1_tail,
             head_width=12, tail_width=1, curve=0.10, segments=48)

    # s2: 竖 (shu) — MMH override anchors
    s2_head = ('C', 0.389, 0.582)
    s2_tail = ('BC', 0.441, 0.927)
    draw_shu(draw, s2_head, s2_tail, width=9)

    img.save(out_path)


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    render(os.path.join(here, '01_亻.png'))
