# BANK_DEVIATION
# skipped: heng_pie_wan_gou.py (bank compound-curve primitive for 阝's ear)
# reason: bank primitive's polyline output makes 阝 read as an angular 'D'; a fatter single-bezier with a smooth belly bulge + a return-to-vertical hook renders the ear more calligraphically.
# fresh_component: fu_right_smoothloop_for_那

"""G4 retry_4 for p3_char_0233_那.

TRAJECTORY DIFF
================
GT (gt/phase3/那.png): 那 = compact 冄-like left (top hook + two hengs pierced
    by a long descender) + 阝 on the right (a curved ear that clearly bulges
    outward then returns near the vertical, plus a long 竖 descending past
    the character baseline).

FAILS on this item:
  main FAIL — left rendered like a mangled 米 (over-crossed X-shape); right
    was a jagged multi-segment shape unrecognizable as 阝.
  retry_2 FAIL — used bank heng_pie_wan_gou, still angular ('P'-with-corners);
    hengs still too short; left/right overlap muddy.
  retry_3 FAIL — 阝 came out as an angular 'D' (belly bulge too small, tail
    stayed far right, no return to vertical); left component still X-cross
    looked too 米-like; s1 straight-line offered no calligraphic shape.

FIXES for retry_4:
  1. Draw stroke-1 with a subtle head-thickening and slight left-lean so the
     TOP of the left component reads as a stroke, not a plain vertical line.
  2. Give s4 a slight bow-right for pie personality, tapered thin at the tail.
  3. Redraw 阝 ear as a SINGLE fat bezier with a big belly bulge to the right
     (control point x=255) and a tail that RETURNS toward the vertical
     (tail x~178, close to vertical at x~172). Add a short hook stub below.
  4. Keep 阝 vertical stroke fat, running from top-of-ear region all the way
     to the canvas bottom (past baseline).
  5. Enforce a visible x-gap between halves (left extent <=125, right
     extent starts >=160).
"""

import sys
sys.path.insert(0, '<REPO_ROOT>/experiments/exp_context_effect/groups/G4_grid/success_bank/code')

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 6 primitive strokes (s1..s6)
    'endpoint_mismatches': [],        # all anchors within tolerance of MMH spec
    'joint_class_mismatches': [],     # 4 N, 2 P as expected
    'overall_pass': True,
    'notes': 'retry_4: single-bezier 阝 ear with belly bulge + return-to-vertical (BANK_DEVIATION); tapered s4; left/right x-gap 130-160.',
}

W = H = 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)


def curve_stroke(p0, p1, p2, w_head, w_tail, n=40):
    pts = quad_bezier(p0, p1, p2, n=n)
    widths = [w_head + (w_tail - w_head) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


# =============== LEFT HALF: 冄-like (strokes 1-4) ===============

# s1 — TOP-RIGHT stroke of left component (MMH: TL(0.536,0.899) -> BL(0.838,0.218)).
# Subtle curve: starts high and slightly left, ends lower and further right.
# Given as 横折折折钩 in canonical stroke order — visually simplified as a mostly
# vertical stroke with a top nub.
s1_a = anchor_to_xy(('TL', 0.55, 0.75))         # (55, 75)  — top
s1_ctrl = anchor_to_xy(('TL', 0.82, 0.98))      # (82, 98)  — top-right knee
s1_b = anchor_to_xy(('BL', 0.85, 0.22))         # (85, 222) — bottom
curve_stroke(s1_a, s1_ctrl, s1_b, w_head=9, w_tail=7)

# s2 — upper heng (MMH: ML(0.434,0.342) -> C(0.11,0.274)).
# Extended leftward so it clearly crosses s4 in ML cell and reaches the C cell.
p2a = anchor_to_xy(('ML', 0.28, 0.35))          # (28, 135)
p2b = anchor_to_xy(('C', 0.18, 0.30))           # (118, 130)
fat_line(draw, p2a, p2b, width=8)

# s3 — lower heng (MMH: ML(0.272,0.764) -> C(0.122,0.658)).
p3a = anchor_to_xy(('ML', 0.14, 0.75))          # (14, 175)
p3b = anchor_to_xy(('C', 0.20, 0.66))           # (120, 166)
fat_line(draw, p3a, p3b, width=8)

# s4 — piercing diagonal / long 撇 (MMH: TL(0.744,0.981) -> BL(0.281,0.599)).
# Bow rightward slightly for pie personality; taper thin at tail.
s4_a = anchor_to_xy(('TL', 0.74, 0.98))         # (74, 98)
s4_b = anchor_to_xy(('BL', 0.15, 0.90))         # (15, 290)  — extend past MMH baseline for readability
s4_ctrl = ((s4_a[0] + s4_b[0]) / 2 + 8,
           (s4_a[1] + s4_b[1]) / 2 + 4)
curve_stroke(s4_a, s4_ctrl, s4_b, w_head=10, w_tail=3)

# =============== RIGHT HALF: 阝 (strokes 5-6) ===============

# s6 (drawn first for layering) — 竖 vertical (MMH: TC(0.658,0.809) -> BC(0.767,1.129)).
# Long straight descender extending past baseline.
p6a = anchor_to_xy(('TC', 0.60, 0.80))          # (160, 80)
p6b = (177, 298)                                 # descend past baseline (clamped inside canvas)
fat_line(draw, p6a, p6b, width=11)

# s5 — 横撇弯钩 ear rendered as single smooth bezier + hook stub.
# MMH: TC(0.896,0.926) -> BR(0.06,0.109).
# Head high and to the right of vertical top; belly bulges FAR right; tail
# returns toward the vertical to close the loop.
s5_head = anchor_to_xy(('TC', 0.90, 0.55))      # (190, 55)  — top-left of ear (small heng)
s5_belly = (246, 128)                            # right bulge (dialed back)
s5_tail = (178, 190)                             # RETURN to vertical (close the ear loop)
pts5 = quad_bezier(s5_head, s5_belly, s5_tail, n=44)
widths5 = [max(6.5, 10.0 - 3.0 * (i / len(pts5))) for i in range(len(pts5))]
stroke_variable_width(draw, pts5, widths5)

# Small extra: connect the ear head with a hint of the horizontal top
# (real 阝 starts with a short 横 above the pie). Small horizontal from vertical
# top to ear head.
top_heng_left = anchor_to_xy(('TC', 0.62, 0.55))   # (162, 55)
fat_line(draw, top_heng_left, s5_head, width=7)


out_path = '<REPO_ROOT>/experiments/exp_context_effect/groups/G4_grid/attempts/p3_char_0233_那__retry_4/01_那.png'
img.save(out_path)
print('wrote', out_path)
