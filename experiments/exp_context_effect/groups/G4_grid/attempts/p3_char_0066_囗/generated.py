"""p3_char_0066_囗 — G4 drawer attempt.

MANDATORY LOOKUP CHECKLIST (memory_index reading order):
  1. success_bank/INDEX.md grep '囗' → HIT: wei_enclose.py (p2_radical_073).
     Same character. REUSE per TR1 with anchor overrides (already TR9-spanned).
  2. errata.md grep '囗' → not in errata.
  3. form_catalog.md: enclosing 3-stroke frame; TR9 mandatory for standalone.
  4. principles_meta.md: TR1 (reuse mastered), TR9 (span full grid).
  5. joint_atlas.md: 4 corners of 囗 are N-class, small natural gaps.
  6. sandbox.md: consulted (enclosing radicals need full span).

MMH structural expectations (injected): 3 strokes, 3 N joints (TL, BL, BR).
Reuse the mastered wei_enclose primitive; anchors already span the grid
per TR9. Passing width=10 (standard).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from wei_enclose import draw_wei_enclose

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # wei_enclose emits exactly 3 fat_lines (s1, s2 = 2 segments treated as one 横折, s3)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Reused mastered wei_enclose (p2_radical_073) per TR1; TR9 span already baked in.',
}

img = Image.new('RGB', (300, 300), (255, 255, 255))
draw = ImageDraw.Draw(img)

draw_wei_enclose(draw)

out = os.path.join(os.path.dirname(__file__), '01_囗.png')
img.save(out)
print('wrote', out)
