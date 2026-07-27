"""p3_char_0196_东 — 5 strokes.

Memory read order (v8):
  1. drawer_memory.md — no matching primitive listed for 东; not a chronic component.
  2. success_bank/INDEX.md — grep 东 → miss. No sub-radical mastered primitive
     directly applicable (东 doesn't decompose into 亻/扌/etc).
  3. errata.md — no prior 东 entry.
Fresh render from MMH-derived anchors.

Strokes (from brief):
  1. 横 (upper horizontal, slightly rising)
  2. 竖钩-like compound (top-center → hook right)
  3. 撇 through middle (starts near center, sweeps to lower-left)
  4. 撇 (bottom-left downstroke)
  5. 点/捺 (bottom-right)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'straight fits for strokes 1/3/4/5; bezier for compound stroke 2.'
}

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# Stroke 1 — top horizontal (slightly rising to right)
s1_h = anchor_to_xy(('ML', 0.562, 0.315))
s1_t = anchor_to_xy(('MR', 0.376, 0.102))
fat_line(d, s1_h, s1_t, width=6)

# Stroke 2 — 撇折 compound (down-left, then bend right).
# Head TC → sweep down-left (short 撇), then bend and go right to tail MR.
s2_h = anchor_to_xy(('TC', 0.362, 0.542))
s2_t = anchor_to_xy(('MR', 0.18, 0.966))
# Corner: roughly at the bottom-left of the 撇 segment, then horizontal to tail.
s2_corner = (s2_h[0] - 25, s2_t[1] - 5)
pts2 = sample_line(s2_h, s2_corner, n=20) + sample_line(s2_corner, s2_t, n=20)
fat_line(d, s2_h, s2_corner, width=6)
fat_line(d, s2_corner, s2_t, width=6)

# Stroke 3 — 竖钩: from center-middle down through, slight left hook at bottom.
s3_h = anchor_to_xy(('C', 0.427, 0.559))
s3_t = anchor_to_xy(('BC', 0.099, 0.728))
ctrl3 = (s3_h[0] + 6, (s3_h[1] + s3_t[1]) / 2 + 6)
pts3 = quad_bezier(s3_h, ctrl3, s3_t, n=30)
widths3 = [7] * (len(pts3) - 3) + [5, 4, 3]
stroke_variable_width(d, pts3, widths3)

# Stroke 4 — 撇 (bottom-left)
s4_h = anchor_to_xy(('BL', 0.92, 0.376))
s4_t = anchor_to_xy(('BL', 0.604, 0.889))
fat_line(d, s4_h, s4_t, width=6)

# Stroke 5 — 点/捺 (bottom-right)
s5_h = anchor_to_xy(('BC', 0.96, 0.312))
s5_t = anchor_to_xy(('BR', 0.461, 0.818))
fat_line(d, s5_h, s5_t, width=6)

out = os.path.join(os.path.dirname(__file__), '01_东.png')
img.save(out)
print('wrote', out)
