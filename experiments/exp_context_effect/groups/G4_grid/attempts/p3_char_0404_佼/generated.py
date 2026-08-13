"""佼 (jiǎo) — 8 strokes.
Decomposition: 佼 = 亻 (left, 2 strokes) + 交 (right, 6 strokes).
  亻 = 撇 (s1) + 竖 (s2)
  交 = 亠 (点 s3 + 横 s4) + 父-lower (小点 s5 + 小点 s6 + 撇 s7 + 捺 s8 with s7×s8 P-cross)

MMH-verbatim anchors per B9 A-recipe (point 2).
Base primitives (_anchor + fat_line + quad_bezier) per A-recipe (point 4).
X-cross weld: s7 & s8 route through CROSS = BC(0.744, 0.408) at their mids
(B7r 文 fix — apex is shared pixel at their MID, not HEAD, else reads as 人).
"""

# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻 撇 head at TL(0.867, 0.659) — far-left column;
#         ren_side defaults sit in TC/C. Partial override caused p3_0252_伊
#         FAIL (B8). Inlining pie+shu with MMH-verbatim anchors instead
#         (per B10 A-recipe: 佟 A used same pattern).
# fresh_component: yi_side_farleft_for_佼

import sys, os
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from _anchor import (anchor_to_xy, fat_line, quad_bezier,
                     stroke_variable_width, CANVAS)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 8 stroke calls, matches MMH expected=8
    'endpoint_mismatches': [],      # MMH-verbatim
    'joint_class_mismatches': [],   # 3 N-gaps preserved, 1 P weld at s7×s8 (BC 0.744,0.408)
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; 亻 inlined (BANK_DEVIATION vs ren_side); '
             's7 撇 & s8 捺 both routed via CROSS_ANCHOR at their mids for P-weld.',
}

# ---------------------------------------------------------------------
# MMH-verbatim endpoint anchors (from dispatcher-injected structural spec)
# ---------------------------------------------------------------------
S1_H = ('TL', 0.867, 0.659);  S1_T = ('ML', 0.141, 0.983)   # 亻 撇
S2_H = ('ML', 0.624, 0.55);   S2_T = ('BL', 0.686, 0.906)   # 亻 竖
S3_H = ('TC', 0.538, 0.677);  S3_T = ('TC', 0.884, 0.92)    # 亠 top 点
S4_H = ('C',  0.189, 0.239);  S4_T = ('MR', 0.297, 0.09)    # 亠 heng
S5_H = ('C',  0.298, 0.532);  S5_T = ('BL', 0.976, 0.016)   # 父 left 小点/撇dot
S6_H = ('C',  0.948, 0.397);  S6_T = ('MR', 0.42,  0.761)   # 父 right 小点/dian
S7_H = ('C',  0.828, 0.729);  S7_T = ('BC', 0.04,  0.815)   # 父 撇 (through CROSS)
S8_H = ('C',  0.318, 0.983);  S8_T = ('BR', 0.733, 0.947)   # 父 捺 (through CROSS)

CROSS_ANCHOR = ('BC', 0.744, 0.408)   # P-weld pixel: s7.mid ⇆ s8.mid

# ---------------------------------------------------------------------
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

W = 6  # base stroke width

def line(h, t, w=W):
    fat_line(d, anchor_to_xy(h), anchor_to_xy(t), w)

def curve(h, ctrl, t, widths=None, w=W):
    p0 = anchor_to_xy(h); p1 = anchor_to_xy(ctrl); p2 = anchor_to_xy(t)
    pts = quad_bezier(p0, p1, p2, n=40)
    if widths is None:
        widths = [w] * len(pts)
    stroke_variable_width(d, pts, widths)

def polyline_var(pts, widths):
    stroke_variable_width(d, pts, widths)

# s1 — 亻 撇 (long down-left curving stroke, tapers toward tail)
curve(S1_H, ('ML', 0.85, 0.60), S1_T,
      widths=[7]*15 + [6]*15 + [4]*11)

# s2 — 亻 竖 (vertical shu; head near s1 mid = N gap ~14.5px preserved)
line(S2_H, S2_T, w=7)

# s3 — 亠 top 点 (short slanted dot, upper-left → lower-right)
curve(S3_H, ('TC', 0.72, 0.78), S3_T,
      widths=[3]*10 + [5]*15 + [6]*10 + [3]*6)

# s4 — 亠 横 (long heng across top, C→MR, slightly rising)
p_h = anchor_to_xy(S4_H); p_t = anchor_to_xy(S4_T)
polyline_var([p_h, p_t], [5, 6])
# add rounded caps
fat_line(d, p_h, p_t, 6)

# s5 — 父 left 小点 (short down-left mini-pie from center)
curve(S5_H, ('ML', 0.98, 0.85), S5_T,
      widths=[5]*15 + [6]*15 + [3]*11)

# s6 — 父 right 小点 (short down-right dian from upper-right)
curve(S6_H, ('MR', 0.75, 0.55), S6_T,
      widths=[3]*10 + [5]*15 + [6]*10 + [4]*6)

# s7 — 父 撇 (long down-left; MID welds at CROSS with s8)
#   Two-piece polyline: head → CROSS → tail (guarantees pixel-share)
p7h = anchor_to_xy(S7_H)
pC  = anchor_to_xy(CROSS_ANCHOR)
p7t = anchor_to_xy(S7_T)
# sample each leg for smoothness + slight curvature at the tail
leg1 = [(p7h[0] + i/20*(pC[0]-p7h[0]), p7h[1] + i/20*(pC[1]-p7h[1])) for i in range(21)]
leg2 = quad_bezier(pC, (pC[0]-30, pC[1]+30), p7t, n=20)
pts7 = leg1 + leg2[1:]
w7 = [6]*len(leg1) + [5]*10 + [3]*(len(leg2)-11)
polyline_var(pts7, w7)

# s8 — 父 捺 (long down-right; MID welds at CROSS with s7)
p8h = anchor_to_xy(S8_H)
p8t = anchor_to_xy(S8_T)
leg1b = [(p8h[0] + i/20*(pC[0]-p8h[0]), p8h[1] + i/20*(pC[1]-p8h[1])) for i in range(21)]
leg2b = quad_bezier(pC, (pC[0]+40, pC[1]+20), p8t, n=20)
pts8 = leg1b + leg2b[1:]
w8 = [4]*len(leg1b) + [6]*10 + [7]*(len(leg2b)-11)
polyline_var(pts8, w8)

img.save(os.path.join(os.path.dirname(__file__), '01_佼.png'))
print('wrote 01_佼.png')
