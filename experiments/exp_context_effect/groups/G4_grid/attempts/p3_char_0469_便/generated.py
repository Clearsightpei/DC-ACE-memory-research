"""
p3_char_0469_便 — 便 (biàn), 9 strokes.

Decomposition: 便 = 亻 (left, 2 strokes) + 更 (right, 7 strokes).
更 = 一 (top) + 曰 (box: 竖 + 横折 + 中横 + 底横) + 撇 (long) + 捺 (long).

MMH places 亻 in the far-left column (TL/ML/BL cells). Following B11 A-recipe:
inline via base primitives with MMH-verbatim anchors rather than importing
ren_side (default TC/C/BC would sit in center).
"""

# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻 in far-left column (TL/ML/BL); ren_side defaults sit at TC/C/BC (center). Partial-override anti-pattern (伊 B8 FAIL); inline 亻 with MMH anchors.
# fresh_component: ren_side_far_left_for_便

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 draw calls, 9 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # P welds inside 曰 box; N gaps preserved
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; 亻 far-left; 更 uses successful retry_2 pattern (撇 crosses through box; 捺 sweeps to BR).',
}

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 '..', '..', 'success_bank', 'code')))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

from PIL import Image, ImageDraw

W = 300
img = Image.new('RGB', (W, W), 'white')
draw = ImageDraw.Draw(img)

STROKE_W = 6

# ---- MMH-verbatim anchors (from dispatcher brief) ----
# s1: 亻 pie
s1_h = anchor_to_xy(('TL', 0.835, 0.671))
s1_t = anchor_to_xy(('ML', 0.141, 0.948))
# s2: 亻 shu
s2_h = anchor_to_xy(('ML', 0.659, 0.468))
s2_t = anchor_to_xy(('BL', 0.709, 0.918))
# s3: 更 top 一
s3_h = anchor_to_xy(('TC', 0.342, 0.847))
s3_t = anchor_to_xy(('TR', 0.215, 0.744))
# s4: 曰 left 竖 (slight lean)
s4_h = anchor_to_xy(('C', 0.096, 0.321))
s4_t = anchor_to_xy(('BC', 0.345, 0.019))
# s5: 曰 横折 top + right
s5_h = anchor_to_xy(('C', 0.222, 0.315))
s5_t = anchor_to_xy(('MR', 0.171, 0.925))
# s6: 曰 middle 横
s6_h = anchor_to_xy(('C', 0.453, 0.644))
s6_t = anchor_to_xy(('MR', 0.06, 0.562))
# s7: 曰 bottom 横
s7_h = anchor_to_xy(('C', 0.406, 0.98))
s7_t = anchor_to_xy(('MR', 0.089, 0.901))
# s8: long 撇 (through box)
s8_h = anchor_to_xy(('TC', 0.588, 0.938))
s8_t = anchor_to_xy(('BL', 0.976, 0.865))
# s9: long 捺 (from inside box to BR)
s9_h = anchor_to_xy(('BC', 0.025, 0.124))
s9_t = anchor_to_xy(('BR', 0.851, 0.921))

# ---- Draw 亻 (far-left column) ----

# s1: pie — curve from upper-right down to lower-left
n1 = 40
ctrl1 = (s1_h[0] - 20, (s1_h[1] + s1_t[1]) / 2)  # bulge slightly left
pts1 = quad_bezier(s1_h, ctrl1, s1_t, n=n1)
widths1 = []
for i in range(len(pts1)):
    t = i / (len(pts1) - 1)
    if t < 0.85:
        w = STROKE_W + 1
    else:
        w = STROKE_W + 1 - (t - 0.85) / 0.15 * 5
    widths1.append(max(2, w))
stroke_variable_width(draw, pts1, widths1)

# s2: shu — nearly straight vertical
fat_line(draw, s2_h, s2_t, STROKE_W)

# ---- Draw 更 ----

# s3: top 一
fat_line(draw, s3_h, s3_t, STROKE_W)

# s4: 曰 left 竖 (slight lean per MMH)
fat_line(draw, s4_h, s4_t, STROKE_W)

# s5: 曰 横折 — draw as two segments meeting at corner
s5_corner = (s5_t[0], s5_h[1])
fat_line(draw, s5_h, s5_corner, STROKE_W)
fat_line(draw, s5_corner, s5_t, STROKE_W)

# s6: middle horizontal
fat_line(draw, s6_h, s6_t, STROKE_W)

# s7: bottom horizontal
fat_line(draw, s7_h, s7_t, STROKE_W)

# s8: long 撇 — start high near TC, sweep through box down to BL
# Build as two-segment bezier: near-vertical through box, then curve out-left
s8_knee = ((s8_h[0] + s8_t[0]) / 2 + 5, (s8_h[1] + s8_t[1]) / 2 + 20)
ctrl8a = (s8_h[0] + 8, s8_h[1] + (s8_knee[1] - s8_h[1]) * 0.5)
pts8a = quad_bezier(s8_h, ctrl8a, s8_knee, n=32)
ctrl8b = (s8_knee[0] - 25, s8_t[1] - 20)
pts8b = quad_bezier(s8_knee, ctrl8b, s8_t, n=32)
pts8 = pts8a + pts8b[1:]
widths8 = []
n8 = len(pts8)
for i in range(n8):
    t = i / (n8 - 1)
    if t < 0.85:
        w = STROKE_W + 0.5
    else:
        w = STROKE_W + 0.5 - (t - 0.85) / 0.15 * 4
    widths8.append(max(2, w))
stroke_variable_width(draw, pts8, widths8)

# s9: long 捺 — from inside box (BC upper) to BR corner
mid9 = ((s9_h[0] + s9_t[0]) / 2, (s9_h[1] + s9_t[1]) / 2 + 12)
pts9 = quad_bezier(s9_h, mid9, s9_t, n=48)
widths9 = []
n9 = len(pts9)
for i in range(n9):
    t = i / (n9 - 1)
    if t < 0.75:
        w = STROKE_W - 1 + 3 * t
    else:
        w = STROKE_W + 1.5 - (t - 0.75) * 12
    widths9.append(max(3, w))
stroke_variable_width(draw, pts9, widths9)

# ---- Save ----
out = os.path.join(os.path.dirname(__file__), '01_便.png')
img.save(out)
print(f"Saved {out}")
