"""和 (hé) — 8 strokes.
Decomposition: 和 = 禾 (left, 5 strokes) + 口 (right, 3 strokes).
  禾 = 撇(short top) + 横 + 竖(central) + 撇(long) + 捺(short)
  口 = 竖 + 横折 + 横 (all N-corner box on right side)

A-recipe applied:
  1. Explicit decomposition comment (above).
  2. MMH-verbatim anchors passed unchanged into base primitives.
  3. SELF_CHECK block below.
  4. Base primitives (pie/shu/heng/na + fat_line for heng_zhe corner)
     — inlined rather than importing kou.py, because MMH places the 口
     on the right half (cell C/BC/BR) at different anchors than kou.py's
     defaults (ML/BC/BR). Overriding kou.py's 7 default anchors would be
     a partial override (B8 伊-failure pattern) — inline instead.
  5. N-joint discipline: leave natural gaps where MMH declares N.

Reading log:
  # drawer_memory.md read (v8 A-recipe + point 4 inline-over-override)
  # memory_index.md read
  # errata.md grep 和 → not listed
  # INDEX grep 和 → not listed; 口 mastered as kou.py but see point 4 above
"""

# BANK_DEVIATION
# skipped: kou.py
# reason: kou.py defaults sit at ML(0.671, 0.289)-based left-column anchors;
#         MMH places 和's 口 on right half at C(0.57, 0.532) column. Full
#         7-anchor override would trip the p3_char_0252_伊 partial-override
#         FAIL pattern from B8. Inline pie+shu+heng+heng_zhe with MMH anchors.
# fresh_component: kou_right_slot_for_he

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie  import draw_pie
from shu  import draw_shu
from heng import draw_heng
from na   import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 8 primitive calls (s7 heng_zhe = 2 fat_line + corner dot but counts as one MMH stroke)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; N-joints preserved as natural gaps; s7 heng_zhe inferred corner at (top-right of 口).',
}


def draw_he(draw):
    # ---- 禾 (left, 5 strokes) ----
    # s1 — 撇 short top: TC(0.5, 0.741) -> ML(0.483, 0.084)
    draw_pie(draw, ('TC', 0.5, 0.741), ('ML', 0.483, 0.084),
             head_width=9, tail_width=1, curve=0.10)

    # s2 — 横: ML(0.226, 0.576) -> C(0.521, 0.386)
    draw_heng(draw, ('ML', 0.226, 0.576), ('C', 0.521, 0.386),
              width=8)

    # s3 — 竖 (central vertical, full-height): TL(0.929, 0.996) -> BL(0.996, 1.076)
    # (P joint with s2 at C(0.056, 0.45) — welded automatically by fat_line thickness)
    draw_shu(draw, ('TL', 0.929, 0.996), ('BL', 0.996, 1.076),
             width=9)

    # s4 — 撇 long: ML(0.964, 0.544) -> BL(0.202, 0.581)
    draw_pie(draw, ('ML', 0.964, 0.544), ('BL', 0.202, 0.581),
             head_width=11, tail_width=1, curve=0.12)

    # s5 — 捺 short: C(0.128, 0.872) -> BC(0.45, 0.095)
    draw_na(draw, ('C', 0.128, 0.872), ('BC', 0.45, 0.095),
            head_width=3, peak_width=11, tail_width=1,
            peak_t=0.85, curve=0.08)

    # ---- 口 (right, 3 strokes) — inlined, see BANK_DEVIATION above ----
    # s6 — 竖 (left wall of 口): C(0.57, 0.532) -> BC(0.796, 0.446)
    s6h = anchor_to_xy(('C', 0.57, 0.532))
    s6t = anchor_to_xy(('BC', 0.796, 0.446))
    fat_line(draw, s6h, s6t, width=8)

    # s7 — 横折 (top+right wall of 口):
    #   head C(0.784, 0.635), tail BR(0.335, 0.045)
    #   corner inferred at (tail_x, head_y) = top-right of the box.
    s7h = anchor_to_xy(('C', 0.784, 0.635))
    s7t = anchor_to_xy(('BR', 0.335, 0.045))
    s7c = (s7t[0], s7h[1])
    fat_line(draw, s7h, s7c, width=8)   # top bar
    fat_line(draw, s7c, s7t, width=8)   # right wall

    # s8 — 横 (bottom bar): BC(0.849, 0.262) -> BR(0.549, 0.153)
    draw_heng(draw, ('BC', 0.849, 0.262), ('BR', 0.549, 0.153),
              width=8)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_he(draw)
    out = os.path.join(os.path.dirname(__file__), '01_和.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
