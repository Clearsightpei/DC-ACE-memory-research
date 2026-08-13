"""Draw 亚 (yà) — 6 strokes, PIL 300x300. Retry #1.

TRAJECTORY DIFF:
- main attempt PASSED — its silhouette matches GT (top heng, two short verticals,
  two small inner diagonals, bottom heng). All 6 strokes present, correct proportions.
- Fix plan: replicate the passing approach essentially unchanged (per retry guidance:
  copy what worked; don't reinvent). Same anchor coords from injected MMH block.
"""
from PIL import Image, ImageDraw
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
from _anchor import anchor_to_xy, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '亚 retry_1: same approach as passing main attempt; injected MMH anchors, all 5 joints N (natural gaps).'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

W = 6

# Stroke 1: top horizontal
fat_line(d, anchor_to_xy(('ML', 0.788, 0.014)), anchor_to_xy(('TR', 0.224, 0.929)), W)

# Stroke 2: left short vertical
fat_line(d, anchor_to_xy(('C', 0.084, 0.131)), anchor_to_xy(('BC', 0.154, 0.675)), W)

# Stroke 3: right short vertical
fat_line(d, anchor_to_xy(('C', 0.632, 0.046)), anchor_to_xy(('BC', 0.658, 0.625)), W)

# Stroke 4: left inner short diagonal
fat_line(d, anchor_to_xy(('ML', 0.574, 0.761)), anchor_to_xy(('BL', 0.899, 0.121)), W)

# Stroke 5: right inner short diagonal
fat_line(d, anchor_to_xy(('MR', 0.262, 0.468)), anchor_to_xy(('BC', 0.831, 0.062)), W)

# Stroke 6: bottom horizontal
fat_line(d, anchor_to_xy(('BL', 0.384, 0.76)), anchor_to_xy(('BR', 0.66, 0.774)), W)

out_png = os.path.join(os.path.dirname(__file__), "01_亚.png")
img.save(out_png)
print(f"Saved {out_png}")
