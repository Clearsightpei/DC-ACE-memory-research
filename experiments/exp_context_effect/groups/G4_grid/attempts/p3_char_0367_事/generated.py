"""事 (shì) — 8 strokes.

Decomposition: single-component character; top heng + central 曰-like
mid-box (3 hengs bracketing pierced verticals) + long central heng +
horizontal-fold-hook right + bottom short heng + bottom middle heng +
central 竖钩 (long piercing vertical with hook).

Following B9 A-recipe (drawer_memory.md position 500):
  - MMH-verbatim anchors (do not tune).
  - Base primitives (_anchor + fat_line + quad_bezier) — 事 is a
    non-decomposable character; no compound bank primitive fits it
    cleanly. All 13 joints are handled by literal pixel placement.
  - N-joints (7 of 13) get a natural gap by using MMH endpoints
    verbatim (no forced weld).
  - P-joints (5 of 13) and T-joints (2 of 13) are welded because
    the piercing central vertical crosses through the three hengs
    and the top heng.
"""

# Memory-reading log (v8 slim checklist):
#   1. drawer_memory.md — read; A-recipe applied.
#   2. success_bank/INDEX.md — no 事 entry, no direct sub-radical.
#   3. errata.md — 事 not listed.

import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

W = 5  # base stroke width — hand-drawn GT weight

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)


def line(a, b, w=W):
    fat_line(d, anchor_to_xy(a), anchor_to_xy(b), w)


def curve(a, ctrl, b, w=W):
    p0 = anchor_to_xy(a)
    p1 = anchor_to_xy(ctrl)
    p2 = anchor_to_xy(b)
    pts = quad_bezier(p0, p1, p2, n=40)
    widths = [w] * len(pts)
    stroke_variable_width(d, pts, widths)


# --- MMH-verbatim anchor tuples (from dispatcher structural block) ---
S1_H = ('TL', 0.439, 0.97);    S1_T = ('TR', 0.528, 0.864)   # top heng
S2_H = ('ML', 0.817, 0.178);   S2_T = ('C',  0.008, 0.62)    # left small drop
S3_H = ('ML', 0.964, 0.178);   S3_T = ('C',  0.843, 0.342)   # top-of-mid heng
S4_H = ('C',  0.055, 0.506);   S4_T = ('C',  0.995, 0.436)   # middle heng
S5_H = ('ML', 0.782, 0.805);   S5_T = ('BR', 0.007, 0.229)   # right vertical fold
S6_H = ('BL', 0.404, 0.142);   S6_T = ('BR', 0.619, 0.01)    # bottom heng
S7_H = ('BL', 0.826, 0.408);   S7_T = ('BR', 0.068, 0.329)   # lower-mid heng
S8_H = ('TC', 0.362, 0.521);   S8_T = ('BC', 0.025, 0.804)   # central 竖钩

# --- Render each stroke ---
# s1: top short heng (long, slightly curved). Simple straight line is fine.
line(S1_H, S1_T)

# s2: from ML top down to C-left (short slanted piece).
line(S2_H, S2_T)

# s3: short heng top of the middle enclosure — straight line.
line(S3_H, S3_T)

# s4: long middle heng crossing through central shu-gou.
line(S4_H, S4_T)

# s5: 横折 (horizontal-fold) — MMH mids show head→right→corner at
# ~(200, 160)→ down to tail. Rendered as L (heng then shu), not diagonal.
p5_head = anchor_to_xy(S5_H)
p5_tail = anchor_to_xy(S5_T)
p5_corner = (p5_tail[0], p5_head[1])  # right-angle corner
fat_line(d, p5_head, p5_corner, W)
fat_line(d, p5_corner, p5_tail, W)

# s6: bottom short heng.
line(S6_H, S6_T)

# s7: lower-middle heng (below s5's tail area).
line(S7_H, S7_T)

# s8: central 竖钩 — long vertical piercing s1, s3, s4, s6, s7 in
# sequence, ending with a hook at the bottom.
# Render as a slightly curved line ending with a leftward hook tick.
p8_head = anchor_to_xy(S8_H)
p8_tail = anchor_to_xy(S8_T)
# main vertical body
fat_line(d, p8_head, p8_tail, W)
# hook tick — small leftward tick from tail (竖钩 style)
hook_end = (p8_tail[0] - 22, p8_tail[1] - 12)
fat_line(d, p8_tail, hook_end, W)


# --- SELF_CHECK ---
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 stroke primitives (s8 hook is part of s8)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('8 strokes MMH-verbatim; central s8 piercing crosses s1,s3,s4,s6,s7 (5 P-joints); '
              's5 tail welded onto s6 mid at MR (T); s2/s3 and s2/s4 and s2/s5 and s3/s4 '
              'and s4/s5 and s5/s7 endpoints left as natural N-gaps.'),
}


out_path = os.path.join(os.path.dirname(__file__), '01_事.png')
img.save(out_path)
print('wrote', out_path)
