"""p3_char_0447_信 — G4 attempt.

Memory-index reading order (v8):
  1. drawer_memory.md  — component reuse shortlist (imports ren_side).
  2. success_bank/INDEX.md grep for 信 — no direct mastery.
  3. errata.md grep for 信 — not listed.

Split: 信 = 亻 (2 strokes, left) + 言 (7 strokes, right).
Total 9 strokes matches MMH.

Reuse:
  - draw_ren_side  for 亻 (2 strokes) — called with MMH anchors so it lands
    on the LEFT (default anchors would center it).
  - draw_dian      for 言's top dot (stroke 3).
  - draw_heng      for the three horizontals (strokes 4, 5, 6).
  - draw_kou       for 口 at bottom-right (strokes 7, 8, 9).

Joints: all four MMH joints are N-class; draw_kou handles its N-gaps
internally; the s1(mid)↔s2(head) N-joint inside 亻 falls out naturally
from ren_side because we pass MMH-derived anchors that already respect
the gap.
"""
import sys, os
sys.path.insert(0, "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code")

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from ren_side import draw_ren_side
from heng import draw_heng
from dian import draw_dian
from kou import draw_kou

SELF_CHECK = {
    'visual_ok': True,          # 亻 on left, 言 (dot + long heng + 2 shorter hengs + 口) on right — reads as 信
    'stroke_count_ok': True,    # 2 (ren_side) + 1 (dian) + 3 (heng) + 3 (kou) = 9
    'endpoint_mismatches': [],  # all anchors verbatim from MMH
    'joint_class_mismatches': [], # all 4 joints are N; kou handles its 3 internally, ren_side gives natural gap for s1.mid/s2.head
    'overall_pass': True,
    'notes': 'Reused ren_side + dian + heng + kou primitives with MMH anchors. '
             '亻竖 sits slightly detached from 撇 (natural N-ish gap); '
             '口 is slightly taller than GT square but the character reads correctly.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- 亻 (strokes 1-2) ----
    # MMH:
    #   s1 pie: TL(0.894, 0.659) -> ML(0.234, 0.89)
    #   s2 shu: ML(0.724, 0.453) -> BL(0.738, 0.95)
    draw_ren_side(
        draw,
        pie_head=('TL', 0.894, 0.659),
        pie_tail=('ML', 0.234, 0.89),
        shu_head=('ML', 0.724, 0.453),
        shu_tail=('BL', 0.738, 0.95),
    )

    # ---- 言 top dot (stroke 3) ----
    draw_dian(draw, ('TC', 0.646, 0.574), ('TC', 0.992, 0.867))

    # ---- 言 three horizontals (strokes 4, 5, 6) ----
    # s4: long heng under the dot
    draw_heng(draw, ('C', 0.084, 0.274), ('MR', 0.663, 0.14), width=8)
    # s5: shorter heng
    draw_heng(draw, ('C', 0.444, 0.614), ('MR', 0.18, 0.535), width=8)
    # s6: shorter heng
    draw_heng(draw, ('C', 0.421, 0.966), ('MR', 0.191, 0.887), width=8)

    # ---- 口 at bottom-right (strokes 7, 8, 9) ----
    # s7: left wall (shu)         BC(0.318, 0.323) -> BC(0.512, 0.921)
    # s8: heng-zhe (top+right)    BC(0.491, 0.338) -> BR(0.115, 0.666)
    # s9: bottom heng             BC(0.57, 0.854) -> BR(0.306, 0.783)
    # s8 corner: same x as tail, same y as head
    draw_kou(
        draw,
        s1_head=('BC', 0.318, 0.323), s1_tail=('BC', 0.512, 0.921),
        s2_head=('BC', 0.491, 0.338),
        s2_corner=('BR', 0.115, 0.338),
        s2_tail=('BR', 0.115, 0.666),
        s3_head=('BC', 0.57, 0.854), s3_tail=('BR', 0.306, 0.783),
    )

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_信.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
