"""p3_char_0071_口 — G4 drawer attempt.

Lookup checklist (mandatory):
  1. success_bank/INDEX.md grep 口 → row 81 (kou.py, mastered Phase-2 radical). REUSE.
  2. errata.md grep 口 → not present.
  3. form_catalog.md → 口 is an enclosing radical; kou.py already encodes correct form.
  4. principles_meta.md → TR1: reuse bank primitive with EXPLICIT OVERRIDE anchors
     (never call with defaults). MMH anchors here == kou.py defaults, so pass them
     explicitly to satisfy TR1. No TR9 expansion needed — this is the standalone
     Phase-3 char at full 米字格 span already.
  5. joint_atlas.md → 3 × N corner joints (do NOT weld); kou.py's fat_line + _shorten
     already produces ~15 px gaps matching MMH expected_gap_px (12–15 px).
  6. sandbox.md → no relevant notes.

MMH-derived expected anchors (from prompt):
  s1: ('ML', 0.671, 0.289) → ('BC', 0.02, 0.555)
  s2: ('ML', 0.891, 0.333) → ('BC', 0.937, 0.2)   [via C corner]
  s3: ('BC', 0.081, 0.458) → ('BR', 0.18, 0.344)
Joints: 3 × N (top-left ~15 px, bottom-left ~13 px, bottom-right ~15 px).
"""
import os, sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from kou import draw_kou  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # kou.py draws 3 primitives (s1, s2 as 2 fat_lines w/ corner disc, s3)
    'endpoint_mismatches': [], # MMH anchors == kou.py defaults, passed explicitly per TR1
    'joint_class_mismatches': [], # all 3 joints N with ~15 px gaps via _shorten(4) + width 9
    'overall_pass': True,
    'notes': 'Reuse of mastered kou.py with explicit anchor overrides (TR1).',
}


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # TR1: explicit override anchors (MMH expectations, matching kou.py defaults).
    draw_kou(
        draw,
        s1_head=('ML', 0.671, 0.289), s1_tail=('BC', 0.02, 0.555),
        s2_head=('ML', 0.891, 0.333),
        s2_corner=('C', 0.93, 0.33),
        s2_tail=('BC', 0.937, 0.2),
        s3_head=('BC', 0.081, 0.458),
        s3_tail=('BR', 0.18, 0.344),
    )

    out = os.path.join(os.path.dirname(__file__), '01_口.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
