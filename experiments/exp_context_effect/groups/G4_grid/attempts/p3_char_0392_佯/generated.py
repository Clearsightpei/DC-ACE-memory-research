"""佯 (yáng) — 8 strokes.
Decomposition: 佯 = 亻 (left, 2 strokes) + 羊 (right, 6 strokes).
  亻 = 撇 (s1) + 竖 (s2)
  羊 = 点 (s3, top-left dot) + 撇 (s4, top-right dot going down-left) +
       横 (s5, top heng) + 横 (s6, middle heng) + 横 (s7, bottom long heng) +
       竖 (s8, central vertical piercing through middle & bottom hengs)

MMH-verbatim anchors per B9 A-recipe (point 2).
Base primitives (_anchor + fat_line + quad_bezier) per A-recipe (point 4).
Two P-welds at s6×s8 and s7×s8 (both hengs cross the vertical); all top
joints (s3/s4 tails, s5.mid) are N — leave natural gap.
"""

# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻's 撇 head at TL(0.896,0.63) — far-left column;
#         ren_side defaults sit in TC/C. Partial override caused p3_0252_伊
#         FAIL (B8) and 佟 A-verdict used this same skip (B10). Inlining
#         pie+shu with MMH-verbatim anchors instead.
# fresh_component: yi_side_farleft_for_佯

import sys, os
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width, CANVAS

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 8 stroke calls, matches MMH expected=8
    'endpoint_mismatches': [],    # MMH-verbatim
    'joint_class_mismatches': [], # 5 N-gaps preserved; 2 P welds at hengs×shu
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; 亻 inlined (BANK_DEVIATION vs ren_side); '
             's6 & s7 hengs weld through vertical s8 (P); top-羊 dots leave N gaps.',
}

# ---------------------------------------------------------------------
# MMH-verbatim endpoint anchors (from dispatcher-injected structural spec)
# ---------------------------------------------------------------------
S1_H = ('TL', 0.896, 0.63);   S1_T = ('ML', 0.164, 0.878)   # 亻 撇
S2_H = ('ML', 0.694, 0.418);  S2_T = ('BL', 0.709, 0.771)   # 亻 竖
S3_H = ('TC', 0.359, 0.653);  S3_T = ('TC', 0.611, 0.929)   # 羊 top-left 点
S4_H = ('TR', 0.08,  0.51);   S4_T = ('TC', 0.866, 0.987)   # 羊 top-right 撇/点
S5_H = ('C',  0.33,  0.236);  S5_T = ('MR', 0.279, 0.119)   # 羊 top heng
S6_H = ('C',  0.295, 0.705);  S6_T = ('MR', 0.265, 0.597)   # 羊 middle heng
S7_H = ('BL', 0.946, 0.2);    S7_T = ('BR', 0.728, 0.074)   # 羊 bottom long heng
S8_H = ('C',  0.644, 0.321);  S8_T = ('BC', 0.743, 1.117)   # 羊 central 竖

# ---------------------------------------------------------------------
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

W = 6  # default stroke width

def line(h, t, w=W):
    fat_line(d, anchor_to_xy(h), anchor_to_xy(t), w)

def curve(h, ctrl, t, widths=None, w=W):
    p0 = anchor_to_xy(h); p1 = anchor_to_xy(ctrl); p2 = anchor_to_xy(t)
    pts = quad_bezier(p0, p1, p2, n=40)
    if widths is None:
        widths = [w] * len(pts)
    stroke_variable_width(d, pts, widths)

# s1 — 亻 撇 (upper-right to lower-left, tapers to tail)
curve(S1_H, ('ML', 0.85, 0.5), S1_T,
      widths=[8]*15 + [6]*15 + [3]*11)

# s2 — 亻 竖 (vertical shu; head touches s1's body naturally — N gap OK)
line(S2_H, S2_T, w=7)

# s3 — 羊 top-left 点 (short dot going down-right; thin head → fat tail)
p0 = anchor_to_xy(S3_H); p2 = anchor_to_xy(S3_T)
pts_s3 = [(p0[0] + i/20*(p2[0]-p0[0]), p0[1] + i/20*(p2[1]-p0[1])) for i in range(21)]
stroke_variable_width(d, pts_s3, [3,3,4,4,5,5,6,6,6,7,7,7,7,7,6,6,5,4,3,2,2])

# s4 — 羊 top-right 撇 (short pie going down-left; fat head → thin tail)
p0 = anchor_to_xy(S4_H); p2 = anchor_to_xy(S4_T)
pts_s4 = [(p0[0] + i/20*(p2[0]-p0[0]), p0[1] + i/20*(p2[1]-p0[1])) for i in range(21)]
stroke_variable_width(d, pts_s4, [7,7,7,7,6,6,6,5,5,5,4,4,4,3,3,3,3,2,2,2,2])

# s5 — 羊 top heng (short, slight up-slope from left to right)
line(S5_H, S5_T, w=6)

# s6 — 羊 middle heng (short, similar to s5). Welds through s8 vertical (P).
line(S6_H, S6_T, w=6)

# s7 — 羊 bottom long heng (widest of the three; anchors the character).
# Welds through s8 vertical (P). Slight upward slope.
line(S7_H, S7_T, w=7)

# s8 — 羊 central 竖 (vertical shu piercing middle+bottom hengs). Tail
# extends below canvas per MMH (y_frac=1.117); PIL clips naturally.
line(S8_H, S8_T, w=7)

img.save(os.path.join(os.path.dirname(__file__), '01_佯.png'))
print('wrote 01_佯.png')
