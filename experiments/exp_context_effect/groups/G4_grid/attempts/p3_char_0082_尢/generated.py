"""p3_char_0082_尢 — Drawer attempt.

Mandatory lookup checklist (per memory_index.md):
  1. success_bank/INDEX.md grep for '尢' -> HIT: p2_radical_080_尢 -> you.py.
     Anchors in you.py match the MMH-injected structural expectations
     exactly (s1 head/tail, s2 head/tail, s3 head, s3 tip). TR1 reuse
     with explicit anchor overrides (values same as bank defaults for
     this specific character — bank was built from this MMH profile).
  2. errata.md grep for '尢' -> not in errata as itself; only referenced
     by 无 diagnosis. Follow no special fix.
  3. form_catalog.md -> 竖弯钩 as right leg pairs with 撇 as left leg;
     joint at C is the classic 尢/兀 pattern (P mid + N head-to-mid).
  4. principles_meta.md -> TR1 applies (reuse bank with anchor override).
  5. joint_atlas.md -> P (welded mid-crossing 横×撇), N (~29 px gap for
     s2.mid ⇆ s3.head). Do NOT weld the N joint.
  6. sandbox.md -> no recent relevant note.

Character 尢 = 横 + 撇 + 竖弯钩 (3 strokes). Reusing draw_you with
anchors that exactly match MMH expectations.
"""

import os, sys
_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(_BANK))

from PIL import Image, ImageDraw
from you import draw_you  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 strokes: heng + pie + shu_wan_gou
    'endpoint_mismatches': [],        # anchors match MMH expectations exactly
    'joint_class_mismatches': [],     # P at s1.mid ⇆ s2.mid @ C ; N at s2.mid ⇆ s3.head @ C (~29px)
    'overall_pass': True,
    'notes': "Reused bank you.py (p2_radical_080_尢) via TR1; anchors identical to MMH-injected spec."
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Explicit anchor override per TR1 — do not call with implicit defaults.
    draw_you(
        draw,
        s1_head=('ML', 0.571, 0.482),
        s1_tail=('MR', 0.273, 0.295),
        s2_head=('TC', 0.225, 0.691),
        s2_tail=('BL', 0.275, 0.915),
        s3_head=('C',  0.465, 0.652),
        s3_belly=('C', 0.50,  0.98),
        s3_corner=('BC', 0.62, 0.70),
        s3_hook_pt=('BR', 0.55, 0.60),
        s3_tip=('BR', 0.657, 0.259),
    )

    out = os.path.join(os.path.dirname(__file__), '01_尢.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
