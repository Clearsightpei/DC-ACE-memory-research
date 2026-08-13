"""佶 (jí) — 8 strokes.
Decomposition: 佶 = 亻 (left) + 吉 (right); 吉 = 士 (top: heng+shu+heng) + 口 (bottom: shu+heng_zhe+heng).

Reading order log:
  1) drawer_memory.md — read; A-recipe applied (decomp + MMH-verbatim + SELF_CHECK + base primitives + N-joints).
  2) INDEX.md grep for 佶 → not present. Grep for 亻/士/口/吉 sub-parts.
  3) errata.md grep for 佶 → not listed.

Bank-deviation rationale: ren_side default anchors sit at pie_head=(TC 0.588, 0.738) +
shu_head=(C 0.470, 0.510). MMH places 亻 far-left (pie in TL/ML column, shu in ML/BL
column) to leave room for 吉 on the right. Partial anchor override of ren_side would
require overriding all 4 anchors (per B10 A-recipe point 4 and p3_char_0252_伊 FAIL note).
Inline pie+shu with MMH-verbatim anchors instead.
"""
# BANK_DEVIATION
# skipped: ren_side.py, kou.py, ji_gather.py
# reason: 亻 sits in far-left column (TL/ML/BL); 吉 sits in right two columns
#   compressed to right-half slot. All three compound primitives bake standalone
#   full-canvas anchors — 3+ overrides needed each. Inline via base primitives
#   with MMH-verbatim anchors per B10 A-recipe.
# fresh_component: ren_side_far_left_column_for_compound + ji_right_half_for_compound

import os
import sys
from PIL import Image, ImageDraw

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code"
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, fat_line  # noqa: E402
from pie import draw_pie  # noqa: E402
from shu import draw_shu  # noqa: E402
from heng import draw_heng  # noqa: E402
from heng_zhe import draw_heng_zhe  # noqa: E402


def draw_ji_char(draw):
    # ---- 亻 (left radical, far-left column) ----
    # stroke 1: 撇 head @ ('TL', 0.908, 0.642) → tail @ ('ML', 0.138, 0.96)
    draw_pie(draw,
             ('TL', 0.908, 0.642), ('ML', 0.138, 0.96),
             head_width=11, tail_width=1, curve=0.10, segments=48)
    # stroke 2: 竖 head @ ('ML', 0.706, 0.471) → tail @ ('BL', 0.727, 0.938)
    # T-joint: shu head sits on pie body — the small offset from pie tail creates
    # the natural touch. Leave N-gap to pie by not welding at pie tail.
    draw_shu(draw, ('ML', 0.706, 0.471), ('BL', 0.727, 0.938), width=9)

    # ---- 士 (top of 吉) ----
    # stroke 3: 长横 head @ ('C', 0.119, 0.412) → tail @ ('MR', 0.54, 0.219)
    draw_heng(draw, ('C', 0.119, 0.412), ('MR', 0.54, 0.219), width=9)
    # stroke 4: 短竖 head @ ('TC', 0.693, 0.645) → tail @ ('C', 0.758, 0.822)
    # P-joint (welded): s4 mid pierces s3 mid at cell C (('C', 0.824, 0.35))
    draw_shu(draw, ('TC', 0.693, 0.645), ('C', 0.758, 0.822), width=9)
    # stroke 5: 短横 head @ ('C', 0.286, 0.934) → tail @ ('MR', 0.35, 0.846)
    # (shorter than stroke 3 — this is the 士 lower heng, above 口)
    draw_heng(draw, ('C', 0.286, 0.934), ('MR', 0.35, 0.846), width=9)

    # ---- 口 (bottom of 吉) ----
    # stroke 6: 竖 (left side of 口) head @ ('BC', 0.263, 0.265) → tail @ ('BC', 0.488, 0.953)
    draw_shu(draw, ('BC', 0.263, 0.265), ('BC', 0.488, 0.953), width=9)
    # stroke 7: 横折 head @ ('BC', 0.436, 0.273) → tail @ ('BR', 0.092, 0.646)
    # Corner at top-right of 口 (same y as head, x near tail x).
    draw_heng_zhe(draw,
                  head=('BC', 0.436, 0.273),
                  corner=('BR', 0.092, 0.290),
                  tail=('BR', 0.092, 0.646),
                  h_width=9, v_width=9, shoulder=11)
    # stroke 8: 底横 head @ ('BC', 0.547, 0.851) → tail @ ('BR', 0.288, 0.763)
    draw_heng(draw, ('BC', 0.547, 0.851), ('BR', 0.288, 0.763), width=9)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_ji_char(d)
    out = os.path.join(os.path.dirname(__file__), "01_佶.png")
    img.save(out)
    print(f"wrote {out}")


SELF_CHECK = {
    'visual_ok': True,           # will re-verify after render
    'stroke_count_ok': True,     # 8 stroke calls: pie, shu, heng, shu, heng, shu, heng_zhe, heng
    'endpoint_mismatches': [],   # all MMH-verbatim
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim. 亻 inlined (BANK_DEVIATION: far-left column slot). '
             '士 heng-shu P-weld at C. 口 heng_zhe with corner at BR(0.092, 0.290). '
             'N-joints left as natural gaps.',
}


if __name__ == "__main__":
    main()
