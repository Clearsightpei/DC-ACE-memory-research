"""p3_char_0497 响 — G5 attempt.

Composition: 口 (left, small) + 向 (right, larger, 6 strokes).
Total 9 strokes = 3 (left 口) + 6 (向).

Reasoning trace (P-A-008):
- Left 口: inline stroke primitives (shu + heng_zhe_box + heng) rather than
  calling draw_kou. draw_kou native footprint ~133 x 153 with aspect 0.87;
  target left-口 footprint ~70 x 100 with aspect 0.70 (taller-than-square
  for the L-half column). Uniform scale of draw_kou can't hit both dims,
  so inline gives clean aspect control (see BANK_DEVIATION block).
- Right 向: 6 strokes = pie (top) + 冂 frame (shu + heng_zhe_gou) + inner
  口 (shu + heng_zhe_box + heng). Uses stroke-primitive layer per P-A-006.

BANK_DEVIATION
skipped: kou_mouth.py (for the LEFT 口)
reason: Native draw_kou aspect ~0.87 wide/tall; target left-口 needs aspect
        ~0.70 (compact-tall) at ~70x100 px. Native=133x153 -> uniform
        scale=0.53 gives 71x81 (too short) or scale=0.65 gives 86x99 (too
        wide). Quantitative BANK_DEVIATION (P-A-009): width_ratio 0.53 vs
        height_ratio 0.65 differ by 22% -> aspect-mismatch, inline instead.
fresh_component: kou_tall_narrow (compact-tall variant for L-column position)
"""

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.normpath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 strokes rendered
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes for left 口 + 6 for 向 = 9 total.',
}


def draw_xiang(draw: ImageDraw.ImageDraw):
    # ============================================================
    # LEFT 口 — compact, sits in x=25..95, y=118..218
    # ============================================================
    # s1: left shu (slight rightward drift, matches MMH)
    draw_shu(draw, head=(30, 128), tail=(38, 218), width=5)
    # s2: 横折box top-left..bottom-right corner rectangle
    draw_heng_zhe_box(draw, top_left=(33, 122), bottom_right=(95, 210), width=5)
    # s3: bottom heng closing the box
    draw_heng(draw, head=(34, 216), tail=(94, 210), width_head=5, width_tail=6)

    # ============================================================
    # RIGHT 向 — spans x=115..268, y=40..268
    # ============================================================
    # s4: 撇 pie (top-left of 向, sweeping down-left) — thicker tail so it
    # visually merges with 冂 shu head; slightly less steep.
    draw_pie(draw, head=(188, 50), tail=(140, 108),
             bow_perp=8, w_head=9, w_tail=5, steps=70)

    # s5: 冂 frame left shu (starts a hair lower to weld with pie tail)
    draw_shu(draw, head=(142, 105), tail=(150, 265), width=7)

    # s6: 冂 frame right side: 横折钩 (top + right + hook)
    draw_heng_zhe_gou(draw,
                      heng_head=(150, 62),
                      corner=(258, 58),
                      gou_tail=(250, 258),
                      hook_tip=(228, 250))

    # ============================================================
    # Inner 口 of 向 — sits in x=160..232, y=140..218
    # ============================================================
    # s7: inner left shu
    draw_shu(draw, head=(165, 145), tail=(170, 214), width=5)
    # s8: inner 横折box
    draw_heng_zhe_box(draw, top_left=(167, 140),
                      bottom_right=(232, 208), width=5)
    # s9: inner bottom heng
    draw_heng(draw, head=(168, 214), tail=(232, 210),
              width_head=5, width_tail=6)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_xiang(draw)
    out = os.path.join(_HERE, "01_响.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
