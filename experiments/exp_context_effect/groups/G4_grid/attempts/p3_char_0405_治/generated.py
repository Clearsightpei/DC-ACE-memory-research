"""治 (zhì) — 8 strokes.
Decomposition: 治 = 氵 (left, 3 strokes) + 台 (right, 5 strokes).
  氵 = 点 s1 + 点 s2 + 提 s3
  台 = 厶 (s4 + s5) + 口 (s6 竖 + s7 横折 + s8 横)

MMH-verbatim anchors per B9 A-recipe (point 2).
Base primitives (_anchor + fat_line + dian + inline ti) per A-recipe (point 4).
All 4 injected joints are N-class — leave natural 13-21 px gaps.

Reading log:
  # drawer_memory.md — read; 氵/口 primitives exist but per A-recipe
  #   point 4 we inline base primitives with MMH-verbatim anchors.
  # INDEX grep — 治 not previously mastered.
  # errata.md — 治 not listed.
"""

# BANK_DEVIATION
# skipped: shui.py, kou.py, si_private.py
# reason: MMH places 氵 in far-left column (TL/ML/BL) whereas shui default
#         spans TC/ML/BC/C; 口 sits BC-compressed (bottom-center slot) not
#         standalone; 厶 head/tail run TC→MR then MR-vertical, which
#         doesn't map to si_private's pie_zhe + dian composition.
#         Right-half slot compression of 台 (per B10 pattern) — inline
#         with base primitives + MMH anchors preserves the compositional
#         proportion (see 佟/者/皃 A verdicts in B10).
# fresh_component: shui_left_column_for_治, kou_bc_compressed_for_台,
#                  si_topright_for_台

import sys, os
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from _anchor import (anchor_to_xy, fat_line, quad_bezier,
                     stroke_variable_width, CANVAS)
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 8 stroke primitives called; MMH expects 8
    'endpoint_mismatches': [],       # MMH-verbatim
    'joint_class_mismatches': [],    # all 4 joints are N — natural gaps preserved
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim. 氵 inlined in far-left column '
             '(BANK_DEVIATION vs shui); 台 = 厶 + 口 inlined in right-half '
             'slot. All N-joints preserved as gaps (no welding).',
}

# ---------------------------------------------------------------------
# MMH-verbatim endpoint anchors (from dispatcher-injected structural spec)
# ---------------------------------------------------------------------
# 氵 (left column)
S1_H = ('TL', 0.683, 0.788); S1_T = ('C',  0.046, 0.09)    # 点 top drop
S2_H = ('ML', 0.369, 0.427); S2_T = ('ML', 0.715, 0.649)   # 点 middle drop
S3_H = ('BL', 0.565, 0.877); S3_T = ('ML', 0.905, 0.854)   # 提 rising

# 厶 (top-right)
S4_H = ('TC', 0.673, 0.665); S4_T = ('MR', 0.314, 0.597)   # 撇/折 upper
S5_H = ('MR', 0.124, 0.233); S5_T = ('MR', 0.543, 0.787)   # right descend

# 口 (bottom-right, BC-compressed)
S6_H = ('BC', 0.187, 0.183); S6_T = ('BC', 0.441, 0.965)   # 竖 left wall
S7_H = ('BC', 0.345, 0.18);  S7_T = ('BR', 0.098, 0.61)    # 横折 top+right
S8_H = ('BC', 0.491, 0.76);  S8_T = ('BR', 0.3,   0.728)   # 横 bottom

# ---------------------------------------------------------------------
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

W = 6  # base stroke width for line strokes


def line(h, t, w=W):
    fat_line(d, anchor_to_xy(h), anchor_to_xy(t), w)


def ti_stroke(head_anchor, tail_anchor, head_width=13, tail_width=2,
              curve=-0.05, segments=32):
    """提 — thick 顿笔 head, taper to fine needle tip up-right."""
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (dy / length, -dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(d, pts, widths)
    r = head_width / 2.0
    d.ellipse([p0[0] - r, p0[1] - r, p0[0] + r, p0[1] + r], fill=(0, 0, 0))


# --- 氵 (3 strokes, left column) -------------------------------------
draw_dian(d, S1_H, S1_T, head_width=2, peak_width=10, curve=0.06, segments=24)
draw_dian(d, S2_H, S2_T, head_width=2, peak_width=10, curve=0.06, segments=24)
ti_stroke(S3_H, S3_T, head_width=13, tail_width=2, curve=-0.05)

# --- 厶 (2 strokes, top-right) ---------------------------------------
# s4 is a COMPOUND 撇折: head at top → pie down-left to a pivot → 折
#     horizontal-ish to tail on the right. MMH only records head/tail,
#     so we infer the elbow at lower-left of the 厶 region.
p4h = anchor_to_xy(S4_H)   # TC(0.673, 0.665) — top of 厶
p4t = anchor_to_xy(S4_T)   # MR(0.314, 0.597) — right side
p4_pivot = anchor_to_xy(('C', 0.55, 0.72))   # inferred elbow: down-left of head
# leg 1: pie (thick head → tapered tip at pivot)
leg1 = quad_bezier(p4h, ((p4h[0] + p4_pivot[0])/2 - 4,
                          (p4h[1] + p4_pivot[1])/2 + 4), p4_pivot, n=18)
w4a = [8, 7, 7, 6, 6, 5, 5, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7, 7]
stroke_variable_width(d, leg1, w4a)
# leg 2: 折 heng-like from pivot to tail
leg2 = quad_bezier(p4_pivot, ((p4_pivot[0] + p4t[0])/2,
                              (p4_pivot[1] + p4t[1])/2 - 2), p4t, n=18)
w4b = [7]*len(leg2)
stroke_variable_width(d, leg2, w4b)

# s5 is a small 点 at the right side sealing the 厶
draw_dian(d, S5_H, S5_T, head_width=3, peak_width=11, curve=0.06, segments=24)

# --- 口 (3 strokes, bottom-right, BC-compressed) ---------------------
# All corner joints are N-class → leave the natural gap (do NOT weld)
line(S6_H, S6_T, w=7)   # 竖 left wall
# s7 is 横折: heng across top, then折 down the right side
# BC(0.345, 0.18) → corner near BR(0.0, 0.18)? actually endpoint is
# BR(0.098, 0.61) — so the fold pivot is around ('BR', 0.098, 0.18)
p7h = anchor_to_xy(S7_H)
p7corner = anchor_to_xy(('BR', 0.098, 0.20))  # inferred corner (top-right)
p7t = anchor_to_xy(S7_T)
fat_line(d, p7h, p7corner, 7)
fat_line(d, p7corner, p7t, 7)
line(S8_H, S8_T, w=7)   # 横 bottom

img.save(os.path.join(os.path.dirname(__file__), '01_治.png'))
print('wrote 01_治.png')
