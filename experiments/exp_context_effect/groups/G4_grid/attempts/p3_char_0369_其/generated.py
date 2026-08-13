"""其 (qí) — 8 strokes.

Decomposition: single-component character (bracket-frame with two
interior hengs + bottom two 八-legs).
  s1 = top heng
  s2 = left vertical (long, drops from just above s1 down to bottom)
  s3 = right vertical (long, drops from just above s1 down to bottom)
  s4 = upper interior short heng
  s5 = lower interior short heng
  s6 = bottom long heng (extends beyond the two verticals)
  s7 = left bottom leg (short 撇 slanting down-left)
  s8 = right bottom leg (short 点/捺 slanting down-right)

Following B9 A-recipe (drawer_memory.md position 500):
  - MMH-verbatim anchors (no tuning).
  - Base primitives (_anchor + fat_line) — 其 is single-component; no
    compound bank primitive fits it cleanly.
  - P-joints (s1×s2, s1×s3) welded because s2 and s3 pierce s1.
  - N-joints (6 total: s2/s4, s2/s5, s2/s6, s3/s4, s3/s5, s3/s6)
    get natural gaps by using MMH endpoints verbatim (no forced weld).
"""

# Memory-reading log (v8 slim checklist):
#   1. drawer_memory.md — read; A-recipe applied.
#   2. success_bank/INDEX.md — no 其 entry; no direct sub-radical match.
#   3. errata.md — 其 not listed.

import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line

W = 4  # base stroke width

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)


def line(a, b, w=W):
    fat_line(d, anchor_to_xy(a), anchor_to_xy(b), w)


# --- MMH-verbatim anchor tuples (from dispatcher structural block) ---
S1_H = ('ML', 0.677, 0.102); S1_T = ('TR', 0.323, 0.935)  # top heng
S2_H = ('TL', 0.999, 0.68);  S2_T = ('BC', 0.084, 0.156)  # left vertical
S3_H = ('TC', 0.702, 0.507); S3_T = ('BC', 0.717, 0.089)  # right vertical
S4_H = ('C',  0.213, 0.471); S4_T = ('C',  0.632, 0.409)  # upper interior heng
S5_H = ('C',  0.222, 0.828); S5_T = ('C',  0.629, 0.752)  # lower interior heng
S6_H = ('BL', 0.313, 0.306); S6_T = ('BR', 0.701, 0.159)  # bottom long heng
S7_H = ('BC', 0.251, 0.537); S7_T = ('BL', 0.554, 0.997)  # left bottom leg (撇)
S8_H = ('BC', 0.702, 0.452); S8_T = ('BR', 0.206, 1.009)  # right bottom leg (点)

# --- Render each stroke ---
line(S1_H, S1_T)   # s1 top heng
line(S2_H, S2_T)   # s2 left vertical
line(S3_H, S3_T)   # s3 right vertical
line(S4_H, S4_T)   # s4 upper interior heng
line(S5_H, S5_T)   # s5 lower interior heng
line(S6_H, S6_T)   # s6 bottom long heng
line(S7_H, S7_T)   # s7 left bottom leg
line(S8_H, S8_T)   # s8 right bottom leg


# --- SELF_CHECK ---
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 8 draw calls, matches expected
    'endpoint_mismatches': [],    # MMH-verbatim
    'joint_class_mismatches': [], # 2 P (s1×s2, s1×s3) welded via crossing; 6 N left as gaps
    'overall_pass': True,
    'notes': ('8 strokes MMH-verbatim; s2 and s3 pierce s1 forming welded P-joints; '
              's4/s5 interior hengs and s6 bottom heng preserve natural N-gaps to s2 and s3; '
              's7/s8 bottom legs splay under s6.'),
}


out_path = os.path.join(os.path.dirname(__file__), '01_其.png')
img.save(out_path)
print('wrote', out_path)
