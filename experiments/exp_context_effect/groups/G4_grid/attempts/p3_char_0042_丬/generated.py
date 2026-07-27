"""p3_char_0042_丬 — G4 Drawer attempt.

MANDATORY LOOKUP CHECKLIST (from memory_index.md):
  1. success_bank/INDEX.md grep for 丬 — HIT: p2_radical_083_丬 -> pan.py (mastered, PASS).
  2. errata.md grep for 丬 — no entry.
  3. form_catalog / principles_meta / joint_atlas — not needed; direct bank reuse.
     TR1: reuse mastered primitive with OVERRIDE anchors (MMH-supplied for this item).
  4. sandbox notes — nothing 丬-specific.

Approach: reuse draw_pan(). This item's MMH anchors are identical to the
mastered radical's — call draw_pan with explicit MMH anchors (TR1: override,
never rely on defaults). 3 strokes, 1 N-joint at C, matching MMH expectation.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Reuse mastered pan.py; MMH anchors passed as explicit overrides per TR1.',
}

import os
import sys
from PIL import Image, ImageDraw

# Make bank code importable (pie/ti/shu/_anchor live in success_bank/code).
BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code',
)
sys.path.insert(0, os.path.abspath(BANK))

from pan import draw_pan  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Explicit MMH anchors from the injected structural expectations.
    # s1 endpoints swapped in call to match pan.py's curve orientation
    # (pie head is upper-right, tail is lower-left).
    s1_head = ('C', 0.342, 0.424)  # MMH tail — becomes pie "from"/head
    s1_tail = ('C', 0.046, 0.081)  # MMH head — becomes pie "to"/tail
    s2_head = ('BL', 0.87, 0.306)
    s2_tail = ('C', 0.576, 0.749)
    s3_head = ('TC', 0.538, 0.7)
    s3_tail = ('BC', 0.638, 1.026)

    draw_pan(draw,
             s1_head=s1_head, s1_tail=s1_tail,
             s2_head=s2_head, s2_tail=s2_tail,
             s3_head=s3_head, s3_tail=s3_tail)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_丬.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
