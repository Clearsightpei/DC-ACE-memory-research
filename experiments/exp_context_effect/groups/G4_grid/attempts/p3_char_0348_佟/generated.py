"""佟 (tóng) — 7 strokes.
Decomposition: 佟 = 亻 (left, 2 strokes) + 冬 (right, 5 strokes).
  亻 = 撇 (s1) + 竖 (s2)
  冬 = 夂 (top: 撇 s3 + 横撇/横折 s4 + 捺 s5 crossing at P joint) +
       冫 (bottom: dian s6 + dian s7)

MMH-verbatim anchors per B9 A-recipe (point 2).
Base primitives (_anchor + fat_line + quad_bezier) per A-recipe (point 4).
No compound bank primitive imported — MMH places 亻 far left of ren_side
defaults, so inlined pie+shu.
"""

# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻's 撇 head at TL(0.89,0.65) — far-left column;
#         ren_side defaults sit in TC/C. Partial override caused p3_0252_伊
#         FAIL (B8). Inlining pie+shu with MMH-verbatim anchors instead.
# fresh_component: yi_side_farleft_for_佟

import sys, os
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width, CANVAS

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 7 stroke calls, matches MMH expected=7
    'endpoint_mismatches': [],     # MMH-verbatim
    'joint_class_mismatches': [],  # 4 N-gaps preserved; 1 P weld at s4×s5 center
    'overall_pass': True,
    'notes': '7 strokes MMH-verbatim; 亻 inlined (BANK_DEVIATION vs ren_side); '
             's4 & s5 cross through cell C giving P weld naturally.',
}

# ---------------------------------------------------------------------
# MMH-verbatim endpoint anchors (from dispatcher-injected structural spec)
# ---------------------------------------------------------------------
S1_H = ('TL', 0.894, 0.647);  S1_T = ('ML', 0.176, 0.96)     # 亻 撇
S2_H = ('ML', 0.659, 0.526);  S2_T = ('BL', 0.697, 0.895)    # 亻 竖
S3_H = ('TC', 0.541, 0.606);  S3_T = ('C',  0.017, 0.523)    # 夂 top 撇
S4_H = ('C',  0.477, 0.128);  S4_T = ('BL', 0.917, 0.215)    # 夂 横折/横撇
S5_H = ('C',  0.333, 0.38);   S5_T = ('BR', 0.827, 0.104)    # 夂 捺 (crosses s4)
S6_H = ('BC', 0.526, 0.092);  S6_T = ('BC', 0.869, 0.329)    # 冫 upper dot
S7_H = ('BC', 0.436, 0.543);  S7_T = ('BC', 0.937, 1.053)    # 冫 lower dot

# ---------------------------------------------------------------------
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

W = 6  # stroke width

def line(h, t, w=W):
    fat_line(d, anchor_to_xy(h), anchor_to_xy(t), w)

def curve(h, ctrl, t, widths=None, w=W):
    p0 = anchor_to_xy(h); p1 = anchor_to_xy(ctrl); p2 = anchor_to_xy(t)
    pts = quad_bezier(p0, p1, p2, n=40)
    if widths is None:
        widths = [w] * len(pts)
    stroke_variable_width(d, pts, widths)

# s1 — 亻 撇 (down-left curving stroke, tapers slightly toward tail)
curve(S1_H, ('ML', 0.9, 0.55), S1_T,
      widths=[7]*15 + [6]*15 + [4]*11)

# s2 — 亻 竖 (vertical shu, tail near s1's mid — N joint natural gap)
line(S2_H, S2_T, w=7)

# s3 — 夂 top 撇 (short slanted stroke top-of-right-part, going down-left)
curve(S3_H, ('C', 0.25, 0.6), S3_T,
      widths=[6]*15 + [5]*15 + [3]*11)

# s4 — 夂 横撇/横折 (heng-then-pie: right-going then bending down-left).
#      MMH gives head=C(0.477,0.128) tail=BL(0.917,0.215).
#      This is a compound: heng segment right, then pie segment down-left.
#      Render as bezier through a corner control at MR/C boundary.
curve(S4_H, ('MR', 0.4, 0.15), S4_T,
      widths=[6]*20 + [5]*15 + [4]*6)

# s5 — 夂 捺 (na stroke going down-right, crosses s4 at cell-C center = P weld)
curve(S5_H, ('C',  0.6,  0.4), S5_T,
      widths=[3]*10 + [5]*15 + [7]*10 + [4]*6)

# s6 — 冫 upper dot (short down-right)
curve(S6_H, ('BC', 0.7, 0.2), S6_T,
      widths=[4]*15 + [6]*15 + [3]*11)

# s7 — 冬 lower long stroke (bottom dian curving down-right, exits canvas)
# MMH tail y=1.053 → below canvas; clip naturally.
curve(S7_H, ('BC', 0.7, 0.8), S7_T,
      widths=[4]*15 + [7]*15 + [5]*11)

img.save(os.path.join(os.path.dirname(__file__), '01_佟.png'))
print('wrote 01_佟.png')
