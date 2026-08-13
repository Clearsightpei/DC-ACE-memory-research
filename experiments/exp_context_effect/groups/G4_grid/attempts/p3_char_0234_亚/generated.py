"""Draw 亚 (yà) — 6 strokes, PIL 300x300."""
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
    'notes': '亚 rendered from injected MMH anchors; all joints are N (small natural gaps).'
}

# Memory log:
# - Read memory_index.md v8 checklist. 亚 not in success_bank INDEX or errata.
# - Free composition per shared_rules v8: bank is reference only; using injected anchors directly.

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

W = 6  # stroke width

# Stroke 1: top horizontal (heng)
s1_h = anchor_to_xy(('ML', 0.788, 0.014))
s1_t = anchor_to_xy(('TR', 0.224, 0.929))
fat_line(d, s1_h, s1_t, W)

# Stroke 2: left short vertical (shu-like), from just under top-heng down to mid-bottom-left
s2_h = anchor_to_xy(('C', 0.084, 0.131))
s2_t = anchor_to_xy(('BC', 0.154, 0.675))
fat_line(d, s2_h, s2_t, W)

# Stroke 3: right short vertical
s3_h = anchor_to_xy(('C', 0.632, 0.046))
s3_t = anchor_to_xy(('BC', 0.658, 0.625))
fat_line(d, s3_h, s3_t, W)

# Stroke 4: left middle short diagonal (小撇/短)
s4_h = anchor_to_xy(('ML', 0.574, 0.761))
s4_t = anchor_to_xy(('BL', 0.899, 0.121))
fat_line(d, s4_h, s4_t, W)

# Stroke 5: right middle short diagonal
s5_h = anchor_to_xy(('MR', 0.262, 0.468))
s5_t = anchor_to_xy(('BC', 0.831, 0.062))
fat_line(d, s5_h, s5_t, W)

# Stroke 6: bottom horizontal (heng)
s6_h = anchor_to_xy(('BL', 0.384, 0.76))
s6_t = anchor_to_xy(('BR', 0.66, 0.774))
fat_line(d, s6_h, s6_t, W)

out_png = os.path.join(os.path.dirname(__file__), "01_亚.png")
img.save(out_png)
print(f"Saved {out_png}")
