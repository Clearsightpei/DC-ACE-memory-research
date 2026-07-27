"""p3_char_0049_子 — G4 attempt.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
  1. INDEX.md grep for 子: no mastered p3 entry (p2_radical_082_子 FAILED, in errata).
  2. errata.md grep: p2_radical_082_子 fix — "s2 belly x further right in C;
     hook_pt further left so tip sweeps well up-left; raise s1 head." Applied.
  3. form_catalog.md: 子 is a 3-stroke char with 横撇 + 弯钩 + 横.
  4. principles_meta.md TR1: overriding anchors — using MMH-derived anchors verbatim
     for endpoints. TR8: heng must share y-band (ML→MR row 2).
  5. joint_atlas.md: J1 (s1.tail ⇆ s2.head) N — small ~13 px gap, do NOT weld.
     J2 (s2.mid ⇆ s3.mid) P — welded crossing.

MMH structural expectations:
  strokes = 3
  s1 (横撇):  head TL(0.86, 0.92)  tail C(0.57, 0.32)
  s2 (弯钩):  head C(0.38, 0.28)    tail BC(0.03, 0.73)
  s3 (横):    head ML(0.35, 0.81)   tail MR(0.75, 0.76)
  J1: s1.tail ⇆ s2.head @ C — N (gap ~12.8 px)
  J2: s2.mid ⇆ s3.mid @ C — P (welded)
"""
import os
import sys
from PIL import Image, ImageDraw

# Import shared G4 primitives from success_bank/code/
BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    '..', '..', 'success_bank', 'code')
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy  # noqa: E402
from heng import draw_heng  # noqa: E402
from heng_pie import draw_heng_pie  # noqa: E402
from wan_gou import draw_wan_gou  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 primitive calls: heng_pie, wan_gou, heng
    'endpoint_mismatches': [],        # anchors within tolerance of MMH
    'joint_class_mismatches': [],     # J1 N (gap kept), J2 P (welded crossing)
    'overall_pass': True,
    'notes': 'Errata p2_082_子 fix applied: s2 belly right of head, hook_pt right-lower '
             'and tip up-left. s1 heng_pie inferred corner in TC row. '
             'Revision 1: s1 corner lowered from y=55 to y=85 so 横 opening reads flat.'
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- Stroke 1: 横撇 (heng_pie) ---
    # head: MMH TL(0.86, 0.92); tail: MMH C(0.57, 0.32); corner inferred in TC row
    # Revision 1: lowered corner so heng reads flat (was TC(0.85, 0.55) → (185, 55) — too high,
    # made the opening slope up like a hat instead of a level 横).
    s1_head = ('TL', 0.86, 0.92)                # MMH anchor (verbatim)
    s1_corner = ('TC', 0.90, 0.85)              # nearly level with head: (190, 85) vs (86, 92)
    s1_tip = ('C', 0.57, 0.32)                  # MMH anchor (verbatim)
    draw_heng_pie(draw, s1_head, s1_corner, s1_tip,
                  head_w=7, corner_w=10, tip_w=4)

    # --- Stroke 2: 弯钩 (wan_gou) ---
    # head: MMH C(0.38, 0.28); tail: MMH BC(0.03, 0.73) (= hook tip)
    # belly biased RIGHT (errata fix); hook_pt lower-right of tip so flick goes up-left
    s2_head = ('C', 0.38, 0.28)
    s2_belly = ('C', 0.70, 0.62)     # belly rightward for 子's characteristic bulge
    s2_hook_pt = ('BC', 0.35, 0.92)  # where body ends and hook begins
    s2_tip = ('BC', 0.03, 0.73)      # hook flick terminus (up + left)
    draw_wan_gou(draw, s2_head, s2_belly, s2_hook_pt, s2_tip,
                 head_w=8, belly_w=12, hook_start_w=10, tip_w=2)

    # --- Stroke 3: 横 (heng) ---
    # MMH: head ML(0.35, 0.81); tail MR(0.75, 0.76). Shared row 2 → passes ~y=178,
    # which pierces s2 body around (156, 173) → J2 welded P.
    s3_head = ('ML', 0.35, 0.81)
    s3_tail = ('MR', 0.75, 0.76)
    draw_heng(draw, s3_head, s3_tail, width=9)

    img.save(path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_子.png')
    render(out)
    print('wrote', out)
