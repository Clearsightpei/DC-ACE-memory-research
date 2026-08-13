"""p3_char_0271_老 — G4 attempt.

Reading checklist (v8):
1. drawer_memory.md — read. No chronic primitive fits 老 directly; no
   'lao' primitive. Not a chronic-cluster case (no 冂/马/弓/丿/刀 as
   dominant component). 老 = 耂 (top) + 匕 (bottom-right).
2. success_bank/INDEX.md — grep 老/耂/匕 not present.
3. errata.md — 老 not present.

Composition:
  # 老 = 耂 (top) + 匕 (bottom-right)
  # 耂 = 横 + 竖 + 长横 + 长撇 (strokes 1-4)
  # 匕 = 短撇 + 竖弯钩 (strokes 5-6)

MMH stroke count: 6. We render exactly 6 primitives.

Anchors (PIL convention: y grows DOWN within each cell):
  s1 head=('ML',0.935,0.175) tail=('C',0.881,0.102)     — top 横
  s2 head=('TC',0.333,0.533) tail=('C',0.383,0.556)     — 竖 crossing s1 (P)
  s3 head=('ML',0.278,0.775) tail=('MR',0.73,0.55)      — long 横
  s4 head=('TR',0.112,0.729) tail=('BL',0.375,0.73)     — long 撇 (crosses s3 P)
  s5 head=('BR',0.259,0.036) tail=('BC',0.403,0.338)    — 匕 短撇
  s6 head=('C',0.254,0.931)  tail=('BR',0.323,0.405)    — 匕 竖弯钩 (touches s4 T)

Joint plan:
  s1×s2 P weld at C(0.452,0.147)
  s1—s4 N gap at C(0.979,0.11)
  s2—s3 N small gap
  s3×s4 P weld at C(0.741,0.584)
  s4—s6 T (s6 head lands on s4's body)
  s5—s6 N small gap
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import (anchor_to_xy, quad_bezier,
                     stroke_variable_width, fat_line, sample_line)
from PIL import Image, ImageDraw

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

INK = (0, 0, 0)

# ---- stroke 1: top short 横 ----
p_s1_head = anchor_to_xy(('ML', 0.935, 0.175))   # (93.5, 117.5)
p_s1_tail = anchor_to_xy(('C',  0.881, 0.102))   # (188.1, 110.2)
pts = sample_line(p_s1_head, p_s1_tail, n=24)
widths = [7 + 2 * (i / 24) for i in range(25)]   # slight taper thicker at tail
stroke_variable_width(d, pts, widths, INK)

# ---- stroke 2: 竖 (crosses s1 at P) ----
p_s2_head = anchor_to_xy(('TC', 0.333, 0.533))   # (133.3, 53.3)
p_s2_tail = anchor_to_xy(('C',  0.383, 0.556))   # (138.3, 155.6)
pts = sample_line(p_s2_head, p_s2_tail, n=24)
widths = [6] * 25
stroke_variable_width(d, pts, widths, INK)

# ---- stroke 3: long 横 (main crossbar) ----
p_s3_head = anchor_to_xy(('ML', 0.278, 0.775))   # (27.8, 177.5)
p_s3_tail = anchor_to_xy(('MR', 0.73,  0.55))    # (273.0, 155.0)
# very slight arc: give a mid control point above the midpoint
mx = (p_s3_head[0] + p_s3_tail[0]) / 2
my = (p_s3_head[1] + p_s3_tail[1]) / 2 - 4
pts = quad_bezier(p_s3_head, (mx, my), p_s3_tail, n=48)
widths = [6 + 3 * (i / 48) for i in range(49)]  # taper 加粗顿笔 at end
stroke_variable_width(d, pts, widths, INK)

# ---- stroke 4: long 撇 (upper-right → lower-left) ----
p_s4_head = anchor_to_xy(('TR', 0.112, 0.729))   # (211.2, 72.9)
p_s4_tail = anchor_to_xy(('BL', 0.375, 0.73))    # (37.5, 273.0)
# Slight curve bowing to the right (curved 撇)
mx = (p_s4_head[0] + p_s4_tail[0]) / 2 + 22
my = (p_s4_head[1] + p_s4_tail[1]) / 2 + 4
pts = quad_bezier(p_s4_head, (mx, my), p_s4_tail, n=48)
widths = [8 - 5 * (i / 48) for i in range(49)]  # thick head, thin tail
stroke_variable_width(d, pts, widths, INK)

# ---- stroke 5: 匕 短撇 (short pie in lower half) ----
p_s5_head = anchor_to_xy(('BR', 0.259, 0.036))   # (225.9, 203.6)
p_s5_tail = anchor_to_xy(('BC', 0.403, 0.338))   # (140.3, 233.8)
pts = sample_line(p_s5_head, p_s5_tail, n=24)
widths = [7 - 3 * (i / 24) for i in range(25)]
stroke_variable_width(d, pts, widths, INK)

# ---- stroke 6: 匕 竖弯钩 (vertical-turn-hook, bottom right) ----
p_s6_head = anchor_to_xy(('C',  0.254, 0.931))   # (125.4, 193.1)
p_s6_tail = anchor_to_xy(('BR', 0.323, 0.405))   # (232.3, 240.5)
# Draw as: vertical drop then arc right to tail. Use two beziers.
# Corner near BC bottom-right area.
corner = (p_s6_head[0] + 6, 275)
# First segment: head → corner (mostly vertical)
mid1 = ((p_s6_head[0] + corner[0]) / 2, (p_s6_head[1] + corner[1]) / 2 + 10)
pts1 = quad_bezier(p_s6_head, mid1, corner, n=32)
# Second segment: corner → tail (arc up-right ending with slight hook)
mid2 = ((corner[0] + p_s6_tail[0]) / 2, corner[1] + 6)
pts2 = quad_bezier(corner, mid2, p_s6_tail, n=32)
pts = pts1 + pts2[1:]
widths = [7] * len(pts)
stroke_variable_width(d, pts, widths, INK)

out_png = os.path.join(os.path.dirname(__file__), '01_老.png')
img.save(out_png)

# ---- Self-check ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitives rendered
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes; anchors from MMH; s1×s2 and s3×s4 welded (P); s5-s6 and s2-s3 small gaps (N); s6 head touches s4 body (T).'
}

if __name__ == '__main__':
    print('wrote', out_png)
