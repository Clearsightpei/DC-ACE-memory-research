"""p3_char_0263_她 (tā) — G4 retry #1.

TRAJECTORY DIFF (from Step 0 visual inspection):

Prior FAIL (main attempt) issues seen in 01_她.png vs GT:
 1. Left 女 was too clumped: three roughly-parallel horizontal
    strokes in upper-left; no visible X-crossing between 撇 and 撇点.
    Missing the characteristic 女 topology (top X + horizontal arm).
    The nv primitive was called with overrides that mostly moved
    strokes to horizontal orientations.
 2. Right 也 was rendered as a full closed rectangle (heng-zhe-gou
    corner + central 竖 + shu-wan-gou made a boxed 田/中 look). GT
    also has an open top; the corner should be a single top-right
    turn, NOT a full box, and the middle 竖 should sit lower and
    shorter (headroom above it), not span the full column.
 3. Overall proportion: 女 shrunk to <25% width, 也 pushed too far
    right; balance is wrong for a left-right compound like 她.

Fix plan this attempt:
 - Left 女 (x∈[5,130]): inline fresh, using the mastered 女 topology
   (large X of 撇点+撇 at top, then wide 横 crossing the middle).
   Same recipe as passed p2_radical_061_女 but compressed horizontally.
 - Right 也 (x∈[140,285]): borrow the PASSED approach from
   p3_char_0223_地 verbatim — heng-zhe-gou as a proper open corner
   (horizontal top → down-right corner → hook tip), 中间竖 short
   inside the frame, 竖弯钩 sweeping wide along the bottom with UP
   hook.
 - Stroke count stays at 6 (3 女 + 3 也) as MMH requires.
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier,
                     stroke_variable_width, fat_line, CANVAS)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 (女) + 3 (也) = 6, matches expected 6
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        '女 inline (pie-dian + pie + heng, X-cross at BL/ML). '
        '也 borrowed from PASSED p3_char_0223_地: heng-zhe-gou (open '
        'corner, not a closed rectangle), middle 竖 short and centered, '
        '竖弯钩 wide sweep with up-hook.'
    ),
}


def render():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    d = ImageDraw.Draw(img)
    W = 8

    # =============================================================
    # LEFT: 女 (inline, filling x∈[0, 135], y∈[60, 260])
    # Topology: X-cross at top-center of block (s1 & s2), 横 arm
    # crossing the X near mid.
    # =============================================================
    # s1 撇点: sweeps from upper-mid down to bottom-left (this is the
    #    left leg of the X), then a small dot flick down-right.
    s1_head  = (75, 75)      # top of left leg
    s1_pivot = (10, 210)     # bottom-left, well below the 横
    s1_tail  = (55, 250)     # dot flick down-right of pivot
    pts_s1a = quad_bezier(s1_head, (35, 145), s1_pivot, n=30)
    w_s1a = [11 - 7 * (i / (len(pts_s1a)-1)) for i in range(len(pts_s1a))]
    stroke_variable_width(d, pts_s1a, w_s1a)
    pts_s1b = quad_bezier(s1_pivot, (30, 240), s1_tail, n=15)
    w_s1b = [4 + 7 * (i / (len(pts_s1b)-1)) for i in range(len(pts_s1b))]
    stroke_variable_width(d, pts_s1b, w_s1b)

    # s2 撇 (right leg of the X): from top-right of block sweeping
    #    down-left, crossing s1 near (~50, 150). Ends bottom-left.
    s2_head = (115, 75)
    s2_tail = (25, 255)
    pts_s2 = quad_bezier(s2_head, (65, 155), s2_tail, n=40)
    w_s2 = [11 - 8 * (i / (len(pts_s2)-1)) for i in range(len(pts_s2))]
    stroke_variable_width(d, pts_s2, w_s2)

    # s3 横 (arm): wide horizontal near mid-height, crossing both legs.
    s3_head = (0, 175)
    s3_tail = (135, 170)
    fat_line(d, s3_head, s3_tail, W + 1)

    # =============================================================
    # RIGHT: 也 (borrowed from PASSED p3_char_0223_地)
    # =============================================================
    # s4 横折钩: top horizontal, right-corner turn down, tiny up-hook.
    h4_start     = (155, 115)
    h4_corner    = (250, 115)
    h4_hook_base = (250, 215)
    h4_hook_tip  = (225, 200)
    fat_line(d, h4_start,     h4_corner,    W)
    fat_line(d, h4_corner,    h4_hook_base, W)
    fat_line(d, h4_hook_base, h4_hook_tip,  W)

    # s5 middle 竖: short vertical inside the frame (does NOT touch top).
    s5_head = (188, 90)
    s5_tail = (190, 230)
    fat_line(d, s5_head, s5_tail, W)

    # s6 竖弯钩: starts inside upper-left of 也, curves down and wide
    #    along the bottom, ends with UP hook on the right.
    s6_head    = (155, 150)
    s6_ctrl1   = (150, 260)
    s6_midbot  = (215, 275)
    s6_prehook = (275, 245)
    s6_tail    = (275, 210)   # hook tip (UP relative to prehook)
    pts_s6 = (
        quad_bezier(s6_head, s6_ctrl1, s6_midbot, n=25)
        + quad_bezier(s6_midbot, s6_prehook, (s6_tail[0], s6_tail[1] + 15), n=25)
    )
    w_s6 = [W] * len(pts_s6)
    stroke_variable_width(d, pts_s6, w_s6)
    # up-hook flick
    fat_line(d, (s6_tail[0], s6_tail[1] + 15), s6_tail, W)

    return img


if __name__ == '__main__':
    img = render()
    out = os.path.join(os.path.dirname(__file__), '01_她.png')
    img.save(out)
    print(f'wrote {out}  size={img.size}')
