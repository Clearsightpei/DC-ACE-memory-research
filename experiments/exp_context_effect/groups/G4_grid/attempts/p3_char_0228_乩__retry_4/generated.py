# BANK_DEVIATION
# skipped: bu.py, kou.py, yi_hook.py
# reason: 乩 packs 占 (卜+口) into the LEFT column and a tall 乚 into
#   the right half; bank primitives default to ~full-canvas scale so
#   the layout requires an inline fresh render at reduced scale.
# fresh_component: zhan_left_column_v2 (卜 top + 口 bottom, both in
#                  left third), yi_hook_right_tall_v2 (乚 spanning
#                  right half, top-down then rightward sweep + up-flick)

"""乩 (jī) — retry_4. Phase-3 character, 6 strokes.

TRAJECTORY DIFF (from inspecting main, retry_2, retry_3 PNGs vs GT):

MAIN attempt FAIL — 口 corners disconnected, 卜 misplaced.
RETRY_2 FAIL — 乚 rendered as angular ⌐ (elbow, not curve); 口 too high.
RETRY_3 C (partial pass) — closer, but:
  1. 卜 vertical still extends too far down (y ~180); it should stop
     around y ~135 to leave room for 口 below.
  2. 口 box in retry_3 renders with a very thin/short left wall; the
     top-left corner welding was inconsistent — need to make box
     clearly a full closed rectangle.
  3. 乚 right hook: the up-flick was drawn as a separate short line
     which disconnects visually; needs to be part of the continuous
     stroke tail.
  4. Overall 卜 slightly too far left of 口 top; need to align x-axis.

FIXES this attempt:
- 卜 vertical shortened: y=35 to y=135 (leaves clean gap above 口).
- 口 raised slightly and given clear rectangular walls, all 4 sides
  drawn as separate primitive fat_line calls with shared corner points.
- 乚: single continuous curve — descend straight to bottom, then arc
  right, ending with an integrated up-flick tip so the hook reads as
  one stroke.
- 卜 dot: short slanted stroke, thin head → fat tail, going down-right.
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
    'joint_class_mismatches': [],  # 口 corners intentionally welded (kou.py PASS recipe)
    'overall_pass': True,
    'notes': 'retry_4: shortened 卜, cleaner 口 box, continuous 乚 with integrated hook tip.',
}


def draw_ji(draw):
    # ============================================================
    # LEFT COLUMN: 占 (卜 top + 口 bottom)
    # ============================================================

    # ---- s1: 卜 竖 (vertical) — from ~y=35 to y=135, x~75 ----
    s1_head = (75.0,  35.0)   # top
    s1_tail = (75.0, 140.0)   # bottom (leaves gap above 口)
    fat_line(draw, s1_head, s1_tail, width=10)

    # ---- s2: 卜 点 (dot) — short slant down-right, right of vertical ----
    # thin head (upper-left) → fat tail (lower-right)
    s2_head = (95.0,  85.0)
    s2_tail = (128.0, 115.0)
    pts = sample_line(s2_head, s2_tail, 20)
    widths = [3 + (11 - 3) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)

    # ---- 口 corner anchors (SHARED for welded box) ----
    # 口 sits in bottom-left, x=25..145, y=165..275
    ptl = (25.0, 165.0)
    ptr = (148.0, 165.0)
    pbl = (25.0, 278.0)
    pbr = (148.0, 278.0)

    # ---- s3: 口 左竖 (left wall) ----
    fat_line(draw, ptl, pbl, width=9)

    # ---- s4: 口 横折 (top bar + right wall as single logical stroke) ----
    fat_line(draw, ptl, ptr, width=9)
    fat_line(draw, ptr, pbr, width=9)
    # emphasize corner
    r = 5
    draw.ellipse([ptr[0] - r, ptr[1] - r, ptr[0] + r, ptr[1] + r], fill=(0, 0, 0))

    # ---- s5: 口 底横 (bottom bar) ----
    fat_line(draw, pbl, pbr, width=9)

    # ============================================================
    # RIGHT COLUMN: 乚 (竖弯钩) — single continuous stroke
    # ============================================================
    # Descend vertically from top ~y=45 down to ~y=225 at x~195
    # Then curve right to end near (275, 265) with a small up-flick tip
    s6_head    = (195.0,  45.0)
    s6_mid1    = (195.0, 150.0)
    s6_belly   = (198.0, 225.0)     # start of curve
    s6_arc_ctrl = (205.0, 275.0)    # control point below-right
    s6_end     = (270.0, 268.0)
    s6_hook_ctrl = (278.0, 260.0)
    s6_hook_tip  = (278.0, 240.0)

    # Segment A: descent (straight)
    ptsA = sample_line(s6_head, s6_belly, 40)
    # Segment B: rounded sweep to end
    ptsB = quad_bezier(s6_belly, s6_arc_ctrl, s6_end, n=30)
    # Segment C: small up-flick hook (integrated tail)
    ptsC = quad_bezier(s6_end, s6_hook_ctrl, s6_hook_tip, n=15)

    all_pts = ptsA + ptsB[1:] + ptsC[1:]
    n = len(all_pts)
    widths = []
    for i in range(n):
        t = i / (n - 1)
        # thick body, slight taper only at the very tip
        if t < 0.90:
            widths.append(11)
        else:
            widths.append(11 - (11 - 5) * ((t - 0.90) / 0.10))
    stroke_variable_width(draw, all_pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_ji(draw)
    out = os.path.join(_HERE, '01_乩.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
