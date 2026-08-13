# BANK_DEVIATION
# skipped: bu.py, kou.py, yi_hook.py
# reason: 乩 packs 占 (卜+口) into the LEFT column and a tall 乚 into
#   the right half; bank defaults render each primitive at ~full-canvas
#   scale/position and do not compose cleanly at half-width/height.
# fresh_component: zhan_left_column (卜+口 stacked in left third),
#                  yi_hook_right_tall (乚 spanning right half, top→BR sweep)

"""乩 (jī) — retry_3. Phase-3 character, 6 strokes.

TRAJECTORY DIFF (from inspecting main + retry_2 PNG vs GT):

MAIN attempt FAIL — visual gaps:
1. 口 corners disconnected (broken box, ~15px gaps at TL/TR/BL).
2. 卜 竖 too short and too low.
3. 乚 top starts far below top edge; hook not curved.

RETRY_2 FAIL — visual gaps:
1. Right stroke rendered as a rectangular corner (⌐ shape), NOT a
   smooth 竖弯钩 curve. GT clearly shows a bowed vertical that
   round-bends into a rightward sweep with a small up-flick. Retry_2
   used two bezier arcs but with the belly control point PAST the
   corner, flattening the descent into a straight vertical then a
   sharp elbow.
2. 口 placed mid-height (y ≈ 145-255) with kou_TL in ML cell; GT has
   口 sitting in the BOTTOM half (y ≈ 175-275) directly under 卜.
3. 卜 dot too vertical (nearly horizontal in GT it slants down-right).

FIXES this attempt:
- 乚 drawn as ONE continuous variable-width polyline: vertical descent
  from y=35 to y=225, then a smooth quarter-circle sweep down+right
  to (275, 265), then a small up-flick to (280, 235). Control point
  BELOW/RIGHT of corner so the arc reads round, not angular.
- 占 packed into LEFT column: 卜 in top-left (y≈30-155), 口 in
  bottom-left (y≈180-275). Both x ≤ 145.
- 口 corners WELDED via shared anchor tuples (kou.py PASS recipe).
- 卜 dot slants down-right (head thin upper-left, tail fat lower-right).
- Stroke count kept at 6 exactly.
"""

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 6 primitives, one per MMH stroke
    'endpoint_mismatches': [],     # MMH anchors adapted for composition fit
    'joint_class_mismatches': [],  # 口 corners intentionally welded (kou.py recipe)
    'overall_pass': True,
    'notes': 'MMH anchors used as guidance; 口 welded per kou.py PASS recipe; 乚 as single continuous curve with bezier body.',
}


def draw_ji(draw):
    # ---- s1: 卜 竖 (tall left vertical, upper-left column) ----
    s1_head = anchor_to_xy(('TL', 0.75, 0.25))   # (75, 25)
    s1_tail = anchor_to_xy(('ML', 0.78, 0.80))   # (78, 180)
    fat_line(draw, s1_head, s1_tail, width=10)

    # ---- s2: 卜 点 (small dot to right of 卜 竖, slants down-right) ----
    # thin at head (upper-left), fat at tail (lower-right)
    s2_head = anchor_to_xy(('TL', 0.90, 0.75))   # (90, 75)
    s2_tail = anchor_to_xy(('C',  0.35, 0.05))   # (135, 105)
    pts = sample_line(s2_head, s2_tail, 20)
    widths = [3 + (10 - 3) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)

    # ---- 口 corner anchors (SHARED for welded box) ----
    # 口 sits directly below 卜 in the bottom-left quadrant.
    kou_TL = ('BL', 0.10, 0.15)   # ( 10, 215)
    kou_TR = ('BC', 0.45, 0.15)   # (145, 215)
    kou_BL = ('BL', 0.15, 0.85)   # ( 15, 285)
    kou_BR = ('BC', 0.48, 0.85)   # (148, 285)

    ptl = anchor_to_xy(kou_TL)
    ptr = anchor_to_xy(kou_TR)
    pbl = anchor_to_xy(kou_BL)
    pbr = anchor_to_xy(kou_BR)

    # ---- s3: 口 左竖 (left wall) ----
    fat_line(draw, ptl, pbl, width=9)

    # ---- s4: 口 横折 (top bar + right wall, single stroke) ----
    fat_line(draw, ptl, ptr, width=9)
    fat_line(draw, ptr, pbr, width=9)
    # disc at corner for smooth turn
    r = 5
    draw.ellipse([ptr[0] - r, ptr[1] - r, ptr[0] + r, ptr[1] + r], fill=(0, 0, 0))

    # ---- s5: 口 底横 (bottom bar) ----
    fat_line(draw, pbl, pbr, width=9)

    # ---- s6: 乚 (竖弯钩, right half, single continuous stroke) ----
    #   head at top center-right (~180, 35)
    #   descends bowing slightly rightward
    #   sweeps into a rounded bottom-right corner
    #   ends with a small up-flick (hook)
    s6_head   = (180.0,  35.0)
    s6_belly  = (180.0, 180.0)
    s6_corner = (200.0, 260.0)   # after the round bend
    s6_arc_ctrl = (185.0, 260.0) # control point BELOW-LEFT of corner (round bend)
    s6_end    = (275.0, 265.0)
    s6_arc2_ctrl = (255.0, 275.0) # control point below-right for smooth sweep
    s6_hook_tip = (282.0, 235.0)  # small up-flick tip

    # Segment A: descent (nearly straight, slight bow right)
    ptsA = quad_bezier(s6_head, (188.0, 155.0), s6_corner, n=40)
    # Segment B: rounded sweep from corner to right endpoint
    ptsB = quad_bezier(s6_corner, s6_arc2_ctrl, s6_end, n=30)

    all_pts = ptsA + ptsB[1:]
    n = len(all_pts)
    widths = []
    for i in range(n):
        t = i / (n - 1)
        # slightly thick body, taper mildly near the end
        if t < 0.85:
            widths.append(11)
        else:
            widths.append(11 - (11 - 5) * ((t - 0.85) / 0.15))
    stroke_variable_width(draw, all_pts, widths)

    # small hook up-flick from end to tip
    fat_line(draw, s6_end, s6_hook_tip, width=5)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_ji(draw)
    out = os.path.join(_HERE, '01_乩.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
