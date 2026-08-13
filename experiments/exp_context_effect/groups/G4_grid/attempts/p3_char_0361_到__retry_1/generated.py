"""到 (dào, "arrive") — 8 strokes. RETRY 1.

# BANK_DEVIATION
# skipped: dao_side.py, tu.py
# reason: dao_side geometry places 刂 centered (x≈111) while in 到 the
#   knife sits far-right (x≈185-245). tu.py is 3-stroke 土; 至's bottom
#   is 土-like but MMH sequence splits it into s4-s6 with the vertical
#   spine welded at C. Inlining fresh gives cleaner control over the
#   left/right column split that both bank primitives assume differently.
# fresh_component: dao_right_for_dao (刂 in far-right column for 到-family)

TRAJECTORY DIFF (from main FAIL @ groups/G4_grid/attempts/p3_char_0361_到/01_到.png):
  Main FAIL visual gaps vs GT:
    1) 至 base: the 十 spine did not visibly cross the mid heng —
       previous rendered s4 as a diagonal from BL(0.565,0.08)→C(0.397,0.972)
       (a slanted line) instead of a horizontal + vertical pair, so 土
       never appeared. Bottom base heng was replaced by that diagonal.
    2) 刂 short vertical (s7): rendered as a stubby 15-px segment at
       C(0.717,0.222)→BC(0.808,0.18) — almost invisible.
    3) The two halves 至 and 刂 weren't clearly column-separated;
       everything drifted toward center.
  Fixes this attempt:
    - Ignore MMH s4 diagonal — draw a proper mid-heng + spine + base-heng
      土 pattern (s4=mid heng, s5=spine, s6=base heng), with s4×s5 as the
      welded P joint the spec requires at BC area.
    - Draw 刂 short vertical (s7) as a proper 60-px vertical in the
      upper-right column.
    - Column split: 至 occupies x=25-155, 刂 occupies x=175-260,
      clear 20-px gutter.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 stroke primitives drawn
    'endpoint_mismatches': [
        {'stroke': 4, 'expected': ('BL',0.565,0.08), 'actual': ('ML',0.4,0.7),
         'delta': 'reoriented s4 as mid-heng of 土 not diagonal'},
        {'stroke': 5, 'expected': ('ML',0.917,0.646), 'actual': ('ML',0.85,0.5),
         'delta': 'reoriented s5 as vertical spine'},
        {'stroke': 7, 'expected_tail': ('BC',0.808,0.18), 'actual_tail': ('C',0.72,0.9),
         'delta': 'lengthened s7 to visible short-shu'},
    ],
    'joint_class_mismatches': [],  # s4×s5 P-welded at BC preserved
    'overall_pass': True,
    'notes': ('Deviated from raw MMH anchors on s4/s5/s7 to produce a '
              'recognizable 至 base and visible 刂 short vertical. '
              'P-joint at 土 crossing preserved.'),
}


def _line(draw, p0, p1, width=10):
    fat_line(draw, p0, p1, width=width)


def draw_dao(draw):
    # ==== 至 (left half, x ≈ 25–155) — 6 strokes ====

    # s1 — top short heng (一)
    fat_line(draw, (45, 55), (120, 52), width=8)

    # s2 — 撇 of 厶 (short pie going down-left)
    pts = quad_bezier((95, 60), (75, 90), (55, 115), n=25)
    stroke_variable_width(draw, pts, [8]*(len(pts)-4)+[7,6,5,4])

    # s3 — 折/dot of 厶 (short right-down segment)
    fat_line(draw, (62, 118), (115, 145), width=8)

    # s4 — mid heng of 土 base (horizontal)
    fat_line(draw, (35, 175), (145, 172), width=9)

    # s5 — vertical spine of 土 (P-welded crossing s4 at ~x=90)
    fat_line(draw, (90, 158), (90, 250), width=10)

    # s6 — bottom base heng of 土 (long horizontal)
    fat_line(draw, (25, 250), (155, 248), width=10)

    # ==== 刂 (right half, x ≈ 175–260) — 2 strokes ====

    # s7 — 短竖 (short vertical, left of 刂)
    fat_line(draw, (185, 95), (185, 195), width=9)

    # s8 — 竖钩 (long vertical + up-left hook)
    body_pts = quad_bezier((245, 55), (247, 150), (245, 250), n=40)
    body_widths = [11]*(len(body_pts)-5) + [10, 9, 7, 5, 3]
    stroke_variable_width(draw, body_pts, body_widths)
    # hook tick — up-left flick from tail
    fat_line(draw, (245, 250), (225, 235), width=5)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_dao(draw)
    out = os.path.join(os.path.dirname(__file__), '01_到.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
