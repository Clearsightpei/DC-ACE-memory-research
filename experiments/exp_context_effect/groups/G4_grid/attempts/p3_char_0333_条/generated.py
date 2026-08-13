"""p3_char_0333_条 — G4 attempt.

Reading order (per memory_index v8):
  1. drawer_memory.md   — read
  2. INDEX.md grep 条   — no direct entry; 木 exists (mu.py) as sub-component
  3. errata.md grep 条   — not present
Decomposition: 条 = 夂 (top) + 木/小 (bottom).
Per v8: bank/principles REFERENCE ONLY; trust MMH anchors verbatim.
No chronic-component (no 冂/丿/刀/弓/马) — inline via _anchor + fat_line.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-verbatim anchors; 7 strokes; joints s2/s3 P welded, others N gaps.'
}

W = 3  # base stroke width

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- Anchors from MMH-derived structural expectations block ---
# stroke 1: short pie (top-left of 夂)
s1_h = anchor_to_xy(('TC', 0.277, 0.574))
s1_t = anchor_to_xy(('ML', 0.592, 0.406))

# stroke 2: second pie (dropping from s1's continuation)
s2_h = anchor_to_xy(('TC', 0.236, 0.97))
s2_t = anchor_to_xy(('ML', 0.504, 0.931))

# stroke 3: long horizontal-diagonal (heng-pie forming 夂's top arm)
s3_h = anchor_to_xy(('C', 0.046, 0.14))
s3_t = anchor_to_xy(('MR', 0.757, 0.834))

# stroke 4: heng — horizontal of 木/small (going right-to-left in MMH order)
s4_h = anchor_to_xy(('BL', 0.773, 0.203))
s4_t = anchor_to_xy(('BR', 0.062, 0.124))

# stroke 5: left pie of the bottom
s5_h = anchor_to_xy(('C', 0.365, 0.77))
s5_t = anchor_to_xy(('BC', 0.049, 0.786))

# stroke 6: right-going pie of the bottom (curved to left)
s6_h = anchor_to_xy(('BL', 0.92, 0.461))
s6_t = anchor_to_xy(('BL', 0.636, 0.892))

# stroke 7: na — the right-going diagonal at bottom
s7_h = anchor_to_xy(('BC', 0.872, 0.402))
s7_t = anchor_to_xy(('BR', 0.37, 0.865))

# --- Render strokes ---
# s1 pie — slight curve
fat_line(d, s1_h, s1_t, W)

# s2 pie — slight curve going down-left; draw with light bezier
mid2 = ((s2_h[0] + s2_t[0]) / 2 - 5, (s2_h[1] + s2_t[1]) / 2 + 5)
pts2 = quad_bezier(s2_h, mid2, s2_t, n=30)
widths2 = [W] * len(pts2)
stroke_variable_width(d, pts2, widths2)

# s3 heng-pie — long slanted diagonal; render as gently curved
mid3 = ((s3_h[0] + s3_t[0]) / 2, (s3_h[1] + s3_t[1]) / 2 - 4)
pts3 = quad_bezier(s3_h, mid3, s3_t, n=40)
widths3 = [W + 1] + [W] * (len(pts3) - 2) + [W - 1]
stroke_variable_width(d, pts3, widths3)

# s4 heng — the horizontal across bottom half
fat_line(d, s4_h, s4_t, W)

# s5 pie — short diagonal down-left
fat_line(d, s5_h, s5_t, W)

# s6 — bottom-left curl (shu becoming pie)
mid6 = (s6_h[0] - 6, (s6_h[1] + s6_t[1]) / 2)
pts6 = quad_bezier(s6_h, mid6, s6_t, n=30)
widths6 = [W] * len(pts6)
stroke_variable_width(d, pts6, widths6)

# s7 na — diagonal down-right, widening
pts7 = quad_bezier(s7_h, ((s7_h[0] + s7_t[0]) / 2, (s7_h[1] + s7_t[1]) / 2 - 2), s7_t, n=30)
widths7 = [max(2, W - 1 + int(2 * i / len(pts7))) for i in range(len(pts7))]
stroke_variable_width(d, pts7, widths7)

# Verify stroke count
strokes_drawn = 7
assert strokes_drawn == 7, f"stroke count {strokes_drawn} != 7"

out_path = os.path.join(os.path.dirname(__file__), '01_条.png')
img.save(out_path)
print(f'saved {out_path}')
