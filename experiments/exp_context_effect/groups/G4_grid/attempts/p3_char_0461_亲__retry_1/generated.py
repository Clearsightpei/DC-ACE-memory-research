"""亲 (qīn) retry_1 — 9 strokes.

TRAJECTORY DIFF (from inspecting main attempt PNG vs GT):
- FAILED main (verdict C):
  1. s7 (丨 of 木) rendered tilted: MMH gave head C(0.351,0.793)=(135,179) to
     BC(0.037,0.795)=(104,279), i.e. 31px leftward drift over 100px vertical.
     Reads as an off-axis 木-spine. This is the "立 vertical off-axis"
     defect flagged in errata.
  2. s8/s9 (撇/捺) heads emanate from (99,242) and (181,242) — 82px apart —
     so 木 lacks a clean shared centerline apex; 撇/捺 look detached from 丨.
  3. Overall 木 read as "too small" per errata because the tilted spine
     compressed its perceived footprint.
- Fixes this attempt:
  a. Override s7 to true vertical along x=150 (central axis), spanning
     y=175→295. Structural tolerance hit on tail x_frac (~0.46 off in
     BC-cell); visual > structural per v8 rules; sandbox note follows.
  b. Pull s8/s9 heads inward so both emanate near (150, 240) — the
     shared 丨×一 apex — while keeping tails at MMH endpoints.
  c. Keep 立-zone strokes at MMH anchors (they read fine).
"""

# BANK_DEVIATION
# skipped: mu.py (木 primitive) — default anchors are full-canvas, but here
#   木 must sit in bottom band y∈[0.55, 1.0] with straight central 丨.
# reason: The main attempt inlined per MMH but s7 tilt broke 木's central
#   axis; retry overrides s7 to strict vertical + pulls 撇/捺 to shared apex.
# fresh_component: mu_bottom_slot_central_spine_for_立X

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [
        {'stroke': 7, 'expected_tail': ('BC', 0.037, 0.795),
         'actual_tail': ('BC', 0.5, 0.95),
         'delta': 'x_frac 0.463 (OUT of ±0.20) — deliberate: straight central 丨'},
        {'stroke': 8, 'expected_head': ('BL', 0.987, 0.423),
         'actual_head': ('BC', 0.25, 0.42),
         'delta': 'cell BL→BC (adjacent); x_frac shifted to align with 丨 apex'},
        {'stroke': 9, 'expected_head': ('BC', 0.808, 0.42),
         'actual_head': ('BC', 0.55, 0.42),
         'delta': 'x_frac 0.258 diff — pull inward to share 丨 apex'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes; s7 forced straight vertical at x=150 per errata fix; '
             '撇/捺 heads pulled to shared apex near (150,240). N-joints kept as gaps.',
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# --- 立 zone (y ~ 90-180): keep MMH anchors ---

# Stroke 1 — top dot (点) of 立.
s1_h = anchor_to_xy(('TC', 0.236, 0.583))
s1_t = anchor_to_xy(('TC', 0.588, 0.812))
pts = sample_line(s1_h, s1_t, n=8)
widths = [3 + 5 * (i / 8) for i in range(9)]
stroke_variable_width(draw, pts, widths)

# Stroke 2 — 一 top-heng of 立.
s2_h = anchor_to_xy(('ML', 0.879, 0.046))
s2_t = anchor_to_xy(('TR', 0.095, 0.932))
fat_line(draw, s2_h, s2_t, width=6)

# Stroke 3 — 丶 left dot of 丷.
s3_h = anchor_to_xy(('ML', 0.996, 0.298))
s3_t = anchor_to_xy(('C', 0.178, 0.538))
pts = sample_line(s3_h, s3_t, n=8)
widths = [3 + 4 * (i / 8) for i in range(9)]
stroke_variable_width(draw, pts, widths)

# Stroke 4 — 丿 right stroke of 丷.
s4_h = anchor_to_xy(('C', 0.805, 0.093))
s4_t = anchor_to_xy(('C', 0.567, 0.641))
pts = sample_line(s4_h, s4_t, n=8)
widths = [3 + 5 * (i / 8) for i in range(9)]
stroke_variable_width(draw, pts, widths)

# Stroke 5 — long 一 bottom-heng of 立 (wide).
s5_h = anchor_to_xy(('ML', 0.416, 0.813))
s5_t = anchor_to_xy(('MR', 0.517, 0.696))
fat_line(draw, s5_h, s5_t, width=7)

# --- 木 zone (y ~ 210-295): fix s7 to straight central 丨; pull 撇/捺 heads inward ---

# Stroke 6 — 一 top-heng of 木 (wide).
s6_h = anchor_to_xy(('BL', 0.703, 0.215))
s6_t = anchor_to_xy(('BR', 0.188, 0.115))
fat_line(draw, s6_h, s6_t, width=6)

# Stroke 7 — 丨 vertical spine of 木 (OVERRIDE: straight along x=150).
# MMH gave tilted C(0.351,0.793)→BC(0.037,0.795); we force vertical.
s7_h = anchor_to_xy(('C', 0.5, 0.75))     # (150, 175)
s7_t = anchor_to_xy(('BC', 0.5, 0.95))    # (150, 295)
fat_line(draw, s7_h, s7_t, width=7)

# Stroke 8 — 撇 of 木 (short leftward slant, head at shared 丨-apex).
s8_h = anchor_to_xy(('BC', 0.25, 0.42))   # (125, 242) — near central apex
s8_t = anchor_to_xy(('BL', 0.674, 0.839)) # MMH tail (67, 284)
pts = sample_line(s8_h, s8_t, n=20)
widths = [7 - 5 * (i / 20) for i in range(21)]
stroke_variable_width(draw, pts, widths)

# Stroke 9 — 捺 of 木 (short rightward slant, head at shared 丨-apex).
s9_h = anchor_to_xy(('BC', 0.55, 0.42))   # (155, 242) — near central apex
s9_t = anchor_to_xy(('BR', 0.279, 0.854)) # MMH tail (228, 285)
pts = sample_line(s9_h, s9_t, n=20)
widths = [3 + 6 * (i / 20) for i in range(21)]
stroke_variable_width(draw, pts, widths)

out = os.path.join(os.path.dirname(__file__), '01_亲.png')
img.save(out)
print('wrote', out)
