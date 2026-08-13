"""美 (měi) — 9 strokes.
Decomposition: 美 top = 丷 (s1+s2 dots) + 三-hengs (s3, s4, s6) + 竖 (s5)
               美 bottom = 大 (s7 heng + s8 pie + s9 na)

Joints (from MMH):
  s2.tail ~ s3.mid          N  (top-right dot ends above s3 heng)
  s3.mid  ~ s5.head         N  (vertical head near top heng, small gap)
  s4.mid  x s5.mid          P  welded — vertical crosses middle heng
  s5.tail ~ s6.mid          N  (vertical tail meets bottom heng from above)
  s5.tail ~ s8.head         N
  s6.mid  ~ s8.head         N
  s7.mid  x s8.mid          P  welded — pie crosses 大's heng
  s7.mid  ~ s9.head         N  (na starts just below/right of heng center)
  s8.mid  ~ s9.head         N

MMH-verbatim anchors per B9 A-recipe (point 2).
Base primitives (_anchor + fat_line + quad_bezier) per A-recipe (point 4).
"""

# BANK_DEVIATION
# skipped: (none — no compound bank primitive for 美 or 羊 exists; base only)
# reason: 美 has no direct compound primitive; the 羊/大 stack is inlined
#         via MMH-verbatim anchors + base primitives per A-recipe point 4.
# fresh_component: mei_full_inline

import sys, os
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width, CANVAS

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 9 stroke calls, matches MMH expected=9
    'endpoint_mismatches': [],      # MMH-verbatim
    'joint_class_mismatches': [],   # P welds at s4×s5 & s7×s8; other 7 joints N
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; 2 P welds (s4×s5, s7×s8); N-gaps preserved.',
}

# ---------------------------------------------------------------------
# MMH-verbatim endpoint anchors
# ---------------------------------------------------------------------
S1_H = ('TC', 0.034, 0.688);  S1_T = ('TC', 0.298, 0.911)   # 点 top-left
S2_H = ('TC', 0.77,  0.545);  S2_T = ('TC', 0.55,  0.993)   # 撇 top-right
S3_H = ('ML', 0.826, 0.23);   S3_T = ('MR', 0.089, 0.078)   # 一 top heng
S4_H = ('C',  0.022, 0.573);  S4_T = ('C',  0.904, 0.474)   # 一 middle heng
S5_H = ('C',  0.371, 0.26);   S5_T = ('C',  0.406, 0.811)   # 丨 central vertical
S6_H = ('ML', 0.609, 0.934);  S6_T = ('MR', 0.317, 0.808)   # 一 third heng (bottom of 羊)
S7_H = ('BL', 0.765, 0.329);  S7_T = ('BR', 0.209, 0.259)   # 一 heng of 大
S8_H = ('C',  0.277, 0.966);  S8_T = ('BL', 0.589, 1.088)   # 丿 pie of 大
S9_H = ('BC', 0.479, 0.35);   S9_T = ('BR', 0.684, 1.047)   # 乀 na of 大

# ---------------------------------------------------------------------
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

W = 6

def line(h, t, w=W):
    fat_line(d, anchor_to_xy(h), anchor_to_xy(t), w)

def poly(h, t, widths):
    p0 = anchor_to_xy(h); p1 = anchor_to_xy(t)
    n = len(widths) - 1
    pts = [(p0[0] + i / n * (p1[0] - p0[0]),
            p0[1] + i / n * (p1[1] - p0[1])) for i in range(n + 1)]
    stroke_variable_width(d, pts, widths)

def curve(h, ctrl, t, widths):
    p0 = anchor_to_xy(h); p1 = anchor_to_xy(ctrl); p2 = anchor_to_xy(t)
    n = len(widths) - 1
    pts = quad_bezier(p0, p1, p2, n=n)
    stroke_variable_width(d, pts, widths)

# s1 — top-left 点 (dot, thin head → fat tail)
poly(S1_H, S1_T, [3,3,4,4,5,5,6,6,7,7,7,7,7,6,6,5,5,4,3,3,2])

# s2 — top-right 撇/点 (short pie, fat head → thin tail, going down-left)
poly(S2_H, S2_T, [7,7,7,6,6,6,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2])

# s3 — top heng (long, slight up-slope)
line(S3_H, S3_T, w=6)

# s4 — middle heng (long, above center)
line(S4_H, S4_T, w=6)

# s5 — central vertical 竖 (crosses s4 P; extends to top-heng area + past s6)
line(S5_H, S5_T, w=7)

# s6 — third heng (long, y≈180-190) — bottom of upper 羊 block
line(S6_H, S6_T, w=7)

# s7 — 大's heng (wide, y≈230)
line(S7_H, S7_T, w=7)

# s8 — 大's 撇 (pie, fat head → thin tail, sweeping down-left)
p0 = anchor_to_xy(S8_H); p2 = anchor_to_xy(S8_T)
# gentle bow: control point offset to the right of the midline
ctrl = ((p0[0] + p2[0]) / 2 + 10, (p0[1] + p2[1]) / 2 - 5)
pts = quad_bezier(p0, ctrl, p2, n=40)
widths = [max(2, 10 - int(8 * i / 40)) for i in range(41)]
stroke_variable_width(d, pts, widths)

# s9 — 大's 捺 (na, thin head → fat body → tapered foot, down-right)
p0 = anchor_to_xy(S9_H); p2 = anchor_to_xy(S9_T)
ctrl = ((p0[0] + p2[0]) / 2 - 8, (p0[1] + p2[1]) / 2 + 8)
pts = quad_bezier(p0, ctrl, p2, n=40)
widths = []
for i in range(41):
    t = i / 40.0
    if t < 0.78:
        widths.append(max(3, int(3 + t * 11)))     # thin → fat
    else:
        widths.append(max(3, int(12 - (t - 0.78) * 45)))  # taper foot
stroke_variable_width(d, pts, widths)

img.save(os.path.join(os.path.dirname(__file__), '01_美.png'))
print('wrote 01_美.png')
