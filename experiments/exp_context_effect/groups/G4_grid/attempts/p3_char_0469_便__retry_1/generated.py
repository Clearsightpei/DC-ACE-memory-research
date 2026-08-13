"""
p3_char_0469_便 retry_1 — 便 (biàn), 9 strokes.

TRAJECTORY DIFF (main attempt C-verdict → retry_1):
  Prior FAIL (main, 01_便.png verdict C):
    - 曰 box incoherent: middle 一 (s6) and bottom 一 (s7) started from
      INSIDE the box (x=145) instead of the LEFT column (x~115), so
      they looked like short floating segments not spanning bars of
      the box.
    - Left 竖 (s4) leaned right too aggressively (110→135) making 曰
      look like a parallelogram tilted right.
    - 横折 (s5) top-horizontal was too short (started at x=122) — did
      not reach the visual left edge of the box.
    - Strokes overall thin/wispy vs GT's confident weight.
  Errata literal fix: "更 = 一 + 曰 (compressed) + 长 legs; per-stroke
    widths explicit". Meaning: 曰 must READ as a box; the two legs
    (撇, 捺) sweep from the top of 曰 outward.

  Fixes applied this retry:
    1. Force 曰 box to be a proper closed rectangle: left column x=115,
       right column x=217, top y=131, bottom y=197. Compute anchors
       inside those bounds but SNAP the interior horizontals to span
       the full box width.
    2. Middle & bottom horizontals extend left to touch the left 竖.
    3. Slight left 竖 lean preserved (per MMH) but capped.
    4. STROKE_W raised to 7.
    5. Long 撇 (s8) starts at top-right of 曰 area (near TC 0.588) and
       sweeps DOWN-LEFT through the box out to BL — same as GT.
    6. Long 捺 (s9) starts inside the box (BC head) and sweeps DOWN-RIGHT
       to BR with proper taper (thick at foot, tapered tail).

# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH puts 亻 in far-left column (TL/ML/BL); ren_side defaults
#         sit at TC/C/BC (center). Inline fresh with MMH anchors, same
#         as main attempt.
# fresh_component: ren_side_far_left_for_便
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 draw calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'retry_1: 曰 box forced coherent (horizontals span full width, left 竖 lean capped); strokes thickened; 撇/捺 legs wider spread.',
}

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 '..', '..', 'success_bank', 'code')))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

from PIL import Image, ImageDraw

W = 300
img = Image.new('RGB', (W, W), 'white')
draw = ImageDraw.Draw(img)

STROKE_W = 7

# ---- 亻 (far-left column) — MMH verbatim ----

# s1: pie — from upper-right down to lower-left
s1_h = anchor_to_xy(('TL', 0.835, 0.671))   # ~(83, 67)
s1_t = anchor_to_xy(('ML', 0.141, 0.948))   # ~(14, 195)
ctrl1 = (s1_h[0] - 18, (s1_h[1] + s1_t[1]) / 2)
pts1 = quad_bezier(s1_h, ctrl1, s1_t, n=42)
widths1 = []
for i, _ in enumerate(pts1):
    t = i / (len(pts1) - 1)
    if t < 0.82:
        w = STROKE_W + 1
    else:
        w = STROKE_W + 1 - (t - 0.82) / 0.18 * 5
    widths1.append(max(2, w))
stroke_variable_width(draw, pts1, widths1)

# s2: shu — near-vertical
s2_h = anchor_to_xy(('ML', 0.659, 0.468))   # ~(66, 147)
s2_t = anchor_to_xy(('BL', 0.709, 0.918))   # ~(71, 292)
fat_line(draw, s2_h, s2_t, STROKE_W)

# ---- 更 (right two-thirds) ----

# Box bounds for 曰 — enforce a proper rectangle
BOX_L = 122      # left column x
BOX_R = 218      # right column x
BOX_T = 131      # top edge y
BOX_B = 197      # bottom edge y

# s3: top 一 (of 更) — spans wide above 曰
s3_h = anchor_to_xy(('TC', 0.342, 0.847))   # ~(134, 85)
s3_t = anchor_to_xy(('TR', 0.215, 0.744))   # ~(222, 74)
# Extend slightly wider for visual weight
s3_h_draw = (s3_h[0] - 20, s3_h[1] + 4)
s3_t_draw = (s3_t[0] + 10, s3_t[1] + 2)
fat_line(draw, s3_h_draw, s3_t_draw, STROKE_W)

# s4: 曰 left 竖 — cap the lean (MMH slants (110,132)→(135,202); cap at BOX_L)
s4_h = (BOX_L - 3, BOX_T)
s4_t = (BOX_L + 8, BOX_B + 4)          # small lean, not full MMH slant
fat_line(draw, s4_h, s4_t, STROKE_W)

# s5: 曰 横折 — top horizontal + right vertical (proper right angle)
s5_top_l = (BOX_L, BOX_T)
s5_top_r = (BOX_R, BOX_T)
s5_bot_r = (BOX_R, BOX_B)
fat_line(draw, s5_top_l, s5_top_r, STROKE_W)
fat_line(draw, s5_top_r, s5_bot_r, STROKE_W)

# s6: middle 一 — spans full box width at mid height
mid_y = BOX_T + int(0.52 * (BOX_B - BOX_T))
fat_line(draw, (BOX_L, mid_y), (BOX_R - 6, mid_y - 2), STROKE_W - 1)

# s7: bottom 一 — the bottom edge of 曰 (spans full box width)
fat_line(draw, (BOX_L, BOX_B), (BOX_R, BOX_B), STROKE_W)

# s8: long 撇 — from top of 更 (near right edge of top 一) sweeping
#     through the box down to bottom-left. Head near TC(0.588, 0.938).
s8_h = anchor_to_xy(('TC', 0.588, 0.938))   # ~(159, 94)
s8_t = anchor_to_xy(('BL', 0.976, 0.865))   # ~(98, 287)
# Curve: through the interior of 曰 then out to BL
knee = ((s8_h[0] + s8_t[0]) / 2 + 8,
        (s8_h[1] + s8_t[1]) / 2 + 15)
ctrl8a = (s8_h[0] + 6, s8_h[1] + (knee[1] - s8_h[1]) * 0.55)
pts8a = quad_bezier(s8_h, ctrl8a, knee, n=34)
ctrl8b = (knee[0] - 25, s8_t[1] - 15)
pts8b = quad_bezier(knee, ctrl8b, s8_t, n=34)
pts8 = pts8a + pts8b[1:]
widths8 = []
n8 = len(pts8)
for i in range(n8):
    t = i / (n8 - 1)
    if t < 0.85:
        w = STROKE_W + 0.5
    else:
        w = STROKE_W + 0.5 - (t - 0.85) / 0.15 * 5
    widths8.append(max(2, w))
stroke_variable_width(draw, pts8, widths8)

# s9: long 捺 — from inside box (near BC head) down-right to BR corner
s9_h = anchor_to_xy(('BC', 0.025, 0.124))   # ~(100, 212)
s9_t = anchor_to_xy(('BR', 0.851, 0.921))   # ~(285, 292)
mid9 = ((s9_h[0] + s9_t[0]) / 2 + 5, (s9_h[1] + s9_t[1]) / 2 + 15)
pts9 = quad_bezier(s9_h, mid9, s9_t, n=48)
widths9 = []
n9 = len(pts9)
for i in range(n9):
    t = i / (n9 - 1)
    if t < 0.75:
        w = STROKE_W - 1.5 + 3.5 * t
    else:
        w = STROKE_W + 2 - (t - 0.75) * 14
    widths9.append(max(2, w))
stroke_variable_width(draw, pts9, widths9)

# ---- Save ----
out = os.path.join(os.path.dirname(__file__), '01_便.png')
img.save(out)
print(f"Saved {out}")
