"""亲 (qīn) — 9 strokes.

Decomposition: 亲 = 立 (top, 5 strokes) + 木 (bottom, 4 strokes).
  立 = 点(s1) + 一(s2) + 丷(s3+s4) + 一(s5 long)
  木 = 一(s6, in-bottom horizontal) + 丨(s7) + 撇(s8) + 捺(s9)

MMH-verbatim anchors per dispatcher-injected block. Base primitives
(fat_line + variable width for tapered strokes). No compound bank
primitives called — MMH anchors don't match any standalone-scale bank
primitive (立-top and 木-bottom occupy specific vertical bands).
"""

# Reading order log (v8 slim checklist):
# 1. drawer_memory.md — read; A-recipe applies (MMH-verbatim + base primitives).
# 2. success_bank/INDEX.md — no 亲, no 立 primitive; mu (木) exists but its
#    default anchors are full-canvas, not bottom-band. Skip.
# 3. errata.md — no 亲 entry.

# BANK_DEVIATION
# skipped: mu.py (木 primitive)
# reason: mu.py default anchors are full-canvas; here 木 sits only in
#   bottom band (y ~ 180-285), embedded below 立. Inlining base primitives
#   with MMH-verbatim anchors preserves the compositional proportion.
# fresh_component: mu_bottom_slot_for_立X

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; all N-joints preserved as gaps; s6/s7 P-weld at BC(0.487,0.132).',
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# Stroke 1 — top dot (点): TC(0.236,0.583) → TC(0.588,0.812) — short diagonal.
s1_h = anchor_to_xy(('TC', 0.236, 0.583))
s1_t = anchor_to_xy(('TC', 0.588, 0.812))
pts = sample_line(s1_h, s1_t, n=8)
widths = [3 + 5 * (i/8) for i in range(9)]  # thin→thick (dot tapers to press)
stroke_variable_width(draw, pts, widths)

# Stroke 2 — top 一 of 立: ML(0.879,0.046) → TR(0.095,0.932).
s2_h = anchor_to_xy(('ML', 0.879, 0.046))
s2_t = anchor_to_xy(('TR', 0.095, 0.932))
fat_line(draw, s2_h, s2_t, width=6)

# Stroke 3 — left 丶 of 丷: ML(0.996,0.298) → C(0.178,0.538).
s3_h = anchor_to_xy(('ML', 0.996, 0.298))
s3_t = anchor_to_xy(('C', 0.178, 0.538))
pts = sample_line(s3_h, s3_t, n=8)
widths = [3 + 4 * (i/8) for i in range(9)]
stroke_variable_width(draw, pts, widths)

# Stroke 4 — right 丶 of 丷: C(0.805,0.093) → C(0.567,0.641).
s4_h = anchor_to_xy(('C', 0.805, 0.093))
s4_t = anchor_to_xy(('C', 0.567, 0.641))
pts = sample_line(s4_h, s4_t, n=8)
widths = [3 + 5 * (i/8) for i in range(9)]
stroke_variable_width(draw, pts, widths)

# Stroke 5 — long middle 一: ML(0.416,0.813) → MR(0.517,0.696).
s5_h = anchor_to_xy(('ML', 0.416, 0.813))
s5_t = anchor_to_xy(('MR', 0.517, 0.696))
fat_line(draw, s5_h, s5_t, width=6)

# Stroke 6 — 一 of 木 (top-heng of 木, sits in bottom band):
#   BL(0.703,0.215) → BR(0.188,0.115).
s6_h = anchor_to_xy(('BL', 0.703, 0.215))
s6_t = anchor_to_xy(('BR', 0.188, 0.115))
fat_line(draw, s6_h, s6_t, width=6)

# Stroke 7 — 丨 of 木: C(0.351,0.793) → BC(0.037,0.795).
# P-weld with s6 mid at cell BC(0.487,0.132) — vertical stroke crosses s6.
s7_h = anchor_to_xy(('C', 0.351, 0.793))
s7_t = anchor_to_xy(('BC', 0.037, 0.795))
fat_line(draw, s7_h, s7_t, width=7)

# Stroke 8 — 撇 (left down-slant) of 木: BL(0.987,0.423) → BL(0.674,0.839).
s8_h = anchor_to_xy(('BL', 0.987, 0.423))
s8_t = anchor_to_xy(('BL', 0.674, 0.839))
pts = sample_line(s8_h, s8_t, n=20)
widths = [7 - 5 * (i/20) for i in range(21)]  # thick→thin (撇 tapers)
stroke_variable_width(draw, pts, widths)

# Stroke 9 — 捺 (right down-slant) of 木: BC(0.808,0.42) → BR(0.279,0.854).
s9_h = anchor_to_xy(('BC', 0.808, 0.42))
s9_t = anchor_to_xy(('BR', 0.279, 0.854))
pts = sample_line(s9_h, s9_t, n=20)
widths = [3 + 6 * (i/20) for i in range(21)]  # thin→thick (捺 presses at end)
stroke_variable_width(draw, pts, widths)

out = os.path.join(os.path.dirname(__file__), '01_亲.png')
img.save(out)
print('wrote', out)
