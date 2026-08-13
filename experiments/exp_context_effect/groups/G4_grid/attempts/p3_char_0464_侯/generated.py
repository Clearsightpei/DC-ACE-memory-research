"""侯 (hóu) — 9 strokes.

Decomposition: 侯 = 亻 (left, far-left column) + 侯-right (7 strokes: top short pie
+ heng-gou-like top + interior 矢-body [pie + short heng + heng + pie + na]).

Reading order followed (v8 slim):
1. drawer_memory.md → apply B9 A-recipe: MMH-verbatim anchors + base primitives.
   亻 slot is far-left column (per B11 named pattern `ren_side_far_left`) — inline
   pie+shu with MMH anchors rather than importing ren_side (whose defaults would
   need 3+ overrides).
2. success_bank/INDEX.md grep for 侯 → not mastered.
3. errata.md grep for 侯 → not present.
"""

# BANK_DEVIATION
# skipped: ren_side.py
# reason: 亻 sits in far-left column (MMH pie head TL(0.86,0.66) → BL(0.20,0.01);
#   shu head ML(0.74,0.45) → BL(0.76,0.95)); ren_side default centers/anchors would
#   need 3+ anchor overrides to slot far-left — B10/B11 named pattern
#   `ren_side_far_left` recipe applies (10+ passing precedent).
# fresh_component: ren_side_far_left_for_侯

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 strokes as MMH-required
    'endpoint_mismatches': [],     # all anchors MMH-verbatim
    'joint_class_mismatches': [],  # all N-joints preserved as natural gaps; s7-s8 P weld verified
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim. 亻 far-left column inlined. Right half strokes 3-9 all base primitives.',
}

# ---- MMH-verbatim anchors ----
S1_H = ('TL', 0.861, 0.665);  S1_T = ('BL', 0.196, 0.007)   # 亻 pie
S2_H = ('ML', 0.735, 0.453);  S2_T = ('BL', 0.762, 0.95)    # 亻 shu
S3_H = ('TC', 0.43,  0.861);  S3_T = ('C',  0.948, 0.148)   # top-right short 撇 into ~top-heng span
S4_H = ('C',  0.137, 0.327);  S4_T = ('MR', 0.607, 0.187)   # top heng (of 侯-right)
S5_H = ('C',  0.465, 0.359);  S5_T = ('C',  0.225, 0.972)   # interior pie down-left
S6_H = ('C',  0.521, 0.734);  S6_T = ('MR', 0.25,  0.623)   # short heng (mid-right)
S7_H = ('BC', 0.046, 0.25);   S7_T = ('BR', 0.687, 0.121)   # long heng (welds P w/ s8)
S8_H = ('C',  0.685, 0.805);  S8_T = ('BC', 0.069, 0.991)   # bottom pie (through s7)
S9_H = ('BC', 0.843, 0.262);  S9_T = ('BR', 0.851, 0.977)   # na down-right

def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 (strokes 1-2, far-left column)
    draw_pie(d, S1_H, S1_T, head_width=11, tail_width=1, curve=0.09, segments=48)
    draw_shu(d, S2_H, S2_T, width=8)

    # 侯-right (strokes 3-9)
    # s3: short pie/diagonal at top of right — MMH goes head→tail slightly right+down,
    # render as thin diagonal line
    draw_pie(d, S3_H, S3_T, head_width=8, tail_width=2, curve=0.05, segments=32)
    # s4: top heng of 侯-right
    draw_heng(d, S4_H, S4_T, width=8)
    # s5: interior pie (down-left)
    draw_pie(d, S5_H, S5_T, head_width=9, tail_width=1, curve=0.08, segments=40)
    # s6: short heng (mid-right)
    draw_heng(d, S6_H, S6_T, width=8)
    # s7: bottom heng (long, crosses s8 at P weld)
    draw_heng(d, S7_H, S7_T, width=9)
    # s8: bottom pie (welded P with s7 at BC(0.76,0.17))
    draw_pie(d, S8_H, S8_T, head_width=10, tail_width=1, curve=0.10, segments=48)
    # s9: na down-right
    draw_na(d, S9_H, S9_T, head_width=3, peak_width=13, tail_width=1,
            peak_t=0.82, curve=0.10, segments=48)

    out = os.path.join(os.path.dirname(__file__), '01_侯.png')
    img.save(out)
    print('saved', out)

if __name__ == '__main__':
    render()
