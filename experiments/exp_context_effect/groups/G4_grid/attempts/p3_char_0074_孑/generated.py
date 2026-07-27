"""p3_char_0074_孑 — G4 grid-bank attempt (first attempt).

Memory lookup checklist:
1. success_bank/INDEX.md grep for 孑 — not present. Related 子 in errata (FAIL).
2. errata.md grep for 孑 — not listed. 子 (082) failed: fix was raise s1 head,
   push s2 belly right, hook_pt left. 孑 differs: top has a broken hook instead
   of a full 横 across, so top arc is more localized; s3 is a diagonal 提 rather
   than a middle 横.
3. form_catalog — 3-stroke char with N+P joint pattern.
4. principles_meta — TR1 override anchors on bank primitives.
5. joint_atlas — J1 N (~16 px gap), J2 P (welded crossing).
6. sandbox — nothing specific for 孑.

Decomposition (3 strokes per MMH):
- s1: 横撇 (heng_pie) — the top curl. head TL(0.79,0.91) → tail C(0.56,0.39).
  Interpreting as heng_pie: head at left, corner at upper-right of curl,
  tail (pie tip) at C region.
- s2: 弯钩 (wan_gou) — descending curved hook body. head C(0.34,0.32) →
  belly around C bottom → hook_pt near BC → tip up-and-left (up-flick).
- s3: 提 (ti) — rising diagonal crossing s2 body. head BL(0.50,0.24) →
  tail MR(0.22,0.54). Head is heavy lower-left, tail needle upper-right.

Joints:
- J1: s1.tail (C 0.56, 0.39) ~ s2.head (C 0.34, 0.32): N — natural gap ~16 px.
- J2: s2.mid ~ s3.mid at C: P — welded crossing (s3 pierces s2 body).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 3 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'revision 1: lowered s1 corner to same row as head (proper 横 top), '
             'shortened s2 body descent slightly, extended hook flick.',
}

import sys, os
_BANK = os.path.join(os.path.dirname(__file__),
                     '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(_BANK))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng_pie import draw_heng_pie
from wan_gou import draw_wan_gou
from ti import draw_ti


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 横撇 top curl.
    # MMH head TL(0.79,0.91) tail C(0.56,0.39). Corner placed at the RIGHT
    # end of the horizontal top (same row as head), pie tip drops down to
    # MMH tail position.
    s1_head = ('TL', 0.79, 0.91)   # actual (79, 91)
    s1_corner = ('TC', 0.75, 0.90) # actual (~175, 90) — right end of 横, same y-row as head
    s1_tip = ('C', 0.56, 0.39)     # actual (~156, 139) — pie tip (MMH tail)
    draw_heng_pie(d, s1_head, s1_corner, s1_tip,
                  head_w=8, corner_w=11, tip_w=3)

    # Stroke 2: 弯钩 descending body.
    s2_head = ('C', 0.34, 0.32)    # (134, 132)
    s2_belly = ('C', 0.32, 0.75)   # slight left drift near lower body
    s2_hook_pt = ('BC', 0.10, 0.74)# (110, 274) — MMH tail
    s2_tip = ('BL', 0.55, 0.55)    # up-and-left flick, longer and further left
    draw_wan_gou(d, s2_head, s2_belly, s2_hook_pt, s2_tip,
                 head_w=8, belly_w=12, hook_start_w=10, tip_w=2)

    # Stroke 3: 提 diagonal rising, pierces s2 body.
    s3_head = ('BL', 0.50, 0.24)   # (50, 224) lower-left
    s3_tail = ('MR', 0.22, 0.54)   # (222, 154) upper-right needle
    draw_ti(d, s3_head, s3_tail,
            head_width=13, tail_width=1, curve=0.06)

    out = os.path.join(os.path.dirname(__file__), '01_孑.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
