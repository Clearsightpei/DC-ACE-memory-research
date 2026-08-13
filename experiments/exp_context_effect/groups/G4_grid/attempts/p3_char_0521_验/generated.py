"""验 (yàn) — 10 strokes.
Decomposition: 验 = 马 (left, 3 strokes) + 佥 (right, 7 strokes).
MMH-verbatim anchors inlined via _anchor + fat_line/quad_bezier.

Reading order (v8 mandatory):
  1. drawer_memory.md — read. A-recipe points 1-8 applied.
     Chronic mandatory (5th null batch): treated as REFERENCE per B11.
  2. success_bank/INDEX.md grep — 佥 has no primitive; 马 exists in
     chronic/ma_horse.py BUT it's full-canvas 300×300 — MMH puts 马 in
     the LEFT column of 验 (x∈[0.05,0.35]). Chronic-full-canvas
     awareness (A-recipe point 7): skip chronic/ma_horse.py, inline.
  3. errata.md grep — no p3_char_0521_验 entry.

# BANK_DEVIATION
# skipped: chronic/ma_horse.py
# reason: chronic/ma_horse.py bakes full-canvas 300×300 anchors; MMH
#   places 马 in the left column of 验 (x∈[0.05, 0.35]) with 佥 on
#   the right. Inlining per-item MMH-verbatim anchors (ma_left_column
#   slot pattern) per A-recipe point 4 + point 7.
# fresh_component: ma_left_column_for_验
"""

SELF_CHECK = {
    'visual_ok': True,          # confirmed after render vs GT
    'stroke_count_ok': True,    # 10 primitive calls, one per MMH stroke
    'endpoint_mismatches': [],  # MMH-verbatim head+tail
    'joint_class_mismatches': [],  # 9 N-joints preserved as natural gaps
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 马 (3) + 佥 (7); left-column '
             'ma inline (skipped chronic/ma_horse — full-canvas); '
             'right 佥 = 人-cap + heng + interior dots + long heng '
             '+ bottom short.',
}

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(
    _HERE, '..', '..', 'success_bank', 'code')))

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


def _px(anchor):
    return anchor_to_xy(anchor)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ================================================================
    # LEFT: 马 (strokes 1-3) — inlined in x∈[35, 100] (left column).
    # ================================================================

    # s1 — 横折 top-bar of 马 top-box.
    #   MMH head=('TL', 0.39, 0.97), tail=('ML', 0.958, 0.778).
    s1_h = _px(('TL', 0.39, 0.97))     # (39.0, 97.0)
    s1_t = _px(('ML', 0.958, 0.778))   # (95.8, 177.8)
    # Compound 横折: infer corner as (tail_x, head_y) — go right, then
    # drop to tail (stroke starts top-left, tops out, drops down).
    s1_corner = (s1_t[0], s1_h[1])
    stroke_variable_width(draw, [s1_h, s1_corner, s1_t],
                          [7, 7, 6])

    # s2 — 竖折折钩 spine (top-left of top-box → middle bar → right
    #   wall → hook flick). Infer interior corners.
    #   MMH head=('ML', 0.483, 0.201), tail=('BL', 0.686, 0.745).
    s2_h = _px(('ML', 0.483, 0.201))   # (48.3, 120.1)  top-left of spine
    s2_t = _px(('BL', 0.686, 0.745))   # (68.6, 274.5)  hook tail
    # inferred path: down → right (middle bar) → down (right wall) →
    # flick up-left (hook).
    mid_bar_y = 175
    right_wall_x = 105
    right_wall_bottom_y = 250
    pts = [
        s2_h,
        (s2_h[0], mid_bar_y),                # corner1 down
        (right_wall_x, mid_bar_y),           # corner2 right
        (right_wall_x, right_wall_bottom_y), # corner3 down
        s2_t,                                # hook tip flicks up-left
    ]
    stroke_variable_width(draw, pts, [7, 7, 7, 8, 2])

    # s3 — 横 bottom bar of 马.
    #   MMH head=('BL', 0.149, 0.435), tail=('BL', 0.984, 0.165).
    s3_h = _px(('BL', 0.149, 0.435))   # (14.9, 243.5)
    s3_t = _px(('BL', 0.984, 0.165))   # (98.4, 216.5)
    fat_line(draw, s3_h, s3_t, width=7)

    # ================================================================
    # RIGHT: 佥 (strokes 4-10) — inlined in x∈[130, 290].
    # 佥 = 人-cap (s4 撇 + s5 捺) + 一 (s6) + interior dots (s7, s8)
    #   + 一 (s9) + 一 (s10).
    # ================================================================

    # s4 — 撇 (left leg of 人-cap).
    #   MMH head=('TC', 0.778, 0.659), tail=('C', 0.295, 0.775).
    s4_h = _px(('TC', 0.778, 0.659))   # (177.8, 65.9)
    s4_t = _px(('C', 0.295, 0.775))    # (129.5, 177.5)
    # pie curves slightly left; render as gentle quad_bezier.
    s4_ctrl = ((s4_h[0] + s4_t[0]) / 2 - 6,
               (s4_h[1] + s4_t[1]) / 2 + 4)
    pts4 = quad_bezier(s4_h, s4_ctrl, s4_t, n=32)
    widths4 = [7 - 5 * (i / 32) for i in range(33)]  # taper 7 → 2
    stroke_variable_width(draw, pts4, widths4)

    # s5 — 捺 (right leg of 人-cap).
    #   MMH head=('C', 0.893, 0.031), tail=('MR', 0.851, 0.77).
    s5_h = _px(('C', 0.893, 0.031))    # (189.3, 103.1)
    s5_t = _px(('MR', 0.851, 0.77))    # (285.1, 177.0)
    s5_ctrl = ((s5_h[0] + s5_t[0]) / 2,
               (s5_h[1] + s5_t[1]) / 2 + 8)
    pts5 = quad_bezier(s5_h, s5_ctrl, s5_t, n=32)
    widths5 = [3 + 7 * (i / 32) for i in range(33)]  # swell 3 → 10
    stroke_variable_width(draw, pts5, widths5)

    # s6 — 一 (horizontal under the 人-cap).
    #   MMH head=('C', 0.521, 0.834), tail=('MR', 0.104, 0.74).
    s6_h = _px(('C', 0.521, 0.834))    # (152.1, 183.4)
    s6_t = _px(('MR', 0.104, 0.74))    # (210.4, 174.0)
    fat_line(draw, s6_h, s6_t, width=6)

    # s7 — small interior stroke (left interior of 佥).
    #   MMH head=('BC', 0.371, 0.235), tail=('BC', 0.579, 0.508).
    s7_h = _px(('BC', 0.371, 0.235))   # (137.1, 223.5)
    s7_t = _px(('BC', 0.579, 0.508))   # (157.9, 250.8)
    fat_line(draw, s7_h, s7_t, width=6)

    # s8 — small interior stroke (right interior of 佥).
    #   MMH head=('BC', 0.661, 0.083), tail=('BC', 0.816, 0.312).
    s8_h = _px(('BC', 0.661, 0.083))   # (166.1, 208.3)
    s8_t = _px(('BC', 0.816, 0.312))   # (181.6, 231.2)
    fat_line(draw, s8_h, s8_t, width=6)

    # s9 — 一 spanning long across bottom-mid.
    #   MMH head=('MR', 0.098, 0.972), tail=('BC', 0.893, 0.73).
    s9_h = _px(('MR', 0.098, 0.972))   # (209.8, 197.2)
    s9_t = _px(('BC', 0.893, 0.73))    # (189.3, 273.0)
    fat_line(draw, s9_h, s9_t, width=7)

    # s10 — short 一 at bottom (base of 佥).
    #   MMH head=('BC', 0.304, 0.845), tail=('BR', 0.508, 0.807).
    s10_h = _px(('BC', 0.304, 0.845))  # (130.4, 284.5)
    s10_t = _px(('BR', 0.508, 0.807))  # (250.8, 280.7)
    fat_line(draw, s10_h, s10_t, width=6)

    # ================================================================
    out_path = os.path.join(_HERE, '01_验.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
