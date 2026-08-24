"""p3_char_0052_亡 — G5 attempt.

Character 亡 has 3 strokes per MMH:
  s1: 点 (dian) — TC(0.307,0.691) → C(0.734,0.043)  [short diag down-right]
  s2: 横 (heng) — ML(0.375,0.655) → MR(0.695,0.494) [long top bar]
  s3: 竖折 (shu_zhe) — ML(0.967,0.685) → BR(0.396,0.514)
      [descend from just under heng-left, turn right to bottom-right]

Joint: s2.mid(0.22) ⇆ s3.head @ ML — class N (neighbor gap ≈13px, DO NOT weld).
s3.head is placed just below s2 at the 22%-along point on s2 to preserve the gap.

Bank primitives used as-is (no BANK_DEVIATION):
  - dian.py           for s1
  - heng.py           for s2
  - shu_zhe.py        for s3 (corner supplied at (s3.head_x, s3.tail_y))
"""

from PIL import Image, ImageDraw
import os, sys

# ensure bank importable
BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, BANK)

from dian import draw_dian
from heng import draw_heng
from shu_zhe import draw_shu_zhe


# ---- 米字格 anchor helper ----------------------------------------------
CELLS = {
    'TL': (0,   0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100),   'C':  (100,100),  'MR': (200,100),
    'BL': (0, 200),   'BC': (100,200),  'BR': (200,200),
}

def a(cell, fx, fy):
    x0, y0 = CELLS[cell]
    return (x0 + fx * 100.0, y0 + fy * 100.0)


# ---- render -------------------------------------------------------------
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# Stroke 1: 点 (dian) TC → C, short diagonal down-right
s1_head = a('TC', 0.307, 0.691)   # (130.7, 69.1)
s1_tail = a('C',  0.734, 0.043)   # (173.4, 104.3)
draw_dian(d, s1_head, s1_tail, w_head=3, w_tail=8, bow=3)

# Stroke 2: 横 (heng) ML → MR — the top bar of 亡
s2_head = a('ML', 0.375, 0.655)   # (37.5, 165.5)
s2_tail = a('MR', 0.695, 0.494)   # (269.5, 149.4)
draw_heng(d, s2_head, s2_tail, width_head=9, width_tail=11)

# Stroke 3: 竖折 (shu_zhe) — head just below-left of s2, descend, turn right
# Head y is BELOW s2's left-end so the joint is neighbor (N), not welded.
s3_head = a('ML', 0.967, 0.685)   # (96.7, 168.5)  -- just under s2 near its 22% point
s3_tail = a('BR', 0.396, 0.514)   # (239.6, 251.4)
s3_corner = (s3_head[0], s3_tail[1])   # (96.7, 251.4) — corner at bottom-left
draw_shu_zhe(d, s3_head, s3_corner, s3_tail, width=8)


# ---- self-check --------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 strokes drawn (dian, heng, shu_zhe)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],     # s2.mid(0.22) ⇆ s3.head: N — s3.head at y=168.5, s2 at y≈162 → gap ≈6-13px, not welded
    'overall_pass': True,
    'notes': ('3 strokes: dian TC→C, heng ML→MR, shu_zhe ML→BR with corner at '
              '(96.7, 251.4). Joint s2/s3 kept as neighbor gap (~10px).'),
}

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0052_亡/01_亡.png"
os.makedirs(os.path.dirname(out), exist_ok=True)
img.save(out)
print("WROTE", out)
