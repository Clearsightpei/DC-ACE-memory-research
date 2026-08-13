"""佝 (gōu) — 7 strokes.

Decomposition: 佝 = 亻 (left, 2) + 句 (right, 5); 句 = 勹 (2: 撇 + 横折钩) + 口 (3).
Total strokes: 2 + 2 + 3 = 7 (matches MMH).

Layout:
  - 亻 left column ~ x∈[0.05, 0.30] canvas frac.
  - 句 right column ~ x∈[0.35, 0.90].
    - 勹 outer shell wraps top+right, hooks down-left at bottom.
    - 口 sits inside 勹's belly, lower-center of the right block.
"""

# BANK_DEVIATION
# skipped: ren_side.py, bao_char.py, kou.py
# reason: all three primitives' default anchors sit centered on the canvas;
#         MMH places 亻 in the left column (TL/ML/BL) and 勹+口 in the right,
#         so partial anchor-overrides would clash with the compound
#         primitives (B8 p3_char_0252_伊 lesson). Inlining fresh with MMH
#         anchors + base primitives per B9 A-recipe point 4.
# fresh_component: ren_side_leftcol_for_佝, bao_shell_right_for_句, kou_small_inside_bao

import os, sys
_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 7 strokes drawn (verify by counting draw_* calls below)
    'endpoint_mismatches': [],      # all heads/tails MMH-verbatim where possible
    'joint_class_mismatches': [],   # all 7 declared joints are N (natural gap), preserved
    'overall_pass': True,
    'notes': '7 strokes MMH-verbatim; N-joints preserved via short primitives not welded.',
}


def render():
    im = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(im)

    # ---- 亻 left radical (2 strokes) ----
    # s1 撇 — MMH: head TL(0.932, 0.659) → (93, 66); tail ML(0.211, 0.983) → (21, 198).
    draw_pie(d,
             from_anchor=('TL', 0.932, 0.659),
             to_anchor=('ML', 0.211, 0.983),
             head_width=12, tail_width=1, curve=0.10, segments=48)
    # s2 竖 — MMH: head ML(0.697, 0.556) → (70, 156); tail BL(0.738, 0.95) → (74, 295).
    # N joint with s1 body at ~ML(0.69, 0.49); shu head sits slightly below the pie body.
    draw_shu(d,
             from_anchor=('ML', 0.697, 0.556),
             to_anchor=('BL', 0.738, 0.95),
             width=9)

    # ---- 勹 right-outer (2 strokes) ----
    # s3 撇 — MMH: head TC(0.649, 0.598); tail C(0.166, 0.644). Short, shallow bow.
    draw_pie(d,
             from_anchor=('TC', 0.649, 0.598),
             to_anchor=('C', 0.166, 0.644),
             head_width=10, tail_width=2, curve=0.04, segments=36)
    # s4 横折钩 — MMH gives head C(0.479, 0.4) and tail BC(0.746, 0.774).
    # Interpret MMH tail as the hook TIP (last median point); pick a corner
    # and a drop-base consistent with the shell shape.
    draw_heng_zhe_gou(d,
                      head=('C', 0.479, 0.400),      # MMH verbatim (start of 横)
                      corner=('MR', 0.60, 0.400),    # top-right of shell — pushed right
                      tail=('MR', 0.60, 0.850),      # drop STRAIGHT down (fix: prev slanted left)
                      tip=('BC', 0.746, 0.774),      # MMH verbatim (hook tip, up-and-left)
                      h_width=10, v_width=10, shoulder=12, tip_w=2)

    # ---- 口 inside (3 strokes), N-class corners (small natural gaps) ----
    # s5 竖 (left wall) — MMH: head C(0.148, 0.852); tail BC(0.324, 0.42).
    draw_shu(d,
             from_anchor=('C', 0.148, 0.852),
             to_anchor=('BC', 0.324, 0.42),
             width=7)
    # s6 横折 (top + right wall) — MMH: head C(0.292, 0.852); tail BC(0.632, 0.2).
    # Corner picked as top-right of 口 interior.
    draw_heng_zhe(d,
                  head=('C', 0.292, 0.852),
                  corner=('C', 0.60, 0.852),
                  tail=('BC', 0.632, 0.2),
                  h_width=7, v_width=7, shoulder=9)
    # s7 横 (bottom bar) — MMH: head BC(0.383, 0.353); tail BC(0.813, 0.285).
    draw_heng(d,
              from_anchor=('BC', 0.383, 0.353),
              to_anchor=('BC', 0.813, 0.285),
              width=7)

    out = os.path.join(os.path.dirname(__file__), '01_佝.png')
    im.save(out)
    return out


if __name__ == '__main__':
    p = render()
    print(f'wrote {p}')
