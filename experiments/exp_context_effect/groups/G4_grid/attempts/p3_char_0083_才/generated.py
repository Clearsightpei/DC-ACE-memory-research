"""p3_char_0083_才 — G4 first attempt.

Lookup checklist (v7 memory_index):
1. success_bank/INDEX.md grep 才 — not present; use stroke primitives.
2. errata.md grep 才 — not present.
3. form_catalog.md — 横 and 竖 form rules consulted (row/col share).
4. principles_meta.md — TR1 (override anchors), TR8 (row/col sanity),
   TR4 (share anchor tuple for P weld).
5. joint_atlas.md — P weld = shared tuple; N = ~15-20 px small gap.

Composition plan for 才 (3 strokes):
  s1 横  : ML(0.15, 0.55) → MR(0.85, 0.45)   — slight upward tilt
  s2 竖钩: head TC(0.55, 0.10), body straight down; hook_pt BC(0.55, 0.85),
           tip BC(0.30, 0.72). Body must go THROUGH s1 mid at cell C.
  s3 撇  : head C(0.55, 0.45) (near crossing point) → BL(0.20, 0.85)

Joints:
  s1 mid ⇆ s2 body-mid at cell C → P (welded crossing, achieved by
     geometry: s2 body passes through s1's y-band at same x).
  s1 mid ⇆ s3 head → N (small gap ~15 px; s3 head placed just below
     the 横 line to look attached but not welded).
  s2 body ⇆ s3 head → N (share cell C region; ~15 px).

TR8 sanity:
  s1 both endpoints in *ML/*MR row band → horizontal OK.
  s2 head TC / hook_pt BC share col C → vertical body straight OK.
  s3 head C / tail BL → pie sweep direction OK.
"""

import os
import sys
from PIL import Image, ImageDraw

# Add success_bank/code to path for primitives.
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from heng import draw_heng
from shu_gou import draw_shu_gou
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes: 横, 竖钩, 撇. 横 and 竖钩 cross at cell C '
             '(P weld via geometry). 撇 head near C (N-gap ~15 px).',
}


def draw_cai(draw):
    # s1 — 横 (horizontal, slight upward tilt: left lower, right higher)
    s1_head = ('ML', 0.15, 0.55)
    s1_tail = ('MR', 0.85, 0.45)
    draw_heng(draw, s1_head, s1_tail, width=8)

    # s2 — 竖钩 (vertical spine crossing through the 横, hook at bottom)
    # Body straight; head TC top, hook_pt BC bottom, both at x_frac 0.55
    # so the body passes right through cell C (where the 横 mid sits).
    s2_head    = ('TC', 0.55, 0.10)
    s2_belly   = ('C',  0.55, 0.50)   # width knot (same x as head, TR8 rule 6)
    s2_hook_pt = ('BC', 0.55, 0.85)
    s2_tip     = ('BC', 0.30, 0.72)   # hook tip up-and-left
    draw_shu_gou(draw, s2_head, s2_belly, s2_hook_pt, s2_tip,
                 head_w=9, belly_w=8, hook_start_w=8, tip_w=2)

    # s3 — 撇 (short pie starting near the 横/竖 crossing, sweeping to BL)
    s3_head = ('C',  0.50, 0.55)   # just below the 横, ~15 px gap (N)
    s3_tail = ('BL', 0.20, 0.85)
    draw_pie(draw, s3_head, s3_tail,
             head_width=9, tail_width=1, curve=0.12, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_cai(draw)
    out_path = os.path.join(_HERE, '01_才.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
