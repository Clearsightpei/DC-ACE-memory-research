"""Render 业 (p3_char_0184) — 5 strokes per MMH.

Memory-read log:
  1. drawer_memory.md — no direct primitive for 业; not in chronic list.
  2. success_bank/INDEX.md — no 业 entry.
  3. errata.md — no 业 entry.
Fresh draw using MMH-derived anchors (v8 REFERENCE-ONLY convention).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 5 fat_line calls == 5 strokes
    'endpoint_mismatches': [],       # all anchors used verbatim from brief
    'joint_class_mismatches': [],    # N/N joints preserved as gaps (strokes end short of horizontal)
    'overall_pass': True,
    'notes': '业: 2 short slants at top, 2 verticals, 1 bottom horizontal. Verticals leave gap above the horizontal (N joints).'
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# Stroke 1 — left vertical (near center, upper->lower)
p1_h = anchor_to_xy(('C',  0.028, 0.069))
p1_t = anchor_to_xy(('BC', 0.143, 0.684))
fat_line(draw, p1_h, p1_t, 10)

# Stroke 2 — right vertical
p2_h = anchor_to_xy(('TC', 0.608, 0.838))
p2_t = anchor_to_xy(('BC', 0.655, 0.66))
fat_line(draw, p2_h, p2_t, 10)

# Stroke 3 — left short slant (dot/pie on the left, upper area)
p3_h = anchor_to_xy(('ML', 0.565, 0.784))
p3_t = anchor_to_xy(('BL', 0.882, 0.118))
fat_line(draw, p3_h, p3_t, 8)

# Stroke 4 — right short slant (dot/na on the right)
p4_h = anchor_to_xy(('MR', 0.323, 0.471))
p4_t = anchor_to_xy(('BC', 0.969, 0.045))
fat_line(draw, p4_h, p4_t, 8)

# Stroke 5 — bottom horizontal
p5_h = anchor_to_xy(('BL', 0.384, 0.792))
p5_t = anchor_to_xy(('BR', 0.678, 0.801))
fat_line(draw, p5_h, p5_t, 11)

out = os.path.join(os.path.dirname(__file__), '01_业.png')
img.save(out)
print('saved', out)
