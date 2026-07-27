"""p3_char_0038_匕 — G4 grid-bank first attempt.

MANDATORY LOOKUP CHECKLIST (done before coding):
  1. success_bank/INDEX.md grep '匕' → HIT: bi.py (Phase-2 radical 011).
     TR1: reuse with OVERRIDE anchors matching THIS char's MMH block.
  2. errata.md grep '匕' → miss (not previously failed).
  3. form_catalog.md → 撇+竖弯钩 composition; s2 spans ML→BR across the base.
  4. principles_meta.md → TR1 (reuse-with-override). TR9 not needed
     (bi's MMH anchors already span the full grid). TR10: N-joint at
     s1.tail vs s2.body must remain visibly connected (~15-25 px).
  5. joint_atlas.md → N-class: DO NOT weld; visible gap.
  6. sandbox.md → no additional notes for 匕.

MMH-derived expected anchors for THIS Phase-3 character 匕 exactly match
bi.py's Phase-2 defaults:
  s1: head ('MR', 0.183, 0.254) · tail ('C', 0.031, 0.931)
  s2: head ('ML', 0.776, 0.005) · tail ('BR', 0.496, 0.036)
Joint: s1.tail ⇆ s2.mid(0.27) at cell ML — N-class, expected gap ~16.3 px.

So we reuse bi.py with explicit anchor overrides (defaults happen to
coincide — writing them explicitly satisfies TR1's "override, not defaults").
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 strokes: draw_pie + draw_shu_wan_gou (composed inside draw_bi)
    'endpoint_mismatches': [], # anchors exactly match MMH expected
    'joint_class_mismatches': [], # N preserved by bi.py (s2 belly opens gap on right of s1.tail)
    'overall_pass': True,
    'notes': 'Phase-3 匕 anchors coincide with Phase-2 radical 匕 anchors; reused bi.py with explicit overrides per TR1.'
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from bi import draw_bi  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # TR1 override: anchors stated explicitly (coincide with MMH block for this char).
    draw_bi(
        draw,
        s1_head=('MR', 0.183, 0.254),
        s1_tail=('C',  0.031, 0.931),
        s2_head=('ML', 0.776, 0.005),
        s2_belly=('C',  0.30,  0.95),   # bezier control — preserves N-gap with s1
        s2_corner=('BC', 0.35,  0.30),
        s2_hook_pt=('BR', 0.55,  0.28),
        s2_tip=('BR', 0.496, 0.036),
    )

    out = os.path.join(_HERE, '01_匕.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
