"""p3_char_0441_前 — 9 strokes.

Composition:
  1-2: 丷 (two dots at top) — inlined; no bank primitive for this specific
       narrow-inverted-V dot pair.
  3:   一 (long horizontal, dominant) — bank draw_heng.
  4-7: 月 (bottom-left) — bank draw_yue_moon (4-stroke composite).
  8-9: 刂 (bottom-right) — bank draw_dao_right (2-stroke composite).

Total called strokes = 2 (inline) + 1 (heng) + 4 (yue_moon internals)
                     + 2 (dao_right internals) = 9. Matches MMH count.

# BANK_DEVIATION
# skipped: (none — used yue_moon.py and dao_right.py at scaled placement;
#          only the top 丷 dots are inline because bank has no matching
#          divergent-dot-pair primitive at this scale)
# reason: 丷 top of 前 has two very short divergent strokes not represented
#         by any single bank primitive; inlining as short pies is simpler
#         than promoting a whole radical bank entry for two 20-30 px dabs.
# fresh_component: fen_top_dots_for_qian (two-dot 丷 pair used in
#                  前/首/兰/羊/半; if these succeed for 前 the curator may
#                  promote as a variant).

# P-A-008 reasoning trace:
#   GT inspection: 前 = 丷 (top) + 一 (long heng) + 月 (BL) + 刂 (BR).
#   MMH gives 9 strokes with s1/s2 in TC (dots), s3 spanning ML→MR (long
#   heng), s4-6 clustered in ML/BL (月 pie + hzg + inner strokes), s7 in
#   BL (last inner heng of 月), s8-9 in C→BC (刂 verticals). Bank has
#   yue_moon (4 strokes, scale to fit BL) and dao_right (2 strokes, scale
#   to fit BR). P-A-006 (stroke-primitive layer) satisfied via inlined
#   dots + bank calls for the standard sub-radicals.
# P-A-009 quantitative BANK_DEVIATION:
#   yue_moon native: 136 w × 205 h (aspect 0.663). Target 月 in 前: needs
#   ~100 w × 155 h (aspect 0.645) → scale ≈ 0.75. Matches native aspect
#   within 3%; use uniform scale=0.75 with ox=15.9, oy=55.
#   dao_right native: 50 w × 199 h (aspect 0.251). Target 刂 in 前:
#   ~40 w × 170 h (aspect 0.235) → scale ≈ 0.85. Matches within 6%;
#   use uniform scale=0.85 with ox=90, oy=45.
"""

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng          # noqa: E402
from yue_moon import draw_yue_moon  # noqa: E402
from dao_right import draw_dao_right  # noqa: E402
from pie import draw_pie            # noqa: E402


def draw_qian(draw: ImageDraw.ImageDraw):
    # ---- 丷 top dots (strokes 1, 2) ----
    # Two short divergent strokes. Left dot slants down-LEFT; right
    # dot slants down-RIGHT. Small w_head, tiny w_tail (dot taper).
    draw_pie(draw, (128, 30), (108, 66),
             bow_perp=3, w_head=5, w_tail=3)   # s1 (left dot)
    draw_pie(draw, (188, 30), (208, 66),
             bow_perp=-3, w_head=5, w_tail=3)  # s2 (right dot)

    # ---- s3: long dominant 一 ----
    draw_heng(draw, (28, 100), (272, 88),
              width_head=9, width_tail=11)

    # ---- s4-s7: 月 (bottom-left) ----
    draw_yue_moon(draw, ox=15.9, oy=55, scale=0.75)

    # ---- s8-s9: 刂 (bottom-right) ----
    draw_dao_right(draw, ox=90, oy=45, scale=0.85)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 dots + 1 heng + 4 (yue_moon) + 2 (dao_right) = 9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 6 joints expected class N — natural gaps preserved
                                   # via disjoint sub-radical placement.
    'overall_pass': True,
    'notes': ('9-stroke count OK. 月 lives in BL (x 55-157, y 110-264), '
              '刂 lives in BR (x 184-227, y 105-274), both hanging below '
              'the long heng at y~90-100. Top dots occupy TC region '
              '(x 108-208, y 30-66). All 6 MMH joints are class N '
              '(natural gap) and are preserved because sub-radicals are '
              'drawn disjoint (no forced welding).')
}


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_qian(d)
    img.save(os.path.join(HERE, "01_前.png"))
    print("wrote 01_前.png")
